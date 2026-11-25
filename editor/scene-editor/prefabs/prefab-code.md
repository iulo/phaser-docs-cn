# 预制体代码生成 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-code)

Prefab 文件是一个场景, 并编译为 JavaScript( 或 TypeScript) 代码。 常规场景文件编译为扩展 [Phaser.Scene](/api/class/scene) 类的类。 它毕竟是一个场景。 然而, Prefab 文件编译为自定义对象类 。

[scene compiler](/editor/scene-editor/scene-compiler)生成的Prefab类扩展了一个游戏对象类,如[Image](/editor/scene-editor/game-objects/image-object),[BitmapText](/editor/scene-editor/game-objects/bitmap-text-object)等. 或[another prefab class](/editor/scene-editor/prefabs/prefab-variant).

这是编译 ** Dragon ** 预制体文件后生成的代码 :

```javascript
class Dragon extends Phaser.GameObjects.Image {

    constructor(scene, x, y, texture, frame) {
        super(scene, x ?? 100, y ?? 100, texture || "dragon", frame ?? "dragon/flamming_00");

        this.scaleX = 0.7;
        this.scaleY = 0.7;
    }
}
```

注意Prefab类扩展了[Phaser.GameObjects.Image](/api/class/gameobjects-image)类,因为Prefab对象是一个[Image](/editor/scene-editor/game-objects/image-object).

**Dragon**类的构造函数有[Image](/editor/scene-editor/game-objects/image-object)类的相同参数,但默认情况下,它使用预制体中设置的纹理。在构造函数体内,还设置了预制体中修改的属性:

```javascript
this.scaleX = 0.7;
this.scaleY = 0.7;
```

[scene compiler](/editor/scene-editor/scene-compiler)编译一个正则场景文件时,其中的预制体实例会作为Prefab类的实例生成: .

```javascript
class Level extends Phaser.Scene {

    constructor() {
        super("Level");
    }

    create() {
        ...

        // create the instance of the Dragon prefab class
        const dragon = new Dragon(this, 190, 120);
        // add the instance to the display list
        this.add.existing(dragon);
        // modify the 'angle' property of the instance
        dragon.angle = -30;
        ...
    }
}
```

另外, Prefab 类可以在游戏的任何时候由您手动进行即时刻刻刻刻。它只是一个自定义对象类, 它看起来就像您用手写它。

---
