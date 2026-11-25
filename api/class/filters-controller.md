# Controller {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-controller)

处理后过滤器效果的基类适用于相机.

滤镜是相机输出顶端的视觉效果, 如模糊、 发光或颜色分级。 每个滤镜由控制器管理, 控制器会保持其配置, 并向渲染器提供粘贴信息 。

您通常不应该直接创建此类的实例, 而是使用一个内置的过滤器来扩展它, 如 `Phaser.Filters` 命名空间中发现的 。

您不应该使用一个以上的控制器。 您想要对每个控制器应用过滤器, 请为它创建一个新实例。 如果您共享控制器, 并摧毁一个所有者, 控制器将被销毁 。

**构造函数**

`new Controller(camera, renderNode)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的摄像机。 |
| renderNode | string | 否 | 此过滤器使用的 RenderNode 的ID 。 |

---


**作用域**: static

> 源码：[src/filters/Controller.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L10)  
引入版本：4.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

切换此布尔以启用或禁用此过滤器,而不将其从相机的过滤器列表中移除并重新添加到其中 。


> 源码：[src/filters/Controller.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L34)  
引入版本：4.0.0


---

### allowBaseDraw {#allowBaseDraw}

#### allowBaseDraw: boolean {#allowbasedraw-boolean}


**说明:**

如果 `true`, 此过滤器将被允许绘制到底质。 例如, 如果过滤器没有实际绘制任何内容, 则此过滤器可能不必要 。

这是渲染器使用的内在旗帜。 您不应该直接修改此值 。


> 源码：[src/filters/Controller.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L85)  
引入版本：4.0.0


---

### camera {#camera}

#### camera: [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) {#camera-phasercamerasscene2dcamera}


**说明:**

指拥有这个过滤器的相机


> 源码：[src/filters/Controller.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L44)  
引入版本：4.0.0


---

### currentPadding {#currentPadding}

#### currentPadding: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#currentpadding-phasergeomrectangle}


**说明:**

此过滤器正在使用的粘贴。 可在渲染过程中通过 `getPadding` 读取, 并且可以通过子类执行更新。 外部列表中使用的过滤器需要更新 。 您不应该直接修改此值 。


> 源码：[src/filters/Controller.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L73)  
引入版本：4.0.0


---

### ignoreDestroy {#ignoreDestroy}

#### ignoreDestroy: boolean {#ignoredestroy-boolean}


**说明:**

此过滤器控制器是否在拥有此控制器的过滤器列表被销毁时被销毁。 如果您启用此程序, 您必须确保您在适当的时候清理过滤器控制器。 这样您就可以重新使用多个对象的控制器, 除非您知道您在做什么, 否则不推荐它。 它往往与外部过滤器一起工作。


> 源码：[src/filters/Controller.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L101)  
引入版本：4.0.0


---

### paddingOverride {#paddingOverride}

#### paddingOverride: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#paddingoverride-phasergeomrectangle}


**说明:**

铺设超重。 这是默认情况下的。 如果设置了, 过滤器会使用此铺设, 而不是计算它 。 倾向于使用 `setPaddingOverride` 而不是直接修改 。


> 源码：[src/filters/Controller.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L62)  
引入版本：4.0.0


---

### renderNode {#renderNode}

#### renderNode: string {#rendernode-string}


**说明:**

此过滤器使用的 RenderNode 的ID 。


> 源码：[src/filters/Controller.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L53)  
引入版本：4.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁此控制器并取消它所拥有的任何引用 。


> 源码：[src/filters/Controller.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L218)  
引入版本：4.0.0


---

### getPadding {#getPadding}

#### \<instance> getPadding() {#instance-getpadding}


**说明:**

返回此过滤器所需的原始粘贴。 这通常不是您想要调用的东西; 而是使用 `getPaddingCeil` 。 此方法的值不四舍五入, 会导致质量损失 。

在创建需要额外空间的过滤器时, 覆盖这种方法, 例如模糊或发光效果 。


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 此过滤器所需的粘贴 。


> 源码：[src/filters/Controller.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L117)  
引入版本：4.0.0


---

### getPaddingCeil {#getPaddingCeil}

#### \<instance> getPaddingCeil() {#instance-getpaddingceil}


**说明:**

返回此过滤器所需的四舍五入的粘贴符 。

大多数滤波器不需要额外的粘贴,但有些可能会在纹理边界之外进行采样,例如模糊或发光效果.

界限被编码为矩形。 要扩大界限, 上值和左值应该是负值, 下值和右值应该是正值 。

这种方法调用 `getPadding()` 以获取原始粘贴值,并使用 `Math.ceil()` 设置值 `paddingOverride` 财务报告和已审计财务报表 `currentPadding`.


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 此过滤器所需的圆形粘贴 。


> 源码：[src/filters/Controller.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L134)  
引入版本：4.1.0


---

### setActive {#setActive}

#### \<instance> setActive(value) {#instance-setactivevalue}


**说明:**

设置此过滤器的活跃状态。

将不使用禁用过滤器 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | `true`可以启用此过滤器,也可以使用`false`来禁用它. |


**返回值:** [Phaser.Filters.Controller](/api/class/filters-controller) - 此过滤实例 。


> 源码：[src/filters/Controller.js#L201](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L201)  
引入版本：4.0.0


---

### setPaddingOverride {#setPaddingOverride}

#### \<instance> setPaddingOverride([left], [top], [right], [bottom]) {#instance-setpaddingoverrideleft-top-right-bottom}


**说明:**

设置粘贴覆盖。 如果设置了, 过滤器会使用此粘贴而不是计算。 呼叫 `setPaddingOverride(null)` 来清除覆盖。 呼叫 `setPaddingOverride()` 来设定粘贴到 0 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| left | number \| null | 是 | 0 | 左胁贴. |
| top | number | 是 | 0 | 顶上贴. |
| right | number | 是 | 0 | 右胁贴. |
| bottom | number | 是 | 0 | 底垫. |


> 源码：[src/filters/Controller.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Controller.js#L170)  
引入版本：4.0.0


---

---
