# ParticleEmitter {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleemitter)

粒子 Emitter 是一类特殊的游戏对象,它控制着一个集合的[Particles](/api/class/gameobjects-particles-particle).

粒子 Emiters 是通过配置对象创建的。 此对象的属性可以用多种格式指定, 给您在它们返回的值上留下大量范围, 从而导致复杂的视觉效果。 以下是您可以给出的不同配置值形式 :

## 明确的静态值 : {#an-explicit-static-value}

```js
x: 400
```

当粒子产卵时,x值永远是400.

## 随机值 : {#a-random-value}

```js
x: [ 100, 200, 300, 400 ]
```

x 值将是给定阵列中随机选择的4个元素之一。

## 习惯回调 : {#a-custom-callback}

```js
x: (particle, key, t, value) => {
  return value + 50;
}
```

x值是调用此函数的结果。 仅在粒子被发射时使用, 因此它提供了初始起始值。 当粒子被更新时不使用( 请参见 onUpdate 调用)

## 起始/ 结束对象 : {#a-start-end-object}

这使得您可以控制在粒子寿命过程中给定的起始参数和结束参数之间的值变化:

```js
scale: { start: 0, end: 1 }
```

当粒子尺度在寿命期内被排放并易于1的尺度时, 粒子尺度将从 0 开始。 您也可以指定用于此变化的易度函数( 默认为 Linear ):

```js
scale: { start: 0, end: 1, ease: 'bounce.out' }
```

## 起始/结束随机对象 : {#a-start-end-random-object}

起始和结尾对象可以有一个可选的 `random` 参数。这迫使它从两个值之间随机选择一个值,并将其作为起始值,然后在参数存在期间将其放松到“结束”参数。

```js
scale: { start: 4, end: 0.5, random: true }
```

粒子将先从0.5到4的随机尺度开始,然后在整个寿命期间缩放到最终值。您可以将以上参数与`ease`参数结合起来,从而控制值的放松。

## 插值对象 : {#an-interpolation-object}

您可以提供一系列在粒子寿命期间用于插值的数值。 您也可以定义要使用的插值函数。 提供了三种: `linear`( 默认值)、 `bezier`和 `catmull`, 或者您可以提供自己的函数 。

```js
x: { values: [ 50, 500, 200, 800 ], interpolation: 'catmull' }
```

粒子尺度在寿命期内通过其他点从50到800的射出时会插到800。您还可以指定一个通过值控制变化速率的易函数(默认为线性):

```js
x: { values: [ 50, 500, 200, 800 ], interpolation: 'catmull', ease: 'bounce.out }
```

## 已踩踏的发射对象 : {#a-stepped-emitter-object}

`steps`参数允许您控制顺序粒子在起始范围之间的位置:

```js
x: { steps: 32, start: 0, end: 576 }
```

这里有576个范围(开始到结束),分为32个步骤。

第一个粒子会在 0 的 x 位置发射。 下一个粒子将在下一个“ 末端” 的 沿边发射, 也就是 18 个。 以下粒子将在下一个步骤发射, 也就是 36 个, 诸如此类。 因为 576 的射程已被 32 个除去, 从而产生 18 像素 。 当一个粒子达到“ 末端”值时, 下一个粒子将重新开始 。

## 带有 Yyo 的 阶梯式发射对象 : {#a-stepped-emitter-object-with-yoyo}

您可以将可选的 `yoyo` 属性添加到一个已踩到的对象中 :

```js
x: { steps: 32, start: 0, end: 576, yoyo: true }
```

和已踩踏的发射器一样, 粒子会按顺序发射, 从“ 启动” 到“ 结束” 的跳跃。 通常情况下, 当一个已踩踏的发射机到达终点时, 它会转动到开始值。 然而, 如果您提供了“ yo” 参数, 那么当它到达终点时, 它将会反向向向返回到“ 启动 ” 。 取决于您需要的效果, 这样的效果通常会更好 。

## 分钟/ 最大对象 : {#a-min-max-object}

这使得您可以在分钟和最大属性之间选择随机浮点值:

```js
x: { min: 100, max: 700 }
```

x 值将是在分钟和最大值之间的随机浮点。

您可以通过设置“ int” 旗来强制它选择整数 :

```js
x: { min: 100, max: 700, int: true }
```

或者,您可以使用“ 随机” 矩阵方法( 见下文)

## 随机对象 : {#a-random-object}

这使得您可以在第一个和第二个阵列元素之间选择随机整数值:

```js
x: { random: [ 100, 700 ] }
```

x 值将是100到700之间的随机整数,因为它将“ 随机” 阵列中的第一个元素作为“ min” 值, 第 2 元素作为“ max” 值。

## 自定义 onEmit和 onUpdate 回调: {#custom-onemit-and-onupdate-callbacks}

如果以上内容不能给您带来您所追求的效果,您可以提供您自己的回调,当粒子同时被排放和更新时,这些回调将被使用:

```js
x: {
  onEmit: (particle, key, t, value) => {
    return value;
  },
  onUpdate: (particle, key, t, value) => {
    return value;
  }
}
```

您可以提供一种或两种功能。 `onEmit` 是在粒子生命开始时调用, 并定义属性在出生时的价值 。

`onUpdate`函数每次粒子 Emitter 更新到粒子死亡时都称为它。两者都必须返回一个值 。

属性为:

粒子 - 指粒子实例。 键 - 属性的字符串键, 即“ x” 或“ lifespan ” t - 当前粒子的正常寿命, 0( 出生) 和 1( 死亡) 之间。 值 - 当前属性值。 您至少应该返回此值 。

通过使用上述配置选项,您可以无限控制您的粒子行为。

## v3.60 差额 {#v360-differences}

在v3.60 Phaser之前,它使用了`ParticleEmitterManager`。在v3.60中,这个被删除,现在叫`this.add.particles`返回一个`ParticleEmitter`的例子。

为了精简内存和显示列表,我们已经完全删除了 `ParticleEmitterManager`。当你给 `this.add.particles`打电话时,你正在创建 `ParticleEmitter`实例,它正直接添加到显示列表中,并且可以像其他游戏对象一样被操纵,即缩放,旋转,定位,添加到容器等。它现在扩展了 `GameObject`的基础类,意思是它也是一个事件发射器,它允许我们为粒子创建一些手动的新事件。

所以,为了创建一个发射器,你现在给它一个xy坐标,一个纹理和一个发射器配置对象(你也可以在稍后设置,但最常见的是,你会在创建时这样做). I. e:

```js
const emitter = this.add.particles(100, 300, 'flares', {
  frame: 'red',
  angle: { min: -30, max: 30 },
  speed: 150
});
```

这将在100×300时产生一个"红色信号弹"发射器.

请更新您的代码, 以确保它遵守新的函数签名 。

**构造函数**

`new ParticleEmitter(scene, [x], [y], [texture], [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属的景点。 一个游戏对象只能一次属于一个景点 。 |
| x | number | 是 | 这个游戏对象在世界的横向位置. |
| y | number | 是 | 此游戏对象在世界的垂直位置 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | 此游戏对象将使用用于渲染的纹理的密钥或实例, 如保存在纹理管理器中 。 |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](/api/typedef/types-gameobjects-particles#particleemitterconfig) | 是 | 此发射器的设置 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)  
> [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle)  
> [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode)  
> [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth)  
> [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting)  
> [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask)  
> [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes)  
> [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor)  
> [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture)  
> [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform)  
> [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible)  



> 源码：[src/gameobjects/particles/ParticleEmitter.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L107)  
引入版本：3.60.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle):**


 - [alpha](/api/namespace/gameobjects-components-alphasingle#alpha)





**From [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode):**


 - [blendMode](/api/namespace/gameobjects-components-blendmode#blendMode)





**From [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth):**


 - [depth](/api/namespace/gameobjects-components-depth#depth)





**From [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters):**


 - [filterCamera](/api/namespace/gameobjects-components-filters#filterCamera)
 - [filters](/api/namespace/gameobjects-components-filters#filters)
 - [filtersAutoFocus](/api/namespace/gameobjects-components-filters#filtersAutoFocus)
 - [filtersFocusContext](/api/namespace/gameobjects-components-filters#filtersFocusContext)
 - [filtersForceComposite](/api/namespace/gameobjects-components-filters#filtersForceComposite)
 - [maxFilterSize](/api/namespace/gameobjects-components-filters#maxFilterSize)
 - [renderFilters](/api/namespace/gameobjects-components-filters#renderFilters)





**From [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting):**


 - [lighting](/api/namespace/gameobjects-components-lighting#lighting)
 - [selfShadow](/api/namespace/gameobjects-components-lighting#selfShadow)





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [mask](/api/namespace/gameobjects-components-mask#mask)





**From [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes):**


 - [customRenderNodes](/api/namespace/gameobjects-components-rendernodes#customRenderNodes)
 - [defaultRenderNodes](/api/namespace/gameobjects-components-rendernodes#defaultRenderNodes)
 - [renderNodeData](/api/namespace/gameobjects-components-rendernodes#renderNodeData)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [scrollFactorX](/api/namespace/gameobjects-components-scrollfactor#scrollFactorX)
 - [scrollFactorY](/api/namespace/gameobjects-components-scrollfactor#scrollFactorY)





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [frame](/api/namespace/gameobjects-components-texture#frame)
 - [texture](/api/namespace/gameobjects-components-texture#texture)





**From [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform):**


 - [angle](/api/namespace/gameobjects-components-transform#angle)
 - [hasTransformComponent](/api/namespace/gameobjects-components-transform#hasTransformComponent)
 - [rotation](/api/namespace/gameobjects-components-transform#rotation)
 - [scale](/api/namespace/gameobjects-components-transform#scale)
 - [scaleX](/api/namespace/gameobjects-components-transform#scaleX)
 - [scaleY](/api/namespace/gameobjects-components-transform#scaleY)
 - [w](/api/namespace/gameobjects-components-transform#w)
 - [x](/api/namespace/gameobjects-components-transform#x)
 - [y](/api/namespace/gameobjects-components-transform#y)
 - [z](/api/namespace/gameobjects-components-transform#z)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [visible](/api/namespace/gameobjects-components-visible#visible)





**From [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject):**


 - [active](/api/class/gameobjects-gameobject#active)
 - [body](/api/class/gameobjects-gameobject#body)
 - [cameraFilter](/api/class/gameobjects-gameobject#cameraFilter)
 - [data](/api/class/gameobjects-gameobject#data)
 - [displayList](/api/class/gameobjects-gameobject#displayList)
 - [ignoreDestroy](/api/class/gameobjects-gameobject#ignoreDestroy)
 - [input](/api/class/gameobjects-gameobject#input)
 - [isDestroyed](/api/class/gameobjects-gameobject#isDestroyed)
 - [name](/api/class/gameobjects-gameobject#name)
 - [parentContainer](/api/class/gameobjects-gameobject#parentContainer)
 - [renderFlags](/api/class/gameobjects-gameobject#renderFlags)
 - [scene](/api/class/gameobjects-gameobject#scene)
 - [state](/api/class/gameobjects-gameobject#state)
 - [tabIndex](/api/class/gameobjects-gameobject#tabIndex)
 - [type](/api/class/gameobjects-gameobject#type)
 - [vertexRoundMode](/api/class/gameobjects-gameobject#vertexRoundMode)




---

## 公开成员 {#public-members}

### acceleration {#acceleration}

#### acceleration: boolean {#acceleration-boolean}


**说明:**

accelerationX和accelerationY是否为非零。在配置过程中自动设定 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L461](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L461)  
引入版本：3.0.0


---

### accelerationX {#accelerationX}

#### accelerationX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#accelerationx-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

水平加速适用于排放的颗粒,以每秒平方像素计。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3132)  
引入版本：3.60.0


---

### accelerationY {#accelerationY}

#### accelerationY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#accelerationy-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

垂直加速度适用于排放的颗粒,以每秒平方像素计。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3156)  
引入版本：3.60.0


---

### animCounter {#animCounter}

#### animCounter: number {#animcounter-number}


**说明:**

内部动画计数器.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3772](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3772)  
引入版本：3.60.0


---

### animQuantity {#animQuantity}

#### animQuantity: number {#animquantity-number}


**说明:**

连续粒子数,接收单动画(每帧周期).


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L787](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L787)  
引入版本：3.60.0


---

### anims {#anims}

#### anims: Array.\<string> {#anims-arraystring}


**说明:**

分配给粒子的动画.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L767](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L767)  
引入版本：3.60.0


---

### bounce {#bounce}

#### bounce: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#bounce-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

如果设定, 速度粒子在从发射方边界反弹时会使用。 0 值意味着不反弹。 1 值意味着完全反弹 。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3356](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3356)  
引入版本：3.60.0


---

### colorEase {#colorEase}

#### colorEase: string {#colorease-string}


**说明:**

控制创建 Emitter 时使用的放松函数, 该函数使用 `color` 属性在粒子的寿命内插入其锡值 。

如果您没有给 Emitter 应用 `particleColor` , 设置此功能将没有效果 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3472](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3472)  
引入版本：3.60.0


---

### completeFlag {#completeFlag}

#### completeFlag: boolean {#completeflag-boolean}


**说明:**

内部完整旗.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3841](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3841)  
引入版本：3.60.0


---

### config {#config}

#### config: [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](/api/typedef/types-gameobjects-particles#particleemitterconfig) {#config-phasertypesgameobjectsparticlesparticleemitterconfig}


**说明:**

内部对象为 Emitter 持有配置 。

这些是Emitter配置剖析的一部分。

你通常不直接访问它们,而是使用`ParticleEmitter.setConfig`或`ParticleEmitter.updateConfig`方法.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L375](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L375)  
引入版本：3.85.0


---

### currentAnim {#currentAnim}

#### currentAnim: number {#currentanim-number}


**说明:**

现动画索引.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3933](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3933)  
引入版本：3.60.0


---

### currentFrame {#currentFrame}

#### currentFrame: number {#currentframe-number}


**说明:**

当前帧指数.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3910](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3910)  
引入版本：3.60.0


---

### deathCallback {#deathCallback}

#### deathCallback: [Phaser.Types.GameObjects.Particles.ParticleDeathCallback](/api/typedef/types-gameobjects-particles#particledeathcallback) {#deathcallback-phasertypesgameobjectsparticlesparticledeathcallback}


**说明:**

粒子死亡时调用函数 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L504](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L504)  
引入版本：3.0.0


---

### deathCallbackScope {#deathCallbackScope}

#### deathCallbackScope: * {#deathcallbackscope}


**说明:**

[Phaser.GameObjects.Particles.ParticleEmitter#deathCallback](/api/class/gameobjects-particles-particleemitter#deathCallback)的呼声背景.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L514](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L514)  
引入版本：3.0.0


---

### deathZones {#deathZones}

#### deathZones: Array.\<[Phaser.GameObjects.Particles.Zones.DeathZone](/api/class/gameobjects-particles-zones-deathzone)> {#deathzones-arrayphasergameobjectsparticleszonesdeathzone}


**说明:**

包含粒子死亡区物体的阵列。 粒子的x/y坐标与配置的死亡区相交后立即被杀死。

在Phaser v3.60之前,一个Emitter只能拥有一个单一的死亡区,在3.60中,现在他们可以拥有一系列死亡区.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L663](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L663)  
引入版本：3.60.0


---

### delay {#delay}

#### delay: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#delay-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

排放后等待粒子更新的毫秒数。 这使得您可以释放显示“ 静态” 或仍在屏幕上的粒子, 然后, 值开始移动 。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3669](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3669)  
引入版本：3.60.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

发射器在停止排放之前,在流动状态下发射颗粒时的毫秒数。 值为 0( 默认值) 表示没有持续时间 。

当持续时间到期时, `STOP`事件会释放。请注意,进入停止状态并不意味着所有粒子都已完成,只是它不会再释放。

要知道最终粒子何时到期,请听听 CompLETE事件.

每次调用`ParticleEmitter.start`方法时,计数器都会重置.

0表示发射机不会根据持续时间停止.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L574](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L574)  
引入版本：3.60.0


---

### elapsed {#elapsed}

#### elapsed: number {#elapsed-number}


**说明:**

内部的柜台。

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3795](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3795)  
引入版本：3.60.0


---

### emitCallback {#emitCallback}

#### emitCallback: [Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](/api/typedef/types-gameobjects-particles#particleemittercallback) {#emitcallback-phasertypesgameobjectsparticlesparticleemittercallback}


**说明:**

粒子发射时调用函数 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L484](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L484)  
引入版本：3.0.0


---

### emitCallbackScope {#emitCallbackScope}

#### emitCallbackScope: * {#emitcallbackscope}


**说明:**

[Phaser.GameObjects.Particles.ParticleEmitter#emitCallback](/api/class/gameobjects-particles-particleemitter#emitCallback)的呼声背景.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L494](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L494)  
引入版本：3.0.0


---

### emitting {#emitting}

#### emitting: boolean {#emitting-boolean}


**说明:**

控制发射体目前排放粒子流(当频率为 QQ 0 时) 。

已经存在的粒子会不断更新,直到到期.

由[Phaser.GameObjects.Particles.ParticleEmitter#start](/api/class/gameobjects-particles-particleemitter#start)和[Phaser.GameObjects.Particles.ParticleEmitter#stop](/api/class/gameobjects-particles-particleemitter#stop)控制.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L610](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L610)  
引入版本：3.0.0


---

### emitZones {#emitZones}

#### emitZones: Array.\<[Phaser.Types.GameObjects.Particles.EmitZoneObject](/api/typedef/types-gameobjects-particles#emitzoneobject)> {#emitzones-arrayphasertypesgameobjectsparticlesemitzoneobject}


**说明:**

包含粒子排放区的阵列。 这些阵列可以是边缘区域,也可以是随机区域。

从此数组中随机选择的区域中释放粒子 。

在Phaser v3.60之前,一个Emitter只能有一个单一的排出区,在3.60中,它们现在可以拥有一系列排出区。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L648](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L648)  
引入版本：3.60.0


---

### flowCounter {#flowCounter}

#### flowCounter: number {#flowcounter-number}


**说明:**

内流计数器.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3726](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3726)  
引入版本：3.60.0


---

### follow {#follow}

#### follow: [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) {#follow-phasertypesmathvector2like}


**说明:**

以位置作为粒子源的游戏对象。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L702](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L702)  
引入版本：3.0.0


---

### followOffset {#followOffset}

#### followOffset: [Phaser.Math.Vector2](/api/class/math-vector2) {#followoffset-phasermathvector2}


**说明:**

抵消来自[Phaser.GameObjects.Particles.ParticleEmitter#follow](/api/class/gameobjects-particles-particleemitter#follow)目标粒子的源头.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L714](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L714)  
引入版本：3.0.0


---

### frameCounter {#frameCounter}

#### frameCounter: number {#framecounter-number}


**说明:**

内框计数器.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3749](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3749)  
引入版本：3.60.0


---

### frameQuantity {#frameQuantity}

#### frameQuantity: number {#framequantity-number}


**说明:**

连续粒子数,得到一个单一的纹理框架(每个帧周期).


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L756](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L756)  
引入版本：3.0.0


---

### frames {#frames}

#### frames: Array.\<[Phaser.Textures.Frame](/api/class/textures-frame)> {#frames-arrayphasertexturesframe}


**说明:**

分配给粒子的纹理框架.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L736](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L736)  
引入版本：3.0.0


---

### frequency {#frequency}

#### frequency: number {#frequency-number}


**说明:**

对于流体发射器, 粒子流周期之间的时间间隔( QQ 0) 以毫秒计。 值为 0 表示每次逻辑更新( 最大流频率) 都有一个粒子流周期。 这是默认设置 。 对于爆炸式发射器, 这个值将是 -1. 调用 [Phaser.GameObjects.Particles.ParticleEmitter#flow](/api/class/gameobjects-particles-particleemitter#flow) 也会使发射器处于流态( QQ0 频率) 。 调用 [Phaser.GameObjects.Particles.ParticleEmitter#explode](/api/class/gameobjects-particles-particleemitter#explode) 也会使该发射器处于爆炸模式( 频率= - 1) 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L595](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L595)  
引入版本：3.0.0


---

### gravityX {#gravityX}

#### gravityX: number {#gravityx-number}


**说明:**

水平加速度适用于排放的粒子,以每秒平方像素计。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L439)  
引入版本：3.0.0


---

### gravityY {#gravityY}

#### gravityY: number {#gravityy-number}


**说明:**

对发射的粒子应用垂直加速,以每秒平方像素计。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L450](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L450)  
引入版本：3.0.0


---

### hold {#hold}

#### hold: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#hold-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

粒子完成后等待时间的毫秒数会被移除。 这样您就可以在粒子到达最终状态后, 在屏幕上“ 持有” , 然后再消失 。

注意所有粒子更新都会停止,包括改变α,尺度,运动或动画.

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3696](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3696)  
引入版本：3.60.0


---

### lifespan {#lifespan}

#### lifespan: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#lifespan-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

所排放粒子的寿命。 此值以毫秒表示, 默认值为1000 毫秒。 当粒子达到此值时, 将死亡 。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3560](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3560)  
引入版本：3.60.0


---

### maxAliveParticles {#maxAliveParticles}

#### maxAliveParticles: number {#maxaliveparticles-number}


**说明:**

最大存活量和释放量的粒子数将会更新。 当达到此限制时, 粒子需要死才能释放另一个粒子 。

0表示无限制.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L538](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L538)  
引入版本：3.60.0


---

### maxParticles {#maxParticles}

#### maxParticles: number {#maxparticles-number}


**说明:**

设定为硬限制该发射器可创建的粒子对象总数。 这是它可以创建的 `Particle` 实例的数目, 而不是“ 活性” 粒子的数目 。

0表示无限.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L524](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L524)  
引入版本：3.0.0


---

### maxVelocityX {#maxVelocityX}

#### maxVelocityX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#maxvelocityx-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

最大水平发射速度粒子可以达到,以每秒像素计.

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3180)  
引入版本：3.60.0


---

### maxVelocityY {#maxVelocityY}

#### maxVelocityY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#maxvelocityy-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

最大垂直速度排放的粒子可以达到,以每秒像素计.

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3205)  
引入版本：3.60.0


---

### moveTo {#moveTo}

#### moveTo: boolean {#moveto-boolean}


**说明:**

是否设定了 moveToX 和 moveToY 。 在配置过程中自动设定 。

当粒子真的向着地球移动 moveToX 财务报告和已审计财务报表 moveToY 坐标和到达生命的尽头 闪亮角度 speedX,和 speedY 被忽略了,我们没有被忽略。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L471](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L471)  
引入版本：3.0.0


---

### moveToX {#moveToX}

#### moveToX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#movetox-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

当[Phaser.GameObjects.Particles.ParticleEmitter#moveTo](/api/class/gameobjects-particles-particleemitter#moveTo)是真的时, x 坐标向发射的粒子移动。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3308](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3308)  
引入版本：3.60.0


---

### moveToY {#moveToY}

#### moveToY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#movetoy-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

当[Phaser.GameObjects.Particles.ParticleEmitter#moveTo](/api/class/gameobjects-particles-particleemitter#moveTo)是真的时,Y坐标发射的粒子会向着它移动。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3332](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3332)  
引入版本：3.60.0


---

### ops {#ops}

#### ops: [Phaser.Types.GameObjects.Particles.ParticleEmitterOps](/api/typedef/types-gameobjects-particles#particleemitterops) {#ops-phasertypesgameobjectsparticlesparticleemitterops}


**说明:**

一个内部对象, 持有所有 EmitterOp 实例 。

这些是Emitter配置剖析的一部分。

您通常不会直接访问它们, 而是使用此类上提供的获取器和设置器, 如 `ParticleEmitter.speedX` 等 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L389](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L389)  
引入版本：3.60.0


---

### particleAlpha {#particleAlpha}

#### particleAlpha: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#particlealpha-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

发射粒子的α值。 这是 0 至 1. 之间的值, 具有α 0 的粒子是无形的, 因此不渲染, 但仍在由 Emitter 处理 。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3533](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3533)  
引入版本：3.60.0


---

### particleAngle {#particleAngle}

#### particleAngle: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#particleangle-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

粒子发射的角度。 数值以度表示。 您可以控制发射器的方向。 如果您想要改变粒子本身的旋转, 请查看 `particleRotate` 属性 。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3586](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3586)  
引入版本：3.60.0


---

### particleBringToTop {#particleBringToTop}

#### particleBringToTop: boolean {#particlebringtotop-boolean}


**说明:**

新排放的颗粒被添加到颗粒清单的顶端,即被制成在已经活着的颗粒之上.

准备去骗他们 让他们去后面

也参见`sortOrder`属性,用于更复杂的粒子分类.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L624](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L624)  
引入版本：3.0.0


---

### particleClass {#particleClass}

#### particleClass: function {#particleclass-function}


**说明:**

由这个 Emitter 发射的粒子级。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L364)  
引入版本：3.0.0


---

### particleColor {#particleColor}

#### particleColor: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#particlecolor-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

用于释放粒子纹理的颜色色线值。 数值应该以六进制格式给出, 即红色线的 0xff000, 并且不应包含 alpha 通道 。

锡是默认的倍数,意思是白(0xffffff)的锡值会有效地将锡重新设置为无.

修改 `ParticleEmitter.tintMode` 属性以改变锡模式 。

当您通过 Emitter 配置定义颜色时, 您应该将其作为一系列颜色值给出。 粒子会在其寿命期内通过这些颜色插入。 设置此值将覆盖任何也可能给出的 `tint`值 。

这是WebGL的唯一功能。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3434](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3434)  
引入版本：3.60.0


---

### particleRotate {#particleRotate}

#### particleRotate: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#particlerotate-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

每个粒子在发射时的旋转(或角度),数值以度表示,并使用右手坐标系统,其中0度指向右方,90度指向下方,-90度指向上方。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3613](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3613)  
引入版本：3.60.0


---

### particleScaleX {#particleScaleX}

#### particleScaleX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#particlescalex-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

排放粒子的横向尺度。

这是相对于 Emiters 和任何父母的尺度。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3382](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3382)  
引入版本：3.60.0


---

### particleScaleY {#particleScaleY}

#### particleScaleY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#particlescaley-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

排放粒子的垂直尺度。

这是相对于 Emiters 和任何父母的尺度。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3408](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3408)  
引入版本：3.60.0


---

### particleTint {#particleTint}

#### particleTint: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#particletint-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

用于释放粒子纹理的颜色色线值。 数值应该以六进制格式给出, 即红色线的 0xff000, 并且不应包含 alpha 通道 。

锡是默认的倍数,意思是白(0xffffff)的锡值会有效地将锡重新设置为无.

修改 `ParticleEmitter.tintMode` 属性以改变锡模式 。

如果提供`color`阵列,则`tint`值将被覆盖。

这是WebGL的唯一功能。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3498](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3498)  
引入版本：3.60.0


---

### particleX {#particleX}

#### particleX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype), [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) {#particlex-phasertypesgameobjectsparticlesemitteroponemittype-phasertypesgameobjectsparticlesemitteroponupdatetype}


**说明:**

X坐标粒子是从中发射出来的.

这是相对于 Emiters x 坐标和任何父坐标的。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3080](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3080)  
引入版本：3.60.0


---

### particleY {#particleY}

#### particleY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype), [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) {#particley-phasertypesgameobjectsparticlesemitteroponemittype-phasertypesgameobjectsparticlesemitteroponupdatetype}


**说明:**

粒子的Y坐标被发射出来。

这是相对于 Emitters y 坐标和任何父母的坐标。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3106](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3106)  
引入版本：3.60.0


---

### processors {#processors}

#### processors: Phaser.Structs.List.\<Phaser.GameObjects.Particles.ParticleProcessor> {#processors-phaserstructslistphasergameobjectsparticlesparticleprocessor}


**说明:**

此 Emitter 管理中的粒子处理器列表 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L893](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L893)  
引入版本：3.60.0


---

### quantity {#quantity}

#### quantity: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#quantity-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

每次排放时,即从一个“爆炸”或一个“流”周期中每个框架排放的粒子数量。

默认为 1.

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3640](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3640)  
引入版本：3.60.0


---

### radial {#radial}

#### radial: boolean {#radial-boolean}


**说明:**

射线发射器会在角分和最大之间向各个方向发射粒子, 使用 [Phaser.GameObjects.Particles.ParticleEmitter#speed](/api/class/gameobjects-particles-particleemitter#speed)作为值。 如果设定为假, 则它就起到点分发射器的作用。 点发射器将只发射出来自 speedX和 speedY 值的方向 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L426](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L426)  
引入版本：3.0.0


---

### randomAnim {#randomAnim}

#### randomAnim: boolean {#randomanim-boolean}


**说明:**

动画是否随机选择 [Phaser.GameObjects.Particles.ParticleEmitter#anims](/api/class/gameobjects-particles-particleemitter#anims) 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L776](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L776)  
引入版本：3.60.0


---

### randomFrame {#randomFrame}

#### randomFrame: boolean {#randomframe-boolean}


**说明:**

是否随机选择纹理 [Phaser.GameObjects.Particles.ParticleEmitter#frames](/api/class/gameobjects-particles-particleemitter#frames) 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L745](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L745)  
引入版本：3.0.0


---

### skipping {#skipping}

#### skipping: boolean {#skipping-boolean}


**说明:**

用于判断发射器何时处于快速前行模式的内部属性.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L839](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L839)  
引入版本：3.60.0


---

### sortCallback {#sortCallback}

#### sortCallback: [Phaser.Types.GameObjects.Particles.ParticleSortCallback](/api/typedef/types-gameobjects-particles#particlesortcallback) {#sortcallback-phasertypesgameobjectsparticlesparticlesortcallback}


**说明:**

用于排序粒子的调用。 只有在 `sortProperty` 设定时才使用。 通过 `setSortCallback` 方法设置 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L883](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L883)  
引入版本：3.60.0


---

### sortOrderAsc {#sortOrderAsc}

#### sortOrderAsc: boolean {#sortorderasc-boolean}


**说明:**

当 `sortProperty` 定义时, 它控制了排序顺序, 无论是升降。 切换来控制视觉效果 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L873](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L873)  
引入版本：3.60.0


---

### sortProperty {#sortProperty}

#### sortProperty: string {#sortproperty-string}


**说明:**

可在此属性基础上对粒子进行可选排序。 属性必须存在于 `Particle` 类上, 如 `y` 、 `lifeT` 、 `scaleX` 等 。

当设定此选项时, 将覆盖 `particleBringToTop` 设置 。

要重设此选项并禁用排序, 请将此属性设置为空字符串 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L858](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L858)  
引入版本：3.60.0


---

### speed {#speed}

#### speed: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#speed-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

发射粒子的初始速度, 以每秒像素计 。

如果用它来获取它,它会返回`speedX`值。

如果使用它作为设置器,它将会将`speedX`和`speedY`更新到给定值.

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3230](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3230)  
引入版本：3.60.0


---

### speedX {#speedX}

#### speedX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#speedx-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

发射粒子的初始水平速度, 以每秒像素计 。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3260](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3260)  
引入版本：3.60.0


---

### speedY {#speedY}

#### speedY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) {#speedy-phasertypesgameobjectsparticlesemitteroponemittype}


**说明:**

发射粒子的初始垂直速度, 以每秒像素计 。

访问此属性通常应该返回一个数字。 但是, 它可以设置为任何有效的 EmitterOp onEmit 类型 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3284](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3284)  
引入版本：3.60.0


---

### stopAfter {#stopAfter}

#### stopAfter: number {#stopafter-number}


**说明:**

如果设定, 无论是通过 Emitter 配置, 还是直接设置此属性, 粒子 Emitter 将在达到此总数后停止排放粒子。 然后它会进入“ 停止” 状态, 发射 `STOP` 事件。 请注意, 进入停止状态并不意味着所有粒子都已完成, 只是它没有再释放。 Name

要知道最终粒子何时到期,请听听 CompLETE事件.

如果您想要发射精确的粒子数, 并随后停止发射, 请使用此程序 。

每次调用`ParticleEmitter.start`方法时,计数器都会重置.

0 表示发射器不会根据总排放颗粒停止.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L551](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L551)  
引入版本：3.60.0


---

### stopCounter {#stopCounter}

#### stopCounter: number {#stopcounter-number}


**说明:**

内站台柜台.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3818](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3818)  
引入版本：3.60.0


---

### timeScale {#timeScale}

#### timeScale: number {#timescale-number}


**说明:**

活性粒子的时间率影响寿命、运动和扭矩。大于1的值比正常的要快。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L638](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L638)  
引入版本：3.0.0


---

### tintMode {#tintMode}

#### tintMode: [Phaser.TintModes](/api/namespace/tintmodes) {#tintmode-phasertintmodes}


**说明:**

此 Emitter 中的粒子所用的锡模式 。

可用模式有:

- Phaser.TintModes.MULTIPLY( 默认)

- Phaser.TintModes.FILL

- Phaser.TintModes.ADD

- Phaser.TintModes.SCREEN

- Phaser.TintModes.OVERLAY

- Phaser.TintModes.HARD_LIGHT


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L902](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L902)  
引入版本：4.0.0


---

### trackVisible {#trackVisible}

#### trackVisible: boolean {#trackvisible-boolean}


**说明:**

发射方的[Phaser.GameObjects.Particles.ParticleEmitter#visible](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleemitter.md#visible)状态是否会跟踪[Phaser.GameObjects.Particles.ParticleEmitter#follow](/api/class/gameobjects-particles-particleemitter#follow)目标能见度状态.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L724](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L724)  
引入版本：3.0.0


---

### viewBounds {#viewBounds}

#### viewBounds: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#viewbounds-phasergeomrectangle}


**说明:**

一个可选的矩形对象,用于渲染粒子时从显示中分解。例如,如果粒子仅限于从源头移到300x300大小的区域,那么您可以将矩形设置为这些维度。

渲染器将检查`viewBounds`矩形是否在渲染步骤中与相机的边框相交,如果不这样做,它是否会跳过完全渲染Emitter.

这样可以让您在场景中创建许多发射器,而无需在内容不可见的情况下进行渲染的成本.

注意 Emitter 将不会进行任何检查, 以查看粒子本身是否在这些界限之外。 它会简单地检查这些界限与相机的对比。 使用 `getBounds` 方法与 `advance` 参数帮助定义视图界限的位置和位置 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L677](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L677)  
引入版本：3.60.0


---

### worldMatrix {#worldMatrix}

#### worldMatrix: [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) {#worldmatrix-phasergameobjectscomponentstransformmatrix}


**说明:**

用于缓存这个发射器世界矩阵的内部变换矩阵.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L849](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L849)  
引入版本：3.60.0


---

### zoneIndex {#zoneIndex}

#### zoneIndex: number {#zoneindex-number}


**说明:**

内区指数.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3864](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3864)  
引入版本：3.60.0


---

### zoneTotal {#zoneTotal}

#### zoneTotal: number {#zonetotal-number}


**说明:**

内区总.

将此属性视为只读 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3887](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3887)  
引入版本：3.60.0


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
 - [shutdown](/api/class/events-eventemitter#shutdown)





**From [Phaser.GameObjects.Components.AlphaSingle](/api/namespace/gameobjects-components-alphasingle):**


 - [clearAlpha](/api/namespace/gameobjects-components-alphasingle#clearAlpha)
 - [setAlpha](/api/namespace/gameobjects-components-alphasingle#setAlpha)





**From [Phaser.GameObjects.Components.BlendMode](/api/namespace/gameobjects-components-blendmode):**


 - [setBlendMode](/api/namespace/gameobjects-components-blendmode#setBlendMode)





**From [Phaser.GameObjects.Components.Depth](/api/namespace/gameobjects-components-depth):**


 - [setAbove](/api/namespace/gameobjects-components-depth#setAbove)
 - [setBelow](/api/namespace/gameobjects-components-depth#setBelow)
 - [setDepth](/api/namespace/gameobjects-components-depth#setDepth)
 - [setToBack](/api/namespace/gameobjects-components-depth#setToBack)
 - [setToTop](/api/namespace/gameobjects-components-depth#setToTop)





**From [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters):**


 - [enableFilters](/api/namespace/gameobjects-components-filters#enableFilters)
 - [focusFilters](/api/namespace/gameobjects-components-filters#focusFilters)
 - [focusFiltersOnCamera](/api/namespace/gameobjects-components-filters#focusFiltersOnCamera)
 - [focusFiltersOverride](/api/namespace/gameobjects-components-filters#focusFiltersOverride)
 - [renderWebGLFilters](/api/namespace/gameobjects-components-filters#renderWebGLFilters)
 - [setFiltersAutoFocus](/api/namespace/gameobjects-components-filters#setFiltersAutoFocus)
 - [setFiltersFocusContext](/api/namespace/gameobjects-components-filters#setFiltersFocusContext)
 - [setFiltersForceComposite](/api/namespace/gameobjects-components-filters#setFiltersForceComposite)
 - [setFilterSize](/api/namespace/gameobjects-components-filters#setFilterSize)
 - [setRenderFilters](/api/namespace/gameobjects-components-filters#setRenderFilters)
 - [willRenderFilters](/api/namespace/gameobjects-components-filters#willRenderFilters)





**From [Phaser.GameObjects.Components.Lighting](/api/namespace/gameobjects-components-lighting):**


 - [setLighting](/api/namespace/gameobjects-components-lighting#setLighting)
 - [setSelfShadow](/api/namespace/gameobjects-components-lighting#setSelfShadow)





**From [Phaser.GameObjects.Components.Mask](/api/namespace/gameobjects-components-mask):**


 - [clearMask](/api/namespace/gameobjects-components-mask#clearMask)
 - [createGeometryMask](/api/namespace/gameobjects-components-mask#createGeometryMask)
 - [setMask](/api/namespace/gameobjects-components-mask#setMask)





**From [Phaser.GameObjects.Components.RenderNodes](/api/namespace/gameobjects-components-rendernodes):**


 - [initRenderNodes](/api/namespace/gameobjects-components-rendernodes#initRenderNodes)
 - [setRenderNodeData](/api/namespace/gameobjects-components-rendernodes#setRenderNodeData)
 - [setRenderNodeRole](/api/namespace/gameobjects-components-rendernodes#setRenderNodeRole)





**From [Phaser.GameObjects.Components.RenderSteps](/api/namespace/gameobjects-components-rendersteps):**


 - [addRenderStep](/api/namespace/gameobjects-components-rendersteps#addRenderStep)
 - [renderWebGLStep](/api/namespace/gameobjects-components-rendersteps#renderWebGLStep)





**From [Phaser.GameObjects.Components.ScrollFactor](/api/namespace/gameobjects-components-scrollfactor):**


 - [setScrollFactor](/api/namespace/gameobjects-components-scrollfactor#setScrollFactor)





**From [Phaser.GameObjects.Components.Texture](/api/namespace/gameobjects-components-texture):**


 - [setFrame](/api/namespace/gameobjects-components-texture#setFrame)
 - [setTexture](/api/namespace/gameobjects-components-texture#setTexture)





**From [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform):**


 - [copyPosition](/api/namespace/gameobjects-components-transform#copyPosition)
 - [getLocalPoint](/api/namespace/gameobjects-components-transform#getLocalPoint)
 - [getLocalTransformMatrix](/api/namespace/gameobjects-components-transform#getLocalTransformMatrix)
 - [getParentRotation](/api/namespace/gameobjects-components-transform#getParentRotation)
 - [getWorldPoint](/api/namespace/gameobjects-components-transform#getWorldPoint)
 - [getWorldTransformMatrix](/api/namespace/gameobjects-components-transform#getWorldTransformMatrix)
 - [setAngle](/api/namespace/gameobjects-components-transform#setAngle)
 - [setPosition](/api/namespace/gameobjects-components-transform#setPosition)
 - [setRandomPosition](/api/namespace/gameobjects-components-transform#setRandomPosition)
 - [setRotation](/api/namespace/gameobjects-components-transform#setRotation)
 - [setScale](/api/namespace/gameobjects-components-transform#setScale)
 - [setW](/api/namespace/gameobjects-components-transform#setW)
 - [setX](/api/namespace/gameobjects-components-transform#setX)
 - [setY](/api/namespace/gameobjects-components-transform#setY)
 - [setZ](/api/namespace/gameobjects-components-transform#setZ)





**From [Phaser.GameObjects.Components.Visible](/api/namespace/gameobjects-components-visible):**


 - [setVisible](/api/namespace/gameobjects-components-visible#setVisible)





**From [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject):**


 - [addToDisplayList](/api/class/gameobjects-gameobject#addToDisplayList)
 - [addToUpdateList](/api/class/gameobjects-gameobject#addToUpdateList)
 - [destroy](/api/class/gameobjects-gameobject#destroy)
 - [disableInteractive](/api/class/gameobjects-gameobject#disableInteractive)
 - [getData](/api/class/gameobjects-gameobject#getData)
 - [getDisplayList](/api/class/gameobjects-gameobject#getDisplayList)
 - [getIndexList](/api/class/gameobjects-gameobject#getIndexList)
 - [incData](/api/class/gameobjects-gameobject#incData)
 - [removeFromDisplayList](/api/class/gameobjects-gameobject#removeFromDisplayList)
 - [removeFromUpdateList](/api/class/gameobjects-gameobject#removeFromUpdateList)
 - [removeInteractive](/api/class/gameobjects-gameobject#removeInteractive)
 - [setActive](/api/class/gameobjects-gameobject#setActive)
 - [setData](/api/class/gameobjects-gameobject#setData)
 - [setDataEnabled](/api/class/gameobjects-gameobject#setDataEnabled)
 - [setInteractive](/api/class/gameobjects-gameobject#setInteractive)
 - [setName](/api/class/gameobjects-gameobject#setName)
 - [setState](/api/class/gameobjects-gameobject#setState)
 - [setVertexRoundMode](/api/class/gameobjects-gameobject#setVertexRoundMode)
 - [toggleData](/api/class/gameobjects-gameobject#toggleData)
 - [update](/api/class/gameobjects-gameobject#update)
 - [willRender](/api/class/gameobjects-gameobject#willRender)
 - [willRoundVertices](/api/class/gameobjects-gameobject#willRoundVertices)




---

## 公开方法 {#public-methods}

### addDeathZone {#addDeathZone}

#### \<instance> addDeathZone(config) {#instance-adddeathzoneconfig}


**说明:**

在此 Emitter 中添加一个新的粒子死亡区 。

一旦一个粒子的x/y坐标与任何配置的死亡区相交,它就会立即被杀死.

`source`可以是几何形状,如圆形,矩形或三角形。只要`Phaser.Geometry`命名空间支持`contains`函数,就可以允许任何有效的对象。您可以设置`type`, 即为`onEnter`或`onLeave`。

单死区实例只能在这个Emitter内部存在一次,但可以属于多个Emitters.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Particles.DeathZoneObject](/api/typedef/types-gameobjects-particles#deathzoneobject) \| Array.\<[Phaser.Types.GameObjects.Particles.DeathZoneObject](/api/typedef/types-gameobjects-particles#deathzoneobject)> | 否 | 死亡区配置对象,死亡区实例,有效的几何对象或其中的数组. |


**返回值:** Array.\<[Phaser.GameObjects.Particles.Zones.DeathZone](/api/class/gameobjects-particles-zones-deathzone)> - 死亡区数组被添加到这个 Emitter 中 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1741](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1741)  
引入版本：3.60.0


---

### addedToScene {#addedToScene}

#### \<instance> addedToScene() {#instance-addedtoscene}


**说明:**

当此游戏对象添加到场景时调用。 将此发射器与场景的更新列表一起注册, 这样它就能收到 `preUpdate` 调用每个帧 。


**Overrides:** Phaser.GameObjects.GameObject#addedToScene


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L948](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L948)  
引入版本：3.60.0


---

### addEmitZone {#addEmitZone}

#### \<instance> addEmitZone(zone) {#instance-addemitzonezone}


**说明:**

在此 Emitter 中添加一个新的粒子排放区。

来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,,来,你,你,,来,来,来,来,,来,来,来,,,,你,你,,,你,,,,,来,,,,你,,来,,来,你,,你,你,来,你,,,,,来,,来,来,来,,,,来,,,你,你,你,来,来,你,你,来,你,来,来,来,你,,,,,来,,,来,你,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,来,,,,,, [EdgeZone](/api/typedef/types-gameobjects-particles#particleemitteredgezoneconfig) 将粒子置于它的边缘。 [source](/api/typedef/types-gameobjects-particles#edgezonesource) 可以是曲线、路径、圆形、椭圆形、线形、多边形、矩形或三角形;或任何具有合适对象的物体 [getPoints](/api/typedef/types-gameobjects-particles#edgezonesourcecallback) 方法。 。 方法。

[RandomZone](/api/typedef/types-gameobjects-particles#particleemitterrandomzoneconfig)将粒子随机置于其内部. 它的[source](/api/class/gameobjects-particles-zones-randomzone#source)可以是圆形,椭圆形,线形,多边形,矩形,或三角形;或者任何具有合适的[getRandomPoint](/api/typedef/types-gameobjects-particles#randomzonesourcecallback)方法的物体.

排放区只能存在一次

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| zone | [Phaser.Types.GameObjects.Particles.EmitZoneData](/api/typedef/types-gameobjects-particles#emitzonedata) \| Array.\<[Phaser.Types.GameObjects.Particles.EmitZoneData](/api/typedef/types-gameobjects-particles#emitzonedata)> | 否 | 排放区配置对象,随机区或边缘区实例,或其中的数组。 |


**返回值:** Array.\<[Phaser.Types.GameObjects.Particles.EmitZoneObject](/api/typedef/types-gameobjects-particles#emitzoneobject)> - 添加到此 Emitter 中的排出区数组 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1839](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1839)  
引入版本：3.60.0


---

### addParticleBounds {#addParticleBounds}

#### \<instance> addParticleBounds(x, [y], [width], [height], [collideLeft], [collideRight], [collideTop], [collideBottom]) {#instance-addparticleboundsx-y-width-height-collideleft-collideright-collidetop-collidebottom}


**说明:**

创建粒子束处理器,并添加到此 Emitter 中。

此处理器将检查是否有活动粒子撞击到定义的边界, 由世界空间的矩形指定 。

如果是这样,它们又被调整速度"再被限制"回来.

反弹的强度由`Particle.bounce`属性控制.

你应该小心确保发射粒子在一定范围内,如果设定的话,否则会随着粒子的迅速重新定位而导致无法预测的视觉结果.

粒子 Bundes 处理器从这种方法返回。 如果您想要修改区域, 您可以直接更改其 `bounds` 属性, 以及 `collideLeft` 等值 。

要禁用界限,您可以将其`active`属性设置为`false`,或者如果你不再需要,请拨打`ParticleEmitter.removeParticleProcessor`.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number \| [Phaser.Types.GameObjects.Particles.ParticleEmitterBounds](/api/typedef/types-gameobjects-particles#particleemitterbounds) | [Phaser.Types.GameObjects.Particles.ParticleEmitterBoundsAlt](/api/typedef/types-gameobjects-particles#particleemitterboundsalt) | 否 |  | 边界左边缘的x坐标,或代表矩形的物体. |
| y | number | 是 |  | 边界顶端的y坐标. |
| width | number | 是 |  | 边界的宽度。 |
| height | number | 是 |  | 界高处. |
| collideLeft | boolean | 是 | true | 粒子是否与边界的左边缘相互作用 。 |
| collideRight | boolean | 是 | true | 粒子是否与边界的右边缘相互作用 。 |
| collideTop | boolean | 是 | true | 粒子是否与边界的顶端相互作用 。 |
| collideBottom | boolean | 是 | true | 粒子是否与边界的底边相互作用 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleBounds](/api/class/gameobjects-particles-particlebounds) - 粒子束处理器。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1495](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1495)  
引入版本：3.60.0


---

### addParticleProcessor {#addParticleProcessor}

#### \<instance> addParticleProcessor(processor) {#instance-addparticleprocessorprocessor}


**说明:**

在此 Emitter 中添加一个粒子处理器, 如重力井 。

只要它的`active`属性设定,它就会从下一次更新开始处理粒子.

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| processor | T | 否 | 要添加到此 Emitter 管理器的粒子处理器 。 |


**返回值:** T - 此 Emitter 管理器中添加的粒子处理器 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2070](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2070)  
引入版本：3.60.0


---

### atLimit {#atLimit}

#### \<instance> atLimit() {#instance-atlimit}


**说明:**

是否该发射器处于其硬盖限制(maxParticles),如果设置的话,或者允许的最大数为“活性”粒子(maxAliveParticles)。


**返回值:** boolean - 返回值 `true` 如果此 Emitter 处于极限,或 `false` 如果没有限制,或低于 `maxParticles` 级别。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2231)  
引入版本：3.0.0


---

### clearDeathZones {#clearDeathZones}

#### \<instance> clearDeathZones() {#instance-cleardeathzones}


**说明:**

清除所有死亡区域 从这个粒子埃米特。


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1824](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1824)  
引入版本：3.70.0


---

### clearEmitZones {#clearEmitZones}

#### \<instance> clearEmitZones() {#instance-clearemitzones}


**说明:**

清除所有排放区 从这个粒子排放。


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1934](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1934)  
引入版本：3.70.0


---

### createEmitter {#createEmitter}

#### \<instance> createEmitter() {#instance-createemitter}


**说明:**

如果错误地称此函数为Phaser v3.55, 则向控制台打印一个警告。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3068](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3068)  
引入版本：3.60.0


---

### createGravityWell {#createGravityWell}

#### \<instance> createGravityWell(config) {#instance-creategravitywellconfig}


**说明:**

创建新的重力井, 添加到此 Emitter 中, 并返回引用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Particles.GravityWellConfig](/api/typedef/types-gameobjects-particles#gravitywellconfig) | 否 | 要创建的重力井配置设置 。 |


**返回值:** [Phaser.GameObjects.Particles.GravityWell](/api/class/gameobjects-particles-gravitywell) - 重力井是创造出来的


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2142)  
引入版本：3.60.0


---

### depthSort {#depthSort}

#### \<instance> depthSort() {#instance-depthsort}


**说明:**

用 [Phaser.GameObjects.Particles.ParticleEmitter#depthSortCallback](/api/class/gameobjects-particles-particleemitter#depthSortCallback) 排序活动粒子 。


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2568](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2568)  
引入版本：3.0.0


---

### depthSortCallback {#depthSortCallback}

#### \<instance> depthSortCallback(a, b) {#instance-depthsortcallbacka-b}


**说明:**

计算两个粒子的差值,以便按深度排序。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | object | 否 | 初一粒粒. |
| b | object | 否 | 第二颗粒子。 |


**返回值:** number - a和b的y坐标的差数.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2583](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2583)  
引入版本：3.0.0


---

### emitParticle {#emitParticle}

#### \<instance> emitParticle([count], [x], [y]) {#instance-emitparticlecount-x-y}


**说明:**

在特定位置(或发射电流位置)发射粒子。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| count | number | 是 | "this.quantity" | 弹出粒子的数量。 |
| x | number | 是 | "this.x" | X坐标从中释放粒子。 |
| y | number | 是 | "this.y" | 发射粒子的Y坐标 |


**返回值:** [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle), undefined - 最近排放的粒子,或如果发射器处于极限,则使用`undefined`。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2684](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2684)  
引入版本：3.0.0


---

### emitParticleAt {#emitParticleAt}

#### \<instance> emitParticleAt([x], [y], [count]) {#instance-emitparticleatx-y-count}


**说明:**

向指定位置发射粒子。 如果没有给出位置, 它将从此 Emiters 当前位置中发射 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | "this.x" | X坐标从中释放粒子。 |
| y | number | 是 | "this.y" | 发射粒子的Y坐标 |
| count | number | 是 | "this.quantity" | 弹出粒子的数量。 |


**返回值:** [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle), undefined - 最近排放的粒子,或如果发射器处于极限,则使用`undefined`。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2666](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2666)  
引入版本：3.0.0


---

### explode {#explode}

#### \<instance> explode([count], [x], [y]) {#instance-explodecount-x-y}


**说明:**

将发射器置于爆炸模式(频率= -1),停止任何流粒子流,并同时发射数颗粒子。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| count | number | 是 | "this.quantity" | 弹出粒子的数量。 |
| x | number | 是 | "this.x" | X坐标从中释放粒子。 |
| y | number | 是 | "this.y" | 发射粒子的Y坐标 |


**返回值:** [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle), undefined - 最近排放的粒子,或如果发射器处于极限,则使用`undefined`。


**Fires:** [Phaser.GameObjects.Particles.Events#event:EXPLODE](/api/event/gameobjects-particles-events#explode)


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2640](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2640)  
引入版本：3.0.0


---

### fastForward {#fastForward}

#### \<instance> fastForward(time, [delta]) {#instance-fastforwardtime-delta}


**说明:**

快速前进这个粒子 释放及其所有粒子

工作方式是将 Emitter `preUpdate` 处理器运行在一个循环中,直到每个循环`delta`步骤达到`time`.

所有通常会发射的回调和发射器相关事件仍将被引用.

您可以使用 `advance` 属性通过 issue 配置使 spast 向前 。 设定此值为您希望 spission 快速向前 。 或者, 将这种方法称为 后创建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 推进粒子喷射器的毫秒数 。 |
| delta | number | 是 | 每一步使用的三角洲数量。默认为1000 / 60. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2765](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2765)  
引入版本：3.60.0


---

### flow {#flow}

#### \<instance> flow(frequency, [count], [stopAfter]) {#instance-flowfrequency-count-stopafter}


**说明:**

将发射器置于流态(频率QQ 0)并启动(或重新启动)粒子流.

要恢复流流的频率和数量,请使用[Phaser.GameObjects.Particles.ParticleEmitter#start](/api/class/gameobjects-particles-particleemitter#start)代替.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| frequency | number | 否 |  | 每个流周期的时间间隔(QQ 0),以ms为单位. |
| count | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 1 | 在每个流周期中发射的粒子数量. |
| stopAfter | number | 是 |  | 一旦达到此值, 停止发射此粒子。 设定为 0 , 以无限计。 设置此参数将覆盖 Emitter 配置对象中已经设定的任何 `stopAfter` 值 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


**Fires:** [Phaser.GameObjects.Particles.Events#event:START](/api/event/gameobjects-particles-events#start)


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2608](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2608)  
引入版本：3.0.0


---

### forEachAlive {#forEachAlive}

#### \<instance> forEachAlive(callback, context) {#instance-foreachalivecallback-context}


**说明:**

调用此发射器中每个活动粒子的函数。 函数发送两个参数: 引用粒子实例和这个 Emitter 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](/api/typedef/types-gameobjects-particles#particleemittercallback) | 否 | 职能. |
| context | * | 否 | 函数调用上下文. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2337](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2337)  
引入版本：3.0.0


---

### forEachDead {#forEachDead}

#### \<instance> forEachDead(callback, context) {#instance-foreachdeadcallback-context}


**说明:**

调用函数, 用于此发射器中的每个不活动粒子 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](/api/typedef/types-gameobjects-particles#particleemittercallback) | 否 | 职能. |
| context | * | 否 | 函数调用上下文. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2363](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2363)  
引入版本：3.0.0


---

### getAliveParticleCount {#getAliveParticleCount}

#### \<instance> getAliveParticleCount() {#instance-getaliveparticlecount}


**说明:**

获得此发射器中的活性(在使用)颗粒数。


**返回值:** number - 带`active=true`的粒子数量.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2192)  
引入版本：3.0.0


---

### getAnim {#getAnim}

#### \<instance> getAnim() {#instance-getanim}


**说明:**

如果人口密集,从 [Phaser.GameObjects.Particles.ParticleEmitter#anims](/api/class/gameobjects-particles-particleemitter#anims) 中选择动画 。


**返回值:** string - 动画片,或者`null`,如果没有。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1368)  
引入版本：3.60.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([padding], [advance], [delta], [output]) {#instance-getboundspadding-advance-delta-output}


**说明:**

返回从当前所有_ 活动_ 粒子在此 Emitter 中的边框计算出的边框矩形。 如果此 Emitter 刚刚创建但尚未渲染, 那么使用此方法将返回一个最大安全整数的矩形。 使用 `advance` 参数来避免此现象 。

通常, 爱密特要花几秒钟才能“ 变暖 ” 。 您可以使用 `advance` 和 `delta` 参数来迫使爱密特“ 快速前进 ” , 以便尝试让边框更准确, 因为它会根据粒子的边界计算出跨越所有时间段的界限, 从而给出更好的结果 。

您也可以使用 `padding` 参数来增加边框的大小。在方向或寿命方面有很多随机性的 Emiters 通常可以返回比最大范围小的边框。如果需要,您可以使用 `padding`(和 `advance`) 来帮助限制此值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| padding | number | 是 | 贴的量,以像素表示,以加入边框矩形. |
| advance | number | 是 | 将粒子 Emitter 推进的 ms 数。默认为 0, 即没有使用 。 |
| delta | number | 是 | 每一步使用的三角洲数量。默认为1000 / 60. |
| output | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 将结果存储的矩形。 如果不给定新的, 将会创建 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 包含此 Emitter 计算界限的矩形 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2966](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2966)  
引入版本：3.60.0


---

### getDeadParticleCount {#getDeadParticleCount}

#### \<instance> getDeadParticleCount() {#instance-getdeadparticlecount}


**说明:**

获取此发射器中的不活动(可用)粒子数量。


**返回值:** number - 带`active=false`的粒子数量.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2205)  
引入版本：3.0.0


---

### getDeathZone {#getDeathZone}

#### \<instance> getDeathZone(particle) {#instance-getdeathzoneparticle}


**说明:**

使用给定的粒子并检查是否将配置的死亡区杀死它并返回结果。 这种方法作为 `Particle.update` 进程的一部分自动调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 用来测试死亡区的粒子 |


**返回值:** boolean - 如果粒子应该被杀死的话,`true`,否则就是`false`.


**Fires:** [Phaser.GameObjects.Particles.Events#event:DEATH_ZONE](/api/event/gameobjects-particles-events#death_zone)


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1998](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1998)  
引入版本：3.60.0


---

### getEmitZone {#getEmitZone}

#### \<instance> getEmitZone(particle) {#instance-getemitzoneparticle}


**说明:**

选择给定的粒子并设置其x/y坐标,以匹配下一个可用的排放区,如果已经配置。这种方法会自动被称为`Particle.fire`进程的一部分。

排泄区是按顺序排列的。一旦一个区域从中释放出粒子,就用下一个区域等循环。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 设定排放区的粒子 。 |


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1951](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1951)  
引入版本：3.60.0


---

### getFrame {#getFrame}

#### \<instance> getFrame() {#instance-getframe}


**说明:**

从 [Phaser.GameObjects.Particles.ParticleEmitter#frames](/api/class/gameobjects-particles-particleemitter#frames) 中选择一个纹理框架 。


**返回值:** [Phaser.Textures.Frame](/api/class/textures-frame) - 纹理框架.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1257)  
引入版本：3.0.0


---

### getParticleCount {#getParticleCount}

#### \<instance> getParticleCount() {#instance-getparticlecount}


**说明:**

获得此发射器中的粒子总数。


**返回值:** number - 粒子的数量,包括生与死.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2218)  
引入版本：3.0.0


---

### getProcessors {#getProcessors}

#### \<instance> getProcessors() {#instance-getprocessors}


**说明:**

获取所有活动粒子处理器。


**返回值:** Array.\<[Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor)> - - 一系列活跃的粒子处理器。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2129)  
引入版本：3.60.0


---

### killAll {#killAll}

#### \<instance> killAll() {#instance-killall}


**说明:**

立即解除这个发射器中的每个粒子的活性.

这些粒子被杀死,但不会发出事件或回电.


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2314](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2314)  
引入版本：3.0.0


---

### onParticleDeath {#onParticleDeath}

#### \<instance> onParticleDeath(callback, [context]) {#instance-onparticledeathcallback-context}


**说明:**

设置一个函数来调用每个粒子死亡。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleDeathCallback](/api/typedef/types-gameobjects-particles#particledeathcallback) | 否 | 职能. |
| context | * | 是 | 函数调用上下文. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2282)  
引入版本：3.0.0


---

### onParticleEmit {#onParticleEmit}

#### \<instance> onParticleEmit(callback, [context]) {#instance-onparticleemitcallback-context}


**说明:**

设置调用每个新发射的粒子的函数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](/api/typedef/types-gameobjects-particles#particleemittercallback) | 否 | 职能. |
| context | * | 是 | 呼唤语境. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2250](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2250)  
引入版本：3.0.0


---

### overlap {#overlap}

#### \<instance> overlap(target) {#instance-overlaptarget}


**说明:**

使用矩形几何天体或弧形物理体进行测试,以查看它是否与这个Emitter中目前存在的任何粒子相交。

重叠粒子在数组中返回, 您可以在此进行进一步处理。 如果无重叠, 数组将是空的 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) \| [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body) | 否 | 一个矩形或弧形物理体 来检查与所有活粒子的交叉点 |


**返回值:** Array.\<[Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle)> - 与给定目标重叠的粒子数组 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2930](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2930)  
引入版本：3.60.0


---

### pause {#pause}

#### \<instance> pause() {#instance-pause}


**说明:**

发射机的[Deactivates](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleemitter.md#active)。


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2467](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2467)  
引入版本：3.0.0


---

### preDestroy {#preDestroy}

#### \<instance> preDestroy() {#instance-predestroy}


**说明:**

摧毁这颗粒子 Emitter 和它拥有的所有粒子。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L3956](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L3956)  
引入版本：3.60.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

更新此发射器及其颗粒。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 请求动画框架或SetTimeout生成的当前时间戳 。 |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


**Fires:** [Phaser.GameObjects.Particles.Events#event:COMPLETE](/api/event/gameobjects-particles-events#complete)


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2806](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2806)  
引入版本：3.0.0


---

### removeDeathZone {#removeDeathZone}

#### \<instance> removeDeathZone(zone) {#instance-removedeathzonezone}


**说明:**

从此 Emitter 中删除指定的粒子死亡区 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| zone | [Phaser.GameObjects.Particles.Zones.DeathZone](/api/class/gameobjects-particles-zones-deathzone) | 否 | 死亡区应该从埃米特中移除 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1807](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1807)  
引入版本：3.60.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

当游戏对象从场景中移除时被调用。 取消对场景更新列表中此发送器的注册, 使其不再收到 `preUpdate` 的呼叫 。


**Overrides:** Phaser.GameObjects.GameObject#removedFromScene


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L960](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L960)  
引入版本：3.60.0


---

### removeEmitZone {#removeEmitZone}

#### \<instance> removeEmitZone(zone) {#instance-removeemitzonezone}


**说明:**

从此 Emitter 中删除指定的粒子排放区。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| zone | [Phaser.GameObjects.Particles.Zones.EdgeZone](/api/class/gameobjects-particles-zones-edgezone) \| [Phaser.GameObjects.Particles.Zones.RandomZone](/api/class/gameobjects-particles-zones-randomzone) | 否 | 排放区应该从这个埃米特中清除 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1915](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1915)  
引入版本：3.60.0


---

### removeParticleProcessor {#removeParticleProcessor}

#### \<instance> removeParticleProcessor(processor) {#instance-removeparticleprocessorprocessor}


**说明:**

从此 Emitter 中删除一个粒子处理器。

处理器必须属于这个 Emitter 才能删除 。

它在移除时未被销毁, 允许您将其移动到另一个 Emitter 管理器, 因此, 如果您不再需要它, 您应该直接调用它的 `destroy` 方法 。

**Tags:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| processor | T | 否 | 要从 Emitter 管理器中移除的粒子处理器 。 |


**返回值:** T - 被移除的粒子处理器, 如果找不到, 则无效 。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2101)  
引入版本：3.60.0


---

### reserve {#reserve}

#### \<instance> reserve(count) {#instance-reservecount}


**说明:**

创建不活动粒子并将其添加到此发射器的池中 。

如果设定了 `ParticleEmitter.maxParticles`, 它会限制传递到这个方法的值, 以确保它不会超过它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| count | number | 否 | 创建的粒子数 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2157](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2157)  
引入版本：3.0.0


---

### resetCounters {#resetCounters}

#### \<instance> resetCounters(frequency, on) {#instance-resetcountersfrequency-on}


**说明:**

重新安装内部的反追踪器 。

你不需要直接打电话

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frequency | number | 否 | 频率计数器. |
| on | boolean | 否 | 设全旗. |


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1189](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1189)  
引入版本：3.60.0


---

### resume {#resume}

#### \<instance> resume() {#instance-resume}


**说明:**

发射机的[Activates](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleemitter.md#active)。


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2482](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2482)  
引入版本：3.0.0


---

### setAnim {#setAnim}

#### \<instance> setAnim(anims, [pickRandom], [quantity]) {#instance-setanimanims-pickrandom-quantity}


**说明:**

设置分配向发射粒子的动画的模式。 `anims` 配置可以是 :

动画:"红色"动画:["红色","绿色","蓝色","平克","白色"]动画: {动画:["红色","绿色","蓝色","平克","白色"],[循环:布尔],[数量:英寸]]

在创建任何粒子之前至少调用一次这种方法,或在创建 Emitter 时将 `anim` 设置在 Patiter 的配置中.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| anims | string \| Array.\<string> | [Phaser.Types.GameObjects.Particles.ParticleEmitterAnimConfig](/api/typedef/types-gameobjects-particles#particleemitteranimconfig) | 否 |  | 一个或多个动画,或配置对象. |
| pickRandom | boolean | 是 | true | 动画是否应该从 `anims` 随机指定。 如果给出了配置对象, 此参数会被忽略 。 |
| quantity | number | 是 | 1 | 将接收每部动画的连续粒子数。 如果给出了配置对象, 此参数会被忽略 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1409](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1409)  
引入版本：3.60.0


---

### setConfig {#setConfig}

#### \<instance> setConfig(config) {#instance-setconfigconfig}


**说明:**

使用一个 Emitter 配置文件并重置此 Emitter, 使用配置中定义的任何属性再设置它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](/api/typedef/types-gameobjects-particles#particleemitterconfig) | 否 | 此发射器的设置 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L972](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L972)  
引入版本：3.60.0


---

### setEmitterAngle {#setEmitterAngle}

#### \<instance> setEmitterAngle(value) {#instance-setemitteranglevalue}


**说明:**

设定 [Phaser.GameObjects.Particles.ParticleEmitter#radial](/api/class/gameobjects-particles-particleemitter#radial) 粒子流的角 。

值用Phaser的右手坐标系统以度表示.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 否 | 发射粒子初始速度的角度, 以度计。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1662](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1662)  
引入版本：3.0.0


---

### setEmitterFrame {#setEmitterFrame}

#### \<instance> setEmitterFrame(frames, [pickRandom], [quantity]) {#instance-setemitterframeframes-pickrandom-quantity}


**说明:**

设置分配向排放的粒子的纹理框架的模式。 `frames` 配置可以是 :

帧: 0 帧:"红色" 帧: [0, 1, 2, 3] 帧: ["红色", "绿色", "蓝色", "平克", "白色" ] 帧: {帧: ["红色', "绿色","蓝色", "平卡", "白色"], [循环: 布尔], [数量: int] ]

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| frames | array \| string | number | [Phaser.Types.GameObjects.Particles.ParticleEmitterFrameConfig](/api/typedef/types-gameobjects-particles#particleemitterframeconfig) | 否 |  | 一个或多个纹理框架,或配置对象. |
| pickRandom | boolean | 是 | true | 是否从 `frames` 随机指定帧 。 |
| quantity | number | 是 | 1 | 接收每个框架的连续粒子数 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1301](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1301)  
引入版本：3.0.0


---

### setEmitZone {#setEmitZone}

#### \<instance> setEmitZone(zone) {#instance-setemitzonezone}


**说明:**

更改当前活动的排放区。 区域应该已经通过排放者配置或 `addEmitZone` 方法添加到此排放区中 。

调用这种方法时, 要么通过数字区指数值, 要么通过区实例本身 。

在 v3.60 之前, Emitter 只能有一个单一的 Emit 区域, 这种方法就是您设置它的方法。 从 3. 60 开始, 它现在在所有可用的活动区域之间履行不同的功能和互换 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| zone | number \| [Phaser.GameObjects.Particles.Zones.EdgeZone](/api/class/gameobjects-particles-zones-edgezone) | [Phaser.GameObjects.Particles.Zones.RandomZone](/api/class/gameobjects-particles-zones-randomzone) | 否 | 解放区将设定为活动区. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2030](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2030)  
引入版本：3.0.0


---

### setFrequency {#setFrequency}

#### \<instance> setFrequency(frequency, [quantity]) {#instance-setfrequencyfrequency-quantity}


**说明:**

设置发射机的[Phaser.GameObjects.Particles.ParticleEmitter#frequency](/api/class/gameobjects-particles-particleemitter#frequency)和[Phaser.GameObjects.Particles.ParticleEmitter#quantity](/api/class/gameobjects-particles-particleemitter#quantity).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frequency | number | 否 | 每个流周期的时间间隔(QQ 0), 以毫秒计;或 -1 使发射器处于爆炸状态. |
| quantity | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 在每个流周期或爆炸时释放的粒子数量. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1715](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1715)  
引入版本：3.0.0


---

### setParticleAlpha {#setParticleAlpha}

#### \<instance> setParticleAlpha(value) {#instance-setparticlealphavalue}


**说明:**

设置所排放粒子的不透明(α) 。

也可以通过`setAlpha`来设置整个发射器的α.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 否 | 0(透明)到1(opaque)之间的值。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1623](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1623)  
引入版本：3.60.0


---

### setParticleGravity {#setParticleGravity}

#### \<instance> setParticleGravity(x, y) {#instance-setparticlegravityx-y}


**说明:**

设定对发射粒子的重力。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 由重力作用, 以像素每秒平方位进行水平加速度。 设定为零, 不重力 。 |
| y | number | 否 | 由重力作用的垂直加速度, 以像素每秒平方位表示。 设置为零, 不重力 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1604](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1604)  
引入版本：3.60.0


---

### setParticleLifespan {#setParticleLifespan}

#### \<instance> setParticleLifespan(value) {#instance-setparticlelifespanvalue}


**说明:**

设定新排放粒子的寿命, 以毫秒计。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 否 | 粒子的寿命,以毫秒计。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1681](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1681)  
引入版本：3.60.0


---

### setParticleScale {#setParticleScale}

#### \<instance> setParticleScale([x], [y]) {#instance-setparticlescalex-y}


**说明:**

设置所排放粒子的垂直和水平尺度。

也可以通过`setScale`设定整个发射器的尺度.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 1 | 发射粒子的横向尺度。 |
| y | number | 是 | "x" | 发射粒子的垂直比例。 如果不设定, 则会使用 `x` 值 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1580](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1580)  
引入版本：3.60.0


---

### setParticleSpeed {#setParticleSpeed}

#### \<instance> setParticleSpeed(x, [y]) {#instance-setparticlespeedx-y}


**说明:**

设定发射粒子的初始射线速度。

将发射器改为射线模式。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 发射粒子的横向速度 。 |
| y | number | 是 | "x" | 发射粒子的垂直速度。 如果不设定, 则会使用 `x` 值 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1546](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1546)  
引入版本：3.60.0


---

### setParticleTint {#setParticleTint}

#### \<instance> setParticleTint(value) {#instance-setparticletintvalue}


**说明:**

设置所排放粒子的颜色。

这是WebGL的唯一功能。

**Tags:**

 - webglOnly

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 否 | 值在 0 至 0xffffff 之间 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1642](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1642)  
引入版本：3.60.0


---

### setQuantity {#setQuantity}

#### \<instance> setQuantity(quantity) {#instance-setquantityquantity}


**说明:**

设定每个流周期或爆炸时释放的粒子数量。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| quantity | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 否 | 在每个流周期或爆炸时释放的粒子数量. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1698](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1698)  
引入版本：3.0.0


---

### setRadial {#setRadial}

#### \<instance> setRadial([value]) {#instance-setradialvalue}


**说明:**

打开或关闭[Phaser.GameObjects.Particles.ParticleEmitter#radial](/api/class/gameobjects-particles-particleemitter#radial)粒子运动.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 辐射模式(真)或点模式(假). |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1476](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1476)  
引入版本：3.0.0


---

### setSortCallback {#setSortCallback}

#### \<instance> setSortCallback([callback]) {#instance-setsortcallbackcallback}


**说明:**

设置调用, 用于在渲染每个框架之前对粒子进行排序 。

这使得您可以在回调中定义自己的逻辑和行为.

回调会被发送两个参数: 比较两个粒子,并必须遵循`compareFn`在`Array.sort`中的标准:

[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#description)

调用此方法没有参数可以重设排序回调 。

设置您的回调将覆盖此 Emitter 的 `particleBringToTop` 和 `sortProperty` 设置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleSortCallback](/api/typedef/types-gameobjects-particles#particlesortcallback) | 是 | 将粒子排序后调用回调。 留未定义以重设为默认值 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2530](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2530)  
引入版本：3.60.0


---

### setSortProperty {#setSortProperty}

#### \<instance> setSortProperty([property], [ascending]) {#instance-setsortpropertyproperty-ascending}


**说明:**

设定在渲染前对活动粒子进行排序的属性 。

它允许你控制粒子的渲染顺序.

这可以是任何有效的财产 `Particle` 类,例如 `y`, `alpha` 或 或 时 间 `lifeT`.

将“ 活性” 粒子阵列排序到每个游戏框。 设置排序属性将覆盖 `particleBringToTop` 设置 。

如果您想使用自己的排序功能,请参见 `setSortCallback` 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| property | string | 是 |  | 需要整理的`Particle`类财产 |
| ascending | boolean | 是 | true | 粒子应依上升或下降顺序排序吗? |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2497](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2497)  
引入版本：3.60.0


---

### start {#start}

#### \<instance> start([advance], [duration]) {#instance-startadvance-duration}


**说明:**

启用放电,将[Phaser.GameObjects.Particles.ParticleEmitter#emitting](/api/class/gameobjects-particles-particleemitter#emitting)设置为`true`,并重置流量计数器.

如果这种发射器处于流态(频率为QQ0;默认),则粒子流将开始(或重新启动).

如果这个发射器处于爆炸模式(频率= -1),则不会发生任何情况。使用[Phaser.GameObjects.Particles.ParticleEmitter#explode](/api/class/gameobjects-particles-particleemitter#explode)或[Phaser.GameObjects.Particles.ParticleEmitter#flow](/api/class/gameobjects-particles-particleemitter#flow)来代替。

使用这种方法将释放 `START`事件。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| advance | number | 是 | 0 | 通过发射器及时推进这个数 ms 。 |
| duration | number | 是 | 0 | 将此发射器限制为只为给定的 ms 数发射粒子。 设置此参数将覆盖 Emitter 配置对象中已经设定的任何持续时间 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


**Fires:** [Phaser.GameObjects.Particles.Events#event:START](/api/event/gameobjects-particles-events#start)


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2387](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2387)  
引入版本：3.0.0


---

### startFollow {#startFollow}

#### \<instance> startFollow(target, [offsetX], [offsetY], [trackVisible]) {#instance-startfollowtarget-offsetx-offsety-trackvisible}


**说明:**

不断移动粒子源以跟随游戏对象的位置.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 |  | 接下来的目标 。 |
| offsetX | number | 是 | 0 | 水平偏移来自 Game Object 的粒子源 。 |
| offsetY | number | 是 | 0 | 垂直抵消来自 Game Object 的粒子源. |
| trackVisible | boolean | 是 | false | 发射器的可见状态是否会跟踪目标可见状态. |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1214](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1214)  
引入版本：3.0.0


---

### stop {#stop}

#### \<instance> stop([kill]) {#instance-stopkill}


**说明:**

将 [off](/api/class/gameobjects-particles-particleemitter#emitting) 转换为发射器,并阻止其再排放粒子。目前,活粒子将一直活动到它们自然失效,除非您将 `kill` 参数设置为 `true` 。

调用此方法将释放 `STOP` 事件。 当最后粒子过期时, `COMPLETE` 事件将释放 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| kill | boolean | 是 | false | 立即杀死一切粒子,或使粒子在寿命到期后死亡。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


**Fires:** [Phaser.GameObjects.Particles.Events#event:STOP](/api/event/gameobjects-particles-events#stop)


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L2432](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L2432)  
引入版本：3.11.0


---

### stopFollow {#stopFollow}

#### \<instance> stopFollow() {#instance-stopfollow}


**说明:**

停止跟踪游戏对象。


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1240](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1240)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

创建适合 JSON 序列化的此发射器描述 。


**Overrides:** Phaser.GameObjects.GameObject#toJSON


**返回值:** [Phaser.Types.GameObjects.JSONGameObject](/api/typedef/types-gameobjects#jsongameobject) - 游戏对象的JSON代表.


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1138](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1138)  
引入版本：3.0.0


---

### updateConfig {#updateConfig}

#### \<instance> updateConfig(config) {#instance-updateconfigconfig}


**说明:**

使用已有的 Emitter 配置文件并更新此 Emitter。 现有属性在添加新属性时被覆盖。 然后将更新的配置传递到 `setConfig` 方法, 以更新的配置重置 Emitter 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](/api/typedef/types-gameobjects-particles#particleemitterconfig) | 否 | 此发射器的设置 。 |


**返回值:** [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) - 这个粒子埃米特。


> 源码：[src/gameobjects/particles/ParticleEmitter.js#L1108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleEmitter.js#L1108)  
引入版本：3.85.0


---

---
