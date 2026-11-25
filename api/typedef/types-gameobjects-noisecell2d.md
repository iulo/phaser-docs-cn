# Types.GameObjects.NoiseCell2D {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-noisecell2d)

## NoiseCell2DConfig {#noisecell2dconfig}

### \<static> NoiseCell2DConfig {#static-noisecell2dconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.NoiseCell2D.NoiseCell2DQuadConfig](/api/typedef/types-gameobjects-noisecell2d#noisecell2dquadconfig) | 是 |  | 此噪声Cell2D 将使用的配置对象 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.NoiseCell2D
> 源码：[src/gameobjects/noise/noisecell2d/typedefs/NoiseCell2DConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell2d/typedefs/NoiseCell2DConfig.js#L1)  
引入版本：4.0.0

---

## NoiseCell2DQuadConfig {#noisecell2dquadconfig}

### \<static> NoiseCell2DQuadConfig {#static-noisecell2dquadconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| noiseCells | Array.\<number> | 是 | "[ 32, 32 ]" | 每个维度的单元格数。 |
| noiseWrap | Array.\<number> | 是 |  | 在模式重复之前, 每个维度中有多少个单元格。 `noiseCells`必须是整数才能正常工作。 默认情况下, 这和 `noiseCells` 相同 。 |
| noiseOffset | Array.\<number> | 是 | "[ 0, 0 ]" | 噪音纹理的抵消 |
| noiseVariation | Array.\<number> | 是 | "[ 1, 1 ]" | 细胞的变异远离完美的网格. |
| noiseIterations | number | 是 | 1 | 有多少八分之的噪音可以产生, 产生一个更详细的输出. |
| noiseMode | number | 是 | 0 | 哪个模式可渲染. 0是尖锐的边缘细胞. 1是平整的色细胞. 2是柔软的边缘细胞. |
| noiseSmoothing | number | 是 | 1 | 模式2的制式如何平滑。 |
| noiseNormalMap | boolean | 是 | false | 是否将噪声转换成普通地图 。 |
| noiseNormalScale | number | 是 | 1 | 如果启用 `noiseNormalMap`, 通常地图中包含多少曲率 。 |
| noiseColorStart | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 细胞中间的颜色. |
| noiseColorEnd | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0xffffff" | 细胞边缘的颜色. |
| noiseSeed | Array.\<number> | 是 | "[ 1, 2, 3, 4, 5, 6, 7, 8 ]" | 确定细胞模式的种子。不同的种子会形成完全不同的模式。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.NoiseCell2D
> 源码：[src/gameobjects/noise/noisecell2d/typedefs/NoiseCell2DQuadConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisecell2d/typedefs/NoiseCell2DQuadConfig.js#L1)  
引入版本：4.0.0

---

---
