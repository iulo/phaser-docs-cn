# EmitterOp {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-emitterop)

该类负责控制粒子类中的单一属性,并管理其排放和更新功能。

`x`,`y`,`scaleX`,`lifespan`等粒子属性都使用EmitterOp实例来管理它们,因为可以以多种形式给出:从简单的值到函数,到动态回调.

更多关于发射机操作配置的细节,请参见`ParticleEmitter`类.

**构造函数**

`new EmitterOp(key, defaultValue, [emitOnly])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 属性名称. |
| defaultValue | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 否 |  | 属性的默认值 。 |
| emitOnly | boolean | 是 | false | 是否只能在粒子被释放时修改属性 。 |

---


**作用域**: static

> 源码：[src/gameobjects/particles/EmitterOp.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L17)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

设定为 `false` 以禁用此 EmitterOp 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L203](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L203)  
引入版本：3.60.0


---

### counter {#counter}

#### counter: number {#counter-number}


**说明:**

渐渐放松的台阶计数器,每发射一次。


> 源码：[src/gameobjects/particles/EmitterOp.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L89)  
引入版本：3.0.0


---

### current {#current}

#### current: number {#current-number}


**说明:**

最新计算值。 每次使用排放或更新方法时都会更新。 仅将它视为只读 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L132)  
引入版本：3.60.0


---

### defaultValue {#defaultValue}

#### defaultValue: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype), [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) {#defaultvalue-phasertypesgameobjectsparticlesemitteroponemittype-phasertypesgameobjectsparticlesemitteroponupdatetype}


**说明:**

此属性的默认值 。

这可以是简单的值,一个阵列,一个函数或一个onEmit配置对象.


> 源码：[src/gameobjects/particles/EmitterOp.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L66)  
引入版本：3.0.0


---

### direction {#direction}

#### direction: number {#direction-number}


**说明:**

反方向,上下各1个


> 源码：[src/gameobjects/particles/EmitterOp.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L110)  
引入版本：3.60.0


---

### ease {#ease}

#### ease: function {#ease-function}


**说明:**

用于更新此属性的放松功能( 如果有的话) 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L152](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L152)  
引入版本：3.0.0


---

### emitOnly {#emitOnly}

#### emitOnly: boolean {#emitonly-boolean}


**说明:**

是否只能在粒子被释放时修改此属性 。

设定为 `true` , 只允许设置 [Phaser.GameObjects.Particles.EmitterOp#onEmit](/api/class/gameobjects-particles-emitterop#onEmit) 回调并影响此属性 。

设定为 `false` , 允许设置 [Phaser.GameObjects.Particles.EmitterOp#onEmit](/api/class/gameobjects-particles-emitterop#onEmit) 和 [Phaser.GameObjects.Particles.EmitterOp#onUpdate](/api/class/gameobjects-particles-emitterop#onUpdate) 调用并影响此属性 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L170](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L170)  
引入版本：3.0.0


---

### end {#end}

#### end: number {#end-number}


**说明:**

此属性的结束值可以轻松介于两者之间 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L142)  
引入版本：3.0.0


---

### interpolation {#interpolation}

#### interpolation: function {#interpolation-function}


**说明:**

用于更新此属性的插值功能( 如果有的话) 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L161](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L161)  
引入版本：3.60.0


---

### method {#method}

#### method: number {#method-number}


**说明:**

这个EmitterOp的onEmit方法类型.

设定为 `setMethod` 的一部分, 在此缓存, 以避免值仅改变时重设 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L212](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L212)  
引入版本：3.60.0


---

### onEmit {#onEmit}

#### onEmit: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitCallback](/api/typedef/types-gameobjects-particles#emitteroponemitcallback) {#onemit-phasertypesgameobjectsparticlesemitteroponemitcallback}


**说明:**

粒子发射时的回调 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L185](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L185)  
引入版本：3.0.0


---

### onUpdate {#onUpdate}

#### onUpdate: [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateCallback](/api/typedef/types-gameobjects-particles#emitteroponupdatecallback) {#onupdate-phasertypesgameobjectsparticlesemitteroponupdatecallback}


**说明:**

更新时对粒子的回调 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L194](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L194)  
引入版本：3.0.0


---

### propertyKey {#propertyKey}

#### propertyKey: string {#propertykey-string}


**说明:**

此属性名.


> 源码：[src/gameobjects/particles/EmitterOp.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L45)  
引入版本：3.0.0


---

### propertyValue {#propertyValue}

#### propertyValue: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype), [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) {#propertyvalue-phasertypesgameobjectsparticlesemitteroponemittype-phasertypesgameobjectsparticlesemitteroponupdatetype}


**说明:**

此属性的当前值 。

这可以是简单的值,一个阵列,一个函数或一个onEmit配置对象.


> 源码：[src/gameobjects/particles/EmitterOp.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L54)  
引入版本：3.0.0


---

### start {#start}

#### start: number, Array.\<number> {#start-number-arraynumber}


**说明:**

此属性的起始值在两者之间可以轻松化 。

如果插值包含数字数据数组的引用。


> 源码：[src/gameobjects/particles/EmitterOp.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L120)  
引入版本：3.0.0


---

### steps {#steps}

#### steps: number {#steps-number}


**说明:**

用于[Phaser.GameObjects.Particles.EmitterOp#start](/api/class/gameobjects-particles-emitterop#start)值和[Phaser.GameObjects.Particles.EmitterOp#end](/api/class/gameobjects-particles-emitterop#end)值之间逐步放松的步骤数,每发射一次。


> 源码：[src/gameobjects/particles/EmitterOp.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L78)  
引入版本：3.0.0


---

### yoyo {#yoyo}

#### yoyo: boolean {#yoyo-boolean}


**说明:**

当台阶计数器达到最大时,是Yoyo回到开始,还是翻过来?


> 源码：[src/gameobjects/particles/EmitterOp.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L99)  
引入版本：3.60.0


---

## 公开方法 {#public-methods}

### defaultEmit {#defaultEmit}

#### \<instance> defaultEmit() {#instance-defaultemit}


**说明:**

返回的值设定了粒子生命中的属性,即发射时的属性。


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L598](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L598)  
引入版本：3.0.0


---

### defaultUpdate {#defaultUpdate}

#### \<instance> defaultUpdate(particle, key, t, value) {#instance-defaultupdateparticle-key-t-value}


**说明:**

返回值更新了粒子寿命期间的属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 属性名称. |
| t | number | 否 | 目前粒子的正常寿命,在0(出生)至1(死亡)之间. |
| value | number | 否 | 属性的当前价值 。 |


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L611](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L611)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁这个 EmitterOp 实例及其所有引用 。

当拥有此 EmitterOp 的粒子报盘被销毁时自动调用 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L899](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L899)  
引入版本：3.60.0


---

### easedValueEmit {#easedValueEmit}

#### \<instance> easedValueEmit(particle, key) {#instance-easedvalueemitparticle-key}


**说明:**

一张`onEmit`回调码 以获得一个宽松的地产。

它用[Phaser.GameObjects.Particles.EmitterOp#easeValueUpdate](/api/class/gameobjects-particles-emitterop#easeValueUpdate)来准备粒子放松.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 属性名称. |


**返回值:** number - [Phaser.GameObjects.Particles.EmitterOp#start](/api/class/gameobjects-particles-emitterop#start),作为房产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L836](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L836)  
引入版本：3.0.0


---

### easeValueUpdate {#easeValueUpdate}

#### \<instance> easeValueUpdate(particle, key, t) {#instance-easevalueupdateparticle-key-t}


**说明:**

来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,,来,你,你,,来,来,来,来,,来,来,来,,,,你,你,,,你,,,,,来,,,,你,,来,,来,你,,你,你,来,你,,,,,来,,来,来,来,,,,来,,,你,你,你,来,来,你,你,来,你,来,来,来,你,,,,,来,,,来,你,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,来,,,,,, `onUpdate` 调回返回在 [Phaser.GameObjects.Particles.EmitterOp#start](/api/class/gameobjects-particles-emitterop#start) 财务报告和已审计财务报表 [Phaser.GameObjects.Particles.EmitterOp#end](/api/class/gameobjects-particles-emitterop#end) 范围。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 属性名称. |
| t | number | 否 | 目前粒子的正常寿命,在0(出生)至1(死亡)之间. |


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L864](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L864)  
引入版本：3.0.0


---

### getMethod {#getMethod}

#### \<instance> getMethod() {#instance-getmethod}


**说明:**

检查 `EmitterOp.propertyValue` 的类型,以确定需要用何种方法才能从此 op 函数返回值。


**返回值:** number - 0到9之间的数字,应该传递到`setMethods`.


> 源码：[src/gameobjects/particles/EmitterOp.js#L360](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L360)  
引入版本：3.60.0


---

### has {#has}

#### \<instance> has(object, key) {#instance-hasobject-key}


**说明:**

检查对象是否有给定属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | object | 否 | 要检查的对象 。 |
| key | string | 否 | 对象中要查找的属性的键 。 |


**返回值:** boolean - `true` 如果该属性存在于对象中, `false` 否则。


> 源码：[src/gameobjects/particles/EmitterOp.js#L548](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L548)  
引入版本：3.0.0


---

### hasBoth {#hasBoth}

#### \<instance> hasBoth(object, key1, key2) {#instance-hasbothobject-key1-key2}


**说明:**

检查对象是否具有两个给定属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | object | 否 | 要检查的对象 。 |
| key1 | string | 否 | 第一个属性的键来检查对象 。 |
| key2 | string | 否 | 第二个属性的键来检查对象 。 |


**返回值:** boolean - `true` 如果物体中存在两个属性, `false` 否则。


> 源码：[src/gameobjects/particles/EmitterOp.js#L564](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L564)  
引入版本：3.0.0


---

### hasEither {#hasEither}

#### \<instance> hasEither(object, key1, key2) {#instance-haseitherobject-key1-key2}


**说明:**

检查对象是否至少拥有一个给定属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | object | 否 | 要检查的对象 。 |
| key1 | string | 否 | 第一个属性的键来检查对象 。 |
| key2 | string | 否 | 第二个属性的键来检查对象 。 |


**返回值:** boolean - 如果对象中至少有一个属性存在,则`true`,如果两者均不存在,则`false`。


> 源码：[src/gameobjects/particles/EmitterOp.js#L581](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L581)  
引入版本：3.0.0


---

### loadConfig {#loadConfig}

#### \<instance> loadConfig([config], [newKey]) {#instance-loadconfigconfig-newkey}


**说明:**

从粒子 Emitter 配置对象中装入属性 。

可选接受新属性键使用,替换当前键.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](/api/typedef/types-gameobjects-particles#particleemitterconfig) | 是 | 拥有此属性的粒子 Emitter 设置 。 |
| newKey | string | 是 | 用于此属性的新键, 如果有的话 。 |


> 源码：[src/gameobjects/particles/EmitterOp.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L247)  
引入版本：3.0.0


---

### onChange {#onChange}

#### \<instance> onChange(value) {#instance-onchangevalue}


**说明:**

更改属性的当前值并更新其召回方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 此属性的新数值 。 |


**返回值:** [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) - 这个 Emitter Op 对象 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L300](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L300)  
引入版本：3.0.0


---

### proxyEmit {#proxyEmit}

#### \<instance> proxyEmit(particle, key, [value]) {#instance-proxyemitparticle-key-value}


**说明:**

返回的值设定了粒子生命中的属性,即发射时的属性。

只有在您提供了自定义的回调时,才会使用这种方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 属性名称. |
| value | number | 是 | 属性的当前价值 。 |


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L629](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L629)  
引入版本：3.60.0


---

### proxyUpdate {#proxyUpdate}

#### \<instance> proxyUpdate(particle, key, t, value) {#instance-proxyupdateparticle-key-t-value}


**说明:**

返回值更新了粒子寿命期间的属性.

只有在您提供了自定义更新回调时才会使用这种方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 属性名称. |
| t | number | 否 | 目前粒子的正常寿命,在0(出生)至1(死亡)之间. |
| value | number | 否 | 属性的当前价值 。 |


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L652](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L652)  
引入版本：3.60.0


---

### randomRangedIntEmit {#randomRangedIntEmit}

#### \<instance> randomRangedIntEmit(particle, key) {#instance-randomrangedintemitparticle-key}


**说明:**

一个`onEmit`召回,返回[Phaser.GameObjects.Particles.EmitterOp#start](/api/class/gameobjects-particles-emitterop#start)和[Phaser.GameObjects.Particles.EmitterOp#end](/api/class/gameobjects-particles-emitterop#end)范围之间的随机整数值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 地产之钥. |


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L746](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L746)  
引入版本：3.60.0


---

### randomRangedValueEmit {#randomRangedValueEmit}

#### \<instance> randomRangedValueEmit(particle, key) {#instance-randomrangedvalueemitparticle-key}


**说明:**

返回[Phaser.GameObjects.Particles.EmitterOp#start](/api/class/gameobjects-particles-emitterop#start)和[Phaser.GameObjects.Particles.EmitterOp#end](/api/class/gameobjects-particles-emitterop#end)范围之间值的`onEmit`召回。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 地产之钥. |


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L719](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L719)  
引入版本：3.0.0


---

### randomStaticValueEmit {#randomStaticValueEmit}

#### \<instance> randomStaticValueEmit() {#instance-randomstaticvalueemit}


**说明:**

一个 `onEmit` 回调,从当前值阵列返回随机值。


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L702](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L702)  
引入版本：3.0.0


---

### setMethods {#setMethods}

#### \<instance> setMethods() {#instance-setmethods}


**说明:**

基于 `getMethod`返回的方法更新 [Phaser.GameObjects.Particles.EmitterOp#onEmit](/api/class/gameobjects-particles-emitterop#onEmit) 和 [Phaser.GameObjects.Particles.EmitterOp#onUpdate](/api/class/gameobjects-particles-emitterop#onUpdate) 回调。 该方法存储在 `EmitterOp.method` 属性中, 包含数字在 0 到 9 之间 。


**返回值:** [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) - 这个 Emitter Op 对象 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L436](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L436)  
引入版本：3.0.0


---

### staticValueEmit {#staticValueEmit}

#### \<instance> staticValueEmit() {#instance-staticvalueemit}


**说明:**

一个返回当前属性值的 `onEmit` 回调 。


**返回值:** number - 属性的当前价值 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L676](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L676)  
引入版本：3.0.0


---

### staticValueUpdate {#staticValueUpdate}

#### \<instance> staticValueUpdate() {#instance-staticvalueupdate}


**说明:**

一个返回当前属性值的 `onUpdate` 回调 。


**返回值:** number - 属性的当前价值 。


> 源码：[src/gameobjects/particles/EmitterOp.js#L689](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L689)  
引入版本：3.0.0


---

### steppedEmit {#steppedEmit}

#### \<instance> steppedEmit() {#instance-steppedemit}


**说明:**

来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,来,,来,你,你,,来,来,来,来,,来,来,来,,,,你,你,,,你,,,,,来,,,,你,,来,,来,你,,你,你,来,你,,,,,来,,来,来,来,,,,来,,,你,你,你,来,来,你,你,来,你,来,来,来,你,,,,,来,,,来,你,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,来,,,,,, `onEmit` 调回返回在 [Phaser.GameObjects.Particles.EmitterOp#start](/api/class/gameobjects-particles-emitterop#start) 财务报告和已审计财务报表 [Phaser.GameObjects.Particles.EmitterOp#end](/api/class/gameobjects-particles-emitterop#end) 范围。


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterOp.js#L773](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L773)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

建立该粒子喷雾器属性的JSON代表。


**返回值:** object - JSON代表了这种颗粒喷射物。


> 源码：[src/gameobjects/particles/EmitterOp.js#L287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterOp.js#L287)  
引入版本：3.0.0


---

---
