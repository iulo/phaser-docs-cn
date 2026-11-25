# 解除预制体实例关联 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-unbox)

## 解除预制体实例关联 {#unboxing-a-prefab-instance}

预制体实例可以被解框以将其转换成一个正则对象群。这意味着,你可以将一个对象与其即时的预制体定义脱钩,因此该对象在场景中成为普通对象。然而,可能情况是,该对象与一个是另一个预制体的预制体变体的预制体连接起来。在这种情况下,将对象解框后,它会与其即时的预制体脱钩,但还是会与原预制体连接起来.

您可以将这个特性用于不同的目的,比如使用某个预制体作为模板在场景中创建对象,然后解框以自由修改.

要取消预制体框实例,请在现场或大纲视图中选择对象,并执行 **Unbox Prefabext**命令。 您可以在上下文菜单中找到此命令: **Prefabs ** → **Ubox Prefabrext**。

让我们举个例子。 这是场景有一个 `levelTemplatePrefab` 预制体实例。 此预制体实例包含游戏关卡的基本元素。 然后, 您可以用它作为模板来创建游戏中不同的关卡 :

![scene with prefab instance to unbox](https://cdn.phaser.games/oss-docs/assets/d0e0d8e6958e686d-scene-editor-unbox-prefab-step-1-2025112.webp)

然后,我们执行`levelTemplatePrefab`实例上的未收件命令:

![unbox menu option](https://cdn.phaser.games/oss-docs/assets/653ac07456489ff7-scene-editor-unbox-prefab-step-2.webp)

然后,预制体实例被解框,其所有物体成为场景中的普通物体:

![unboxed prefab instance](https://cdn.phaser.games/oss-docs/assets/4482c18576e12a08-scene-editor-unbox-prefab-step-3.webp)

---
