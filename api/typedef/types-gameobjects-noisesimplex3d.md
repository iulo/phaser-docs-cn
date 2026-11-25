# Types.GameObjects.NoiseSimplex3D {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-noisesimplex3d)

## NoiseSimplex3DConfig {#noisesimplex3dconfig}

### \<static> NoiseSimplex3DConfig {#static-noisesimplex3dconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.NoiseSimplex3D.NoiseSimplex3DQuadConfig](/api/typedef/types-gameobjects-noisesimplex3d#noisesimplex3dquadconfig) | 是 |  | 此噪声Simplex3D 将使用的配置对象 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.NoiseSimplex3D
> 源码：[src/gameobjects/noise/noisesimplex3d/typedefs/NoiseSimplex3DConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex3d/typedefs/NoiseSimplex3DConfig.js#L1)  
引入版本：4.0.0

---

## NoiseSimplex3DQuadConfig {#noisesimplex3dquadconfig}

### \<static> NoiseSimplex3DQuadConfig {#static-noisesimplex3dquadconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| noiseCells | Array.\<number> | 是 | "[ 32, 32, 32 ]" | 每个维度的单元格数。 |
| noisePeriod | Array.\<number> | 是 |  | 模式重现前每个维度中有多少个单元格。默认情况下,这与`noiseCells`相同。 |
| noiseOffset | Array.\<number> | 是 | "[ 0, 0, 0 ]" | 噪音纹理的抵消 |
| noiseFlow | number | 是 | 0 | 噪音场的初始流。 利用这个来沿一个时期演化场 。 |
| noiseWarpAmount | number | 是 | 0 | 噪音场会有多少的扰动 |
| noiseIterations | number | 是 | 1 | 有多少八分之的噪音可以产生, 产生一个更详细的输出. |
| noiseWarpIterations | number | 是 | 1 | 如果`noiseWarpAmount`大于0,作为扰流作用的噪声要达到多少八分之. |
| noiseNormalMap | boolean | 是 | false | 是否将噪声转换成普通地图 。 |
| noiseNormalScale | number | 是 | 1 | 如果启用 `noiseNormalMap`, 通常地图中包含多少曲率 。 |
| noiseColorStart | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 细胞中间的颜色. |
| noiseColorEnd | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0xffffff" | 细胞边缘的颜色. |
| noiseDetailPower | number | 是 | 2 | 每八度增加详细度多少. |
| noiseFlowPower | number | 是 | 2 | 每八度增加流量多少. |
| noiseContributionPower | number | 是 | 2 | 每八进制贡献可减少多少. |
| noiseWarpDetailPower | number | 是 | 2 | 每八进制增加曲速细节多少 。 |
| noiseWarpFlowPower | number | 是 | 2 | 每八进制增加曲率流量多少 。 |
| noiseWarpContributionPower | number | 是 | 2 | 每八进制时, 曲率贡献要减少多少 。 |
| noiseValueFactor | number | 是 | 0.5 | 输出时的噪声值要缩放多少 。 |
| noiseValueAdd | number | 是 | 0.5 | 输出时的噪音值要增加多少 。 |
| noiseValuePower | number | 是 | 1 | 用于输出的噪声值的表示。 |
| noiseSeed | Array.\<number> | 是 | "[ 1, 2, 3 ]" | 散列种子。 每个种子产生不同的模式。 数字必须是整数 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.NoiseSimplex3D
> 源码：[src/gameobjects/noise/noisesimplex3d/typedefs/NoiseSimplex3DQuadConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/noisesimplex3d/typedefs/NoiseSimplex3DQuadConfig.js#L1)  
引入版本：4.0.0

---

---
