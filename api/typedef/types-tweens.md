# Types.Tweens {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-tweens)

## TweenConfigDefaults {#tweenconfigdefaults}

### \<static> TweenConfigDefaults {#static-tweenconfigdefaults}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| targets | object \| Array.\<object> | 否 |  | 运行 tween 的物体,或一系列物体。 |
| delay | number | 是 | 0 | 开始前要延迟的毫秒数 。 |
| duration | number | 是 | 1000 | 千分之长的曲折时间. |
| ease | string | 是 | "'Power0'" | 用于 tween 的宽松方程。 这是像 `'Linear'`、 `'Quad.easeIn'`、 `'Cubic.easeOut'` 或 `'Bounce.easeInOut'` 这样的字符串键。 完整的支持值列表请参见 `Phaser.Tweens.Builders.GetEaseFunction` 。 |
| easeParams | array | 是 |  | 如果支持,则可选择一系列附加参数,以传递给放松函数。 |
| hold | number | 是 | 0 | 柳英之前的手提琴数 |
| repeat | number | 是 | 0 | 复次  者数. |
| repeatDelay | number | 是 | 0 | 复次前的数毫秒暂停. |
| yoyo | boolean | 是 | false | 如果修补完成, 那么将数值递增反转, 回到起始的修补值 。 反修补需要 `duration` 毫秒才能完成 。 |
| flipX | boolean | 是 | false | 水平翻转 Tween 完成时的目标( 如果设定在 Yoyos 完成前) 。 只为支持 `flipX` 属性的目标工作 。 |
| flipY | boolean | 是 | false | 垂直翻转 Tween 完成时的目标( 如果设定在 Yoyos 完成前) 。 只为支持 `flipY` 属性的目标工作 。 |
| persist | boolean | 是 | false | 保留Tween管理器内的调值,即使播放完成后也保留? |
| interpolation | function | 是 | null | 用于基于数组的 tween 值的插值函数。 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/tween/Defaults.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/tween/Defaults.js#L7)  
引入版本：3.0.0

---

## Event {#event}

### \<static> Event {#static-event}


事件.

**类型**: string

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/Event.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/Event.js#L1)  
引入版本：3.19.0

---

## GetActiveCallback {#getactivecallback}

### \<static> GetActiveCallback {#static-getactivecallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/GetActiveCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/GetActiveCallback.js#L1)  
引入版本：3.19.0

---

## GetEndCallback {#getendcallback}

### \<static> GetEndCallback {#static-getendcallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/GetEndCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/GetEndCallback.js#L1)  
引入版本：3.18.0

---

## GetStartCallback {#getstartcallback}

### \<static> GetStartCallback {#static-getstartcallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/GetStartCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/GetStartCallback.js#L1)  
引入版本：3.18.0

---

## NumberTweenBuilderConfig {#numbertweenbuilderconfig}

### \<static> NumberTweenBuilderConfig {#static-numbertweenbuilderconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| from | number | 是 | 0 | 初标号. |
| to | number | 是 | 1 | 端数. |
| delay | number | 是 | 0 | 计数器启动前要延迟的毫秒数 。 |
| duration | number | 是 | 1000 | 计数器的长度以毫秒计. |
| ease | string \| function | 是 | "'Power0'" | 用来做计数器的放松方程式。 |
| easeParams | array | 是 |  | 可选的宽松参数. |
| hold | number | 是 | 0 | 柳英之前的计数器要用毫秒 |
| repeat | number | 是 | 0 | 复次答问数. |
| repeatDelay | number | 是 | 0 | 计数器重复前的数位数 。 |
| yoyo | boolean | 是 | false | 反弹是否要向前到最终值, 然后倒向开始? 反弹是否还需要 `duration` 毫秒才能完成 。 |
| completeDelay | string \| number | function | object | array | 是 | 0 | 计数器将等待onComplete事件完成后发送的时间,以毫秒计. |
| loop | string \| number | function | object | array | 是 | 0 | 计数器重复的次数(值为1表示计数器将播放两次,因为重复一次. ) |
| loopDelay | string \| number | function | object | array | 是 | 0 | 计数器在开始一个yoyo或返回开始重复之前会暂停时间. |
| paused | boolean | 是 | false | 计数器是以暂停状态( true) 开始还是以播放( 假) 开始 ? |
| callbackScope | any | 是 |  | 调用对象的范畴( 此) 。 默认范围是计数器 。 |
| onComplete | [Phaser.Types.Tweens.TweenOnCompleteCallback](/api/typedef/types-tweens#tweenoncompletecallback) | 是 |  | 柜台完成后调用功能 。 |
| onCompleteParams | array | 是 |  | 附加参数通过到 `onComplete`. |
| onLoop | [Phaser.Types.Tweens.TweenOnLoopCallback](/api/typedef/types-tweens#tweenonloopcallback) | 是 |  | 每次调用反转盘的函数 。 |
| onLoopParams | array | 是 |  | 附加参数通过到 `onLoop`. |
| onRepeat | [Phaser.Types.Tweens.TweenOnRepeatCallback](/api/typedef/types-tweens#tweenonrepeatcallback) | 是 |  | 每次计数器重复调用时, 都会调用一个函数 。 |
| onRepeatParams | array | 是 |  | 附加参数通过到 `onRepeat`. |
| onStart | [Phaser.Types.Tweens.TweenOnStartCallback](/api/typedef/types-tweens#tweenonstartcallback) | 是 |  | 计数器启动时调用功能 。 |
| onStartParams | array | 是 |  | 附加参数通过到 `onStart`. |
| onStop | [Phaser.Types.Tweens.TweenOnStopCallback](/api/typedef/types-tweens#tweenonstopcallback) | 是 |  | 停止计数器时调用功能 。 |
| onStopParams | array | 是 |  | 附加参数通过到 `onStop`. |
| onUpdate | [Phaser.Types.Tweens.TweenOnUpdateCallback](/api/typedef/types-tweens#tweenonupdatecallback) | 是 |  | 每次调用计数器步骤的函数 。 |
| onUpdateParams | array | 是 |  | 附加参数通过到 `onUpdate`. |
| onYoyo | [Phaser.Types.Tweens.TweenOnYoyoCallback](/api/typedef/types-tweens#tweenonyoyocallback) | 是 |  | 每次打来电话都得用 |
| onYoyoParams | array | 是 |  | 附加参数通过到 `onYoyo`. |
| onPause | [Phaser.Types.Tweens.TweenOnPauseCallback](/api/typedef/types-tweens#tweenonpausecallback) | 是 |  | 暂停计数器时调用函数 。 |
| onPauseParams | array | 是 |  | 附加参数通过到 `onPause`. |
| onResume | [Phaser.Types.Tweens.TweenOnResumeCallback](/api/typedef/types-tweens#tweenonresumecallback) | 是 |  | 暂停后恢复计数器时调用功能 。 |
| onResumeParams | array | 是 |  | 附加参数通过到 `onResume`. |
| persist | boolean | 是 |  | 柜台在完成后会自动销毁,还是保留下来供将来重播? |
| interpolation | string \| function | 是 |  | 如果给定的 `value` , 插值函数是数组 。 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/NumberTweenBuilderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/NumberTweenBuilderConfig.js#L1)  
引入版本：3.18.0

---

## StaggerConfig {#staggerconfig}

### \<static> StaggerConfig {#static-staggerconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number | 是 | 0 | 启动交错的值。 可以在仍然使用范围来抵消交错时使用。 Name |
| ease | string \| function | 是 | "'Linear'" | 跨错位值的易用性。 可以是字符串, 如“ 正中” , 也可以是函数 。 |
| from | string \| number | 是 | 0 | 启动交错位置的索引。可以是弦式`first`、`last`或`center`,也可以是代表交错位置的整数。 |
| grid | Array.\<number> | 是 |  | 设置跨网格运行的交错点, 提供一个阵列, 其中0元素是网格宽度, 1元素是高度。 结合“ 从” 属性来控制方向 。 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/StaggerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/StaggerConfig.js#L1)  
引入版本：3.19.0

---

## TweenBuilderConfig {#tweenbuilderconfig}

### \<static> TweenBuilderConfig {#static-tweenbuilderconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| targets | any | 否 |  | 运行 tween 的物体,或一系列物体。 |
| delay | number \| function | 是 | 0 | 开始前要延迟的毫秒数 。 |
| duration | number | 是 | 1000 | 千分之长的曲折时间. |
| ease | string \| function | 是 | "'Power0'" | 放松方程用于  . |
| easeParams | array | 是 |  | 可选的宽松参数. |
| hold | number | 是 | 0 | 柳英之前的手提琴数 |
| repeat | number | 是 | 0 | 每一财产的重复次数。 |
| repeatDelay | number | 是 | 0 | 重复前的数位数 。 |
| yoyo | boolean | 是 | false | 如果修补完成, 那么将数值递增反转, 回到起始的修补值 。 反修补需要 `duration` 毫秒才能完成 。 |
| flipX | boolean | 是 | false | 水平翻转 Tween 完成时的目标( 如果设定在 Yoyos 完成前) 。 只为支持 `flipX` 属性的目标工作 。 |
| flipY | boolean | 是 | false | 垂直翻转 Tween 完成时的目标( 如果设定在 Yoyos 完成前) 。 只为支持 `flipY` 属性的目标工作 。 |
| completeDelay | string \| number | function | object | array | 是 | 0 | 时间,Twen将等待 等待onComplete事件 完成后发送,以毫秒。 |
| loop | string \| number | function | object | array | 是 | 0 | 重复的次数( 1 值表示重复一次的次数) 第一个循环开始于每次完成一次的次数 。 |
| loopDelay | string \| number | function | object | array | 是 | 0 | 时间, 调子会暂停, 然后再开始一个 YOYO 或返回开始重复 。 |
| paused | boolean | 是 | false | 曲折的开始是暂停状态(真)还是播放(假)? |
| props | Object.\<string, (number, string, [Phaser.Types.Tweens.GetEndCallback](/api/typedef/types-tweens#getendcallback), [Phaser.Types.Tweens.TweenPropConfig](/api/typedef/types-tweens#tweenpropconfig))> | 是 |  | 属性至  . |
| callbackScope | any | 是 |  | 所有调用时的范畴(或上下文),默认范围是 tween. |
| onComplete | [Phaser.Types.Tweens.TweenOnCompleteCallback](/api/typedef/types-tweens#tweenoncompletecallback) | 是 |  | 调用时的函数 。 |
| onCompleteParams | array | 是 |  | 附加参数通过到 `onComplete`. |
| onLoop | [Phaser.Types.Tweens.TweenOnLoopCallback](/api/typedef/types-tweens#tweenonloopcallback) | 是 |  | 每次调用调色圈的函数 。 |
| onLoopParams | array | 是 |  | 附加参数通过到 `onLoop`. |
| onRepeat | [Phaser.Types.Tweens.TweenOnRepeatCallback](/api/typedef/types-tweens#tweenonrepeatcallback) | 是 |  | 每次重复一次属性调用函数。每个目标每次调用一次属性 。 |
| onRepeatParams | array | 是 |  | 附加参数通过到 `onRepeat`. |
| onStart | [Phaser.Types.Tweens.TweenOnStartCallback](/api/typedef/types-tweens#tweenonstartcallback) | 是 |  | 当 tween 开始重播时, 任何延迟都过期后调用函数 。 |
| onStartParams | array | 是 |  | 附加参数通过到 `onStart`. |
| onStop | [Phaser.Types.Tweens.TweenOnStopCallback](/api/typedef/types-tweens#tweenonstopcallback) | 是 |  | 当调用调用调用时, 函数值将停止 。 |
| onStopParams | array | 是 |  | 附加参数通过到 `onStop`. |
| onUpdate | [Phaser.Types.Tweens.TweenOnUpdateCallback](/api/typedef/types-tweens#tweenonupdatecallback) | 是 |  | 每次调用调用时, 每个目标每个属性调用一次 。 |
| onUpdateParams | array | 是 |  | 附加参数通过到 `onUpdate`. |
| onYoyo | [Phaser.Types.Tweens.TweenOnYoyoCallback](/api/typedef/types-tweens#tweenonyoyocallback) | 是 |  | 每次调用财产 tween yoyos 的函数。 在每个目标中调用一次 。 |
| onYoyoParams | array | 是 |  | 附加参数通过到 `onYoyo`. |
| onActive | [Phaser.Types.Tweens.TweenOnActiveCallback](/api/typedef/types-tweens#tweenonactivecallback) | 是 |  | 当 tween 开始活跃于 Tween 管理器内时调用函数 。 |
| onActiveParams | array | 是 |  | 附加参数通过到 `onActive`. |
| onPause | [Phaser.Types.Tweens.TweenOnPauseCallback](/api/typedef/types-tweens#tweenonpausecallback) | 是 |  | 当 tween 暂停时调用函数 。 |
| onPauseParams | array | 是 |  | 附加参数通过到 `onPause`. |
| onResume | [Phaser.Types.Tweens.TweenOnResumeCallback](/api/typedef/types-tweens#tweenonresumecallback) | 是 |  | 一个函数,用于在暂停后恢复调用 tween 。 |
| onResumeParams | array | 是 |  | 附加参数通过到 `onResume`. |
| persist | boolean | 是 |  | 修补完成后,Tween会自动销毁,还是保留下来供将来播放? |
| interpolation | string \| function | 是 |  | 如果给定的 `value` , 插值函数是数组 。 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenBuilderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenBuilderConfig.js#L1)  
引入版本：3.18.0

---

## TweenCallbacks {#tweencallbacks}

### \<static> TweenCallbacks {#static-tweencallbacks}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| onActive | [Phaser.Types.Tweens.TweenOnActiveCallback](/api/typedef/types-tweens#tweenonactivecallback) | 是 | 当 tween 开始活跃于 Tween 管理器内时调用函数 。 |
| onStart | [Phaser.Types.Tweens.TweenOnStartCallback](/api/typedef/types-tweens#tweenonstartcallback) | 是 | 当 tween 开始重播时, 任何延迟都过期后调用函数 。 |
| onComplete | [Phaser.Types.Tweens.TweenOnCompleteCallback](/api/typedef/types-tweens#tweenoncompletecallback) | 是 | 调用时的函数 。 |
| onLoop | [Phaser.Types.Tweens.TweenOnLoopCallback](/api/typedef/types-tweens#tweenonloopcallback) | 是 | 每次调用调色圈的函数 。 |
| onPause | [Phaser.Types.Tweens.TweenOnPauseCallback](/api/typedef/types-tweens#tweenonpausecallback) | 是 | 每次调用 tween 时都会调用函数 。 |
| onResume | [Phaser.Types.Tweens.TweenOnResumeCallback](/api/typedef/types-tweens#tweenonresumecallback) | 是 | 每次恢复调用调用时, 都会调用一个函数 。 |
| onRepeat | [Phaser.Types.Tweens.TweenOnRepeatCallback](/api/typedef/types-tweens#tweenonrepeatcallback) | 是 | 每次重复调用 tween 函数。 每个目标调用一次 。 |
| onStop | [Phaser.Types.Tweens.TweenOnStopCallback](/api/typedef/types-tweens#tweenonstopcallback) | 是 | 当调用调用调用时, 函数值将停止 。 |
| onUpdate | [Phaser.Types.Tweens.TweenOnUpdateCallback](/api/typedef/types-tweens#tweenonupdatecallback) | 是 | 每次调用调用时, 每个目标每个属性调用一次 。 |
| onYoyo | [Phaser.Types.Tweens.TweenOnYoyoCallback](/api/typedef/types-tweens#tweenonyoyocallback) | 是 | 每次调用 tween yoyos 的函数。 每个目标调用一次 。 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenCallbacks.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenCallbacks.js#L1)  
引入版本：3.60.0

---

## TweenCallbackTypes {#tweencallbacktypes}

### \<static> TweenCallbackTypes {#static-tweencallbacktypes}

**类型**: 'onActive' | 'onComplete' | 'onLoop' | 'onPause' | 'onRepeat' | 'onResume' | 'onStart' | 'onStop' | 'onUpdate' | 'onYoyo'

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenCallbackTypes.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenCallbackTypes.js#L1)  
引入版本：3.60.0

---

## TweenChainBuilderConfig {#tweenchainbuilderconfig}

### \<static> TweenChainBuilderConfig {#static-tweenchainbuilderconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| targets | any | 否 |  | 运行每个调值的对象,或一系列对象。 |
| delay | number \| function | 是 | 0 | 链条开始前要延迟的毫秒数 。 |
| completeDelay | string \| number | function | object | array | 是 | 0 | 链条在onComplete事件完成后发出前, 时间将等待, 以毫秒计 。 |
| loop | string \| number | function | object | array | 是 | 0 | 链会重复的次数 。 (1 值意味着链会播放两次, 如重复一次 。 ) 第一次循环开始于每次完成一次后 。 |
| loopDelay | string \| number | function | object | array | 是 | 0 | 链条在返回开始前会暂停时间以重复一次 。 |
| paused | boolean | 是 | false | 链条是以暂停状态( true) 开始的还是播放( 假) ? |
| tweens | Array.\<[Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig)> | 是 |  | 以连锁. |
| callbackScope | any | 是 |  | 所有调用回调的范畴(或上下文),默认范围是链条. |
| onComplete | [Phaser.Types.Tweens.TweenOnCompleteCallback](/api/typedef/types-tweens#tweenoncompletecallback) | 是 |  | 链条完成后调用函数 。 |
| onCompleteParams | array | 是 |  | 附加参数通过到 `onComplete`. |
| onLoop | [Phaser.Types.Tweens.TweenOnLoopCallback](/api/typedef/types-tweens#tweenonloopcallback) | 是 |  | 每次连锁循环调用函数 。 |
| onLoopParams | array | 是 |  | 附加参数通过到 `onLoop`. |
| onStart | [Phaser.Types.Tweens.TweenOnStartCallback](/api/typedef/types-tweens#tweenonstartcallback) | 是 |  | 当链条开始回放时, 任何延迟都会过期 。 |
| onStartParams | array | 是 |  | 附加参数通过到 `onStart`. |
| onStop | [Phaser.Types.Tweens.TweenOnStopCallback](/api/typedef/types-tweens#tweenonstopcallback) | 是 |  | 停止链时调用函数 。 |
| onStopParams | array | 是 |  | 附加参数通过到 `onStop`. |
| onActive | [Phaser.Types.Tweens.TweenOnActiveCallback](/api/typedef/types-tweens#tweenonactivecallback) | 是 |  | 当链条在Tween管理器内活动时调用函数 。 |
| onActiveParams | array | 是 |  | 附加参数通过到 `onActive`. |
| onPause | [Phaser.Types.Tweens.TweenOnPauseCallback](/api/typedef/types-tweens#tweenonpausecallback) | 是 |  | 当链条暂停时调用函数 。 |
| onPauseParams | array | 是 |  | 附加参数通过到 `onPause`. |
| onResume | [Phaser.Types.Tweens.TweenOnResumeCallback](/api/typedef/types-tweens#tweenonresumecallback) | 是 |  | 暂停后恢复链时调用函数 。 |
| onResumeParams | array | 是 |  | 附加参数通过到 `onResume`. |
| persist | boolean | 是 |  | 修补完成后,Tween会自动销毁,还是保留下来供将来播放? |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenChainBuilderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenChainBuilderConfig.js#L1)  
引入版本：3.60.0

---

## TweenDataConfig {#tweendataconfig}

### \<static> TweenDataConfig {#static-tweendataconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | any | 否 |  | 目标到弯曲。 |
| index | number | 否 |  | Tween目标阵列内的目标指数. |
| key | string | 否 |  | 目标的财产被扭曲。 |
| getActiveValue | [Phaser.Types.Tweens.GetActiveCallback](/api/typedef/types-tweens#getactivecallback) | 否 |  | 如果不是无效,则在TweenData运行后立即引用_imteme_,并设定在目标属性上. |
| getEndValue | [Phaser.Types.Tweens.GetEndCallback](/api/typedef/types-tweens#getendcallback) | 否 |  | 返回的值设定了在Tween的端点将是什么财产。 |
| getStartValue | [Phaser.Types.Tweens.GetStartCallback](/api/typedef/types-tweens#getstartcallback) | 否 |  | 归还的值确定在Tween裁武条约上的财产将是什么。 |
| ease | function | 否 |  | 此 tween 使用的易操作 。 |
| duration | number | 是 | 0 | 以毫秒计的扭矩持续时间,不包括yoyo或重复的时间。 |
| totalDuration | number | 是 | 0 | 计算出TweenData的总持续时间(根据持续时间、重复、延迟和yoyo) |
| delay | number | 是 | 0 | 时间在毫秒后,Tween开始。 |
| yoyo | boolean | 是 | false | 使 tween 值在持有到期后返回到它的起始值 。 |
| hold | number | 是 | 0 | 时间(毫秒) 时长将暂停运行 Yyo 或开始重复。 |
| repeat | number | 是 | 0 | 重复 tween 的次数。 tween 将总是运行一次, 不管怎样, 因此“ 1” 的重复值将播放两次 tween 。 |
| repeatDelay | number | 是 | 0 | 重复开始前的时长为毫秒。 |
| flipX | boolean | 是 | false | 当TweenData yoyos或重复时自动调用 toggleFlipX |
| flipY | boolean | 是 | false | 当TweenData yoyos或重复时自动调用 toggleFlipY |
| progress | number | 是 | 0 | 0到1之间显示此TweenData完成. |
| elapsed | number | 是 | 0 | 三角洲计数器 |
| repeatCounter | number | 是 | 0 | 有多少次重复还剩跑步? |
| start | number | 是 | 0 | 易地开始时的属性价值. |
| current | number | 是 | 0 | 现财产值. |
| previous | number | 是 | 0 | 上个财产价值. |
| end | number | 是 | 0 | 易经末的财产价值. |
| gen | [Phaser.Types.Tweens.TweenDataGenConfig](/api/typedef/types-tweens#tweendatagenconfig) | 是 |  | 装入 Vale 生成函数 。 |
| state | [Phaser.Tweens.StateType](/api/typedef/tweens#statetype) | 是 | 0 | 已删除 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenDataConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenDataConfig.js#L1)  
引入版本：3.0.0

---

## TweenDataGenConfig {#tweendatagenconfig}

### \<static> TweenDataGenConfig {#static-tweendatagenconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delay | function | 否 | 时间在毫秒后,Tween开始。 |
| duration | function | 否 | 以毫秒计的扭矩持续时间,不包括yoyo或重复的时间。 |
| hold | function | 否 | 时间(毫秒) 时长将暂停运行 Yyo 或开始重复。 |
| repeat | function | 否 | 重复 tween 的次数。 tween 将总是运行一次, 不管怎样, 因此“ 1” 的重复值将播放两次 tween 。 |
| repeatDelay | function | 否 | 重复开始前的时长为毫秒。 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenDataGenConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenDataGenConfig.js#L1)  
引入版本：3.0.0

---

## TweenFrameDataConfig {#tweenframedataconfig}

### \<static> TweenFrameDataConfig {#static-tweenframedataconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | any | 否 |  | 目标到弯曲。 |
| index | number | 否 |  | Tween目标阵列内的目标指数. |
| key | string | 否 |  | 目标的财产被扭曲。 |
| duration | number | 是 | 0 | 以毫秒计的扭矩持续时间,不包括yoyo或重复的时间。 |
| totalDuration | number | 是 | 0 | 计算出TweenData的总持续时间(根据持续时间、重复、延迟和yoyo) |
| delay | number | 是 | 0 | 时间在毫秒后,Tween开始。 |
| hold | number | 是 | 0 | 时间(毫秒) 时长将暂停运行 Yyo 或开始重复。 |
| repeat | number | 是 | 0 | 重复 tween 的次数。 tween 将总是运行一次, 不管怎样, 因此“ 1” 的重复值将播放两次 tween 。 |
| repeatDelay | number | 是 | 0 | 重复开始前的时长为毫秒。 |
| flipX | boolean | 是 | false | 当TweenData yoyos或重复时自动调用 toggleFlipX |
| flipY | boolean | 是 | false | 当TweenData yoyos或重复时自动调用 toggleFlipY |
| progress | number | 是 | 0 | 0到1之间显示此TweenData完成. |
| elapsed | number | 是 | 0 | 三角洲计数器 |
| repeatCounter | number | 是 | 0 | 有多少次重复还剩跑步? |
| gen | [Phaser.Types.Tweens.TweenDataGenConfig](/api/typedef/types-tweens#tweendatagenconfig) | 是 |  | 装入 Vale 生成函数 。 |
| state | [Phaser.Tweens.StateType](/api/typedef/tweens#statetype) | 是 | 0 | 已删除 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenFrameDataConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenFrameDataConfig.js#L1)  
引入版本：3.60.0

---

## TweenOnActiveCallback {#tweenonactivecallback}

### \<static> TweenOnActiveCallback {#static-tweenonactivecallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnActiveCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnActiveCallback.js#L1)  
引入版本：3.19.0

---

## TweenOnCompleteCallback {#tweenoncompletecallback}

### \<static> TweenOnCompleteCallback {#static-tweenoncompletecallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnCompleteCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnCompleteCallback.js#L1)  
引入版本：3.18.0

---

## TweenOnLoopCallback {#tweenonloopcallback}

### \<static> TweenOnLoopCallback {#static-tweenonloopcallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnLoopCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnLoopCallback.js#L1)  
引入版本：3.18.0

---

## TweenOnPauseCallback {#tweenonpausecallback}

### \<static> TweenOnPauseCallback {#static-tweenonpausecallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnPauseCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnPauseCallback.js#L1)  
引入版本：3.60.0

---

## TweenOnRepeatCallback {#tweenonrepeatcallback}

### \<static> TweenOnRepeatCallback {#static-tweenonrepeatcallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnRepeatCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnRepeatCallback.js#L1)  
引入版本：3.18.0

---

## TweenOnResumeCallback {#tweenonresumecallback}

### \<static> TweenOnResumeCallback {#static-tweenonresumecallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnResumeCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnResumeCallback.js#L1)  
引入版本：3.60.0

---

## TweenOnStartCallback {#tweenonstartcallback}

### \<static> TweenOnStartCallback {#static-tweenonstartcallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnStartCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnStartCallback.js#L1)  
引入版本：3.18.0

---

## TweenOnStopCallback {#tweenonstopcallback}

### \<static> TweenOnStopCallback {#static-tweenonstopcallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnStopCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnStopCallback.js#L1)  
引入版本：3.24.0

---

## TweenOnUpdateCallback {#tweenonupdatecallback}

### \<static> TweenOnUpdateCallback {#static-tweenonupdatecallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnUpdateCallback.js#L1)  
引入版本：3.18.0

---

## TweenOnYoyoCallback {#tweenonyoyocallback}

### \<static> TweenOnYoyoCallback {#static-tweenonyoyocallback}

**类型**: function

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenOnYoyoCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenOnYoyoCallback.js#L1)  
引入版本：3.18.0

---

## TweenPropConfig {#tweenpropconfig}

### \<static> TweenPropConfig {#static-tweenpropconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number \| Array.\<number> | string | [Phaser.Types.Tweens.GetEndCallback](/api/typedef/types-tweens#getendcallback) | [Phaser.Types.Tweens.TweenPropConfig](/api/typedef/types-tweens#tweenpropconfig) | 是 | 特温的末端会有什么财产 |
| getActive | [Phaser.Types.Tweens.GetActiveCallback](/api/typedef/types-tweens#getactivecallback) | 是 | 当这小节开始活动时 财产会立即设定什么 |
| getEnd | [Phaser.Types.Tweens.GetEndCallback](/api/typedef/types-tweens#getendcallback) | 是 | 特温的末端会有什么财产 |
| getStart | [Phaser.Types.Tweens.GetStartCallback](/api/typedef/types-tweens#getstartcallback) | 是 | 特温号的裁武条约会有什么财产? |
| ease | string \| function | 是 | 此 tween 使用的易操作 。 |
| delay | number | 是 | 时间在毫秒后,Tween开始。 |
| duration | number | 是 | 以毫秒计的扭矩持续时间 。 |
| yoyo | boolean | 是 | 确定在持有到期后, twin是否应该返回其起始值 。 |
| hold | number | 是 | 时间( 毫秒) , 调值在重现或返回其起始值之前会暂停, 如果 Yyo 设定为真实 。 |
| repeat | number | 是 | 重复 tween 的次数。 tween 将总是运行一次, 不管怎样, 因此“ 1” 的重复值将播放两次 tween 。 |
| repeatDelay | number | 是 | 重复开始前的时长为毫秒。 |
| flipX | boolean | 是 | 黄  还是重复时,应该叫toggleFlipX? |
| flipY | boolean | 是 | 黄  还是重复时,应该叫toggleFlipY? |
| interpolation | string \| function | 是 | 如果给定的 `value` , 插值函数是数组 。 |

**类型**: object

**Member of**: Phaser.Types.Tweens
> 源码：[src/tweens/typedefs/TweenPropConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/typedefs/TweenPropConfig.js#L1)  
引入版本：3.18.0

---

---
