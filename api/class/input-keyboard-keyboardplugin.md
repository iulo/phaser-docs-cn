# KeyboardPlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/input-keyboard-keyboardplugin)

键盘插件是一个属于Scene自有输入系统的输入插件.

其作用是聆听原生的DOM键盘事件,然后处理.

您不需要直接创建此类, 输入系统会自动创建实例 。

您可以使用 `this.input.keyboard` 从场景内部访问它。 例如, 你可以:

```javascript
this.input.keyboard.on('keydown', callback, context);
```

或者,听一个特定的密钥:

```javascript
this.input.keyboard.on('keydown-A', callback, context);
```

您也可以创建关键对象, 然后在游戏循环中进行投票 :

```javascript
var spaceBar = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);
```

如果您有多个平行的 Scase, 每一个尝试获得键盘输入, 请确保禁用它们上抓取它们, 以阻止它们从列表中的另一个 Scase 中窃取输入 。 您可以在 Scase 中使用 `this.input.keyboard.enabled = false` 来阻止所有输入, 或者 `this.input.keyboard.preventDefault = false` 来阻止 Scase 停止在另一个 Scase 上的输入 。

_Note_:由于被称为鬼怪的硬件限制,许多键盘无法处理某些组合的密钥,详见[http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/](http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/),并使用网站[https://w3c.github.io/uievents/tools/key-event-viewer.html](https://w3c.github.io/uievents/tools/key-event-viewer.html)在浏览器中测试您的n键支持.

请注意某些浏览器扩展可以禁用或覆盖 Phaser键盘处理。 例如, Chrome 扩展 vimium 已被知道可以禁用 Phaser 使用 D 键, 而 EverNote 则禁用反键。 还有其它的。 因此, 请在打开 Phaser 键问题前检查您的扩展名, 否则无法工作 。

**构造函数**

`new KeyboardPlugin(sceneInputPlugin)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| sceneInputPlugin | [Phaser.Input.InputPlugin](/api/class/input-inputplugin) | 否 | 键盘插件属于的 Scene 输入插件的引用 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/input/keyboard/KeyboardPlugin.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L21)  
引入版本：3.10.0

## 公开成员 {#public-members}

### combos {#combos}

#### combos: Array.\<[Phaser.Input.Keyboard.KeyCombo](/api/class/input-keyboard-keycombo)> {#combos-arrayphaserinputkeyboardkeycombo}


**说明:**

要处理的 KeyCombo 对象阵列 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L142)  
引入版本：3.10.0


---

### enabled {#enabled}

#### enabled: boolean {#enabled-boolean}


**说明:**

如果启用此键盘插件, 则会显示布林值。 可以切换到苍蝇上 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L122)  
引入版本：3.10.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

参考核心游戏,这样我们就可以听取可见事件.


> 源码：[src/input/keyboard/KeyboardPlugin.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L77)  
引入版本：3.16.0


---

### keys {#keys}

#### keys: Array.\<[Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key)> {#keys-arrayphaserinputkeyboardkey}


**说明:**

处理的密钥对象阵列 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L133)  
引入版本：3.10.0


---

### manager {#manager}

#### manager: [Phaser.Input.Keyboard.KeyboardManager](/api/class/input-keyboard-keyboardmanager) {#manager-phaserinputkeyboardkeyboardmanager}


**说明:**

环球键盘管理器的参考文献.


> 源码：[src/input/keyboard/KeyboardPlugin.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L113)  
引入版本：3.16.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

引用此输入插件负责的场景 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L86](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L86)  
引入版本：3.10.0


---

### sceneInputPlugin {#sceneInputPlugin}

#### sceneInputPlugin: [Phaser.Input.InputPlugin](/api/class/input-inputplugin) {#sceneinputplugin-phaserinputinputplugin}


**说明:**

引用创建此键盘插件的场景输入插件 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L104)  
引入版本：3.10.0


---

### settings {#settings}

#### settings: [Phaser.Types.Scenes.SettingsObject](/api/typedef/types-scenes#settingsobject) {#settings-phasertypesscenessettingsobject}


**说明:**

用于参考场景系统设置的参考文献 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L95)  
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

### addCapture {#addCapture}

#### \<instance> addCapture(keycode) {#instance-addcapturekeycode}


**说明:**

默认情况下, 按下一个键的 Phaser 将不会阻止事件向浏览器传播。 有些键会令您感到烦恼, 例如箭头键或空间栏, 这使得浏览器窗口滚动 。

这种`addCapture`方法可以消耗特定键的键盘事件,所以不会泡上浏览器,引起默认行为.

请注意键盘抓取是全局的。 这意味着, 如果您从场景内调用这种方法, 也就是说防止空间 BAR 触发页卷轴, 那么它将会防止您游戏中的任何场景, 而不仅仅是调用它 。

您可以通过一个单一的密钥代码值 :

```javascript
this.input.keyboard.addCapture(62);
```

一系列密钥代码 :

```javascript
this.input.keyboard.addCapture([ 62, 63, 64 ]);
```

或者,一个逗号限制字符串:

```javascript
this.input.keyboard.addCapture('W,S,A,D');
```

要使用非α数字键,请使用一个字符串,如“ UP”、“SPACE” 或“ LEFT”。

也可以提供混合字符串和密钥代码整数的数组.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keycode | string \| number | Array.\<number> | Array.\<any> | 否 | 启用事件抓取的密钥代码 。 |


**返回值:** [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) - 此键盘缓冲对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L243)  
引入版本：3.16.0


---

### addKey {#addKey}

#### \<instance> addKey(key, [enableCapture], [emitOnRepeat]) {#instance-addkeykey-enablecapture-emitonrepeat}


**说明:**

将密钥对象添加到此键盘插件中。

给定的参数可以是现有的密钥对象,字符串,如`A`或`SPACE`,也可以是密钥代码值.

如果给定了密钥对象,且一个对象已经存在匹配同一密钥代码,则现有的对象会被替换为新的对象.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) \| string | number | 否 |  | 或键对象,字符串,如`A`或`SPACE`,或键码值. |
| enableCapture | boolean | 是 | true | 在本地 DOM 浏览器事件上自动调用 `preventDefault` , 用于添加密钥代码 。 |
| emitOnRepeat | boolean | 是 | false | 控件 : 键在被扣下时会连续发出一个“ 下” 事件( 真实) , 或只发出一次事件( 假的, 默认的) 。 |


**返回值:** [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) - 新建的密钥对象, 或者如果在密钥数组中已经存在的话, 引用它 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L475](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L475)  
引入版本：3.10.0


---

### addKeys {#addKeys}

#### \<instance> addKeys(keys, [enableCapture], [emitOnRepeat]) {#instance-addkeyskeys-enablecapture-emitonrepeat}


**说明:**

实用方法创建包含用户所选的热键的对象 。

例如:

```javascript
this.input.keyboard.addKeys({ 'up': Phaser.Input.Keyboard.KeyCodes.W, 'down': Phaser.Input.Keyboard.KeyCodes.S });
```

返回含有属性的对象( )`up` 财务报告和已审计财务报表 `down`) 绘制到W和S [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) 对象。

也可以通过逗号分隔的字符串 :

```javascript
this.input.keyboard.addKeys('W,S,A,D');
```

将带有W、S、A和D属性的天体映射到相关的密钥对象。

要使用非α数字键,请使用一个字符串,如“ UP”、“SPACE” 或“ LEFT”。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| keys | object \| string | 否 |  | 包含密钥代码或逗号分隔字符串的对象。 |
| enableCapture | boolean | 是 | true | 在本地 DOM 浏览器事件上自动调用 `preventDefault` , 用于添加密钥代码 。 |
| emitOnRepeat | boolean | 是 | false | 控件 : 键在被扣下时会连续发出一个“ 下” 事件( 真实) , 或只发出一次事件( 假的, 默认的) 。 |


**返回值:** object - 包含密钥对象的天体,映射到输入属性。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L413](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L413)  
引入版本：3.10.0


---

### checkDown {#checkDown}

#### \<instance> checkDown(key, [duration]) {#instance-checkdownkey-duration}


**说明:**

检查当前是否按住给定的密钥对象 。

这种方法与直接检查`Key.isDown`属性的区别在于, 您可以为这种方法提供持续时间。 例如, 如果您想要按键来发射子弹, 但你只想它能够每100ms发射一次, 那么您可以使用每100ms的`duration`来调用这种方法, 它只会每100ms返回`true` 。

如果键盘插件已被禁用,此方法将总是返回 `false`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 |  | 一个密钥对象 。 |
| duration | number | 是 | 0 | 必须在多长时间后才能将关键值视为已下调。 |


**返回值:** boolean - 如果在指定期限内键被下调,则`true`,否则则`false`.


> 源码：[src/input/keyboard/KeyboardPlugin.js#L687](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L687)  
引入版本：3.11.0


---

### clearCaptures {#clearCaptures}

#### \<instance> clearCaptures() {#instance-clearcaptures}


**说明:**

删除所有键盘抓取 。

请注意, 这是一个全局变化。 它会清除您游戏中的所有事件捕获, 而不仅仅是针对这个特定场景 。


**返回值:** [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) - 此键盘缓冲对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L376](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L376)  
引入版本：3.16.0


---

### createCombo {#createCombo}

#### \<instance> createCombo(keys, [config]) {#instance-createcombokeys-config}


**说明:**

创建新的 KeyCombo 。

一个键盘Combo会从键盘中听到一个特定的键串,当它收到键盘时,它会从这个键盘插件中发出一个`keycombomatch`事件.

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

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keys | string \| Array.\<number> | Array.\<object> | 否 | 构成这个组合的密钥 。 |
| config | [Phaser.Types.Input.Keyboard.KeyComboConfig](/api/typedef/types-input-keyboard#keycomboconfig) | 是 | 一个密钥组合对象 。 |


**返回值:** [Phaser.Input.Keyboard.KeyCombo](/api/class/input-keyboard-keycombo) - 新的 KeyCombo 对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L645](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L645)  
引入版本：3.10.0


---

### createCursorKeys {#createCursorKeys}

#### \<instance> createCursorKeys() {#instance-createcursorkeys}


**说明:**

创建并返回包含6个上、下、左和右热键以及空间栏和Shift的对象。


**返回值:** [Phaser.Types.Input.Keyboard.CursorKeys](/api/typedef/types-input-keyboard#cursorkeys) - 包含属性的对象 : `up`, `down`, `left`, `right`, `space` 财务报告和已审计财务报表 `shift`.


> 源码：[src/input/keyboard/KeyboardPlugin.js#L393](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L393)  
引入版本：3.10.0


---

### disableGlobalCapture {#disableGlobalCapture}

#### \<instance> disableGlobalCapture() {#instance-disableglobalcapture}


**说明:**

禁用 Phaser 来阻止您定义的任何密钥捕获, 而不会实际删除它们。 您可以使用此功能来暂时禁用事件捕获, 例如, 如果您将此功能交换到 DOM 元素 。


**返回值:** [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) - 此键盘缓冲对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L360)  
引入版本：3.16.0


---

### enableGlobalCapture {#enableGlobalCapture}

#### \<instance> enableGlobalCapture() {#instance-enableglobalcapture}


**说明:**

允许 Phaser 防止您在浏览器上浮起时定义的任何密钥捕获。 如果您通过 `disableGlobalCapture` 暂停了它, 您可以使用此功能来重新启用事件捕获 。


**返回值:** [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) - 此键盘缓冲对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L344](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L344)  
引入版本：3.16.0


---

### getCaptures {#getCaptures}

#### \<instance> getCaptures() {#instance-getcaptures}


**说明:**

返回包含当前启用的所有键盘抓取的数组 。


**返回值:** Array.\<number> - 包含当前所有抓取密钥代码的数组 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L331](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L331)  
引入版本：3.16.0


---

### isActive {#isActive}

#### \<instance> isActive() {#instance-isactive}


**说明:**

检查此插件及其所属的景色是否活动 。


**返回值:** boolean - `true` 如果插件和它所属的场景是活动.


> 源码：[src/input/keyboard/KeyboardPlugin.js#L230](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L230)  
引入版本：3.10.0


---

### removeAllKeys {#removeAllKeys}

#### \<instance> removeAllKeys([destroy], [removeCapture]) {#instance-removeallkeysdestroy-removecapture}


**说明:**

删除由_This_键盘插件创建的所有关键对象。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| destroy | boolean | 是 | false | 给每个删除的密钥对象打电话 `Key.destroy` ? |
| removeCapture | boolean | 是 | false | 删除此插件拥有的密钥对象的全部密钥抓取 ? |


**返回值:** [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) - 此键盘缓冲对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L604](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L604)  
引入版本：3.24.0


---

### removeCapture {#removeCapture}

#### \<instance> removeCapture(keycode) {#instance-removecapturekeycode}


**说明:**

删除已有的密钥抓取。

请注意键盘抓取是全局的。 这意味着, 如果您从场景内调用这种方法, 以删除抓取的键, 那么它将会从游戏中切除, 而不仅仅是调用它 。

您可以通过一个单一的密钥代码值 :

```javascript
this.input.keyboard.removeCapture(62);
```

一系列密钥代码 :

```javascript
this.input.keyboard.removeCapture([ 62, 63, 64 ]);
```

或者,一个逗号限制字符串:

```javascript
this.input.keyboard.removeCapture('W,S,A,D');
```

要使用非α数字键,请使用一个字符串,如“ UP”、“SPACE” 或“ LEFT”。

也可以提供混合字符串和密钥代码整数的数组.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keycode | string \| number | Array.\<number> | Array.\<any> | 否 | 禁用事件抓取的密钥代码 。 |


**返回值:** [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) - 此键盘缓冲对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L289)  
引入版本：3.16.0


---

### removeKey {#removeKey}

#### \<instance> removeKey(key, [destroy], [removeCapture]) {#instance-removekeykey-destroy-removecapture}


**说明:**

从此键盘插件中删除密钥对象。

给定的参数可以是键对象,字符串,如`A`或`SPACE`,也可以是键码值.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) \| string | number | 否 |  | 或键对象,字符串,如`A`或`SPACE`,或键码值. |
| destroy | boolean | 是 | false | 在已删除的密钥对象上拨打 `Key.destroy` ? |
| removeCapture | boolean | 是 | false | 从被捕获中移除此密钥 ? 只有在设定用于创建时才适用 。 |


**返回值:** [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) - 此键盘缓冲对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L541](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L541)  
引入版本：3.10.0


---

### resetKeys {#resetKeys}

#### \<instance> resetKeys() {#instance-resetkeys}


**说明:**

将_this_键盘插件创建的所有密钥对象重置到默认的未压态。 这只能重置通过 `addKey`、 `addKeys` 或 `createCursorKeys` 方法创建的密钥。 如果您直接创建了密钥对象, 您需要自己重置它 。

当键盘插件关闭时,这种方法会自动被称作,但可以在任何需要的时候直接被引用.


**返回值:** [Phaser.Input.Keyboard.KeyboardPlugin](/api/class/input-keyboard-keyboardplugin) - 此键盘缓冲对象 。


> 源码：[src/input/keyboard/KeyboardPlugin.js#L840](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/KeyboardPlugin.js#L840)  
引入版本：3.15.0


---

---
