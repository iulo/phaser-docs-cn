# Phaser.Types.GameObjects.Particles {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/types-gameobjects-particles)

Scope: 
static
> 源码：[src/gameobjects/particles/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/index.js#L7)  


## 静态函数 {#static-functions}

### DeathZoneObject {#DeathZoneObject}

#### DeathZoneObject {#deathzoneobject}


> 源码：[src/gameobjects/particles/typedefs/DeathZoneObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/DeathZoneObject.js#L1)  
引入版本：3.60.0


---

### DeathZoneSource {#DeathZoneSource}

#### DeathZoneSource {#deathzonesource}


> 源码：[src/gameobjects/particles/typedefs/DeathZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/DeathZoneSource.js#L1)  
引入版本：3.0.0


---

### DeathZoneSourceCallback {#DeathZoneSourceCallback}

#### DeathZoneSourceCallback {#deathzonesourcecallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 粒子的x坐标来检查这个源区域. |
| y | number | 否 | 粒子的y坐标以检查此源区域 。 |


**返回值:** boolean - - 如果坐标在源区域之内,那就是真的了


> 源码：[src/gameobjects/particles/typedefs/DeathZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/DeathZoneSourceCallback.js#L1)  
引入版本：3.0.0


---

### EdgeZoneSource {#EdgeZoneSource}

#### EdgeZoneSource {#edgezonesource}


> 源码：[src/gameobjects/particles/typedefs/EdgeZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EdgeZoneSource.js#L1)  
引入版本：3.0.0


---

### EdgeZoneSourceCallback {#EdgeZoneSourceCallback}

#### EdgeZoneSourceCallback {#edgezonesourcecallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| quantity | number | 否 | 将粒子数放置在源边。 如果 0, 则应该使用 `stepRate` 。 |
| stepRate | number | 是 | 每个粒子之间的距离。设定时, `quantity` 表示并设定为 `0` 。 |


**返回值:** Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> - - 源头边缘的点数


> 源码：[src/gameobjects/particles/typedefs/EdgeZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EdgeZoneSourceCallback.js#L1)  
引入版本：3.0.0


---

### EmitterOpCustomEmitConfig {#EmitterOpCustomEmitConfig}

#### EmitterOpCustomEmitConfig {#emitteropcustomemitconfig}


> 源码：[src/gameobjects/particles/typedefs/EmitterOpCustomEmitConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpCustomEmitConfig.js#L1)  
引入版本：3.0.0


---

### EmitterOpCustomUpdateConfig {#EmitterOpCustomUpdateConfig}

#### EmitterOpCustomUpdateConfig {#emitteropcustomupdateconfig}


> 源码：[src/gameobjects/particles/typedefs/EmitterOpCustomUpdateConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpCustomUpdateConfig.js#L1)  
引入版本：3.0.0


---

### EmitterOpEaseConfig {#EmitterOpEaseConfig}

#### EmitterOpEaseConfig {#emitteropeaseconfig}


**说明:**

定义一个能产生一个跨区域连续递增值的操作。


> 源码：[src/gameobjects/particles/typedefs/EmitterOpEaseConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpEaseConfig.js#L1)  
引入版本：3.0.0


---

### EmitterOpInterpolationConfig {#EmitterOpInterpolationConfig}

#### EmitterOpInterpolationConfig {#emitteropinterpolationconfig}


**说明:**

定义一个在插值数据集中持续递增的操作。


> 源码：[src/gameobjects/particles/typedefs/EmitterOpInterpolationConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpInterpolationConfig.js#L1)  
引入版本：3.60.0


---

### EmitterOpOnEmitCallback {#EmitterOpOnEmitCallback}

#### EmitterOpOnEmitCallback {#emitteroponemitcallback}


**说明:**

返回的值设定了粒子生命中的财产,即发射时的财产。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 是 | 粒子 粒子 粒子 粒子 |
| key | string | 是 | 财产名称. |
| value | number | 是 | 财产的当前价值 。 |


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/typedefs/EmitterOpOnEmitCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpOnEmitCallback.js#L1)  
引入版本：3.0.0


---

### EmitterOpOnEmitType {#EmitterOpOnEmitType}

#### EmitterOpOnEmitType {#emitteroponemittype}


> 源码：[src/gameobjects/particles/typedefs/EmitterOpOnEmitType.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpOnEmitType.js#L1)  
引入版本：3.18.0


---

### EmitterOpOnUpdateCallback {#EmitterOpOnUpdateCallback}

#### EmitterOpOnUpdateCallback {#emitteroponupdatecallback}


**说明:**

返回值更新了粒子寿命期间的属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |
| key | string | 否 | 财产名称. |
| t | number | 否 | 粒子的正常寿命,在 0(起始)至 1(结束)之间. |
| value | number | 否 | 财产的当前价值 。 |


**返回值:** number - 地产的新价值.


> 源码：[src/gameobjects/particles/typedefs/EmitterOpOnUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpOnUpdateCallback.js#L1)  
引入版本：3.0.0


---

### EmitterOpOnUpdateType {#EmitterOpOnUpdateType}

#### EmitterOpOnUpdateType {#emitteroponupdatetype}


> 源码：[src/gameobjects/particles/typedefs/EmitterOpOnUpdateType.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpOnUpdateType.js#L1)  
引入版本：3.18.0


---

### EmitterOpRandomConfig {#EmitterOpRandomConfig}

#### EmitterOpRandomConfig {#emitteroprandomconfig}


**说明:**

定义在一定范围内产生随机值的操作。


> 源码：[src/gameobjects/particles/typedefs/EmitterOpRandomConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpRandomConfig.js#L1)  
引入版本：3.0.0


---

### EmitterOpRandomMinMaxConfig {#EmitterOpRandomMinMaxConfig}

#### EmitterOpRandomMinMaxConfig {#emitteroprandomminmaxconfig}


**说明:**

定义在一定范围内产生随机值的操作。


> 源码：[src/gameobjects/particles/typedefs/EmitterOpRandomMinMaxConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpRandomMinMaxConfig.js#L1)  
引入版本：3.0.0


---

### EmitterOpSteppedConfig {#EmitterOpSteppedConfig}

#### EmitterOpSteppedConfig {#emitteropsteppedconfig}


**说明:**

定义一个通过跨区域步骤递增的操作。


> 源码：[src/gameobjects/particles/typedefs/EmitterOpSteppedConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpSteppedConfig.js#L1)  
引入版本：3.0.0


---

### EmitZoneData {#EmitZoneData}

#### EmitZoneData {#emitzonedata}


> 源码：[src/gameobjects/particles/typedefs/EmitZoneData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitZoneData.js#L1)  
引入版本：3.60.0


---

### EmitZoneObject {#EmitZoneObject}

#### EmitZoneObject {#emitzoneobject}


> 源码：[src/gameobjects/particles/typedefs/EmitZoneObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitZoneObject.js#L1)  
引入版本：3.60.0


---

### GravityWellConfig {#GravityWellConfig}

#### GravityWellConfig {#gravitywellconfig}


> 源码：[src/gameobjects/particles/typedefs/GravityWellConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/GravityWellConfig.js#L1)  
引入版本：3.0.0


---

### ParticleClassConstructor {#ParticleClassConstructor}

#### ParticleClassConstructor {#particleclassconstructor}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 本粒子所属的 Emitter 。 |


> 源码：[src/gameobjects/particles/typedefs/ParticleClassConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleClassConstructor.js#L1)  
引入版本：3.0.0


---

### ParticleData {#ParticleData}

#### ParticleData {#particledata}


> 源码：[src/gameobjects/particles/typedefs/ParticleData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleData.js#L1)  
引入版本：3.60.0


---

### ParticleDataValue {#ParticleDataValue}

#### ParticleDataValue {#particledatavalue}


> 源码：[src/gameobjects/particles/typedefs/ParticleDataValue.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleDataValue.js#L1)  
引入版本：3.60.0


---

### ParticleDeathCallback {#ParticleDeathCallback}

#### ParticleDeathCallback {#particledeathcallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 死亡的粒子 死亡的粒子 |


> 源码：[src/gameobjects/particles/typedefs/ParticleDeathCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleDeathCallback.js#L1)  
引入版本：3.0.0


---

### ParticleEmitterAnimConfig {#ParticleEmitterAnimConfig}

#### ParticleEmitterAnimConfig {#particleemitteranimconfig}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterAnimConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterAnimConfig.js#L1)  
引入版本：3.60.0


---

### ParticleEmitterBounds {#ParticleEmitterBounds}

#### ParticleEmitterBounds {#particleemitterbounds}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterBounds.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterBounds.js#L1)  
引入版本：3.0.0


---

### ParticleEmitterBoundsAlt {#ParticleEmitterBoundsAlt}

#### ParticleEmitterBoundsAlt {#particleemitterboundsalt}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterBoundsAlt.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterBoundsAlt.js#L1)  
引入版本：3.0.0


---

### ParticleEmitterCallback {#ParticleEmitterCallback}

#### ParticleEmitterCallback {#particleemittercallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 和呼叫有关的粒子 |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](/api/class/gameobjects-particles-particleemitter) | 否 | 这个粒子发射器与呼叫有关. |


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterCallback.js#L1)  
引入版本：3.0.0


---

### ParticleEmitterConfig {#ParticleEmitterConfig}

#### ParticleEmitterConfig {#particleemitterconfig}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterConfig.js#L1)  
引入版本：3.0.0


---

### ParticleEmitterCreatorConfig {#ParticleEmitterCreatorConfig}

#### ParticleEmitterCreatorConfig {#particleemittercreatorconfig}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterCreatorConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterCreatorConfig.js#L1)  
引入版本：3.60.0


---

### ParticleEmitterDeathZoneConfig {#ParticleEmitterDeathZoneConfig}

#### ParticleEmitterDeathZoneConfig {#particleemitterdeathzoneconfig}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterDeathZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterDeathZoneConfig.js#L1)  
引入版本：3.0.0


---

### ParticleEmitterEdgeZoneConfig {#ParticleEmitterEdgeZoneConfig}

#### ParticleEmitterEdgeZoneConfig {#particleemitteredgezoneconfig}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterEdgeZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterEdgeZoneConfig.js#L1)  
引入版本：3.0.0


---

### ParticleEmitterFrameConfig {#ParticleEmitterFrameConfig}

#### ParticleEmitterFrameConfig {#particleemitterframeconfig}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterFrameConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterFrameConfig.js#L1)  
引入版本：3.0.0


---

### ParticleEmitterOps {#ParticleEmitterOps}

#### ParticleEmitterOps {#particleemitterops}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterOps.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterOps.js#L1)  
引入版本：3.60.0


---

### ParticleEmitterRandomZoneConfig {#ParticleEmitterRandomZoneConfig}

#### ParticleEmitterRandomZoneConfig {#particleemitterrandomzoneconfig}


> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterRandomZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterRandomZoneConfig.js#L1)  
引入版本：3.0.0


---

### ParticleSortCallback {#ParticleSortCallback}

#### ParticleSortCallback {#particlesortcallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 比较了第一个粒子 |
| b | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 第二品相比较. |


> 源码：[src/gameobjects/particles/typedefs/ParticleSortCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleSortCallback.js#L1)  
引入版本：3.60.0


---

### RandomZoneSource {#RandomZoneSource}

#### RandomZoneSource {#randomzonesource}


> 源码：[src/gameobjects/particles/typedefs/RandomZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/RandomZoneSource.js#L1)  
引入版本：3.0.0


---

### RandomZoneSourceCallback {#RandomZoneSourceCallback}

#### RandomZoneSourceCallback {#randomzonesourcecallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 一点要修改。 |


> 源码：[src/gameobjects/particles/typedefs/RandomZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/RandomZoneSourceCallback.js#L1)  
引入版本：3.0.0


---

---
