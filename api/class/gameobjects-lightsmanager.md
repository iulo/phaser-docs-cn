# LightsManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-lightsmanager)

灯光管理者负责管理场景中所有[Phaser.GameObjects.Light](/api/class/gameobjects-light)对象,以及适用于所有点亮的游戏对象的环境光色.

它由景区系统自动创建,并在景区内通过`this.lights`访问. 要使用照明系统,请拨打`this.lights.enable()`,并确保任何您想要受到照明影响的游戏对象都应用`setLighting(true)`.

灯光管理器与灯光过滤器(仅限WebGL)配合工作。 游戏对象通过此过滤器对活动灯光和环境颜色进行样本, 并使用分配给其纹理的任何普通地图来产生动态照明效果。 灯光在 Canvas 渲染中没有任何效果 。

每个场景都支持固定的最大数量同时点燃的灯光,通过游戏配置中的`maxLights`属性设定. 当存在比最大灯光更多的灯光时,管理者会把每个帧距离摄像机最远的灯光堵住. 使用[Phaser.GameObjects.LightsManager#addLight](/api/class/gameobjects-lightsmanager#addLight)来创建灯光和[Phaser.GameObjects.LightsManager#setAmbientColor](/api/class/gameobjects-lightsmanager#setAmbientColor)来控制底光.


**作用域**: static

> 源码：[src/gameobjects/lights/LightsManager.js#L23](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L23)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

是否启用灯光管理器 。


> 源码：[src/gameobjects/lights/LightsManager.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L71)  
引入版本：3.0.0


---

### ambientColor {#ambientColor}

#### ambientColor: [Phaser.Display.RGB](/api/class/display-rgb) {#ambientcolor-phaserdisplayrgb}


**说明:**

环境颜色。


> 源码：[src/gameobjects/lights/LightsManager.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L62)  
引入版本：3.50.0


---

### lights {#lights}

#### lights: Array.\<[Phaser.GameObjects.Light](/api/class/gameobjects-light)> {#lights-arrayphasergameobjectslight}


**说明:**

景中灯.


> 源码：[src/gameobjects/lights/LightsManager.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L52)  
引入版本：3.0.0


---

### maxLights {#maxLights}

#### maxLights: number {#maxlights-number}


**说明:**

单个摄像机和灯光遮蔽器所能处理的最大灯光数量。 可以通过游戏配置中的 `maxLights` 属性更改此功能, 因为它无法在运行时更改 。


> 源码：[src/gameobjects/lights/LightsManager.js#L81](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L81)  
引入版本：3.15.0


---

### visibleLights {#visibleLights}

#### visibleLights: number {#visiblelights-number}


**说明:**

_前_帧处理的灯光数量.


> 源码：[src/gameobjects/lights/LightsManager.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L92)  
引入版本：3.50.0


---

## 公开方法 {#public-methods}

### addLight {#addLight}

#### \<instance> addLight([x], [y], [radius], [rgb], [intensity], [z]) {#instance-addlightx-y-radius-rgb-intensity-z}


**说明:**

创建新的 [Phaser.GameObjects.Light](/api/class/gameobjects-light) 对象, 添加到此 Lights 管理器中, 并返回它。 光会使用位于其半径内的 Light Filter 来影响所有游戏对象, 使用纹理的普通映射数据来计算阴影 。 您可以配置它的位置、 半径、 颜色、 强度和 z 高度( 影响阴影效果的角度) 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 光线的横向位置. |
| y | number | 是 | 0 | 光明的垂直位置 。 |
| radius | number | 是 | 128 | 光之半径. |
| rgb | number | 是 | "0xffffff" | 光线的整数RGB颜色. |
| intensity | number | 是 | 1 | 光之强度. |
| z | number | 是 |  | 光线的z位置。 如果省略, 将设定为 `radius * 0.1` 。 |


**返回值:** [Phaser.GameObjects.Light](/api/class/gameobjects-light) - 所加之光.


> 源码：[src/gameobjects/lights/LightsManager.js#L301](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L301)  
引入版本：3.0.0


---

### addPointLight {#addPointLight}

#### \<instance> addPointLight(x, y, [color], [radius], [intensity], [attenuation]) {#instance-addpointlightx-y-color-radius-intensity-attenuation}


**说明:**

创建新的点光游戏对象,并添加到场景中。

注意:只有在点光游戏对象已建入Phaser时,此方法才会被使用.

点光游戏对象提供了一个在你的游戏中添加点光效果的方法,而不需要传统的点光游戏对象的昂贵的遮荫处理要求.

不同之处在于点光会使用自定义的遮阳器,设计来给人以点光源的印象,在游戏中可以变的半径,强度和颜色。然而,与点光游戏对象不同,它不会影响其他任何游戏对象,或者使用普通的地图进行计算。这使得它们与灯光相比,制作速度非常快,并且适合特殊效果,例如闪烁的火炬或口袋闪光。

为了达到最大性能, 您应该将点光游戏对象进行批量。 这意味着它们可以确保显示列表中彼此连续跟踪。 理想的做法是使用一个图层游戏对象, 然后在其中添加点光, 这样它就可以将显示的灯光进行批量。 您没有_ 这样做, 如果您的游戏中只有少数点光, 那么将它们作为正常的显示列表中混合是完全安全的。 但是, 如果您使用了大量的, 请考虑它们是如何被混合到显示列表中的 。

渲染器会自动凸出点光。 半径与摄像机不相交的会跳过渲染列表。 自动发生这种情况, 并且刷新每个摄像机的凹陷状态 。

点光的起源总是0.5,不能改变.

点灯是WebGL唯一的特性,没有Canvas对应功能.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 世界上这个点光的横向位置. |
| y | number | 否 |  | 世界上这个点光的垂直位置. |
| color | number | 是 | "0xffffff" | 点光的颜色,作为六进制值给出. |
| radius | number | 是 | 128 | 点光号的半径. |
| intensity | number | 是 | 1 | 点光的强度,或颜色混合. |
| attenuation | number | 是 | 0.1 | 点光的衰减,这是从中心点的光的衰减. |


**返回值:** [Phaser.GameObjects.PointLight](/api/class/gameobjects-pointlight) - 创建的游戏对象 。


> 源码：[src/gameobjects/lights/LightsManager.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L103)  
引入版本：3.50.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

灭灭灯管理者.

清理所有参考文献,叫[Phaser.GameObjects.LightsManager#shutdown](/api/class/gameobjects-lightsmanager#shutdown)。


> 源码：[src/gameobjects/lights/LightsManager.js#L374](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L374)  
引入版本：3.0.0


---

### disable {#disable}

#### \<instance> disable() {#instance-disable}


**说明:**

禁用灯光管理器。 禁用后, 照明系统将不再影响使用灯光过滤器的游戏对象的渲染, 并有效切换到未亮的渲染。 现有的灯光和环境颜色将保留下来, 如果管理器重新启用, 将会再次生效 。


**返回值:** [Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager) - 这个灯光管理器实例 。


> 源码：[src/gameobjects/lights/LightsManager.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L171)  
引入版本：3.0.0


---

### enable {#enable}

#### \<instance> enable() {#instance-enable}


**说明:**

启用灯光管理器。 启用此功能会激活景色的照明系统, 导致所有使用灯光过滤器的游戏对象受到所配置的灯光和环境颜色的影响。 在启用时, `maxLights`值会从渲染器配置中读取 。


**返回值:** [Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager) - 这个灯光管理器实例 。


> 源码：[src/gameobjects/lights/LightsManager.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L149)  
引入版本：3.0.0


---

### getLightCount {#getLightCount}

#### \<instance> getLightCount() {#instance-getlightcount}


**说明:**

获取灯光管理器管理过的灯光数量 。


**返回值:** number - 灯光管理器管理的灯光数量.


> 源码：[src/gameobjects/lights/LightsManager.js#L288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L288)  
引入版本：3.0.0


---

### getLights {#getLights}

#### \<instance> getLights(camera) {#instance-getlightscamera}


**说明:**

获取所有可以被给定的镜头所看见的灯光.

它会自动地在镜头的世界视野之外 点燃灯光

如果返回的灯光比渲染器支持的灯光多,那么灯光就会根据距离摄像机中心的位置而被挤压,只有最接近的灯光才会被渲染.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 摄像机可以把灯光烧掉 |


**返回值:** Array.\<[Phaser.GameObjects.Light](/api/class/gameobjects-light)> - 塞灯.


> 源码：[src/gameobjects/lights/LightsManager.js#L189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L189)  
引入版本：3.50.0


---

### getMaxVisibleLights {#getMaxVisibleLights}

#### \<instance> getMaxVisibleLights() {#instance-getmaxvisiblelights}


**说明:**

返回允许同时出现的灯光的最大数量。


**返回值:** number - 允许同时出现的灯光的最大数量.


> 源码：[src/gameobjects/lights/LightsManager.js#L275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L275)  
引入版本：3.0.0


---

### removeLight {#removeLight}

#### \<instance> removeLight(light) {#instance-removelightlight}


**说明:**

从此 Lights 管理器中删除 [Phaser.GameObjects.Light](/api/class/gameobjects-light)。 该 Light 将不再影响任何游戏对象的渲染。 光本身没有被破坏; 它只是从管理器的活动列表中删除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| light | [Phaser.GameObjects.Light](/api/class/gameobjects-light) | 否 | 光照去除. |


**返回值:** [Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager) - 这个灯光管理器实例 。


> 源码：[src/gameobjects/lights/LightsManager.js#L337](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L337)  
引入版本：3.0.0


---

### setAmbientColor {#setAmbientColor}

#### \<instance> setAmbientColor(rgb) {#instance-setambientcolorrgb}


**说明:**

设置环境光色 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| rgb | number | 否 | 环境光的整数RGB颜色. |


**返回值:** [Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager) - 这个灯光管理器实例 。


> 源码：[src/gameobjects/lights/LightsManager.js#L256](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L256)  
引入版本：3.0.0


---

### shutdown {#shutdown}

#### \<instance> shutdown() {#instance-shutdown}


**说明:**

关闭灯光管理器并清除所有活动的灯光。 当场景关闭时, 自动调用。 灯光管理器可以在之后通过拨打 [Phaser.GameObjects.LightsManager#enable](/api/class/gameobjects-lightsmanager#enable)来重新启用 。


> 源码：[src/gameobjects/lights/LightsManager.js#L361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L361)  
引入版本：3.0.0


---

### sortByDistance {#sortByDistance}

#### \<instance> sortByDistance(a, b) {#instance-sortbydistancea-b}


**说明:**

排序函数以按摄像机的距离排序灯光。 排序顺序为反向, 以便最远的光先被剪切 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | number | 否 | 一个光线输入物体,带有`distance`属性,代表它与摄像机中心之间的距离. |
| b | number | 否 | 一个光线输入物体,带有`distance`属性,代表它与摄像机中心之间的距离. |


**返回值:** boolean - 如果`a`比`b`还远,否则会弄虚作假.


> 源码：[src/gameobjects/lights/LightsManager.js#L240](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsManager.js#L240)  
引入版本：4.0.0


---

---
