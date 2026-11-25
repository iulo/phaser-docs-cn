# Phaser.GameObjects.Particles.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-particles-events)

Scope: 
static
> 源码：[src/gameobjects/particles/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/index.js#L7)  


## 静态函数 {#static-functions}

### COMPLETE {#COMPLETE}

#### COMPLETE {#complete}


**说明:**

粒子发射事件

当被停止的粒子颗粒释放的最后一个粒子死亡时, 就会发出此事件。 接到此事件后, 您就知道, 目前还没有粒子在渲染 。

利用`ParticleEmitter.on('complete', listener)`在粒子喷射物中听

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 提到刚刚完成的粒子喷射器 |


> 源码：[src/gameobjects/particles/events/COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/COMPLETE_EVENT.js#L7)  
引入版本：3.60.0


---

### DEATH_ZONE {#DEATH_ZONE}

#### DEATH_ZONE {#death_zone}


**说明:**

粒子喷射死亡区事件。

死亡区杀死粒子时, 就会发出这个事件。

利用`ParticleEmitter.on('deathzone', listener)`在粒子喷射物中听

如果你想知道最后颗粒何时被杀死,请参见`COMPLETE`事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 指拥有粒子和死亡区的粒子喷射器 |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 被杀死的粒子 |
| zone | [Phaser.GameObjects.Particles.Zones.DeathZone](/api/class/gameobjects-particles-zones-deathzone) | 否 | 杀死粒子的死亡区 |


> 源码：[src/gameobjects/particles/events/DEATH_ZONE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/DEATH_ZONE_EVENT.js#L7)  
引入版本：3.60.0


---

### EXPLODE {#EXPLODE}

#### EXPLODE {#explode}


**说明:**

粒子喷发事件。

当粒子 Emitter 爆炸一组粒子时, 就会发出此事件 。

利用`ParticleEmitter.on('explode', listener)`在粒子喷射物中听

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 提到刚刚完成的粒子喷射器 |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 最近排放的粒子。 |


> 源码：[src/gameobjects/particles/events/EXPLODE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/EXPLODE_EVENT.js#L7)  
引入版本：3.60.0


---

### START {#START}

#### START {#start}


**说明:**

粒子喷射启动事件 。

当粒子发射物开始排放粒子时,便发出此事件。

利用`ParticleEmitter.on('start', listener)`在粒子喷射物中听

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 提到刚刚完成的粒子喷射器 |


> 源码：[src/gameobjects/particles/events/START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/START_EVENT.js#L7)  
引入版本：3.60.0


---

### STOP {#STOP}

#### STOP {#stop}


**说明:**

粒子喷射器停止事件 。

当粒子 Emitter 停止时, 发送此事件。 可能发生于您直接调用 `ParticleEmitter.stop` 方法, 或者在设定时间后通过 `duration` 属性配置该发射器停止, 或者在设定数后通过 `stopAfter` 属性 。

利用`ParticleEmitter.on('stop', listener)`在粒子喷射物中听

注意,只是因为发射器停止了, 这并不意味着没有粒子还活着, 并且产生。它只是意味着发射器停止了发射粒子。

如果你想知道最后颗粒何时被杀死,请参见`COMPLETE`事件.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 提到刚刚完成的粒子喷射器 |


> 源码：[src/gameobjects/particles/events/STOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/STOP_EVENT.js#L7)  
引入版本：3.60.0


---

---
