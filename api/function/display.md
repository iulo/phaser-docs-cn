# Phaser.Display.Align.In {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/display)

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


# Phaser.Display.Align.To {#page-title-1}

### BottomCenter {#BottomCenter-1}

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


### BottomLeft {#BottomLeft-1}

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


### BottomRight {#BottomRight-1}

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


### LeftCenter {#LeftCenter-1}

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


### QuickSet {#QuickSet-1}

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


### RightCenter {#RightCenter-1}

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


### TopCenter {#TopCenter-1}

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


### TopLeft {#TopLeft-1}

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


### TopRight {#TopRight-1}

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


# Phaser.Display.Bounds {#page-title-2}

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


# Phaser.Display.Canvas.CanvasInterpolation {#page-title-3}

### setCrisp {#setCrisp}

#### \<static> setCrisp(canvas) {#static-setcrispcanvas}


**说明:**

设置 CSS 设置 `image-rendering` 属性在给定的画布上使用最近的邻(crisp)缩放。这可以禁用反变异功能,使每个像素都变成硬的块,这是像素艺术游戏的理想。多个供应商前置的值被按顺序应用,以确保交叉浏览器兼容性,包括Firefox()`-moz-crisp-edges`),歌剧(`-o-crisp-edges`),WebKit(英语:`-webkit-optimize-contrast`),和互联网浏览器(`msInterpolationMode: nearest-neighbor`).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | HTMLCanvasElement | 否 | 要设置样式的画布对象 。 |


**返回值:** HTMLCanvasElement - 画布


> 源码：[src/display/canvas/CanvasInterpolation.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasInterpolation.js#L21)  
引入版本：3.0.0


### setBicubic {#setBicubic}

#### \<static> setBicubic(canvas) {#static-setbicubiccanvas}


**说明:**

将给定的画布上的 CSS `image-rendering` 属性设置为 `auto` , 恢复默认浏览器行为。 这样浏览器在画布缩放时可以应用平滑( 典型的双立) 插值, 其边缘比较柔和, 更适合高分辨率的纹理或非像素艺术的内容 。 同时将 IE 专用的 `msInterpolationMode` 设置为 `bicubic` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| canvas | HTMLCanvasElement | 否 | 要设置样式的画布对象 。 |


**返回值:** HTMLCanvasElement - 画布


> 源码：[src/display/canvas/CanvasInterpolation.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasInterpolation.js#L49)  
引入版本：3.0.0


# Phaser.Display.Canvas.CanvasPool {#page-title-4}

### create {#create}

#### \<static> create(parent, [width], [height], [canvasType], [selfParent]) {#static-createparent-width-height-canvastype-selfparent}


**说明:**

创建新的 Canvas DOM 元素,如果空闲,则从池中拉出。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| parent | * | 否 |  | 坎瓦斯天体的母体. |
| width | number | 是 | 1 | 坎瓦斯号的宽度. |
| height | number | 是 | 1 | 坎瓦斯人的高度。 |
| canvasType | number | 是 | "Phaser.CANVAS" | 风扇的型号,要么是`Phaser.CANVAS`,要么是`Phaser.WEBGL`. |
| selfParent | boolean | 是 | false | 使用生成的 Canvas 元素作为父元素 ? |


**返回值:** HTMLCanvasElement - 由池中创建或提取的画布元素 。


> 源码：[src/display/canvas/CanvasPool.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L29)  
引入版本：3.0.0


### create2D {#create2D}

#### \<static> create2D(parent, [width], [height]) {#static-create2dparent-width-height}


**说明:**

创建新的 2D 坎瓦 DOM 元素,或者如果空闲的话从池中拉出一个。

这是`create`周围的方便包装器,它将`canvasType`强制到`Phaser.CANVAS`,确保返回的画布总是用于2D渲染上下文.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| parent | * | 否 |  | 坎瓦斯天体的母体. |
| width | number | 是 | 1 | 坎瓦斯号的宽度. |
| height | number | 是 | 1 | 坎瓦斯人的高度。 |


**返回值:** HTMLCanvasElement - 由池中创建或提取的画布元素 。


> 源码：[src/display/canvas/CanvasPool.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L91)  
引入版本：3.0.0


### createWebGL {#createWebGL}

#### \<static> createWebGL(parent, [width], [height]) {#static-createwebglparent-width-height}


**说明:**

创建新的 WebGL Canvas DOM 元素。

这是`create`周围的方便包装,将`canvasType`强制到`Phaser.WEBGL`. WebGL画布从不添加到游泳池,因为一旦设置了WebGL上下文的选项,它们就不能被更改,使得集合不适合它们.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| parent | * | 否 |  | 坎瓦斯天体的母体. |
| width | number | 是 | 1 | 坎瓦斯号的宽度. |
| height | number | 是 | 1 | 坎瓦斯人的高度。 |


**返回值:** HTMLCanvasElement - 创建的 WebGL画布.


> 源码：[src/display/canvas/CanvasPool.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L111)  
引入版本：3.0.0


### first {#first}

#### \<static> first([canvasType]) {#static-firstcanvastype}


**说明:**

从泳池里拿到第一个免费帆布容器.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| canvasType | number | 是 | "Phaser.CANVAS" | 风扇的型号,要么是`Phaser.CANVAS`,要么是`Phaser.WEBGL`. |


**返回值:** HTMLCanvasElement - 如果需要WebGL帆布,或者游泳池没有免费帆布,则使用第一个免费帆布,或者`null`.


> 源码：[src/display/canvas/CanvasPool.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L132)  
引入版本：3.0.0


### remove {#remove}

#### \<static> remove(parent) {#static-removeparent}


**说明:**

以父画为基础, 查看一张画布, 如果发现它会放回池中, 将它放出来重新使用。 画布的宽度和高度设定为 1, 而它的父属性无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | * | 否 | 画布或画布的母体可以自由使用. |


> 源码：[src/display/canvas/CanvasPool.js#L164](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L164)  
引入版本：3.0.0


### total {#total}

#### \<static> total() {#static-total}


**说明:**

获取池中已使用的画布元素的总数。


**返回值:** number - 旧画布的数量 。


> 源码：[src/display/canvas/CanvasPool.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L189)  
引入版本：3.0.0


### free {#free}

#### \<static> free() {#static-free}


**说明:**

获取池中自由画布元素的总数。


**返回值:** number - 免费画布的数量 。


> 源码：[src/display/canvas/CanvasPool.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L212)  
引入版本：3.0.0


### disableSmoothing {#disableSmoothing}

#### \<static> disableSmoothing() {#static-disablesmoothing}


**说明:**

禁用创建的任何新 Canvas 元素上的环境平滑 。


> 源码：[src/display/canvas/CanvasPool.js#L225](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L225)  
引入版本：3.0.0


### enableSmoothing {#enableSmoothing}

#### \<static> enableSmoothing() {#static-enablesmoothing}


**说明:**

启用创建的任何新 Canvas 元素上下文的平滑 。


> 源码：[src/display/canvas/CanvasPool.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/CanvasPool.js#L236)  
引入版本：3.0.0


# Phaser.Display.Canvas.Smoothing {#page-title-5}

### getPrefix {#getPrefix}

#### \<static> getPrefix(context) {#static-getprefixcontext}


**说明:**

获取给定上下文使用的平滑启用的供应商前缀, 或设置无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D \| WebGLRenderingContext | 否 | 画布上下文要检查 。 |


**返回值:** string - 控制图像平滑的上下文(`imageSmoothingEnabled`或供应商前缀版本)上的财产名称,或者不支持的`null`。


> 源码：[src/display/canvas/Smoothing.js#L24](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L24)  
引入版本：3.0.0


### enable {#enable}

#### \<static> enable(context) {#static-enablecontext}


**说明:**

启用给定上下文的图像平滑属性。 默认浏览器启用图像平滑, 这并不总是您想要的, 特别是在游戏中使用像素艺术时。 请注意, 将属性设置在上下文本身上, 这样任何绘制到上下文的图像都会受到影响 。 这将设置当前所有浏览器的属性, 但支持在先前的浏览器上, 特别是在移动上是补丁的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D \| WebGLRenderingContext | 否 | 使平滑化成为可能的上下文 。 |


**返回值:** CanvasRenderingContext2D, WebGLRenderingContext - 提供的背景。


> 源码：[src/display/canvas/Smoothing.js#L51](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L51)  
引入版本：3.0.0


### disable {#disable}

#### \<static> disable(context) {#static-disablecontext}


**说明:**

禁用给定上下文的图像平滑属性。 默认浏览器启用图像平滑, 这并不总是您想要的, 特别是在游戏中使用像素艺术时。 请注意, 将属性设置在上下文本身上, 这样任何绘制到上下文的图像都会受到影响 。 这将设置当前所有浏览器的属性, 但支持在先前的浏览器上, 特别是在移动上是补丁的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D \| WebGLRenderingContext | 否 | 禁用平滑的上下文 。 |


**返回值:** CanvasRenderingContext2D, WebGLRenderingContext - 提供的背景。


> 源码：[src/display/canvas/Smoothing.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L80)  
引入版本：3.0.0


### isEnabled {#isEnabled}

#### \<static> isEnabled(context) {#static-isenabledcontext}


**说明:**

如果上下文允许图像平滑, 返回 `true`, 否则返回 `false`。 如果无法平滑前缀, 返回无效 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| context | CanvasRenderingContext2D \| WebGLRenderingContext | 否 | 需要检查的背景 。 |


**返回值:** boolean - 如果上下文允许平滑,则使用`true`,否则使用`false`。如果不支持,则使用`null`。


> 源码：[src/display/canvas/Smoothing.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/Smoothing.js#L109)  
引入版本：3.0.0


# Phaser.Display.Canvas {#page-title-6}

### TouchAction {#TouchAction}

#### \<static> TouchAction(canvas, [value]) {#static-touchactioncanvas-value}


**说明:**

设置画布样式上的触摸动作属性。 可用于禁用默认浏览器触摸动作 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| canvas | HTMLCanvasElement | 否 |  | 应用样式的画布元素 。 |
| value | string | 是 | "'none'" | 画布上设定的触摸动作值。 设定为 `none` 以禁用触摸动作 。 |


**返回值:** HTMLCanvasElement - 画布元素.


> 源码：[src/display/canvas/TouchAction.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/TouchAction.js#L7)  
引入版本：3.0.0


### UserSelect {#UserSelect}

#### \<static> UserSelect(canvas, [value]) {#static-userselectcanvas-value}


**说明:**

设置画布样式上的用户选择属性。可用于禁用默认浏览器选择动作。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| canvas | HTMLCanvasElement | 否 |  | 应用样式的画布元素 。 |
| value | string | 是 | "'none'" | 用户选择要在画布上设定的值。 设定为 `none` 以禁用默认浏览器文本选择和触摸点名 。 |


**返回值:** HTMLCanvasElement - 画布元素.


> 源码：[src/display/canvas/UserSelect.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/canvas/UserSelect.js#L7)  
引入版本：3.0.0


# Phaser.Display.Color {#page-title-7}

### ColorSpectrum {#ColorSpectrum}

#### \<static> ColorSpectrum([limit]) {#static-colorspectrumlimit}


**说明:**

返回代表全色谱的彩色对象数组。

谱色周期通过色轮按顺序排列:红,黄,绿,青,蓝,紫,回红.

默认情况下,此函数将返回一个包含 1024 元素的数组 。

但是,如果需要,您可以通过指定 `limit` 参数来将它减少到较小的数量。当给出一个小于 1024 的限值时,颜色在全谱中均匀地取样,这样无论阵列大小,色调分布都保持统一。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| limit | number | 是 | 1024 | 返回的颜色是多少? 最多为 1024 个, 但需要时可以设定较小的颜色 。 |


**返回值:** Array.\<[Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject)> - 包含 `limit` 参数数的元素数组,其中每个元素包含一个色彩对象.


> 源码：[src/display/color/ColorSpectrum.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ColorSpectrum.js#L9)  
引入版本：3.50.0


### ColorToRGBA {#ColorToRGBA}

#### \<static> ColorToRGBA(color) {#static-colortorgbacolor}


**说明:**

将给定的颜色值转换成包含 r、g、b 和属性的对象。

颜色值可以是24位RGB整数(如`0xRRGGBB`)或32位ARGB整数(如 `0xAARRGGBB`),如果值是24位(即不超过`0xFFFFFF`),返回对象的α组件默认为255(完全不透明),否则,α从值的上8位中提取.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number | 否 | 一个24位RGB或32位ARGB的颜色整数,可选地在最显著的字节中包含一个α元件. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 包含解析的颜色值的对象。


> 源码：[src/display/color/ColorToRGBA.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ColorToRGBA.js#L7)  
引入版本：3.0.0


### ComponentToHex {#ComponentToHex}

#### \<static> ComponentToHex(color) {#static-componenttohexcolor}


**说明:**

返回包含给定颜色组件的六进制表示符的字符串。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number | 否 | 获取六进制值的颜色通道,必须是0到255之间的值. |


**返回值:** string - 长度2字符的字符串,即255=ff,100=64.


> 源码：[src/display/color/ComponentToHex.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ComponentToHex.js#L7)  
引入版本：3.0.0


### GetColor {#GetColor}

#### \<static> GetColor(red, green, blue) {#static-getcolorred-green-blue}


**说明:**

将三个独立的红,绿,蓝三个颜色成分值按0xRGGBB格式,组合成一个单一的24位整数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| red | number | 否 | 红色值,数字在0到255之间 |
| green | number | 否 | 绿色的颜色值,数字在0到255之间. |
| blue | number | 否 | 蓝色的颜色值,数字在0到255之间. |


**返回值:** number - 组合的颜色值作为0xRRGGBB格式中的24位整数.


> 源码：[src/display/color/GetColor.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/GetColor.js#L7)  
引入版本：3.0.0


### GetColor32 {#GetColor32}

#### \<static> GetColor32(red, green, blue, alpha) {#static-getcolor32red-green-blue-alpha}


**说明:**

将4个ARGB组件值(红,绿,蓝,和α)以ARGB格式包装成一个32位单数整数.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| red | number | 否 | 红色值,数字在0到255之间 |
| green | number | 否 | 绿色的颜色值,数字在0到255之间. |
| blue | number | 否 | 蓝色的颜色值,数字在0到255之间. |
| alpha | number | 否 | α颜色值,数字在 0 到 255 之间 。 |


**返回值:** number - 装箱的32位ARGB颜色值.


> 源码：[src/display/color/GetColor32.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/GetColor32.js#L7)  
引入版本：3.0.0


### HexStringToColor {#HexStringToColor}

#### \<static> HexStringToColor(hex, [color]) {#static-hexstringtocolorhex-color}


**说明:**

将六角弦转换成 Phaser 颜色对象。

十六进制字符串可以以`'#0033ff'`或`'#03f'`的短手格式提供;它可以从可选的"#"或"0x"开始,也可以不设前缀.

支持的 Alpha 频道为 _ not_ 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| hex | string | 否 | 要转换的六角星颜色值,例如`#0033ff`或短手格式:`#03f`. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 将存储新颜色的颜色。如果不定义,则返回新颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 以给定字符串的值为对象的颜色对象。


> 源码：[src/display/color/HexStringToColor.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HexStringToColor.js#L9)  
引入版本：3.0.0


### HSLToColor {#HSLToColor}

#### \<static> HSLToColor(h, s, l, [color]) {#static-hsltocolorh-s-l-color}


**说明:**

将 HSL( 色调、 饱和度和光度) 值转换为 Phaser 颜色对象 。

所有三个输入值都应该在0到1之间,如果饱和度为0,则将颜色作为色度(greyscale)处理。否则将采用标准的HSL-对RGB算法,在将每个信道下放到`HueToComponent`之前,使用光度值来得出中间q和p系数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| h | number | 否 | 0到1之间的色值. |
| s | number | 否 | 0到1之间的饱和值. |
| l | number | 否 | 0到1之间的轻度值. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 与转换值填充的可选颜色对象。如果不提供,则创建并返回新的颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 包含由给定的 h、 s 和 l 输入产生的 RGB 值的颜色对象。 或者是 `color` 参数( 如果提供的话) , 或是新创建的颜色对象 。


> 源码：[src/display/color/HSLToColor.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HSLToColor.js#L10)  
引入版本：3.0.0


### HSVColorWheel {#HSVColorWheel}

#### \<static> HSVColorWheel([s], [v]) {#static-hsvcolorwheels-v}


**说明:**

生成一个 HSV 颜色轮,作为360 色彩对象条目的数组,每度调值从 0 到 359 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| s | number | 是 | 1 | 饱和度,在0 - 1 之间. |
| v | number | 是 | 1 | 值,在0 - 1 之间. |


**返回值:** Array.\<[Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject)> - 360色彩对象元素的阵列,每个元素代表HSV色彩轮的那一色阶的RGB颜色.


> 源码：[src/display/color/HSVColorWheel.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HSVColorWheel.js#L9)  
引入版本：3.0.0


### HSVToRGB {#HSVToRGB}

#### \<static> HSVToRGB(h, s, v, [out]) {#static-hsvtorgbh-s-v-out}


**说明:**

将 HSV( 色调、 饱和度和值) 颜色设置转换为 RGB 。

[https://en.wikipedia.org/wiki/HSL_and_HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)的转换公式

假设HSV值包含在集 [0, 1] 中.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| h | number | 否 | 色调,在0 - 1 度之间,这是底色. |
| s | number | 否 | 饱和度,在0 - 1. 范围中,这控制了最终颜色中多少色调,其中1完全饱和,0会给你一个灰度的颜色. |
| v | number | 否 | 值,在0 - 1. 范围中,这控制着颜色的亮度,其中1尽可能亮,0为黑色. |
| out | [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) \| [Phaser.Display.Color](/api/namespace/display-color) | 是 | 用于存储结果的颜色对象。如果不给定新的颜色对象,则将创建 。 |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject), [Phaser.Display.Color](/api/namespace/display-color) - 对象,在 r, g 和 b 属性中设置红色,绿色和蓝色的值.


> 源码：[src/display/color/HSVToRGB.js#L30](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HSVToRGB.js#L30)  
引入版本：3.0.0


### HueToComponent {#HueToComponent}

#### \<static> HueToComponent(p, q, t) {#static-huetocomponentp-q-t}


**说明:**

从一个 hue 偏移和 HSL 到 RGB 转换期间所用的两个中间光度值计算出一个 RGB 通道值。 给每个通道( 红、 绿、 蓝) 调用一次此函数, 每次通过适当的 hue 偏移 。 基于 Michael Jackson 的代码( https://github.com/mjijackson))

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| p | number | 否 | 第一个中间值是从HSL到RGB转换期间的轻度得到的. |
| q | number | 否 | 第二个中间值是从HSL到RGB转换期间的轻度和饱和度中衍生出来的. |
| t | number | 否 | 用于计算颜色通道(红、绿或蓝色)的色调抵消。 |


**返回值:** number - 给定的hue 偏移的 RGB 通道值,在 0 到 1 之间 。


> 源码：[src/display/color/HueToComponent.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/HueToComponent.js#L7)  
引入版本：3.0.0


### IntegerToColor {#IntegerToColor}

#### \<static> IntegerToColor(input, [color]) {#static-integertocolorinput-color}


**说明:**

将给定的颜色值转换成颜色对象实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| input | number | 否 | 转换的32位整数颜色值,例如像`0xff0000`这样的六进制值表示红色. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 保存结果的可选颜色对象。如果不提供,则创建并返回新的颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 一个包含从给定整数中提取的红、绿、蓝和α组件的彩色对象。


> 源码：[src/display/color/IntegerToColor.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/IntegerToColor.js#L10)  
引入版本：3.0.0


### IntegerToRGB {#IntegerToRGB}

#### \<static> IntegerToRGB(color) {#static-integertorgbcolor}


**说明:**

返回颜色的组件部分作为对象,其属性为α,红,绿,蓝.

如果颜色值包括一个α组件(0xAARGGBB),则它会被提取并设置在`a`属性中。否则,α默认值为255(完全不透明).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number | 否 | 转换成彩色对象的颜色值。 |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - a, r, g, 和 b 属性中设定的α, 红色, 绿色, 和蓝色值的对象 。


> 源码：[src/display/color/IntegerToRGB.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/IntegerToRGB.js#L7)  
引入版本：3.0.0


### ObjectToColor {#ObjectToColor}

#### \<static> ObjectToColor(input, [color]) {#static-objecttocolorinput-color}


**说明:**

转换含有对象 `r`, `g`, `b` 财务报告和已审计财务报表 `a` 属性为颜色类实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| input | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | 否 | 含有`r`,`g`,`b`和`a`属性的天体,范围为0至255. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 将存储新颜色的颜色。如果不定义,则返回新颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 颜色对象。


> 源码：[src/display/color/ObjectToColor.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ObjectToColor.js#L9)  
引入版本：3.0.0


### RandomRGB {#RandomRGB}

#### \<static> RandomRGB([min], [max]) {#static-randomrgbmin-max}


**说明:**

创建一个新的颜色对象,其中 r、g和b 值被设定为基于给定的 min 最大值的随机值。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| min | number | 是 | 0 | 设定随机范围最小值从( 0 到 255 之间) |
| max | number | 是 | 255 | 设置随机范围的最大值( 0 到 255 之间) |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 颜色对象。


> 源码：[src/display/color/RandomRGB.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/RandomRGB.js#L10)  
引入版本：3.0.0


### RGBStringToColor {#RGBStringToColor}

#### \<static> RGBStringToColor(rgb, [color]) {#static-rgbstringtocolorrgb-color}


**说明:**

将 CSS 网络字符串转换为 Phaser 颜色对象。

网格字符串可以是r/g/b在[0.255]范围内,a在[0.1]范围内,格式为`'rgb(r,g,b)'`或`'rgba(r,g,b,a)'`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | string | 否 | CSS格式的颜色字符串,使用`rgb`或`rgba`格式. |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 包含解析值的可选颜色对象。如果不提供,则创建并返回新的颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 含有解析的 RGB 或 RGBA 值的颜色对象。


> 源码：[src/display/color/RGBStringToColor.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/RGBStringToColor.js#L9)  
引入版本：3.0.0


### RGBToHSV {#RGBToHSV}

#### \<static> RGBToHSV(r, g, b, [out]) {#static-rgbtohsvr-g-b-out}


**说明:**

将 RGB 颜色值转换为 HSV( 色调、 饱和度和值 )。 从 [http://en.wikipedia.org/wiki/HSL_color_space.](http://en.wikipedia.org/wiki/HSL_color_space.) 的 ASumes RGB 值转换公式包含在 sects [0, 255] 中, 返回 h, s 和 v 包含在 secut [0, 1] 中。 基于 Michael Jackson 的代码( https://github.com/mjijackson)Z)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| r | number | 否 | 红色值,数字在0到255之间 |
| g | number | 否 | 绿色的颜色值,数字在0到255之间. |
| b | number | 否 | 蓝色的颜色值,数字在0到255之间. |
| out | [Phaser.Types.Display.HSVColorObject](/api/typedef/types-display#hsvcolorobject) \| [Phaser.Display.Color](/api/namespace/display-color) | 是 | 将颜色值存储在其中的对象。 如果不给定 HSV 颜色对象, 将会创建 。 |


**返回值:** [Phaser.Types.Display.HSVColorObject](/api/typedef/types-display#hsvcolorobject), [Phaser.Display.Color](/api/namespace/display-color) - 具有`h`,`s`和`v`等特性的天体.


> 源码：[src/display/color/RGBToHSV.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/RGBToHSV.js#L7)  
引入版本：3.0.0


### RGBToString {#RGBToString}

#### \<static> RGBToString(r, g, b, [a], [prefix]) {#static-rgbtostringr-g-b-a-prefix}


**说明:**

将给定的红色、绿色、蓝色和α色成分值转换成六重彩色字符串。

当使用 `#` 前缀时,结果为`#rrggbb`格式的6个字符形 CSS 兼容六元字符串。此格式不包括α值。

使用`0x`前缀时,结果为`0xaarrggbb`格式的8字符串ARGB六元字符串,其中包含α元件作为最显著的字节.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| r | number | 否 |  | 红色值,数字在0到255之间 |
| g | number | 否 |  | 绿色的颜色值,数字在0到255之间. |
| b | number | 否 |  | 蓝色的颜色值,数字在0到255之间. |
| a | number | 是 | 255 | α值,数字在0到255之间. |
| prefix | string | 是 | "#" | 弦的前缀,要么是`#`,要么是`0x`. |


**返回值:** string - 以`#rrggbb`或`0xaarrggbb`格式的六角色字符串,视前缀而定.


> 源码：[src/display/color/RGBToString.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/RGBToString.js#L9)  
引入版本：3.0.0


### ValueToColor {#ValueToColor}

#### \<static> ValueToColor(input, [color]) {#static-valuetocolorinput-color}


**说明:**

将给定的源颜色值转换成颜色类实例。该值可以是字符串(前缀均不包含) `rgb` 表示已打包的 RGB 整数,或带有 `r`, `g`,和 `b` 属性。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| input | string \| number | [Phaser.Types.Display.InputColorObject](/api/typedef/types-display#inputcolorobject) | 否 | 要转换的源颜色值 。 |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 是 | 保存结果的已有颜色对象。如果不提供,则创建并返回新的颜色对象。 |


**返回值:** [Phaser.Display.Color](/api/namespace/display-color) - 包含转换的颜色值的颜色对象。


> 源码：[src/display/color/ValueToColor.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/ValueToColor.js#L12)  
引入版本：3.0.0


# Phaser.Display.Color.Interpolate {#page-title-8}

### RGBWithRGB {#RGBWithRGB}

#### \<static> RGBWithRGB(r1, g1, b1, r2, g2, b2, [length], [index]) {#static-rgbwithrgbr1-g1-b1-r2-g2-b2-length-index}


**说明:**

将两者间给定的 RGB 颜色值在所提供长度上进行国际化 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| r1 | number | 否 |  | 红色价值。 |
| g1 | number | 否 |  | 绿色价值。 |
| b1 | number | 否 |  | 蓝值. |
| r2 | number | 否 |  | 红色价值。 |
| g2 | number | 否 |  | 绿色价值。 |
| b2 | number | 否 |  | 蓝值. |
| length | number | 是 | 100 | 距离内插到那边去 |
| index | number | 是 | 0 | 索引从. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 一个包含插值的物体。


> 源码：[src/display/color/Interpolate.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L17)  
引入版本：3.0.0


### HSVWithHSV {#HSVWithHSV}

#### \<static> HSVWithHSV(h1, s1, v1, h2, s2, v2, [length], [index], [sign]) {#static-hsvwithhsvh1-s1-v1-h2-s2-v2-length-index-sign}


**说明:**

将两种给定的 HSV 颜色在所提供的长度内进行Interprotection 。 `sign` 参数控制了 hue 插值的方向: 0 找到最近的路径, 正值总是增加 hue, 负值总是减少 hue 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| h1 | number | 否 |  | 第一色的色调( 0 到 1 ) 。 |
| s1 | number | 否 |  | 初色饱和度( 0 到 1 ). |
| v1 | number | 否 |  | 第一色的值(亮度) (0比1). |
| h2 | number | 否 |  | 第二色的色调(0到1). |
| s2 | number | 否 |  | 第二色的饱和度( 0 到 1 ) 。 |
| v2 | number | 否 |  | 第二色的值( 亮度) (0 至 1 ) 。 |
| length | number | 是 | 100 | 距离内插到那边去 |
| index | number | 是 | 0 | 索引从. |
| sign | number | 是 | 0 | 色调插向. 0=最近,正数=总增,负数=总减. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 一个包含插值的物体。


> 源码：[src/display/color/Interpolate.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L55)  
引入版本：4.0.0


### ColorWithColor {#ColorWithColor}

#### \<static> ColorWithColor(color1, color2, [length], [index], [hsv], [hsvSign]) {#static-colorwithcolorcolor1-color2-length-index-hsv-hsvsign}


**说明:**

在所提供长度上将两个给定的颜色对象间插入。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color1 | [Phaser.Display.Color](/api/namespace/display-color) | 否 |  | 第一个颜色对象。 |
| color2 | [Phaser.Display.Color](/api/namespace/display-color) | 否 |  | 第二色物标. |
| length | number | 是 | 100 | 距离内插到那边去 |
| index | number | 是 | 0 | 索引从. |
| hsv | boolean | 是 | false | 是否在 HSV 中插入 。 |
| hsvSign | number | 是 | 0 | 优先使用 HSV 插值。 0 离它最近, 负数总是减少 。 负数总是增加 。 |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 一个包含插值的物体。


> 源码：[src/display/color/Interpolate.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L102)  
引入版本：3.0.0


### ColorWithRGB {#ColorWithRGB}

#### \<static> ColorWithRGB(color, r, g, b, [length], [index]) {#static-colorwithrgbcolor-r-g-b-length-index}


**说明:**

将颜色对象和颜色值之间插入到所提供长度上。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| color | [Phaser.Display.Color](/api/namespace/display-color) | 否 |  | 颜色对象 。 |
| r | number | 否 |  | 红色价值。 |
| g | number | 否 |  | 绿色价值。 |
| b | number | 否 |  | 蓝值. |
| length | number | 是 | 100 | 距离内插到那边去 |
| index | number | 是 | 0 | 索引从. |


**返回值:** [Phaser.Types.Display.ColorObject](/api/typedef/types-display#colorobject) - 一个包含插值的物体。


> 源码：[src/display/color/Interpolate.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/color/Interpolate.js#L132)  
引入版本：3.0.0

---
