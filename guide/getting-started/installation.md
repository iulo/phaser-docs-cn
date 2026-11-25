# 安装 Phaser {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/getting-started/installation)

## 创建 Phaser 游戏项目 {#create-phaser-game-app}

Phaser快速启动的最简单方式是我们的`create-phaser-game`应用。这个 CLI 工具将呈现一个交互选择的官方项目模板和演示游戏。 发布命令、 回答一些问题, 应用将下载和配置合适的软件包 。

```bash
npm create @phaserjs/game@latest
npx @phaserjs/create-game@latest
yarn create @phaserjs/game
pnpm create @phaserjs/game@latest
bun create @phaserjs/game@latest
```

我们有一个[create game app tutorial](https://phaser.io/tutorials/create-game-app),你可以读到 更多关于这个工具 和它提供。

## 通过 npm 安装 Phaser {#installing-phaser-from-npm}

通过 [npm](https://www.npmjs.com/package/phaser) 安装 :

```bash
npm install phaser
```

## 从 GitHub 克隆 Phaser {#cloning-phaser-from-github}

Phaser在GitHub上可以使用[https://github.com/phaserjs/phaser](https://github.com/phaserjs/phaser).

可以通过 git 两种方式复制:

```bash
https://github.com/phaserjs/phaser.git
# or
git@github.com:phaserjs/phaser.git
```

或者,你可以使用 GitHub 桌面。详情请见 [Phaser GitHub page](https://github.com/phaserjs/phaser) 。

## 通过 CDN 使用 Phaser {#using-phaser-from-a-cdn}

[Phaser is on jsDelivr](https://www.jsdelivr.com/package/npm/phaser)是“ 超快的 CDN 开发者” 。 在您的 html 中包含 _ 任一 _ :

```html
<script src="//cdn.jsdelivr.net/npm/phaser@3.86.0/dist/phaser.js"></script>
<script src="//cdn.jsdelivr.net/npm/phaser@3.86.0/dist/phaser.min.js"></script>
```

也可从Cloudflare的[cdnjs](https://cdnjs.com/libraries/phaser)中找到:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/phaser/3.86.0/phaser.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/phaser/3.86.0/phaser.min.js"></script>
```

## Phaser TypeScript 类型声明 {#phaser-typescript-definitions}

TypeScript定义全称可以在[types folder](https://github.com/phaserjs/phaser/tree/master/types)内部找到,它们也在`package.json`中的`types`条目中被引用,这意味着VSCode等现代编辑器会自动检测到.

根据您的项目, 您可能需要在您的 `tsconfig.json` 文件中添加以下内容 :

```json
"lib": ["es6", "dom", "dom.iterable", "scripthost"],
"typeRoots": ["./node_modules/phaser/types"],
"types": ["Phaser"]
```

---
