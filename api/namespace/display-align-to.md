# Phaser.Display.Align.To {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/display-align-to)

Scope: 
static
> 源码：[src/display/align/to/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/index.js#L7)  


## 静态函数 {#static-functions}

### BottomCenter {#BottomCenter}

#### \<static> BottomCenter(gameObject, alignTo, [offsetX], [offsetY]) {#static-bottomcentergameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其顶端边缘与`alignTo`游戏对象的底部相冲,并横向以它为中心.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/BottomCenter.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/BottomCenter.js#L12)  
引入版本：3.0.0


---

### BottomLeft {#BottomLeft}

#### \<static> BottomLeft(gameObject, alignTo, [offsetX], [offsetY]) {#static-bottomleftgameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其直接置于`alignTo`游戏对象下方,其左边缘与`alignTo`左边缘对齐.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/BottomLeft.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/BottomLeft.js#L12)  
引入版本：3.0.0


---

### BottomRight {#BottomRight}

#### \<static> BottomRight(gameObject, alignTo, [offsetX], [offsetY]) {#static-bottomrightgameobject-alignto-offsetx-offsety}


**说明:**

取出一个给定的游戏对象并与之对齐,使其直接置于下方,并冲到其他游戏对象的右边缘。右边缘 `gameObject` 与右边对齐 `alignTo`,然后将顶端 `gameObject` 放在最下端边沿 `alignTo`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/BottomRight.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/BottomRight.js#L12)  
引入版本：3.0.0


---

### LeftBottom {#LeftBottom}

#### \<static> LeftBottom(gameObject, alignTo, [offsetX], [offsetY]) {#static-leftbottomgameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其右边缘触碰`alignTo`游戏对象的左边缘,其下边缘与`alignTo`的下边缘对齐.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/LeftBottom.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/LeftBottom.js#L12)  
引入版本：3.0.0


---

### LeftCenter {#LeftCenter}

#### \<static> LeftCenter(gameObject, alignTo, [offsetX], [offsetY]) {#static-leftcentergameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其右边缘触碰`alignTo`游戏对象的左边缘,其垂直中心匹配.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/LeftCenter.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/LeftCenter.js#L12)  
引入版本：3.0.0


---

### LeftTop {#LeftTop}

#### \<static> LeftTop(gameObject, alignTo, [offsetX], [offsetY]) {#static-lefttopgameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其右边缘触碰`alignTo`游戏对象的左边缘,其顶边缘与`alignTo`顶端对齐.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/LeftTop.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/LeftTop.js#L12)  
引入版本：3.0.0


---

### QuickSet {#QuickSet}

#### \<static> QuickSet(child, alignTo, position, [offsetX], [offsetY]) {#static-quicksetchild-alignto-position-offsetx-offsety}


**说明:**

在一个游戏对象上, 在指定位置, 将其对齐。 所使用的对齐基于 `position` 参数,这是 `Phaser.Display.Align` 财产,例如 `LEFT_CENTER` 或 或 时 间 `TOP_RIGHT`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| position | number | 否 |  | 将游戏对象与游戏对象对齐的位置。 这是一个对齐常数, 如 `Phaser.Display.Align.LEFT_CENTER` 。 |
| offsetX | number | 是 | 0 | 位置上可选水平偏移,以像素计. |
| offsetY | number | 是 | 0 | 位置上可选垂直偏移,以像素计. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/QuickSet.js#L24](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/QuickSet.js#L24)  
引入版本：3.22.0


---

### RightBottom {#RightBottom}

#### \<static> RightBottom(gameObject, alignTo, [offsetX], [offsetY]) {#static-rightbottomgameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并校对,使其立即放置在`alignTo`游戏对象的右侧,并与其底边对齐.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/RightBottom.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/RightBottom.js#L12)  
引入版本：3.0.0


---

### RightCenter {#RightCenter}

#### \<static> RightCenter(gameObject, alignTo, [offsetX], [offsetY]) {#static-rightcentergameobject-alignto-offsetx-offsety}


**说明:**

使用一个给定的游戏对象并校对它,使其左边缘与`alignTo`游戏对象的右边缘冲出,并与其垂直中心匹配.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/RightCenter.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/RightCenter.js#L12)  
引入版本：3.0.0


---

### RightTop {#RightTop}

#### \<static> RightTop(gameObject, alignTo, [offsetX], [offsetY]) {#static-righttopgameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其左边缘与`alignTo`游戏对象的右边缘相冲,其顶边缘与`alignTo`的顶边缘相匹配.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/RightTop.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/RightTop.js#L12)  
引入版本：3.0.0


---

### TopCenter {#TopCenter}

#### \<static> TopCenter(gameObject, alignTo, [offsetX], [offsetY]) {#static-topcentergameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并校正它,使其直接放在上方 `alignTo` 游戏对象, 水平中心。 下边缘 `gameObject` 以顶端边缘定位的冲 `alignTo`,则它们的中心X坐标匹配。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/TopCenter.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/TopCenter.js#L12)  
引入版本：3.0.0


---

### TopLeft {#TopLeft}

#### \<static> TopLeft(gameObject, alignTo, [offsetX], [offsetY]) {#static-topleftgameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其下边缘与`alignTo`游戏对象的上边缘相冲,左边缘对齐。结果 `gameObject`出现在`alignTo`的正上方,锚在它的左侧。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/TopLeft.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/TopLeft.js#L12)  
引入版本：3.0.0


---

### TopRight {#TopRight}

#### \<static> TopRight(gameObject, alignTo, [offsetX], [offsetY]) {#static-toprightgameobject-alignto-offsetx-offsety}


**说明:**

取一个给定的游戏对象并校对,使其直接位于`alignTo`游戏对象上方,其右边缘对齐.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignTo | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/to/TopRight.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/to/TopRight.js#L12)  
引入版本：3.0.0


---

---
