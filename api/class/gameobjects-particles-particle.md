# Particle {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particle)

粒子是由粒子Emitter拥有和控制的轻量级对象。 每个粒子都拥有自己的位置、速度、加速、旋转、尺度、α、锡和寿命值, 由 Emitter 配置的 EmitterOp 实例更新。 粒子集合和回收后, 粒子会被 Emitter 的寿命到期时, 粒子被关闭并返回池中重新使用, 而不是被销毁。 您通常不会直接创建粒子事件, 而是由 Emitter 管理其生命周期。 您可以通过在 发射器配置中提供自定义的 `particleClass` 来扩展此类, 以添加自定义属性 。

**构造函数**

`new Particle(emitter)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 本粒子所属的 Emitter 。 |

---


**作用域**: static

> 源码：[src/gameobjects/particles/Particle.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L15)  
引入版本：3.0.0

## 公开成员 {#public-members}

### accelerationX {#accelerationX}

#### accelerationX: number {#accelerationx-number}


**说明:**

此粒子的x加速度, 以每秒平方像素计 。


> 源码：[src/gameobjects/particles/Particle.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L121)  
引入版本：3.0.0


---

### accelerationY {#accelerationY}

#### accelerationY: number {#accelerationy-number}


**说明:**

此粒子的y加速度, 以像素每秒平方位为单位 。


> 源码：[src/gameobjects/particles/Particle.js#L131](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L131)  
引入版本：3.0.0


---

### alpha {#alpha}

#### alpha: number {#alpha-number}


**说明:**

此粒子的α值 。


> 源码：[src/gameobjects/particles/Particle.js#L191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L191)  
引入版本：3.0.0


---

### angle {#angle}

#### angle: number {#angle-number}


**说明:**

以度表示的这个粒子角度 。


> 源码：[src/gameobjects/particles/Particle.js#L201](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L201)  
引入版本：3.0.0


---

### anims {#anims}

#### anims: [Phaser.Animations.AnimationState](/api/class/animations-animationstate) {#anims-phaseranimationsanimationstate}


**说明:**

本粒子的动画状态组件。

此组件提供了将动画应用于此粒子的特性,它负责播放,加载,排队动画用于以后的播放,动画间的混合以及将当前动画框设置为此粒子.

只有在粒子的Emitter至少有一幅动画时才会创建.


> 源码：[src/gameobjects/particles/Particle.js#L333](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L333)  
引入版本：3.60.0


---

### bounce {#bounce}

#### bounce: number {#bounce-number}


**说明:**

丰厚,或归还,此品.


> 源码：[src/gameobjects/particles/Particle.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L161)  
引入版本：3.0.0


---

### bounds {#bounds}

#### bounds: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#bounds-phasergeomrectangle}


**说明:**

已发出`Particle.getBounds`方法的调用后, 设有此粒子界限的矩形 。


> 源码：[src/gameobjects/particles/Particle.js#L354](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L354)  
引入版本：3.60.0


---

### data {#data}

#### data: [Phaser.Types.GameObjects.Particles.ParticleData](/api/typedef/types-gameobjects-particles#particledata) {#data-phasertypesgameobjectsparticlesparticledata}


**说明:**

存储此粒子每个属性的分/最大插值( 如α、 锡、 scaleX、 旋转等) 的对象, 因为这些值在粒子寿命期间会有所缓解。 这些值被母的 EmitterOp 实例所覆盖和使用 。


> 源码：[src/gameobjects/particles/Particle.js#L281](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L281)  
引入版本：3.0.0


---

### delayCurrent {#delayCurrent}

#### delayCurrent: number {#delaycurrent-number}


**说明:**

排放时该物质的延迟适用,以毫秒计。


> 源码：[src/gameobjects/particles/Particle.js#L251](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L251)  
引入版本：3.0.0


---

### emitter {#emitter}

#### emitter: [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) {#emitter-phasergameobjectsparticlesparticleemitter}


**说明:**

本粒子所属的 Emitter 。

一颗粒子只能属于一个单一的Emitter,并由它创建,更新和销毁.


> 源码：[src/gameobjects/particles/Particle.js#L39](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L39)  
引入版本：3.0.0


---

### frame {#frame}

#### frame: [Phaser.Textures.Frame](/api/class/textures-frame) {#frame-phasertexturesframe}


**说明:**

本粒子在制作时使用的纹理框架 。


> 源码：[src/gameobjects/particles/Particle.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L60)  
引入版本：3.0.0


---

### holdCurrent {#holdCurrent}

#### holdCurrent: number {#holdcurrent-number}


**说明:**

本保留在它到期前适用于此粒子,以毫秒计。


> 源码：[src/gameobjects/particles/Particle.js#L261](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L261)  
引入版本：3.60.0


---

### life {#life}

#### life: number {#life-number}


**说明:**

以毫秒计的这一粒子的寿命。


> 源码：[src/gameobjects/particles/Particle.js#L231](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L231)  
引入版本：3.0.0


---

### lifeCurrent {#lifeCurrent}

#### lifeCurrent: number {#lifecurrent-number}


**说明:**

以毫秒计的这个粒子的当前寿命 。


> 源码：[src/gameobjects/particles/Particle.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L241)  
引入版本：3.0.0


---

### lifeT {#lifeT}

#### lifeT: number {#lifet-number}


**说明:**

正常寿命值 T, 其中0为起始值, 1为结束值 。


> 源码：[src/gameobjects/particles/Particle.js#L271](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L271)  
引入版本：3.0.0


---

### maxVelocityX {#maxVelocityX}

#### maxVelocityX: number {#maxvelocityx-number}


**说明:**

此粒子的最大水平速度可以以每秒像素的速度行驶。


> 源码：[src/gameobjects/particles/Particle.js#L141](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L141)  
引入版本：3.0.0


---

### maxVelocityY {#maxVelocityY}

#### maxVelocityY: number {#maxvelocityy-number}


**说明:**

此粒子的最大垂直速度可以以每秒像素的速度进行。


> 源码：[src/gameobjects/particles/Particle.js#L151](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L151)  
引入版本：3.0.0


---

### rotation {#rotation}

#### rotation: number {#rotation-number}


**说明:**

弧度中这个粒子的角度.


> 源码：[src/gameobjects/particles/Particle.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L211)  
引入版本：3.0.0


---

### scaleX {#scaleX}

#### scaleX: number {#scalex-number}


**说明:**

本粒子的横向尺度 。


> 源码：[src/gameobjects/particles/Particle.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L171)  
引入版本：3.0.0


---

### scaleY {#scaleY}

#### scaleY: number {#scaley-number}


**说明:**

本粒子的垂直比例 。


> 源码：[src/gameobjects/particles/Particle.js#L181](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L181)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

引用此游戏对象所属的景色 。

游戏对象只能属于一个场景.

您应该将此属性视为只读。 您不能简单地更改它, 而将游戏对象移动到另一个场景 。


> 源码：[src/gameobjects/particles/Particle.js#L319](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L319)  
引入版本：3.60.0


---

### texture {#texture}

#### texture: [Phaser.Textures.Texture](/api/class/textures-texture) {#texture-phasertexturestexture}


**说明:**

本粒子在制作时使用的纹理 。


> 源码：[src/gameobjects/particles/Particle.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L50)  
引入版本：3.60.0


---

### tint {#tint}

#### tint: number {#tint-number}


**说明:**

锡适用于此粒子。

**Tags:**

 - webglOnly


> 源码：[src/gameobjects/particles/Particle.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L221)  
引入版本：3.0.0


---

### velocityX {#velocityX}

#### velocityX: number {#velocityx-number}


**说明:**

此粒子的x速度, 以像素每秒为单位 。


> 源码：[src/gameobjects/particles/Particle.js#L101](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L101)  
引入版本：3.0.0


---

### velocityY {#velocityY}

#### velocityY: number {#velocityy-number}


**说明:**

此粒子的y 速度, 以像素每秒为单位 。


> 源码：[src/gameobjects/particles/Particle.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L111)  
引入版本：3.0.0


---

### worldPosition {#worldPosition}

#### worldPosition: [Phaser.Math.Vector2](/api/class/math-vector2) {#worldposition-phasermathvector2}


**说明:**

地球空间中这一粒子的坐标.

更新为`computeVelocity`的一部分.


> 源码：[src/gameobjects/particles/Particle.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L90)  
引入版本：3.60.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

本粒子的x坐标 。


> 源码：[src/gameobjects/particles/Particle.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L70)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

此粒子的y坐标 。


> 源码：[src/gameobjects/particles/Particle.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L80)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### computeVelocity {#computeVelocity}

#### \<instance> computeVelocity(emitter, delta, step, processors, t) {#instance-computevelocityemitter-delta-step-processors-t}


**说明:**

计算粒子速度及其世界位置的内部方法。它也会对设置在 Emitter 上的任何活动处理器进行运行。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 正在更新此粒子的 Emitter 。 |
| delta | number | 否 | 三角洲时间以ms计. |
| step | number | 否 | 三角洲值除以1000. |
| processors | Array.\<[Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor)> | 否 | 一组所有活跃的粒子处理器。 |
| t | number | 否 | 目前粒子的正常寿命,在0(出生)至1(死亡)之间. |


> 源码：[src/gameobjects/particles/Particle.js#L675](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L675)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

将本粒子的引用取消给发射体、纹理、帧和场景的引用,从而破坏此粒子。如果此粒子具有动画状态,则该粒子也已被销毁。在使用此方法后,不应再次使用该粒子。


> 源码：[src/gameobjects/particles/Particle.js#L796](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L796)  
引入版本：3.60.0


---

### emit {#emit}

#### \<instance> emit(event, [a1], [a2], [a3], [a4], [a5]) {#instance-emitevent-a1-a2-a3-a4-a5}


**说明:**

事件 Emitter 代理服务器 。

将所有参数传递到 `ParticleEmitter` 直接发射.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | string \| Symbol | 否 | 事件名称. |
| a1 | any | 是 | 任择论点1。 |
| a2 | any | 是 | 可选论点2。 |
| a3 | any | 是 | 任择论点3。 |
| a4 | any | 是 | 任择论点4。 |
| a5 | any | 是 | 任择论点5。 |


**返回值:** boolean - 如果有听众的话,就用`true`,否则用`false`.


> 源码：[src/gameobjects/particles/Particle.js#L365](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L365)  
引入版本：3.60.0


---

### fire {#fire}

#### \<instance> fire([x], [y]) {#instance-firex-y}


**说明:**

从给定的坐标开始此粒子。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 是 | X坐标从此发射此粒子. |
| y | number | 是 | 发射此粒子的Y坐标 。 |


**返回值:** boolean - 如果粒子还活着,`true`, 如果它是在死区产下的,`false`。


> 源码：[src/gameobjects/particles/Particle.js#L432](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L432)  
引入版本：3.0.0


---

### getBounds {#getBounds}

#### \<instance> getBounds([matrix]) {#instance-getboundsmatrix}


**说明:**

获得此粒子的边界作为几何矩形,在母发射器的任何变换中和显示列表中其他任何上方的变换中计及.

一旦计算,边界可以通过`Particle.bounds`属性访问。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| matrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 可选变换矩阵适用于此粒子 。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 包含这个粒子的变形界限的矩形.


> 源码：[src/gameobjects/particles/Particle.js#L742](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L742)  
引入版本：3.60.0


---

### isAlive {#isAlive}

#### \<instance> isAlive() {#instance-isalive}


**说明:**

检查此粒子是否存活和更新 。


**返回值:** boolean - `true` 如果这颗粒子还活着并更新,否则 `false`.


> 源码：[src/gameobjects/particles/Particle.js#L387](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L387)  
引入版本：3.0.0


---

### kill {#kill}

#### \<instance> kill() {#instance-kill}


**说明:**

杀死此粒子。 它将 `lifeCurrent` 值设置为 0, 从而迫使粒子在下次母 Emitter 运行更新时被删除 。


> 源码：[src/gameobjects/particles/Particle.js#L400](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L400)  
引入版本：3.60.0


---

### setPosition {#setPosition}

#### \<instance> setPosition([x], [y]) {#instance-setpositionx-y}


**说明:**

将这个粒子的位置设置到给定的 x/y 坐标。

如果参数未定义,它会将粒子重新放回(0,0).

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 设置此粒子的 x 坐标 。 |
| y | number | 是 | 0 | 设置此粒子的 Y 坐标 。 |


> 源码：[src/gameobjects/particles/Particle.js#L412](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L412)  
引入版本：3.60.0


---

### setSizeToFrame {#setSizeToFrame}

#### \<instance> setSizeToFrame() {#instance-setsizetoframe}


**说明:**

这是诺OP方法,在呼叫时不起作用。


> 源码：[src/gameobjects/particles/Particle.js#L731](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L731)  
引入版本：3.60.0


---

### update {#update}

#### \<instance> update(delta, step, processors) {#instance-updatedelta-step-processors}


**说明:**

本粒子的主要更新方法.

更新其寿命值,计算速度并重新定位粒子。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| delta | number | 否 | 三角洲时间以ms计. |
| step | number | 否 | 三角洲值除以1000. |
| processors | Array.\<[Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor)> | 否 | 一组所有活跃的粒子处理器。 |


**返回值:** boolean - 如果此粒子已经过期, 则应返回 `true`, 否则如果仍然有效, 则返回 `false` 。


> 源码：[src/gameobjects/particles/Particle.js#L570](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/Particle.js#L570)  
引入版本：3.0.0


---

---
