# Phaser.Display.Align.In {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/display-align-in)

Scope: 
static
> 源码：[src/display/align/in/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/index.js#L7)  


## 静态函数 {#static-functions}

### BottomCenter {#BottomCenter}

#### \<static> BottomCenter(gameObject, alignIn, [offsetX], [offsetY]) {#static-bottomcentergameobject-alignin-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其下边缘与`alignIn`游戏对象的下边缘相匹配,其水平中心与`alignIn`的横向中心对齐.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/BottomCenter.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/BottomCenter.js#L12)  
引入版本：3.0.0


---

### BottomLeft {#BottomLeft}

#### \<static> BottomLeft(gameObject, alignIn, [offsetX], [offsetY]) {#static-bottomleftgameobject-alignin-offsetx-offsety}


**说明:**

取一个给定的游戏对象并校对, 使其位于另一个对象的左下角。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/BottomLeft.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/BottomLeft.js#L12)  
引入版本：3.0.0


---

### BottomRight {#BottomRight}

#### \<static> BottomRight(gameObject, alignIn, [offsetX], [offsetY]) {#static-bottomrightgameobject-alignin-offsetx-offsety}


**说明:**

取一个给定的游戏对象并校对, 使其定位在下方右角 `alignIn` 游戏对象。 右边缘 `gameObject` 匹配到右边 `alignIn`,然后将下边缘 `gameObject` 匹配到 `alignIn`.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/BottomRight.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/BottomRight.js#L12)  
引入版本：3.0.0


---

### Center {#Center}

#### \<static> Center(gameObject, alignIn, [offsetX], [offsetY]) {#static-centergameobject-alignin-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其定位在另一个对象的中心。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/Center.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/Center.js#L11)  
引入版本：3.0.0


---

### LeftCenter {#LeftCenter}

#### \<static> LeftCenter(gameObject, alignIn, [offsetX], [offsetY]) {#static-leftcentergameobject-alignin-offsetx-offsety}


**说明:**

选择一个特定的游戏对象并与之对齐,使其左边缘与 `alignIn`游戏对象的左边缘相冲,其垂直中心与 `alignIn` 的垂直中心相匹配。这可将游戏对象置于参考对象的左中心内部位置。可选择的偏移可以应用来调整任意一轴的最后一个位置。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/LeftCenter.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/LeftCenter.js#L12)  
引入版本：3.0.0


---

### QuickSet {#QuickSet}

#### \<static> QuickSet(child, alignIn, position, [offsetX], [offsetY]) {#static-quicksetchild-alignin-position-offsetx-offsety}


**说明:**

取一个给定的游戏对象并校正它, 使其相对于另一个游戏对象的位置。 所使用的对齐基于 `position` 参数, 是一个 `ALIGN_CONST` 值, 如 `LEFT_CENTER` 或 `TOP_RIGHT` 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| position | number | 否 |  | 将游戏对象与游戏对象对齐的位置。 这是一个对齐常数, 如 `ALIGN_CONST.LEFT_CENTER` 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/QuickSet.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/QuickSet.js#L25)  
引入版本：3.0.0


---

### RightCenter {#RightCenter}

#### \<static> RightCenter(gameObject, alignIn, [offsetX], [offsetY]) {#static-rightcentergameobject-alignin-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其右边缘与`alignIn`游戏对象的右边缘相冲,其垂直中心与`alignIn`游戏对象的垂直中心对齐.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/RightCenter.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/RightCenter.js#L12)  
引入版本：3.0.0


---

### TopCenter {#TopCenter}

#### \<static> TopCenter(gameObject, alignIn, [offsetX], [offsetY]) {#static-topcentergameobject-alignin-offsetx-offsety}


**说明:**

取一个给定的游戏对象并与之对齐,使其顶端边缘与`alignIn`游戏对象的顶端边缘相冲,横向居中.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/TopCenter.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/TopCenter.js#L12)  
引入版本：3.0.0


---

### TopLeft {#TopLeft}

#### \<static> TopLeft(gameObject, alignIn, [offsetX], [offsetY]) {#static-topleftgameobject-alignin-offsetx-offsety}


**说明:**

取下给定的游戏对象并校对,使其位于`alignIn`游戏对象的左上角。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/TopLeft.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/TopLeft.js#L12)  
引入版本：3.0.0


---

### TopRight {#TopRight}

#### \<static> TopRight(gameObject, alignIn, [offsetX], [offsetY]) {#static-toprightgameobject-alignin-offsetx-offsety}


**说明:**

取一个给定的游戏对象并校对,使其定位在`alignIn`游戏对象的右上角。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将定位的游戏对象 。 |
| alignIn | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 将校正位置置于此上的游戏对象 。 |
| offsetX | number | 是 | 0 | 职位可选横向抵销。 |
| offsetY | number | 是 | 0 | 职位可选垂直抵销。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 已对齐的游戏对象 。


> 源码：[src/display/align/in/TopRight.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/align/in/TopRight.js#L12)  
引入版本：3.0.0


---

---
