# RandomZone {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-zones-randomzone)

随机区(Random Zone)是一个将粒子放在形状区域内的随机位置的Emit区,形状必须提供`getRandomPoint`方法,它接收一个矢量2,并从形状的任意位置向它注入随机坐标.

Phaser几何对象如`Phaser.Geom.Rectangle`,`Phaser.Geom.Circle`,`Phaser.Geom.Ellipse`,以及`Phaser.Geom.Triangle`都执行这种方法,可以直接作为这个区的源.

使用这个区域,当您想要粒子在分布在形状内部的随机位置上产卵时。要在形状边缘上产卵粒子,请使用边缘区域。

**构造函数**

`new RandomZone(source)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Types.GameObjects.Particles.RandomZoneSource](/api/typedef/types-gameobjects-particles#randomzonesource) | 否 | 一个具有`getRandomPoint(point)`方法的天体实例. |

---


**作用域**: static

> 源码：[src/gameobjects/particles/zones/RandomZone.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/RandomZone.js#L10)  
引入版本：3.0.0

## 公开成员 {#public-members}

### source {#source}

#### source: [Phaser.Types.GameObjects.Particles.RandomZoneSource](/api/typedef/types-gameobjects-particles#randomzonesource) {#source-phasertypesgameobjectsparticlesrandomzonesource}


**说明:**

一个具有`getRandomPoint(point)`方法的天体实例.


> 源码：[src/gameobjects/particles/zones/RandomZone.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/RandomZone.js#L36)  
引入版本：3.0.0


---

### total {#total}

#### total: number {#total-number}


**说明:**

这一区块的总数将在排放区清单中将控制转移到下一个区之前释放出来。

默认是 - 1 , 也就是说它永远不会从此区域传递到另一个区域。 您可以调用 `ParticleEmitter.setEmitZone` 方法来更改它, 或者通过配置设置此值到其它的值, 或者在运行时直接 。

1的值将意味着区间按顺序旋转,但可以设定为任意整数.


> 源码：[src/gameobjects/particles/zones/RandomZone.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/RandomZone.js#L55)  
引入版本：3.60.0


---

## 公开方法 {#public-methods}

### getPoint {#getPoint}

#### \<instance> getPoint(particle) {#instance-getpointparticle}


**说明:**

获取"区"中的下一个点,并将其坐标设定在给定的粒子上.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |


> 源码：[src/gameobjects/particles/zones/RandomZone.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/RandomZone.js#L74)  
引入版本：3.0.0


---

---
