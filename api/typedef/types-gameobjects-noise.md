# Types.GameObjects.Noise {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-noise)

## NoiseConfig {#noiseconfig}

### \<static> NoiseConfig {#static-noiseconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | string \| [Phaser.Types.GameObjects.Noise.NoiseQuadConfig](/api/typedef/types-gameobjects-noise#noisequadconfig) | 是 |  | 此噪声将使用的配置对象 。 |
| width | number | 是 | 128 | 游戏对象的宽度 。 |
| height | number | 是 | 128 | 游戏对象的高度 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Noise
> 源码：[src/gameobjects/noise/typedefs/NoiseConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/typedefs/NoiseConfig.js#L1)  
引入版本：4.0.0

---

## NoiseQuadConfig {#noisequadconfig}

### \<static> NoiseQuadConfig {#static-noisequadconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| noiseOffset | Array.\<number> | 是 | "[ 0, 0 ]" | 噪音纹理的抵消 |
| noisePower | number | 是 |  | 噪声值的表示符。 下值去除低值; 高值去除高值 。 |
| noiseColorStart | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0x000000" | 细胞中间的颜色. |
| noiseColorEnd | number \| string | Array.\<number> | [Phaser.Display.Color](/api/namespace/display-color) | 是 | "0xffffff" | 细胞边缘的颜色. |
| noiseRandomChannels | boolean | 是 |  | 是否在每个颜色通道中随机产生噪音 。 |
| noiseRandomNormal | boolean | 是 |  | 是否随机制作出正常矢量。 这覆盖 `noiseRandomChannels` 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Noise
> 源码：[src/gameobjects/noise/typedefs/NoiseQuadConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/noise/typedefs/NoiseQuadConfig.js#L1)  
引入版本：4.0.0

---

---
