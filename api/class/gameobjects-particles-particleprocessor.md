# ParticleProcessor {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particleprocessor)

这一类提供了所有粒子处理器所需的结构.

您应该扩展它并添加您的处理器所需的功能, 包括清理 `destroy` 方法中可能创建的任何资源 。

以Gravity Well为例,参见处理器.

**构造函数**

`new ParticleProcessor([x], [y], [active])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 粒子处理器的x坐标,在世界空间中. |
| y | number | 是 | 0 | 粒子处理器的y坐标,在世界空间。 |
| active | boolean | 是 | true | 此粒子处理器的活跃状态 。 |

---


**作用域**: static

> 源码：[src/gameobjects/particles/ParticleProcessor.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleProcessor.js#L9)  
引入版本：3.60.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

粒子处理器的活跃状态 。

一个不活动的粒子处理器将被跳过, 由其母 Emitter 处理 。


> 源码：[src/gameobjects/particles/ParticleProcessor.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleProcessor.js#L66)  
引入版本：3.60.0


---

### emitter {#emitter}

#### emitter: [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) {#emitter-phasergameobjectsparticlesparticleemitter}


**说明:**

属于此处理器的粒子 Emitter 引用。 当处理器添加到 Emitter 时, 此选项会自动设定, 当删除或销毁时, 则无效 。


> 源码：[src/gameobjects/particles/ParticleProcessor.js#L37](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleProcessor.js#L37)  
引入版本：3.60.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

粒子处理器的x坐标,在世界空间中.


> 源码：[src/gameobjects/particles/ParticleProcessor.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleProcessor.js#L48)  
引入版本：3.60.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

粒子处理器的y坐标,在世界空间。


> 源码：[src/gameobjects/particles/ParticleProcessor.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleProcessor.js#L57)  
引入版本：3.60.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

删除所有外部引用, 从而销毁此粒子处理器。

当拥有的粒子 Emitter 被销毁时,此名称会自动被称作 。


> 源码：[src/gameobjects/particles/ParticleProcessor.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleProcessor.js#L96)  
引入版本：3.60.0


---

### update {#update}

#### \<instance> update(particle, delta, step, t) {#instance-updateparticle-delta-step-t}


**说明:**

粒子处理器更新方法应该被你自己的方法所压倒,并处理粒子的处理,一般根据这个处理器的标准修改它们的velocityX/Y值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子要更新。 |
| delta | number | 否 | 三角洲时间以ms计. |
| step | number | 否 | 三角洲值除以1000. |
| t | number | 否 | 目前粒子的正常寿命,在0(出生)至1(死亡)之间. |


> 源码：[src/gameobjects/particles/ParticleProcessor.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleProcessor.js#L79)  
引入版本：3.60.0


---

---
