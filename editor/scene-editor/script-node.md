# 脚本节点 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/script-node)

脚本节点是新型对象。 它不是一个显示对象, 而不是一个逻辑对象, 它可以有不同的目的, 特别是用于表达简单和复杂的行为。

直到现在,用户组件是唯一一个您需要添加到游戏对象中的功能的方法。脚本节点是一个更强大和通用的工具,您可以使用同样的目的。

基本上,脚本节点是一个逻辑对象,你可以添加到一个场景,游戏对象,或者另一个脚本节点。但更令人兴奋的是,你可以以同样的方式使脚本节点可以重复使用和扩展:使用预制体游戏对象。

这意味着,你可以制作一个脚本节点的预制体文件,添加自定义属性,创建预制体文件的变体,创建巢居预制体文件,并将脚本节点附加到预制体文件实例中.

这允许在等级结构中表达结合逻辑构件(ScriptNode prefabs)的复杂行为.

脚本节点的概念来自[visual programming languages](https://en.wikipedia.org/wiki/Visual_programming_language)和像[behavior tree](https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)这样的概念。然而,我们并不假装要创建完整、全功能的视觉语言。我们的建议是使用脚本节点来制作游戏中重复行为的块。你可以用它处理UI界面、菜单屏幕、内幕。你可以在游戏中使用它,但不能通过组合很多通用块,或者通过组合你为游戏专门做的块。

关于使用视觉脚本语言的优点的一个论点是,没有传统编程经验的创作者可以制作游戏。但我们的脚本节点概念是,你,JavaScript高级程序员,可以为你的游戏执行脚本节点“框架”,并交付给游戏级别设计师,用于将脚本与游戏对象和场景连接起来.

脚本节点是游戏的可选选择。 如果您是喜欢编码所有文件的人, 您根本不需要脚本节点。 然而, 我们发现很多情况下使用脚本节点可以节省时间。 想想行为, 如: 

- 点击此按钮时, 请启动 X 场景 。
- 当场景开始时,淡出此天体.
- 场景开始时,播放此声音.

您可以使用脚本节点和用户组件创建这些行为, 并且只能使用视觉工具将其与游戏对象和场景连接起来。 您可以创建 ** OnClick** 和 ** OnScenet Start** 脚本节点, 它们是事件类节点。 并且创建 ** FadeIn**, ** PlaySund**, ** StartScene** 脚本节点, 是动作类节点。 然后, 您可以在场景编辑器中连接它们, 而且您有一个完整的行为, 无需写单行代码 。

## 教学 {#tutorials}

至今我们还没有很多关于脚本节点的教育材料,但是, [Scott Westover](https://scottwestover.dev) 在他的影片中, 他做了一件出色的工作, 详细解释如何创建自己的脚本节点:

[Phaser Editor v4 Script Nodes Crash Course - Modular Game Development](https://www.youtube.com/watch?v=MI80DpDbwYg)

[![Scott video in youtube](https://cdn.phaser.games/oss-docs/assets/1b8b7d174056a3cc-script-nodes-scott-video-20241108.webp)](https://www.youtube.com/watch?v=MI80DpDbwYg)

---
