# EmitterColorOp {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-emittercolorop)

一个专门管理粒子终生的 `color` 属性的发射程序。与 Scalar 发射程序不同, `EmitterColorOp` 接受一个十六进制的颜色值( 如 `[0xff0000, 0x00ff00, 0x0000ff]`) 阵列, 并在它们之间作为粒子年龄进行平稳的插值, 产生从出生到死亡的梯度颜色过渡 。

色彩阵列在配置上分解成单独的红,绿,蓝三个组件阵列,每个更新步骤都使用线性插值功能将其重新压缩到当前包装的RGB颜色值中.

当 `color` 属性在发射器配置中存在时, 此类会由 `ParticleEmitter` 自动创建和管理; 您通常不需要直接即时处理 。

更多关于发射机操作配置的细节,请参见`ParticleEmitter`类.

**构造函数**

`new EmitterColorOp(key)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 属性名称. |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop)  



> 源码：[src/gameobjects/particles/EmitterColorOp.js#L14](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L14)  
引入版本：3.60.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop):**


 - [active](/api/class/gameobjects-particles-emitterop#active)
 - [counter](/api/class/gameobjects-particles-emitterop#counter)
 - [current](/api/class/gameobjects-particles-emitterop#current)
 - [defaultValue](/api/class/gameobjects-particles-emitterop#defaultValue)
 - [direction](/api/class/gameobjects-particles-emitterop#direction)
 - [ease](/api/class/gameobjects-particles-emitterop#ease)
 - [emitOnly](/api/class/gameobjects-particles-emitterop#emitOnly)
 - [end](/api/class/gameobjects-particles-emitterop#end)
 - [interpolation](/api/class/gameobjects-particles-emitterop#interpolation)
 - [method](/api/class/gameobjects-particles-emitterop#method)
 - [onEmit](/api/class/gameobjects-particles-emitterop#onEmit)
 - [onUpdate](/api/class/gameobjects-particles-emitterop#onUpdate)
 - [propertyKey](/api/class/gameobjects-particles-emitterop#propertyKey)
 - [propertyValue](/api/class/gameobjects-particles-emitterop#propertyValue)
 - [start](/api/class/gameobjects-particles-emitterop#start)
 - [steps](/api/class/gameobjects-particles-emitterop#steps)
 - [yoyo](/api/class/gameobjects-particles-emitterop#yoyo)




---

## 公开成员 {#public-members}

### b {#b}

#### b: Array.\<number> {#b-arraynumber}


**说明:**

包含蓝色的颜色值的阵列 。

使用`setMethods`法进行配种.


> 源码：[src/gameobjects/particles/EmitterColorOp.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L76)  
引入版本：3.60.0


---

### g {#g}

#### g: Array.\<number> {#g-arraynumber}


**说明:**

包含绿色值的阵列 。

使用`setMethods`法进行配种.


> 源码：[src/gameobjects/particles/EmitterColorOp.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L65)  
引入版本：3.60.0


---

### r {#r}

#### r: Array.\<number> {#r-arraynumber}


**说明:**

包含红色值的阵列 。

使用`setMethods`法进行配种.


> 源码：[src/gameobjects/particles/EmitterColorOp.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L54)  
引入版本：3.60.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop):**


 - [defaultEmit](/api/class/gameobjects-particles-emitterop#defaultEmit)
 - [defaultUpdate](/api/class/gameobjects-particles-emitterop#defaultUpdate)
 - [destroy](/api/class/gameobjects-particles-emitterop#destroy)
 - [has](/api/class/gameobjects-particles-emitterop#has)
 - [hasBoth](/api/class/gameobjects-particles-emitterop#hasBoth)
 - [hasEither](/api/class/gameobjects-particles-emitterop#hasEither)
 - [loadConfig](/api/class/gameobjects-particles-emitterop#loadConfig)
 - [onChange](/api/class/gameobjects-particles-emitterop#onChange)
 - [proxyEmit](/api/class/gameobjects-particles-emitterop#proxyEmit)
 - [proxyUpdate](/api/class/gameobjects-particles-emitterop#proxyUpdate)
 - [randomRangedIntEmit](/api/class/gameobjects-particles-emitterop#randomRangedIntEmit)
 - [randomRangedValueEmit](/api/class/gameobjects-particles-emitterop#randomRangedValueEmit)
 - [randomStaticValueEmit](/api/class/gameobjects-particles-emitterop#randomStaticValueEmit)
 - [staticValueEmit](/api/class/gameobjects-particles-emitterop#staticValueEmit)
 - [staticValueUpdate](/api/class/gameobjects-particles-emitterop#staticValueUpdate)
 - [steppedEmit](/api/class/gameobjects-particles-emitterop#steppedEmit)
 - [toJSON](/api/class/gameobjects-particles-emitterop#toJSON)




---

## 公开方法 {#public-methods}

### easedValueEmit {#easedValueEmit}

#### \<instance> easedValueEmit(particle, key) {#instance-easedvalueemitparticle-key}


**说明:**

一张`onEmit`回调码 以获得一个宽松的地产。

它用[Phaser.GameObjects.Particles.EmitterColorOp#easeValueUpdate](/api/class/gameobjects-particles-emittercolorop#easeValueUpdate)来准备粒子放松.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 属性名称. |


**重写:** Phaser.GameObjects.Particles.EmitterOp#easedValueEmit


**返回值:** number - [Phaser.GameObjects.Particles.EmitterColorOp#start](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-emittercolorop.md#start),作为房产的新价值.


> 源码：[src/gameobjects/particles/EmitterColorOp.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L173)  
引入版本：3.60.0


---

### easeValueUpdate {#easeValueUpdate}

#### \<instance> easeValueUpdate(particle, key, t) {#instance-easevalueupdateparticle-key-t}


**说明:**

基于粒子当前正常寿命,返回所配置的颜色阵列上插件的RGB颜色值的`onUpdate`调回。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 属性名称. |
| t | number | 否 | 目前粒子的正常寿命,在0(出生)至1(死亡)之间. |


**重写:** Phaser.GameObjects.Particles.EmitterOp#easeValueUpdate


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/EmitterColorOp.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L193)  
引入版本：3.60.0


---

### getMethod {#getMethod}

#### \<instance> getMethod() {#instance-getmethod}


**说明:**

检查 `EmitterOp.propertyValue` 的类型,以确定需要用何种方法才能从此 op 函数返回值。


**重写:** Phaser.GameObjects.Particles.EmitterOp#getMethod


**返回值:** number - 如果未设置颜色属性值, 则使用 `0` , 如果配置了颜色数组, 则使用 `9` 。 其结果应传递给 `setMethods` 。


> 源码：[src/gameobjects/particles/EmitterColorOp.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L88)  
引入版本：3.60.0


---

### setEase {#setEase}

#### \<instance> setEase(ease) {#instance-seteaseease}


**说明:**

设置用于彩色插值的易用函数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| ease | string | 否 | 以字符串为基础的 Ease 函数的名称。 |


> 源码：[src/gameobjects/particles/EmitterColorOp.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L158)  
引入版本：3.60.0


---

### setMethods {#setMethods}

#### \<instance> setMethods() {#instance-setmethods}


**说明:**

配置此颜色 Op 的发回和更新调用, 其依据是当前 `method` 值。 当一个颜色数组存在( 方法 9) 时, 它会将 `propertyValue` 中每个已包装的六进制颜色分解为单独的红、绿和蓝元件数组, 设置线性宽松和插值功能, 并指定易控的发回和更新处理器。 如果设置了颜色值( 方法 0) , 默认的不操作处理器会被使用 。


**重写:** Phaser.GameObjects.Particles.EmitterOp#setMethods


**返回值:** [Phaser.GameObjects.Particles.EmitterColorOp](/api/class/gameobjects-particles-emittercolorop) - 这个 Emitter Op 对象 。


> 源码：[src/gameobjects/particles/EmitterColorOp.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/EmitterColorOp.js#L102)  
引入版本：3.60.0


---

---
