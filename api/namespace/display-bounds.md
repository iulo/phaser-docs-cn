# Phaser.Display.Bounds {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/display-bounds)

Scope: 
static
> 源码：[src/display/bounds/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/index.js#L7)  


## 静态函数 {#static-functions}

### CenterOn {#CenterOn}

#### \<static> CenterOn(gameObject, x, y) {#static-centerongameobject-x-y}


**说明:**

定位游戏对象,使其以给定坐标为中心。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将重新定位的游戏对象 。 |
| x | number | 否 | 水平坐标将游戏对象定位在 。 |
| y | number | 否 | 垂直坐标将游戏对象定位在 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 定位的游戏对象 。


> 源码：[src/display/bounds/CenterOn.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/CenterOn.js#L10)  
引入版本：3.0.0


---

### GetBottom {#GetBottom}

#### \<static> GetBottom(gameObject) {#static-getbottomgameobject}


**说明:**

从游戏对象的边界返回底坐标。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |


**返回值:** number - 游戏对象界限的下方坐标 。


> 源码：[src/display/bounds/GetBottom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetBottom.js#L7)  
引入版本：3.0.0


---

### GetBounds {#GetBounds}

#### \<static> GetBounds(gameObject, [output]) {#static-getboundsgameobject-output}


**说明:**

返回游戏对象的未旋转边框为矩形。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |
| output | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| object | 是 | 存储值的对象。 如果不提供新的矩形, 将会创建 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle), object - - 游戏对象的界限。


> 源码：[src/display/bounds/GetBounds.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetBounds.js#L13)  
引入版本：3.24.0


---

### GetCenterX {#GetCenterX}

#### \<static> GetCenterX(gameObject) {#static-getcenterxgameobject}


**说明:**

从游戏对象的界限返回中心x坐标。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |


**返回值:** number - 游戏对象边界的中心x坐标.


> 源码：[src/display/bounds/GetCenterX.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetCenterX.js#L7)  
引入版本：3.0.0


---

### GetCenterY {#GetCenterY}

#### \<static> GetCenterY(gameObject) {#static-getcenterygameobject}


**说明:**

从游戏对象的界限返回中心 y 坐标。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |


**返回值:** number - 游戏对象的边界的中心y坐标.


> 源码：[src/display/bounds/GetCenterY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetCenterY.js#L7)  
引入版本：3.0.0


---

### GetLeft {#GetLeft}

#### \<static> GetLeft(gameObject) {#static-getleftgameobject}


**说明:**

从游戏对象的界限返回左坐标。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |


**返回值:** number - 游戏对象的边界的左坐标 。


> 源码：[src/display/bounds/GetLeft.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetLeft.js#L7)  
引入版本：3.0.0


---

### GetOffsetX {#GetOffsetX}

#### \<static> GetOffsetX(gameObject) {#static-getoffsetxgameobject}


**说明:**

返回游戏对象从 x 坐标中视似抵消的量。 这与 `width * origin.x` 相同。 如果 `origin.x` 的数值不等于 0, 此值将只大于 0 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |


**返回值:** number - 游戏对象的横向偏移 。


> 源码：[src/display/bounds/GetOffsetX.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetOffsetX.js#L7)  
引入版本：3.0.0


---

### GetOffsetY {#GetOffsetY}

#### \<static> GetOffsetY(gameObject) {#static-getoffsetygameobject}


**说明:**

返回游戏对象从 Y 坐标中视似抵消的量。 这与 `height * origin.y` 相同。 如果 `origin.y` 的数值不等于 0, 此值将只大于 0 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |


**返回值:** number - 游戏对象的垂直偏移 。


> 源码：[src/display/bounds/GetOffsetY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetOffsetY.js#L7)  
引入版本：3.0.0


---

### GetRight {#GetRight}

#### \<static> GetRight(gameObject) {#static-getrightgameobject}


**说明:**

从游戏对象的界限返回正确的坐标。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |


**返回值:** number - 游戏对象界限的右坐标 。


> 源码：[src/display/bounds/GetRight.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetRight.js#L7)  
引入版本：3.0.0


---

### GetTop {#GetTop}

#### \<static> GetTop(gameObject) {#static-gettopgameobject}


**说明:**

从游戏对象的界限返回顶部坐标。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 获取边界值的游戏对象 。 |


**返回值:** number - 游戏对象界限的顶部坐标 。


> 源码：[src/display/bounds/GetTop.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/GetTop.js#L7)  
引入版本：3.0.0


---

### SetBottom {#SetBottom}

#### \<static> SetBottom(gameObject, value) {#static-setbottomgameobject-value}


**说明:**

定位游戏对象,使其界限底部与给定坐标一致。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将重新定位的游戏对象 。 |
| value | number | 否 | 将游戏对象的界限定位的坐标 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 定位的游戏对象 。


> 源码：[src/display/bounds/SetBottom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/SetBottom.js#L7)  
引入版本：3.0.0


---

### SetCenterX {#SetCenterX}

#### \<static> SetCenterX(gameObject, x) {#static-setcenterxgameobject-x}


**说明:**

定位游戏对象,使其边界的横向中心与给定坐标保持一致。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将重新定位的游戏对象 。 |
| x | number | 否 | 将游戏对象的界限定位的坐标 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 定位的游戏对象 。


> 源码：[src/display/bounds/SetCenterX.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/SetCenterX.js#L7)  
引入版本：3.0.0


---

### SetCenterY {#SetCenterY}

#### \<static> SetCenterY(gameObject, y) {#static-setcenterygameobject-y}


**说明:**

定位游戏对象,使其边界的垂直中心与给定坐标一致。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将重新定位的游戏对象 。 |
| y | number | 否 | 将游戏对象的界限定位的坐标 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 定位的游戏对象 。


> 源码：[src/display/bounds/SetCenterY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/SetCenterY.js#L7)  
引入版本：3.0.0


---

### SetLeft {#SetLeft}

#### \<static> SetLeft(gameObject, value) {#static-setleftgameobject-value}


**说明:**

定位游戏对象,使其边界的左侧与给定坐标一致。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将重新定位的游戏对象 。 |
| value | number | 否 | 将游戏对象的界限定位的坐标 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 定位的游戏对象 。


> 源码：[src/display/bounds/SetLeft.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/SetLeft.js#L7)  
引入版本：3.0.0


---

### SetRight {#SetRight}

#### \<static> SetRight(gameObject, value) {#static-setrightgameobject-value}


**说明:**

定位游戏对象,使其边界的右侧与给定坐标一致。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将重新定位的游戏对象 。 |
| value | number | 否 | 将游戏对象的界限定位的坐标 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 定位的游戏对象 。


> 源码：[src/display/bounds/SetRight.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/SetRight.js#L7)  
引入版本：3.0.0


---

### SetTop {#SetTop}

#### \<static> SetTop(gameObject, value) {#static-settopgameobject-value}


**说明:**

定位游戏对象,使其边界的顶端与给定坐标保持一致。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将重新定位的游戏对象 。 |
| value | number | 否 | 将游戏对象的界限定位的坐标 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 定位的游戏对象 。


> 源码：[src/display/bounds/SetTop.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/bounds/SetTop.js#L7)  
引入版本：3.0.0


---

---
