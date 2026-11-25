# 故障排查 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/troubleshooting)

这是专门用来处理常见错误或问题的章节,您可以使用场景编辑器找到.


## 场景依赖性模型 {#scene-dependencies-model}

场景编辑器是一个复杂的工具。 它取决于整个工程的状态。 资源文件、 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 或 Prefab 文件的更改会影响场景编辑器的内容。 因此, 您可以在编辑器中发现一个故障或一些奇怪的东西, 就像没有图像或图像过时的物体。 在这种情况下, 您可以做其他任何步骤 :

* 执行 ** Refresh Scene** 命令:按 `Ctrl+Alt+U` 或从上下文菜单中找到它.
* 重新装入项目资源:按`Ctrl+Alt+R`键或点击[Main menu](/editor/workbench/main-menu)中的**重新装入项目**选项.


## 已过期生成代码 {#outdated-generated-code}

执行游戏时,你看到的场景可能不同。一个可能的原因是,场景在Prefab文件更改后没有重新编译 。

如果您更改了 Prefab 文件, 例如您更改了 prefab 对象的类型, 那么您应该重新编译所有引用 Prefab 文件的场景 。 快速的解决方案是重新编译整个工程: 按 `Ctrl+Alt+B` 或选择 [Main menu](/editor/workbench/main-menu) 中的 ** 编译工程 ** 选项 。


## 复制的场景标识符 {#duplicated-scene-identifier}

每个场景文件都有标识符,在项目中应该是独一无二的。当你创建新的场景文件时,会生成一个新的标识符。但是,如果复制一个场景文件的内容,并与之创建新的文件,那么您将会得到不同的文件,并带有相同的标识符。

如果是这种情况,编辑器会用相同的标识符文件显示错误消息:

![Duplicated scene ID message.](https://cdn.phaser.io/editor-docs/scene-editor-troubleshooting-duplicated-id-msg-08122020.webp)

你必须纠正这个错误,因为它会造成出乎意料的行为.

修补一下,打开 [Command Palette](/editor/workbench/command-palette) (`Ctrl+K`)并运行**Fix重复的Scenes ID**命令.

此命令将为所有共享同一标识符的场景文件生成新的标识符。 只有原始文件没有修改, 在这种情况下, 修改时间为旧的文件 。

我们建议使用 **Fix 重复的 Scenes ID** 命令,但您可以手动修改场景标识符。只需打开文本编辑器中的文件,并更改 `id` 字段 。

```javascript
{
    id: "write-here-a-unique-identifier",
    // ...
}
```

场景编辑器使用 `Phaser.Utils.String.UUID()` 函数生成新的标识符。 您可以使用同样的功能 。


## 禁用像素艺术渲染 {#disable-pixel-art-rendering}

默认情况下, Scene Editor 创建了启用 pixelArt 渲染旗的游戏。 您可以执行 ** Scene Editer: Deputy Pixel Art Rendering ** 命令并刷新页面, 从而更改此配置 。

---
