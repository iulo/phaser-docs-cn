# 容器 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/container-object)

在Phaser中,唯一有孩子的游戏对象类型是容器([Phaser.GameObjects.Container](/api/class/gameobjects-container))和[Layer](/editor/scene-editor/game-objects/layer-object)对象,但只有容器可以用来改造孩子(位置,角度和尺度).

[Learn more about working with parent objects in the Scene Editor](/editor/scene-editor/working-with-parent-objects).

可以通过在现场投放容器内置块来创建容器,或者使用[Create Container with Selection](#grouping-objects-in-a-container)命令.

![Creating an empty container.](https://cdn.phaser.io/editor-docs/scene-editor-container-drop-into-scene-12172020.webp)

[scene compiler](/editor/scene-editor/scene-compiler)生成的代码,用来创建容器,就是这样:

```javascript
// x=100, y=20
const container_1 = this.add.container(100, 20);

// some object is created and added to the container
const someObject = ... ;
container_1.add(someObject);
```


## 在容器中组合对象 {#grouping-objects-in-a-container}

有些情况下,您需要创建带有若干对象的容器。您可以通过选择对象和执行 [Create Container with Selection](#grouping-objects-in-a-container) 命令来做到这一点。

要执行命令,可以按下`J`键,也可以选择[context menu](/editor/scene-editor/working-with-parent-objects#parent-context-menu)键.

1. 选择对象。
2. 执行命令(按`J`).
3. 创建了一个新的容器。
4. 对象从原父删除.
5. 物体被添加到新的容器中.
6. 新容器是[trimmed](#trimming-a-container).

![Create container with selection.](https://cdn.phaser.io/editor-docs/scene-editor-create-container-with-selection-04182020.webp)


## 调整容器 {#trimming-a-container}

**Trim容器**命令清除了容器的空白空间,这意味着子对象被转移到左/上角的容器,容器被重新定位,使子对象处于相同的全球位置。

要执行此命令, 请按 `Shift+T` 键, 或选择 [context menu](/editor/scene-editor/working-with-parent-objects#parent-context-menu) 的 ** Trim Contain ** 选项 。

![Trim container.](https://cdn.phaser.io/editor-docs/scene-editor-trim-container-04182020.webp)

## 容器属性 {#container-properties}

容器类型中包含一些[common object properties](/editor/scene-editor/game-objects/common-object-properties):

* [Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties)
* [Lists properties](/editor/scene-editor/game-objects/common-object-properties#lists-properties)
* [Children properties](/editor/scene-editor/game-objects/common-object-properties#children-properties)
* [Transform properties](/editor/scene-editor/game-objects/common-object-properties#transform-properties)
* [Visible property](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties.md#visible-property)

---
