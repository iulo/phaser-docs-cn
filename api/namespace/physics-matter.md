# Phaser.Physics.Matter {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter)

Scope: 
static
> 源码：[src/physics/matter-js/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/index.js#L7)  


## 静态函数 {#static-functions}

- [BodyBounds](/api/class/physics-matter-bodybounds)
- [Factory](/api/class/physics-matter-factory)
- [Image](/api/class/physics-matter-image)
- [MatterPhysics](/api/class/physics-matter-matterphysics)
- [PointerConstraint](/api/class/physics-matter-pointerconstraint)
- [Sprite](/api/class/physics-matter-sprite)
- [TileBody](/api/class/physics-matter-tilebody)
- [World](/api/class/physics-matter-world)
## 静态函数 {#static-functions-1}

- [Components](/api/namespace/physics-matter-components)
- [Events](/api/namespace/physics-matter-events)
- [Matter](/api/namespace/physics-matter-matter)
- [PhysicsEditorParser](/api/namespace/physics-matter-physicseditorparser)
- [PhysicsJSONParser](/api/namespace/physics-matter-physicsjsonparser)
## 静态函数 {#static-functions-2}

### MatterGameObject {#MatterGameObject}

#### \<static> MatterGameObject(world, gameObject, [options], [addToWorld]) {#static-mattergameobjectworld-gameobject-options-addtoworld}


**说明:**

将所有 Matter.js 物理组件混合到任何现有的 Phaser 游戏对象,包括您自己扩展或创建的游戏对象的工厂函数。这使得您能够给任何游戏对象完全的 Matter 物理能力,而无需它扩展特定类。

以下组件直接混合到游戏对象上: 弹跳、 碰撞、 强制、 硬盘、 重力、 质量、 感应器、 秒拍、 睡眠、 静态、 变形和 速度。 这意味着在调用此功能后, `setVelocity`、 `setFriction` 和 `isSensor` 等方法可以直接在游戏对象上使用 。

如果 `options`是现有的物质体实例(即它的 `type`属性等于 `'body'`),则通过 `setExistingBody` 来附加该物理体,否则, `options` 被作为 `MatterBodyConfig` 处理,并通过 `setBody` 创建新物理体,如果不提供 `shape`属性,则默认为矩形.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| world | [Phaser.Physics.Matter.World](/api/class/physics-matter-world) | 否 |  | 物质世界来增加物理体。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将应用物质对象的游戏对象 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) \| MatterJS.Body | 是 |  | 物质体的配置对象, 或物质体的示例 。 |
| addToWorld | boolean | 是 | true | 刚刚创建的机构应该立即加入世界吗? |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 游戏对象被传递,现在用Matter 物理组件增强.


> 源码：[src/physics/matter-js/MatterGameObject.js#L26](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/MatterGameObject.js#L26)  
引入版本：3.3.0


---

---
