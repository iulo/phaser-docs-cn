# Types.GameObjects.NineSlice {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-nineslice)

## NineSliceConfig {#ninesliceconfig}

### \<static> NineSliceConfig {#static-ninesliceconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 |  | 此游戏对象将使用用于渲染的纹理的键或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 |  | 游戏对象正在用此渲染的纹理的可选框架 。 |
| width | number | 是 | 256 | 九切游戏对象的宽度。 您可以调整创建后的宽度 。 |
| height | number | 是 | 256 | 九切游戏对象的高度。 如果这是 3 切片对象, 高度将固定到纹理高度, 无法更改 。 |
| leftWidth | number | 是 | 10 | 左纵列的大小(A). |
| rightWidth | number | 是 | 10 | 右垂直列的大小(B). |
| topHeight | number | 是 | 0 | 顶部的大小( C) 。 设置为 0 或未定义以创建 3 切片对象 。 |
| bottomHeight | number | 是 | 0 | 底部的大小( D) 。 设定为 0 或未定义以创建 3 切片对象 。 |
| tileX | boolean | 是 | false | 启用水平轴上的瓦片模式 。 |
| tileY | boolean | 是 | false | 启用垂直轴上的瓦片模式 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.NineSlice
> 源码：[src/gameobjects/nineslice/typedefs/NineSliceConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/nineslice/typedefs/NineSliceConfig.js#L1)  
引入版本：3.60.0

---

---
