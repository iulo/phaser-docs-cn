# Input.Keyboard.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/input-keyboard-events)

## ANY_KEY_DOWN {#any_key_down}


**说明:** 全球钥匙下架事件.

当键盘上的任何键被按下时,此事件由键盘插件发送 。

使用:`this.input.keyboard.on('keydown', listener)`,从场内听这个事件.

您也可以按下特定键。 详情请参见 [Keyboard. Events.KEY_DOWN] QQlinkcode Phaser.Input.Keyboard.Events# event: KEY_DOWN] 。

最后,您可以创建关键对象, 您也可以从中听到事件。 详情请参见 [Keyboard. Events. DOWN] @ linkcode Phaser.Input.Keyboard.Events# event: DOWN] 。

_Note_:由于硬件的限制,许多键盘无法处理某些组合的密钥,被称为"鬼魂".
读[此篇关于鬼神的文章] 详细内容请链接http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/}.

另外,请注意一些浏览器扩展可以禁用或超过Phaser键盘处理.
例如,Chrome扩展的vimium已知可以禁用Phaser使用D密钥,而EverNote则禁用反键.
还有其它的,所以如果你发现你的扩展键不起作用,请检查您的扩展键。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 了解更多按下键、 任何修改符等信息 。 |

**Member of:** [Phaser.Input.Keyboard.Events](/api/namespace/input-keyboard-events)
> 源码：[src/input/keyboard/events/ANY_KEY_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/ANY_KEY_DOWN_EVENT.js#L7)  
引入版本：3.0.0

## ANY_KEY_UP {#any_key_up}


**说明:** 全球键起事件.

当键盘上的任何键被发布时,此事件由键盘插件发出.

使用:`this.input.keyboard.on('keyup', listener)`,从场内听这个事件.

您也可以监听正在发布的特定密钥。 详情请参见 [Keyboard. Events.KEY_UP] QQlinkcode Phaser.Input.Keyboard.Events#event: KEY_UP] 。

最后,您可以创建关键对象, 您也可以从中听到事件。 详情请参见 [Keyboard. Events. UP] QQlinkcode Phaser.Input.Keyboard.Events# event: UP] 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 了解更多已发布的键, 任何修改器等 。 |

**Member of:** [Phaser.Input.Keyboard.Events](/api/namespace/input-keyboard-events)
> 源码：[src/input/keyboard/events/ANY_KEY_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/ANY_KEY_UP_EVENT.js#L7)  
引入版本：3.0.0

## COMBO_MATCH {#combo_match}


**说明:** 密钥Combo火柴事件.

当一个 [Key Combo]\\\\ n链接时, 此事件由键盘插件发送 。 Phaser.Input.Keyboard.KeyCombo\ n匹配。

组合创建后从密钥插件中听到此事件 :

```javascript
this.input.keyboard.createCombo([ 38, 38, 40, 40, 37, 39, 37, 39, 66, 65, 13 ], { resetOnMatch: true });

this.input.keyboard.on('keycombomatch', function (event) {
    console.log('Konami Code entered!');
});
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| keycombo | [Phaser.Input.Keyboard.KeyCombo](/api/class/input-keyboard-keycombo) | 否 | 匹配的密钥Combo 对象 。 |
| event | KeyboardEvent | 否 | 组合中最终键的本地 DOM 键盘事件。 您可以检查此选项以了解更多关于任何修改符等的信息 。 |

**Member of:** [Phaser.Input.Keyboard.Events](/api/namespace/input-keyboard-events)
> 源码：[src/input/keyboard/events/COMBO_MATCH_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/COMBO_MATCH_EVENT.js#L7)  
引入版本：3.0.0

## DOWN {#down}


**说明:** 钥匙下沉事件.

此事件由按下时的 [Key] QQLink Phaser.Input.Keyboard.Key] 对象发送 。

从关键对象实例直接听到此事件 :

```javascript
var spaceBar = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);

spaceBar.on('down', listener)
```

您也可以创建通用的“ 全球” 听器。 详情请参见 [Keyboard. Events.ANY_KEY_DOWN] QQlinkcode Phaser.Input.Keyboard.Events#event: ANY_KEY_DOWN] 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 被按下的关键对象 。 |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 以便了解更多修改器等 。 |

**Member of:** [Phaser.Input.Keyboard.Events](/api/namespace/input-keyboard-events)
> 源码：[src/input/keyboard/events/DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/DOWN_EVENT.js#L7)  
引入版本：3.0.0

## KEY_DOWN {#key_down}


**说明:** 钥匙下沉事件.

当键盘上的任何键被按下时,此事件由键盘插件发送 。

不同于 `ANY_KEY_DOWN` 事件, 此事件有一个特殊的动态事件名称。 例如, 要为正在按下的 `A` 密钥监听
使用以下在场景中显示的: `this.input.keyboard.on('keydown-A', listener)`。 您可以替换事件中的 `-A` 部分 。
名称, 带有任何有效的 [关键代码字符串] @%link Phaser.Input.Keyboard.KeyCodes} 。 例如, 它将为空间栏倾听 :
`this.input.keyboard.on('keydown-SPACE', listener)`.

您也可以创建通用的“ 全球” 听器。 详情请参见 [Keyboard. Events.ANY_KEY_DOWN] QQlinkcode Phaser.Input.Keyboard.Events#event: ANY_KEY_DOWN] 。

最后,您可以创建关键对象, 您也可以从中听到事件。 详情请参见 [Keyboard. Events. DOWN] @ linkcode Phaser.Input.Keyboard.Events# event: DOWN] 。

_Note_:由于硬件的限制,许多键盘无法处理某些组合的密钥,被称为"鬼魂".
读[此篇关于鬼神的文章] 详细内容请链接http://www.html5gamedevs.com/topic/4876-impossible-to-use-more-than-2-keyboard-input-buttons-at-the-same-time/}.

另外,请注意一些浏览器扩展可以禁用或超过Phaser键盘处理.
例如,Chrome扩展的vimium已知可以禁用Phaser使用D密钥,而EverNote则禁用反键.
还有其它的,所以如果你发现你的扩展键不起作用,请检查您的扩展键。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 了解更多按下键、 任何修改符等信息 。 |

**Member of:** [Phaser.Input.Keyboard.Events](/api/namespace/input-keyboard-events)
> 源码：[src/input/keyboard/events/KEY_DOWN_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/KEY_DOWN_EVENT.js#L7)  
引入版本：3.0.0

## KEY_UP {#key_up}


**说明:** 钥匙事件。

当键盘上的任何键被发布时,此事件由键盘插件发出.

与 `ANY_KEY_UP` 事件不同, 此事件有一个特殊的动态事件名称。 例如, 用于为 `A` 键发布
使用以下在场景中显示的: `this.input.keyboard.on('keyup-A', listener)`。 您可以替换事件中的 `-A` 部分 。
名称, 带有任何有效的 [关键代码字符串] @%link Phaser.Input.Keyboard.KeyCodes} 。 例如, 它将为空间栏倾听 :
`this.input.keyboard.on('keyup-SPACE', listener)`.

您也可以创建通用的“ 全球” 收听器。 详情请参见 [Keyboard. Events. ANY_KEY_UP] QQlinkcode Phaser.Input.Keyboard.Events# event: ANY_KEY_UP] 。

最后,您可以创建关键对象, 您也可以从中听到事件。 详情请参见 [Keyboard. Events. UP] QQlinkcode Phaser.Input.Keyboard.Events# event: UP] 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 了解更多已发布的键, 任何修改器等 。 |

**Member of:** [Phaser.Input.Keyboard.Events](/api/namespace/input-keyboard-events)
> 源码：[src/input/keyboard/events/KEY_UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/KEY_UP_EVENT.js#L7)  
引入版本：3.0.0

## UP {#up}


**说明:** 钥匙事件。

此事件在发布时由 [Key] QQLink Phaser.Input.Keyboard.Key] 对象发送 。

从关键对象实例直接听到此事件 :

```javascript
var spaceBar = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.SPACE);

spaceBar.on('up', listener)
```

您也可以创建通用的“ 全球” 收听器。 详情请参见 [Keyboard. Events. ANY_KEY_UP] QQlinkcode Phaser.Input.Keyboard.Events# event: ANY_KEY_UP] 。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 已发布的密钥对象 。 |
| event | KeyboardEvent | 否 | 本地 DOM 键盘事件。 您可以检查此事件, 以便了解更多修改器等 。 |

**Member of:** [Phaser.Input.Keyboard.Events](/api/namespace/input-keyboard-events)
> 源码：[src/input/keyboard/events/UP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/events/UP_EVENT.js#L7)  
引入版本：3.0.0

---
