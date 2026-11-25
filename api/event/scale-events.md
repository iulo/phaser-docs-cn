# Scale.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/scale-events)

## ENTER_FULLSCREEN {#enter_fullscreen}


**说明:** 缩放管理器已成功进入全屏模式 。

**Member of:** [Phaser.Scale.Events](/api/namespace/scale-events)
> 源码：[src/scale/events/ENTER_FULLSCREEN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/events/ENTER_FULLSCREEN_EVENT.js#L7)  
引入版本：3.16.1

## FULLSCREEN_FAILED {#fullscreen_failed}


**说明:** 缩放管理器尝试进入全屏模式, 但失败 。

**Member of:** [Phaser.Scale.Events](/api/namespace/scale-events)
> 源码：[src/scale/events/FULLSCREEN_FAILED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/events/FULLSCREEN_FAILED_EVENT.js#L7)  
引入版本：3.17.0

## FULLSCREEN_UNSUPPORTED {#fullscreen_unsupported}


**说明:** Scale管理器曾尝试输入全屏模式,但浏览器不支持.

**Member of:** [Phaser.Scale.Events](/api/namespace/scale-events)
> 源码：[src/scale/events/FULLSCREEN_UNSUPPORTED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/events/FULLSCREEN_UNSUPPORTED_EVENT.js#L7)  
引入版本：3.16.1

## LEAVE_FULLSCREEN {#leave_fullscreen}


**说明:** 缩放管理器处于全屏模式,但后来离开了,要么直接通过游戏代码,
或者通过用户手势,例如按下ESC键.

**Member of:** [Phaser.Scale.Events](/api/namespace/scale-events)
> 源码：[src/scale/events/LEAVE_FULLSCREEN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/events/LEAVE_FULLSCREEN_EVENT.js#L7)  
引入版本：3.16.1

## ORIENTATION_CHANGE {#orientation_change}


**说明:** 缩放管理器方向改变事件 。

当缩放管理器从浏览器中检测到方向变化事件时,此事件会被发送 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| orientation | string | 否 | 新方向值, 要么是`Phaser.Scale.Orientation.LANDSCAPE`, 要么是`Phaser.Scale.Orientation.PORTRAIT`. |

**Member of:** [Phaser.Scale.Events](/api/namespace/scale-events)
> 源码：[src/scale/events/ORIENTATION_CHANGE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/events/ORIENTATION_CHANGE_EVENT.js#L7)  
引入版本：3.16.1

## RESIZE {#resize}


**说明:** 缩放管理器调整事件大小 。

当缩放管理器从浏览器中检测到一个调整大小的事件时,此事件会被发送.
它向调用回调发送三个参数, 每个参数都是大小组件。 您可以读取
编号 `width`, `height`, `aspectRatio` 以及这些组件的其他属性
缩放您的游戏内容。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameSize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 游戏大小组件的参考。 这是您的游戏画布的未缩放大小 。 |
| baseSize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 参考 Base Sigp 组件。 这是游戏大小 。 |
| displaySize | [Phaser.Structs.Size](/api/class/structs-size) | 否 | 引用“显示大小”组件。这是应用缩放和缩放模式后缩放的画布大小 。 |
| previousWidth | number | 否 | 如果 `gameSize` 已更改,则此值包含其先前的宽度,否则包含当前宽度. |
| previousHeight | number | 否 | 如果 `gameSize` 已改变,则此值包含其先前的高度,否则包含当前高度. |

**Member of:** [Phaser.Scale.Events](/api/namespace/scale-events)
> 源码：[src/scale/events/RESIZE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scale/events/RESIZE_EVENT.js#L7)  
引入版本：3.16.1

---
