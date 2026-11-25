# Phaser.Physics.Arcade.Components {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-arcade-components)

Scope: 
static
> 源码：[src/physics/arcade/components/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/index.js#L7)  


## 静态函数 {#static-functions}

- [Acceleration](/api/namespace/physics-arcade-components-acceleration)
- [Angular](/api/namespace/physics-arcade-components-angular)
- [Bounce](/api/namespace/physics-arcade-components-bounce)
- [Collision](/api/namespace/physics-arcade-components-collision)
- [Debug](/api/namespace/physics-arcade-components-debug)
- [Drag](/api/namespace/physics-arcade-components-drag)
- [Enable](/api/namespace/physics-arcade-components-enable)
- [Friction](/api/namespace/physics-arcade-components-friction)
- [Gravity](/api/namespace/physics-arcade-components-gravity)
- [Immovable](/api/namespace/physics-arcade-components-immovable)
- [Mass](/api/namespace/physics-arcade-components-mass)
- [Pushable](/api/namespace/physics-arcade-components-pushable)
- [Size](/api/namespace/physics-arcade-components-size)
- [Velocity](/api/namespace/physics-arcade-components-velocity)
## 静态函数 {#static-functions-1}

### OverlapCirc {#OverlapCirc}

#### \<static> OverlapCirc(world, x, y, radius, [includeDynamic], [includeStatic]) {#static-overlapcircworld-x-y-radius-includedynamic-includestatic}


**说明:**

这种方法将搜索给定的圆形区域,并返回所有与之重叠的物理体的阵列。它可以返回动态、静态体或两者的混合体。

尸体只需与要考虑的搜索区域相交,不需要完全控制在其中.

如果设定使用RTree(默认为RTree),那么搜索速度相当快,否则搜索是O(N)的动态天体.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 |  | 拱廊物理世界. |
| x | number | 否 |  | 区域中心的x坐标以像素为单位进行内部搜索. |
| y | number | 否 |  | 区域中心的y坐标以像素为单位进行内部搜索。 |
| radius | number | 否 |  | 搜索区域半径在内部,以像素表示. |
| includeDynamic | boolean | 是 | true | 搜索中是否应该包括动态天体? |
| includeStatic | boolean | 是 | false | 搜索内容应该包括静态尸体吗? |


**返回值:** Array.\<[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body)>, Array.\<[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody)> - 一系列与指定区域重叠的天体.


> 源码：[src/physics/arcade/components/OverlapCirc.js#L6](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/OverlapCirc.js#L6)  
引入版本：3.21.0


---

### OverlapRect {#OverlapRect}

#### \<static> OverlapRect(world, x, y, width, height, [includeDynamic], [includeStatic]) {#static-overlaprectworld-x-y-width-height-includedynamic-includestatic}


**说明:**

这种方法将搜索给定的矩形区域,并返回所有与它重叠的物理体的阵列。它可以返回动态、静态体或两者的混合体。

尸体只需与要考虑的搜索区域相交,不需要完全控制在其中.

如果设定使用RTree(默认为RTree),那么搜索速度极快,否则搜索是O(N)的动态天体.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 |  | 拱廊物理世界. |
| x | number | 否 |  | 左上方的x坐标 搜索区域内部。 |
| y | number | 否 |  | 左上方的坐标 搜索区域内部。 |
| width | number | 否 |  | 搜索区域宽度 。 |
| height | number | 否 |  | 搜索区域高度 |
| includeDynamic | boolean | 是 | true | 搜索中是否应该包括动态天体? |
| includeStatic | boolean | 是 | false | 搜索内容应该包括静态尸体吗? |


**返回值:** Array.\<[Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body)>, Array.\<[Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody)> - 一系列与指定区域重叠的天体.


> 源码：[src/physics/arcade/components/OverlapRect.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/components/OverlapRect.js#L1)  
引入版本：3.17.0


---

---
