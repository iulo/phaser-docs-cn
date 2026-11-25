# Types.Input.Keyboard {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-input-keyboard)

## CursorKeys {#cursorkeys}

### \<static> CursorKeys {#static-cursorkeys}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| up | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | UP箭头键的键对象映射 。 |
| down | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 向下箭头键绘制键对象映射 。 |
| left | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 向 LEFT 箭头键绘制键对象映射 。 |
| right | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 右箭头键的键对象映射 。 |
| space | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 空间 BAR 键的键对象映射 。 |
| shift | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 用于 SHIFT 键的键对象映射 。 |

**类型**: object

**所属**: Phaser.Types.Input.Keyboard
> 源码：[src/input/keyboard/typedefs/CursorKeys.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/typedefs/CursorKeys.js#L1)  
引入版本：3.0.0

---

## KeyboardKeydownCallback {#keyboardkeydowncallback}

### \<static> KeyboardKeydownCallback {#static-keyboardkeydowncallback}

**类型**: function

**所属**: Phaser.Types.Input.Keyboard
> 源码：[src/input/keyboard/typedefs/KeyboardKeydownCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/typedefs/KeyboardKeydownCallback.js#L1)  
引入版本：3.0.0

---

## KeyComboConfig {#keycomboconfig}

### \<static> KeyComboConfig {#static-keycomboconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| resetOnWrongKey | boolean | 是 | true | 如果他们按错了键 我们是否要重设组合? |
| maxKeyDelay | number | 是 | 0 | 每个键按键之间的最大延迟 。 重置此组合 。 0 表示禁用 。 |
| resetOnMatch | boolean | 是 | false | 如果之前匹配, 他们又按下组合键的第一个键, 它会重置吗 ? |
| deleteOnMatch | boolean | 是 | false | 如果组合匹配, 它会删除它自己吗 ? |

**类型**: object

**所属**: Phaser.Types.Input.Keyboard
> 源码：[src/input/keyboard/typedefs/KeyComboConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/typedefs/KeyComboConfig.js#L1)  
引入版本：3.0.0

---

---
