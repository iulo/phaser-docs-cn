# 脚本节点库 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/script-node/script-node-libraries)

在 Phaser 编辑器的 v3. 65 中, 我们引入了脚本库。 脚本库是一个可以在您的项目中安装的节点模块。 它和其他节点库一样有效。 您可以为您的游戏创建常见的行为, 并作为节点库分发 。

在Phaser编辑器中,我们创建了几个具有基本行为的库。我们应该继续研究这些库,增加更多的行为:

* [@phaserjs/editor-scripts-base](https://github.com/phaserjs/editor-scripts-base): 这是一个小库,每个游戏或任何其他脚本库都有基本的脚本和用户组件,默认会包含在所有项目模板中.
* [@phaserjs/editor-scripts-quick](https://github.com/phaserjs/editor-scripts-quick):这是一个更大的库,拥有脚本节点和用户组件,可以覆盖游戏开发的不同领域,它处于活跃的开发中,应该随着时间演化而增加更多的事件和行动.

请检查每个仓库 详细信息。


## 安装脚本库 {#installing-a-script-library}

正如我们以前提到的那样,脚本库只是节点模块,你把它们作为其他节点模块安装:

```bash
npm install @phaserjs/editor-scripts-quick
```

下一步是将库添加到`phasereditor2d.config.json`文件的`scripts`部分:

```javascript
{
    "plugins": [],
    "scripts": [
        "@phaserjs/editor-scripts-base",
        "@phaserjs/editor-scripts-quick"
    ],
    "skip": [
        "dist"
    ],
    "playUrl": "http://localhost:8080"
}
```

您可以检查安装在 [Files view](/editor/workbench/files-view) 中的库 :

![Script libraries.](https://cdn.phaser.io/editor-docs/scene-editor-script-nodes-lirabries-files-view-20231205.webp)

如果您查看库内, 它包含场景和用户组件文件, 和任何工程一样。 您可以浏览、 打开、 并作为其它脚本节点使用。 请不要修改它们 。

脚本节点广泛使用[scene display name](/editor/scene-editor/display-properties)和[prefab instance display name](/editor/scene-editor/prefabs/prefab-display-properties)。

默认情况下, `node_modules`文件夹被排除在 Phaser编辑器项目之外。 然而, 当您安装脚本库时, 它将只包含与库相关的文件, 这意味着, 请, [keep excluding the Node modules](/editor/misc/resources-filtering) 将您从游戏项目中选择 。


### 香草 JavaScript 的脚本节点库 {#script-node-libraries-for-vanilla-javascript}

许多人喜欢用香草 JavaScript来编码或原型游戏, 但没有捆绑或编译器。 您被覆盖。 在每一个脚本库的 `browser` 文件夹中, 您可以包含在您的项目中的文件。 请读读库的 README 文件以获得详细的指令 。

当您将一个库“复制”到您的项目时, 会有包含该库版本的 `library.txt` 文件。 另外, 编辑器使用该文件来显示该库文件的颜色更轻。

---
