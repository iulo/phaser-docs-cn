# Barrel {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-barrel)

弹匣过滤器控制器。

此过滤器控制器管理相机的枪管扭曲效果。 枪管效果允许您对视图应用“ pinch” 或“ 扩展” 扭曲效果。 效果的大小可以实时修改 。

透过过滤列表组件, 将Barrel效果添加到相机中:

```js
const camera = this.cameras.main;

camera.filters.internal.addBarrel();
camera.filters.external.addBarrel();
```

**构造函数**

`new Barrel(camera, [amount])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 |  | 拥有这个过滤器的相机. |
| amount | number | 是 | 1 | 用于枪管效果的扭曲量。 1 值不是扭曲值。 通常保持在+-1 内 。 |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/Barrel.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Barrel.js#L10)  
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

### amount {#amount}

#### amount: number {#amount-number}


**说明:**

扭曲的幅度适用于枪管效应。

1 的值不应用扭曲。 1 的值将视图向外扩展( 弹匣扭曲), 而 1 以下的值将视图向内压缩( 宾库希翁 扭曲 ) 。 通常将它保持在 1 的默认值的± 1 之内 。


> 源码：[src/filters/Barrel.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/Barrel.js#L44)  
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
