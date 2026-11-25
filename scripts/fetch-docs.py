"""Download the Phaser 4 Guide, API v4.1.0 and Editor v5 Markdown snapshot."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
from subprocess import check_output
from urllib.parse import urlsplit
from xml.etree import ElementTree


ORIGIN = 'https://phaser.io'
GUIDE = '/oss/docs/phaser/'
API = '/oss/docs/api-documentation/'
EDITOR = '/oss/docs/phaser-editor/'


def fetch(url):
    return check_output(['curl', '-fsSL', '--max-time', '30', '--retry', '3', url])


def sources():
    sitemap = ElementTree.fromstring(fetch(ORIGIN + '/sitemap.xml'))
    for location in sitemap.findall('.//{*}loc'):
        path = urlsplit(location.text).path
        if path.startswith(GUIDE):
            yield 'guide/' + path.removeprefix(GUIDE), path
        elif path.startswith(API):
            relative = path.removeprefix(API)
            if relative and not relative[0].isdigit():
                if relative == 'api-documentation':
                    relative = 'index'
                elif relative.endswith('/'):
                    relative += 'index'
                yield 'api/' + relative, path
        elif path.startswith(EDITOR):
            relative = path.removeprefix(EDITOR)
            if not re.match(r'v\d+(?:/|$)', relative):
                route = relative.rstrip('/') + '/index' if relative.endswith('/') else relative or 'index'
                yield 'editor/' + route, path.rstrip('/')


def download(snapshot, route, path):
    destination = snapshot / 'original' / (route + '.md')
    content = destination.read_bytes() if destination.exists() else fetch(ORIGIN + path + '.md')
    frontmatter = content.split(b'\n---\n', 1)[0]
    if not frontmatter.startswith(b'---\ntitle: '):
        raise ValueError(f'{path} did not return documentation Markdown')
    if route.startswith('api/') and b'docs: "Phaser v4.1.0"' not in frontmatter:
        raise ValueError(f'{path} is no longer the pinned v4.1.0 API')
    if route.startswith('editor/') and b'docs: "Phaser Editor v5"' not in frontmatter:
        raise ValueError(f'{path} is no longer the pinned Editor v5 manual')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot', type=Path)
    snapshot = parser.parse_args().snapshot
    snapshot.mkdir(parents=True, exist_ok=True)
    routes = dict(sources())
    with ThreadPoolExecutor(max_workers=8) as pool:
        for _ in pool.map(lambda item: download(snapshot, *item), routes.items()):
            pass
    (snapshot / 'sources.json').write_text(json.dumps(routes, indent=2) + '\n')
    print(f'已保存 {len(routes)} 个源页面。')


if __name__ == '__main__':
    main()
