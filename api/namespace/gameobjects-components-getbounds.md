# Phaser.GameObjects.Components.GetBounds {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-getbounds)

Scope: 
static
> 源码：[src/gameobjects/components/GetBounds.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L11)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### getBottomCenter {#getBottomCenter}

#### \<instance> getBottomCenter([output], [includeParent]) {#instance-getbottomcenteroutput-includeparent}


**说明:**

获得此游戏对象的下端- 中心坐标, 不管来源如何 。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L239](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L239)  
引入版本：3.18.0


---

### getBottomLeft {#getBottomLeft}

#### \<instance> getBottomLeft([output], [includeParent]) {#instance-getbottomleftoutput-includeparent}


**说明:**

获取此游戏对象的左下角坐标, 不论来源。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L213)  
引入版本：3.0.0


---

### getBottomRight {#getBottomRight}

#### \<instance> getBottomRight([output], [includeParent]) {#instance-getbottomrightoutput-includeparent}


**说明:**

获取此游戏对象的右下角坐标, 不论来源。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L265)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([output]) {#instance-getboundsoutput}


**说明:**

获得此游戏对象的轴对齐矩形, 不论来源。

边框矩是通过检索游戏对象的所有四个角位置(上左,上右,下左,下右),应用任何旋转和母容器变换,然后计算完全连接所有四个点的最小轴对齐矩来计算.

数值被存储并返回到矩形,或像矩形的物体中。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| output | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 是 | 存储值的对象。 如果不提供新的矩形, 将会创建 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle), object - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L291)  
引入版本：3.0.0


---

### getCenter {#getCenter}

#### \<instance> getCenter([output], [includeParent]) {#instance-getcenteroutput-includeparent}


**说明:**

获得此游戏对象的中心坐标, 不管来源如何 。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L57)  
引入版本：3.0.0


---

### getLeftCenter {#getLeftCenter}

#### \<instance> getLeftCenter([output], [includeParent]) {#instance-getleftcenteroutput-includeparent}


**说明:**

获得此游戏对象的左中点坐标, 不管来源如何 。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L161)  
引入版本：3.18.0


---

### getRightCenter {#getRightCenter}

#### \<instance> getRightCenter([output], [includeParent]) {#instance-getrightcenteroutput-includeparent}


**说明:**

获得此游戏对象的右中心坐标, 不论来源如何 。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L187)  
引入版本：3.18.0


---

### getTopCenter {#getTopCenter}

#### \<instance> getTopCenter([output], [includeParent]) {#instance-gettopcenteroutput-includeparent}


**说明:**

获得此游戏对象的顶端中心坐标, 不论来源如何 。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L109)  
引入版本：3.18.0


---

### getTopLeft {#getTopLeft}

#### \<instance> getTopLeft([output], [includeParent]) {#instance-gettopleftoutput-includeparent}


**说明:**

获得此游戏对象的左上角坐标, 不管来源为何。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L83](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L83)  
引入版本：3.0.0


---

### getTopRight {#getTopRight}

#### \<instance> getTopRight([output], [includeParent]) {#instance-gettoprightoutput-includeparent}


**说明:**

获得此游戏对象的右上角坐标, 不论来源。

返回点在本地空间计算,而不在任何母容器中计算,除非`includeParent`参数设置为`true`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 |  | 存储值的对象。 如果不提供新的矢量2, 将会创建 。 |
| includeParent | boolean | 是 | false | 如果此游戏对象有母容器, 则将它( 和所有其他祖先) 包含在生成的矢量中 ? |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 输出对象中存储的值 。


> 源码：[src/gameobjects/components/GetBounds.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/GetBounds.js#L135)  
引入版本：3.0.0


---

---
