# 创建脚本节点预制体 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/script-node/script-node-prefab)

脚本节点的力量在于您可以创建它们中的预制体. Prefabs是编辑器的核心功能,用于创建您角色的预制体,游戏项目,UI元素. PrefabS提供了灵活的架构(Prefabs).[nested prefabs](/editor/scene-editor/prefabs/prefab-nested), [prefab variants](/editor/scene-editor/prefabs/prefab-variant), [prefab properties](/editor/scene-editor/prefabs/prefab-user-properties), [appendable prefabs](/editor/scene-editor/prefabs/prefab-instance-children))用于创建可重复使用的对象。现在也可以创建游戏的行为(或部分美人).

您可以以同样的方式创建一个脚本节点预制体, 以创建游戏对象的预制体:

1. [Create a prefab file](/editor/scene-editor/prefabs/prefab-new-file).
2. [Add a script node to the scene](/editor/scene-editor/script-node/script-node-create).

如果在预制体场景中添加脚本节点预制体,则会生成预制体变体,其效果与游戏对象预制体相同,可以添加自定义属性.

如果你使用内置的[ScriptNode class](/editor/scene-editor/script-node/script-node-class)(我们建议你做什么),那么你可以实施该类提供的任何方法,如**醒**或**执行**方法。

用于脚本节点预制体文件的代码看起来是这样的:

```javascript
// You can write more code here

/* START OF COMPILED CODE */

import OnEventScript from "./OnEventScript";
import ScriptNode from "./ScriptNode";
import Phaser from "phaser";
/* START-USER-IMPORTS */
/* END-USER-IMPORTS */

export default class OnPointerDownScript extends OnEventScript {

    constructor(parent: ScriptNode | Phaser.GameObjects.GameObject | Phaser.Scene) {
        super(parent);

        // this (prefab fields)
        this.eventName = "pointerdown";

        /* START-USER-CTR-CODE */
        // Write your code here.
        /* END-USER-CTR-CODE */
    }

    /* START-USER-CODE */

    override awake(): void {

        this.gameObject.setInteractive();

        super.awake();
    }

    /* END-USER-CODE */
}

/* END OF COMPILED CODE */

// You can write more code here
```

以上代码为TypeScript,是执行**OnPointerDownScript**,这是**OnEventScript **预制体文件的[prefab variant](/editor/scene-editor/prefabs/prefab-variant),两个预制体文件都是[Basic Scripts project](/editor/scene-editor/script-node/script-node-basic-scripts-project)的一部分.

---
