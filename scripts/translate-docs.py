"""Generate the Chinese VitePress pages from a Phaser Markdown snapshot."""

import argparse
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import re
import sqlite3
from urllib.parse import unquote, urlsplit, urlunsplit

import ctranslate2
import sentencepiece
from markdown_it import MarkdownIt
from opencc import OpenCC


LABELS = {
    "Author Credits": "作者署名",
    "Content on this page includes work by:": "本页包含以下作者贡献的内容。",
    "Constructor": "构造函数", "Parameters": "参数", "Returns": "返回值",
    "Description": "说明", "Default": "默认值", "Examples": "示例",
    "Example": "示例", "Since": "引入版本", "Scope": "作用域", "Type": "类型",
    "Source": "源码", "See also": "另请参阅", "Extends": "继承",
    "Inherited from": "继承自", "Inherited Members": "继承的成员",
    "Inherited Methods": "继承的方法", "Public Members": "公开成员",
    "Public Methods": "公开方法", "Protected Members": "受保护的成员",
    "Protected Methods": "受保护的方法", "Private Members": "私有成员",
    "Private Methods": "私有方法", "Static Members": "静态成员",
    "Static Methods": "静态方法", "Static functions": "静态函数", "Members": "成员", "Methods": "方法",
    "Classes": "类", "Namespaces": "命名空间", "Events": "事件",
    "Functions": "函数", "Constants": "常量", "Typedefs": "类型定义",
    "Game Objects": "游戏对象", "Physics": "物理", "Properties": "属性",
    "name": "名称", "type": "类型", "optional": "可选", "description": "说明",
    "Yes": "是", "No": "否", "What is Phaser?": "什么是 Phaser？",
    "Installing": "安装 Phaser", "Working with Phaser": "配置开发环境",
    "Project Templates": "项目模板", "Making your first Phaser game": "制作第一个 Phaser 游戏",
    "Create Phaser Game App": "创建 Phaser 游戏项目",
    "Installing Phaser from NPM": "通过 npm 安装 Phaser",
    "Cloning Phaser from GitHub": "从 GitHub 克隆 Phaser",
    "Using Phaser from a CDN": "通过 CDN 使用 Phaser",
    "Phaser Examples": "Phaser 示例", "Online Phaser Examples": "在线 Phaser 示例",
    "Arcade Physics": "Arcade 物理", "Matter Physics": "Matter 物理",
}
TERMS = {
    "Game Object": "游戏对象", "Game Objects": "游戏对象",
    "Display List": "显示列表", "Texture Frame": "纹理帧",
    "Pointer": "指针", "Scene": "场景", "Camera": "摄像机", "Tween": "补间动画",
    "Render Node": "渲染节点", "Shader Program": "着色器程序",
    "Sprite": "精灵", "Tileset": "图块集", "Tilemap": "瓦片地图",
}
GUIDE_TITLES = {
    'making-your-first-phaser-game': '制作第一个 Phaser 游戏',
    'actions': '动作（Actions）', 'fx': '视觉特效（FX）',
    'factories': '游戏对象工厂', 'blitter': '位块传送器（Blitter）',
    'container': '容器', 'dom-element': 'DOM 元素', 'group': '组（Group）',
    'light': '光源', 'mesh': '网格（Mesh）', 'nine-slice': '九宫格（NineSlice）',
    'particles': '粒子', 'plane': '平面（Plane）', 'render-texture': '渲染纹理',
    'rope': '绳索', 'shader': '着色器', 'tile-sprite': '平铺精灵',
    'input': '输入', 'loader': '资源加载器', 'cache': '缓存',
    'cross-scene-communication': '场景间通信', 'tweens': '补间动画',
    'utils': '实用工具', 'masks': '遮罩',
}
# Keep Markdown syntax, URLs and identifiers intact during translation.
INLINE = re.compile(
    r"`+[^`\n]+`+|!?\[[^\[\]\n]*\]\([^\n]*?\)|"
    r"\[(?:\s*[-+]?\d+(?:\.\d+)?\s*,)+\s*[-+]?\d+(?:\.\d+)?\s*\]|"
    r"\\?<[/!][^<>\n]*>|\\?<\w+(?:\s+[^<>\n]*)?\s*/?>|"
    r"https?://[^\s<>]+|&[a-zA-Z#][a-zA-Z0-9#]*;|"
    r"\bPhaser(?:\.[A-Za-z_$][\w$]*)*\b|\bthis(?:\.[A-Za-z_$][\w$]*)+\b|"
    r"\b(?:npm|pnpm|WebGL|JavaScript|TypeScript)\b|"
    r"\b[a-z_$]+[A-Z][A-Za-z0-9_$]*\b",
)
LINK = re.compile(r"(!?\[[^\[\]\n]*\]\()([^\s)]+)")
HEADING = re.compile(r"^(#{1,6}) +(.+?)\s*$")
LIST = re.compile(r"^([ \t]*(?:(?:>|[-*+]|\d+[.)]) +)*(?:\[[ xX]\] +)?)(.*)$")
LEADING_BOLD = re.compile(r"^\*\*([^*]+?)\*\*(\s*:?\s*)(.*)$")
TABLE_RULE = re.compile(r"^\s*:?-{2,}:?\s*$")
LEGACY_API_LINKS = {
    "Phaser.Input.Events": "api/namespace/input-events",
    "Phaser.Input.InputPlugin": "api/class/input-inputplugin",
    "Phaser.Scenes.Events": "api/namespace/scenes-events",
}
ASCII_WORD = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)*")
PLACEHOLDER = re.compile(r"Z\s*Z\s*(\d+)\s*Z\s*Z", re.I)
SKIP_PROMO = re.compile(r"^> This page is about the open-source Phaser framework,.*\n\n", re.M)
OUTPUT_ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = MarkdownIt('commonmark').enable('table')
SIMPLIFIED = OpenCC('t2s')


def source_body(text):
    if text.startswith("---\n"):
        text = text.split("\n---\n", 1)[1]
    # The Earcut example's closing fence shares a line with the following prose.
    text = text.replace('\n```Returns the relative difference', '\n```\n\nReturns the relative difference')
    return re.split(r"^## For AI agents: Phaser AE\s*$", SKIP_PROMO.sub("", text), 1, flags=re.M)[0].strip()


def slug(title):
    title = re.sub(r"!?(\[[^]]+\])\([^)]*\)", r"\1", title)
    return re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", title.lower()).strip())


def heading_anchor(level, title, api):
    if level == 1:
        return 'page-title'
    if api and level == 3 and re.fullmatch(r"[\w.$~:-]+", title):
        return title
    return slug(title)


def words(text):
    return len(ASCII_WORD.findall(text))


def terminology(translation):
    translation = SIMPLIFIED.convert(translation.replace('▁', ' ').replace('⁇', '').strip())
    for old, new in (
        ("游戏对象对象", "游戏对象"), ("现场管理器", "场景管理器"),
        ("场面管理器", "场景管理器"), ("摄像头", "摄像机"),
        ("摄影机", "摄像机"),
        ("发色器", "着色器"), ("阴影器", "着色器"),
        ("度玛", "Gamma"), ("帕塞尔", "Phaser"), ("相位器", "Phaser"),
    ):
        translation = translation.replace(old, new)
    return translation


class Translation:
    def __init__(self, cache, model=None, count=False):
        self.db = sqlite3.connect(cache)
        self.db.execute("CREATE TABLE IF NOT EXISTS strings (source TEXT PRIMARY KEY, target TEXT NOT NULL)")
        self.cache = dict(self.db.execute("SELECT source, target FROM strings"))
        self.pending = set()
        self.count = count
        self.model = model

    def __call__(self, text):
        if text in LABELS:
            return LABELS[text]
        if text in TERMS:
            return TERMS[text]
        if not words(text):
            return text
        replaced = []

        def mask(match):
            replaced.append(match[0])
            return f"ZZ{len(replaced) - 1}ZZ"

        encoded = INLINE.sub(mask, text)
        if not words(PLACEHOLDER.sub("", encoded)):
            return text
        result = self.cache.get(encoded)
        if result is None:
            self.pending.add(encoded)
            for portion in (part.strip() for part in INLINE.split(text)) if replaced else []:
                if words(portion) and portion not in LABELS and portion not in TERMS and portion not in self.cache:
                    self.pending.add(portion)
            return text
        result = terminology(result) or encoded
        result = result.replace('<', '&lt;').replace('[', r'\[').replace(']', r'\]')
        if replaced:
            markers = Counter(int(match[1]) for match in PLACEHOLDER.finditer(result))
            if markers != Counter(range(len(replaced))):
                return text if self.count else self._translate_around_markup(text)
            result = PLACEHOLDER.sub(lambda match: replaced[int(match[1])], result)
        return result

    def _translate_around_markup(self, text):
        parts = []
        start = 0
        for match in INLINE.finditer(text):
            parts.append(self._fragment(text[start:match.start()]))
            parts.append(match[0])
            start = match.end()
        parts.append(self._fragment(text[start:]))
        return "".join(parts)

    def _fragment(self, text):
        stripped = text.strip()
        if not stripped or not words(stripped):
            return text
        leading = text[:len(text) - len(text.lstrip())]
        trailing = text[len(text.rstrip()):]
        translated = LABELS.get(stripped) or TERMS.get(stripped) or self.cache.get(stripped)
        if translated is None:
            self.pending.add(stripped)
            translated = stripped
        return leading + (terminology(translated) or stripped).replace('<', '&lt;') + trailing

    def translate_batch(self):
        model_folder = self.model
        prefix = ">>cmn_Hans<< " if (model_folder / "source.spm").exists() else ""
        source_file = model_folder / ("source.spm" if prefix else "sentencepiece.model")
        target_file = model_folder / "target.spm" if prefix else source_file
        source = sentencepiece.SentencePieceProcessor(model_file=str(source_file))
        target = sentencepiece.SentencePieceProcessor(model_file=str(target_file))
        translator = ctranslate2.Translator(
            str(model_folder if prefix else model_folder / "model"),
            device="cpu", compute_type="int8", inter_threads=3, intra_threads=2,
        )
        items = sorted(self.pending, key=len)
        for start in range(0, len(items), 256):
            batch = items[start:start + 256]
            encoded = source.encode([prefix + item for item in batch], out_type=str)
            results = translator.translate_batch(
                encoded, beam_size=1, max_batch_size=2048, batch_type="tokens",
                max_input_length=512, max_decoding_length=min(450, 2 * max(map(len, encoded)) + 20),
                no_repeat_ngram_size=6,
            )
            values = [terminology(target.decode(result.hypotheses[0]).strip()) for result in results]
            self.db.executemany(
                "INSERT OR REPLACE INTO strings VALUES (?, ?)", zip(batch, values),
            )
            self.db.commit()
            self.cache.update(zip(batch, values))
            print(f"翻译片段 {min(start + 256, len(items))}/{len(items)}", flush=True)
        self.pending.clear()


def rewrite_links(text, route, all_routes, anchors):
    def local_url(url, image):
        parts = urlsplit(url)
        if parts.scheme and parts.netloc not in {"phaser.io", "www.phaser.io", "docs.phaser.io"}:
            return url
        if url.startswith("#"):
            target = route
        else:
            path = parts.path.removesuffix(".md").rstrip("/")
            target = all_routes.get(path) or LEGACY_API_LINKS.get(path.removeprefix('./'))
            if not target and path == "/oss/docs":
                return "/guide/"
        if image or not target:
            if parts.path.startswith("/") and not parts.netloc:
                return "https://phaser.io" + url
            return url
        fragment = unquote(parts.fragment)
        if fragment and fragment not in anchors[target]:
            identifier = fragment.removeprefix('event:')
            canonical = slug(identifier)
            if canonical not in anchors[target]:
                matches = [anchor for anchor in anchors[target] if anchor.casefold() == identifier.casefold()]
                if not matches:
                    if url.startswith("#"):
                        return f"https://phaser.io{next(path for path, page in all_routes.items() if page == route)}{url}"
                    return url
                canonical = matches[0]
            fragment = canonical
        path = "" if url.startswith("#") else "/" + target.removesuffix("/index")
        if target.endswith("/index") and path:
            path += "/"
        return urlunsplit(("", "", path, parts.query, fragment))

    return LINK.sub(lambda match: match[1] + local_url(match[2], match[1].startswith("!")), text)


def cell_text(text, translate, api, index):
    content = text.strip()
    if not content:
        return text
    if TABLE_RULE.fullmatch(text):
        return text
    if content in LABELS:
        rendered = LABELS[content]
    elif api and not index:
        return text
    else:
        rendered = translate(content)
    rendered = rendered.replace("|", r"\|") if "|" not in content else rendered
    return text[:len(text) - len(text.lstrip())] + rendered + text[len(text.rstrip()):]


def render_line(line, translate, api):
    if line.startswith("|"):
        cells = re.split(r"(?<!\\)\|", line)
        return "|".join(
            cell_text(cell, translate, api, index == len(cells) - 2)
            for index, cell in enumerate(cells)
        )
    if line.startswith("`") and line.endswith("`") and line.count("`") == 2:
        return line
    if line.strip().startswith("<") and line.strip().endswith(">"):
        return line
    prefix, prose = LIST.match(line).groups()
    if prose.startswith("![") or not prose.strip():
        return line
    if match := LEADING_BOLD.match(prose):
        label, separator, rest = match.groups()
        colon = ":" if label.endswith(":") else ""
        name = label.rstrip(":")
        rendered = LABELS.get(name) or (name if api else translate(name))
        if name in {"Scope", "Type", "Extends", "Default"}:
            tail = rest
        elif api and name == "Returns" and " - " in rest:
            result_type, separator_text, description = rest.partition(" - ")
            tail = result_type + separator_text + translate(description)
        else:
            tail = translate(rest)
        return prefix + f"**{rendered}{colon}**{separator}{tail}"
    for label in ("Since", "Source", "Inherited from", "See also"):
        if prose.startswith(label + ":"):
            return prefix + LABELS[label] + "：" + prose[len(label) + 1:].lstrip()
    if api and (prose.startswith("[") and prose.endswith(")")):
        return line
    text = prose.strip()
    if words(text) < 2 and text not in LABELS and text not in TERMS:
        return line
    return prefix + translate(text) + prose[len(prose.rstrip()):]


def api_heading(title, depth, route, translate):
    if depth >= 3 or (depth == 1 and route != "api/index"):
        return title
    if route == "api/index" and depth == 1:
        return "Phaser v4.1.0 API 参考"
    label = title.rstrip(':')
    if label in LABELS:
        return LABELS[label]
    return title if re.fullmatch(r"[\w.$~:-]+", title) else translate(title)


@lru_cache(maxsize=800)
def code_lines(body):
    return {
        line
        for token in MARKDOWN.parse(body)
        if token.type in {'fence', 'code_block'} and token.map
        for line in range(*token.map)
    }


def inspect_anchors(body, api):
    found = set()
    fenced = code_lines(body)
    for index, line in enumerate(body.splitlines()):
        if index not in fenced and (heading := HEADING.match(line)):
            found.add(heading_anchor(len(heading[1]), heading[2], api))
    found.discard("")
    return found


def render(route, body, translate, routes, all_routes, anchors):
    api = route.startswith("api/")
    source = "https://phaser.io" + routes[route]
    lines, ids = [], set(anchors[route])
    used = set()
    title = None
    fenced = code_lines(body)
    for index, line in enumerate(body.splitlines()):
        if index in fenced:
            lines.append(line)
            continue
        updated = rewrite_links(line, route, all_routes, anchors)
        if heading := HEADING.match(line):
            hashes, original = heading.groups()
            depth = len(hashes)
            current = HEADING.match(updated)[2]
            if api:
                rendered = api_heading(current, depth, route, translate)
            else:
                standard_title = GUIDE_TITLES.get(route.rsplit('/', 1)[-1]) if depth == 1 else None
                rendered = standard_title or translate(current)
            base = heading_anchor(depth, original, api) or "section"
            anchor = base
            index = 1
            while anchor in used or (anchor != base and anchor in ids):
                anchor = f"{base}-{index}"
                index += 1
            used.add(anchor)
            lines.append(f"{hashes} {rendered} {{#{anchor}}}")
            if depth == 1 and title is None:
                title = rendered
                lines.extend(["", f"{'Phaser v4.1.0' if api else 'Phaser 4 指南'} · [英文原文]({source})"])
        else:
            lines.append(render_line(updated, translate, api))
    if not title:
        raise ValueError(f"Missing title in {route}")
    return title, "\n".join(lines).strip() + "\n"


def write_all(routes, bodies, anchors, translate):
    sidebar = []
    all_routes = {source.rstrip('/'): route for route, source in routes.items()}
    for route, body in bodies.items():
        title, page = render(route, body, translate, routes, all_routes, anchors)
        if translate.count:
            continue
        file = OUTPUT_ROOT / (route + ".md")
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(page)
        if route.startswith("guide/"):
            sidebar.append({"text": title, "link": "/" + route})
    if not translate.count:
        (OUTPUT_ROOT / ".vitepress" / "guide-sidebar.json").write_text(
            json.dumps(sidebar, ensure_ascii=False, indent=2) + "\n"
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path, help="directory with sources.json and original/ Markdown files")
    parser.add_argument("--model", type=Path, help="local CTranslate2 model directory")
    parser.add_argument("--count", action="store_true", help="inspect the number of distinct phrases without writing pages")
    options = parser.parse_args()
    if options.model is None and not options.count:
        parser.error("--model is required when generating docs")
    root = options.snapshot
    snapshot_routes = json.loads((root / "sources.json").read_text())
    bodies, routes = {}, {}
    for route, source in snapshot_routes.items():
        local = route + "index" if route.endswith("/") else route
        bodies[local] = source_body((root / "original" / (route + ".md")).read_text())
        routes[local] = source
    if not bodies:
        raise SystemExit("No Markdown files in the snapshot.")
    anchors = {route: inspect_anchors(body, route.startswith("api/")) for route, body in bodies.items()}
    translate = Translation(root / "translations.sqlite", options.model, options.count)
    original_count = translate.count
    translate.count = True
    write_all(routes, bodies, anchors, translate)
    translate.count = original_count
    print(f"{len(bodies)} 篇文档，{len(translate.pending)} 个待翻译片段", flush=True)
    if not options.count:
        while True:
            if translate.pending:
                translate.translate_batch()
            write_all(routes, bodies, anchors, translate)
            if not translate.pending:
                break


if __name__ == "__main__":
    main()
