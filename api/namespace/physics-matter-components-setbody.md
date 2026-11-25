# Phaser.Physics.Matter.Components.SetBody {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-components-setbody)

Scope: 
static
> 源码：[src/physics/matter-js/components/SetBody.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/SetBody.js#L15)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### setBody {#setBody}

#### \<instance> setBody(config, [options]) {#instance-setbodyconfig-options}


**说明:**

设定此游戏对象以创建并使用基于给定的配置对象的新对象 。

调用此方法可以重新设置您在机体上设置的所有先前属性, 包括插件、 质量、 摩擦、 碰撞类别等 。 因此请按需要重新应用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | string \| [Phaser.Types.Physics.Matter.MatterSetBodyConfig](/api/typedef/types-physics-matter#mattersetbodyconfig) | 否 | 要么是一个字符串,如 `circle`, 要么是一个 Matter Set 机构配置对象。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** [Phaser.Physics.Matter.Components.SetBody](/api/namespace/physics-matter-components-setbody) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/SetBody.js#L175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/SetBody.js#L175)  
引入版本：3.0.0


---

### setCircle {#setCircle}

#### \<instance> setCircle(radius, [options]) {#instance-setcircleradius-options}


**说明:**

设定此游戏对象的Matter 物理体为圆形 。

调用此方法可以重新设置您在机体上设置的所有先前属性, 包括插件、 质量、 摩擦、 碰撞类别等 。 因此请按需要重新应用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radius | number | 否 | 圆之半径. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** [Phaser.Physics.Matter.Components.SetBody](/api/namespace/physics-matter-components-setbody) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/SetBody.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/SetBody.js#L43)  
引入版本：3.0.0


---

### setExistingBody {#setExistingBody}

#### \<instance> setExistingBody(body, [addToWorld]) {#instance-setexistingbodybody-addtoworld}


**说明:**

设定此游戏对象以使用给定的已存在物质对象 。

主体首先被从世界中移除,然后被添加到这个游戏对象中.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| body | MatterJS.BodyType | 否 |  | 此游戏对象应该使用的物理体 。 |
| addToWorld | boolean | 是 | true | 物理体应该立即加入世界吗? |


**返回值:** [Phaser.Physics.Matter.Components.SetBody](/api/namespace/physics-matter-components-setbody) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/SetBody.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/SetBody.js#L103)  
引入版本：3.0.0


---

### setPolygon {#setPolygon}

#### \<instance> setPolygon(radius, sides, [options]) {#instance-setpolygonradius-sides-options}


**说明:**

设定此游戏对象的Matter 物理体为多边形形状 。

调用此方法可以重新设置您在机体上设置的所有先前属性, 包括插件、 质量、 摩擦、 碰撞类别等 。 因此请按需要重新应用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radius | number | 否 | 多边形的"辐射",即从它的中心到任何顶点的距离,这也是它的环绕半径. |
| sides | number | 否 | 多边形的边数 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** [Phaser.Physics.Matter.Components.SetBody](/api/namespace/physics-matter-components-setbody) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/SetBody.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/SetBody.js#L62)  
引入版本：3.0.0


---

### setRectangle {#setRectangle}

#### \<instance> setRectangle(width, height, [options]) {#instance-setrectanglewidth-height-options}


**说明:**

设定此游戏对象的Matter 物理体为矩形 。

调用此方法可以重新设置您在机体上设置的所有先前属性, 包括插件、 质量、 摩擦、 碰撞类别等 。 因此请按需要重新应用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 长方形的宽度。 |
| height | number | 否 | 长方形的高度. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** [Phaser.Physics.Matter.Components.SetBody](/api/namespace/physics-matter-components-setbody) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/SetBody.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/SetBody.js#L23)  
引入版本：3.0.0


---

### setTrapezoid {#setTrapezoid}

#### \<instance> setTrapezoid(width, height, slope, [options]) {#instance-settrapezoidwidth-height-slope-options}


**说明:**

设定此游戏对象的Matter 物理体为tapezoid形状 。

调用此方法可以重新设置您在机体上设置的所有先前属性, 包括插件、 质量、 摩擦、 碰撞类别等 。 因此请按需要重新应用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 宽度的Trepezoid体。 |
| height | number | 否 | 夹层体的高度。 |
| slope | number | 否 | 夹角的斜率. 0 创建矩形, 1 创建三角形。 正面值使上方缩短, 而负值则使下方缩短 。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** [Phaser.Physics.Matter.Components.SetBody](/api/namespace/physics-matter-components-setbody) - 此游戏对象实例 。


> 源码：[src/physics/matter-js/components/SetBody.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/components/SetBody.js#L82)  
引入版本：3.0.0


---

---
