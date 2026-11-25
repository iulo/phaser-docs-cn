# Phaser.Input.Keyboard.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/input-keyboard-events)

Scope: 
static
> 源码：[src/input/keyboard/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/index.js#L7)  


## 静态函数 {#static-functions}

### ANY_KEY_DOWN {#ANY_KEY_DOWN}

#### ANY_KEY_DOWN {#any_key_down}


**说明:**

全球钥匙下架事件.

当键盘上的任何键被按下时,此事件由键盘插件发送 。

使用:`this.input.keyboard.on('keydown', listener)`,从场内听这个事件.

您也可以监听按下的特定键。详情请参见 [``Keyboard.Events.KEY_DOWN``](/api/event/input-keyboard-events#key_down) 。

最后,您可以创建键对象, 您也可以从中听到事件。 详情请参见 [``Keyboard.Events.DOWN``](/api/event/input-keyboard-events#down) 。

_Note_:由于被称为鬼神的硬件限制,许多键盘无法处理某些组合的键. 读[此篇关于鬼神的文章]QQlink [http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/](http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/)]以了解细节.

另外,请注意,一些浏览器扩展可以禁用或覆盖 Phaser键盘处理。例如, Chrome扩展维米被已知可以禁用 Phaser 使用 D 键, 而 EverNote 则禁用反键。 还有其它。 如果您发现您有特定的键不能工作, 请检查您的扩展 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 了解更多按下键、 任何修改符等信息 。 |


> 源码：[src/input/keyboard/events/ANY_KEY_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/ANY_KEY_DOWN_EVENT.js#L7)  
引入版本：3.0.0


---

### ANY_KEY_UP {#ANY_KEY_UP}

#### ANY_KEY_UP {#any_key_up}


**说明:**

全球键起事件.

当键盘上的任何键被发布时,此事件由键盘插件发出.

使用:`this.input.keyboard.on('keyup', listener)`,从场内听这个事件.

您也可以监听正在发布的特定键。详情请参见 [``Keyboard.Events.KEY_UP``](/api/event/input-keyboard-events#key_up) 。

最后,您可以创建键对象, 您也可以从中听到事件。 详情请参见 [``Keyboard.Events.UP``](/api/event/input-keyboard-events#up) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 了解更多已发布的键, 任何修改器等 。 |


> 源码：[src/input/keyboard/events/ANY_KEY_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/ANY_KEY_UP_EVENT.js#L7)  
引入版本：3.0.0


---

### COMBO_MATCH {#COMBO_MATCH}

#### COMBO_MATCH {#combo_match}


**说明:**

键Combo火柴事件.

当一个 [Key Combo](/api/class/input-keyboard-keycombo) 匹配时,此事件由键盘插件发送 。

组合创建后从键插件中听到此事件 :

```javascript
this.input.keyboard.createCombo([ 38, 38, 40, 40, 37, 39, 37, 39, 66, 65, 13 ], { resetOnMatch: true });

this.input.keyboard.on('keycombomatch', function (event) {
    console.log('Konami Code entered!');
});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keycombo | [Phaser.Input.Keyboard.KeyCombo](/api/class/input-keyboard-keycombo) | 否 | 匹配的键Combo 对象 。 |
| event | KeyboardEvent | 否 | 组合中最终键的本地 DOM 键盘事件。 您可以检查此选项以了解更多关于任何修改符等的信息 。 |


> 源码：[src/input/keyboard/events/COMBO_MATCH_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/COMBO_MATCH_EVENT.js#L7)  
引入版本：3.0.0


---

### DOWN {#DOWN}

#### DOWN {#down}


**说明:**

钥匙下沉事件.

此事件在按下时由 [Key](/api/class/input-keyboard-key) 对象发送 。

从关键对象实例直接听到此事件 :

```javascript
var spaceBar = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);

spaceBar.on('down', listener)
```

您也可以创建通用的“ 全球” 听器。 详情请参见 [``Keyboard.Events.ANY_KEY_DOWN``](/api/event/input-keyboard-events#any_key_down) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 被按下的关键对象 。 |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 以便了解更多修改器等 。 |


> 源码：[src/input/keyboard/events/DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/DOWN_EVENT.js#L7)  
引入版本：3.0.0


---

### KEY_DOWN {#KEY_DOWN}

#### KEY_DOWN {#key_down}


**说明:**

钥匙下沉事件.

当键盘上的任何键被按下时,此事件由键盘插件发送 。

不像是说 `ANY_KEY_DOWN` 事件,此事件有一个特殊的动态事件名称。例如,为您聆听 `A` 键正在按下,使用场景内的以下内容: `this.input.keyboard.on('keydown-A', listener)`中,您可以替换 `-A` 事件名称中含有任何有效名称的部分 [Key Code string](/api/namespace/input-keyboard-keycodes)。例如,此选项将用于空间栏: `this.input.keyboard.on('keydown-SPACE', listener)`.

您也可以创建通用的“ 全球” 听器。 详情请参见 [``Keyboard.Events.ANY_KEY_DOWN``](/api/event/input-keyboard-events#any_key_down) 。

最后,您可以创建键对象, 您也可以从中听到事件。 详情请参见 [``Keyboard.Events.DOWN``](/api/event/input-keyboard-events#down) 。

_Note_:由于硬件限制被称为鬼神,许多键盘无法处理某些组合的键. Read [此篇关于鬼神的文章]QQlink http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/}的详情.

另外,请注意,一些浏览器扩展可以禁用或覆盖 Phaser键盘处理。例如, Chrome扩展维米被已知可以禁用 Phaser 使用 D 键, 而 EverNote 则禁用反键。 还有其它。 如果您发现您有特定的键不能工作, 请检查您的扩展 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 了解更多按下键、 任何修改符等信息 。 |


> 源码：[src/input/keyboard/events/KEY_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/KEY_DOWN_EVENT.js#L7)  
引入版本：3.0.0


---

### KEY_UP {#KEY_UP}

#### KEY_UP {#key_up}


**说明:**

钥匙事件。

当键盘上的任何键被发布时,此事件由键盘插件发出.

与 `ANY_KEY_UP` 事件不同, 此事件有一个特殊的动态事件名称。 例如, 要为正在释放的 `A` 键聆听, 请使用以下 Scene 中的内容 : `this.input.keyboard.on('keyup-A', listener)` 。 您可以用任何有效的 [Key Code string](/api/namespace/input-keyboard-keycodes) 来替换事件名称中的 `-A` 部分 。 例如, 这将为空间栏监听 : `this.input.keyboard.on('keyup-SPACE', listener)` 。

您也可以创建通用的“ 全球” 听器。 详情请参见 [``Keyboard.Events.ANY_KEY_UP``](/api/event/input-keyboard-events#any_key_up) 。

最后,您可以创建键对象, 您也可以从中听到事件。 详情请参见 [``Keyboard.Events.UP``](/api/event/input-keyboard-events#up) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 了解更多已发布的键, 任何修改器等 。 |


> 源码：[src/input/keyboard/events/KEY_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/KEY_UP_EVENT.js#L7)  
引入版本：3.0.0


---

### UP {#UP}

#### UP {#up}


**说明:**

钥匙事件。

此事件在发布时由 [Key](/api/class/input-keyboard-key) 对象发送 。

从关键对象实例直接听到此事件 :

```javascript
var spaceBar = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);

spaceBar.on('up', listener)
```

您也可以创建通用的“ 全球” 听器。 详情请参见 [``Keyboard.Events.ANY_KEY_UP``](/api/event/input-keyboard-events#any_key_up) 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 已发布的键对象 。 |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 以便了解更多修改器等 。 |


> 源码：[src/input/keyboard/events/UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/UP_EVENT.js#L7)  
引入版本：3.0.0


---

---
