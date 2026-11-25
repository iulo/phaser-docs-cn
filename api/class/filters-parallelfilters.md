# ParallelFilters {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/filters-parallelfilters)

平行过滤控制器 。

这个过滤控制器将输入分为两个过滤列表,分别运行每个列表,然后将结果混合在一起.

并行过滤器效果对重用输入很有用。 通常情况下, 过滤器会修改输入并传递到下一个过滤器。 这种效果允许您在其它地方分割输入并重用。 它不会从并行处理中获得性能好处; 它是重用输入的便利 。

平行过滤器效果本身不是过滤器。 它是管理两个过滤器的控件, 也是将结果组合在一起的最后一个混合过滤器。 过滤器列表被命名为“ 顶” 和“ 底” 。 “ 顶” 输出被应用为“ 底” 输出的混合纹理 。

您不必填充两个列表。 如果只包含一个列表, 则它将被与结尾的原始输入混合。 如果您想要保留在过滤过程中丢失的图像数据, 这样做将很有用 。

通过过滤列表组件,将一个平行过滤器效果添加到摄像机中:

```js
const camera = this.cameras.main;
camera.filters.internal.addParallelFilters();
camera.filters.external.addParallelFilters();
```

**构造函数**

`new ParallelFilters(camera)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 拥有这个过滤器的摄像机. |

---


**作用域**: static


**继承**

> [Phaser.Filters.Controller](/api/class/filters-controller)  



> 源码：[src/filters/ParallelFilters.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ParallelFilters.js#L12)  
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

### blend {#blend}

#### blend: [Phaser.Filters.Blend](/api/class/filters-blend) {#blend-phaserfiltersblend}


**说明:**

将上下过滤器输出合成一个结果的混合过滤器控制器。 它是一个标准的 [Phaser.Filters.Blend](/api/class/filters-blend)控制器, 可以配置其混合模式和量来控制两种输出的组合。 更多信息请参见 [Phaser.Filters.Blend](/api/class/filters-blend) 。

混合控制器的`texture`属性将在渲染过程中被覆盖.


> 源码：[src/filters/ParallelFilters.js#L91](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ParallelFilters.js#L91)  
引入版本：4.0.0


---

### bottom {#bottom}

#### bottom: [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist) {#bottom-phasergameobjectscomponentsfilterlist}


**说明:**

底部过滤列表。 添加到此列表的过滤器接收原始输入, 并且独立于顶部列表进行处理。 此列表的最终输出将作为由 Blend 控制器混合顶部输出的基础图像 。


> 源码：[src/filters/ParallelFilters.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ParallelFilters.js#L79)  
引入版本：4.0.0


---

### top {#top}

#### top: [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist) {#top-phasergameobjectscomponentsfilterlist}


**说明:**

上部 FilterList。 添加到此列表的过滤器接收原始输入, 并独立于下部列表进行处理。 此列表的最终输出会作为混合纹理传递给 Blend 控制器, 然后将它合成到下部输出 。


> 源码：[src/filters/ParallelFilters.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/filters/ParallelFilters.js#L67)  
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
