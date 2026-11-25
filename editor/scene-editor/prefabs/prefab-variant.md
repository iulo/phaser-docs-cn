# 预制体变体 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-variant)

预制体变体是扩展其他预制体的预制体。这是一个类似于[Unity Engine](https://unity.com) **预制体变体**的概念,所以我们使用同名的。然而,与场景编辑器中的其他所有内容一样,预制体变体的最好理解方式是研究生成的代码。然后你意识到,预制体变体是预制体类的子类。

一种预制体变体继承了基质Prefab的属性和值,但是,你可以解锁属性并修改属性.

[Learn more about unlock a prefab property](/editor/scene-editor/prefabs/prefab-set-properties).

你可以很容易地创建一个预制体变体,你只需要使用预制体作为预制体文件的预制体对象.

假设我们想创造出一个紫色的预制体变体, 来表示“Dragon**预制体”。

- 创建一个新的 Prefab 文件, 命名为 ** PurpleDragon **. Learn [how to create a prefab file](/editor/scene-editor/prefabs/prefab-new-file).
- 将 ** Dragon ** Prefab 丢弃到现场。 这会产生一个文件的prefab 对象 。
  
  ![Create prefab object with Dragon prefab.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-variant-1-04222020.webp)

- 解锁对象的[texture property](/editor/scene-editor/game-objects/common-object-properties#text-property),将其改为紫龙纹理,保存文件.
  
  ![Change the prefab object texture.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-variant-2-04222020.webp)

- 打开 ** Level** 场景文件, 在 Blocks 视图中查看 。 将 ** Prefab 和 ** PurpleDragon ** Prefab 放在现场, 它将创建一个新的, 紫色的, 预fab 实例 。

  ![Create a green and purple dragons.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-variant-3-04222020.webp)

- 但是,你要缩小两条龙的大小。为此,您要改变**Dragon**Prefab的X轴大小,这将影响两例,即**Dragon **和**PurpleDragon**,因为**Purpledragon**是现在缩放的**Dragon***Prefab的变种.

  ![The new scale is applied to both instances.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-variant-4-04222020.webp)

---
