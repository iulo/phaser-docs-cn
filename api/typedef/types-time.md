# Types.Time {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-time)

## TimelineEvent {#timelineevent}

### \<static> TimelineEvent {#static-timelineevent}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| complete | boolean | 否 |  | 这件事情已经结束了吗? |
| once | boolean | 否 |  | 这是一次吗? |
| time | number | 否 |  | 时间(以毫秒计), |
| repeat | number | 是 | 0 | 事件重复的次数。 |
| if | function | 是 | null | 用户本地调用, 如果设置了, 将会调用。 如果返回 `true`, 那么此事件将运行全部的动作, 否则会跳过 。 |
| run | function | 是 | null | 用户- 本地调用, 当事件发生时将调用 。 |
| loop | function | 是 | null | 用户区域调用, 当事件循环时, 将会调用 。 |
| tween | [Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig) \| [Phaser.Types.Tweens.TweenChainBuilderConfig](/api/typedef/types-tweens#tweenchainbuilderconfig) | [Phaser.Tweens.Tween](/api/class/tweens-tween) | [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) | 是 | null | 用于创建事件一旦设定时的 Tween 配置对象 。 |
| set | object | 是 | null | 事件一旦设定时, 包含属性的天体将设定在 `target` 上 。 |
| sound | string \| object | 是 | null | 声音配置对象, 如果设定事件起火时用于创建声音 。 |
| target | * | 是 |  | 用于引用运行的 `callback`的瞄准镜(`this`对象). |
| event | string | 是 |  | 事件发生时的可选事件名称 。 |
| tweenInstance | [Phaser.Tweens.Tween](/api/class/tweens-tween) \| [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) | 是 | null | 如果事件使用Tween来管理它的行动,则该财产将包含一个引用. |

**类型**: object

**Member of**: Phaser.Types.Time
> 源码：[src/time/typedefs/TimelineEvent.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/typedefs/TimelineEvent.js#L1)  
引入版本：3.60.0

---

## TimelineEventConfig {#timelineeventconfig}

### \<static> TimelineEventConfig {#static-timelineeventconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| at | number | 是 | 0 | 事件发射的时间(以毫秒计),时间线从 0 开始。 |
| in | number | 是 |  | 如果时间线运行, 则事件将根据其当前已过期值开火的时间( ms) 。 如果设定, 它将覆盖 `at` 属性 。 |
| from | number | 是 |  | 在时间线上前一事件后发射“ 从” 毫秒。 如果设定的话, 将覆盖 `at` 和 `in` 属性 。 |
| run | function | 是 |  | 事件发生时, 函数将被称为 。 |
| loop | function | 是 |  | 当事件循环时, 函数会调用, 如果未使用 `repeat` 方法, 或第一次重复时, 则不调用 。 |
| event | string | 是 |  | 事件发生时, 以字符串为基础的事件名称可选择。 事件从时间线实例中释放 。 |
| target | * | 是 |  | 如果设定, 引用运行的 `callback` 范围( `this` 对象) 。 |
| once | boolean | 是 | false | 如果设定, 活动会在发射时从时间线上移除 。 |
| stop | boolean | 是 | false | 如果设定了, 时间线将会在此事件发生时停止并输入一个完整的状态, 即使事件发生后还有其他事件 。 |
| tween | [Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig) \| [Phaser.Types.Tweens.TweenChainBuilderConfig](/api/typedef/types-tweens#tweenchainbuilderconfig) | [Phaser.Tweens.Tween](/api/class/tweens-tween) | [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) | 是 |  | Tween 或 TweenChain 配置对象或实例。 如果设定, 事件会在它开火时创建 Tween 。 |
| set | object | 是 |  | 当事件发生时, 要设置在 `target` 上的属性密钥值对象。 如果没有给出 `target`, 则忽略了 。 |
| sound | string \| object | 是 |  | 声音管理器的要播放的密钥, 或者事件发生时要播放声音的配置对象。 如果配置对象必须提供两个属性 : `key` 财务报告和已审计财务报表 `config`。该词 `key` 声音的键,和 `config` 配置是一个 Phaser.Types.Sound.SoundConfig 对象。 |

**类型**: object

**Member of**: Phaser.Types.Time
> 源码：[src/time/typedefs/TimelineEventConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/typedefs/TimelineEventConfig.js#L1)  
引入版本：3.60.0

---

## TimerEventConfig {#timereventconfig}

### \<static> TimerEventConfig {#static-timereventconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| delay | number | 是 | 0 | 计时器事件发射的延迟, 以毫秒计 。 |
| repeat | number | 是 | 0 | 计时器事件在完成前将重复的总数 。 |
| loop | boolean | 是 | false | 如果计时器事件 无限期重复的话, `true`。 |
| callback | function | 是 |  | 计时器事件时会召回的呼唤 |
| callbackScope | * | 是 |  | 引用 `callback` 的范畴( `this` 对象) 。 默认是定时器事件 。 |
| args | Array.\<*> | 是 |  | 补充论点将转至`callback`。 |
| timeScale | number | 是 | 1 | 时间的长度。 |
| startAt | number | 是 | 0 | 初始时间用毫秒表示。 如果您想要用重复来延长时间, 但第一个循环需要快速开火, 则有用 。 |
| paused | boolean | 是 | false | 如果计时器事件暂停, 请使用 `true` 。 |

**类型**: object

**Member of**: Phaser.Types.Time
> 源码：[src/time/typedefs/TimerEventConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/typedefs/TimerEventConfig.js#L1)  
引入版本：3.0.0

---

---
