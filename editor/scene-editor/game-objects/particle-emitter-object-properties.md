# 粒子发射器属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/particle-emitter-object-properties)

Ptrict Emitter 有大量属性。 您可以编辑检查器视图中的属性。 属性被分成多个部分 。


## 预览属性 {#preview-properties}

预览属性不是粒子 Emitter 配置的一部分。 它们只是用于场景编辑器显示场景编辑器中的发送器。 预览属性是 :

* **预览活动**: 启用/ 失效发射器预览的旗。 它仍然可见, 但粒子没有更新 。
* **预览预览预览**: 在启动发射器之前, 它会以给定的毫秒数推进粒子的动画。 默认情况下, 它会在1秒内推进动画。 如果您从一开始就想看到动画, 您可以将此参数设置为 0 和 [refresh the scene](/editor/scene-editor/game-objects/particle-emitter-object#play-and-refresh-the-scene) 。

![Preview properties](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-props-preview-20240611.webp)


## 配置属性 {#configuration-properties}

在继续剩余属性之前,我们应该解释您可以设置到某种发射器属性的不同值.

粒子 Emitters 是通过配置对象创建的。此对象的属性可以用多种格式指定,使您拥有超过它们返回的值的足够范围,从而导致复杂的视觉效果。 

在编辑器中,您可以选择属性的格式,接下来它会显示与该配置相关的不同参数.

以下为您可以给予属性的不同配置值形式。


### 空的 。 {#empty}

默认情况下,该属性没有值,因此编辑器没有将其包含在配置对象中.

![The None format of a property](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-prop-value-20240611.webp)


### 明确价值 {#an-explicit-value}

```js
x: 400
```

![The Value format](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-prop-value-20240611.webp)

当粒子产卵时,x值永远是400.


### 随机值 : {#a-random-value}

```js
x: [ 100, 200, 300, 400 ]
```

![The Random type](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-prop-random-20240611.webp)

x 值将是给定阵列中随机选择的4个元素之一。

注意, 您必须在编辑器的 UI 中将数组值用逗号分隔出来 。


### 开始/结束配置 : {#a-startend-configuration}

这使得您可以控制在粒子寿命过程中给定的起始参数和结束参数之间的值变化:

```js
scale: { start: 0, end: 1 }
```

当粒子尺度在寿命期内被排放并易于1的尺度时, 粒子尺度将从 0 开始。 您也可以指定用于此变化的易度函数( 默认为 Linear ):

```js
scale: { start: 0, end: 1, ease: "Bounce.easeOut" }
```

起始和结尾配置可以有一个可选的 ``random`` 参数。这迫使它从两个值中随机选择一个值,并将其作为起始值,然后在其存在期间放松到“结束”参数。

```js
scale: { start: 4, end: 0.5, random: true }
```

粒子将先从0.5到4的随机尺度开始,然后在整个寿命期内缩放到最终值。您可以将以上参数和易性参数结合起来,同时控制值放松。

编辑的UI里是这样看的:

![Start/end format](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-prop-start-end-20240612.webp)


### 插值配置 {#an-interpolation-configuration}

您可以提供一系列在粒子寿命期间用于插值的数值。 您也可以定义要使用的插值函数。 提供了三种: 线性( 默认值)、 贝塞尔和猫头鹰, 或者您可以提供自己的函数 。

```js
x: { values: [ 50, 500, 200, 800 ], interpolation: "catmull" }
```

粒子尺度在寿命期内通过其他点从50到800的射出时会插到800。您还可以指定一个通过值控制变化速率的易函数(默认为线性):

```js
x: { values: [ 50, 500, 200, 800 ], interpolation: "catmull", ease: "Bounce.easeOut" }
```

这就是您在编辑器中配置它的方式:

![Interpolation configuration](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-prop-interpolation-20240612.webp)

注意 ** Valees ** 参数允许用逗号来写分隔的值。


### 已步进配置 {#a-stepped-configuration}

步骤参数允许您控制从起始端到起始端范围的相继粒子的位置:

```js
x: { steps: 32, start: 0, end: 576 }
```

这里有576个范围(开始到结束),分为32个步骤。

第一个粒子会在 0 的 x 位置发射。 下一个粒子将在下一个“ 末端” 的 沿边发射, 也就是 18 个。 以下粒子将在下一个步骤发射, 也就是 36 个, 诸如此类。 因为 576 的射程已被 32 个除去, 从而产生 18 像素 。 当一个粒子达到“ 末端”值时, 下一个粒子将重新开始 。

您可以在已踩到的对象中添加可选的 Yoyo 属性 :

```js
x: { steps: 32, start: 0, end: 576, yoyo: true }
```

和已踩踏的发射器一样, 粒子会按顺序发射, 从“ 启动” 到“ 结束” 的跳跃。 通常情况下, 当一个已踩踏的发射机到达终点时, 它会转动到开始值。 然而, 如果您提供了“ yo” 参数, 那么当它到达终点时, 它将会反向向向返回到“ 启动 ” 。 取决于您需要的效果, 这样的效果通常会更好 。

![Stepped configuration](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-prop-stepped-20240612.webp)


### 分钟/ 最大配置 : {#a-minmax-configuration}

这使得您可以在分钟和最大属性之间选择随机浮点值:

```js
x: { min: 100, max: 700 }
```

x 值将是在分钟和最大值之间的随机浮点。

您可以通过设置“ int” 旗来强制它选择整数 :

```js
x: { min: 100, max: 700, int: true }
```

![Min/max configuration](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-prop-min-max-20240612.webp)


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

论点是:

- **粒子** - 提到粒子实例。
- **键** - 属性的字符串键, 即“ x” 或“ lifespan ” 。
- **计数** - 目前粒子正常寿命,0(出生)至1(死亡)。
- **价值** - 当前的属性价值,至少你应该还回去。

通过使用上述配置选项,您可以无限控制您的粒子行为。

![Custom callbacks](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-prop-custom-callbacks-20240612.webp)

## 变形属性 {#transform-properties}

我们把粒子 Emitter 属性分成若干个部分。 第一部分是变换属性。 这些属性与发射方的位置、 比例和旋转有关 。

- [x](/api/class/gameobjects-particles-particleemitter#particleX)
- [y](/api/class/gameobjects-particles-particleemitter#particleY)
- [moveToX](/api/class/gameobjects-particles-particleemitter#moveToX)
- [moveToY](/api/class/gameobjects-particles-particleemitter#moveToY)
- [scale](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleemitter.md#scale)
- [particleScaleX](/api/class/gameobjects-particles-particleemitter#particleScaleX)
- [particleScaleY](/api/class/gameobjects-particles-particleemitter#particleScaleY)
- [particleAngle](/api/class/gameobjects-particles-particleemitter#particleAngle)
- [particleRotate](/api/class/gameobjects-particles-particleemitter#particleRotate)

![transform properties](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-props-transform-20240612.webp)

## 物理属性 {#physics-properties}

本节包含粒子发射属性,专门用于物理学.

- [accelerationX](/api/class/gameobjects-particles-particleemitter#accelerationX)
- [accelerationY](/api/class/gameobjects-particles-particleemitter#accelerationY)
- [maxVelocityX](/api/class/gameobjects-particles-particleemitter#maxVelocityX)
- [maxVelocityY](/api/class/gameobjects-particles-particleemitter#maxVelocityY)
- [speed](/api/class/gameobjects-particles-particleemitter#speed)
- [speedX](/api/class/gameobjects-particles-particleemitter#speedX)
- [speedY](/api/class/gameobjects-particles-particleemitter#speedY)
- [gravityX](/api/class/gameobjects-particles-particleemitter#gravityX)
- [gravityY](/api/class/gameobjects-particles-particleemitter#gravityY)
- [radial](/api/class/gameobjects-particles-particleemitter#radial)

![particle emitter physics properties](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-physics-properties-20240612.webp)

## 时间属性 {#timing-properties}

本节包含专用于计时的粒子 Emitter 属性 。

- [delay](/api/class/gameobjects-particles-particleemitter#delay)
- [hold](/api/class/gameobjects-particles-particleemitter#hold)
- [lifespan](/api/class/gameobjects-particles-particleemitter#lifespan)
- [quantity](/api/class/gameobjects-particles-particleemitter#quantity)
- [duration](/api/class/gameobjects-particles-particleemitter#duration)
- [frequency](/api/class/gameobjects-particles-particleemitter#frequency)
- [maxAliveParticles](/api/class/gameobjects-particles-particleemitter#maxAliveParticles)
- [maxParticles](/api/class/gameobjects-particles-particleemitter#maxParticles)
- [stopAfter](/api/class/gameobjects-particles-particleemitter#stopAfter)
- [advance](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleemitter.md#advance)
- [timeScale](/api/class/gameobjects-particles-particleemitter#timeScale)

![timing properties](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-props-timing-20240612.webp)

## 颜色属性 {#color-properties}

本节包含专用于色彩的粒子 Emitter 属性 。

- [particleAlpha](/api/class/gameobjects-particles-particleemitter#particleAlpha)
- [particleTint](/api/class/gameobjects-particles-particleemitter#particleTint)
- [particleColor](/api/class/gameobjects-particles-particleemitter#particleColor)
- [colorEase](/api/class/gameobjects-particles-particleemitter#colorEase)
- [blendMode](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleemitter.md#blendmode)
- [tintFill](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleemitter.md#tintfill)

![color properties](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-props-color-20240612.webp)

## 排序属性 {#sorting-properties}

本节包含用于排序的粒子 Emitter 属性 。

- [particleBringToTop](/api/class/gameobjects-particles-particleemitter#particleBringToTop)
- [sortOrderAsc](/api/class/gameobjects-particles-particleemitter#sortOrderAsc)
- [sortProperty](/api/class/gameobjects-particles-particleemitter#sortProperty)

![sorting properties](https://cdn.phaser.io/editor-docs/phaser-editor-particle-emitter-props-sorting-20240612.webp)

## 属性之后 {#following-properties}

本节包含专用于跟踪对象的粒子发射属性。

- [follow](/api/class/gameobjects-particles-particleemitter#follow) - 在编辑器中,您可以写入对象的变量名称,以跟随或点击"浏览"按钮从场景中选择对象.
- [trackVisible](/api/class/gameobjects-particles-particleemitter#trackVisible)

![particle emitter follow properties](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-props-follow-20240612.webp)

## 动画属性 {#animations-properties}

在此部分中, 您可以选择用于发送器的图示动画 。

** 动画 ** 字段包含动画名称的阵列。 您可以点击“ 文件夹” 图标修改它们 。 

![Emitter animations properties](https://cdn.phaser.games/oss-docs/assets/c7c3c40232f78402-scene-editor-particle-emitter-animations.webp)

它打开了所有可用的图示动画的对话框。 您可以在该对话框中选择多个动画 。

![Select animations dialog](https://cdn.phaser.games/oss-docs/assets/a9c02378fd39ba50-scene-editor-particle-emitter-animations.webp)

## 纹理帧属性 {#texture-frame-properties}

本节包含专用于纹理帧的粒子 Emitter 属性.

![particle frames](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-props-frames-20240612.webp)

要添加新框架,请单击“ 添加” 按钮。 它显示一个对话框, 与同一纹理和所有其他剩余纹理的框相连接。 在此选择您要添加的框架 。

![particle emitter select frames dialog](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-select-frames-dialog-20240612.webp)

如果您选择从其他纹理中添加帧, 那么编辑器会用所选的新帧替换( 而不是附件) 当前帧。 它遵循了这个规则, 因为粒子发射器只允许从同一纹理中添加帧 。

要删除一个框架,请选择它并点击"删除"按钮.

---
