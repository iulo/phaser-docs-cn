# GamepadPlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-gamepad-gamepadplugin)

Gamepad插件是属于Scene自有输入系统的输入插件.

其作用是聆听原生的DOM Gamepad事件,然后处理.

您不需要直接创建此类, 输入系统会自动创建实例 。

你可以从场内使用`this.input.gamepad`访问它.

要监听正在连接的游戏盘 :

```javascript
this.input.gamepad.once('connected', function (pad) {
    //   'pad' is a reference to the gamepad that was just connected
});
```

请注意,浏览器可能要求您在允许您访问游戏盘之前按下一个按钮, 原因有安全性。 但是, 它也可能已经信任该页面, 在这种情况下您不会得到“ 连接” 事件, 而是应该检查 `GamepadPlugin.total` , 看看它是否认为有游戏盘已经连接过 。

一旦收到连接事件,或对游戏板进行投票,发现它们已启用,您可以通过内置属性访问它们 `GamepadPlugin.pad1` 改为: `pad4`,最多4个游戏垫。在游戏盘中,您可以查看其按钮和轴杆。请查看游戏盘上可用的属性和方法。 `Gamepad` 课上详细信息。

截至2020年9月,Chrome,以及可能的其他浏览器,很快将开始要求请求访问Gamepad API的游戏在SSL下运行,如果没有,它们会积极屏蔽API的访问.

关于浏览器中的Gamepad支持的更多信息,请参见以下资源: 页面存档备份,存于互联网档案馆,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,腾讯网,网易网,网易网,网易网,网易网,网易网,网易网,网易网,网易网,网易网,网易网,网易网,网易网,网易网易网,网易网易网,网易网易网,网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网易网网易网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网网微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微微

[https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API) [https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API) [https://www.smashingmagazine.com/2015/11/gamepad-api-in-web-games/](https://www.smashingmagazine.com/2015/11/gamepad-api-in-web-games/) [http://html5gamepad.com/](http://html5gamepad.com/)

**构造函数**

`new GamepadPlugin(sceneInputPlugin)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sceneInputPlugin | [Phaser.Input.InputPlugin](/api/class/input-inputplugin) | 否 | 引用 Gamepad Plugin 所属的场景输入插件 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/input/gamepad/GamepadPlugin.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L15)  
引入版本：3.10.0

## 公开成员 {#public-members}

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

如果启用 Gamepad 管理器, 则控制布尔值。 可以在运行时切换 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L98)  
引入版本：3.10.0


---

### gamepads {#gamepads}

#### gamepads: Array.\<[Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad)> {#gamepads-arrayphaserinputgamepadgamepad}


**说明:**

连接的 Gamepad 阵列 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L119](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L119)  
引入版本：3.10.0


---

### pad1 {#pad1}

#### pad1: [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) {#pad1-phaserinputgamepadgamepad}


**说明:**

参考了第一个连接的 Gamepad 。

如果没有连接到任何一个垫,或者浏览器尚未发布一个游戏板连接,则此选项将无法定义,即使一个Gamepad被插入,但还没有按下任何按钮,也可能发生这种情况.


> 源码：[src/input/gamepad/GamepadPlugin.js#L558](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L558)  
引入版本：3.10.0


---

### pad2 {#pad2}

#### pad2: [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) {#pad2-phaserinputgamepadgamepad}


**说明:**

参考第二个连接的 Gamepad 。

如果没有连接到任何一个垫,或者浏览器尚未发布一个游戏板连接,则此选项将无法定义,即使一个Gamepad被插入,但还没有按下任何按钮,也可能发生这种情况.


> 源码：[src/input/gamepad/GamepadPlugin.js#L578](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L578)  
引入版本：3.10.0


---

### pad3 {#pad3}

#### pad3: [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) {#pad3-phaserinputgamepadgamepad}


**说明:**

第三个连接的 Gamepad 的参考文献 。

如果没有连接到任何一个垫,或者浏览器尚未发布一个游戏板连接,则此选项将无法定义,即使一个Gamepad被插入,但还没有按下任何按钮,也可能发生这种情况.


> 源码：[src/input/gamepad/GamepadPlugin.js#L598](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L598)  
引入版本：3.10.0


---

### pad4 {#pad4}

#### pad4: [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) {#pad4-phaserinputgamepadgamepad}


**说明:**

参考第四部连接的Gamepad.

如果没有连接到任何一个垫,或者浏览器尚未发布一个游戏板连接,则此选项将无法定义,即使一个Gamepad被插入,但还没有按下任何按钮,也可能发生这种情况.


> 源码：[src/input/gamepad/GamepadPlugin.js#L618](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L618)  
引入版本：3.10.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

引用此输入插件负责的场景 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L71](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L71)  
引入版本：3.10.0


---

### sceneInputPlugin {#sceneInputPlugin}

#### sceneInputPlugin: [Phaser.Input.InputPlugin](/api/class/input-inputplugin) {#sceneinputplugin-phaserinputinputplugin}


**说明:**

引用创建此 Gamepad 插件的场景输入插件 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L89)  
引入版本：3.10.0


---

### settings {#settings}

#### settings: [Phaser.Types.Scenes.SettingsObject](/api/typedef/types-scenes#settingsobject) {#settings-phasertypesscenessettingsobject}


**说明:**

用于参考场景系统设置的参考文献 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L80)  
引入版本：3.10.0


---

### target {#target}

#### target: any {#target-any}


**说明:**

Gamepad Event 目标, 定义在 Game Config 中。 通常情况下, 浏览器窗口, 但可以是任何交互式 DOM 元素 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L109)  
引入版本：3.10.0


---

### total {#total}

#### total: number {#total-number}


**说明:**

连接的游戏垫子的总数 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L542](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L542)  
引入版本：3.10.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)




---

## 公开方法 {#public-methods}

### disconnectAll {#disconnectAll}

#### \<instance> disconnectAll() {#instance-disconnectall}


**说明:**

断开当前所有 Gamepad 的连接 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L312)  
引入版本：3.10.0


---

### getAll {#getAll}

#### \<instance> getAll() {#instance-getall}


**说明:**

返回当前连接的 Gamepad 数组 。


**返回值:** Array.\<[Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad)> - 一组当前连接的 Gamepad 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L407](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L407)  
引入版本：3.10.0


---

### getPad {#getPad}

#### \<instance> getPad(index) {#instance-getpadindex}


**说明:**

根据给定的索引值, 查出一个单独的 Gamepad 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 游戏板的索引要获取 。 |


**返回值:** [Phaser.Input.Gamepad.Gamepad](/api/class/input-gamepad-gamepad) - 匹配给定索引的 Gamepad, 或找不到未定义的 。


> 源码：[src/input/gamepad/GamepadPlugin.js#L431](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L431)  
引入版本：3.10.0


---

### isActive {#isActive}

#### \<instance> isActive() {#instance-isactive}


**说明:**

检查此插件及其所属的景色是否活动 。


**返回值:** boolean - `true` 如果插件和它所属的场景是活动.


> 源码：[src/input/gamepad/GamepadPlugin.js#L234](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/gamepad/GamepadPlugin.js#L234)  
引入版本：3.10.0


---

---
