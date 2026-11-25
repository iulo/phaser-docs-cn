# Sampler {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-sampler)

样本过滤器控制器 。

这个控制器读取了相机输出的像素数据,并将其传递给用户定义的调回。 与其他过滤器控制器不同, 样本器不会以任何方式改变已渲染的图像—— 它纯粹是一个数据提取工具。 它可以对一个单点、 矩形区域或整个相机视图进行采样, 并且对诸如采色、 像素完美检测、 或运行时间视觉分析等技术有用 。

手术很贵,请少用

通过过滤列表组件在相机中添加一个采样器:

```js
const camera = this.cameras.main;

camera.filters.internal.addSampler(callback, region);
camera.filters.external.addSampler(callback, region);
```

**构造函数**

`new Sampler(camera, callback, [region])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的摄像机。 |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 随采样者结果调用回调. |
| region | null \| [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | null | 要采样的区域。 如果 `null`, 整个相机视图都会被采样。 如果一个 `Phaser.Types.Math.Vector2Like`, 则会采样一个点。 如果一个 `Phaser.Geom.Rectangle`, 区域会被采样 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Sampler.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Sampler.js#L10)  
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

### callback {#callback}

#### callback: [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) {#callback-phasertypesrenderersnapshotsnapshotcallback}


**说明:**

调用到被采样区域读取像素数据后, 即可引用。 它收到快照结果, 这可能是一个 `HTMLImageElement` (用于区域快照)或 `Phaser.Display.Color` (指点快照),视具体情况而定 `region` 类型。


> 源码：[src/filters/Sampler.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Sampler.js#L52)  
引入版本：4.0.0


---

### region {#region}

#### region: null, [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like), [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#region-null-phasertypesmathvector2like-phasergeomrectangle}


**说明:**

要采样的区域。 如果 `null`, 整个相机视图都会被采样。 如果一个 `Phaser.Types.Math.Vector2Like`, 则会采样一个点。 如果一个 `Phaser.Geom.Rectangle`, 区域会被采样 。


> 源码：[src/filters/Sampler.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Sampler.js#L64)  
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

---
