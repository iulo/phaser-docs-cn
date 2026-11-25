# 对象列表 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/object-list)

通常情况下,您需要将具有共同属性或类型,或在游戏中具有共同目标的物体分组,例如,您需要将敌人对象,可采项,平台对象分组,这样您就可以测试玩家是否与它们碰撞.

为此,场景编辑器允许将场景对象分组为JavaScript阵列.

您可以在现场中丢弃列表内置块来创建对象列表 :

![Add object list from the Blocks view.](https://cdn.phaser.io/editor-docs/scene-editor-object-list-add-from-blocks-20230516.webp)

或者在列表中添加对象时创建新列表 :

![Create new list in the Lists section.](https://cdn.phaser.io/editor-docs/scene-editor-object-list-new-list-from-section-20230516.webp)![Enter the name of the new list.](https://cdn.phaser.io/editor-docs/scene-editor-object-list-add-new-2-20230516.webp)

要将对象添加到对象列表, 请选择对象并查找 ** 列表 ** 区域。 点击 ** 列表 ** 属性的下拉, 它会显示在现场可用的列表, 并选择将选中的对象添加到列表中, 或者从列表中删除 :

![Add object to the list.](https://cdn.phaser.io/editor-docs/scene-editor-object-list-add-object-20230516.webp)

大纲视图显示您所在位置的对象列表, 属于 ** 列表 ** 类。 它也显示每个列表的对象 :

![Object lists in the outline.](https://cdn.phaser.io/editor-docs/scene-editor-object-list-outline-20230516.webp)

您可以通过在大纲中选择项目并按下**Delete**命令(`Del`)从列表中删除项目。

另外,您还可以用 Move 命令排序列表中的项目, 就像您命令场景中的游戏对象一样:

![Sorting commands.](https://cdn.phaser.io/editor-docs/scene-editor-object-list-order-commands-20230627.webp)

您可以在现场中找到列表项。 请选择列表项, 在检查器视图的 ** 列表项** 部分, 点击 ** 选择游戏对象** 按钮:

![List Item section.](https://cdn.phaser.io/editor-docs/scene-editor-object-list-item-section-20230516.webp)


## 对象列表属性 {#object-list-properties}

对象列表类型不是[Phaser API](https://phaser.io/oss/docs/docs/latest.md)的一部分,而是场景编辑器引入的。在**可变** 的检查器视图部分,它显示[Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties):

![Object List properties.](https://cdn.phaser.io/editor-docs/scene-editor-object-list-section-20230516.webp)

可在本节修改列表名称,参见列表项的推断类型,并更改对象列表变量的范围(默认为`CLASS`).


## 对象列表代码生成 {#object-list-code-generation}

[scene compiler](/editor/scene-editor/scene-compiler)生成的代码,创建一个列表,就是这样:

```javascript
this.pickableItems = [melon, melon_1, melon_2, bomb, bomb_1, bomb_2];
```

如果输出语言是 TypeScript,则 [scene compiler](/editor/scene-editor/scene-compiler) 生成列表的字段声明 :

```javascript
private pickableItems: Array<Melon|Bomb>;
```

注意[scene compiler](/editor/scene-editor/scene-compiler)推断出阵列元素的类型:`Melon`和`Bomb`的结合,它们都是预制体型。如果是Phaser内置型,它也推断出元素的类型:

```javascript
private parallax: Phaser.GameObjects.Image[];
```

这种详细的数组类型声明允许[Visual Studio Code](https://code.visualstudio.com)这样的代码编辑器能够提供更聪明的编码经验.


## 对象列表对 Phaser 组 {#object-list-vs-phaser-group}

传统上,Phaser使用[Group game object](/api/class/gameobjects-group)将对象围绕一个共同目的进行组合。但分组并不是[Group game object](/api/class/gameobjects-group)的唯一特征 :

* 它执行一个对象池。
* 是一个具有分类和排列项目方法的数据结构。
* 可用于作为修改物品状态的代理.
* 唤作物之法.
* 将游戏相关的全球操作应用到项目中.

那么,为什么场景编辑器没有使用[Group game object](/api/class/gameobjects-group)?

1. [Group game object](/api/class/gameobjects-group)的许多特性特别有助于实现游戏的逻辑,但我们认为,关卡制作者需要的只是组织对象.
2. [Group game object](/api/class/gameobjects-group)类型没有参数化。一个代码编辑器类型推导/自动补全引擎使用简单的JavaScript阵列效果更好。当你写到`const enemies = [enemy1, enemy2, ...]`时,像[Visual Studio Code](https://code.visualstudio.com)这样的代码编辑器可以推断出阵列项目的类型。
3. 即使对于人类来说,简单的JavaScript阵列也可以更容易理解.
4. 如果您需要 [Group game object](/api/class/gameobjects-group), 您可以用场景编辑器生成的天体阵列创建它 :
```javascript
const pickableItemsGroup = this.add.group(this.pickableItems);
```

---
