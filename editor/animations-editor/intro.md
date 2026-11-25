# 简介 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/animations-editor/intro)

[Sprite animations](/api/class/animations-animation)是Phaser游戏中最常使用动画字符的选项,这种动画技术的原则是显示一个图像的序列(帧),以给定的“速度”或帧速率.

Animation:

![Eagle animation.](https://cdn.phaser.io/editor-docs/eagle.gif)

动画框架 :

![Eagle animation frames.](https://cdn.phaser.io/editor-docs/eagle-spritesheet.webp)

在Phaser v3中,动画是作为全球物体的[created](/api/class/animations-animationmanager#create),在[animations manager](/api/class/animations-animationmanager)中:

您可以创建单动画 :

```javascript
this.anims.create({
    "key": "acorn",
    "frameRate": 12,
    "repeat": -1,
    "frames": [
        {
        "key": "atlas",
        "frame": "acorn-1"
        },
        {
        "key": "atlas",
        "frame": "acorn-2"
        },
        {
        "key": "atlas",
        "frame": "acorn-3"
        }
    ]
});
```

或多动画:

```javascript
this.anims.fromJSON(
    "anims": [
        {
            "key": "acorn",
            // ....
        },
        {
            "key": "player",
            // ....
        }
    ]
);
```

在练习中,您可以在游戏中一次创建所有动画, 很可能是在预装机场景中。 然后, 您可以在将动画键传递到 [play()](/api/class/gameobjects-sprite#play) 方法的 spirite 对象上播放动画 :

```javascript
mySprite.play("acorn");
```

创建动画的另一种方法是将它们全部装入一个JSON文件,并使用[this.load.animation(..)](/api/class/loader-loaderplugin#animation)方法加载文件:

```javascript
this.load.animation("my-anims", "assets/animations.json");
```

Phaser编辑器提供动画编辑器,以创建动画JSON文件。所以,工作流程非常简单:

* 与动画编辑器创建动画 JSON 文件.
* 将动画 JSON 文件导入到带有[Asset Pack Editor](/editor/asset-pack-editor/intro)的**Asset Pack**文件.
* 播放代码中的动画,并使用 [play()](/api/class/gameobjects-sprite#play) 方法或使用方法 [animation properties](/editor/scene-editor/game-objects/common-object-properties#animation-properties) 或 图标 [user components and prefabs](/editor/scene-editor/prefabs/prefab-user-properties#animation-key-property-type).

在下一节中,我们将涵盖动画编辑部的所有方面。

![Animations Editor](https://cdn.phaser.io/editor-docs/welcome-animations-editor-overview.webp)

---
