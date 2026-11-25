# AnimationState {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/animations-animationstate)

动画国产部分.

这个组件提供了将动画应用到Game Objects的功能,负责加载,排队动画进行后期的回放,动画之间的混合,并将当前动画框设置到拥有这个组件的Game Objector上.

此组件作为实例存在于任何它定义的游戏对象中,例如Sprites.

您可以通过 `anims` 属性,即 `Sprite.anims` 访问它的属性和方法.

除了播放存储在全球动画管理器中的动画外,这个组件还可以创建存储在它内部的本地动画,详见`create`方法.

在Phaser 3.50之前,这个组件只叫做`Animation`,并住在`Phaser.GameObjects.Components`命名空间中,在3.50中改名为`AnimationState`,以帮助在浏览文档时更好地识别其真实目的.

**构造函数**

`new AnimationState(parent)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| parent | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此动画组件所属的游戏对象 。 |

---


**作用域**: static

> 源码：[src/animations/AnimationState.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L14)  
引入版本：3.0.0

## 公开成员 {#public-members}

### accumulator {#accumulator}

#### accumulator: number {#accumulator-number}


**说明:**

内部时间溢出积聚器.

这张上面加了`delta`时间 作为`update`步骤的一部分.


> 源码：[src/animations/AnimationState.js#L376](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L376)  
引入版本：3.0.0


---

### animationManager {#animationManager}

#### animationManager: [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) {#animationmanager-phaseranimationsanimationmanager}


**说明:**

参考全球动画管理器.


> 源码：[src/animations/AnimationState.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L59)  
引入版本：3.0.0


---

### anims {#anims}

#### anims: Phaser.Structs.Map.\<string, [Phaser.Animations.Animation](/api/class/animations-animation)> {#anims-phaserstructsmapstring-phaseranimationsanimation}


**说明:**

动画在本地存储在这个动画组件中.

不直接修改此地图的内容,而是使用 `add`, `create` 财务报告和已审计财务报表 `remove` 使用该类的方法。


**Access:** 保护


> 源码：[src/animations/AnimationState.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L80)  
引入版本：3.50.0


---

### currentAnim {#currentAnim}

#### currentAnim: [Phaser.Animations.Animation](/api/class/animations-animation) {#currentanim-phaseranimationsanimation}


**说明:**

当前动画装入了此动画组件 。

如果还没有装入动画, 将会是 `null` 。


> 源码：[src/animations/AnimationState.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L113)  
引入版本：3.0.0


---

### currentFrame {#currentFrame}

#### currentFrame: [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) {#currentframe-phaseranimationsanimationframe}


**说明:**

此动画组件正在显示当前动画Frame 。

如果还没有装入动画, 将会是 `null` 。


> 源码：[src/animations/AnimationState.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L125)  
引入版本：3.0.0


---

### delay {#delay}

#### delay: number {#delay-number}


**说明:**

开始回放当前动画之前的延迟, 以毫秒计 。

当新动画装入此组件时设定此值, 并且应当作为只读处理, 因为一旦重播开始后更改它不会改变动画。 要更改延迟, 请在 `PlayAnimationConfig` 对象中提供新值 。

在Phaser 3.50之前,这批财产是私有的,称为`_delay`.


> 源码：[src/animations/AnimationState.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L241)  
引入版本：3.50.0


---

### delayCounter {#delayCounter}

#### delayCounter: number {#delaycounter-number}


**说明:**

计数器记录了在重播开始前, 以毫秒计的延迟时间。

此设定通过`playAfterDelay`方法,虽然如果需要,可以在运行时修改,只要动画还没有开始播放.


> 源码：[src/animations/AnimationState.js#L400](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L400)  
引入版本：3.50.0


---

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

现动画的长度,以毫秒计.

当新动画装入此组件时, 此值被设定, 并且应该作为只读处理, 因为一旦开始播放时更改它不会改变动画。 要更改持续时间, 请在 `PlayAnimationConfig`Z 对象中提供新值 。


> 源码：[src/animations/AnimationState.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L193)  
引入版本：3.0.0


---

### forward {#forward}

#### forward: boolean {#forward-boolean}


**说明:**

玩家是否在前进`true`)或倒数(`false`) ?


> 源码：[src/animations/AnimationState.js#L352](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L352)  
引入版本：3.0.0


---

### frameRate {#frameRate}

#### frameRate: number {#framerate-number}


**说明:**

播放的帧率,即当前动画的帧率,以帧每秒为单位.

当新动画装入此组件时, 此值被设定, 并且应该作为只读处理, 因为一旦重播开始, 更改它不会改变动画。 要改变帧速率, 请在 `PlayAnimationConfig`Z 对象中提供新值 。


> 源码：[src/animations/AnimationState.js#L179](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L179)  
引入版本：3.0.0


---

### hasStarted {#hasStarted}

#### hasStarted: boolean {#hasstarted-boolean}


**说明:**

目前的动画是否开始播放, 还是在等待延迟到期?


> 源码：[src/animations/AnimationState.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L103)  
引入版本：3.50.0


---

### hideOnComplete {#hideOnComplete}

#### hideOnComplete: boolean {#hideoncomplete-boolean}


**说明:**

游戏对象的`visible`属性是否应该设定为动画完成后`false`?.

此值设定为新动画装入此组件时, 但也可以在运行时修改, 假设动画仍在积极播放.


> 源码：[src/animations/AnimationState.js#L340](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L340)  
引入版本：3.50.0


---

### inReverse {#inReverse}

#### inReverse: boolean {#inreverse-boolean}


**说明:**

一个内部触发器, 告诉组件它是否应该以反向模式( “ true” ) 播放动画 。 使用这个触发器是因为 `forward` 可以通过 `yoyo` 特性更改 。

在Phaser 3.50之前,这批财产是私有的,称为`_reverse`.


> 源码：[src/animations/AnimationState.js#L362](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L362)  
引入版本：3.50.0


---

### isPaused {#isPaused}

#### isPaused: boolean {#ispaused-boolean}


**说明:**

`true`如果当前动画暂停,否则`false`.


> 源码：[src/animations/AnimationState.js#L1987](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1987)  
引入版本：3.4.0


---

### isPlaying {#isPlaying}

#### isPlaying: boolean {#isplaying-boolean}


**说明:**

动画是现在播放还是没有播放?


> 源码：[src/animations/AnimationState.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L93)  
引入版本：3.0.0


---

### msPerFrame {#msPerFrame}

#### msPerFrame: number {#msperframe-number}


**说明:**

每个帧的毫秒数,不包括动画数据中可能存在的帧特定修饰符.

当新动画装入此组件时, 此值会被计算, 并且应该作为只读处理。 更改它不会改变播放速度 。


> 源码：[src/animations/AnimationState.js#L207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L207)  
引入版本：3.0.0


---

### nextAnim {#nextAnim}

#### nextAnim: string, [Phaser.Animations.Animation](/api/class/animations-animation), [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) {#nextanim-string-phaseranimationsanimation-phasertypesanimationsplayanimationconfig}


**说明:**

当当前动画完成时,要装入此动画组件的下一个动画的密钥,实例,或配置.

如果没有动画排队的话, 将会是 `null` 。


> 源码：[src/animations/AnimationState.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L137)  
引入版本：3.16.0


---

### nextAnimsQueue {#nextAnimsQueue}

#### nextAnimsQueue: array {#nextanimsqueue-array}


**说明:**

当当前动画完成时,要装入此动画组件的动画队列.

通过 `chain` 方法填入此队列 。


> 源码：[src/animations/AnimationState.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L150)  
引入版本：3.24.0


---

### nextTick {#nextTick}

#### nextTick: number {#nexttick-number}


**说明:**

下一部动画框架将改变的时间点.

将这个值与`accumulator`作为`update`步骤的一部分进行比较.


> 源码：[src/animations/AnimationState.js#L388](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L388)  
引入版本：3.0.0


---

### parent {#parent}

#### parent: [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) {#parent-phasergameobjectsgameobject}


**说明:**

此动画组件所属的游戏对象 。

您通常可以通过 `this.anims` 属性从 Game Object 访问此组件 。


> 源码：[src/animations/AnimationState.js#L47](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L47)  
引入版本：3.0.0


---

### pendingRepeat {#pendingRepeat}

#### pendingRepeat: boolean {#pendingrepeat-boolean}


**说明:**

内旗追踪待发复发事件


> 源码：[src/animations/AnimationState.js#L426](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L426)  
引入版本：3.0.0


---

### randomFrame {#randomFrame}

#### randomFrame: boolean {#randomframe-boolean}


**说明:**

从随机帧开始播放这款动画?


> 源码：[src/animations/AnimationState.js#L231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L231)  
引入版本：3.60.0


---

### repeat {#repeat}

#### repeat: number {#repeat-number}


**说明:**

重复播放当前动画的次数.

如果-1,表示动画会永远重复.

当新动画装入此组件时, 此值会被设定, 并且应该作为只读处理, 因为一旦开始播放时更改它不会改变动画。 要改变重复次数, 请在 `PlayAnimationConfig`Z 对象中提供新值 。

在Phaser 3.50之前,这批财产是私有的,称为`_repeat`.


> 源码：[src/animations/AnimationState.js#L257](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L257)  
引入版本：3.50.0


---

### repeatCounter {#repeatCounter}

#### repeatCounter: number {#repeatcounter-number}


**说明:**

一个追踪有多少重复的计数器

当新动画装入此组件时, 此值会被设定, 但也可以在运行时修改 。


> 源码：[src/animations/AnimationState.js#L413](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L413)  
引入版本：3.0.0


---

### repeatDelay {#repeatDelay}

#### repeatDelay: number {#repeatdelay-number}


**说明:**

在当前动画的重复播放开始前等待的毫秒数.

当新动画装入此组件时, 此值会被设定, 但也可以在运行时修改 。

您可以在 `PlayAnimationConfig` 对象中提供新值来改变重复延迟 。

在Phaser 3.50之前,这批财产是私有的,称为`_repeatDelay`.


> 源码：[src/animations/AnimationState.js#L275](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L275)  
引入版本：3.0.0


---

### showBeforeDelay {#showBeforeDelay}

#### showBeforeDelay: boolean {#showbeforedelay-boolean}


**说明:**

如果动画有延迟设置, 在播放开始前, 当第一个帧设定在 Sprite 上时, 将控制此设定。 如果此属性是“ 假的 ” , 则此帧仅在延迟到期后设定 。 这是默认的行为 。

如果此属性是“ true ” , 那么此动画的第一个帧会立即设定, 然后当延迟到期时, 开始播放 。


> 源码：[src/animations/AnimationState.js#L311](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L311)  
引入版本：3.60.0


---

### showOnStart {#showOnStart}

#### showOnStart: boolean {#showonstart-boolean}


**说明:**

当动画开始播放时,游戏对象的`visible`属性是否应该设定为`true`?

这将发生_after_任何可能设定的延迟 。

此值设定为新动画装入此组件时, 但也可以在运行时修改, 假设动画目前被延迟 。


> 源码：[src/animations/AnimationState.js#L326](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L326)  
引入版本：3.50.0


---

### skipMissedFrames {#skipMissedFrames}

#### skipMissedFrames: boolean {#skipmissedframes-boolean}


**说明:**

如果时间滞后, 跳过框架, 还是总是向前?


> 源码：[src/animations/AnimationState.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L221)  
引入版本：3.0.0


---

### textureManager {#textureManager}

#### textureManager: [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) {#texturemanager-phasertexturestexturemanager}


**说明:**

纹理管理器的参考文献.


**Access:** 保护


> 源码：[src/animations/AnimationState.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L70)  
引入版本：3.50.0


---

### timeScale {#timeScale}

#### timeScale: number {#timescale-number}


**说明:**

时间尺度因子.

您可以调整此值, 以修改当前播放的动画的时间跨度。 例如, 设定为 2 会让动画播放速度快一倍 。 或者设定为 0. 5 将会让动画慢下来 。

您可以在运行时更改此值, 或者通过 `PlayAnimationConfig` 设置它 。

在Phaser 3.50之前,这批财产是私有的,称为`_timeScale`.


> 源码：[src/animations/AnimationState.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L161)  
引入版本：3.50.0


---

### yoyo {#yoyo}

#### yoyo: boolean {#yoyo-boolean}


**说明:**

是否应该使用当前动画 Yoyo ? 一种 Yoyos 将反向播放的动画, 从尾到尾, 然后再重复或完成。 不使用 Yoyo 的动画将只从尾到尾播放 。

当新动画装入此组件时, 此值会被设定, 但也可以在运行时修改 。

您可以在 `PlayAnimationConfig` 对象中提供新值来更改 Yyo。

在Phaser 3.50之前,这批财产是私有的,称为`_yoyo`.


> 源码：[src/animations/AnimationState.js#L292](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L292)  
引入版本：3.50.0


---

## 公开方法 {#public-methods}

### chain {#chain}

#### \<instance> chain([key]) {#instance-chainkey}


**说明:**

设定动画,或一系列动画,在目前动画完成或停止后,未来将播放.

当前动画必须输入一个"完成"状态才能实现,即完成它的所有重复,延迟等,或者有一种`stop`方法被调用.

永久重复的动画集,除非停止,否则永远不会进入一个完成状态.

您可以在任何时间,包括当前动画开始播放之前,期间,或当它结束(通过其`animationcomplete`事件)时,对新动画进行链条.

链条动画是游戏对象特有,意为不同的游戏对象可以有不同的链条动画,而不会影响他们正在玩的全球动画.

调用此方法, 无需参数来重置所有目前串联的动画 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | Array.\<string> | Array.\<[Phaser.Animations.Animation](/api/class/animations-animation)> | Array.\<[Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig)> | 是 | 动画的弦键要播放,或动画实例,或`PlayAnimationConfig`对象,或其中的数组. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


> 源码：[src/animations/AnimationState.js#L484](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L484)  
引入版本：3.16.0


---

### complete {#complete}

#### \<instance> complete() {#instance-complete}


**说明:**

当前动画已经完成。 发送 `ANIMATION_COMPLETE` 事件 。

这种方法被动画实例所调用,通常不应直接引用.

如果没有加载动画,则不会发出事件.

如果另一部动画已经排队进行回放,则会在事件起火后开始.


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_COMPLETE](/api/event/animations-events#animation_complete)


> 源码：[src/animations/AnimationState.js#L1309](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1309)  
引入版本：3.50.0


---

### create {#create}

#### \<instance> create(config) {#instance-createconfig}


**说明:**

创建本地特指此 Sprite 的新动画 。

当一个Sprite拥有一个动画时,它被从全球动画管理器中保留出来,这意味着你可以自由地使用可能已经定义的密钥。除非您特别需要一个Sprite来拥有一个独特的动画,否则您应该倾向于使用全球动画,因为这样可以跨多个Sprite使用同一动画,保存在内存上。然而,如果这个Sprite是唯一使用这个动画的人,那么在这里创建它是明智的。

如果给定了一个无效的密钥, 此方法将返回 `false` 。

如果您通过本地已经存在的动画的密钥,该动画会被返回.

只有在密钥有效且本Sprite尚未使用时,才会创建全新的动画.

如果您希望重新使用已有的密钥,请先拨打`remove`方法,然后拨打这个方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Animations.Animation](/api/typedef/types-animations#animation) | 否 | 动画的配置设置 。 |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation), false - 创建的动画, 或者如果密钥已经使用的话, `false` 。


> 源码：[src/animations/AnimationState.js#L1699](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1699)  
引入版本：3.50.0


---

### createFromAseprite {#createFromAseprite}

#### \<instance> createFromAseprite(key, [tags]) {#instance-createfromasepritekey-tags}


**说明:**

从装入的 Aseprite JSON 文件创建一个或多个动画 。

Aseprite是一个强大的动画图案编辑器和像素艺术工具.

您可以在 [https://www.aseprite.org/](https://www.aseprite.org/) 找到更多细节

要在 Aseprite 中导出兼容的 JSON 文件, 请做以下操作 :

1. 转到“ 文件 - 导出工作表”

2. 标签上写着:

2a. 设置“ 套座类型” 为“ 套座”

2b 设置"约束"为"无".

2c. 请检查date=中的日期值 (帮助) "Morge Reverses" 复本复选框

3. 标签上:

3a. 将“ 线条” 设置为“ 可见层 ”

3b. 将“ Frames” 设定为“ 所有框架”,除非您仅希望导出一组子标签

4. 在**边界**标签上:

4a. 请检查date=中的日期值 (帮助) "Trim Sprite"和"Trim Cells"选项

4b. 确保“边境铺设”、“间隔”和“内部铺设”均大于0(1通常足够)

5. 在**产出**标签上:

5a. 检查“ 输出文件” , 给您图像一个名称, 并确保您选择“ png 文件” 作为文件类型

5b. 检查"JSON Data",并给您的Json文件一个名字

5c. JSON Data类型可以是哈什或阵列,Phaser不介意.

5d. 确保“ Tags” 在 Meta 选项中被检查

5e. 在“项目文件名” 输入框中,请确保只写“ {frame} ” , 仅此而已 。

6. 单击导出

测试时采用了Aeprite 1.2.25.

这将导出一个 png 和 json 文件, 您可以使用 Aseprite 装入器装入, 即 :

```javascript
function preload ()
{
    this.load.path = 'assets/animations/aseprite/';
    this.load.aseprite('paladin', 'paladin.png', 'paladin.json');
}
```

装入后,您可以在 Sprite 上使用“ atlas” 键调用这种方法 :

```javascript
const sprite = this.add.sprite(400, 300);

sprite.anims.createFromAseprite('paladin');
```

JSON 中定义的任何动画现在都可以在此Sprite上使用,您通过他们的 Tag 名称播放它们。 例如, 如果您在 Aseprite 时间表中有名为 “ 战争哭” 的动画, 您可以使用该 Tag 名称在 Sprite 上播放 :

```javascript
const sprite = this.add.sprite(400, 300);

sprite.anims.createFromAseprite('paladin');

sprite.play('War Cry');
```

在调用此方法时, 您可以选择提供一系列标记名称, 只有这些动画才会被创建 。 例如 :

```javascript
sprite.anims.createFromAseprite('paladin', [ 'step', 'War Cry', 'Magnum Break' ]);
```

这将只创建定义的 3 个动画。 请注意, 标记名称是区分大小写 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 装入的 Aseprite 地图集的密钥。 它一定是在调用此方法之前装入的 。 |
| tags | Array.\<string> | 是 | 标记名称的数组。 如果提供了, 将只创建此数组中的动画 。 |


**返回值:** Array.\<[Phaser.Animations.Animation](/api/class/animations-animation)> - 成功创建的动画实例数组 。


> 源码：[src/animations/AnimationState.js#L1753](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1753)  
引入版本：3.60.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个动画组件 。

未注册事件听众并清理其参考文献.


> 源码：[src/animations/AnimationState.js#L1961](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1961)  
引入版本：3.0.0


---

### exists {#exists}

#### \<instance> exists(key) {#instance-existskey}


**说明:**

检查是否已经将给定的密钥在存储在这个 Sprite 上的动画中局部使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 动画的钥匙来检查. |


**返回值:** boolean - `true` 如果动画存在本地,或 `false` 如果有键,或者没有本地动画。


> 源码：[src/animations/AnimationState.js#L1684](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1684)  
引入版本：3.50.0


---

### generateFrameNames {#generateFrameNames}

#### \<instance> generateFrameNames(key, [config]) {#instance-generateframenameskey-config}


**说明:**

从纹理密钥和配置对象生成 [Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe) 对象的阵列 。

生成基于字符串的框架名称的对象,由给定的 [Phaser.Types.Animations.GenerateFrameNames](/api/typedef/types-animations#generateframenames) 配置.

这是一个帮助方法,旨在方便您从纹理图集中提取所有框架名称。如果您正在使用一个图示表,请参见 `generateFrameNumbers` 方法。

Example:

如果你有一个纹理图集,叫做`gems`, 里面有6个框架,叫做`ruby_0001`,`ruby_0002`等等, 你可以使用:`this.anims.generateFrameNames('gems', { prefix: 'ruby_', end: 6, zeroPad: 4 })`来称呼这个方法。

`end`值告诉它寻找6帧,增量编号,全部从前缀`ruby_`开始. `zeroPad`值告诉它有多少零点会铺设数字。要用这种方法创建动画,你可以:

```javascript
this.anims.create({
  key: 'ruby',
  repeat: -1,
  frames: this.anims.generateFrameNames('gems', {
    prefix: 'ruby_',
    end: 6,
    zeroPad: 4
  })
});
```

详情请参见动画示例.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 包含动画帧的纹理的密钥. |
| config | [Phaser.Types.Animations.GenerateFrameNames](/api/typedef/types-animations#generateframenames) | 是 | 动画框架名称的配置对象. |


**返回值:** Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> - [Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)物体的阵列。


> 源码：[src/animations/AnimationState.js#L1840](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1840)  
引入版本：3.50.0


---

### generateFrameNumbers {#generateFrameNumbers}

#### \<instance> generateFrameNumbers(key, [config]) {#instance-generateframenumberskey-config}


**说明:**

从纹理密钥和配置对象生成 [Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe) 对象的阵列 。

生成带有编号框架名称的物体, 由给定的 [Phaser.Types.Animations.GenerateFrameNumbers](/api/typedef/types-animations#generateframenumbers) 配置 。

如果你正在用纹理图集工作,请参见`generateFrameNames`方法.

这是一种帮助方法,旨在方便您从图示工作表提取帧.

Example:

如果你装上了一个名为`explosion`的图示表,其中包含12帧,那么你可以使用:`this.anims.generateFrameNumbers('explosion', { start: 0, end: 11 })`来称呼这种方法.

`end`值告诉它12帧后停止。要使用这种方法创建动画,你可以:

```javascript
this.anims.create({
  key: 'boom',
  frames: this.anims.generateFrameNumbers('explosion', {
    start: 0,
    end: 11
  })
});
```

注意`start`是可选的,如果动画从帧0开始,则不需要包含.

要指定反向动画, 请将 `start` 和 `end` 值互换 。

如果帧不是顺序的,您可以通过一个帧数组,例如:

`this.anims.generateFrameNumbers('explosion', { frames: [ 0, 1, 2, 1, 2, 3, 4, 0, 1, 2 ] })`

请参看动画示例和 `GenerateFrameNumbers` 配置文件,以了解更多细节。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 包含动画帧的纹理的密钥. |
| config | [Phaser.Types.Animations.GenerateFrameNumbers](/api/typedef/types-animations#generateframenumbers) | 是 | 动画框架的配置对象 。 |


**返回值:** Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> - [Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)物体的阵列。


> 源码：[src/animations/AnimationState.js#L1883](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1883)  
引入版本：3.50.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

获取本地在此 Sprite 上创建的动画实例 。

详见`create`方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 动画的钥匙要取回. |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 动画,或如果密钥无效,则使用 `null` 。


> 源码：[src/animations/AnimationState.js#L1667](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1667)  
引入版本：3.50.0


---

### getFrameName {#getFrameName}

#### \<instance> getFrameName() {#instance-getframename}


**说明:**

返回当前由此组件显示的动画框架的密钥 。


**返回值:** string - 动画框架的密钥当前由此组件显示, 或者如果没有加载动画, 则使用空字符串 。


> 源码：[src/animations/AnimationState.js#L554](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L554)  
引入版本：3.50.0


---

### getName {#getName}

#### \<instance> getName() {#instance-getname}


**说明:**

返回当前装入此组件的动画密钥 。

在Phaser 3.50之前,这种方法被称为`getCurrentKey`.


**返回值:** string - 动画当前装入此组件的密钥, 或者如果没有装入则装入空字符串 。


> 源码：[src/animations/AnimationState.js#L539](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L539)  
引入版本：3.50.0


---

### getProgress {#getProgress}

#### \<instance> getProgress() {#instance-getprogress}


**说明:**

返回0到1之间的值,表示此动画的经过有多远,忽略重复和yoyos.

值以当前帧为主,动画中这个距离有多远,不以动画的持续时间为主.


**返回值:** number - 画面中当前动画的进展,在0到1之间.


> 源码：[src/animations/AnimationState.js#L1150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1150)  
引入版本：3.4.0


---

### getTotalFrames {#getTotalFrames}

#### \<instance> getTotalFrames() {#instance-gettotalframes}


**说明:**

返回此动画中帧的总数, 如果没有装入动画, 则返回零 。


**返回值:** number - 当前动画中帧的总数, 如果没有加载动画则为零 。


> 源码：[src/animations/AnimationState.js#L1473](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1473)  
引入版本：3.4.0


---

### globalRemove {#globalRemove}

#### \<instance> globalRemove([key], [animation]) {#instance-globalremovekey-animation}


**说明:**

处理动画管理器中动画的删除事宜.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 是 | 被移除动画的密钥. |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 是 | 被移除的动画. |


> 源码：[src/animations/AnimationState.js#L1232](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1232)  
引入版本：3.50.0


---

### load {#load}

#### \<instance> load(key) {#instance-loadkey}


**说明:**

用于将动画加载到此组件的内部方法.


**Access:** 保护

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 | 动画中基于字符串的键来播放,或者一个`PlayAnimationConfig`对象. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


> 源码：[src/animations/AnimationState.js#L567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L567)  
引入版本：3.0.0


---

### nextFrame {#nextFrame}

#### \<instance> nextFrame() {#instance-nextframe}


**说明:**

将动画推进到下一个帧, 不论时间或动画状态如何。 如果动画被设定重复, 或者 Yoyo, 则仍然生效 。

调用此选项不会改变动画的方向。 即如果它目前是反向播放, 调用此方法不会改变方向为向前 。


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 此动画组件所属的游戏对象 。


> 源码：[src/animations/AnimationState.js#L1623](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1623)  
引入版本：3.16.0


---

### pause {#pause}

#### \<instance> pause([atFrame]) {#instance-pauseatframe}


**说明:**

暂停当前动画, 将 `isPlaying` 属性设置为 `false` 。 您可以在特定框架上可选择地暂停它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| atFrame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 是 | 预留动画后设定的可选框 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


> 源码：[src/animations/AnimationState.js#L644](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L644)  
引入版本：3.0.0


---

### play {#play}

#### \<instance> play(key, [ignoreIfPlaying]) {#instance-playkey-ignoreifplaying}


**说明:**

开始在此Sprite上播放给定的动画.

Phaser中的动画可以属于全球动画管理器,也可以具体属于这个Sprite.

全球动画的好处是,多部Sprite可以全部播放相同的动画,而无需重复数据。你可以一次一次地在任意的Sprite上播放。

以下代码显示如何创建全球重复动画。 动画将从装入密钥“ muybridge” 的图示工作表中的所有框架创建 :

```javascript
var config = {
    key: 'run',
    frames: 'muybridge',
    frameRate: 15,
    repeat: -1
};

//  This code should be run from within a Scene:
this.anims.create(config);
```

然而,如果您想要创建一个这个Sprite独有的动画, 而这个Sprite单独使用, 您可以调用 `Animation.create` 方法。 它接受与创建全局动画时完全相同的参数, 然而所产生的数据会保存在这个Sprite 中 。

在全球或本地创作的动画中,你可以在这个Sprite上播放:

```javascript
this.add.sprite(x, y).play('run');
```

或者,如果您想要以不同的帧率运行,例如,您可以通过一个配置对象:

```javascript
this.add.sprite(x, y).play({ key: 'run', frameRate: 24 });
```

当在 Sprite 上播放动画时, 它会首先检查它能否在 Sprite 内找到匹配的密钥。 如果可以, 它会播放本地动画。 如果不行, 它会搜索全球动画管理器, 并在那里查找 。

如果您需要Sprite来同时播放本地和全局动画,请确保它们没有相互冲突的密钥.

关于此方面的更多细节,请参看`PlayAnimationConfig`配置对象的文档.

另外,关于动画创作的进一步详情,请参见动画管理器中的文档.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 |  | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| ignoreIfPlaying | boolean | 是 | false | 如果这款动画已经播放了,那么就忽略这个电话. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/animations/AnimationState.js#L799](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L799)  
引入版本：3.0.0


---

### playAfterDelay {#playAfterDelay}

#### \<instance> playAfterDelay(key, delay) {#instance-playafterdelaykey-delay}


**说明:**

等待指定的延迟,以毫秒计,然后开始播放指定的动画.

如果动画_ also_ 在其配置中有一个延迟值设置,则会被**加到此处给出的延迟中** 。

如果动画已经运行,并且给这个方法提供了新的动画,它将会等待给定的延迟,然后开始新的动画.

如果目前没有运行动画,则在延迟后开始给定动画.

在Phaser 3.50之前,这种方法被称为"delayedPlay",参数为反序.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| delay | number | 否 | 延迟,以毫秒计,等待动画开始播放. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/animations/AnimationState.js#L699](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L699)  
引入版本：3.50.0


---

### playAfterRepeat {#playAfterRepeat}

#### \<instance> playAfterRepeat(key, [repeatCount]) {#instance-playafterrepeatkey-repeatcount}


**说明:**

等待当前动画完成`repeatCount`的重复周期数,然后开始回放给定动画.

你可以用这个来确保两组动画之间没有严酷的跳动,即通过让它们顺利地融合到彼此中来从闲动画到行走动画.

如果目前没有动画运行,则给定的动画会立即开始.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 |  | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| repeatCount | number | 是 | 1 | 动画在下一部开始前要重复多少次?. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/animations/AnimationState.js#L748](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L748)  
引入版本：3.50.0


---

### playReverse {#playReverse}

#### \<instance> playReverse(key, [ignoreIfPlaying]) {#instance-playreversekey-ignoreifplaying}


**说明:**

开始在这张Sprite上播放给定的动画,反向播放.

Phaser中的动画可以属于全球动画管理器,也可以具体属于这个Sprite.

全球动画的好处是,多部Sprite可以全部播放相同的动画,而无需重复数据。你可以一次一次地在任意的Sprite上播放。

以下代码显示如何创建全球重复动画。 动画将从装入密钥“ muybridge” 的图示工作表中的所有框架创建 :

```javascript
var config = {
    key: 'run',
    frames: 'muybridge',
    frameRate: 15,
    repeat: -1
};

//  This code should be run from within a Scene:
this.anims.create(config);
```

然而,如果您想要创建一个这个Sprite独有的动画, 而这个Sprite单独使用, 您可以调用 `Animation.create` 方法。 它接受与创建全局动画时完全相同的参数, 然而所产生的数据会保存在这个Sprite 中 。

在全球或本地创作的动画中,你可以在这个Sprite上播放:

```javascript
this.add.sprite(x, y).playReverse('run');
```

或者,如果您想要以不同的帧率运行,例如,您可以通过一个配置对象:

```javascript
this.add.sprite(x, y).playReverse({ key: 'run', frameRate: 24 });
```

当在 Sprite 上播放动画时, 它会首先检查它能否在 Sprite 内找到匹配的密钥。 如果可以, 它会播放本地动画。 如果不行, 它会搜索全球动画管理器, 并在那里查找 。

如果您需要Sprite来同时播放本地和全局动画,请确保它们没有相互冲突的密钥.

关于此方面的更多细节,请参看`PlayAnimationConfig`配置对象的文档.

另外,关于动画创作的进一步详情,请参见动画管理器中的文档.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 |  | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| ignoreIfPlaying | boolean | 是 | false | 如果动画已经播放了,那么就忽略这个电话. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/animations/AnimationState.js#L894](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L894)  
引入版本：3.12.0


---

### previousFrame {#previousFrame}

#### \<instance> previousFrame() {#instance-previousframe}


**说明:**

将动画推进到前一个帧, 不论时间或动画状态如何。 如果动画被设定重复, 或者 Yoyo, 则仍然生效 。

调用此选项不会改变动画的方向。 如果它目前是向前播放, 调用此方法不会改变方向为向后。


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 此动画组件所属的游戏对象 。


> 源码：[src/animations/AnimationState.js#L1645](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1645)  
引入版本：3.16.0


---

### remove {#remove}

#### \<instance> remove(key) {#instance-removekey}


**说明:**

从此 Sprite 中移除本地创建的动画, 其依据是给定的密钥 。

一旦动画被移除,这个Sprite无法在不重新创建的情况下再次播放.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的动画密钥 。 |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 从此 Sprite 中删除的动画实例, 如果密钥是有效的 。


> 源码：[src/animations/AnimationState.js#L1932](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1932)  
引入版本：3.50.0


---

### restart {#restart}

#### \<instance> restart([includeDelay], [resetRepeats]) {#instance-restartincludedelay-resetrepeats}


**说明:**

重新激活当前动画的起始位置 。

你可以选择重置延迟,也可以重复计数器.

调用这个会立即发射`ANIMATION_RESTART`事件.

如果`includeDelay`,它也会在延迟到期后发射`ANIMATION_START`事件,否则,播放会立即开始.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| includeDelay | boolean | 是 | false | 是否包含动画重启时的延迟值 。 |
| resetRepeats | boolean | 是 | false | 是否重设重置计数器? |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_RESTART](/api/event/animations-events#animation_restart)


> 源码：[src/animations/AnimationState.js#L1253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1253)  
引入版本：3.0.0


---

### resume {#resume}

#### \<instance> resume([fromFrame]) {#instance-resumefromframe}


**说明:**

将暂停动画的播放回放, 并将 `isPlaying` 属性设置为 `true` 。 您可以选择告诉它从特定框开始播放 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fromFrame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 是 | 重启播放前的可选框架 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


> 源码：[src/animations/AnimationState.js#L672](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L672)  
引入版本：3.0.0


---

### reverse {#reverse}

#### \<instance> reverse() {#instance-reverse}


**说明:**

反转游戏对象上已经播放的动画 。


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


> 源码：[src/animations/AnimationState.js#L1130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1130)  
引入版本：3.12.0


---

### setCurrentFrame {#setCurrentFrame}

#### \<instance> setCurrentFrame(animationFrame) {#instance-setcurrentframeanimationframe}


**说明:**

设定给定的动画框架为当前框架,并将其应用到母游戏对象,根据需要调整大小和来源.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animationFrame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 动画框要更改为. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 此动画组件所属的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_UPDATE](/api/event/animations-events#animation_update), [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/animations/AnimationState.js#L1564](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1564)  
引入版本：3.4.0


---

### setProgress {#setProgress}

#### \<instance> setProgress([value]) {#instance-setprogressvalue}


**说明:**

使用0到1之间的值,并用它来设定此动画通过回放的距离.

不考虑重复或 Yoyos, 但处理前向或后向播放。

值以当前帧为主,动画中这个距离有多远,不以动画的持续时间为主.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 进度值, 0 到 1 之间 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


> 源码：[src/animations/AnimationState.js#L1180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1180)  
引入版本：3.4.0


---

### setRepeat {#setRepeat}

#### \<instance> setRepeat(value) {#instance-setrepeatvalue}


**说明:**

设定动画在第一次播放后应重复的次数。 例如, 如果重复为 1, 动画将总共播放两次: 初始播放加1 重复 。

无限重复,使用 -1. 值应该始终是一个整数.

仅在动画已经运行时才使用这种方法。 否则, 当下一个动画加载时, 这里指定的任何值都会被覆盖。 要避免这种情况, 请使用 `PlayAnimationConfig` 对象的 `repeat` 属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 动画应重复的次数. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


> 源码：[src/animations/AnimationState.js#L1207](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1207)  
引入版本：3.4.0


---

### startAnimation {#startAnimation}

#### \<instance> startAnimation(key) {#instance-startanimationkey}


**说明:**

根据密钥加载动画, 并设置所有重启所需的内部值。 如果没有延迟, 也会点燃启动事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 | 动画中基于字符串的键来播放,或者一个`PlayAnimationConfig`对象. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_START](/api/event/animations-events#animation_start)


> 源码：[src/animations/AnimationState.js#L975](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L975)  
引入版本：3.50.0


---

### stop {#stop}

#### \<instance> stop() {#instance-stop}


**说明:**

立即停止当前动画播放,并发送`ANIMATION_STOP`事件.

如果没有动画运行,则不会发出事件.

如果队列中还有另一款动画(通过`chain`方法设定),则会开始播放.


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/animations/AnimationState.js#L1347](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1347)  
引入版本：3.0.0


---

### stopAfterDelay {#stopAfterDelay}

#### \<instance> stopAfterDelay(delay) {#instance-stopafterdelaydelay}


**说明:**

停止在指定时间延迟后播放当前动画,以毫秒计。

然后它就发出`ANIMATION_STOP`事件.

如果没有动画运行,则不会发出事件.

如果队列中还有另一部动画(通过`chain`方法设定),那么当当前动画停止时,它就会开始播放.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delay | number | 否 | 等待的毫秒数,然后停止这款动画. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/animations/AnimationState.js#L1385](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1385)  
引入版本：3.4.0


---

### stopAfterRepeat {#stopAfterRepeat}

#### \<instance> stopAfterRepeat([repeatCount]) {#instance-stopafterrepeatrepeatcount}


**说明:**

停止当前动画在下次重复时播放。

然后它就发出`ANIMATION_STOP`事件.

如果没有动画运行,则不会发出事件.

如果队列中还有另一部动画(通过`chain`方法设定),那么当当前动画停止时,它就会开始播放.

在Phaser 3.50之前,这种方法被称为`stopOnRepeat`,没有参数.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| repeatCount | number | 是 | 1 | 动画在停播前要重复多少次?. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/animations/AnimationState.js#L1411](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1411)  
引入版本：3.50.0


---

### stopOnFrame {#stopOnFrame}

#### \<instance> stopOnFrame(frame) {#instance-stoponframeframe}


**说明:**

当当前动画下个设定给定的帧时停止播放。 如果此帧不存在在动画中, 则不会阻止它播放 。

然后它就发出`ANIMATION_STOP`事件.

如果没有动画运行,则不会发出事件.

如果队列中还有另一部动画(通过`chain`方法设定),那么当当前动画停止时,它就会开始播放.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frame | [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) | 否 | 停止这段动画前要检查的帧 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 拥有此动画组件的游戏对象 。


**Fires:** [Phaser.Animations.Events#event:ANIMATION_STOP](/api/event/animations-events#animation_stop)


> 源码：[src/animations/AnimationState.js#L1446](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1446)  
引入版本：3.4.0


---

### update {#update}

#### \<instance> update(time, delta) {#instance-updatetime-delta}


**说明:**

动画状态组件的内部更新循环.

这被`Sprite.preUpdate`方法自动称为.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 现时时标. |
| delta | number | 否 | 三角洲时间,以ms计, 过去了,自上一个框架。 |


> 源码：[src/animations/AnimationState.js#L1487](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationState.js#L1487)  
引入版本：3.0.0


---

---
