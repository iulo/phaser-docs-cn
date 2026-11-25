# ObjectHelper {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-objecthelper)

将倾斜对象 GID 解析为相应的倾斜数据,并将 Tilesets 的每片属性应用于对象。它通过提供倾斜编辑器中定义的纹理框架、动画和自定义属性,协助从倾斜对象层创建 Game Objects 。

**构造函数**

`new ObjectHelper(tilesets)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tilesets | Array.\<[Phaser.Tilemaps.Tileset](/api/class/tilemaps-tileset)> | 否 | 支持的平板数据 。 |

---


**作用域**: static

> 源码：[src/tilemaps/ObjectHelper.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ObjectHelper.js#L9)  
引入版本：3.60.0

## 公开成员 {#public-members}

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

如果对象帮助器到达了瓷砖以获取数据,则启用。如果它只直接使用在基德对象上的数据,则禁用。


> 源码：[src/tilemaps/ObjectHelper.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ObjectHelper.js#L63)  
引入版本：3.60.0


---

### gids {#gids}

#### gids: array {#gids-array}


**说明:**

用于查找运行时 GID 的平面图。


> 源码：[src/tilemaps/ObjectHelper.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ObjectHelper.js#L29)  
引入版本：3.60.0


---

## 公开方法 {#public-methods}

### getTypeIncludingTile {#getTypeIncludingTile}

#### \<instance> getTypeIncludingTile(obj) {#instance-gettypeincludingtileobj}


**说明:**

从对象或后面的`gid`获得平面`type`字段值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| obj | [Phaser.Types.Tilemaps.TiledObject](/api/typedef/types-tilemaps#tiledobject) | 否 | 平板电脑的反对者 调查。 |


**返回值:** string - 物体的`type`,物体的`gid`后面的瓦片,或称`undefined`.


> 源码：[src/tilemaps/ObjectHelper.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ObjectHelper.js#L85)  
引入版本：3.60.0


---

### setPropertiesFromTiledObject {#setPropertiesFromTiledObject}

#### \<instance> setPropertiesFromTiledObject(sprite, obj) {#instance-setpropertiesfromtiledobjectsprite-obj}


**说明:**

设置对象及其瓦片上从平板属性(如果有)产生的`sprite.data`字段。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 用于设置数据的游戏对象 。 |
| obj | [Phaser.Types.Tilemaps.TiledObject](/api/typedef/types-tilemaps#tiledobject) | 否 | 将应用属性的平面对象 。 |


> 源码：[src/tilemaps/ObjectHelper.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ObjectHelper.js#L171)  
引入版本：3.60.0


---

### setTextureAndFrame {#setTextureAndFrame}

#### \<instance> setTextureAndFrame(sprite, [key], [frame], [obj]) {#instance-settextureandframesprite-key-frame-obj}


**说明:**

将图示纹理数据设定为指定的(通常是在配置中),或者,如果失败,则设定为正在装入对象的`gid`(如果有的话)中指定的。

只有在将砖块装入图案时,这个倒置才会起作用,它能匹配被装入图案的图案的几何形状,例如: 砖块内的"砖块 id #Z`3`"与从砖块的图像中提取的纹理框架 `3`相同.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sprite | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 要修改的游戏对象 。 |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | 要设置的纹理密钥( 或者如果有的话, `obj.gid` 的瓦片会被使用) 。 |
| frame | string \| number | [Phaser.Textures.Frame](/api/class/textures-frame) | 是 | 要设置的框架密钥( 或者如果有的话, `obj.gid` 的瓦片会被使用) 。 |
| obj | [Phaser.Types.Tilemaps.TiledObject](/api/typedef/types-tilemaps#tiledobject) | 是 | 倒置对象 。 |


> 源码：[src/tilemaps/ObjectHelper.js#L124](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ObjectHelper.js#L124)  
引入版本：3.60.0


---

---
