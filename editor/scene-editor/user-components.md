# 用户组件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/user-components)

一个组件是[design pattern](https://gameprogrammingpatterns.com/component),可以使用它来创建可重复使用的代码,并扩展游戏对象的行为和数据,使用[composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance).

例如,可以将一个 ** Horizontal Move** 组件添加到任何一种从一个位置水平移动到另一个位置的敌方对象上。这个组件类可以大致像这样写入(如实例,请参见 [User Components compiler](/editor/scene-editor/user-components/user-components-compiler) 一节):

```javascript
class HorizontalMove {

    constructor(gameObject) {

        // in the component, keep a reference to the entity
        this.gameObject = gameObject;
        // in the entity, keep a reference ('horizontalMove') to the component
        this.gameObject.horizontalMove = this;
        // init properties with default values
        this.minX = 0;
        this.maxX = 800;
        this.horizVelocity = 10;
    }

    start() {
        this.gameObject.body.velocity.x = this.horizVelocity;
    }

    update() {

        // the behavior of the component

        const velocity = this.gameObject.body.velocity;

        if (this.gameObject.x < this.minX) {
            velocity.x = Math.abs(this.horizVelocity);
        }

        if (this.gameObject.x > this.maxX) {
            velocity.x = -Math.abs(this.horizVelocity);
        }
    }
}
```

在场景中,您可以创建对象,并在其中添加 ** Horizontal Move ** 组件。然后,更新每个游戏循环步骤的组件 :

```javascript
class Level extends Phaser.Scene {

    create() {

        // create two objects, alien and spider, and add the HorizontalMove
        // component to both, but with different property values.

        this.alien = this.add.sprite(10, 10, "enemies", "alien");
        const alienMove = new HorizontalMove(this.alien);
        alienMove.minX = 10;
        alienMove.maxX = 100;
        alienMove.horizVelocity = 40;
        alienMove.start();

        this.spider = this.add.sprite(80, 100, "enemies", "spider");
        const spiderMove = new HorizontalMove(this.spider);
        spiderMove.minX = 50;
        spiderMove.maxX = 200;
        spiderMove.horizVelocity = -20;
        spiderMove.start();
    }

    update() {

        // update the HorizontalMove component of each object

        this.alien.horizontalMove.update();
        this.spider.horizontalMove.update();

         // in a real case, the component can register
         // a listener to the UPDATE event of the scene.
    }
}
```

在Phaser编辑器中,我们提供了一种创建游戏对象组件的方法(我们将其命名为**User组件**,以区别内置的Phaser组件),并在场景编辑器中使用它们. 预制体系统是创建可重复使用的行为和数据,但有其使用继承的局限性.

和场景编辑器一样,我们提供[User Components Editor](/editor/scene-editor/user-components/user-components-editor).

[User Components Editor](/editor/scene-editor/user-components/user-components-editor)允许您创建用户组件配置文件。 一个用户组件配置文件( `*.components`) 包含一个编译为 JavaScript( 或 TypeScript) 代码的组件配置列表, 它与 [scene compiler](/editor/scene-editor/scene-compiler) 相当相似 。

---
