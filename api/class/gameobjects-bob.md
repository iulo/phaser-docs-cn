# Bob {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-bob)

鲍勃游戏对象

一个鲍勃属于一个闪光游戏对象。闪光游戏负责管理和渲染此对象。

鲍勃从它用来渲染的纹理中具有一个位置、 α 值和一个框架。 您也可以切换鲍勃的翻转和可见状态。 鲍勃用来渲染的框架可以动态修改, 但必须是父光滑体所使用的纹理内的一个框架 。

Bob的位置相对闪电母。所以,如果你移动闪电母,所有Bob的孩子的位置也会受到这个变化的影响。

您可以直接从游戏代码中操纵Bob对象, 但是其创建和破坏应通过闪烁母程序处理.

**构造函数**

`new Bob(blitter, x, y, frame, visible)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| blitter | [Phaser.GameObjects.Blitter](/api/class/gameobjects-blitter) | 否 | 母体闪烁对象负责更新这个 Bob. |
| x | number | 否 | 相对于父光滑位置,此游戏对象在世界的横向位置. |
| y | number | 否 | 相对于父光滑位置,此游戏对象在世界的垂直位置. |
| frame | string \| number | 否 | 鲍勃将制作的框架, 其定义在父光滑器使用的纹理中 。 |
| visible | boolean | 否 | 鲍勃是应该先显身还是不要显身? |

---


**作用域**: static

> 源码：[src/gameobjects/blitter/Bob.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

鲍勃的α值,在0到1之间.

带α0的鲍勃会跳过渲染


> 源码：[src/gameobjects/blitter/Bob.js#L412](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L412)  
引入版本：3.0.0


---

### data {#data}

#### data: object {#data-object}


**说明:**

一个空白对象,可用于存储与这个鲍勃相关的数据.


> 源码：[src/gameobjects/blitter/Bob.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L81)  
引入版本：3.0.0


---

### flipX {#flipX}

#### flipX: boolean {#flipx-boolean}


**说明:**

Bob 的横向翻转状态。 横向翻转的 Bob 将反向反向反向反转。 翻转总是从纹理中间进行 。


> 源码：[src/gameobjects/blitter/Bob.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L122)  
引入版本：3.0.0


---

### flipY {#flipY}

#### flipY: boolean {#flipy-boolean}


**说明:**

Bob的垂直翻转状态。 垂直翻转的Bob会使垂直轴( 即倒转) 反转总是从纹理中间进行 。


> 源码：[src/gameobjects/blitter/Bob.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L133)  
引入版本：3.0.0


---

### frame {#frame}

#### frame: [Phaser.Textures.Frame](/api/class/textures-frame) {#frame-phasertexturesframe}


**说明:**

Bob用来制作的帧,为了改变帧,采用了`Bob.setFrame`方法.


**访问权限:** 受保护


> 源码：[src/gameobjects/blitter/Bob.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L70)  
引入版本：3.0.0


---

### parent {#parent}

#### parent: [Phaser.GameObjects.Blitter](/api/class/gameobjects-blitter) {#parent-phasergameobjectsblitter}


**说明:**

鲍勃属于的闪光物体


> 源码：[src/gameobjects/blitter/Bob.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L43)  
引入版本：3.0.0


---

### tint {#tint}

#### tint: number {#tint-number}


**说明:**

这个鲍勃的无价值


> 源码：[src/gameobjects/blitter/Bob.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L91)  
引入版本：3.20.0


---

### visible {#visible}

#### visible: boolean {#visible-boolean}


**说明:**

鲍勃的可见状态。

看不见的鲍勃会跳过渲染


> 源码：[src/gameobjects/blitter/Bob.js#L388](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L388)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

鲍勃的x位置,相对于闪光号的x位置.


> 源码：[src/gameobjects/blitter/Bob.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L52)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

鲍勃的y位置,相对于闪光器的y位置.


> 源码：[src/gameobjects/blitter/Bob.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L61)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁这个 Bob 实例。 将自己从 Blitter 中移除并清除父、 框架和数据属性 。


> 源码：[src/gameobjects/blitter/Bob.js#L370](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L370)  
引入版本：3.0.0


---

### reset {#reset}

#### \<instance> reset(x, y, [frame]) {#instance-resetx-y-frame}


**说明:**

把这个鲍勃收起来

更改给定值的位置,并选择修改帧 。

并重置 flipX和 flipY 值,将α 设定为 1 , 并可见为真 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 鲍勃的x位置. 鲍勃坐标相对闪光物体的位置. |
| y | number | 否 | 鲍勃的y位置 鲍勃坐标是相对于闪光物体的位置的 |
| frame | string \| number | [Phaser.Textures.Frame](/api/class/textures-frame) | 是 | Bob 将使用的框架。 它必须是父闪点对象所使用的纹理的一部分 。 |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L202)  
引入版本：3.0.0


---

### resetFlip {#resetFlip}

#### \<instance> resetFlip() {#instance-resetflip}


**说明:**

将这个鲍勃的横向和垂直翻转状态恢复到默认的未滑动状态.


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L186)  
引入版本：3.0.0


---

### setAlpha {#setAlpha}

#### \<instance> setAlpha(value) {#instance-setalphavalue}


**说明:**

设置此 Bob 的 Alpha 级别。 阿尔法控制游戏对象的不透明性。 Alpha 值作为浮点在 0 、 完全透明、 和 1 之间 。

带α0的鲍勃会跳过渲染

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 用于这个 Bob 的α值, 0 到 1 之间 。 |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L330)  
引入版本：3.0.0


---

### setFlip {#setFlip}

#### \<instance> setFlip(x, y) {#instance-setflipx-y}


**说明:**

设置这个鲍勃的横向和纵向翻转状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | boolean | 否 | 水平翻转状态。 `false` 用于不翻转,或者 `true` 用于翻转 。 |
| y | boolean | 否 | 垂直翻转状态。 `false` 表示不翻转,或 `true` 表示不翻转 。 |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L292](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L292)  
引入版本：3.0.0


---

### setFlipX {#setFlipX}

#### \<instance> setFlipX(value) {#instance-setflipxvalue}


**说明:**

设置这个鲍勃的横向翻转状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 翻转状态,`false`无翻转,或`true`被翻转. |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L258)  
引入版本：3.0.0


---

### setFlipY {#setFlipY}

#### \<instance> setFlipY(value) {#instance-setflipyvalue}


**说明:**

设置这个 Bob 的垂直翻转状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 翻转状态,`false`无翻转,或`true`被翻转. |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L275)  
引入版本：3.0.0


---

### setFrame {#setFrame}

#### \<instance> setFrame([frame]) {#instance-setframeframe}


**说明:**

更改此 Bob 使用的纹理帧。 框架必须是父 Blitter 使用的纹理的一部分。 如果没有给出值, 则会使用 Blitter 父的默认框架 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frame | string \| number | [Phaser.Textures.Frame](/api/class/textures-frame) | 是 | 渲染时要使用的帧 。 |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L156)  
引入版本：3.0.0


---

### setPosition {#setPosition}

#### \<instance> setPosition(x, y) {#instance-setpositionx-y}


**说明:**

将这个 Bob 的位置更改为给出的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 鲍勃的x位置. 鲍勃坐标相对闪光物体的位置. |
| y | number | 否 | 鲍勃的y位置 鲍勃坐标是相对于闪光物体的位置的 |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L239](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L239)  
引入版本：3.20.0


---

### setTint {#setTint}

#### \<instance> setTint(value) {#instance-settintvalue}


**说明:**

设置此 Bob 的颜色。 颜色是六进制的颜色值, 与 Bob 的纹理相乘, 允许您在不需要单独纹理的情况下进行颜色化 。 `0xffffff`( 白色) 的值不会使用锡。 `0xff0000` 的值会将 Bob 红色涂上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 鲍勃的锡值 0到0xffffff之间 |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L350](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L350)  
引入版本：3.20.0


---

### setVisible {#setVisible}

#### \<instance> setVisible(value) {#instance-setvisiblevalue}


**说明:**

设定这个鲍勃的能见度.

看不见的鲍勃会跳过渲染

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 游戏对象的可见状态 。 |


**返回值:** [Phaser.GameObjects.Bob](/api/class/gameobjects-bob) - 这个鲍勃游戏对象。


> 源码：[src/gameobjects/blitter/Bob.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/blitter/Bob.js#L311)  
引入版本：3.0.0


---

---
