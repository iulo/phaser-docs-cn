# Types.GameObjects.Rope {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-rope)

## RopeConfig {#ropeconfig}

### \<static> RopeConfig {#static-ropeconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 是 |  | 此游戏对象将使用的纹理键用于渲染, 如保存在纹理管理器中。 如果不给出, 则使用 `__DEFAULT` 。 |
| frame | string \| integer | null | 是 |  | 游戏对象正在用此渲染的纹理的可选框架 。 |
| points | integer \| Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 是 | 2 | 包含此绳索的顶点数据的数组, 或表示要将纹理帧分割成多少段的数组。 如果未提供, 则创建一个简单的四边形。 请参见 `setPoints` 设置此创建后 。 |
| horizontal | boolean | 是 | true | 这个绳子的顶点应水平对齐(`true`),还是垂直对齐(`false`)? |
| colors | Array.\<number> | 是 |  | 包含此绳索的颜色数据的可选数组。 您应该提供每对顶点一个颜色值 。 |
| alphas | Array.\<number> | 是 |  | 包含此绳索的α数据的可选数组。 您应该提供每对顶点一个α值 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Rope
> 源码：[src/gameobjects/rope/typedefs/RopeConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/rope/typedefs/RopeConfig.js#L1)  
引入版本：3.50.0

---

---
