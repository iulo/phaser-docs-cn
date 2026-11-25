# GameObjects.Particles.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/gameobjects-particles-events)

## COMPLETE {#complete}


**说明:** 粒子发射事件

当颗粒发射出最后颗粒时, 发送此事件。
已停止, 死亡。 接到事件后, 您就知道没有粒子存在
还在此时此刻进行渲染

利用`ParticleEmitter.on('complete', listener)`在粒子喷射物中听

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 提到刚刚完成的粒子喷射器 |

**所属:** [Phaser.GameObjects.Particles.Events](/api/namespace/gameobjects-particles-events)
> 源码：[src/gameobjects/particles/events/COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/COMPLETE_EVENT.js#L7)  
引入版本：3.60.0

## DEATH_ZONE {#death_zone}


**说明:** 粒子喷射死亡区事件。

死亡区杀死粒子时, 就会发出这个事件。

利用`ParticleEmitter.on('deathzone', listener)`在粒子喷射物中听

如果你想知道最后颗粒何时被杀死,请参见`COMPLETE`事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 指拥有粒子和死亡区的粒子喷射器 |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 被杀死的粒子 |
| zone | [Phaser.GameObjects.Particles.Zones.DeathZone](/api/class/gameobjects-particles-zones-deathzone) | 否 | 杀死粒子的死亡区 |

**所属:** [Phaser.GameObjects.Particles.Events](/api/namespace/gameobjects-particles-events)
> 源码：[src/gameobjects/particles/events/DEATH_ZONE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/DEATH_ZONE_EVENT.js#L7)  
引入版本：3.60.0

## EXPLODE {#explode}


**说明:** 粒子喷发事件。

当粒子 Emitter 爆炸一组粒子时, 就会发出此事件 。

利用`ParticleEmitter.on('explode', listener)`在粒子喷射物中听

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 提到刚刚完成的粒子喷射器 |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 最近排放的粒子。 |

**所属:** [Phaser.GameObjects.Particles.Events](/api/namespace/gameobjects-particles-events)
> 源码：[src/gameobjects/particles/events/EXPLODE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/EXPLODE_EVENT.js#L7)  
引入版本：3.60.0

## START {#start}


**说明:** 粒子喷射启动事件 。

当粒子发射物开始排放粒子时,便发出此事件。

利用`ParticleEmitter.on('start', listener)`在粒子喷射物中听

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 提到刚刚完成的粒子喷射器 |

**所属:** [Phaser.GameObjects.Particles.Events](/api/namespace/gameobjects-particles-events)
> 源码：[src/gameobjects/particles/events/START_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/START_EVENT.js#L7)  
引入版本：3.60.0

## STOP {#stop}


**说明:** 粒子喷射器停止事件 。

当粒子 Emitter 停止时, 发送此事件。 也可以发生 。
直接调用 `ParticleEmitter.stop` 方法时,或者如果发射器有
配置后,通过 `duration` 属性设定时间后停止,或经过 a
通过 `stopAfter` 属性设定粒子数。

利用`ParticleEmitter.on('stop', listener)`在粒子喷射物中听

注意,只是因为发射器停止了, 这并不意味着没有
粒子活化和渲染,只是表示发射者停止了微粒的释放.

如果你想知道最后颗粒何时被杀死,请参见`COMPLETE`事件.

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 提到刚刚完成的粒子喷射器 |

**所属:** [Phaser.GameObjects.Particles.Events](/api/namespace/gameobjects-particles-events)
> 源码：[src/gameobjects/particles/events/STOP_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/events/STOP_EVENT.js#L7)  
引入版本：3.60.0

---
