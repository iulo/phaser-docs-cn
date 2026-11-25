# 简介 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/asset-pack-editor/intro)

在 Phaser 游戏中,您使用 [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) 类的方法加载文件。 您可以这样来加载 [load a sprite-sheet](/api/class/loader-loaderplugin#spritesheet) 的文件 :

```javascript
this.load.spritesheet("bot", "images/robot.png", {
  frameWidth: 32,
  frameHeight: 38,
});
```

您通过一个键( `'bot'`) 来识别 [game cache](/api/class/cache-cachemanager) 中的文件, 文件的URL( `'images/robot.png'`) 和一个图示表配置对象, 以及像框架大小等其他信息 。

或者,你可以通过一个单一的参数,一个[SpriteSheetFileConfig](https://phaser.io/oss/docs/api-documentation/class/types-loader-filetypes.md#-spritesheetfileconfig)配置对象来加载文件:

```javascript
this.load.spritesheet({
  key: "bot",
  url: "images/robot.png",
  frameConfig: {
    frameWidth: 32,
    frameHeight: 38,
  },
});
```

每个文件类型都可以使用它的配置对象加载,这仅仅是一个JSON对象。按照这个逻辑,Phaser有一个特殊类型的文件,包含其他文件的配置:[Asset Pack file](/editor/asset-pack-editor/asset-pack-file).

使用加载器的`pack(...)`方法可以装入[Asset Pack file](/editor/asset-pack-editor/asset-pack-file):

```javascript
this.load.pack("level1", "assets/pack.json");
```

资源包编辑器允许您编辑一个 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file), 这使得您可以很容易地在游戏中加载资源。 您不用手写 JSON 文件的珍贵时间, 也可以用 [Asset Pack Editor](/editor/asset-pack-editor/intro) 来加载您的资源, 并使用视觉工具和智能操作 。

![Asset Pack Editor](https://cdn.phaser.io/editor-docs/asset-pack-editor-overview-20241005.webp)

电话 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 与IDE相关,主要原因有二:

- 它是一种 Phaser 内置格式。 这意味着您可以创建一个 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) , 并使用 Phaser 编辑器, 并用于任何 Phaser 工程, 即使您正在使用另一个 IDE 。
- 场景编辑器和最终由IDE提供的其他工具都是基于Phaser的,这意味着IDE可以重新使用[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)信息,将资源装入其内部工具.

---
