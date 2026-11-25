# 用 Phaser 事件实现行为 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/user-components/user-components-start-update-methods)

您将创建的许多用户组件将执行对象的某些行为。 这种行为应该初始化, 并在游戏循环的每一步骤更新 。

[Unity](https://unity.com)等游戏引擎,支持类似的设计模式,[use a Start and Update methods](https://docs.unity3d.com/Manual/CreatingAndUsingScripts)来实施组件的行为.

Phaser框架没有提供类似的方法,组件不属于Phaser API. 然而,Phaser提供了很多事件,您可以处理并执行游戏游戏。例如,您可以使用用户组件和Phaser事件模拟Unity脚本。您可以创建一个处理事件的**EventComputer**类:

```javascript
class EventComponent {

    /**
    * @param {Phaser.GameObjects.GameObject} gameObject
    */
    constructor(gameObject) {

        this.scene = gameObject.scene;

        // first time the scene is updated, call the `start` method
        this.scene.events.once(Phaser.Scenes.Events.UPDATE, this.start, this);
        // each time the scene is updated, call the `update` method
        this.scene.events.on(Phaser.Scenes.Events.UPDATE, this.update, this);
        // if the object is destroyed, call the `destroy` method
        gameObject.on(Phaser.GameObjects.Events.DESTROY, this.destroy, this);
    }

    start() {
        // to be overridden in derived classes
    }

    update() {
        // to be overridden in derived classes
    }

    destroy() {
        // the object is destroyed, so we remove all the event handlers
        this.scene.events.off(Phaser.Scenes.Events.UPDATE, this.start, this);
        this.scene.events.off(Phaser.Scenes.Events.UPDATE, this.update, this);
    }
}
```

然后,你可以设置**EventCompent**类作为所有组件的超级类:

![Setting a super class to components.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-super-class-07302020.webp)

现在,你可以取消组件类中的** start**,**update**,和**drew**方法。

```javascript
class HorizontalMove extends EventComponent {

    ...

    update() {

        this.gameObject.x += this.deltaX;
    }
}
```

`EventComponent`课程只是你能做的一个例子。它有一个弱点:并非所有组件都需要倾听所有事件。它浪费了资源,在所有情况下都增加了场景监听器。

自 v3. 13. 0 起, 编辑器可以“ 写” 一个基础类, 它可以是一个更好的解决方案。 然而, 您可以修改其代码, 并适应您的特定域。 请检查下一节 以了解更多细节 。

---
