# 核心脚本项目 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/script-node/script-node-basic-scripts-project)

在上一节中,我们谈到如何创建 `ScriptNode` 类。 这是非常基本的, 这是使用脚本节点所需的最小值。 为此, 我们创建了一个项目, 并配有您可以在游戏中使用的其他基本脚本节点: [scripts-core](http://github.com/phaserjs/editor-scripts-core) 工程 。

这是一个开发中的项目。在制作更多游戏时,我们可以通过脚本节点来改变它或增加上面的脚本数量。

接下来我们向您介绍项目概要。您可从项目网站了解更多情况:

[github.com/PhaserEditor2D/scripts-core](http://github.com/phaserjs/editor-scripts-core)

剧本分为三组:**Base**,**Events**,**Actions**.


## 基础脚本 {#base-scripts}

包含基本/抽象功能。您通常会创建它们预制体变体( 扩展它们) 。

* **脚本节点** - 全部剧本的基班课
* **斯普丽特脚本节点** - 访问图示对象的脚本节点的基础预制体文件。
* **根脚本节点** - 一个脚本节点,它可以自己注册到游戏对象中,并可以用作其他脚本的容器.


## 事件脚本 {#event-scripts}

这些脚本会聆听某些事件。 当事件被释放时, 然后处决孩子们, 也就是行动 。

* **在线脚本** - 登记给给定的`eventEmitter`,并听给定的`eventName`事件.
* **现场醒悟脚本** - 听现场的`scene-awake`事件。
* **上“ 点” 下脚本** - 聆听游戏对象的`pointerdown`事件.


## 动作脚本 {#action-scripts}

动作是手动执行的脚本, 或其他节点, 如事件或其他动作。 这一点很重要, 动作脚本本身不会执行 。

* **回调动作脚本** - 执行给定的 `callback` 表达式。
* **开始现场操作脚本** - 开始`sceneKey`的场景
* **执行动作脚本** - 执行给定的`targetAction`。
* **EmitEvent 动作脚本** - 给定的`eventEmitter` 发出给定的`eventName`。
* **提醒动作脚本** - 显示浏览器的提醒对话框, 并显示给定的 `message` 。
* **控制台LogAction 脚本** - 将给定的 `message` 登录到浏览器控制台。
* **销毁动作脚本** - 摧毁游戏对象。

---
