# 插件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/misc/plugins)

[Phaser Editor Workbench](/editor/workbench/views)和Phaser开发工具基于插件.

内置插件和用户插件有两组。内置插件由编辑器安装提供。您可以在游戏项目或全球范围内安装用户插件。


## 内建插件 {#built-in-plugins}

编辑器的内置插件包含在编辑器的安装中。 这些插件包含整个工作台和 Phaser 开发工具。 您不需要“ 触摸” 这些插件, 除非您想要运行不同的编辑器版本。 例如, 如果您想要尝试编辑器的内置版本, 您可以使用 `-editor` 旗来设定编辑器的另外执行路径, 包括新的插件 。

```bash
$ PhaserEditor -project "/path/to/project" -editor "path/to/another/editor"
```


## 全局插件 {#global-plugins}

您可以在全球安装所有编辑器的插件。 只要将插件放在 `<user-home>/.phasereditor2d/plugins` 文件夹中即可 。


## 项目插件 {#projects-plugins}

您只能为您的工程提供插件。 方法就是指定 [project configuration file](/editor/misc/project-config) `phasereditor2d.config.json` 中的插件文件夹 :

```bash
{
    "plugins": ["./my-fonts-plugins", "./my-gameobjects-plugins"]
}
```

所有路径都与项目位置相对。


## 项目的国家预防机制一揽子计划 {#projects-npm-packages}

您可以通过 [NPM](https://www.npmjs.com) 包安装插件 。

什么时候开始 [Phaser Editor Core](/editor/intro/distributions#phaser-editor-core) 它在工程中查找安装在 `devDependencies` 报告 `package.json` 并加载套件包裹的插件。

例如,您可以这样安装 [phasereditor2d-ninepatch-plugin](https://www.npmjs.com/package/phasereditor2d-ninepatch-plugin) :

```bash
$ npm install phasereditor2d-ninepatch-plugin --save-dev
```

我们建议这样安装第三方插件。


## 额外插件 {#extra-plugins}

你可以用这个 `-plugins` 旗帜 [Phaser Editor Core](/editor/intro/distributions#phaser-editor-core) 用于加载额外插件 :

```bash
$ PhaserEditor -plugins "/demo/plugins;/some/extra/plugins" -project .
```

`-plugins`旗的参数是一个带有额外插件绝对路径的字符串,用分号`;`分隔.

---
