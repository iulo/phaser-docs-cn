# DeathZone {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-zones-deathzone)

一个死亡地带。

死亡区是一类特殊类型的区域,它一进入或离开该区,就会杀死一颗粒子.

区由`source`组成,它可以是几何形状,如矩形或椭圆形,或者你自己的物体,只要它包括`contains`方法,可以用来测试粒子。

**构造函数**

`new DeathZone(source, killOnEnter)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Types.GameObjects.Particles.DeathZoneSource](/api/typedef/types-gameobjects-particles#deathzonesource) | 否 | 一个具有`contains`方法的物体实例,当给定`x`和`y`参数时,它返回布尔值。 |
| killOnEnter | boolean | 否 | 粒子进入区域时是应该杀死它? `true`还是离开它? `false` |

---


**作用域**: static

> 源码：[src/gameobjects/particles/zones/DeathZone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/DeathZone.js#L9)  
引入版本：3.0.0

## 公开成员 {#public-members}

### killOnEnter {#killOnEnter}

#### killOnEnter: boolean {#killonenter-boolean}


**说明:**

如果粒子进入此区域, 则设定为 `true` 。 如果粒子离开此区域, 设定为 `false` 。


> 源码：[src/gameobjects/particles/zones/DeathZone.js#L42](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/DeathZone.js#L42)  
引入版本：3.0.0


---

### source {#source}

#### source: [Phaser.Types.GameObjects.Particles.DeathZoneSource](/api/typedef/types-gameobjects-particles#deathzonesource) {#source-phasertypesgameobjectsparticlesdeathzonesource}


**说明:**

对象实例具有 `contains` 方法,在给定 `x` 和 `y` 参数时返回布尔值。这可能是几何形状, 如 `Phaser.Geom.Circle` , 或您自己的自定义对象 。


> 源码：[src/gameobjects/particles/zones/DeathZone.js#L32](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/DeathZone.js#L32)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### willKill {#willKill}

#### \<instance> willKill(particle) {#instance-willkillparticle}


**说明:**

检查给定的粒子是否会被此区所杀 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 用来测试死亡区的粒子 |


**返回值:** boolean - 如果要杀死粒子,则返回`true`,否则返回`false`.


> 源码：[src/gameobjects/particles/zones/DeathZone.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/DeathZone.js#L53)  
引入版本：3.0.0


---

---
