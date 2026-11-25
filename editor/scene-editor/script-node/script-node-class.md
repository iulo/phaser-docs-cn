# 脚本节点类 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/script-node/script-node-class)

当创建脚本节点实例时, [scene compiler](/editor/scene-editor/scene-compiler) 生成这样的代码:

```javascript
new ScriptNode(parent);
```

这意味着它创造了一个`ScriptNode`类的例子。但是这个类不属于Phaser API,是您应该自行编码的类。

此类的协议很简单, 它需要一个接受父参数的构造器。 类似的东西 :

```javascript
class ScriptNode {

   constructor(parent) {
   }
}
```

很简单,但如果你需要的话,你可以创建一个具有更多特性的预制体,比如处理子对象,事件等......

好消息是, 此类包含在 Phaser 编辑器项目模板中。 如果您的项目不是基于模板, 您可以从 `@phaserjs/editor-scripts-core` 脚本库中安装 。 [Learn more about the script libraries](/editor/scene-editor/script-node/script-node-libraries) 。

另外,Phaser编辑器可以为您生成该类的默认执行,具有基本功能:

1. 在 [Files view](/editor/workbench/files-view) 中,您要在要添加类文件时选择文件夹 。
2. 打开 [Command Palette](/editor/workbench/command-palette) (`Ctrl+K`)和搜索(搜索) `script`.
3. 选择带有所希望的格式的命令(TypeScript,JavaScript,ES模块,...).
4. **执行** 命令,并生成选定文件夹中的类文件。

![Create ScriptNode class commands.](https://cdn.phaser.io/editor-docs/script-node-create-script-node-class-1-20230323.webp)

编辑器提供的这个内置类包含一些功能:

* 保留了对场景,游戏对象,以及父方的参考.
* 管理一个子节点的阵列。
* 注册执行**ake**、**agart**、**update**和**destroy**事件的现场和游戏对象,它遵循与[User Components events](/editor/scene-editor/user-components/user-components-super-class)相同的逻辑。
* 提供“行动节点”的接口。


## 父母亲 {#the-parent}

当创建 `ScriptNode` 类的新实例时, 它会接收父节点作为参数。 这个父节点可以是场景、 游戏对象, 或是另一个脚本节点 。

脚本节点实例保留了对父的引用,但也保留了对游戏对象和场景的引用. 当然,如果在场景中添加了节点,则游戏对象引用不更新,它会保留`undefined`.

与父母相关,该类提供以下属性: 父母的性格,包括: 父母的性能,包括: 父母一方的性格,包括父母的性格,以及父母的性格,如父母一方的性格等.

- `parent()`: 类型是: `Phaser.Scene | Phaser.GameObjects.GameObject | ScriptNode`.
- `gameObject()`: 类型是: `Phaser.GameObjects.GameObject | undefined`.
- `scene()`: 类型是: `Phaser.Scene`.


## 子对象 {#the-children}

`ScriptNode` 类有保留子的节点阵列。 当创建新节点时, 此数组会更新。 也提供了一些相关的方法 :

* `children ()`: 供孩子们流浪的属性.
* `add()`: 添加新孩子的方法。 当创建新孩子时, 这种方法会自动被称作 。


## 事件 {#the-events}

`ScriptNode`课程提供了几种处理特殊事件的方法,可能有助于您实施行为。它和[User Components events](/editor/scene-editor/user-components/user-components-super-class)一样有效。这些方法是:

- `awake()`: 当场景的所有对象被创建时它被称为。 此时将可获得用户属性( prifab) 的值, 这样您就可以超越这种方法来进行需要属性值的计算。 它的工作就像 [UserComponent “awake” method](/editor/scene-editor/user-components/user-components-awake-event) 一样 。
- `start()`:这被称为第一次现场更新.
- 每当现场更新时,它都会被称作"`update()`"("SHE").
- `destroy()`:当游戏对象被摧毁或场景关闭时,它被称为"游戏对象".


## 行动方法 {#the-action-methods}

我们认为建立动作脚本节点的协议是方便的。动作脚本是一个执行一定任务的脚本节点。为此,类提供了以下方法:

- `execute()`:包含动作代码.
- `executeChildren()`:执行子孙.

在下一章中,我们提到一个包含基本节点执行的项目,您可以将它包含在游戏中。这些脚本提供了您可以用来进行游戏的协议或样式。


## 行动的目标 {#the-actions-target}

动作节点大多修改或读取了节点的游戏对象。这对很多情况来说是好的,但有点有限。让我们看看一个例子。

想要在玩家对象和硬币对象列表之间制作一个对撞器,并在玩家触碰硬币时销毁硬币:

![The scene for collecting coins](https://cdn.phaser.io/editor-docs/scene-editor-script-node-target-action-game-20240109.webp)

我们有一个 **Make collider 动作** 节点,您可以添加到玩家中。 此节点有一个参数来选择您想要拼接的另一个对象。 在这种情况下,它是一个与硬币相配合的容器 :

![Make collider node.](https://cdn.phaser.io/editor-docs/scene-editor-script-node-demo-collider-node-20240109.webp)![Make collider node properties](https://cdn.phaser.io/editor-docs/scene-editor-script-node-demo-collider-node-props-20240109.webp)

当碰撞发生时,对撞器节点执行孩子,并传递两个对象作为参数,在第一个参数中玩家走,在第二个参数中走硬币.

因此,我们在拼接器节点上添加了 **Destroy Object Action**。这个节点是破坏对象的行动。默认情况下,它会摧毁与之相关的游戏对象:玩家。但我们想要摧毁硬币,而不是玩家。所以我们需要将毁灭行动的目标从游戏对象改为第二个参数。

为此,我们将“行动目标配置”的用户部分添加到破坏对象行动中,并将“目标**”设置为“ARG_2”**。然后,销毁行动将获得第二个论据并销毁它。

![The destroy action node](https://cdn.phaser.io/editor-docs/scene-editor-script-node-collider-demo-destroy-action-20240109.webp)![The properties of the destroy action](https://cdn.phaser.io/editor-docs/scene-editor-script-node-collider-demo-destroy-action-properties-20240109.webp)

**目标**参数显示了一系列选项,**GAME_OBJECT**(默认),**ARG_1**,.,**ARG_8**。

除了 ** 目标**, 您可以设置动作的 ** 目标名称 ** 。 此名称只涉及语法糖, 并且使得节点在大纲视图中更容易读取 。 请查看上一张截图, 节点的起始值为 ** 目标** 加上 ** 目标名称** 。


## 自定义动作脚本节点 {#custom-action-script-node}

制作一个新的动作节点非常简单。 只要创建一个 ** 脚本节点** 的预制体, 并应用 `execute()` 方法。 如果您想要支持 ** 动作目标配置** 组件, 您可以使用 `ScriptNode.getActionTargetObject()` 工具方法 :

```javascript
execute(...args: any[]) {

   const obj = this.getActionTargetObject(args);

   obj.doSomething();
}
```

该实用方法的用途如下:

- 检查节点中是否有 ** Action target 配置 ** 用户组件。如果它存在,且配置了目标以返回一个参数,那么返回正确的参数。
- 否则,它会返回节点的游戏对象.

---
