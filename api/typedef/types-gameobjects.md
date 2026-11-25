# Types.GameObjects {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects)

## DecomposeMatrixResults {#decomposematrixresults}

### \<static> DecomposeMatrixResults {#static-decomposematrixresults}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| translateX | number | 否 | 翻译的 x 值 。 |
| translateY | number | 否 | 翻译的y值. |
| rotation | number | 否 | 旋转值. |
| scaleX | number | 否 | 缩放 x 值 。 |
| scaleY | number | 否 | 缩放 y 值 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects
> 源码：[src/gameobjects/typedefs/DecomposeMatrixResults.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/DecomposeMatrixResults.js#L1)  
引入版本：3.60.0

---

## FiltersInternalExternal {#filtersinternalexternal}

### \<static> FiltersInternalExternal {#static-filtersinternalexternal}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| internal | [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist) | 否 | 游戏对象的内部过滤列表。这些过滤器首先应用在游戏对象的本地空间中。 |
| external | [Phaser.GameObjects.Components.FilterList](/api/class/gameobjects-components-filterlist) | 否 | 游戏对象的外部过滤列表。 这些过滤器是最后应用的, 位于游戏对象的母空间 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects
> 源码：[src/gameobjects/typedefs/FiltersInternalExternal.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/FiltersInternalExternal.js#L1)  
引入版本：4.0.0

---

## GameObjectConfig {#gameobjectconfig}

### \<static> GameObjectConfig {#static-gameobjectconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number \| object | 是 | 0 | 游戏对象的x位置. |
| y | number \| object | 是 | 0 | 游戏对象的y位置 。 |
| depth | number | 是 | 0 | 游戏对象的深度 。 |
| flipX | boolean | 是 | false | 游戏对象的横向翻转状态 。 |
| flipY | boolean | 是 | false | 游戏对象的垂直翻转状态 。 |
| scale | number \| object | 是 | null | 游戏对象的尺度 。 |
| scrollFactor | number \| object | 是 | null | 游戏对象的滚动因子 。 |
| rotation | number \| object | 是 | 0 | 游戏对象的旋转角度,以弧度表示. |
| angle | number \| object | 是 | null | 游戏对象的旋转角度, 以度计 。 |
| alpha | number \| object | 是 | 1 | 游戏对象的α( opacity) 。 |
| origin | number \| object | 是 | null | 游戏对象的起源 。 |
| scaleMode | number | 是 | "ScaleModes.DEFAULT" | 游戏对象的缩放模式 。 |
| blendMode | number | 是 | "BlendModes.DEFAULT" | 游戏对象的混合模式 。 |
| visible | boolean | 是 | true | 游戏对象的可见状态 。 |
| add | boolean | 是 | true | 将游戏对象添加到现场 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects
> 源码：[src/gameobjects/typedefs/GameObjectConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/GameObjectConfig.js#L1)  
引入版本：3.0.0

---

## GetCalcMatrixResults {#getcalcmatrixresults}

### \<static> GetCalcMatrixResults {#static-getcalcmatrixresults}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| cameraExternal | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 计算出的相机外部矩阵(相机在屏幕上的地方). |
| camera | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 计算出的相机视图矩阵,包括经滚动因子修改的卷轴. |
| sprite | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 计算出的Sprite( Game 对象) 矩阵( 世界位置) 。 |
| calc | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 否 | 计算结果矩阵,将所有其他结果都计入在内。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects
> 源码：[src/gameobjects/typedefs/GetCalcMatrixResults.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/GetCalcMatrixResults.js#L1)  
引入版本：3.50.0

---

## JSONGameObject {#jsongameobject}

### \<static> JSONGameObject {#static-jsongameobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| 名称 | string | 否 | 此游戏对象的名称 。 |
| 类型 | string | 否 | 此游戏对象的文字表达,即`sprite`. |
| x | number | 否 | 此游戏对象的 x 位置 。 |
| y | number | 否 | 此游戏对象的y 位置 。 |
| scale | object | 否 | 此游戏对象的大小 |
| scale.x | number | 否 | 此游戏对象的横向尺度 。 |
| scale.y | number | 否 | 此游戏对象的垂直尺度 。 |
| origin | object | 否 | 此游戏对象的起源 。 |
| origin.x | number | 否 | 此游戏对象的横向来源 。 |
| origin.y | number | 否 | 此游戏对象的垂直源头 。 |
| flipX | boolean | 否 | 游戏对象的横向翻转状态 。 |
| flipY | boolean | 否 | 游戏对象的垂直翻转状态 。 |
| rotation | number | 否 | 弧度中的此游戏对象角度 。 |
| alpha | number | 否 | 游戏对象的α值 。 |
| visible | boolean | 否 | 游戏对象的可见状态 。 |
| scaleMode | number | 否 | 此游戏对象正在使用的缩放模式 。 |
| blendMode | number \| string | 否 | 设置此游戏对象正在使用的混合模式。 |
| textureKey | string | 否 | 此游戏对象的纹理密钥 。 |
| frameKey | string | 否 | 此游戏对象的帧键 。 |
| data | object | 否 | 此游戏对象的数据 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects
> 源码：[src/gameobjects/typedefs/JSONGameObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/JSONGameObject.js#L1)  
引入版本：3.0.0

---

## RenderWebGLStep {#renderwebglstep}

### \<static> RenderWebGLStep {#static-renderwebglstep}


执行给定的游戏对象上的渲染操作的函数 。
这通常是游戏对象本身的`renderWebGL`方法,
但是 `Phaser.GameObjects.Components.RenderSteps`允许您定义
一系列按顺序运行的步骤。
该职能预计不会在任何特定范围内运作,
因此,它不应使用`this`。相反,所有所需的属性都应该是
通过`gameObject`访问.

**类型**: function

**Member of**: Phaser.Types.GameObjects
> 源码：[src/gameobjects/typedefs/RenderWebGLStep.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/typedefs/RenderWebGLStep.js#L1)  
引入版本：4.0.0

---

---
