# Blocky {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-blocky)

布莱基过滤器控制器。

此过滤器控制器管理一个块状效果 。

块状效果通过取块状像素的中央像素,并用它来填充整个块,从而产生像素化的效果.

它降低了图像的分辨率,创造了像素或块状的外观,这经常用于像素艺术等结构化目的. 一种技术是使游戏在更高分辨率,以N的因子缩放,然后在大小 N 上应用块状效果. 这创造了大,可见的像素,适合进一步分层化,效果也可以用来遮蔽游戏中的某些元素,比如在过渡期间或者检查特定内容.

Blocky在游戏上最擅长无反异名,因此它可以从原始图像中读取未过滤的像素颜色,它保存了原始艺术的颜色,而不是像像像素素滤镜那样混合.

通过过滤列表组件将一个块状效果添加到摄像机中:

```js
const camera = this.cameras.main;
camera.filters.internal.addBlocky({ size: 4 });
camera.filters.external.addBlocky({ size: { x: 2, y: 4 }, offset: { x: 1, y: 2 } });
```

**构造函数**

`new Blocky(camera, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的摄像机。 |
| config | [Phaser.Types.Filters.BlockyConfig](/api/typedef/types-filters#blockyconfig) | 是 | Blocky 效果的配置对象 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Blocky.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blocky.js#L10)  
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

### offset {#offset}

#### offset: [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) {#offset-phasertypesmathvector2like}


**说明:**

图像左上角的块的偏移 。


> 源码：[src/filters/Blocky.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blocky.js#L72)  
引入版本：4.0.0


---

### size {#size}

#### size: [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) {#size-phasertypesmathvector2like}


**说明:**

块的大小。 您可以将 x 和 y 值设定为任意数字, 但过滤器将限制最小值为 1 。


> 源码：[src/filters/Blocky.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Blocky.js#L57)  
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
