# Phaser.Physics.Matter.PhysicsJSONParser {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-physicsjsonparser)

Scope: 
static
> 源码：[src/physics/matter-js/PhysicsJSONParser.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsJSONParser.js#L10)  
引入版本：3.22.0

## 静态函数 {#static-functions}

### parseBody {#parseBody}

#### \<static> parseBody(x, y, config, [options]) {#static-parsebodyx-y-config-options}


**说明:**

从给定的JSON数据中分析一个物理体元素.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 物理体的横向世界位置. |
| y | number | 否 | 物理体的垂直世界位置. |
| config | object | 否 | 体型配置数据. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** MatterJS.BodyType - 联合来文机构。


> 源码：[src/physics/matter-js/PhysicsJSONParser.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsJSONParser.js#L53)  
引入版本：3.22.0


---

---
