# Types.GameObjects.Sprite {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-sprite)

## SpriteConfig {#spriteconfig}

### \<static> SpriteConfig {#static-spriteconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| frame | string \| number | 是 | 游戏对象正在用此渲染的纹理的可选框架 。 |
| anims | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 是 | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| useSpriteSheet | boolean | 是 | 此属性完全由 `Tilemap.createFromTiles` 使用。 如果此 Sprite 是由 Tilemap 创建, 并且是 spriteshet 的一部分, 则设置为 `true` 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Sprite
> 源码：[src/gameobjects/sprite/typedefs/SpriteConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/sprite/typedefs/SpriteConfig.js#L1)  
引入版本：3.0.0

---

---
