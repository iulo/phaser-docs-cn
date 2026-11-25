# Phaser.Types.GameObjects.Group {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/types-gameobjects-group)

Scope: 
static
> 源码：[src/gameobjects/group/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/index.js#L7)  


## 静态函数 {#static-functions}

### GroupCallback {#GroupCallback}

#### GroupCallback {#groupcallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| item | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 集团成员 |


> 源码：[src/gameobjects/group/typedefs/GroupCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupCallback.js#L1)  
引入版本：3.0.0


---

### GroupClassTypeConstructor {#GroupClassTypeConstructor}

#### GroupClassTypeConstructor {#groupclasstypeconstructor}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属景点 。 |
| x | number | 否 | 这个游戏对象在世界的横向位置. |
| y | number | 否 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |


> 源码：[src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1)  
引入版本：3.0.0


---

### GroupConfig {#GroupConfig}

#### GroupConfig {#groupconfig}


> 源码：[src/gameobjects/group/typedefs/GroupConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupConfig.js#L1)  
引入版本：3.0.0


---

### GroupCreateConfig {#GroupCreateConfig}

#### GroupCreateConfig {#groupcreateconfig}


**说明:**

创建对象的总数将

键,长度 *帧,长度 * frameQuantity * (yoo? 2:1) *(1+重复)

如果`max`是非零的,那么创建的总数量不会超过`max`.

需要`key`。 [Phaser.GameObjects.Group#defaultKey](/api/class/gameobjects-group#defaultKey)没有使用。


> 源码：[src/gameobjects/group/typedefs/GroupCreateConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupCreateConfig.js#L1)  
引入版本：3.0.0


---

### GroupMultipleCreateCallback {#GroupMultipleCreateCallback}

#### GroupMultipleCreateCallback {#groupmultiplecreatecallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| items | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 新设立的集团成员 |


> 源码：[src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1)  
引入版本：3.0.0


---

---
