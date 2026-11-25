# 视频 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/video-object)

视频是内置的Phaser对象类型:[Phaser.GameObjects.Video](/api/class/gameobjects-video).


视频对象使用 [video factory](https://phaser.io/oss/docs/api-documentation/class/gameobjects-gameobjectfactory.md#video) 代码创建。 [scene compiler](/editor/scene-editor/scene-compiler) 就是这样生成视频代码的:

```javascript
const player = this.add.video(192, 512, "my-video");
```

前两句是视频的位置,最后一句是 `"my-video"` 是一个在资源包中显示视频资源的关键。

要创建视频对象,您可以拖动视频块,将其丢入现场:

![Add video](https://cdn.phaser.io/editor-docs/scene-editor-video-object-add-20240730.webp)

视频对象需要打开视频文件。 当您放弃视频块时, 它会显示一个对话框来选择资源包文件中定义的视频键 :

![Select video key](https://cdn.phaser.io/editor-docs/scene-editor-video-object-select-key-20240730.webp)

一旦您选择了视频键, 视频对象将在场景中创建 :

![Video object in the scene](https://cdn.phaser.io/editor-docs/scene-editor-video-add-done-20240730.webp)

您可以通过从 Blocks 视图拖曳视频键并把它扔到现场来创建相同的视频对象:

![Create video object from video key](https://cdn.phaser.io/editor-docs/scene-editor-add-video-object-from-key-20240730.webp)


## 视频属性 {#video-properties}

视频对象具有以下属性: 视频对象具有以下特性: 视频对象具有下列特性: 视频对象有视频对象, 视频对象有视频属性:

- **自动播放**: 如果选中的话, 视频在开始播放时开始播放 。
- **循环**: 如果选中, 视频会循环播放 。
- **当前时间**: 以秒数搜索给定时间的视频.
- **视频键**: 资源包中视频资源的关键.

![Video properties](https://cdn.phaser.io/editor-docs/scene-editor-video-object-properties-20240730.webp)

要更改视频键( 文件), 请点击 ** Video 键** 按钮。 它打开对话框来选择另一个视频键 :

![Select a new video key](https://cdn.phaser.io/editor-docs/scene-editor-video-object-change-key.webp)

除了属性, Video 区域还有一个播放工具栏, 用于播放现场的视频。 它有播放、暂停、 寻求启动和寻求结束按钮 :

![Video properties](https://cdn.phaser.io/editor-docs/scene-editor-video-object-properties-20240730.webp)

视频类型具有其他对象类型常见的其他属性: 视频类型具有其他特性, 视频类型具有其他常见的属性, 视频类型具有其它常见的属性 :

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Origin properties](/editor/scene-editor/game-objects/common-object-properties#origin-properties)
* [Flip properties](/editor/scene-editor/game-objects/common-object-properties#flip-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)
* [Alpha properties](/editor/scene-editor/game-objects/common-object-properties#alpha-properties)
* [Tint](/editor/scene-editor/game-objects/common-object-properties#tint-properties)
* [Filters](https://phaser.io/oss/docs/phaser-editor/scene-editor/filters.md#a-filter-as-a-scene-object)
* [Hit Area](/editor/scene-editor/input#hit-area)

## 更新循环 {#update-loop}

Video 对象每次更新场景都会显示下一个视频帧。默认情况下,为了表现考虑,场景编辑器会一步步运行更新循环,只有在用户在场景中进行操作时才会运行,因此,您可以看到视频没有播放。要连续看到视频,您可以在场景编辑器工具栏中启用**Run Update Loop**选项:

![Run the update loop](https://cdn.phaser.io/editor-docs/scene-editor-video-object-scene-toolbar-20240730.webp)

此工具栏还包含一个按钮, 用于在现场所有视频的音频上/ 关闭声音 。

---
