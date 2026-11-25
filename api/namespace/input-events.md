# Phaser.Input.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/input-events)

Scope: 
static
> 源码：[src/input/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/index.js#L7)  


## 静态函数 {#static-functions}

### BOOT {#BOOT}

#### BOOT {#boot}


**说明:**

输入插件靴子事件 。

这个内部事件由输入插件在它向它的所有系统发出信号以创建自己时发出.


> 源码：[src/input/events/BOOT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/BOOT_EVENT.js#L7)  
引入版本：3.0.0


---

### DESTROY {#DESTROY}

#### DESTROY {#destroy}


**说明:**

输入插件销毁事件 。

内部事件在被摧毁时由输入插件发出,信号到其所有系统自行毁灭.


> 源码：[src/input/events/DESTROY_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DESTROY_EVENT.js#L7)  
引入版本：3.0.0


---

### DRAG {#DRAG}

#### DRAG {#drag}


**说明:**

指针拖动输入事件 。

如果一个指针在拖动游戏对象时移动,则该事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('drag', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_DRAG``](/api/event/input-events#gameobject_drag) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |
| dragX | number | 否 | x 坐标指针当前拖动游戏对象的地方, 在世界空间中. |
| dragY | number | 否 | 指针当前在世界空间拖动游戏对象的位置的 Y 坐标 。 |


> 源码：[src/input/events/DRAG_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_EVENT.js#L7)  
引入版本：3.0.0


---

### DRAG_END {#DRAG_END}

#### DRAG_END {#drag_end}


**说明:**

指针拖动结束输入事件 。

如果指针停止拖曳游戏对象,此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('dragend', listener)`,从场内听这个事件.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_DRAG_END``](/api/event/input-events#gameobject_drag_end) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针停止拖曳的交互式游戏对象 。 |
| dropped | boolean | 否 | 游戏对象是否被丢入目标 。 |


> 源码：[src/input/events/DRAG_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_END_EVENT.js#L7)  
引入版本：3.0.0


---

### DRAG_ENTER {#DRAG_ENTER}

#### DRAG_ENTER {#drag_enter}


**说明:**

指针拖动输入事件 。

如果指针将游戏对象拖入拖动目标,则此事件由属于 Scene 的输入插件发送。

使用:`this.input.on('dragenter', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_DRAG_ENTER``](/api/event/input-events#gameobject_drag_enter) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针已移动到的拖曳目标 。 |


> 源码：[src/input/events/DRAG_ENTER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_ENTER_EVENT.js#L7)  
引入版本：3.0.0


---

### DRAG_LEAVE {#DRAG_LEAVE}

#### DRAG_LEAVE {#drag_leave}


**说明:**

指针拖放输入事件 。

如果指针将游戏对象拖出拖曳目标,则属于 Scene 的输入插件会发出此事件 。

使用:`this.input.on('dragleave', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_DRAG_LEAVE``](/api/event/input-events#gameobject_drag_leave) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针所留下的拖曳目标 。 |


> 源码：[src/input/events/DRAG_LEAVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_LEAVE_EVENT.js#L7)  
引入版本：3.0.0


---

### DRAG_OVER {#DRAG_OVER}

#### DRAG_OVER {#drag_over}


**说明:**

指针拖动输入事件 。

如果指针将游戏对象拖过拖曳目标,则属于 Scene 的输入插件会发出此事件。

当游戏对象首次进入拖曳目标时, 它会发出 `dragenter`事件。 如果它随后在拖曳目标内移动, 它会发出这个事件 。

使用:`this.input.on('dragover', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_DRAG_OVER``](/api/event/input-events#gameobject_drag_over) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 这个指针移动到这里的拖曳目标 。 |


> 源码：[src/input/events/DRAG_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_OVER_EVENT.js#L7)  
引入版本：3.0.0


---

### DRAG_START {#DRAG_START}

#### DRAG_START {#drag_start}


**说明:**

指针拖动启动输入事件 。

如果指针开始拖动任何游戏对象,则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('dragstart', listener)`,从场内听这个事件.

指针只能一次拖动单个游戏对象.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_DRAG_START``](/api/event/input-events#gameobject_drag_start) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针正在拖动的交互式游戏对象 。 |


> 源码：[src/input/events/DRAG_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DRAG_START_EVENT.js#L7)  
引入版本：3.0.0


---

### DROP {#DROP}

#### DROP {#drop}


**说明:**

指针投放事件.

如果指针在拖放目标上丢弃游戏对象,则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('drop', listener)`,从场内听这个事件.

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_DROP``](/api/event/input-events#gameobject_drop) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针所拖曳的交互式游戏对象 。 |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 拖曳目标`gameObject`已经投放。 |


> 源码：[src/input/events/DROP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/DROP_EVENT.js#L7)  
引入版本：3.0.0


---

### GAME_OUT {#GAME_OUT}

#### GAME_OUT {#game_out}


**说明:**

输入插件游戏出局事件 。

如果活动指针离开游戏画布,并且现在不在它之外,则该事件由输入插件发送,在网页的其他地方.

使用:`this.input.on('gameout', listener)`,从场内听这个事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| event | MouseEvent \| TouchEvent | 否 | 引发画布的DOM事件 |


> 源码：[src/input/events/GAME_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAME_OUT_EVENT.js#L7)  
引入版本：3.16.1


---

### GAME_OVER {#GAME_OVER}

#### GAME_OVER {#game_over}


**说明:**

输入插件游戏“ 事件” 。

如果活动指针进入游戏画布,并且已经覆盖,则此事件由输入插件发送,因为此前该网页上已经存在其它内容。

使用:`this.input.on('gameover', listener)`,从场内听这个事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| event | MouseEvent \| TouchEvent | 否 | 引发画布的DOM事件 |


> 源码：[src/input/events/GAME_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAME_OVER_EVENT.js#L7)  
引入版本：3.16.1


---

### GAMEOBJECT_DOWN {#GAMEOBJECT_DOWN}

#### GAMEOBJECT_DOWN {#gameobject_down}


**说明:**

游戏对象下输入事件 。

如果在_any_ 交互式游戏对象上按下指针,则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('gameobjectdown', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_POINTER_DOWN``](/api/event/input-events#gameobject_pointer_down) 事件 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_DOWN``](/api/event/input-events#gameobject_pointer_down)

2. [``GAMEOBJECT_DOWN``](/api/event/input-events#gameobject_down)

3. [``POINTER_DOWN``](/api/namespace/input-events#pointer_down) or [``POINTER_DOWN_OUTSIDE``](/api/event/input-events#pointer_down_outside)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 将指针按下游戏对象 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DOWN_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_DRAG {#GAMEOBJECT_DRAG}

#### GAMEOBJECT_DRAG {#gameobject_drag}


**说明:**

游戏对象拖放事件 。

如果一个指针在拖动时移动,则此事件由交互式游戏对象发送 。

从游戏对象中听此事件使用: `gameObject.on('drag', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式并启用拖放。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| dragX | number | 否 | x 坐标指针当前拖动游戏对象的地方, 在世界空间中. |
| dragY | number | 否 | 指针当前在世界空间拖动游戏对象的位置的 Y 坐标 。 |


> 源码：[src/input/events/GAMEOBJECT_DRAG_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_DRAG_END {#GAMEOBJECT_DRAG_END}

#### GAMEOBJECT_DRAG_END {#gameobject_drag_end}


**说明:**

游戏对象拖曳结束事件 。

如果指针停止拖曳,此事件由交互式游戏对象发送 。

从游戏对象中听此事件使用: `gameObject.on('dragend', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式并启用拖放。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| dragX | number | 否 | 指针停止拖曳游戏对象的 x 坐标, 在世界空间中 。 |
| dragY | number | 否 | 指针停止拖曳游戏对象的地方的y坐标, 在世界空间中. |
| dropped | boolean | 否 | 游戏对象是否被丢入目标 。 |


> 源码：[src/input/events/GAMEOBJECT_DRAG_END_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_END_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_DRAG_ENTER {#GAMEOBJECT_DRAG_ENTER}

#### GAMEOBJECT_DRAG_ENTER {#gameobject_drag_enter}


**说明:**

游戏对象拖放 Enter Evention 。

如果指针将其拖入拖动目标,则此事件由交互式游戏对象发送.

从游戏对象中听此事件使用: `gameObject.on('dragenter', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式并启用拖放。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针已移动到的拖曳目标 。 |


> 源码：[src/input/events/GAMEOBJECT_DRAG_ENTER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_ENTER_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_DRAG_LEAVE {#GAMEOBJECT_DRAG_LEAVE}

#### GAMEOBJECT_DRAG_LEAVE {#gameobject_drag_leave}


**说明:**

游戏对象拖放事件 。

如果指针将其拖出拖动目标,此事件由交互式游戏对象发送.

从游戏对象中听此事件使用: `gameObject.on('dragleave', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式并启用拖放。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此指针所留下的拖曳目标 。 |


> 源码：[src/input/events/GAMEOBJECT_DRAG_LEAVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_LEAVE_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_DRAG_OVER {#GAMEOBJECT_DRAG_OVER}

#### GAMEOBJECT_DRAG_OVER {#gameobject_drag_over}


**说明:**

游戏对象拖曳事件 。

如果指针将其拖过拖曳目标,则此事件由交互式游戏对象发送.

当游戏对象首次进入拖曳目标时, 它会发出 `dragenter`事件。 如果它随后在拖曳目标内移动, 它会发出这个事件 。

从游戏对象中听此事件使用: `gameObject.on('dragover', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式并启用拖放。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 这个指针移动到这里的拖曳目标 。 |


> 源码：[src/input/events/GAMEOBJECT_DRAG_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_OVER_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_DRAG_START {#GAMEOBJECT_DRAG_START}

#### GAMEOBJECT_DRAG_START {#gameobject_drag_start}


**说明:**

游戏对象拖动启动事件 。

如果一个指针开始拖动,此事件由交互式游戏对象发送 。

从游戏对象中听此事件使用: `gameObject.on('dragstart', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式并启用拖放。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

拖曳时, 游戏对象内会设置许多有用的拖曳属性。 例如, `gameObject.input.dragStartX`、 `dragStartY`等 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| dragX | number | 否 | x 坐标指针当前拖动游戏对象的地方, 在世界空间中. |
| dragY | number | 否 | 指针当前在世界空间拖动游戏对象的位置的 Y 坐标 。 |


> 源码：[src/input/events/GAMEOBJECT_DRAG_START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DRAG_START_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_DROP {#GAMEOBJECT_DROP}

#### GAMEOBJECT_DROP {#gameobject_drop}


**说明:**

游戏对象抛放事件 。

如果指针在拖放目标上丢弃,此事件由交互式游戏对象发送 。

从游戏对象中听此事件使用: `gameObject.on('drop', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式并启用拖放。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 拖曳目标`gameObject`已经投放。 |


> 源码：[src/input/events/GAMEOBJECT_DROP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_DROP_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_MOVE {#GAMEOBJECT_MOVE}

#### GAMEOBJECT_MOVE {#gameobject_move}


**说明:**

游戏对象移动输入事件 。

如果一个指针移动到_ 任意_ 交互式游戏对象之间, 则属于 Scene 的输入插件会发出此事件 。

使用:`this.input.on('gameobjectmove', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_POINTER_MOVE``](/api/event/input-events#gameobject_pointer_move) 事件 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_MOVE``](/api/event/input-events#gameobject_pointer_move)

2. [``GAMEOBJECT_MOVE``](/api/event/input-events#gameobject_move)

3. [``POINTER_MOVE``](/api/event/input-events#pointer_move)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 指针被移动的游戏对象 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_MOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_MOVE_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_OUT {#GAMEOBJECT_OUT}

#### GAMEOBJECT_OUT {#gameobject_out}


**说明:**

游戏对象输出事件 。

如果指针移动到 __任何_交互式游戏对象,则属于 Scene 的输入插件会发出此事件。

使用:`this.input.on('gameobjectout', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_POINTER_OUT``](/api/event/input-events#gameobject_pointer_out) 事件 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_OUT``](/api/event/input-events#gameobject_pointer_out)

2. [``GAMEOBJECT_OUT``](/api/event/input-events#gameobject_out)

3. [``POINTER_OUT``](/api/event/input-events#pointer_out)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

如果指针离开游戏布局本身, 它不会触发此事件。 要处理这些案件, 请聆听 [``GAME_OUT``](/api/event/input-events#game_out) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 指针移动出来的游戏对象 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_OUT_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_OVER {#GAMEOBJECT_OVER}

#### GAMEOBJECT_OVER {#gameobject_over}


**说明:**

游戏对象超越输入事件 。

如果指针移动到 __任何_交互式游戏对象上,则此事件由属于 Scene 的输入插件发送。

使用:`this.input.on('gameobjectover', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_POINTER_OVER``](/api/event/input-events#gameobject_pointer_over) 事件 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_OVER``](/api/event/input-events#gameobject_pointer_over)

2. [``GAMEOBJECT_OVER``](/api/event/input-events#gameobject_over)

3. [``POINTER_OVER``](/api/event/input-events#pointer_over)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 指针移动到的游戏对象 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_OVER_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_POINTER_DOWN {#GAMEOBJECT_POINTER_DOWN}

#### GAMEOBJECT_POINTER_DOWN {#gameobject_pointer_down}


**说明:**

游戏对象指针下行事件.

如果一个指针被压下, 此事件由交互式游戏对象发送 。

从游戏对象中听此事件使用: `gameObject.on('pointerdown', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_DOWN``](/api/event/input-events#gameobject_pointer_down)

2. [``GAMEOBJECT_DOWN``](/api/event/input-events#gameobject_down)

3. [``POINTER_DOWN``](/api/namespace/input-events#pointer_down) or [``POINTER_DOWN_OUTSIDE``](/api/event/input-events#pointer_down_outside)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_POINTER_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_DOWN_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_POINTER_MOVE {#GAMEOBJECT_POINTER_MOVE}

#### GAMEOBJECT_POINTER_MOVE {#gameobject_pointer_move}


**说明:**

游戏对象指针移动事件 。

如果在移动指针时移动了该事件,则由交互式游戏对象发送。

从游戏对象中听此事件使用: `gameObject.on('pointermove', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_MOVE``](/api/event/input-events#gameobject_pointer_move)

2. [``GAMEOBJECT_MOVE``](/api/event/input-events#gameobject_move)

3. [``POINTER_MOVE``](/api/event/input-events#pointer_move)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_POINTER_MOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_MOVE_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_POINTER_OUT {#GAMEOBJECT_POINTER_OUT}

#### GAMEOBJECT_POINTER_OUT {#gameobject_pointer_out}


**说明:**

游戏对象指针事件( Out Event).

如果指针移动出此事件, 则由交互式游戏对象发送 。

从游戏对象中听此事件使用: `gameObject.on('pointerout', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_OUT``](/api/event/input-events#gameobject_pointer_out)

2. [``GAMEOBJECT_OUT``](/api/event/input-events#gameobject_out)

3. [``POINTER_OUT``](/api/event/input-events#pointer_out)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

如果指针离开游戏布局本身, 它不会触发此事件。 要处理这些案件, 请聆听 [``GAME_OUT``](/api/event/input-events#game_out) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_POINTER_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_OUT_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_POINTER_OVER {#GAMEOBJECT_POINTER_OVER}

#### GAMEOBJECT_POINTER_OVER {#gameobject_pointer_over}


**说明:**

游戏对象指针在事件上.

如果指针移动到它上面,此事件由交互式游戏对象发送 。

从游戏对象中听此事件使用: `gameObject.on('pointerover', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_OVER``](/api/event/input-events#gameobject_pointer_over)

2. [``GAMEOBJECT_OVER``](/api/event/input-events#gameobject_over)

3. [``POINTER_OVER``](/api/event/input-events#pointer_over)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_POINTER_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_OVER_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_POINTER_UP {#GAMEOBJECT_POINTER_UP}

#### GAMEOBJECT_POINTER_UP {#gameobject_pointer_up}


**说明:**

游戏对象指针事件(英语:Game Object Power Up Evention).

如果在游戏上方发布了指针,则此事件由交互式游戏对象发送.

从游戏对象中听此事件使用: `gameObject.on('pointerup', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_UP``](/api/event/input-events#gameobject_pointer_up)

2. [``GAMEOBJECT_UP``](/api/event/input-events#gameobject_up)

3. [``POINTER_UP``](/api/namespace/input-events#pointer_up) or [``POINTER_UP_OUTSIDE``](/api/event/input-events#pointer_up_outside)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_POINTER_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_UP_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_POINTER_WHEEL {#GAMEOBJECT_POINTER_WHEEL}

#### GAMEOBJECT_POINTER_WHEEL {#gameobject_pointer_wheel}


**说明:**

游戏对象指针轮事件.

如果指针在移动时其方向盘被移动,则此事件由交互式游戏对象发送 。

从游戏对象中听此事件使用: `gameObject.on('wheel', listener)`。 请注意, 监听器的范围被自动设定为游戏对象实例本身 。

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_WHEEL``](/api/event/input-events#gameobject_pointer_wheel)

2. [``GAMEOBJECT_WHEEL``](/api/event/input-events#gameobject_wheel)

3. [``POINTER_WHEEL``](/api/event/input-events#pointer_wheel)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| deltaX | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的水平滚动量. |
| deltaY | number | 否 | 由用户移动鼠标轮盘或类似输入设备产生的垂直滚动量。 如果用户向上滚动, 则该数值通常小于 0, 向下滚动时大于 0 。 |
| deltaZ | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的z轴滚动量. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_POINTER_WHEEL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_POINTER_WHEEL_EVENT.js#L7)  
引入版本：3.18.0


---

### GAMEOBJECT_UP {#GAMEOBJECT_UP}

#### GAMEOBJECT_UP {#gameobject_up}


**说明:**

游戏对象向上输入事件 。

如果在_ 任意_ 交互式游戏对象时发布指针, 此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('gameobjectup', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_POINTER_UP``](/api/event/input-events#gameobject_pointer_up) 事件 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_UP``](/api/event/input-events#gameobject_pointer_up)

2. [``GAMEOBJECT_UP``](/api/event/input-events#gameobject_up)

3. [``POINTER_UP``](/api/namespace/input-events#pointer_up) or [``POINTER_UP_OUTSIDE``](/api/event/input-events#pointer_up_outside)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 游戏对象 指针发布时结束 。 |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_UP_EVENT.js#L7)  
引入版本：3.0.0


---

### GAMEOBJECT_WHEEL {#GAMEOBJECT_WHEEL}

#### GAMEOBJECT_WHEEL {#gameobject_wheel}


**说明:**

游戏对象轮输入事件.

如果指针在_ 任意_ 交互式游戏对象时移动了方向盘, 则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('gameobjectwheel', listener)`,从场内听这个事件.

要接收此事件, 游戏对象必须设定为交互式。 详情请参见 [GameObject.setInteractive](/api/class/gameobjects-gameobject#setInteractive) 。

要从 _ 特定_ 游戏对象中聆听此事件, 请使用 [``GAMEOBJECT_POINTER_WHEEL``](/api/event/input-events#gameobject_pointer_wheel) 事件 。

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_WHEEL``](/api/event/input-events#gameobject_pointer_wheel)

2. [``GAMEOBJECT_WHEEL``](/api/event/input-events#gameobject_wheel)

3. [``POINTER_WHEEL``](/api/event/input-events#pointer_wheel)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 方向盘改变时, 游戏对象结束 。 |
| deltaX | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的水平滚动量. |
| deltaY | number | 否 | 由用户移动鼠标轮盘或类似输入设备产生的垂直滚动量。 如果用户向上滚动, 则该数值通常小于 0, 向下滚动时大于 0 。 |
| deltaZ | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的z轴滚动量. |
| event | [Phaser.Types.Input.EventData](/api/typedef/types-input#eventdata) | 否 | Phaser输入事件。您可以拨打`stopPropagation()`, 阻止事件流中的任何进一步。 |


> 源码：[src/input/events/GAMEOBJECT_WHEEL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/GAMEOBJECT_WHEEL_EVENT.js#L7)  
引入版本：3.18.0


---

### MANAGER_BOOT {#MANAGER_BOOT}

#### MANAGER_BOOT {#manager_boot}


**说明:**

输入管理器靴子事件 。

此内部事件由输入管理器在拖曳时发送 。


> 源码：[src/input/events/MANAGER_BOOT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/MANAGER_BOOT_EVENT.js#L7)  
引入版本：3.0.0


---

### MANAGER_PROCESS {#MANAGER_PROCESS}

#### MANAGER_PROCESS {#manager_process}


**说明:**

输入管理器处理事件 。

此内部事件由输入管理器在不使用遗留队列系统时发出,它希望输入插件能够自我更新.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/input/events/MANAGER_PROCESS_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/MANAGER_PROCESS_EVENT.js#L7)  
引入版本：3.0.0


---

### MANAGER_UPDATE {#MANAGER_UPDATE}

#### MANAGER_UPDATE {#manager_update}


**说明:**

输入管理器更新事件 。

内部事件由输入管理器发出,作为其更新步骤的一部分.


> 源码：[src/input/events/MANAGER_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/MANAGER_UPDATE_EVENT.js#L7)  
引入版本：3.0.0


---

### POINTER_DOWN {#POINTER_DOWN}

#### POINTER_DOWN {#pointer_down}


**说明:**

指向下输入事件。

如果一个指针被按下, 属于 Scene 的输入插件会发出此事件 。

使用:`this.input.on('pointerdown', listener)`,从场内听这个事件.

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_DOWN``](/api/event/input-events#gameobject_pointer_down)

2. [``GAMEOBJECT_DOWN``](/api/event/input-events#gameobject_down)

3. [``POINTER_DOWN``](/api/namespace/input-events#pointer_down) or [``POINTER_DOWN_OUTSIDE``](/api/event/input-events#pointer_down_outside)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| currentlyOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针已关闭的所有交互式游戏对象的阵列 。 |


> 源码：[src/input/events/POINTER_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_DOWN_EVENT.js#L7)  
引入版本：3.0.0


---

### POINTER_DOWN_OUTSIDE {#POINTER_DOWN_OUTSIDE}

#### POINTER_DOWN_OUTSIDE {#pointer_down_outside}


**说明:**

指向外输入事件。

如果游戏画布外的任何地方按下指针,则此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('pointerdownoutside', listener)`,从场内听这个事件.

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_DOWN``](/api/event/input-events#gameobject_pointer_down)

2. [``GAMEOBJECT_DOWN``](/api/event/input-events#gameobject_down)

3. [``POINTER_DOWN``](/api/namespace/input-events#pointer_down) or [``POINTER_DOWN_OUTSIDE``](/api/event/input-events#pointer_down_outside)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |


> 源码：[src/input/events/POINTER_DOWN_OUTSIDE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_DOWN_OUTSIDE_EVENT.js#L7)  
引入版本：3.16.1


---

### POINTER_MOVE {#POINTER_MOVE}

#### POINTER_MOVE {#pointer_move}


**说明:**

指针移动输入事件 。

如果指针移动到任何地方,此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('pointermove', listener)`,从场内听这个事件.

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_MOVE``](/api/event/input-events#gameobject_pointer_move)

2. [``GAMEOBJECT_MOVE``](/api/event/input-events#gameobject_move)

3. [``POINTER_MOVE``](/api/event/input-events#pointer_move)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| currentlyOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针已关闭的所有交互式游戏对象的阵列 。 |


> 源码：[src/input/events/POINTER_MOVE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_MOVE_EVENT.js#L7)  
引入版本：3.0.0


---

### POINTER_OUT {#POINTER_OUT}

#### POINTER_OUT {#pointer_out}


**说明:**

指针输出事件 。

如果指针从任何交互式游戏对象中移动,则该事件由属于 Scene 的输入插件发送。

使用:`this.input.on('pointerout', listener)`,从场内听这个事件.

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_OUT``](/api/event/input-events#gameobject_pointer_out)

2. [``GAMEOBJECT_OUT``](/api/event/input-events#gameobject_out)

3. [``POINTER_OUT``](/api/event/input-events#pointer_out)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

如果指针离开游戏布局本身, 它不会触发此事件。 要处理这些案件, 请聆听 [``GAME_OUT``](/api/event/input-events#game_out) 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| justOut | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含所有交互式游戏对象的阵列,指针在事件创建时移动出. |


> 源码：[src/input/events/POINTER_OUT_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_OUT_EVENT.js#L7)  
引入版本：3.0.0


---

### POINTER_OVER {#POINTER_OVER}

#### POINTER_OVER {#pointer_over}


**说明:**

指针输入事件。

如果指针移动到任何交互式游戏对象上,此事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('pointerover', listener)`,从场内听这个事件.

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_OVER``](/api/event/input-events#gameobject_pointer_over)

2. [``GAMEOBJECT_OVER``](/api/event/input-events#gameobject_over)

3. [``POINTER_OVER``](/api/event/input-events#pointer_over)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| justOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针移动到所有交互式游戏对象的阵列 。 |


> 源码：[src/input/events/POINTER_OVER_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_OVER_EVENT.js#L7)  
引入版本：3.0.0


---

### POINTER_UP {#POINTER_UP}

#### POINTER_UP {#pointer_up}


**说明:**

指向输入事件。

如果向任何地方放出指针,则该事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('pointerup', listener)`,从场内听这个事件.

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_UP``](/api/event/input-events#gameobject_pointer_up)

2. [``GAMEOBJECT_UP``](/api/event/input-events#gameobject_up)

3. [``POINTER_UP``](/api/namespace/input-events#pointer_up) or [``POINTER_UP_OUTSIDE``](/api/event/input-events#pointer_up_outside)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| currentlyOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针已关闭的所有交互式游戏对象的阵列 。 |


> 源码：[src/input/events/POINTER_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_UP_EVENT.js#L7)  
引入版本：3.0.0


---

### POINTER_UP_OUTSIDE {#POINTER_UP_OUTSIDE}

#### POINTER_UP_OUTSIDE {#pointer_up_outside}


**说明:**

指向外部输入事件。

如果在游戏画布以外的任何地方发布指针,则该事件由属于Scene的输入插件发送.

使用:`this.input.on('pointerupoutside', listener)`,从场内听这个事件.

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_UP``](/api/event/input-events#gameobject_pointer_up)

2. [``GAMEOBJECT_UP``](/api/event/input-events#gameobject_up)

3. [``POINTER_UP``](/api/namespace/input-events#pointer_up) or [``POINTER_UP_OUTSIDE``](/api/event/input-events#pointer_up_outside)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |


> 源码：[src/input/events/POINTER_UP_OUTSIDE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_UP_OUTSIDE_EVENT.js#L7)  
引入版本：3.16.1


---

### POINTER_WHEEL {#POINTER_WHEEL}

#### POINTER_WHEEL {#pointer_wheel}


**说明:**

指针轮输入事件.

如果指针的轮子更新了,则该事件由属于 Scene 的输入插件发送 。

使用:`this.input.on('wheel', listener)`,从场内听这个事件.

事件按以下顺序触发。

1. [``GAMEOBJECT_POINTER_WHEEL``](/api/event/input-events#gameobject_pointer_wheel)

2. [``GAMEOBJECT_WHEEL``](/api/event/input-events#gameobject_wheel)

3. [``POINTER_WHEEL``](/api/event/input-events#pointer_wheel)

事件按列表顺序从最高层向下触发。上层事件处理器可以阻止事件继续传播。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pointer | [Phaser.Input.Pointer](/api/class/input-pointer) | 否 | 负责触发事件的方向者. |
| currentlyOver | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 包含事件创建时指针已关闭的所有交互式游戏对象的阵列 。 |
| deltaX | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的水平滚动量. |
| deltaY | number | 否 | 由用户移动鼠标轮盘或类似输入设备产生的垂直滚动量。 如果用户向上滚动, 则该数值通常小于 0, 向下滚动时大于 0 。 |
| deltaZ | number | 否 | 由用户移动鼠标轮或类似输入设备而发生的z轴滚动量. |


> 源码：[src/input/events/POINTER_WHEEL_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTER_WHEEL_EVENT.js#L7)  
引入版本：3.18.0


---

### POINTERLOCK_CHANGE {#POINTERLOCK_CHANGE}

#### POINTERLOCK_CHANGE {#pointerlock_change}


**说明:**

输入管理器 指针锁定改变事件 。

此事件由输入管理器在处理本地的指针锁变换 DOM 事件时发送 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | Event | 否 | 本地的DOM事件. |
| locked | boolean | 否 | 鼠标指针的锁定状态 。 |


> 源码：[src/input/events/POINTERLOCK_CHANGE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/POINTERLOCK_CHANGE_EVENT.js#L7)  
引入版本：3.0.0


---

### PRE_UPDATE {#PRE_UPDATE}

#### PRE_UPDATE {#pre_update}


**说明:**

输入插件更新前事件 。

此内部事件由输入插件在其 `preUpdate` 方法的开始时发送。 此钩子是专门为输入插件设计的, 但也可以从用户- land 代码中听取 。


> 源码：[src/input/events/PRE_UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/PRE_UPDATE_EVENT.js#L7)  
引入版本：3.0.0


---

### SHUTDOWN {#SHUTDOWN}

#### SHUTDOWN {#shutdown}


**说明:**

输入插件关闭事件 。

内部事件由输入插件在关闭时发出,信号到其所有系统关闭自己.


> 源码：[src/input/events/SHUTDOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/SHUTDOWN_EVENT.js#L7)  
引入版本：3.0.0


---

### START {#START}

#### START {#start}


**说明:**

输入插件启动事件 。

内部事件由输入插件在完成设置后发送,信号到其所有内部系统启动.


> 源码：[src/input/events/START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/START_EVENT.js#L7)  
引入版本：3.0.0


---

### UPDATE {#UPDATE}

#### UPDATE {#update}


**说明:**

输入插件更新事件 。

此内部事件由输入插件在其 `update` 方法的开始时发送。 此钩子是专门为输入插件设计的, 但也可以从用户- land 代码中听取 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/input/events/UPDATE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/events/UPDATE_EVENT.js#L7)  
引入版本：3.0.0


---

---
