# Factory {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/physics-arcade-factory)

Arcade 物理工厂允许您轻松创建Arcade物理允许的游戏对象。这个工厂创建的物体会自动添加到物理世界中。

**构造函数**

`new Factory(world)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| world | [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) | 否 | Arcade 物理世界实例. |

---


**作用域**: static

> 源码：[src/physics/arcade/Factory.js#L16](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L16)  
引入版本：3.0.0

## 公开成员 {#public-members}

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

提到这个Arcade物理实验的场景


> 源码：[src/physics/arcade/Factory.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L43)  
引入版本：3.0.0


---

### sys {#sys}

#### sys: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#sys-phaserscenessystems}


**说明:**

参考了场景. Systems 这个Arcade物理实例属于。


> 源码：[src/physics/arcade/Factory.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L52)  
引入版本：3.0.0


---

### world {#world}

#### world: [Phaser.Physics.Arcade.World](/api/class/physics-arcade-world) {#world-phaserphysicsarcadeworld}


**说明:**

参考 Arcade物理世界.


> 源码：[src/physics/arcade/Factory.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L34)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### body {#body}

#### \<instance> body(x, y, [width], [height]) {#instance-bodyx-y-width-height}


**说明:**

创建一个具有指定位置和大小的新的物理正体。

这个物理体与任何游戏对象都没有关联,但在世界范围内仍然存在,可以测试碰撞,具有速度等.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 物理学界这个物理体的横向位置. |
| y | number | 否 |  | 物理学界这个物理体的垂直位置. |
| width | number | 是 | 64 | 物理体的宽度, 以像素表示。 无法为负数或为零 。 |
| height | number | 是 | 64 | 物理体的高度以像素表示。 无法为负数或为零 。 |


**返回值:** [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) - 被创造的躯体。


> 源码：[src/physics/arcade/Factory.js#L254](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L254)  
引入版本：3.60.0


---

### collider {#collider}

#### \<instance> collider(object1, object2, [collideCallback], [processCallback], [callbackContext]) {#instance-colliderobject1-object2-collidecallback-processcallback-callbackcontext}


**说明:**

创建新的Arcade 物理对撞器对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个检查碰撞的物体 。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第二个检查碰撞的物体 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 当两个物体碰撞时,调用符来引用. |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 在测试两个对象碰撞时可选择调用回调。 返回 `true` 允许处理碰撞, 或者返回 `false` 防止碰撞 。 |
| callbackContext | * | 是 | 呼叫回调的范围。 |


**返回值:** [Phaser.Physics.Arcade.Collider](/api/class/physics-arcade-collider) - 被创造的碰撞器。


> 源码：[src/physics/arcade/Factory.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L62)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这工厂


> 源码：[src/physics/arcade/Factory.js#L318](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L318)  
引入版本：3.5.0


---

### existing {#existing}

#### \<instance> existing(gameObject, [isStatic]) {#instance-existinggameobject-isstatic}


**说明:**

将Arcade 物理体添加到给定的游戏对象中。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 一个游戏对象。 |
| isStatic | boolean | 是 | false | 创建静态体(真)或动态体(假). |


**返回值:** [Phaser.Types.Physics.Arcade.GameObjectWithBody](/api/typedef/types-physics-arcade#gameobjectwithbody) - 游戏对象.


> 源码：[src/physics/arcade/Factory.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L100)  
引入版本：3.0.0


---

### group {#group}

#### \<instance> group([children], [config]) {#instance-groupchildren-config}


**说明:**

创建物理组对象。该组创建的所有游戏对象将自动成为动态Arcade 物理对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> \| [Phaser.Types.Physics.Arcade.PhysicsGroupConfig](/api/typedef/types-physics-arcade#physicsgroupconfig) | [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 要添加到此组的游戏对象; 或 `config` 参数 。 |
| config | [Phaser.Types.Physics.Arcade.PhysicsGroupConfig](/api/typedef/types-physics-arcade#physicsgroupconfig) \| [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 此组的设置 。 |


**返回值:** [Phaser.Physics.Arcade.Group](/api/class/physics-arcade-group) - 创建的 Group 对象 。


> 源码：[src/physics/arcade/Factory.js#L237](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L237)  
引入版本：3.0.0


---

### image {#image}

#### \<instance> image(x, y, texture, [frame]) {#instance-imagex-y-texture-frame}


**说明:**

创建一个带有动态物理体的新弧形图像对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的键或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.Types.Physics.Arcade.ImageWithDynamicBody](/api/typedef/types-physics-arcade#imagewithdynamicbody) - 创建的图像对象 。


> 源码：[src/physics/arcade/Factory.js#L146](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L146)  
引入版本：3.0.0


---

### overlap {#overlap}

#### \<instance> overlap(object1, object2, [collideCallback], [processCallback], [callbackContext]) {#instance-overlapobject1-object2-collidecallback-processcallback-callbackcontext}


**说明:**

创建新的 Arcade 物理对撞器 Overlap 对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object1 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第一个检查重叠对象 。 |
| object2 | [Phaser.Types.Physics.Arcade.ArcadeColliderType](/api/typedef/types-physics-arcade#arcadecollidertype) | 否 | 第二个检查重叠对象 。 |
| collideCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 当两个对象重叠时,调用符。 |
| processCallback | [Phaser.Types.Physics.Arcade.ArcadePhysicsCallback](/api/typedef/types-physics-arcade#arcadephysicscallback) | 是 | 当测试两个对象重叠时可选择调用。 返回 `true` 允许处理重叠, 或者返回 `false` 防止重叠 。 |
| callbackContext | * | 是 | 呼叫回调的范围。 |


**返回值:** [Phaser.Physics.Arcade.Collider](/api/class/physics-arcade-collider) - 被创造的碰撞器。


> 源码：[src/physics/arcade/Factory.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L81)  
引入版本：3.0.0


---

### sprite {#sprite}

#### \<instance> sprite(x, y, key, [frame]) {#instance-spritex-y-key-frame}


**说明:**

创建一个带有动态物理体的新Arcade Sprite对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| key | string | 否 | 此游戏对象将使用的质地键用于渲染, 如保存在质地管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.Types.Physics.Arcade.SpriteWithDynamicBody](/api/typedef/types-physics-arcade#spritewithdynamicbody) - 创建的 Sprite 对象 。


> 源码：[src/physics/arcade/Factory.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L195)  
引入版本：3.0.0


---

### staticBody {#staticBody}

#### \<instance> staticBody(x, y, [width], [height]) {#instance-staticbodyx-y-width-height}


**说明:**

创建一个具有指定位置和大小的新的静态物理体。

此物理体与任何游戏对象都没有关联,但在世界范围内仍然存在,可以测试碰撞等.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 物理学界这个物理体的横向位置. |
| y | number | 否 |  | 物理学界这个物理体的垂直位置. |
| width | number | 是 | 64 | 物理体的宽度, 以像素表示。 无法为负数或为零 。 |
| height | number | 是 | 64 | 物理体的高度以像素表示。 无法为负数或为零 。 |


**返回值:** [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody) - 所创建的静态体.


> 源码：[src/physics/arcade/Factory.js#L286](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L286)  
引入版本：3.60.0


---

### staticGroup {#staticGroup}

#### \<instance> staticGroup([children], [config]) {#instance-staticgroupchildren-config}


**说明:**

创建静态物理组对象。该组创建的所有游戏对象将自动成为静态Arcade 物理对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> \| [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) | [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 要添加到此组的游戏对象; 或 `config` 参数 。 |
| config | [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) \| [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 此组的设置 。 |


**返回值:** [Phaser.Physics.Arcade.StaticGroup](/api/class/physics-arcade-staticgroup) - 已创建的静态组对象 。


> 源码：[src/physics/arcade/Factory.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L220)  
引入版本：3.0.0


---

### staticImage {#staticImage}

#### \<instance> staticImage(x, y, texture, [frame]) {#instance-staticimagex-y-texture-frame}


**说明:**

创建一个带有静态物理体的新 Arcade 图像对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的键或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.Types.Physics.Arcade.ImageWithStaticBody](/api/typedef/types-physics-arcade#imagewithstaticbody) - 创建的图像对象 。


> 源码：[src/physics/arcade/Factory.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L122)  
引入版本：3.0.0


---

### staticSprite {#staticSprite}

#### \<instance> staticSprite(x, y, texture, [frame]) {#instance-staticspritex-y-texture-frame}


**说明:**

创建一个带有静态物理体的新 Arcade Sprite 对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的键或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


**返回值:** [Phaser.Types.Physics.Arcade.SpriteWithStaticBody](/api/typedef/types-physics-arcade#spritewithstaticbody) - 创建的 Sprite 对象 。


> 源码：[src/physics/arcade/Factory.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/arcade/Factory.js#L170)  
引入版本：3.0.0


---

---
