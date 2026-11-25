# Key {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-key)

键过滤控制器 。

键效应可以去除或隔离图像中的特定颜色,可用于去除图像中的背景颜色,或者隔离特定颜色,以便进一步处理.

默认情况下, Key 将会删除匹配键颜色的像素。 您可以设置 `isolate` 来保存匹配的像素 。

阈值和羽毛设置控制了键颜色匹配的几近程度. 匹配通过"颜色矢量之间的距离"来测量;即像素的RGB值与键颜色的RGB值的距离有多近.

通过过滤列表组件向摄像机添加一个键过滤器:

```js
const camera = this.cameras.main;
camera.filters.internal.addKey({ color: '#ff00ff' });
camera.filters.external.addKey({ color: 0x00ff00 });
```

**构造函数**

`new Key(camera, [config])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机. |
| config | [Phaser.Types.Filters.KeyConfig](/api/typedef/types-filters#keyconfig) | 是 | "{}" | 过滤器的配置 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Key.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Key.js#L11)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [active](/api/class/filters-controller#active)
 - [allowBaseDraw](/api/class/filters-controller#allowBaseDraw)
 - [camera](/api/class/filters-controller#camera)
 - [currentPadding](/api/class/filters-controller#currentPadding)
 - [ignoreDestroy](/api/class/filters-controller#ignoreDestroy)
 - [paddingOverride](/api/class/filters-controller#paddingOverride)
 - [renderNode](/api/class/filters-controller#renderNode)




---

## 公开成员 {#public-members}

### color {#color}

#### color: Array.\<number> {#color-arraynumber}


**说明:**

键使用的颜色。 它是在 0 和 1 之间 的 4 个数字的阵列, 代表 RGBA 值 。


> 源码：[src/filters/Key.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Key.js#L50)  
引入版本：4.0.0


---

### feather {#feather}

#### feather: number {#feather-number}


**说明:**

键色的羽毛值。 阈值以外的像素, 但仍在羽毛内部, 将是部分匹配值。 这应该是 0 到 1 之间的值 。


> 源码：[src/filters/Key.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Key.js#L93)  
引入版本：4.0.0


---

### isolate {#isolate}

#### isolate: boolean {#isolate-boolean}


**说明:**

是否保持区域匹配键颜色。 如果选中, 匹配键颜色的区域将被保留, 其余区域将被删除。 如果错误, 匹配键色的区域将被删除, 其他区域将被保留 。


> 源码：[src/filters/Key.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Key.js#L63)  
引入版本：4.0.0


---

### threshold {#threshold}

#### threshold: number {#threshold-number}


**说明:**

键色的阈值。 如果像素和键色之间的差小于阈值, 则像素被认为是键色。 这应该是 0 到 1 之间的阈值是 1 / 16, 对于大多数图像来说, 其是一个很好的起点 。


> 源码：[src/filters/Key.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Key.js#L78)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Filters.Controller](/api/class/filters-controller):**


 - [destroy](/api/class/filters-controller#destroy)
 - [getPadding](/api/class/filters-controller#getPadding)
 - [getPaddingCeil](/api/class/filters-controller#getPaddingCeil)
 - [setActive](/api/class/filters-controller#setActive)
 - [setPaddingOverride](/api/class/filters-controller#setPaddingOverride)




---

## 公开方法 {#public-methods}

### setAlpha {#setAlpha}

#### \<instance> setAlpha(alpha) {#instance-setalphaalpha}


**说明:**

设置用于键的α值。 Alpha 控制了按键颜色匹配的像素的不透明度, 范围在 0 到 1 之间。 这一点保存在颜色阵列的第四个元素中。 RGB 颜色值被保存 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| alpha | number | 否 | 设置在键纹理上的α值,介于 0(完全透明)至 1(完全不透明)之间. |


**返回值:** [Phaser.Filters.Key](/api/class/filters-key) - 此过滤控制器 。


> 源码：[src/filters/Key.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Key.js#L108)  
引入版本：4.0.0


---

### setColor {#setColor}

#### \<instance> setColor(color) {#instance-setcolorcolor}


**说明:**

设置要用于键的颜色。此颜色存储在颜色阵列的前三个元素中。 阿尔法值被保存。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| color | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 否 | 用于键的颜色。 它可以是六进制码数或字符串, 3 个数字的阵列在 0 到 1 之间, 也可以是 color 对象 。 |


**返回值:** [Phaser.Filters.Key](/api/class/filters-key) - 此过滤控制器 。


> 源码：[src/filters/Key.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Key.js#L125)  
引入版本：4.0.0


---

---
