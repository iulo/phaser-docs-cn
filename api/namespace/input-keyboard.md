# Phaser.Input.Keyboard {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/input-keyboard)

Scope: 
static
> 源码：[src/input/keyboard/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/index.js#L7)  


## 静态函数 {#static-functions}

- [Key](/api/class/input-keyboard-key)
- [KeyboardManager](/api/class/input-keyboard-keyboardmanager)
- [KeyboardPlugin](/api/class/input-keyboard-keyboardplugin)
- [KeyCombo](/api/class/input-keyboard-keycombo)
## 静态函数 {#static-functions-1}

### DownDuration {#DownDuration}

#### \<static> DownDuration(key, [duration]) {#static-downdurationkey-duration}


**说明:**

返回值 `true` 如果按键在 `duration` 值,基于当前游戏时钟时间。或 `false` 如果不是没下来,或者比规定的时间更早被压下来。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 |  | 要测试的键对象 。 |
| duration | number | 是 | 50 | 时间长度,以毫秒计,其中键必须按下。 |


**返回值:** boolean - 如果钥匙在`duration`米前按下的话,就按`true`,否则按`false`.


> 源码：[src/input/keyboard/keys/DownDuration.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/DownDuration.js#L7)  
引入版本：3.0.0


---

### JustDown {#JustDown}

#### \<static> JustDown(key) {#static-justdownkey}


**说明:**

justDown值允许您测试是否刚刚按下此键 。

当你检查这个值时,如果键下,它会返回`true`,否则返回`false`.

您只能每按下一次 justDown。 它只能返回 `true`一次, 直到键被再次发布并按下。 这样您就可以在您想要检查此键是否在下方没有使用事件的情况下使用, 如在核心游戏循环中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 检查的钥匙 看看它是不是刚刚下来。 |


**返回值:** boolean - 如果按键是按的,那么就按`true`,否则按`false`.


> 源码：[src/input/keyboard/keys/JustDown.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/JustDown.js#L7)  
引入版本：3.0.0


---

### JustUp {#JustUp}

#### \<static> JustUp(key) {#static-justupkey}


**说明:**

justUp值允许您测试此键是否刚刚被发布 。

检查此值时, 将返回 `true` 如果钥匙是上,否则 `false`.

您只能每一次调用 JustUp 键。 它只能返回一次 `true`, 直到按下键并再次放出。 这样您就可以在您想要检查是否该键升起时使用它, 如在核心游戏循环中使用此键 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 检查的钥匙 看看是不是刚刚起步 |


**返回值:** boolean - 如果钥匙刚刚放出来,就用`true`,否则用`false`.


> 源码：[src/input/keyboard/keys/JustUp.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/JustUp.js#L7)  
引入版本：3.0.0


---

### UpDuration {#UpDuration}

#### \<static> UpDuration(key, [duration]) {#static-updurationkey-duration}


**说明:**

如果键在给定的 `duration` 值范围内释放, 则返回 `true`。 如果键尚未打开, 或者比给定的时钟时间早释放, 返回 `false` 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 |  | 要测试的键对象 。 |
| duration | number | 是 | 50 | 时间,以毫秒计,其中键必须已经放出. |


**返回值:** boolean - 如果钥匙在`duration` mss 之前就释放了,那么就用`true`,否则用`false`.


> 源码：[src/input/keyboard/keys/UpDuration.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/UpDuration.js#L7)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-2}

- [Events](/api/namespace/input-keyboard-events)
- [KeyCodes](/api/namespace/input-keyboard-keycodes)

---
