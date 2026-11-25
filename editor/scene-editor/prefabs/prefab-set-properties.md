# 修改预制体实例的属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-set-properties)

正如我们在前面几节中解释的那样,一个Prefab只是扩展其他Prefab类的类,或者一个Phaser内置型.

当创建前发实例时,新对象会得到在前发实例中设定的属性。例如,新实例的纹理是前发实例中(在前发实例类的构造器中)的相同纹理设定.

如果您更改了 Prefab 的纹理, 所有预制体实例都会使用新的纹理。 然而, 您可以解锁某些实例的 [texture property](/editor/scene-editor/prefabs/prefab-user-properties#texture-config-property-type) , 并设置不同的纹理 。

请注意, 当您选择一个预制体实例时, 检查器视图会在对象属性旁边显示一个“ 锁定” 图标。 该图标表示属性是锁定的。 如果您单击图标, 它将被修改为“ 未锁定” 图标, 意味着属性是解锁的 。

当您解锁一个属性时, 您可以更改其值, 如果该属性在 Prefab 中被更改, 则不会更新。 未解锁的属性将不再与 Prefab 链接 。

很容易理解,如果从类和类实例来看,则该实例会得到类构建器中设定的属性。但是,当你创建实例时,您可以改变该值,而无论您改变类构建器,它都保持不变。

现在,如果你再次锁定属性,属性将获得Prefab中设定的值。解锁一个属性就像重置到Prefab值。

让我们一步一步地看看一个例子:

- 创建两个 prefab 的例。 两种例都使用 Prefab 的相同纹理: 一个绿色的龙 :
  
  ![Two prefab instances.](https://cdn.phaser.io/editor-docs/prefab-set-property-example-1-04212020.webp)
  
- 您想要更改第一种的纹理, 所以您解锁 [texture property](/editor/scene-editor/prefabs/prefab-user-properties#texture-config-property-type) 并选择一个新的图像 :
  
  ![Unlock texture property.](https://cdn.phaser.io/editor-docs/prefab-set-property-example-2-04212020.webp)

- 你想看看它与紫色纹理的外观, 但你在** Dragon** Prefab文件中修改它, 所以,第二个预fab实例会自动更新, 以显示新的紫色龙纹理:
  
  ![You changed the texture in the prefab.](https://cdn.phaser.io/editor-docs/prefab-set-property-example-3-04212020.webp)

- OK,你喜欢龙的紫色,所以你希望所有的**Dragon**预制体实例都有相同的颜色。为了做到这一点,你再次锁定了第一只(黄褐色)龙的[texture property](/editor/scene-editor/prefabs/prefab-user-properties#texture-config-property-type),它得到了Prefab纹理:紫色的:

  ![Both instances with the same prefab texture.](https://cdn.phaser.io/editor-docs/prefab-set-property-example-4-04212020.webp)

---
