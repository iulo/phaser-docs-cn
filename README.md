# Phaser 4 中文文档

Phaser 4 的非官方简体中文文档。首版翻译以 Phaser [v4.2.1](https://github.com/phaserjs/phaser/releases/tag/v4.2.1) 为基线，包含 [3 → 4 迁移指南](guide/migration.md)和[着色器指南](guide/shaders.md)。

## 本地开发

```sh
pnpm install --frozen-lockfile
pnpm dev
pnpm build
```

构建产物位于 `.vitepress/dist`，可用 `pnpm preview` 预览。

## Cloudflare Pages

在 Cloudflare Pages 连接私有仓库 `iulo/phaser-docs-cn`。生产分支为 `main`，工作目录为仓库根目录，构建命令为 `pnpm build`，输出目录为 `.vitepress/dist`。

## 上游和许可

译文页链接到对应的上游提交。同步时保留已有 URL 和章节锚点，核对示例代码和 API 名称，并更新逐页的版本和原文链接。上游文档、示例和插图所附的 MIT 许可见 [public/license.txt](public/license.txt)。

官网指南、API 和 Editor 手册的英文原文见 [Phaser 官方文档](https://www.phaser.io/oss/docs/)。
