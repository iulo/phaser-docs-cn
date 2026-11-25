# 用户组件的基类 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/user-components/user-components-super-class)

在上一节,我们探讨了如何通过聆听Phaser事件来实施行为。在那里,我们对所有组件实施了`EventComponent`基础类。

Phaser编辑器提供的组件概念是灵活的,但我们认为提出执行组件的方法是一个好主意。

为此,我们创建了**UserComponent**类,您可以将其作为所有组件的基类。该类包含在 [phasereditor2d-scripts-core](https://github.com/phaserjs/editor-scripts-core)库中,如果您用 Phaser编辑器项目模板创建了该类,则应当包含在您的项目中。

[Learn more about script libraries](/editor/scene-editor/script-node/script-node-libraries)

如果您不使用脚本库, 您可以选择告诉编辑器生成 ** UserComputer** 类, 并且它会创建一个文件并“ 为您写入代码 ”。

程序很简单, 只要打开用户组件编辑器的上下文菜单。 在 **Resources ** 菜单中, 有选项可以以不同格式创建 `UserComponent.js`文件 :

![Context menu for creating the UserComponent.js file.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-create-base-class-file-04012021.webp)

备选方案是:

* **创建用户组件( U).js**: 创建带有JavaScript代码的`UserComponent.js`文件.
* **创建用户组件( U).ts**: 创建带有TypeScript代码的`UserComponent.ts`文件.
* **创建用户组件( ES 模块) (UserComputer.js)**: 使用 ES 模块导出规则,创建带有 JavaScript 文件的 `UserComponent.js` 文件.
* **创建用户组件( ES 模块)**: 使用ES模块导出规则,创建带有TypeScript代码的`UserComponent.ts`文件.

如果文件存在, 编辑器会询问您是否确认替换它 。

只需一次操作即可,除非您弄乱了文件内容,想要重设它.

文件创建后,可以使用**UserComponent**类作为组件的超级类.


## 用户组件类内 {#inside-the-usercomponent-class}

在[Implementing behaviors with the Phaser events](/editor/scene-editor/user-components/user-components-start-update-methods)部分,我们解释一个组件如何可以注册Phaser事件的监听器,用于执行特定的行为。**用户组件**类是相同的。它听Phaser事件,并调用特殊方法,这些方法可以在衍生的类中被推翻。这些是**用户组件**类所呈现的方法:

```javascript
class UserComponent {

    constructor(gameObject) {
        // registers the event listeners and call the methods
    }

    awake() { }

    start() { }

    update() { }

    destroy() { }
}
```

它在构造器中记录事件监听器:

```javascript
constructor(gameObject) {

    this.scene = gameObject.scene;

    const listenAwake =
            this.awake !== UserComponent.prototype.awake;
    const listenStart =
            this.start !== UserComponent.prototype.start;
    const listenUpdate =
            this.update !== UserComponent.prototype.update;
    const listenDestroy =
            this.destroy !== UserComponent.prototype.destroy;

    if (listenAwake) {

        this.scene.events.once("scene-awake", this.awake, this);
    }

    if (listenStart) {

        this.scene.events.once(
            Phaser.Scenes.Events.UPDATE, this.start, this);
    }

    if (listenUpdate) {

        this.scene.events.on(
            Phaser.Scenes.Events.UPDATE, this.update, this);
    }

    if (listenStart || listenUpdate || listenDestroy) {

        gameObject.on(Phaser.GameObjects.Events.DESTROY, () => {

            this.scene.events.off(
                Phaser.Scenes.Events.UPDATE, this.start, this);
            this.scene.events.off(
                Phaser.Scenes.Events.UPDATE, this.update, this);

            if (listenDestroy) {

                this.destroy();
            }
        });
    }
}
```

但让我们一步一步地走。首先,它检查要听什么事件。注意**awake()**,**start()**等方法是空的。所以,如果组件实例不能为其中一种方法提供不同的执行,那么它就意味着它可以跳过调用该方法。然后,首先要知道该怎么称呼:

```javascript
const listenAwake =
    this.awake !== UserComponent.prototype.awake;

const listenStart =
    this.start !== UserComponent.prototype.start;

const listenUpdate =
    this.update !== UserComponent.prototype.update;

const listenDestroy =
    this.destroy !== UserComponent.prototype.destroy;
```

在以下几行中,它会增加Phaser事件的监听器,但只有在需要时才会: .

```javascript
...
if (listenStart) {

    this.scene.events.once(Phaser.Scenes.Events.UPDATE, this.start, this);
}

if (listenUpdate) {

    this.scene.events.on(Phaser.Scenes.Events.UPDATE, this.update, this);
}
...
```

在构建器的结尾, 它会注册一个游戏对象的毁灭事件的监听器, 并删除所有监听器。 它这样做是为了避免在对象不活动时调用一个方法 。

当创建新组件时,只需执行**update()**方法即可更新:

```javascript
class RotateObject extends UserComponent {

    constructor(gameObject) {
        super(gameObject);
    }

    ...

    update() {

        // this method is called when the scene
        // emits the UPDATE event

        this.gameObject.angle += 1;
    }
}
```

** 用户组件** 类对许多情况来说“ 足够好”, 但您可以修改或使用完全不同的类别。 或者直接在您的组件中使用 Phaser事件 。

---
