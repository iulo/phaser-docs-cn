# ParticleBounds {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-particlebounds)

粒子束处理器

定义一个矩形区域,在世界空间中,粒子运动在其中受到限制.

利用特性`collideLeft`,`collideRight`,`collideTop`和`collideBottom`来控制一个粒子是否会从边界的一侧反弹,或者不是.

当粒子worldPosition x/y坐标击中边界时,就会发生这种情况.

反弹的强度由`Particle.bounce`属性决定.

**构造函数**

`new ParticleBounds(x, y, width, height, [collideLeft], [collideRight], [collideTop], [collideBottom])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 界界的x位置(左上),在世界空间. |
| y | number | 否 |  | 界界的y位置(左上),在世界空间. |
| width | number | 否 |  | 界之宽. |
| height | number | 否 |  | 界之高处. |
| collideLeft | boolean | 是 | true | 粒子是否与边界的左边缘相互作用 。 |
| collideRight | boolean | 是 | true | 粒子是否与边界的右边缘相互作用 。 |
| collideTop | boolean | 是 | true | 粒子是否与边界的顶端相互作用 。 |
| collideBottom | boolean | 是 | true | 粒子是否与边界的底边相互作用 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor)  



> 源码：[src/gameobjects/particles/ParticleBounds.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleBounds.js#L11)  
引入版本：3.60.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor):**


 - [active](/api/class/gameobjects-particles-particleprocessor#active)
 - [emitter](/api/class/gameobjects-particles-particleprocessor#emitter)
 - [x](/api/class/gameobjects-particles-particleprocessor#x)
 - [y](/api/class/gameobjects-particles-particleprocessor#y)




---

## 公开成员 {#public-members}

### bounds {#bounds}

#### bounds: [Phaser.Geom.Rectangle](/api/class/geom-rectangle) {#bounds-phasergeomrectangle}


**说明:**

矩形边界限制粒子运动。 使用粒子边界属性`collideLeft`、`collideRight`、`collideTop`和`collideBottom`来控制粒子是否从边界的一侧反弹。 当粒子x/y坐标击中边界时, 就会发生这种情况 。


> 源码：[src/gameobjects/particles/ParticleBounds.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleBounds.js#L56)  
引入版本：3.60.0


---

### collideBottom {#collideBottom}

#### collideBottom: boolean {#collidebottom-boolean}


**说明:**

粒子是否与发射器[Phaser.GameObjects.Particles.ParticleBounds#bounds](/api/class/gameobjects-particles-particlebounds#bounds)的底端边缘相互作用.


> 源码：[src/gameobjects/particles/ParticleBounds.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleBounds.js#L98)  
引入版本：3.60.0


---

### collideLeft {#collideLeft}

#### collideLeft: boolean {#collideleft-boolean}


**说明:**

粒子是否与 [Phaser.GameObjects.Particles.ParticleBounds#bounds](/api/class/gameobjects-particles-particlebounds#bounds) 的左边缘相互作用 。


> 源码：[src/gameobjects/particles/ParticleBounds.js#L68](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleBounds.js#L68)  
引入版本：3.60.0


---

### collideRight {#collideRight}

#### collideRight: boolean {#collideright-boolean}


**说明:**

粒子是否与发射器[Phaser.GameObjects.Particles.ParticleBounds#bounds](/api/class/gameobjects-particles-particlebounds#bounds)的右边缘相互作用.


> 源码：[src/gameobjects/particles/ParticleBounds.js#L78](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleBounds.js#L78)  
引入版本：3.60.0


---

### collideTop {#collideTop}

#### collideTop: boolean {#collidetop-boolean}


**说明:**

粒子是否与发射器[Phaser.GameObjects.Particles.ParticleBounds#bounds](/api/class/gameobjects-particles-particlebounds#bounds)的顶端相互作用.


> 源码：[src/gameobjects/particles/ParticleBounds.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleBounds.js#L88)  
引入版本：3.60.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.GameObjects.Particles.ParticleProcessor](/api/class/gameobjects-particles-particleprocessor):**


 - [destroy](/api/class/gameobjects-particles-particleprocessor#destroy)




---

## 公开方法 {#public-methods}

### update {#update}

#### \<instance> update(particle) {#instance-updateparticle}


**说明:**

对照边界矩检查给定的粒子。如果粒子的世界位置越过一个活动边缘,则其位置被夹在边界内,其沿该轴的速度被粒子的`bounce`值抵消和缩放,使其反弹。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子要更新。 |


**重写:** Phaser.GameObjects.Particles.ParticleProcessor#更新日期


> 源码：[src/gameobjects/particles/ParticleBounds.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/ParticleBounds.js#L109)  
引入版本：3.0.0


---

---
