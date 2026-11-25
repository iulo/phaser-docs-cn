# Input.Gamepad.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/input-gamepad-events)

## BUTTON_DOWN {#button_down}


**说明:** 游戏板扣子下架事件.

当任何正在运行的 Gamepad 上按下按钮时,此事件由 Gamepad 插件发送 。

使用:`this.input.gamepad.on('down', listener)`,从场内听这个事件.

您也可以从 Gamepad 实例中收听一个下调事件。 详情请参见 [GAMPAD_ BUTTON_ DOWN] QQlinkcode Phaser.Input.Gamepad.Events# event: GAMPAD_ BUTTON_ DOWN] 事件 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pad | [Phaser.Input.Gamepad](/api/namespace/input-gamepad) | 否 | 引用按下按钮的 Gamepad 。 |
| button | [Phaser.Input.Gamepad.Button](/api/class/input-gamepad-button) | 否 | 被按下按钮的提示 。 |
| value | number | 否 | 按钮按下时的值。 0 至 1 之间, 有些 Gamepad 具有压力敏感按钮 。 |

**Member of:** [Phaser.Input.Gamepad.Events](/api/namespace/input-gamepad-events)
> 源码：[src/input/gamepad/events/BUTTON_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/events/BUTTON_DOWN_EVENT.js#L7)  
引入版本：3.10.0

## BUTTON_UP {#button_up}


**说明:** Gamepad按钮事件.

当任何活动 Gamepad 上发布了按钮时,此事件由 Gamepad 插件发送 。

使用:`this.input.gamepad.on('up', listener)`,从场内听这个事件.

您也可以从 Gamepad 实例中听到 UP 事件。 详情请参见 [GAMPAD_ BUTTON_ UP] QQlinkcode Phaser.Input.Gamepad.Events#event: GAMPAD_ BUTTON_ UP] 事件 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pad | [Phaser.Input.Gamepad](/api/namespace/input-gamepad) | 否 | 引用了该按钮的Gamepad 。 |
| button | [Phaser.Input.Gamepad.Button](/api/class/input-gamepad-button) | 否 | 引用了已经发布的按钮。 |
| value | number | 否 | 发布时按钮的值。 0 到 1 之间, 有些 Gamepad 具有压力敏感按钮 。 |

**Member of:** [Phaser.Input.Gamepad.Events](/api/namespace/input-gamepad-events)
> 源码：[src/input/gamepad/events/BUTTON_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/events/BUTTON_UP_EVENT.js#L7)  
引入版本：3.10.0

## CONNECTED {#connected}


**说明:** 游戏板连接事件.

当一个 Gamepad 连接到时, Gamepad 插件会发出此事件 。

使用:`this.input.gamepad.once('connected', listener)`,从场内听这个事件.

注意浏览器可能要求您按下一个游戏盘上的按钮,然后才能允许您访问它,
不过,它可能已经相信了,如果这样的话,你就不会得到
连接到的事件, 而不是检查 `GamepadPlugin.total` 是否认为有游戏板
已经连接。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pad | [Phaser.Input.Gamepad](/api/namespace/input-gamepad) | 否 | 引用了连接的 Gamepad 。 |
| event | Event | 否 | 引发了连接的本地 DOM事件. |

**Member of:** [Phaser.Input.Gamepad.Events](/api/namespace/input-gamepad-events)
> 源码：[src/input/gamepad/events/CONNECTED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/events/CONNECTED_EVENT.js#L7)  
引入版本：3.0.0

## DISCONNECTED {#disconnected}


**说明:** 游戏板断开事件.

当一个 Gamepad 已断开时, 此事件由 Gamepad 插件发送 。

使用:`this.input.gamepad.once('disconnected', listener)`,从场内听这个事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pad | [Phaser.Input.Gamepad](/api/namespace/input-gamepad) | 否 | 提到Gamepad时断开的 |
| event | Event | 否 | 引发断开的本地 DOM 事件 。 |

**Member of:** [Phaser.Input.Gamepad.Events](/api/namespace/input-gamepad-events)
> 源码：[src/input/gamepad/events/DISCONNECTED_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/events/DISCONNECTED_EVENT.js#L7)  
引入版本：3.0.0

## GAMEPAD_BUTTON_DOWN {#gamepad_button_down}


**说明:** 游戏板扣子下架事件.

此事件由 Gamepad 实例在按下按钮时发送 。

从 Gamepad 实例中聆听此事件。 获取此消息的一个方法来自 Gamepad 插件上的 `pad1` 、 `pad2` 等属性 :
`this.input.gamepad.pad1.on('down', listener)`.

注意, 在浏览器认为 Gamepad 已“ 连接” 之前, 您不会收到 Gamepad 按钮事件 。

您也可以从 Gamepad 插件中收听一个下行事件。 详情请参见 [BUTTON_ DOWN] @%linkcode Phaser.Input.Gamepad.Events# event: BUTTON_ DOWN] 事件 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 被按下的按钮索引 。 |
| value | number | 否 | 按钮按下时的值。 0 至 1 之间, 有些 Gamepad 具有压力敏感按钮 。 |
| button | [Phaser.Input.Gamepad.Button](/api/class/input-gamepad-button) | 否 | 被按下按钮的提示 。 |

**Member of:** [Phaser.Input.Gamepad.Events](/api/namespace/input-gamepad-events)
> 源码：[src/input/gamepad/events/GAMEPAD_BUTTON_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/events/GAMEPAD_BUTTON_DOWN_EVENT.js#L7)  
引入版本：3.10.0

## GAMEPAD_BUTTON_UP {#gamepad_button_up}


**说明:** Gamepad按钮事件.

此事件由 Gamepad 实例发出, 当该实例上发布了按钮 。

从 Gamepad 实例中聆听此事件。 获取此消息的一个方法来自 Gamepad 插件上的 `pad1` 、 `pad2` 等属性 :
`this.input.gamepad.pad1.on('up', listener)`.

注意, 在浏览器认为 Gamepad 已“ 连接” 之前, 您不会收到 Gamepad 按钮事件 。

您也可以从 Gamepad 插件中收听 UP 事件。 详情请参见 [BUTTON_ UP] @%linkcode Phaser.Input.Gamepad.Events# event: BUTTON_ UP] 事件 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 已发布的按钮索引 。 |
| value | number | 否 | 发布时按钮的值。 0 到 1 之间, 有些 Gamepad 具有压力敏感按钮 。 |
| button | [Phaser.Input.Gamepad.Button](/api/class/input-gamepad-button) | 否 | 引用了已经发布的按钮。 |

**Member of:** [Phaser.Input.Gamepad.Events](/api/namespace/input-gamepad-events)
> 源码：[src/input/gamepad/events/GAMEPAD_BUTTON_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/events/GAMEPAD_BUTTON_UP_EVENT.js#L7)  
引入版本：3.10.0

---
