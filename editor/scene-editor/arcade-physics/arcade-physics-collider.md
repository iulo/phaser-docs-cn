# Arcade 物理碰撞器 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/arcade-physics/arcade-physics-collider)

[Collider](/api/class/physics-arcade-collider)是检查多个物理对象之间碰撞的物体。 Scene Editor允许通过从块视图拖到场景来创建对撞器 :

![Adding a collider.](https://cdn.phaser.io/editor-docs/arcade-physics-add-collider-1-20221011.webp)

相撞对象在纲要视图的**Acade**部分显示:

![Collider in the outline.](https://cdn.phaser.io/editor-docs/arcade-physics-collider-outline-20221011.webp)

当您选中它时, 它会显示检查器视图中的对撞器属性。 每个参数都对应 [Collider](/api/class/physics-arcade-collider) 构造器中的参数 :

![Collider parameters.](https://cdn.phaser.io/editor-docs/arcade-physics-collider-properties-20221011.webp)

属性为:

* [overlapOnly](/api/class/physics-arcade-collider#overlapOnly)
* [object1](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-collider.md#onject1)
* [object2](/api/class/physics-arcade-collider#object2)
* [collideCallback](/api/class/physics-arcade-collider#collideCallback)
* [processCallback](/api/class/physics-arcade-collider#processCallback)
* [callbackContext](/api/class/physics-arcade-collider#callbackContext)

[scene compiler](/editor/scene-editor/scene-compiler)将参数的值(除**overlapOnly**)与代码相匹配,这样您就可以将任何JavaScript的有效表达式写入参数值。

如果是**对象1**和**对象2**参数,您可以选择选择场景对象的变量名称:

![Select a variable name of an object of the scene.](https://cdn.phaser.io/editor-docs/arcade-physics-collider-object-dialog-20221011.webp)

除了物体,还可以参考[Object List](/editor/scene-editor/object-list).

因此,对撞器物体是用Arcade [Factory](/api/class/physics-arcade-factory)类的[collider](/api/class/physics-arcade-factory#collider)或[overlap](/api/class/physics-arcade-factory#overlap)方法在代码中生成的。类似这样的东西:

```javascript
const collider_stone = this.physics.add.collider(gorilla, stone, this.onCollideGorillaWithStone, undefined, this);
```

或者,如果选中**重叠只**参数:

```javascript
const collider_stone = this.physics.add.overlap(gorilla, stone, this.onCollideGorillaWithStone, undefined, this);
```

除了碰撞器的特性外,它还包含[Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties).

---
