# Phaser.Renderer.WebGL.RenderNodes.Defaults {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-webgl-rendernodes-defaults)

Scope: 
static
> 源码：[src/renderer/webgl/renderNodes/defaults/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/defaults/index.js#L7)  


## 静态函数 {#static-functions}

### DefaultTileSpriteNodes {#DefaultTileSpriteNodes}

#### DefaultTileSpriteNodes: Phaser.Structs.Map.\<string, string> {#defaulttilespritenodes-phaserstructsmapstring-string}


**说明:**

一张地图定义了TileSprite游戏对象在WebGL渲染器中使用的默认渲染节点.

每个条目都会将一个节点角色名称映射到负责该角色的渲染节点类的字符串标识符。这些节点在渲染管道中一起工作,处理并绘制一个 TileSprite :

- `Submitter`: 将提勒斯普里特几何提交批次绘制( )`SubmitterTileSprite`).

- `BatchHandler`:管理积聚TileSprite绘图调用(`BatchHandlerTileSprite`)的WebGL批次.

- `Transformer`:计算用于TileSprite(`TransformerTileSprite`)的世界变换矩阵.

- `Texturer`: 解析并应用TileSprite(`TexturerTileSprite`)的滚动纹理坐标.

此地图用于构建一个 TileSprite 的渲染节点图, 确保每个角色都通过适当的默认执行实现, 除非被推翻 。


> 源码：[src/renderer/webgl/renderNodes/defaults/DefaultTileSpriteNodes.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/defaults/DefaultTileSpriteNodes.js#L9)  
引入版本：3.90.0


---

---
