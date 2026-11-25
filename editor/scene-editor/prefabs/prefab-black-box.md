# 将预制体作为黑盒使用 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-black-box)

此时, Scene 编辑器支持 [Phaser API](https://phaser.io/oss/docs/docs/latest.md) 中存在的对象类型的小子集。 最终, 我们将对所有内置对象类型执行支持 。

但是,如果需要将一个非支持类型的对象(Phaser对象类型或没有完全支持Phaser的任何其他类型)添加到场景中,则可以使用Prefab作为黑匣子来“加热”场景编辑器。

黑盒式的Prefab是一个非常简单的概念:它是一个不由[scene compiler](/editor/scene-editor/scene-compiler)编译的Prefab,所以你应该手动写Prefab类的代码.

比如,我们假设你想在现场添加一些在运行时产生纹理的物体,这些纹理形状是随机的颜色和位置。 让我们把它们命名为“面条 ” 。

首先,创建一个与你想要的类似,至少具有相同尺寸的纹理(此示例中的100x100).

像这样的:

![A reference image for the custom object.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-black-box-doodle.webp)

这是一个参考纹理。 上传到项目中并添加到 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file)。 您可以创建一个新的 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file), 只能由编辑器使用, 这样您就可以将其排除在游戏的发行架构之外 。

所以,创建一个**面** 预fab 与**面**纹理:

![Add the doodle image to the prefab file.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-black-box-1.webp)

我们有我们的预制体。但是你要在运行时生成纹理。要做到这一点,首先要禁用场景的编译,在[Scene compiler settings](/editor/scene-editor/scene-compiler#compiler-settings)中:

![Disable code generation.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-black-box-2.webp)

现在您已禁用代码编译, 您必须在 `Doodle.js` 文件中写入 `Doodle` 类。 它是一个简单的类, 它扩展了 [Phaser.GameObjects.Image](/api/class/gameobjects-image) , 但是它不会产生真实的图像纹理, 而是在运行时:

```javascript
class Doodle extends Phaser.GameObjects.Image {

    static ID = 0;
    static COLORS = ["red", "blue", "orange"];

    /**
     * @param scene {Phaser.Scene}
     */
    constructor(scene, x, y) {
        super(scene, x, y);

        // create a new texture key
        Doodle.ID++;
        const key = "doodle-" + Doodle.ID;

        // create a new canvas-based texture and add it
        // to the TextureManager with the new key
        const texture = scene.textures.createCanvas(key, 200, 200);

        // get the context of the texture and draw the random doodle
        const ctx = texture.getContext();

        ctx.strokeStyle = "black";

        // draw 5 shapes
        for (let i = 0; i < 5; i++) {

            ctx.save();

            // add a little rotation to the shape
            const angle = Phaser.Math.RND.integerInRange(-10, 10);
            ctx.rotate(Phaser.Math.DegToRad(angle));

            ctx.beginPath();

            // draw a rect, at a random position with a random size
            ctx.rect(
                Phaser.Math.RND.integerInRange(0, 50),
                Phaser.Math.RND.integerInRange(0, 50),
                Phaser.Math.RND.integerInRange(20, 50),
                Phaser.Math.RND.integerInRange(20, 50));

            // fill it with a random color
            const color = Phaser.Math.RND.pick(Doodle.COLORS);
            ctx.fillStyle = color;

            ctx.fill();
            ctx.stroke();

            ctx.restore();
        }

        // needed if the game is using the WebGL renderer
        texture.refresh();

        // set the new texture to the object
        this.setTexture(key);
    }

}
```

打开 ** Level ** 场景文件, 并添加几个 ** Doodle ** 预制体实例:

![The Doodle prefab instances in the level scene.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-black-box-3.webp)

注意所有 ** Doodle ** 实例看起来都是一样的。 您所写的自定义代码在游戏中执行, 而不是在编辑器中执行。 编辑器正在使用您创建的 `doodle.png` 图像作为参考 。

查看 `Level.js` 文件: 预制体实例是按预期创建的。 这里的诀窍是, ** Doodle** 构造器内部的代码是您的代码, 而不是 [scene compiler](/editor/scene-editor/scene-compiler) 生成的代码。 您只需要写一个与 `Level.js` 文件代码兼容的构造器签名 :

```javascript
class Level extends Phaser.Scene {

    constructor() {
        super("Level");

    }

    create() {

        // ...

        // doodle
        const doodle = new Doodle(this, 388, 105);
        this.add.existing(doodle);

        // doodle_1
        const doodle_1 = new Doodle(this, 380, 240);
        this.add.existing(doodle_1);

        // doodle_2
        const doodle_2 = new Doodle(this, 530, 170);
        this.add.existing(doodle_2);

        // ...
    }

}
```

因此,现在运行游戏:您可以看到**Doodle** 实例是随机的形状和颜色。这些实例正在使用您的自定义代码和方式创建纹理 :

![The different doodles in the game.](https://cdn.phaser.io/editor-docs/scene-editor-prefab-black-box-4.webp)

这个“黑盒”的技巧并不完美。 一个理想的编辑器应该运行您的**Doodle**自定义代码,并用自定义的纹理显示场景编辑器中的预制体实例。 但执行起来非常复杂。

使用黑匣子 Prefab , 您可以做“ 黑魔法 ” 。 想想用它可以将3D 对象放置在现场, 使用第三方框架和 [Extern game object](/api/class/gameobjects-extern) 。 或者用动画工具建模的复合 2D 对象。 或者用 Phaser 格式创建的砖图 。

---
