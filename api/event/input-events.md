# Input.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/input-events)

## BOOT {#boot}


**说明:** 输入插件靴子事件 。

这个内部事件由输入插件在它向它的所有系统发出信号以创建自己时发出.

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/BOOT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/BOOT_EVENT.js#L7)  
引入版本：3.0.0

## DESTROY {#destroy}


**说明:** 输入插件销毁事件 。

内部事件在被摧毁时由输入插件发出,信号到其所有系统自行毁灭.

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0

## DRAG_END {#drag_end}


**说明:** 指针拖动结束输入事件 。

如果指针停止拖曳游戏对象,此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('dragend', listener)`,从场内听这个事件.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ DRAG_END] QQlinkcode Phaser.Input.Events#event: GameoOBJECT_ DRAG_END] 事件代替 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针停止拖曳的交互式游戏对象 。 |
| dropped | boolean | 否 | 游戏对象是否被丢入目标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/DRAG_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_END_EVENT.js#L7)  
引入版本：3.0.0

## DRAG_ENTER {#drag_enter}


**说明:** 指针拖动输入事件 。

如果指针将游戏对象拖入拖动目标,则此事件由属于 Scene 的输入插件发送。

使用:`this.input.on('dragenter', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ DRAG_ENTER] \\ linkcode Phaser.Input.Events# event: GameoOBJECT_ DRAG_ENTER] 事件代替 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针已移动到的拖曳目标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/DRAG_ENTER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_ENTER_EVENT.js#L7)  
引入版本：3.0.0

## DRAG {#drag}


**说明:** 指针拖动输入事件 。

如果一个指针在拖动游戏对象时移动,则该事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('drag', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ DRAG] QQlinkcode Phaser.Input.Events# event: GameoOBJECT_ DRAG] 事件代替 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |
| dragX | number | 否 | x 坐标指针当前拖动游戏对象的地方, 在世界空间中. |
| dragY | number | 否 | 指针当前在世界空间拖动游戏对象的位置的 Y 坐标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/DRAG_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_EVENT.js#L7)  
引入版本：3.0.0

## DRAG_LEAVE {#drag_leave}


**说明:** 指针拖放输入事件 。

如果指针将游戏对象拖出拖曳目标,则属于 Scene 的输入插件会发出此事件 。

使用:`this.input.on('dragleave', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ DRAG_LEAVE] QQlinkcode Phaser.Input.Events#event: GameoOBJECT_ DRAG_LAVE] 事件代替 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针所留下的拖曳目标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/DRAG_LEAVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_LEAVE_EVENT.js#L7)  
引入版本：3.0.0

## DRAG_OVER {#drag_over}


**说明:** 指针拖动输入事件 。

如果指针将游戏对象拖过拖曳目标,则属于 Scene 的输入插件会发出此事件。

游戏对象首次进入拖曳目标时, 它会发出 `dragenter`事件。 如果它会在内部移动
拖曳目标,它会释放出这个事件。

使用:`this.input.on('dragover', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ DRAG_OVER] QQlinkcode Phaser.Input.Events# event: GameoOBJECT_ DRAG_OVER] 事件代替 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 这个指针移动到这里的拖曳目标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/DRAG_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_OVER_EVENT.js#L7)  
引入版本：3.0.0

## DRAG_START {#drag_start}


**说明:** 指针拖动启动输入事件 。

如果指针开始拖动任何游戏对象,则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('dragstart', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ DRAG_START] QQlinkcode Phaser.Input.Events#event: GameoOBJECT_ DRAG_START] 事件代替 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/DRAG_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_START_EVENT.js#L7)  
引入版本：3.0.0

## DROP {#drop}


**说明:** 指针投放事件.

如果指针在拖放目标上丢弃游戏对象,则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('drop', listener)`,从场内听这个事件.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ DROP] QQlinkcode Phaser.Input.Events#event: GameoOBJECT_ DROP] 事件代替 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针所拖曳的交互式游戏对象 。 |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 拖曳目标`gameObject`已经投放。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/DROP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DROP_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_DOWN {#gameobject_down}


**说明:** 游戏对象下输入事件 。

如果在_any_ 交互式游戏对象上按下指针,则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('gameobjectdown', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ POPINTER_ DOWN] QQlinkcode Phaser.Input.Events#event: GAMEOBJECT_ POINTER_DOWN] 事件代替 。

事件等级如下:

1. [GAMEOBJECT_POINTER_DOWN] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_DOWN] (歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词:
2. [GAMEOBJECT_DOWN] 链接码Phaser.Input.Events#事件:GAMEOBJECT_DOWN]
3. [POINTER_DOWN] 链接码Phaser.Input.Events#事件:POINTER_DOWN]或 [POINTER_DOWN_OUTSIDE] 链接码Phaser.Input.Events#事件:POINTER_DOWN_OUTSIDE]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将指针按下游戏对象 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DOWN_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_DRAG_END {#gameobject_drag_end}


**说明:** 游戏对象拖曳结束事件 。

如果指针停止拖曳,此事件由交互式游戏对象发送 。

使用: `gameObject.on('dragend', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式并启用拖动 。
详情请见[GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive)。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| dragX | number | 否 | 指针停止拖曳游戏对象的 x 坐标, 在世界空间中 。 |
| dragY | number | 否 | 指针停止拖曳游戏对象的地方的y坐标, 在世界空间中. |
| dropped | boolean | 否 | 游戏对象是否被丢入目标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_DRAG_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_END_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_DRAG_ENTER {#gameobject_drag_enter}


**说明:** 游戏对象拖放 Enter Evention 。

如果指针将其拖入拖动目标,则此事件由交互式游戏对象发送.

使用: `gameObject.on('dragenter', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式并启用拖动 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针已移动到的拖曳目标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_DRAG_ENTER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_ENTER_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_DRAG {#gameobject_drag}


**说明:** 游戏对象拖放事件 。

如果一个指针在拖动时移动,则此事件由交互式游戏对象发送 。

使用: `gameObject.on('drag', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式并启用拖动 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| dragX | number | 否 | x 坐标指针当前拖动游戏对象的地方, 在世界空间中. |
| dragY | number | 否 | 指针当前在世界空间拖动游戏对象的位置的 Y 坐标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_DRAG_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_DRAG_LEAVE {#gameobject_drag_leave}


**说明:** 游戏对象拖放事件 。

如果指针将其拖出拖动目标,此事件由交互式游戏对象发送.

使用: `gameObject.on('dragleave', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式并启用拖动 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针所留下的拖曳目标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_DRAG_LEAVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_LEAVE_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_DRAG_OVER {#gameobject_drag_over}


**说明:** 游戏对象拖曳事件 。

如果指针将其拖过拖曳目标,则此事件由交互式游戏对象发送.

游戏对象首次进入拖曳目标时, 它会发出 `dragenter`事件。 如果它会在内部移动
拖曳目标,它会释放出这个事件。

使用: `gameObject.on('dragover', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式并启用拖动 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 这个指针移动到这里的拖曳目标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_DRAG_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_OVER_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_DRAG_START {#gameobject_drag_start}


**说明:** 游戏对象拖动启动事件 。

如果一个指针开始拖动,此事件由交互式游戏对象发送 。

使用: `gameObject.on('dragstart', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式并启用拖动 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

游戏对象中有许多有用的拖动属性在拖动时设置.
例如`gameObject.input.dragStartX`,`dragStartY`等.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| dragX | number | 否 | x 坐标指针当前拖动游戏对象的地方, 在世界空间中. |
| dragY | number | 否 | 指针当前在世界空间拖动游戏对象的位置的 Y 坐标 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_DRAG_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_START_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_DROP {#gameobject_drop}


**说明:** 游戏对象抛放事件 。

如果指针在拖放目标上丢弃,此事件由交互式游戏对象发送 。

使用: `gameObject.on('drop', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式并启用拖动 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 拖曳目标`gameObject`已经投放。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_DROP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DROP_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_MOVE {#gameobject_move}


**说明:** 游戏对象移动输入事件 。

如果一个指针移动到_ 任意_ 交互式游戏对象之间, 则属于 Scene 的输入插件会发出此事件 。

使用:`this.input.on('gameobjectmove', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ POPINTER_MOVE] QQlinkcode Phaser.Input.Events#event: GameoOBJECT_ POPINTER_MOVE] 事件代替 。

事件等级如下:

1. [GAMEOBECT_POINTER_移动] QQLinkcode Phaser.Input.Events#事件:GAMEOBJECT_POINTER_移动] 互联网档案馆的存档,存档日期2011-03-02.
2. [GAMEOBJECT_MOVE] 链接码Phaser.Input.Events#事件:GAMEOBJECT_MOVE] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_MOVE] 链接代码 Phaser.Input.Events活动: 节目(POINTER_MOVE)

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 指针被移动的游戏对象 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_MOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_MOVE_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_OUT {#gameobject_out}


**说明:** 游戏对象输出事件 。

如果指针移动到 __任何_交互式游戏对象,则属于 Scene 的输入插件会发出此事件。

使用:`this.input.on('gameobjectout', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ POPINTER_ OUT] \\ linkcode Phaser.Input.Events# event: GameoOBJECT_ PONTER_ OUT] 事件代替 。

事件等级如下:

1. [GAMEOBJECT_POINTER_OUT] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_OUT] (歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词:
2. [GAMEOBJECT_OUT] 链接码Phaser.Input.Events#事件:GAMEOBJECT_OUT]
3. [POINTER_OUT] 链接码Phaser.Input.Events#事件:POINTER_OUT]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

如果指针离开游戏布局本身,它不会触发此事件。要处理这些案件,
请听一下[GAME_OUT]的QQlinkcode Phaser.Input.Events#event:GAME_OUT]事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 指针移动出来的游戏对象 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_OUT_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_OVER {#gameobject_over}


**说明:** 游戏对象超越输入事件 。

如果指针移动到 __任何_交互式游戏对象上,则此事件由属于 Scene 的输入插件发送。

使用:`this.input.on('gameobjectover', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ POPINTER_ Over] QQlinkcode Phaser.Input.Events#event: GameoOBJECT_ POPINTER_ Over] 事件代替 。

事件等级如下:

1. [GAMEOBJECT_POINTER_over] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_over] (歌词).
2. [GAMEOBJECT_over] 链接码Phaser.Input.Events#事件:GAMEOBJECT_over] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_over] 链接码Phaser.Input.Events#事件:POINTER_over] 互联网档案馆的存档,存档日期2014-09-02.

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 指针移动到的游戏对象 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_OVER_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_POINTER_DOWN {#gameobject_pointer_down}


**说明:** 游戏对象指针下行事件.

如果一个指针被压下, 此事件由交互式游戏对象发送 。

使用: `gameObject.on('pointerdown', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

事件等级如下:

1. [GAMEOBJECT_POINTER_DOWN] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_DOWN] (歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词:
2. [GAMEOBJECT_DOWN] 链接码Phaser.Input.Events#事件:GAMEOBJECT_DOWN]
3. [POINTER_DOWN] 链接码Phaser.Input.Events#事件:POINTER_DOWN]或 [POINTER_DOWN_OUTSIDE] 链接码Phaser.Input.Events#事件:POINTER_DOWN_OUTSIDE]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_POINTER_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_DOWN_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_POINTER_MOVE {#gameobject_pointer_move}


**说明:** 游戏对象指针移动事件 。

如果在移动指针时移动了该事件,则由交互式游戏对象发送。

使用: `gameObject.on('pointermove', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

事件等级如下:

1. [GAMEOBECT_POINTER_移动] QQLinkcode Phaser.Input.Events#事件:GAMEOBJECT_POINTER_移动] 互联网档案馆的存档,存档日期2011-03-02.
2. [GAMEOBJECT_MOVE] 链接码Phaser.Input.Events#事件:GAMEOBJECT_MOVE] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_MOVE] 链接代码 Phaser.Input.Events活动: 节目(POINTER_MOVE)

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_POINTER_MOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_MOVE_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_POINTER_OUT {#gameobject_pointer_out}


**说明:** 游戏对象指针事件( Out Event).

如果指针移动出此事件, 则由交互式游戏对象发送 。

使用: `gameObject.on('pointerout', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

事件等级如下:

1. [GAMEOBJECT_POINTER_OUT] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_OUT] (歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词:
2. [GAMEOBJECT_OUT] 链接码Phaser.Input.Events#事件:GAMEOBJECT_OUT]
3. [POINTER_OUT] 链接码Phaser.Input.Events#事件:POINTER_OUT]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

如果指针离开游戏布局本身,它不会触发此事件。要处理这些案件,
请听一下[GAME_OUT]的QQlinkcode Phaser.Input.Events#event:GAME_OUT]事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_POINTER_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_OUT_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_POINTER_OVER {#gameobject_pointer_over}


**说明:** 游戏对象指针在事件上.

如果指针移动到它上面,此事件由交互式游戏对象发送 。

使用: `gameObject.on('pointerover', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

事件等级如下:

1. [GAMEOBJECT_POINTER_over] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_over] (歌词).
2. [GAMEOBJECT_over] 链接码Phaser.Input.Events#事件:GAMEOBJECT_over] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_over] 链接码Phaser.Input.Events#事件:POINTER_over] 互联网档案馆的存档,存档日期2014-09-02.

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_POINTER_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_OVER_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_POINTER_UP {#gameobject_pointer_up}


**说明:** 游戏对象指针事件(英语:Game Object Power Up Evention).

如果在游戏上方发布了指针,则此事件由交互式游戏对象发送.

使用: `gameObject.on('pointerup', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

事件等级如下:

1. [GAMEOBJECT_POINTER_UP] QQLINKE代码Phaser.Input.Events#事件:GAMEOBJECT_POINTER_UP] 互联网档案馆的存档,存档日期2014-09-02.
2. [GAMEOBJECT_UP] 链接码Phaser.Input.Events#事件:GAMEOBJECT_UP]
3. [POINTER_UP] 链接代码 Phaser.Input.Events或[POINTER_UP_OUTSIDE] 链接码 Phaser.Input.Events活动: 节目的结束

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_POINTER_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_UP_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_POINTER_WHEEL {#gameobject_pointer_wheel}


**说明:** 游戏对象指针轮事件.

如果指针在移动时其方向盘被移动,则此事件由交互式游戏对象发送 。

使用: `gameObject.on('wheel', listener)` 的游戏对象中收听此事件 。
注意,听众的范围自动设定为Game Object 实例本身.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

事件等级如下:

1. [GAMEOBJECT_POINTER_WHEEL] 链接码 Phaser.Input.Events活动: 游戏的音乐
2. [Gameoobject_WHELL] 链接码Phaser.Input.Events#事件:Gameoobject_WHELL] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_WHELL] 链接码Phaser.Input.Events#事件:POINTER_WHELL]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| deltaX | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的水平滚动量. |
| deltaY | number | 否 | 由用户移动鼠标轮盘或类似输入设备产生的垂直滚动量。 如果用户向上滚动, 则该数值通常小于 0, 向下滚动时大于 0 。 |
| deltaZ | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的z轴滚动量. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_POINTER_WHEEL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_WHEEL_EVENT.js#L7)  
引入版本：3.18.0

## GAMEOBJECT_UP {#gameobject_up}


**说明:** 游戏对象向上输入事件 。

如果在_ 任意_ 交互式游戏对象时发布指针, 此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('gameobjectup', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ POPINTER_UP] QQ linkcode Phaser.Input.Events#event: GameoOBJECT_ POPINTER_UP] 事件代替 。

事件等级如下:

1. [GAMEOBJECT_POINTER_UP] QQLINKE代码Phaser.Input.Events#事件:GAMEOBJECT_POINTER_UP] 互联网档案馆的存档,存档日期2014-09-02.
2. [GAMEOBJECT_UP] 链接码Phaser.Input.Events#事件:GAMEOBJECT_UP]
3. [POINTER_UP] 链接代码 Phaser.Input.Events或[POINTER_UP_OUTSIDE] 链接码 Phaser.Input.Events活动: 节目的结束

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象 指针发布时结束 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_UP_EVENT.js#L7)  
引入版本：3.0.0

## GAMEOBJECT_WHEEL {#gameobject_wheel}


**说明:** 游戏对象轮输入事件.

如果指针在_ 任意_ 交互式游戏对象时移动了方向盘, 则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('gameobjectwheel', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式 。
详见[Game Object.ZsetInteractive] ^ 链接Phaser.GameObjects.GameObject#setInteractive] 更多细节.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [GameoOBJECT_ POPINTER_ WHEEL] \\ linkcode Phaser.Input.Events# event: GameoOBJECT_ POINTER_WHEEL] 事件代替 。

事件等级如下:

1. [GAMEOBJECT_POINTER_WHEEL] 链接码 Phaser.Input.Events活动: 游戏的音乐
2. [Gameoobject_WHELL] 链接码Phaser.Input.Events#事件:Gameoobject_WHELL] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_WHELL] 链接码Phaser.Input.Events#事件:POINTER_WHELL]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 方向盘改变时, 游戏对象结束 。 |
| deltaX | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的水平滚动量. |
| deltaY | number | 否 | 由用户移动鼠标轮盘或类似输入设备产生的垂直滚动量。 如果用户向上滚动, 则该数值通常小于 0, 向下滚动时大于 0 。 |
| deltaZ | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的z轴滚动量. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAMEOBJECT_WHEEL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_WHEEL_EVENT.js#L7)  
引入版本：3.18.0

## GAME_OUT {#game_out}


**说明:** 输入插件游戏出局事件 。

如果活动指针离开游戏画布,则此事件由输入插件发送, 此时已存在
外边,别处的网页上

使用:`this.input.on('gameout', listener)`,从场内听这个事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| event | MouseEvent \| TouchEvent | 否 | 引发画布的DOM事件 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAME_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAME_OUT_EVENT.js#L7)  
引入版本：3.16.1

## GAME_OVER {#game_over}


**说明:** 输入插件游戏“ 事件” 。

如果活动指针进入游戏画布,则此事件由输入插件发送, 并且现在是
之前在网页上其他地方

使用:`this.input.on('gameover', listener)`,从场内听这个事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| event | MouseEvent \| TouchEvent | 否 | 引发画布的DOM事件 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/GAME_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAME_OVER_EVENT.js#L7)  
引入版本：3.16.1

## MANAGER_BOOT {#manager_boot}


**说明:** 输入管理器靴子事件 。

此内部事件由输入管理器在拖曳时发送 。

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/MANAGER_BOOT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/MANAGER_BOOT_EVENT.js#L7)  
引入版本：3.0.0

## MANAGER_PROCESS {#manager_process}


**说明:** 输入管理器处理事件 。

内部事件由输入管理器在不使用遗留队列系统时发出,
它希望输入插件能够更新自己。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/MANAGER_PROCESS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/MANAGER_PROCESS_EVENT.js#L7)  
引入版本：3.0.0

## MANAGER_UPDATE {#manager_update}


**说明:** 输入管理器更新事件 。

内部事件由输入管理器发出,作为其更新步骤的一部分.

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/MANAGER_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/MANAGER_UPDATE_EVENT.js#L7)  
引入版本：3.0.0

## POINTERLOCK_CHANGE {#pointerlock_change}


**说明:** 输入管理器 指针锁定改变事件 。

此事件由输入管理器在处理本地的指针锁变换 DOM 事件时发送 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | Event | 否 | 本地的DOM事件. |
| locked | boolean | 否 | 鼠标指针的锁定状态 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTERLOCK_CHANGE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTERLOCK_CHANGE_EVENT.js#L7)  
引入版本：3.0.0

## POINTER_DOWN {#pointer_down}


**说明:** 指向下输入事件。

如果一个指针被按下, 属于 Scene 的输入插件会发出此事件 。

使用:`this.input.on('pointerdown', listener)`,从场内听这个事件.

事件等级如下:

1. [GAMEOBJECT_POINTER_DOWN] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_DOWN] (歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词:
2. [GAMEOBJECT_DOWN] 链接码Phaser.Input.Events#事件:GAMEOBJECT_DOWN]
3. [POINTER_DOWN] 链接码Phaser.Input.Events#事件:POINTER_DOWN]或 [POINTER_DOWN_OUTSIDE] 链接码Phaser.Input.Events#事件:POINTER_DOWN_OUTSIDE]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| currentlyOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针已关闭的所有交互式游戏对象的阵列 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTER_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_DOWN_EVENT.js#L7)  
引入版本：3.0.0

## POINTER_DOWN_OUTSIDE {#pointer_down_outside}


**说明:** 指向外输入事件。

如果游戏画布外的任何地方按下指针,则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('pointerdownoutside', listener)`,从场内听这个事件.

事件等级如下:

1. [GAMEOBJECT_POINTER_DOWN] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_DOWN] (歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词:
2. [GAMEOBJECT_DOWN] 链接码Phaser.Input.Events#事件:GAMEOBJECT_DOWN]
3. [POINTER_DOWN] 链接码Phaser.Input.Events#事件:POINTER_DOWN]或 [POINTER_DOWN_OUTSIDE] 链接码Phaser.Input.Events#事件:POINTER_DOWN_OUTSIDE]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTER_DOWN_OUTSIDE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_DOWN_OUTSIDE_EVENT.js#L7)  
引入版本：3.16.1

## POINTER_MOVE {#pointer_move}


**说明:** 指针移动输入事件 。

如果指针移动到任何地方,此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('pointermove', listener)`,从场内听这个事件.

事件等级如下:

1. [GAMEOBECT_POINTER_移动] QQLinkcode Phaser.Input.Events#事件:GAMEOBJECT_POINTER_移动] 互联网档案馆的存档,存档日期2011-03-02.
2. [GAMEOBJECT_MOVE] 链接码Phaser.Input.Events#事件:GAMEOBJECT_MOVE] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_MOVE] 链接代码 Phaser.Input.Events活动: 节目(POINTER_MOVE)

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| currentlyOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针已关闭的所有交互式游戏对象的阵列 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTER_MOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_MOVE_EVENT.js#L7)  
引入版本：3.0.0

## POINTER_OUT {#pointer_out}


**说明:** 指针输出事件 。

如果指针从任何交互式游戏对象中移动,则该事件由属于 Scene 的输入插件发送。

使用:`this.input.on('pointerout', listener)`,从场内听这个事件.

事件等级如下:

1. [GAMEOBJECT_POINTER_OUT] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_OUT] (歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词: 歌词:
2. [GAMEOBJECT_OUT] 链接码Phaser.Input.Events#事件:GAMEOBJECT_OUT]
3. [POINTER_OUT] 链接码Phaser.Input.Events#事件:POINTER_OUT]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

如果指针离开游戏布局本身,它不会触发此事件。要处理这些案件,
请听一下[GAME_OUT]的QQlinkcode Phaser.Input.Events#event:GAME_OUT]事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| justOut | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含所有交互式游戏对象的阵列,指针在事件创建时移动出. |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTER_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_OUT_EVENT.js#L7)  
引入版本：3.0.0

## POINTER_OVER {#pointer_over}


**说明:** 指针输入事件。

如果指针移动到任何交互式游戏对象上,此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('pointerover', listener)`,从场内听这个事件.

事件等级如下:

1. [GAMEOBJECT_POINTER_over] 链接码 Phaser.Input.Events活动: Gameoobject_POINTER_over] (歌词).
2. [GAMEOBJECT_over] 链接码Phaser.Input.Events#事件:GAMEOBJECT_over] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_over] 链接码Phaser.Input.Events#事件:POINTER_over] 互联网档案馆的存档,存档日期2014-09-02.

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| justOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针移动到所有交互式游戏对象的阵列 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTER_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_OVER_EVENT.js#L7)  
引入版本：3.0.0

## POINTER_UP {#pointer_up}


**说明:** 指向输入事件。

如果向任何地方放出指针,则该事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('pointerup', listener)`,从场内听这个事件.

事件等级如下:

1. [GAMEOBJECT_POINTER_UP] QQLINKE代码Phaser.Input.Events#事件:GAMEOBJECT_POINTER_UP] 互联网档案馆的存档,存档日期2014-09-02.
2. [GAMEOBJECT_UP] 链接码Phaser.Input.Events#事件:GAMEOBJECT_UP]
3. [POINTER_UP] 链接代码 Phaser.Input.Events或[POINTER_UP_OUTSIDE] 链接码 Phaser.Input.Events活动: 节目的结束

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| currentlyOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针已关闭的所有交互式游戏对象的阵列 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTER_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_UP_EVENT.js#L7)  
引入版本：3.0.0

## POINTER_UP_OUTSIDE {#pointer_up_outside}


**说明:** 指向外部输入事件。

如果在游戏画布以外的任何地方发布指针,则该事件由属于Scene的输入插件发送.

使用:`this.input.on('pointerupoutside', listener)`,从场内听这个事件.

事件等级如下:

1. [GAMEOBJECT_POINTER_UP] QQLINKE代码Phaser.Input.Events#事件:GAMEOBJECT_POINTER_UP] 互联网档案馆的存档,存档日期2014-09-02.
2. [GAMEOBJECT_UP] 链接码Phaser.Input.Events#事件:GAMEOBJECT_UP]
3. [POINTER_UP] 链接代码 Phaser.Input.Events或[POINTER_UP_OUTSIDE] 链接码 Phaser.Input.Events活动: 节目的结束

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTER_UP_OUTSIDE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_UP_OUTSIDE_EVENT.js#L7)  
引入版本：3.16.1

## POINTER_WHEEL {#pointer_wheel}


**说明:** 指针轮输入事件.

如果指针的轮子更新了,则该事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('wheel', listener)`,从场内听这个事件.

事件等级如下:

1. [GAMEOBJECT_POINTER_WHEEL] 链接码 Phaser.Input.Events活动: 游戏的音乐
2. [Gameoobject_WHELL] 链接码Phaser.Input.Events#事件:Gameoobject_WHELL] 互联网档案馆的存档,存档日期2011-09-02.
3. [POINTER_WHELL] 链接码Phaser.Input.Events#事件:POINTER_WHELL]

将先发送顶级事件, 然后从列表中流出。 请注意, 更高级的事件处理器可以停止 。
宣传这一事件。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| currentlyOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针已关闭的所有交互式游戏对象的阵列 。 |
| deltaX | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的水平滚动量. |
| deltaY | number | 否 | 由用户移动鼠标轮盘或类似输入设备产生的垂直滚动量。 如果用户向上滚动, 则该数值通常小于 0, 向下滚动时大于 0 。 |
| deltaZ | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的z轴滚动量. |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/POINTER_WHEEL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_WHEEL_EVENT.js#L7)  
引入版本：3.18.0

## PRE_UPDATE {#pre_update}


**说明:** 输入插件更新前事件 。

此内部事件由输入插件在其`preUpdate`方法开始时发送.
这个钩子是专门为输入插件设计的,但也可以从用户-土地代码中听取.

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/PRE_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/PRE_UPDATE_EVENT.js#L7)  
引入版本：3.0.0

## SHUTDOWN {#shutdown}


**说明:** 输入插件关闭事件 。

内部事件由输入插件在关闭时发出,信号到其所有系统关闭自己.

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/SHUTDOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/SHUTDOWN_EVENT.js#L7)  
引入版本：3.0.0

## START {#start}


**说明:** 输入插件启动事件 。

内部事件由输入插件在完成设置后发送,
向它的所有内部系统发出信号

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/START_EVENT.js#L7)  
引入版本：3.0.0

## UPDATE {#update}


**说明:** 输入插件更新事件 。

此内部事件由输入插件在其`update`方法开始时发送.
这个钩子是专门为输入插件设计的,但也可以从用户-土地代码中听取.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |

**Member of:** [Phaser.Input.Events](/api/namespace/input-events)
> 源码：[src/input/events/UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/UPDATE_EVENT.js#L7)  
引入版本：3.0.0

---
