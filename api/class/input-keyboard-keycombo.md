# KeyCombo {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-keyboard-keycombo)

一个键盘Combo会从键盘中监听一个特定的串键,当它收到键盘时,它会从键盘管理器中发出一个`keycombomatch`事件.

需要听的密钥可以定义为:

字符串(即“ ATARI”) 组合整数( 键码) 或字符串, 或两个组合的组合 。 组合对象( 如“ 键对象”) 具有公共“ keyCode” 属性

例如,要听 Konami 代码( 上, 上, 下, 下, 左, 右, 左, 右, b, a, 输入) , 您可以通过以下数组密钥代码 :

```javascript
this.input.keyboard.createCombo([ 38, 38, 40, 40, 37, 39, 37, 39, 66, 65, 13 ], { resetOnMatch: true });

this.input.keyboard.on('keycombomatch', function (event) {
    console.log('Konami Code entered!');
});
```

或者,为输入PHASER一词的用户听:

```javascript
this.input.keyboard.createCombo('PHASER');
```

**构造函数**

`new KeyCombo(keyboardPlugin, keys, [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keyboardPlugin | [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) | 否 | 键盘插件的引用 。 |
| keys | string \| Array.\<number> | Array.\<object> | 否 | 构成这个组合的密钥 。 |
| config | [Phaser.Types.Input.Keyboard.KeyComboConfig](/api/typedef/types-input-keyboard#keycomboconfig) | 是 | 一个密钥组合对象 。 |

---


**作用域**: static

> 源码：[src/input/keyboard/combo/KeyCombo.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L13)  
引入版本：3.0.0

## 公开成员 {#public-members}

### current {#current}

#### current: number {#current-number}


**说明:**

组合组正在等待的当前 keyCode.


> 源码：[src/input/keyboard/combo/KeyCombo.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L114)  
引入版本：3.0.0


---

### deleteOnMatch {#deleteOnMatch}

#### deleteOnMatch: boolean {#deleteonmatch-boolean}


**说明:**

如果组合成功匹配, 此 KeyCombo 实例将自动毁灭自身 。


> 源码：[src/input/keyboard/combo/KeyCombo.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L202)  
引入版本：3.0.0


---

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

用于控制此密钥是否正在积极处理密钥的旗帜 。


> 源码：[src/input/keyboard/combo/KeyCombo.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L74)  
引入版本：3.0.0


---

### index {#index}

#### index: number {#index-number}


**说明:**

`keyCodes`阵列中等待的密钥的当前索引 。


> 源码：[src/input/keyboard/combo/KeyCombo.js#L123](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L123)  
引入版本：3.0.0


---

### keyCodes {#keyCodes}

#### keyCodes: array {#keycodes-array}


**说明:**

包含此组合的密钥代码组 。


> 源码：[src/input/keyboard/combo/KeyCombo.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L84)  
引入版本：3.0.0


---

### manager {#manager}

#### manager: [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) {#manager-phaserinputkeyboardkeyboardplugin}


**说明:**

键盘插件的引用


> 源码：[src/input/keyboard/combo/KeyCombo.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L65)  
引入版本：3.0.0


---

### matched {#matched}

#### matched: boolean {#matched-boolean}


**说明:**

这个密钥Combo是否匹配?


> 源码：[src/input/keyboard/combo/KeyCombo.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L152)  
引入版本：3.0.0


---

### maxKeyDelay {#maxKeyDelay}

#### maxKeyDelay: number {#maxkeydelay-number}


**说明:**

每个密钥按键之间的最大延迟 。 重置此组合 。 0 表示禁用 。


> 源码：[src/input/keyboard/combo/KeyCombo.js#L182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L182)  
引入版本：3.0.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

组合完成多远?值在 0 到 1 之间 。


> 源码：[src/input/keyboard/combo/KeyCombo.js#L252](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L252)  
引入版本：3.0.0


---

### resetOnMatch {#resetOnMatch}

#### resetOnMatch: boolean {#resetonmatch-boolean}


**说明:**

如果组合键之前已经匹配,用户再次按下组合键的第一个键,组合键会重置.


> 源码：[src/input/keyboard/combo/KeyCombo.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L192)  
引入版本：3.0.0


---

### resetOnWrongKey {#resetOnWrongKey}

#### resetOnWrongKey: boolean {#resetonwrongkey-boolean}


**说明:**

如果用户按错键,组合序列会被重置到起始.


> 源码：[src/input/keyboard/combo/KeyCombo.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L172)  
引入版本：3.0.0


---

### size {#size}

#### size: number {#size-number}


**说明:**

此组合的长度( 键码)


> 源码：[src/input/keyboard/combo/KeyCombo.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L133)  
引入版本：3.0.0


---

### timeLastMatched {#timeLastMatched}

#### timeLastMatched: number {#timelastmatched-number}


**说明:**

组合键中前一键匹配的时间 。


> 源码：[src/input/keyboard/combo/KeyCombo.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L142)  
引入版本：3.0.0


---

### timeMatched {#timeMatched}

#### timeMatched: number {#timematched-number}


**说明:**

整个组合的时间都匹配.


> 源码：[src/input/keyboard/combo/KeyCombo.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L162)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这把钥匙 Combo 及其所有参考文献 。


> 源码：[src/input/keyboard/combo/KeyCombo.js#L269](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/KeyCombo.js#L269)  
引入版本：3.0.0


---

---
