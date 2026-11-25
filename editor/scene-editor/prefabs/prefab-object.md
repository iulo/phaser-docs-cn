# 预制体对象 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-object)

预制体对象是Prefab文件顶部的对象,您可以将许多对象添加到场景中,但只有顶部的物体会被视作真正的Prefab,其他物体会被忽略.

我们这样做是为了简单,但也让我们可以创建不同版本的预制体对象,并移动到列表的首位,以防我们想将不同的对象作为预制体对象来宣传.

查看下一张图像,它显示的是**Dragon**预制体。文件中有三个对象,但只有**Green Dragon**预制体的物体将用作**Dragon **预制体。此外,看看其他的,非顶部物体在大纲视图中透明化:

![Prefab object](https://cdn.phaser.io/editor-docs/scene-editor-prefab-object-1-06272020.webp)

如果你后来决定用另一条龙来做你的Prefab, 那你可以把它移到现场的顶端, 仅此而已:

![Another prefab object](https://cdn.phaser.io/editor-docs/scene-editor-prefab-object-2-06272020.webp)

预制体对象的另一个特征是,你不能编辑它的[Variable properties](/editor/scene-editor/game-objects/common-object-properties#variable-properties),因为在生成的代码中,它不作为变量引用,它作为`this`引用.

预制体物体可以是任何类型的物体([Image](/editor/scene-editor/game-objects/image-object)、文本、容器、由场景编辑器支持的种类),甚至也可以是预制体物体。当预制体物体是预制体物体(Prefab **Somepreprefab**)时,我们说它是**Somepreprefab ** Prefab的预制体变体。


## 自动创建容器 {#automatic-container-creation}

在许多情况下, 您的 Prefab 将像图像一样成为单一对象。 在其他情况下, 您会在一个容器中组合多个对象 。

为了简化创建Prefab的工作流程,场景编辑器将遵循这些规则:

- 如果在空的 Prefab 场景中添加一个对象,则新对象将是 Prefab 对象.
- 如果您创建了对象, 但是 Prefab 场景已经包含一个 prafab 对象, 那么 :
   - 如果预制体对象是一个容器,则将新对象添加到其中。
   - 如果预制体对象不是容器,则会创建一个新的容器来组合旧的预制体对象和新对象。最后,新创建的容器将是新的预制体对象。

几句话,按照这些规则,场景编辑器在必要时自动将对象分组在一个容器中.

---
