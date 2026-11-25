# Textures.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/textures-events)

## ADD {#add}


**说明:** 纹理添加事件.

此事件由纹理管理器在添加纹理时发出.

使用:`this.textures.on('addtexture', listener)`,从场内听这个事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 添加到纹理管理器中的纹理键. |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 提及纹理管理器中添加的纹理. |

**所属:** [Phaser.Textures.Events](/api/namespace/textures-events)
> 源码：[src/textures/events/ADD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/events/ADD_EVENT.js#L7)  
引入版本：3.0.0

## ADD_KEY {#add_key}


**说明:** 纹理添加键事件 。

当添加了给定键的纹理时,此事件由纹理管理器发出.

使用:`this.textures.on('addtexture-key', listener)`,从场内听这个事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 提及纹理管理器中添加的纹理. |

**所属:** [Phaser.Textures.Events](/api/namespace/textures-events)
> 源码：[src/textures/events/ADD_KEY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/events/ADD_KEY_EVENT.js#L7)  
引入版本：3.60.0

## ERROR {#error}


**说明:** 纹理负载错误事件 。

当纹理管理器请求加载时, 纹理管理器会发出此事件 。
只有在基数64编码纹理失败时才会发生这种情况。所有其他纹理类型都通过加载器插件加载。

使用:`this.textures.on('onerror', listener)`,从场内听这个事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 无法加载到纹理管理器的纹理键 。 |

**所属:** [Phaser.Textures.Events](/api/namespace/textures-events)
> 源码：[src/textures/events/ERROR_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/events/ERROR_EVENT.js#L7)  
引入版本：3.0.0

## LOAD {#load}


**说明:** 纹理载荷事件.

当纹理装入完毕时, 纹理管理器会发出此事件 。
这只发生在基数64编码纹理。所有其他纹理类型都通过加载器插件加载 。

使用:`this.textures.on('onload', listener)`,从场内听这个事件.

此事件在[ADD]QQLinkcode Phaser.Textures.Events#event:ADD]事件后发出.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 纹理管理器装入的纹理键 。 |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 纹理管理器装入的纹理参考文献 。 |

**所属:** [Phaser.Textures.Events](/api/namespace/textures-events)
> 源码：[src/textures/events/LOAD_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/events/LOAD_EVENT.js#L7)  
引入版本：3.0.0

## READY {#ready}


**说明:** 内部事件表明纹理管理器已经准备好了,游戏可以继续启动.

当一个 Phaser 游戏实例首次启动时, 纹理管理器必须等待一些非屏蔽
完全准备继续前的同步事件。 当完成时, 纹理管理器通过游戏发布此事件
例子,它告诉游戏继续启动。

**所属:** [Phaser.Textures.Events](/api/namespace/textures-events)
> 源码：[src/textures/events/READY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/events/READY_EVENT.js#L7)  
引入版本：3.16.1

## REMOVE {#remove}


**说明:** 纹理删除事件 。

此事件由纹理管理器在从中移除纹理时发出.

使用:`this.textures.on('removetexture', listener)`,从场内听这个事件.

如果您还有游戏对象仍然使用已删除的纹理, 它们会开始投掷
下一次尝试渲染时出错。 请确定清除此事件处理器中所有纹理的使用 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从纹理管理器中移除的纹理键. |

**所属:** [Phaser.Textures.Events](/api/namespace/textures-events)
> 源码：[src/textures/events/REMOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/events/REMOVE_EVENT.js#L7)  
引入版本：3.0.0

## REMOVE_KEY {#remove_key}


**说明:** 纹理删除键事件 。

当带给定键的纹理被移除时,此事件由纹理管理器发出.

使用:`this.textures.on('removetexture-key', listener)`,从场内听这个事件.

如果您还有游戏对象仍然使用已删除的纹理, 它们会开始投掷
下一次尝试渲染时出错。 请确定清除此事件处理器中所有纹理的使用 。

**所属:** [Phaser.Textures.Events](/api/namespace/textures-events)
> 源码：[src/textures/events/REMOVE_KEY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/events/REMOVE_KEY_EVENT.js#L7)  
引入版本：3.60.0

---
