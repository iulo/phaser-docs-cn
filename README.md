# Phaser 4 中文文档

Phaser 4 的非官方简体中文文档。站点包含[官方 Guide 的中文译文](guide/index.md)、[Phaser v4.1.0 API 参考](api/index.md)、[3 → 4 迁移指南](guide/migration.md)和[着色器指南](guide/shaders.md)。每页提供英文原文链接。Guide 和 API 使用机器翻译，代码示例和 API 标识符沿用原文。

## 本地开发

```sh
pnpm install --frozen-lockfile
pnpm dev
pnpm build
```

构建产物位于 `.vitepress/dist`，包含 Pagefind 全文搜索索引，可用 `pnpm preview` 预览。

## Cloudflare Pages

在 Cloudflare Pages 连接私有仓库 `iulo/phaser-docs-cn`。生产分支为 `main`，工作目录为仓库根目录，构建命令为 `pnpm build`，输出目录为 `.vitepress/dist`。

## 同步上游

先在项目外准备一个快照目录及 Argos English → Chinese 1.9 模型。使用 Python 3.12 执行下列命令。翻译缓存保存在快照目录中，脚本可继续未完成的翻译。

```sh
python -m pip install ctranslate2 sentencepiece markdown-it-py opencc-python-reimplemented
python scripts/fetch-docs.py /path/to/snapshot
python scripts/translate-docs.py /path/to/snapshot --model /path/to/translate-en_zh-1_9
pnpm build
```

迁移指南和着色器指南基于 Phaser [v4.2.1](https://github.com/phaserjs/phaser/releases/tag/v4.2.1)，上游 MIT 许可见 [public/license.txt](public/license.txt)。
