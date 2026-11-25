# 简介 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/intro)

场景编辑器是IDE最重要的编辑器:它提供了视觉工具来创建场景(关卡)和可重复使用的游戏对象(前置).

![Scene Editor screenshot.](https://cdn.phaser.io/editor-docs/scene-editor-04102020.webp)

场景编辑器与其他场景制作工具类似,最奇特的特点是这个编辑器[compiles the scene](/editor/scene-editor/scene-compiler)变成可读的Phaser代码.

Phaser为某些文件格式提供支持,如[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)(由[Asset Pack Editor](/editor/asset-pack-editor/intro)编辑),但它缺乏适合级别编辑的全版场景文件格式。也许应该这样,因为Phaser是一个框架,而你可能以非常不同的方式和非常不同的上下文使用它。

如何开发场景编辑器? 我们知道我们需要以自定义格式保存场景。 我们有两个主要选项:

1. 我们可以创建自定义运行时间,或者插件,在游戏中加载场景文件,并在苍蝇中创建对象.
2. 我们可以创建一个场景编译器,将场景数据文件翻译为Phaser代码.

第二个选项在Phaser编辑器哲学中演奏得更好, 即完全兼容一个香草 Phaser运行时间。 因此, 这个编译器得到了一个场景数据文件( `.scene`) , 并生成一个干净, 可读, 手写般的 Phaser 代码。 即使这个选项还有其它优点: 非常容易调试场景, 并且知道对象是如何创建和修改的 。

在以前的基于桌面的Phaser编辑器中, Scene编辑器使用自定义的渲染器来构建场景。 此渲染是基于桌面 UI 工具包。 在这个版本中, 我们使用 Phaser 和浏览器来渲染编辑器中的场景。 这是一个巨大的优势, 现在, 在 Scene编辑器中看到的就是游戏中获得的。

本章涵盖深度的场景编辑器工具和概念,如果想要快速的教程来创建场景,请阅读[First steps chapter](/editor/first-steps/download-and-install).

---
