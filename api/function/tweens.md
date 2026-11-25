# Phaser.Tweens.Builders {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/tweens)

### GetBoolean {#GetBoolean}

#### \<static> GetBoolean(source, key, defaultValue) {#static-getbooleansource-key-defaultvalue}


**说明:**

从源对象中获取给定键的布尔值,如果键缺失或未提供源对象,则返回默认值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 取回该值的对象 。 |
| key | string | 否 | `source`对象中要寻找的键. |
| defaultValue | boolean | 否 | 如果 `key` 不存在, 或者没有提供 `source` 对象, 则默认值返回 。 |


**返回值:** boolean - 与键相关的布尔值, 或如果键不存在或未提供源对象, 则与 `defaultValue` 相关 。


> 源码：[src/tweens/builders/GetBoolean.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/GetBoolean.js#L7)  
引入版本：3.0.0


### GetEaseFunction {#GetEaseFunction}

#### \<static> GetEaseFunction(ease, [easeParams]) {#static-geteasefunctionease-easeparams}


**说明:**

返回给定的 `ease` 值的宽松函数,用于 Tween 。

电话 `ease` 参数可以是 EaseMap 中准确的键(例如) 。 `'Power2'`, `'Quad.easeIn'`),一个短手点注音字符串(例如. `'quad.in'`, `'cubic.inout'`),或自定义的放松功能。如果字符串不能解决,则函数会回到 `Power0` (线性放松).

当提供`easeParams`时,返回的功能是将这些附加参数转发到每个调用上解析的易功能的包线,使像Stepped或Back Leasing这样的参数化的宽松成为可能.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ease | string \| function | 否 | 解析的易。 接受 EaseMap 键, 点注释的简写( 如 `'quad.in'`) , 或者自定义的宽松功能 。 |
| easeParams | Array.\<number> | 是 | 可选的附加参数数组,以传递给每个调用时的易操作功能. |


**返回值:** function - 解析的易功能,或应用解析的易与提供的参数的折叠函数.


> 源码：[src/tweens/builders/GetEaseFunction.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/GetEaseFunction.js#L10)  
引入版本：3.0.0


### GetInterpolationFunction {#GetInterpolationFunction}

#### \<static> GetInterpolationFunction(interpolation) {#static-getinterpolationfunctioninterpolation}


**说明:**

返回用于多值属性的 Tween 的插值函数。

电话 `interpolation` 参数可以是字符串键、自定义函数,或 `null`。有效的字符串键是 `'linear'`, `'bezier'`, `'catmull'`,和 `'catmullrom'`。如果提供了字符串但未予识别,则函数会回到线性插值。如果 `null` 已经过去了, `null` 返回,表示不应用插值。如果通过自定义函数,则直接返回并用作插值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| interpolation | string \| function | null | 否 | 内插函数可以解析。 可以是字符串键( Q)`'linear'`, `'bezier'`, `'catmull'`, `'catmullrom'`),自定义插值函数,或 `null`. |


**返回值:** function - 解析的插值函数,或者 `null` 如果 `null` 被传入的话.


> 源码：[src/tweens/builders/GetInterpolationFunction.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/GetInterpolationFunction.js#L18)  
引入版本：3.60.0


### GetNewValue {#GetNewValue}

#### \<static> GetNewValue(source, key, defaultValue) {#static-getnewvaluesource-key-defaultvalue}


**说明:**

Tween 构建器用于创建值解调器调用一个 tween 属性的内部函数。 它检查给定的 `source` 指定对象 `key` ,然后返回一个在 tween 插值中适合使用的包件函数。如果属性存在于源上,而本身是函数,则包件可以接收完整的 tween 上下文(目标, targetKey,数值, targetIndex, totalTargets, tween),在每次调用中。如果属性是一个静态值,则总是返回该值的函数会被创建。如果源没有属性,则 `defaultValue` 被使用——或者直接使用(如果它已经是一个函数),或者被包裹在返回它的函数中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | any | 否 | 源对象从中获取值 。 |
| key | string | 否 | 取自源头的属性. |
| defaultValue | any | 否 | 如果源代码没有设置属性, 则使用默认值。 可能本身是一个函数 。 |


**返回值:** function - 函数,在调用时,从源返回解析的属性值,或者如果属性不存在,则返回默认值.


> 源码：[src/tweens/builders/GetNewValue.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/GetNewValue.js#L7)  
引入版本：3.0.0


### GetProps {#GetProps}

#### \<static> GetProps(config) {#static-getpropsconfig}


**说明:**

Tween 构建器用于提取 Tween 将动画属性列表的内部函数。 它需要 Tween 配置对象, 并遵循两个路径之一 : 如果配置包含一个 `props` 对象,它会按住其键,并跳过任何以下划线开头的键;否则,它会直接跳过顶级配置键,跳过任何以下线开头的键和保留属性列表中出现的键(例如). `targets`, `delay`, `duration`).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig) | 否 | Tween 的配置对象,用于获取属性 。 |


**返回值:** Array.\<string> - 代表每个属性的 `{ key, value }` 对象阵列, 将动画化 。


> 源码：[src/tweens/builders/GetProps.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/GetProps.js#L9)  
引入版本：3.0.0


### GetTargets {#GetTargets}

#### \<static> GetTargets(config) {#static-gettargetsconfig}


**说明:**

从 Tween 配置对象中提取一系列目标。

目标将在 `targets` 属性中查找。 如果是一个函数, 则会使用它的返回值来获取 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | object | 否 | Tween配置对象包含 `targets` 属性以提取. |


**返回值:** array - 一系列目标(可能只包含一个元素),或者如果没有指定目标,则使用`null`.


> 源码：[src/tweens/builders/GetTargets.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/GetTargets.js#L9)  
引入版本：3.0.0


### GetValueOp {#GetValueOp}

#### \<static> GetValueOp(key, propertyValue) {#static-getvalueopkey-propertyvalue}


**说明:**

返回值 `getActive`, `getStart` 财务报告和已审计财务报表 `getEnd` 基于目标属性和端值的TweenData函数。

`getActive`如果不是无效,则在TweenData运行后立即引用_立即_,并设置在目标属性上. `getEnd`一旦启动延迟过期,返回该值的值,则会被引用. `getStart`在  到达尾端,需要重复或yoyo时,它会返回要返回的值.

如果端值是一个数字, 它将被作为绝对值对待, 属性会被调整到它。 可以提供字符串来指定由操作构成的相对端值( )`+=` 以加入当前值, `-=` 以减去当前值, `*=` 以乘以当前值,或 `/=` 以除以当前值),然后是其操作。

可以提供一种功能,以允许对终端值进行更大的控制;它会接收被子化的目标对象,被子化的属性名称,以及作为参数的当前属性值,必须返回一个值.

如果需要控制起始值和结尾值,则可以提供`getStart`和`getEnd`调回符的对象,这些对象将接收相同的参数。如果提供`value`属性的对象,则根据本文所述的相同规则,该属性将作为有效值使用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要修改的属性名称 。 |
| propertyValue | * | 否 | 上文所述的属性的期末价值。 |


**返回值:** function - 包含 `getActive`, `getStart`, 和 `getEnd` 函数的天体, 函数会根据所提供的值返回属性的活跃值, 起始值和结尾值 。


> 源码：[src/tweens/builders/GetValueOp.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/GetValueOp.js#L42)  
引入版本：3.0.0


### NumberTweenBuilder {#NumberTweenBuilder}

#### \<static> NumberTweenBuilder(parent, config, defaults) {#static-numbertweenbuilderparent-config-defaults}


**说明:**

创建新的数字补间,也称为计数补间.

与标准 tween 不同, Number Tween 并不针对 Game Object 的属性。 相反, 它在 tween 过程中将 `from` 和 `to` 之间的一个纯数值插入到一个纯数值中。 当前插值可以通过 `tween.getValue()` 随时读取。 这使得 Number Tweens 的理想值可以用于驱动自定义动画、 UI 计数器、 遮阳制服, 或任何需要随时间而顺利变化而无需直接绑定到 Game Objecter 属性的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) | 否 | 新特温的主人. |
| config | [Phaser.Types.Tweens.NumberTweenBuilderConfig](/api/typedef/types-tweens#numbertweenbuilderconfig) | 否 | 新图文的配置 。 |
| defaults | [Phaser.Types.Tweens.TweenConfigDefaults](/api/typedef/types-tweens#tweenconfigdefaults) | 否 | 调频配置默认值. |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 新  .


> 源码：[src/tweens/builders/NumberTweenBuilder.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/NumberTweenBuilder.js#L19)  
引入版本：3.0.0


### StaggerBuilder {#StaggerBuilder}

#### \<static> StaggerBuilder(value, [options]) {#static-staggerbuildervalue-options}


**说明:**

创建 Staggger 函数,供 Tween 属性使用。

交错函数将允许您在 tween 的所有目标上错开属性值的更改 。

只有在  有多个目标时才值得使用.

以下将错开百米的延迟,跨过所有  的目标,使其在指定期限内缩放到0.2: 1.

```javascript
this.tweens.add({
    targets: [ ... ],
    scale: 0.2,
    ease: 'linear',
    duration: 1000,
    delay: this.tweens.stagger(100)
});
```

以下将使用10×6格栅在  的所有目标上错开500ms的延迟,从中心向外突起,使用立方易行.

```javascript
this.tweens.add({
    targets: [ ... ],
    scale: 0.2,
    ease: 'linear',
    duration: 1000,
    delay: this.tweens.stagger(500, { grid: [ 10, 6 ], from: 'center', ease: 'cubic.out' })
});
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number \| Array.\<number> | 否 | 由或包含两个元素的阵列交错的金额, 代表分钟和最大值, 以在两者之间交错 。 |
| options | [Phaser.Types.Tweens.StaggerConfig](/api/typedef/types-tweens#staggerconfig) | 是 | 跳跃配置对象 。 |


**返回值:** function - 一个交错函数,当Tween系统为每个目标引用时,会根据其指数,目标总数,以及提供的交错配置计算并返回该目标交错属性值.


> 源码：[src/tweens/builders/StaggerBuilder.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/StaggerBuilder.js#L11)  
引入版本：3.19.0


### TweenBuilder {#TweenBuilder}

#### \<static> TweenBuilder(parent, config, defaults) {#static-tweenbuilderparent-config-defaults}


**说明:**

分析一个 Tween 配置对象,并构建一个完全初始化的 `Tween` 实例, 准备添加到 Tween 管理器中 。

此构建器从配置中解决对象和属性列表, 创建 `TweenData` 输入每个目标/属性组合,并应用默认值来缓解、持续时间、延迟、持有、重复、yoyo、翻转和插值。 `scale` 支持快捷键: 如果目标没有本地 `scale` 属性, 构建者自动将其扩展为单独的 `scaleX` 财务报告和已审计财务报表 `scaleY` TweenData条目. Texture tweenning(随时间推移改变目标纹理和帧)也被作为单独的代码路径处理.

在构建 TweenData 条目后, 构建者配置顶级的 Tween 属性, 如 `loop`, `loopDelay`, `completeDelay`, `paused`, `persist`,以及配置中定义的任何调用(例如) `onStart`, `onUpdate`, `onComplete`).

如果`config`已经是一个`Tween`的例子,则更新其`parent`,并按原样返回,不再进行进一步处理。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) | 否 | 新特温的主人. |
| config | [Phaser.Types.Tweens.TweenBuilderConfig](/api/typedef/types-tweens#tweenbuilderconfig) \| object | 否 | 新图文的配置 。 |
| defaults | [Phaser.Types.Tweens.TweenConfigDefaults](/api/typedef/types-tweens#tweenconfigdefaults) | 否 | 调频配置默认值. |


**返回值:** [Phaser.Tweens.Tween](/api/class/tweens-tween) - 新  .


> 源码：[src/tweens/builders/TweenBuilder.js#L22](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/TweenBuilder.js#L22)  
引入版本：3.0.0


### TweenChainBuilder {#TweenChainBuilder}

#### \<static> TweenChainBuilder(parent, config) {#static-tweenchainbuilderparent-config}


**说明:**

从给定的配置对象创建一个新的 TweenChain 实例。 TweenChain 是一组 Tweens 的顺序, 顺序是按顺序, 而不是一次全部播放。 这使得它有利于创建多步动画, 每一步必须在下一个步骤开始前完成 。

此构建器在使用 `scene.tweens.chain()` 时被 TweenManager 内部调用。 它处理配置对象设置链的起始延迟、 循环计数、 循环延迟、 完成延迟、 暂停状态、 生命周期回调, 以及构成链的单个 Tweens。 如果配置中定义了任何顶级的 `targets`, 则它们会作为默认值传递给每个未指定自身目标的 Tween 。

如果 `config` 参数已经是一个 TweenChain 实例, 则其父被更新, 并返回为正则而不重建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | [Phaser.Tweens.TweenManager](/api/class/tweens-tweenmanager) | 否 | 新特温的主人. |
| config | [Phaser.Types.Tweens.TweenChainBuilderConfig](/api/typedef/types-tweens#tweenchainbuilderconfig) \| object | 否 | 新图文的配置 。 |


**返回值:** [Phaser.Tweens.TweenChain](/api/class/tweens-tweenchain) - 新  铁链.


> 源码：[src/tweens/builders/TweenChainBuilder.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tweens/builders/TweenChainBuilder.js#L15)  
引入版本：3.60.0

---
