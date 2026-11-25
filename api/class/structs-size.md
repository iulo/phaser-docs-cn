# Size {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/structs-size)

大小组件允许您设置 `width`和 `height` 属性,并定义它们之间的关系.

组件可以自动维持两个值之间的宽比,并把它们固定在定义的分钟最大范围内。您也可以控制主轴。当大小组件被赋予它,使其超过它的分钟最大范围时,则根据主轴调整尺寸。

**构造函数**

`new Size([width], [height], [aspectMode], [parent])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 0 | 大小组件的宽度 。 |
| height | number | 是 | "width" | 大小组件的高度。 如果不给出, 它将使用 `width` 。 |
| aspectMode | number | 是 | 0 | 大小组件的侧面模式。默认为 0, 没有模式 。 |
| parent | any | 是 | null | 此大小组件的父部分。 可以是任何具有公共 `width` 和 `height` 属性的天体。 尺寸被夹住, 尽可能将其保留在父部分的内 。 |

---


**作用域**: static

> 源码：[src/structs/Size.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L12)  
引入版本：3.16.0

## 公开成员 {#public-members}

### aspectMode {#aspectMode}

#### aspectMode: number {#aspectmode-number}


**说明:**

此大小组件在计算其尺寸时将使用的侧面模式。 此属性只读。 要更改它, 使用 `setAspectMode` 方法 。


> 源码：[src/structs/Size.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L71)  
引入版本：3.16.0


---

### aspectRatio {#aspectRatio}

#### aspectRatio: number {#aspectratio-number}


**说明:**

宽度和高度之间的比例关系.

此属性只读,在`width`或`height`属性被改变时会自动更新,视侧面模式而定.


> 源码：[src/structs/Size.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L82)  
引入版本：3.16.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

此大小组件的高度 。

如果启用, 此值会被夹在 `minHeight` 和 `maxHeight` 指定的范围 。

高度永远不能小于零.

如果启用宽比锁定, 更改此值将自动更新 `width`。 您也可以使用 `setHeight` 方法 。


> 源码：[src/structs/Size.js#L692](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L692)  
引入版本：3.16.0


---

### maxHeight {#maxHeight}

#### maxHeight: number {#maxheight-number}


**说明:**

允许的最大高度。 此值只读。 要更改它, 请看到 `setMax` 方法 。


> 源码：[src/structs/Size.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L130)  
引入版本：3.16.0


---

### maxWidth {#maxWidth}

#### maxWidth: number {#maxwidth-number}


**说明:**

允许的最大宽度。 此值只读。 要更改它, 请查看 `setMax` 方法 。


> 源码：[src/structs/Size.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L119)  
引入版本：3.16.0


---

### minHeight {#minHeight}

#### minHeight: number {#minheight-number}


**说明:**

允许的最小高度。 不可小于零。 此值只读, 要更改它, 请看到 `setMin` 方法 。


> 源码：[src/structs/Size.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L107)  
引入版本：3.16.0


---

### minWidth {#minWidth}

#### minWidth: number {#minwidth-number}


**说明:**

允许最小宽度。 不可小于零。 此值只读, 要更改它, 请看到 `setMin` 方法 。


> 源码：[src/structs/Size.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L95)  
引入版本：3.16.0


---

### snapTo {#snapTo}

#### snapTo: [Phaser.Math.Vector2](/api/class/math-vector2) {#snapto-phasermathvector2}


**说明:**

含有水平和垂直坐标值的矢量2,宽度和高度在调整大小时会断裂。

默认此选项已禁用 。

此属性只读。 要更改它, 请查看 `setSnap` 方法 。


> 源码：[src/structs/Size.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L141)  
引入版本：3.16.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此大小组件的宽度 。

如果启用, 此值会被夹在 `minWidth` 和 `maxWidth` 指定的范围 。

宽度永远不能小于零.

如果启用宽比锁定, 更改此值将自动更新 `height`。 您也可以使用 `setWidth` 方法 。


> 源码：[src/structs/Size.js#L664](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L664)  
引入版本：3.16.0


---

## 公开方法 {#public-methods}

### constrain {#constrain}

#### \<instance> constrain([width], [height], [fit]) {#instance-constrainwidth-height-fit}


**说明:**

目前`width`和`height`调整,以适应给定维度,同时保持宽度比.

如果 `fit` 是真的, 如果其侧面比不同, 目标区域内可能有一些空间没有覆盖。 如果 `fit` 是假的, 如果侧面比不同, 该大小可能会比目标区域进一步扩大 。

如果此大小组件有父集, 那么将夹住此方法的宽度和高度, 使其不能超过父集 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 0 | 大小组件的新宽度 。 |
| height | number | 是 |  | 大小组件的新高度。 如果不给出, 它将使用宽度值 。 |
| fit | boolean | 是 | true | 执行`fit`(真)约束,或`envelop`(假)约束。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L452](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L452)  
引入版本：3.16.0


---

### copy {#copy}

#### \<instance> copy(destination) {#instance-copydestination}


**说明:**

复制从此大小组件到给定大小组件的侧面模式、 宽度和高度。 请注意, 如果设定了父部分, 则不会被复制到整个组件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| destination | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 将数值复制到的大小组件 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 更新的目标大小组件 。


> 源码：[src/structs/Size.js#L628](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L628)  
引入版本：3.16.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此大小组件。

此选项清除本地属性和任何父对象, 如果设置的话 。

无法重用已销毁的大小组件 。


> 源码：[src/structs/Size.js#L648](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L648)  
引入版本：3.16.0


---

### envelop {#envelop}

#### \<instance> envelop([width], [height]) {#instance-envelopwidth-height}


**说明:**

目前的`width`和`height`进行了调整,以便它们完全包罗给定的维度,同时保持宽度比.

如果方方面面比率不同,其规模可能比目标区域更远。

如果此大小组件有父集, 那么会将值夹住, 以便它不会超过最长轴上的父集 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 0 | 大小组件的新宽度 。 |
| height | number | 是 |  | 大小组件的新高度。 如果不给出, 它将使用宽度值 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L542](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L542)  
引入版本：3.16.0


---

### fitTo {#fitTo}

#### \<instance> fitTo([width], [height]) {#instance-fittowidth-height}


**说明:**

目前`width`和`height`调整,以适应给定维度,同时保持宽度比.

如果目标区域内方圆比不同,则可能有一些空间没有覆盖。

如果此大小组件有父集, 那么将夹住此方法的宽度和高度, 使其不能超过父集 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 0 | 大小组件的新宽度 。 |
| height | number | 是 |  | 大小组件的新高度。 如果不给出, 它将使用宽度值 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L521](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L521)  
引入版本：3.16.0


---

### getNewHeight {#getNewHeight}

#### \<instance> getNewHeight(value, [checkParent]) {#instance-getnewheightvalue-checkparent}


**说明:**

取一个新的高度,然后通过分/最大夹,然后检查它不会超过母高.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 夹住和检查的值 。 |
| checkParent | boolean | 是 | true | 如果设定, 请对照父方检查给定的值 。 |


**返回值:** number - 修改的高度值 。


> 源码：[src/structs/Size.js#L427](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L427)  
引入版本：3.16.0


---

### getNewWidth {#getNewWidth}

#### \<instance> getNewWidth(value, [checkParent]) {#instance-getnewwidthvalue-checkparent}


**说明:**

取一个新的宽度,然后通过分/最大夹,然后检查它不会超过母宽.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 夹住和检查的值 。 |
| checkParent | boolean | 是 | true | 如果设定, 请对照父方检查给定的值 。 |


**返回值:** number - 修改宽度值 。


> 源码：[src/structs/Size.js#L402](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L402)  
引入版本：3.16.0


---

### resize {#resize}

#### \<instance> resize(width, [height]) {#instance-resizewidth-height}


**说明:**

设置此大小组件的新宽度和高度,并在此基础上更新宽度比。

它不会_ doesn_改变`aspectMode`,并且仍然会改变大小限制的因子,如min max和父边界.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 否 |  | 大小组件的新宽度 。 |
| height | number | 是 | "width" | 大小组件的新高度。 如果不给出, 它将会使用 `width` 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L380](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L380)  
引入版本：3.16.0


---

### setAspectMode {#setAspectMode}

#### \<instance> setAspectMode([value]) {#instance-setaspectmodevalue}


**说明:**

设置此大小组件的侧面模式。

侧面模式控制着修改`width`或`height`属性时发生的情况,或者调用`setSize`.

它可以是从0到4的数字,也可以是大小常数:

0. None = 不使大小符合宽度比。大小变化时改变比例。

1. WIDTH_CONTROLS_HEIGHT = 高度根据宽度自动调整.

2. HEGHT_CONTROLS_WIDTH = 宽度根据高度自动调整.

3. FIT = 宽度和高度自动调整,以适应给定目标区域,同时保持宽度比,视宽度比而定,在未覆盖区域内可能有一些空间.

4. ENVELOP = 宽度和高度自动调整,使大小覆盖整个目标区域,同时保持宽度比,这可能会比目标大小更远.

必要时,调用这种方法会自动重新计算`width`和`height`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 侧面模式值 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L156)  
引入版本：3.16.0


---

### setAspectRatio {#setAspectRatio}

#### \<instance> setAspectRatio(ratio) {#instance-setaspectratioratio}


**说明:**

设置一个新的宽度比, 压倒以前的水平 。

然后它立即使用当前维度调用`setSize`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ratio | number | 否 | 新的宽度比。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L361)  
引入版本：3.16.0


---

### setCSS {#setCSS}

#### \<instance> setCSS(element) {#instance-setcsselement}


**说明:**

将这个大小组件的值设定为给定 DOM 元素的 `element.style.width` 和 `height` 属性。属性设定为 `px` 值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| element | HTMLElement | 否 | 设置 CSS 样式的 DOM 元素 。 |


> 源码：[src/structs/Size.js#L610](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L610)  
引入版本：3.17.0


---

### setHeight {#setHeight}

#### \<instance> setHeight(value) {#instance-setheightvalue}


**说明:**

设置此大小组件的高度。

根据侧面模式,改变高度也可能更新宽度和侧面比.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 大小组件的新高度 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L580](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L580)  
引入版本：3.16.0


---

### setMax {#setMax}

#### \<instance> setMax([width], [height]) {#instance-setmaxwidth-height}


**说明:**

设定大小组件允许的最大宽度和高度值 。

设置此选项将自动调整 `width` 和 `height` 两种属性,以确保它们都在射程内 。

注意基于侧面模式,如果此大小组件是否有父集,则在此设置的最大值_可_在某些情况下被超越 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | "Number.MAX_VALUE" | 大小组件的最大允许宽度 。 |
| height | number | 是 | "width" | 大小组件的最大允许高度。 如果不给出, 则会使用 `width` 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L276)  
引入版本：3.16.0


---

### setMin {#setMin}

#### \<instance> setMin([width], [height]) {#instance-setminwidth-height}


**说明:**

设定大小组件允许的最小宽度和高度值 。

最小值永远不能低于零,或者大于最大值.

设置此选项将自动调整 `width` 和 `height` 两种属性,以确保它们都在射程内 。

注意基于侧面模式,如果此大小组件是否有父集,则在此设置的最小值_可_在某些情况下被超越 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 0 | 最小允许宽度大小组件 。 |
| height | number | 是 | "width" | 大小组件的最小允许高度。 如果不给出, 它会使用 `width` 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L247)  
引入版本：3.16.0


---

### setParent {#setParent}

#### \<instance> setParent([parent]) {#instance-setparentparent}


**说明:**

设置,或清除此大小组件的母部分 。

清除父程序时, 无需参数即可使用这种方法 。

父影响此大小组件的最大范围, 以侧面模式为基础 :

None - 母端夹宽度和高度。 WIDTH_ CONTROLS_HEIGH - 母端夹长度。 HEIGH_ CONTRORS_ WIDTH - 母端紧紧夹高度。 FIT - 母端夹短度按需要以何种轴键确保大小符合其内部。 ENVELOP - 母端用于确保大小完全包围父端 。

使用这种方法自动使用`setSize`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | any | 是 | 设置此大小组件的父部分。 不要为清除已有的父部分提供值 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L217](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L217)  
引入版本：3.16.0


---

### setSize {#setSize}

#### \<instance> setSize([width], [height]) {#instance-setsizewidth-height}


**说明:**

根据侧面模式设定此大小组件的宽度和高度。

如果侧面模式是“ 无” , 那么调用此方法会改变侧面比, 否则当前侧面比会被其他所有模式所遵守 。

如果设定了 snapTo 值,那么在通过分/最大值或母体进行任何进一步调整之前,先将给定的宽度和高度断裂。

如果指定了最小和/或最大尺寸,则在调整前将把给予这种方法的值夹入该范围,但可能仍然会超过这些值,取决于方方面面模式。

如果此大小组件有父集, 且侧面模式为 `fit` 或 `envelop`, 那么给定的大小将被夹在父集指定的范围 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 0 | 大小组件的新宽度 。 |
| height | number | 是 | "width" | 大小组件的新高度。 如果不给出, 它将会使用 `width` 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L303](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L303)  
引入版本：3.16.0


---

### setSnap {#setSnap}

#### \<instance> setSnap([snapWidth], [snapHeight]) {#instance-setsnapsnapwidth-snapheight}


**说明:**

通过设置坐标值, 当修改大小组件时, 其尺寸会自动被折断到最近的网格切片, 使用下限。 例如, 如果您的坐标值为 16, 宽度会变为 68, 那么它会被折断到 64 ( 下限时为 16 的最近倍数 )

注意在母调整或最小/ 最大设置之前进行抓取。 如果这些值不是给定抓取值的倍数, 则可能导致未抓取的维数 。

使用此方法不设参数来重设坐标值 。

必要时,调用这种方法会自动重新计算`width`和`height`.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| snapWidth | number | 是 | 0 | 宽度的大小。 如果您不想宽度的大小, 则通过 0 值 。 |
| snapHeight | number | 是 | "snapWidth" | 将高度调高到的数值。 如果不提供, 它将使用 `snapWidth` 值。 如果您不想调高, 请通过 0 值 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L187)  
引入版本：3.16.0


---

### setWidth {#setWidth}

#### \<instance> setWidth(value) {#instance-setwidthvalue}


**说明:**

设置此大小组件的宽度。

根据侧面模式,改变宽度也可能更新高度和侧面比.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 大小组件的新宽度 。 |


**返回值:** [Phaser.Structs.Size](/api/class/structs-size) - 此大小组件实例 。


> 源码：[src/structs/Size.js#L563](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L563)  
引入版本：3.16.0


---

### toString {#toString}

#### \<instance> toString() {#instance-tostring}


**说明:**

返回此大小组件的字符串表示符。


**返回值:** string - 此大小组件的字符串表示 。


> 源码：[src/structs/Size.js#L597](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L597)  
引入版本：3.16.0


---

## 常量 {#constants}

## 公开成员 {#public-members-1}

### ENVELOP {#ENVELOP}

#### ENVELOP: number {#envelop-number}


**说明:**

宽度和高度会自动调整, 使大小覆盖整个目标区域, 同时保持宽度比。 这可能会比目标大小更远 。


> 源码：[src/structs/Size.js#L762](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L762)  
引入版本：3.16.0


---

### FIT {#FIT}

#### FIT: number {#fit-number}


**说明:**

宽度和高度会自动调整,以适应给定目标区域,同时保持宽度比。视宽度比而定,在区域内可能有一些空间没有覆盖。


> 源码：[src/structs/Size.js#L752](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L752)  
引入版本：3.16.0


---

### HEIGHT_CONTROLS_WIDTH {#HEIGHT_CONTROLS_WIDTH}

#### HEIGHT_CONTROLS_WIDTH: number {#height_controls_width-number}


**说明:**

宽度根据高度自动调整.


> 源码：[src/structs/Size.js#L742](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L742)  
引入版本：3.16.0


---

### NONE {#NONE}

#### NONE: number {#none-number}


**说明:**

不要使大小符合侧面比。大小变化时改变比例。


> 源码：[src/structs/Size.js#L722](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L722)  
引入版本：3.16.0


---

### WIDTH_CONTROLS_HEIGHT {#WIDTH_CONTROLS_HEIGHT}

#### WIDTH_CONTROLS_HEIGHT: number {#width_controls_height-number}


**说明:**

高度根据宽度自动调整.


> 源码：[src/structs/Size.js#L732](https://github.com/phaserjs/phaser/blob/v4.1.0/src/structs/Size.js#L732)  
引入版本：3.16.0


---

---
