# Light {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-light)

一辆2D灯

这些由[Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager)创建,从场景内部通过`this.lights`提供.

任何带有照明组件的游戏对象,以及`setLighting(true)`,都会受到这些光线的影响。如果它们有普通的地图,就会使用它。如果没有,灯光会使用默认的普通地图,平面。

也可以简单地用来代表你自己的目的的点光.

灯光不能添加到容器中,它们被设计成存在于场景的根部。

**构造函数**

`new Light(x, y, radius, r, g, b, intensity, [z])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 光线的横向位置. |
| y | number | 否 | 光线的垂直位置. |
| radius | number | 否 | 光之半径. |
| r | number | 否 | 光线的红色, 值在 0 到 1 之间 。 |
| g | number | 否 | 光线的绿色,值在 0 到 1 之间 。 |
| b | number | 否 | 光线的蓝色颜色, 值在 0 到 1 之间 。 |
| intensity | number | 否 | 光的强度. |
| z | number | 是 | 光线的z位置。 如果不给定, 将设定为 `radius * 0.1` 。 |

---


**作用域**: static


**继承**

> [Phaser.Geom.Circle](/api/class/geom-circle)  
> [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/lights/Light.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L13)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [displayOriginX](/api/namespace/gameobjects-components-origin#displayOriginX)
 - [displayOriginY](/api/namespace/gameobjects-components-origin#displayOriginY)
 - [originX](/api/namespace/gameobjects-components-origin#originX)
 - [originY](/api/namespace/gameobjects-components-origin#originY)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [scrollFactorX](/api/namespace/gameobjects-components-scrollfactor#scrollFactorX)
 - [scrollFactorY](/api/namespace/gameobjects-components-scrollfactor#scrollFactorY)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [visible](/api/namespace/gameobjects-components-visible#visible)





**From [Phaser.Geom.Circle](/api/class/geom-circle):**


 - [bottom](/api/class/geom-circle#bottom)
 - [diameter](/api/class/geom-circle#diameter)
 - [left](/api/class/geom-circle#left)
 - [radius](/api/class/geom-circle#radius)
 - [right](/api/class/geom-circle#right)
 - [top](/api/class/geom-circle#top)
 - [type](/api/class/geom-circle#type)
 - [x](/api/class/geom-circle#x)
 - [y](/api/class/geom-circle#y)




---

## 公开成员 {#public-members}

### cameraFilter {#cameraFilter}

#### cameraFilter: number {#camerafilter-number}


**说明:**

如果此游戏对象是否由相机绘制, 控制此位码。 通常不直接设定, 而是直接调用 `Camera.ignore`, 但是您可以直接使用相机设置此属性 。 id 属性 :


> 源码：[src/gameobjects/lights/Light.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L115)  
引入版本：3.0.0


---

### color {#color}

#### color: [Phaser.Display.RGB](/api/class/display-rgb) {#color-phaserdisplayrgb}


**说明:**

光之色相.


> 源码：[src/gameobjects/lights/Light.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L63)  
引入版本：3.50.0


---

### displayHeight {#displayHeight}

#### displayHeight: number {#displayheight-number}


**说明:**

这个光游戏对象的高度, 这和`Light.diameter`相同 。


> 源码：[src/gameobjects/lights/Light.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L156)  
引入版本：3.60.0


---

### displayWidth {#displayWidth}

#### displayWidth: number {#displaywidth-number}


**说明:**

此 Light Game Object 的宽度, 与 `Light.diameter` 相同 。


> 源码：[src/gameobjects/lights/Light.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L135)  
引入版本：3.60.0


---

### height {#height}

#### height: number {#height-number}


**说明:**

这个光游戏对象的高度, 这和`Light.diameter`相同 。


> 源码：[src/gameobjects/lights/Light.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L198)  
引入版本：3.60.0


---

### intensity {#intensity}

#### intensity: number {#intensity-number}


**说明:**

光的强度。 缩放光效果的整体亮度。 1 值被认为是正常亮度。 更高的值会产生更强、 更亮的光 。


> 源码：[src/gameobjects/lights/Light.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L72)  
引入版本：3.50.0


---

### renderFlags {#renderFlags}

#### renderFlags: number {#renderflags-number}


**说明:**

对比 `RENDER_MASK` 的旗帜,以确定此 Light 是否渲染。 相关的位点是 0001, 由可见组件设置。 其余的位点被 Light 使用, 但需要时保留自定义使用 。


> 源码：[src/gameobjects/lights/Light.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L103)  
引入版本：3.0.0


---

### width {#width}

#### width: number {#width-number}


**说明:**

此 Light Game Object 的宽度, 与 `Light.diameter` 相同 。


> 源码：[src/gameobjects/lights/Light.js#L177](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L177)  
引入版本：3.60.0


---

### z {#z}

#### z: number {#z-number}


**说明:**

光的z位置。 这影响了光产生的解脱效果。 更高的值会让光更亮。

lit游戏对象被认为是z=0. 因此,如果z大于光的半径,光不会影响它们,强值在0到半径/2之间.

这不是一个真实的位置,也不会受到视角或相机位置的影响。它不会被设定为 `setTo`使用中选择 `setZ` 设置它,或 `setZNormal` 以设定半径的一小部分。


> 源码：[src/gameobjects/lights/Light.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L82)  
引入版本：4.0.0


---

### zNormal {#zNormal}

#### zNormal: number {#znormal-number}


**说明:**

光的z位置,作为半径的一小部分,这影响了光产生的解脱效果,更高的值会让光出现更高的亮度,强值在0到0.5之间.


> 源码：[src/gameobjects/lights/Light.js#L219](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L219)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.GameObjects.Components.Origin](/api/namespace/gameobjects-components-origin):**


 - [setDisplayOrigin](/api/namespace/gameobjects-components-origin#setDisplayOrigin)
 - [setOrigin](/api/namespace/gameobjects-components-origin#setOrigin)
 - [setOriginFromFrame](/api/namespace/gameobjects-components-origin#setOriginFromFrame)
 - [updateDisplayOrigin](/api/namespace/gameobjects-components-origin#updateDisplayOrigin)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [setScrollFactor](/api/namespace/gameobjects-components-scrollfactor#setScrollFactor)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [setVisible](/api/namespace/gameobjects-components-visible#setVisible)





**From [Phaser.Geom.Circle](/api/class/geom-circle):**


 - [contains](/api/class/geom-circle#contains)
 - [getPoint](/api/class/geom-circle#getPoint)
 - [getPoints](/api/class/geom-circle#getPoints)
 - [getRandomPoint](/api/class/geom-circle#getRandomPoint)
 - [isEmpty](/api/class/geom-circle#isEmpty)
 - [setEmpty](/api/class/geom-circle#setEmpty)
 - [setPosition](/api/class/geom-circle#setPosition)
 - [setTo](/api/class/geom-circle#setTo)




---

## 公开方法 {#public-methods}

### setColor {#setColor}

#### \<instance> setColor(rgb) {#instance-setcolorrgb}


**说明:**

从一个单整数的RGB值中设定光线的颜色。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | number | 否 | 光线的整数RGB颜色. |


**返回值:** [Phaser.GameObjects.Light](/api/class/gameobjects-light) - 此光明物.


> 源码：[src/gameobjects/lights/Light.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L257)  
引入版本：3.0.0


---

### setIntensity {#setIntensity}

#### \<instance> setIntensity(intensity) {#instance-setintensityintensity}


**说明:**

设定光的强度。 以这个尺度衡量光效果的整体亮度。 1 值被认为是正常亮度。 更高的值会产生更强、 更亮的光 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| intensity | number | 否 | 光线的强度(亮度乘数). |


**返回值:** [Phaser.GameObjects.Light](/api/class/gameobjects-light) - 此光明物.


> 源码：[src/gameobjects/lights/Light.js#L276](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L276)  
引入版本：3.0.0


---

### setRadius {#setRadius}

#### \<instance> setRadius(radius) {#instance-setradiusradius}


**说明:**

设定光线的半径, 以像素形式。 这定义了点燃的游戏对象受此光线影响的圆形影响区域 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radius | number | 否 | 光线的半径,以像素表示. |


**返回值:** [Phaser.GameObjects.Light](/api/class/gameobjects-light) - 此光明物.


> 源码：[src/gameobjects/lights/Light.js#L294](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L294)  
引入版本：3.0.0


---

### setZ {#setZ}

#### \<instance> setZ(z) {#instance-setzz}


**说明:**

设定光的z位置。 这控制了场景上方的光的感知高度, 影响降光( 正常映射阴影) 效果。 数值较大使光值出现更高。 Lit Game Objects被认为在 z=0 时, 如果 z 超过光的半径, 光不会影响它们。 强值在 0 到半径/2 之间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| z | number | 否 | 光线的z位置,其中0与点亮的游戏对象处于同一关卡. |


**返回值:** [Phaser.GameObjects.Light](/api/class/gameobjects-light) - 此光明物.


> 源码：[src/gameobjects/lights/Light.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L312)  
引入版本：4.0.0


---

### setZNormal {#setZNormal}

#### \<instance> setZNormal(z) {#instance-setznormalz}


**说明:**

将光的z位置设定为半径的一小部分。 这影响到光产生的解脱效果。 更高的值会让光的出现更高。 强值在 0 到 0. 5 之间 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| z | number | 否 | 光线的正常Z位置。 |


**返回值:** [Phaser.GameObjects.Light](/api/class/gameobjects-light) - 此光明物.


> 源码：[src/gameobjects/lights/Light.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L333)  
引入版本：4.0.0


---

### willRender {#willRender}

#### \<instance> willRender(camera) {#instance-willrendercamera}


**说明:**

将 renderMask 和 renderFlags 比较,看看此游戏对象是否渲染。 还可以根据给定的相机排除列表检查游戏对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用于检查此游戏对象的相机 。 |


**返回值:** boolean - 如果游戏对象应该被渲染, 否则会弄虚作假 。


> 源码：[src/gameobjects/lights/Light.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L241)  
引入版本：3.50.0


---

## 常量 {#constants}

## 公开成员 {#public-members-1}

### RENDER_MASK {#RENDER_MASK}

#### RENDER_MASK: number {#render_mask-number}


**说明:**

`GameObject.renderFlags` 的比特掩码用于确定游戏对象是否渲染.


> 源码：[src/gameobjects/lights/Light.js#L355](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/Light.js#L355)  



---

---
