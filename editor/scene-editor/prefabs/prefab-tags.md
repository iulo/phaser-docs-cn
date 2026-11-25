# 预制体标签 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs/prefab-tags)

## 预制体标签 {#prefab-tags}

预制体标签是Phaser编辑器中的一种新机制,可以对内容进行排序和过滤。目前,[prefab constraints](/editor/scene-editor/script-node/script-node-constraints)和[Game Object Reference user properties](/editor/scene-editor/prefabs/prefab-user-properties#game-object-reference-property-type)都使用标记。

标记在预制体文件中被定义, 并应用到预制体文件中。 与编辑器预先定义的 [prefab constraints](/editor/scene-editor/script-node/script-node-constraints) 不同, 标记由用户定义。 也就是说, 要对预制体中应用标记, 您必须先在项目中相同的预制体中或任何其他预制体中定义它。 预制体中定义的标记可以被项目中的任何其他预制体中使用 。

标签定义有名称,描述,以及一组超级标杆.

要定义标签, 编辑器会在检查器视图中显示 ** Prefab 标签定义** 部分。 此部分显示您在 prab 中已经定义的标签列表和添加新定义的按钮( ** Add Tag Definitation **) 。

![prefab tag definitions](https://cdn.phaser.games/oss-docs/assets/0935177332c944aa-script-nodes-tag-definitions-20250604.webp)

当单击 ** 添加标记定义 ** 按钮时, 显示一个对话框, 用于输入您要定义的标记的名称和描述 。

![Add tag definition dialog](https://cdn.phaser.games/oss-docs/assets/e2ec820785f1a2fe-script-node-add-tag-def-dialog-20250604.webp)

然后,这个定义将出现在定义列表中。尽管您可以看到,它不仅仅是一个列表,它是一个树,因为您可以定义等级标记。例如,您可以定义一个标签 ** 标签列表** , 并带有超级标签 ** 列表** 。 这意味着,使用 ** 列表** 标签的所有限制也适用于** 宠物列表** 标签。

要创建此标签等级, 您必须点击您想要成为新标签子的标签, 并选择 **Add Super- Tag ** 选项。 这将打开对话框, 将新标签定义为选中标签子的子 。

![Add super-tag](https://cdn.phaser.games/oss-docs/assets/952fea8fffb8d870-script-nodes-add-super-tag-20250604.webp)

同样,也可以编辑标签定义或删除.

### 添加标记到预制体文件 {#add-tags-to-a-prefab}

定义了要使用的标签后, 您可以将它们添加到预制体文件中。 要做到这一点, 请到预制体文件的检查器视图中的 ** Prefab Tags ** 区域。 您可以看到您已经添加到预制体文件的标签列表和添加新标签的按钮( ** Add Tag**) 。

如预期,一个变体预fab继承了原预fab的标记. 以下图像显示的是一个继承了**ListScript**预fab的**ListOffPetsScript **预fab的标记,可见预fab**ListOffpetsScript **有标记**listlict**的标记,这是在预fab**LestScript***中定义的标记,同时也是本地标记**宠物列表**.

![prefab tags](https://cdn.phaser.games/oss-docs/assets/552672609fdf0f90-script-node-prefab-tags-20250604.webp)

目前我们只使用预制体标记来表示脚本节点的限制。 然而,将来我们可能将这些标记用于其他目的。

---
