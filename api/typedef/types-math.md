# Types.Math {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-math)

## HashCellConfig {#hashcellconfig}

### \<static> HashCellConfig {#static-hashcellconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| algorithm | number | 是 | 0 | 使用的算法. 0是TRIG. 1是PCG. 2是PCG_FLOAT. |
| noiseCells | Array.\<number> | 是 | "[ 32, 32, 32, 32 ]" | 每个轴(XYZW)上的0-1范围单元格数。未使用的轴无需定义 。 |
| noiseWrap | boolean \| Array.\<number> | 是 | true | 是否平稳地包扎单元格。如果数字数组,单元格会在此数组之后重复。如果 `true, the wrap is set to equal `noiseCells`. |
| noiseVariation | Array.\<number> | 是 | "[ 1, 1, 1, 1 ]" | 离完美网格的单元格的变异。 不需要定义未使用的轴 。 |
| noiseIterations | number | 是 | 1 | 有多少八分之的噪音可以产生, 产生一个更详细的输出. |
| noiseMode | number | 是 | 0 | 哪个模式可渲染. 0是尖锐的边缘细胞. 1是平整的色细胞. 2是柔软的边缘细胞. |
| noiseSmoothing | number | 是 | 1 | 模式2的制式如何平滑。 |
| noiseSeed | Array.\<number> | 是 | "[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]" | 决定单元格模式的种子。不同的种子会形成完全不同的模式。您只需要与输入矢量长度(1、4、9或16)的平方相等的数字。 |

**类型**: object

**Member of**: Phaser.Types.Math
> 源码：[src/math/typedefs/HashCellConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/typedefs/HashCellConfig.js#L1)  
引入版本：4.0.0

---

## HashSimplexConfig {#hashsimplexconfig}

### \<static> HashSimplexConfig {#static-hashsimplexconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| noiseCells | Array.\<number> | 是 | "[ 32, 32, 32 ]" | 每个维度的单元格数。 |
| noisePeriod | Array.\<number> | 是 |  | 模式重现前每个维度中有多少个单元格。默认情况下,这与`noiseCells`相同。 |
| noiseFlow | number | 是 | 0 | 噪音场的初始流。 利用这个来沿一个时期演化场 。 |
| noiseWarpAmount | number | 是 | 0 | 噪音场会有多少的扰动 |
| noiseIterations | number | 是 | 1 | 有多少八分之的噪音可以产生, 产生一个更详细的输出. |
| noiseWarpIterations | number | 是 | 1 | 如果`noiseWarpAmount`大于0,作为扰流作用的噪声要达到多少八分之. |
| noiseDetailPower | number | 是 | 2 | 每八度增加详细度多少. |
| noiseFlowPower | number | 是 | 2 | 每八度增加流量多少. |
| noiseContributionPower | number | 是 | 2 | 每八进制贡献可减少多少. |
| noiseWarpDetailPower | number | 是 | 2 | 每八进制增加曲速细节多少 。 |
| noiseWarpFlowPower | number | 是 | 2 | 每八进制增加曲率流量多少 。 |
| noiseWarpContributionPower | number | 是 | 2 | 每八进制时, 曲率贡献要减少多少 。 |
| noiseSeed | Array.\<number> | 是 | "[ 1, 2, 3 ]" | 散列种子。 每个种子产生不同的模式。 数字必须是整数 。 |

**类型**: object

**Member of**: Phaser.Types.Math
> 源码：[src/math/typedefs/HashSimplexConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/typedefs/HashSimplexConfig.js#L1)  
引入版本：4.0.0

---

## RectangleLike {#rectanglelike}

### \<static> RectangleLike {#static-rectanglelike}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | ×组件. |
| y | number | 否 | y组件. |
| width | number | 否 | 宽度组件 。 |
| height | number | 否 | 高度组件。 |

**类型**: object

**Member of**: Phaser.Types.Math
> 源码：[src/math/typedefs/RectangleLike.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/typedefs/RectangleLike.js#L1)  
引入版本：3.80.0

---

## SinCosTable {#sincostable}

### \<static> SinCosTable {#static-sincostable}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sin | number | 否 | 值是正弦值 。 |
| cos | number | 否 | 余弦值(原变种). |
| length | number | 否 | 长短. |

**类型**: object

**Member of**: Phaser.Types.Math
> 源码：[src/math/typedefs/SinCosTable.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/typedefs/SinCosTable.js#L1)  
引入版本：3.0.0

---

## Vector2Like {#vector2like}

### \<static> Vector2Like {#static-vector2like}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | ×组件. |
| y | number | 否 | y组件. |

**类型**: object

**Member of**: Phaser.Types.Math
> 源码：[src/math/typedefs/Vector2Like.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/typedefs/Vector2Like.js#L1)  
引入版本：3.0.0

---

## Vector3Like {#vector3like}

### \<static> Vector3Like {#static-vector3like}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | ×组件. |
| y | number | 是 | y组件. |
| z | number | 是 | z组件. |

**类型**: object

**Member of**: Phaser.Types.Math
> 源码：[src/math/typedefs/Vector3Like.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/typedefs/Vector3Like.js#L1)  
引入版本：3.50.0

---

## Vector4Like {#vector4like}

### \<static> Vector4Like {#static-vector4like}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | ×组件. |
| y | number | 是 | y组件. |
| z | number | 是 | z组件. |
| w | number | 是 | 维元件. |

**类型**: object

**Member of**: Phaser.Types.Math
> 源码：[src/math/typedefs/Vector4Like.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/typedefs/Vector4Like.js#L1)  
引入版本：3.50.0

---

---
