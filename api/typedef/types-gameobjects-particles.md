# Types.GameObjects.Particles {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-particles)

## DeathZoneObject {#deathzoneobject}

### \<static> DeathZoneObject {#static-deathzoneobject}

**类型**: [Phaser.GameObjects.Particles.Zones.DeathZone](/api/class/gameobjects-particles-zones-deathzone) | [Phaser.Types.GameObjects.Particles.ParticleEmitterDeathZoneConfig](/api/typedef/types-gameobjects-particles#particleemitterdeathzoneconfig) | [Phaser.Types.GameObjects.Particles.DeathZoneSource](/api/typedef/types-gameobjects-particles#deathzonesource)

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/DeathZoneObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/DeathZoneObject.js#L1)  
引入版本：3.60.0

---

## DeathZoneSource {#deathzonesource}

### \<static> DeathZoneSource {#static-deathzonesource}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| contains | [Phaser.Types.GameObjects.Particles.DeathZoneSourceCallback](/api/typedef/types-gameobjects-particles#deathzonesourcecallback) | 否 | 未提供说明 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/DeathZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/DeathZoneSource.js#L1)  
引入版本：3.0.0

---

## DeathZoneSourceCallback {#deathzonesourcecallback}

### \<static> DeathZoneSourceCallback {#static-deathzonesourcecallback}

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/DeathZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/DeathZoneSourceCallback.js#L1)  
引入版本：3.0.0

---

## EdgeZoneSource {#edgezonesource}

### \<static> EdgeZoneSource {#static-edgezonesource}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| getPoints | [Phaser.Types.GameObjects.Particles.EdgeZoneSourceCallback](/api/typedef/types-gameobjects-particles#edgezonesourcecallback) | 否 | 函数将点放置在源边或边上。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EdgeZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EdgeZoneSource.js#L1)  
引入版本：3.0.0

---

## EdgeZoneSourceCallback {#edgezonesourcecallback}

### \<static> EdgeZoneSourceCallback {#static-edgezonesourcecallback}

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EdgeZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EdgeZoneSourceCallback.js#L1)  
引入版本：3.0.0

---

## EmitterOpCustomEmitConfig {#emitteropcustomemitconfig}

### \<static> EmitterOpCustomEmitConfig {#static-emitteropcustomemitconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| onEmit | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitCallback](/api/typedef/types-gameobjects-particles#emitteroponemitcallback) | 否 | 每次发射发射粒子时都会被引用的回调. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpCustomEmitConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpCustomEmitConfig.js#L1)  
引入版本：3.0.0

---

## EmitterOpCustomUpdateConfig {#emitteropcustomupdateconfig}

### \<static> EmitterOpCustomUpdateConfig {#static-emitteropcustomupdateconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| onEmit | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitCallback](/api/typedef/types-gameobjects-particles#emitteroponemitcallback) | 是 | 每次发射发射粒子时都会被引用的回调. |
| onUpdate | [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateCallback](/api/typedef/types-gameobjects-particles#emitteroponupdatecallback) | 否 | 一次每次发送器更新时都会引用的回调 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpCustomUpdateConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpCustomUpdateConfig.js#L1)  
引入版本：3.0.0

---

## EmitterOpEaseConfig {#emitteropeaseconfig}

### \<static> EmitterOpEaseConfig {#static-emitteropeaseconfig}


定义一个能产生一个跨区域连续递增值的操作。

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| start | number | 否 |  | 初标值. |
| end | number | 否 |  | 终极值. |
| random | boolean | 是 |  | 如果真,粒子在起始值和结束值之间以最小的随机值开始. |
| ease | string \| function | 是 | "'Linear'" | 容易找到。 这可以是 EaseMap 的字符串, 也可以是自定义函数 。 |
| easeParams | Array.\<number> | 是 |  | 随易的可选的易解参数组. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpEaseConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpEaseConfig.js#L1)  
引入版本：3.0.0

---

## EmitterOpInterpolationConfig {#emitteropinterpolationconfig}

### \<static> EmitterOpInterpolationConfig {#static-emitteropinterpolationconfig}


定义一个在插值数据集中持续递增的操作。

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| values | Array.\<number> | 否 |  | 要插入的数字值的数组。 |
| interpolation | string \| function | 是 | "'Linear'" | 插值函数。 通常为 `linear` 、 `bezier` 或 `catmull` 或自定义函数 。 |
| ease | string \| function | 是 | "'Linear'" | 要使用的可选易用功能。 这可以是 EaseMap 的字符串, 也可以是自定义的功能 。 |
| easeParams | Array.\<number> | 是 |  | 随易的可选的易解参数组. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpInterpolationConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpInterpolationConfig.js#L1)  
引入版本：3.60.0

---

## EmitterOpOnEmitCallback {#emitteroponemitcallback}

### \<static> EmitterOpOnEmitCallback {#static-emitteroponemitcallback}


返回的值设定了粒子生命中的财产,即发射时的财产。

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpOnEmitCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpOnEmitCallback.js#L1)  
引入版本：3.0.0

---

## EmitterOpOnEmitType {#emitteroponemittype}

### \<static> EmitterOpOnEmitType {#static-emitteroponemittype}

**类型**: number | Array.\<number> | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitCallback](/api/typedef/types-gameobjects-particles#emitteroponemitcallback) | [Phaser.Types.GameObjects.Particles.EmitterOpRandomConfig](/api/typedef/types-gameobjects-particles#emitteroprandomconfig) | [Phaser.Types.GameObjects.Particles.EmitterOpRandomMinMaxConfig](/api/typedef/types-gameobjects-particles#emitteroprandomminmaxconfig) | [Phaser.Types.GameObjects.Particles.EmitterOpSteppedConfig](/api/typedef/types-gameobjects-particles#emitteropsteppedconfig) | [Phaser.Types.GameObjects.Particles.EmitterOpCustomEmitConfig](/api/typedef/types-gameobjects-particles#emitteropcustomemitconfig)

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpOnEmitType.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpOnEmitType.js#L1)  
引入版本：3.18.0

---

## EmitterOpOnUpdateCallback {#emitteroponupdatecallback}

### \<static> EmitterOpOnUpdateCallback {#static-emitteroponupdatecallback}


返回值更新了粒子寿命期间的属性.

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpOnUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpOnUpdateCallback.js#L1)  
引入版本：3.0.0

---

## EmitterOpOnUpdateType {#emitteroponupdatetype}

### \<static> EmitterOpOnUpdateType {#static-emitteroponupdatetype}

**类型**: [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateCallback](/api/typedef/types-gameobjects-particles#emitteroponupdatecallback) | [Phaser.Types.GameObjects.Particles.EmitterOpEaseConfig](/api/typedef/types-gameobjects-particles#emitteropeaseconfig) | [Phaser.Types.GameObjects.Particles.EmitterOpCustomUpdateConfig](/api/typedef/types-gameobjects-particles#emitteropcustomupdateconfig) | [Phaser.Types.GameObjects.Particles.EmitterOpInterpolationConfig](/api/typedef/types-gameobjects-particles#emitteropinterpolationconfig)

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpOnUpdateType.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpOnUpdateType.js#L1)  
引入版本：3.18.0

---

## EmitterOpRandomConfig {#emitteroprandomconfig}

### \<static> EmitterOpRandomConfig {#static-emitteroprandomconfig}


定义在一定范围内产生随机值的操作。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| random | Array.\<number> | 否 | 最小值和最大值,作为[min, 最大值]。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpRandomConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpRandomConfig.js#L1)  
引入版本：3.0.0

---

## EmitterOpRandomMinMaxConfig {#emitteroprandomminmaxconfig}

### \<static> EmitterOpRandomMinMaxConfig {#static-emitteroprandomminmaxconfig}


定义在一定范围内产生随机值的操作。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 最低值。 。 |
| max | number | 否 | 最大值( 最大值 ) 。 |
| int | boolean | 是 | 如果选中真, 则只选择该范围的整数 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpRandomMinMaxConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpRandomMinMaxConfig.js#L1)  
引入版本：3.0.0

---

## EmitterOpSteppedConfig {#emitteropsteppedconfig}

### \<static> EmitterOpSteppedConfig {#static-emitteropsteppedconfig}


定义一个通过跨区域步骤递增的操作。

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| start | number | 否 | 初标值. |
| end | number | 否 | 终极值. |
| steps | number | 否 | 起止间步数. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitterOpSteppedConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitterOpSteppedConfig.js#L1)  
引入版本：3.0.0

---

## EmitZoneData {#emitzonedata}

### \<static> EmitZoneData {#static-emitzonedata}

**类型**: [Phaser.Types.GameObjects.Particles.ParticleEmitterEdgeZoneConfig](/api/typedef/types-gameobjects-particles#particleemitteredgezoneconfig) | [Phaser.Types.GameObjects.Particles.ParticleEmitterRandomZoneConfig](/api/typedef/types-gameobjects-particles#particleemitterrandomzoneconfig) | [Phaser.GameObjects.Particles.Zones.EdgeZone](/api/class/gameobjects-particles-zones-edgezone) | [Phaser.GameObjects.Particles.Zones.RandomZone](/api/class/gameobjects-particles-zones-randomzone)

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitZoneData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitZoneData.js#L1)  
引入版本：3.60.0

---

## EmitZoneObject {#emitzoneobject}

### \<static> EmitZoneObject {#static-emitzoneobject}

**类型**: [Phaser.GameObjects.Particles.Zones.EdgeZone](/api/class/gameobjects-particles-zones-edgezone) | [Phaser.GameObjects.Particles.Zones.RandomZone](/api/class/gameobjects-particles-zones-randomzone)

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/EmitZoneObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/EmitZoneObject.js#L1)  
引入版本：3.60.0

---

## GravityWellConfig {#gravitywellconfig}

### \<static> GravityWellConfig {#static-gravitywellconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 引力井的x坐标,在世界空间。 |
| y | number | 是 | 0 | 引力井的Y坐标,在世界空间。 |
| power | number | 是 | 0 | 重力的强度 - 数量较多产生更强大的力. |
| epsilon | number | 是 | 100 | 计算重力的最小距离。 |
| gravity | number | 是 | 50 | 引力力 引力井。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/GravityWellConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/GravityWellConfig.js#L1)  
引入版本：3.0.0

---

## ParticleClassConstructor {#particleclassconstructor}

### \<static> ParticleClassConstructor {#static-particleclassconstructor}

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleClassConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleClassConstructor.js#L1)  
引入版本：3.0.0

---

## ParticleData {#particledata}

### \<static> ParticleData {#static-particledata}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| tint | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0xffffff,max:0xffffff}" | 未提供说明 |
| alpha | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:1,max:1}" | 未提供说明 |
| rotate | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| scaleX | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:1,max:1}" | 未提供说明 |
| scaleY | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:1,max:1}" | 未提供说明 |
| x | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| y | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| accelerationX | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| accelerationY | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| maxVelocityX | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| maxVelocityY | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| moveToX | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| moveToY | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |
| bounce | [Phaser.Types.GameObjects.Particles.ParticleDataValue](/api/typedef/types-gameobjects-particles#particledatavalue) | 是 | "{min:0,max:0}" | 未提供说明 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleData.js#L1)  
引入版本：3.60.0

---

## ParticleDataValue {#particledatavalue}

### \<static> ParticleDataValue {#static-particledatavalue}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 最低值。 。 |
| max | number | 否 | 最大值( 最大值 ) 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleDataValue.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleDataValue.js#L1)  
引入版本：3.60.0

---

## ParticleDeathCallback {#particledeathcallback}

### \<static> ParticleDeathCallback {#static-particledeathcallback}

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleDeathCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleDeathCallback.js#L1)  
引入版本：3.0.0

---

## ParticleEmitterAnimConfig {#particleemitteranimconfig}

### \<static> ParticleEmitterAnimConfig {#static-particleemitteranimconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| anims | string \| Array.\<string> | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | Array.\<[Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig)> | 是 |  | 一个或多个动画名称,或播放动画配置对象. |
| cycle | boolean | 是 | false | 动画是连续(真)还是随机(假)分配. |
| quantity | number | 是 | 1 | 连续接收每部动画的粒子数, 当 `cycle` 是真的. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterAnimConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterAnimConfig.js#L1)  
引入版本：3.60.0

---

## ParticleEmitterBounds {#particleemitterbounds}

### \<static> ParticleEmitterBounds {#static-particleemitterbounds}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 矩形的左边缘. |
| y | number | 否 | 矩形顶端边缘. |
| width | number | 否 | 矩形的宽度 。 |
| height | number | 否 | 长方形的高度. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterBounds.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterBounds.js#L1)  
引入版本：3.0.0

---

## ParticleEmitterBoundsAlt {#particleemitterboundsalt}

### \<static> ParticleEmitterBoundsAlt {#static-particleemitterboundsalt}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 矩形的左边缘. |
| y | number | 否 | 矩形顶端边缘. |
| w | number | 否 | 矩形的宽度 。 |
| h | number | 否 | 长方形的高度. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterBoundsAlt.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterBoundsAlt.js#L1)  
引入版本：3.0.0

---

## ParticleEmitterCallback {#particleemittercallback}

### \<static> ParticleEmitterCallback {#static-particleemittercallback}

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterCallback.js#L1)  
引入版本：3.0.0

---

## ParticleEmitterConfig {#particleemitterconfig}

### \<static> ParticleEmitterConfig {#static-particleemitterconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| active | boolean | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#Active}。 设置此选项会阻止发射者运行。 如果您只是想阻止粒子的释放, 请设定 `emitting` 属性。 |
| blendMode | [Phaser.BlendModes](/api/namespace/blendmodes) \| string | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#blendMode}. |
| callbackScope | * | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#deathCallbackScope和 \\ n链接 Phaser.GameObjects.Particles.ParticleEmitter#emitCallbackScope}. |
| collideBottom | boolean | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#collideBottom}. |
| collideLeft | boolean | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#collideLeft}. |
| collideRight | boolean | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#collideRight}. |
| collideTop | boolean | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#collideTop}. |
| deathCallback | function | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#deathCallback}. |
| deathCallbackScope | * | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#deathCallbackScope}. |
| emitCallback | function | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#emitCallback}. |
| emitCallbackScope | * | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#emitCallbackScope}. |
| follow | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 设定QQLink Phaser.GameObjects.Particles.ParticleEmitter#Follow}. |
| frequency | number | 是 | 设定QQLink Phaser.GameObjects.Particles.ParticleEmitter#频率]. |
| gravityX | number | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#gravityX}. |
| gravityY | number | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#gravityY}. |
| maxParticles | number | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#maxParticles}. |
| maxAliveParticles | number | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#maxAliveParticles}. |
| 名称 | string | 是 | 设置 QQLink Phaser.GameObjects.Particles.ParticleEmitter#name}. |
| emitting | boolean | 是 | 设定 QQLINK Phaser.GameObjects.Particles.ParticleEmitter# 排放 。 |
| particleBringToTop | boolean | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleBringToTop}. |
| particleClass | function | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleClass}. |
| radial | boolean | 是 | 设定 QQLINK Phaser.GameObjects.Particles.ParticleEmitter#射线]. |
| timeScale | number | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#timeScale}. |
| trackVisible | boolean | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#trackVisible}. |
| visible | boolean | 是 | 设定为 QQLink Phaser.GameObjects.Particles.ParticleEmitter# 隐形 。 |
| accelerationX | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#accelerationX}. |
| accelerationY | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#accelerationY}. |
| alpha | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleAlpha}. |
| angle | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 设置 QQLINK Phaser.GameObjects.Particles.ParticleEmitter#particleAngle} (仅限密电). |
| bounce | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设定 QQLINK Phaser.GameObjects.Particles.ParticleEmitter#bounce }. |
| delay | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 设置 QQLink Phaser.GameObjects.Particles.ParticleEmitter#延时 } (仅限密电). |
| hold | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 设置 QQLink Phaser.GameObjects.Particles.ParticleEmitter#hold } (仅限密电). |
| lifespan | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 设置 QQLink Phaser.GameObjects.Particles.ParticleEmitter#lishspan} (仅限微米). |
| maxVelocityX | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#maxVelocityX}. |
| maxVelocityY | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#maxVelocityY}. |
| moveToX | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#moveToX} 如果设置, 将覆盖 `angle` 财务报告和已审计财务报表 `speed` 属性。 |
| moveToY | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#moveToY} 如果设置, 将覆盖 `angle` 财务报告和已审计财务报表 `speed` 属性。 |
| quantity | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 设置 QQLink Phaser.GameObjects.Particles.ParticleEmitter# 数量 } (仅限 ). |
| rotate | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleRotate}. |
| scale | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 和Phaser.GameObjects.Particles.ParticleEmitter#setScale}一样 |
| scaleX | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleScaleX}. |
| scaleY | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleScaleY}. |
| speed | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 以QQLINK Phaser.GameObjects.Particles.ParticleEmitter#setSpeed}(仅限微量). |
| speedX | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 设置 QQLINK Phaser.GameObjects.Particles.ParticleEmitter#speedX} (仅限密电). |
| speedY | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) | 是 | 设置 QQLINK Phaser.GameObjects.Particles.ParticleEmitter#speedY} (仅限密电). |
| tint | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleTint}. |
| color | Array.\<number> | 是 | 粒子在生命中插入的颜色值。如果设定,则覆盖任何 `tint` 属性。 |
| colorEase | string | 是 | 如果您已经通过 `color` 属性启用粒子颜色插值, 则 Easing 函数的字符串名称将使用, 否则将无效果 。 |
| x | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleX}. |
| y | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](/api/typedef/types-gameobjects-particles#emitteroponemittype) \| [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](/api/typedef/types-gameobjects-particles#emitteroponupdatetype) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#particleY}. |
| emitZone | [Phaser.Types.GameObjects.Particles.EmitZoneData](/api/typedef/types-gameobjects-particles#emitzonedata) \| Array.\<[Phaser.Types.GameObjects.Particles.EmitZoneData](/api/typedef/types-gameobjects-particles#emitzonedata)> | 是 | 和Phaser.GameObjects.Particles.ParticleEmitter#setEmitZone}一样 |
| deathZone | [Phaser.Types.GameObjects.Particles.DeathZoneObject](/api/typedef/types-gameobjects-particles#deathzoneobject) \| Array.\<[Phaser.Types.GameObjects.Particles.DeathZoneObject](/api/typedef/types-gameobjects-particles#deathzoneobject)> | 是 | 和Phaser.GameObjects.Particles.ParticleEmitter#setDeathZone}一样 |
| bounds | [Phaser.Types.GameObjects.Particles.ParticleEmitterBounds](/api/typedef/types-gameobjects-particles#particleemitterbounds) \| [Phaser.Types.GameObjects.Particles.ParticleEmitterBoundsAlt](/api/typedef/types-gameobjects-particles#particleemitterboundsalt) | 是 | 和Phaser.GameObjects.Particles.ParticleEmitter#setBounds}一样 |
| followOffset | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 坐标偏移,指定给QQlink Phaser.GameObjects.Particles.ParticleEmitter#followOffset}。 |
| anim | string \| Array.\<string> | [Phaser.Types.GameObjects.Particles.ParticleEmitterAnimConfig](/api/typedef/types-gameobjects-particles#particleemitteranimconfig) | 是 | 设定为 QQLINK Phaser.GameObjects.Particles.ParticleEmitter#anims}. |
| frame | number \| Array.\<number> | string | Array.\<string> | [Phaser.Textures.Frame](/api/class/textures-frame) | Array.\<[Phaser.Textures.Frame](/api/class/textures-frame)> | [Phaser.Types.GameObjects.Particles.ParticleEmitterFrameConfig](/api/typedef/types-gameobjects-particles#particleemitterframeconfig) | 是 | 设定 QQLINK Phaser.GameObjects.Particles.ParticleEmitter#帧 。 |
| texture | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter# 纹理} 覆盖 Emitter 上已经设置的任何纹理 。 |
| reserve | number | 是 | 创建指定的不活动粒子数量, 并添加到此发射器的池中 。 @ @ link Phaser.GameObjects.Particles.ParticleEmitter# reserve} |
| advance | number | 是 | 如果您想要及时“ 快速转发” , 请将这个值设定为代表 发送器应前进 ms 的数。 这样就将 `emitting` 默认为 `true` 。 |
| duration | number | 是 | 限制发射器释放粒子, 最大为 `duration` ms。 默认为零, 意思是“ 永远” 。 |
| stopAfter | number | 是 | 限制发射器释放出这个精确的粒子数然后停止。默认为零, 表示没有限制 。 |
| sortCallback | [Phaser.Types.GameObjects.Particles.ParticleSortCallback](/api/typedef/types-gameobjects-particles#particlesortcallback) | 是 | 渲染前的调用。 设置 QQlink Phaser.GameObjects.Particles.ParticleEmitter# sortCallback} 。 |
| sortOrderAsc | boolean | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#sortOrderAsc}. |
| sortProperty | string | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#sortProperty}. |
| tintMode | [Phaser.TintModes](/api/namespace/tintmodes) | 是 | 设置 QQlink 选项 Phaser.GameObjects.Particles.ParticleEmitter#tintMode}. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterConfig.js#L1)  
引入版本：3.0.0

---

## ParticleEmitterCreatorConfig {#particleemittercreatorconfig}

### \<static> ParticleEmitterCreatorConfig {#static-particleemittercreatorconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 是 | 用于渲染粒子的纹理键, 如存储在纹理管理器中 。 |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](/api/typedef/types-gameobjects-particles#particleemitterconfig) | 是 | Patient 报盘配置对象 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterCreatorConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterCreatorConfig.js#L1)  
引入版本：3.60.0

---

## ParticleEmitterDeathZoneConfig {#particleemitterdeathzoneconfig}

### \<static> ParticleEmitterDeathZoneConfig {#static-particleemitterdeathzoneconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| source | [Phaser.Types.GameObjects.Particles.DeathZoneSource](/api/typedef/types-gameobjects-particles#deathzonesource) | 否 |  | 代表区块的形状。 请见 XQLink Phaser.GameObjects.Particles.Zones.DeathZone# source}. |
| 类型 | string | 是 | "'onEnter'" | "onEnter"或"onLeave". |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterDeathZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterDeathZoneConfig.js#L1)  
引入版本：3.0.0

---

## ParticleEmitterEdgeZoneConfig {#particleemitteredgezoneconfig}

### \<static> ParticleEmitterEdgeZoneConfig {#static-particleemitteredgezoneconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| source | [Phaser.Types.GameObjects.Particles.EdgeZoneSource](/api/typedef/types-gameobjects-particles#edgezonesource) | 否 |  | 代表区块的形状。 请见 XQLink Phaser.GameObjects.Particles.Zones.EdgeZone# source}. |
| 类型 | string | 否 |  | 尖端的。 |
| quantity | number | 否 |  | 将粒子数放置在源边上。 设定为 0 , 改为使用 `stepRate` 。 |
| stepRate | number | 是 |  | 每个粒子之间的距离。 设定时, `quantity` 表示并设定为 0 。 |
| yoyo | boolean | 是 | false | 粒子是否从始至终被放置,然后从始至终被放置. |
| seamless | boolean | 是 | true | 如果一个终点与另一个终点完全相同,是否将去除. |
| total | number | 是 | 1 | 这个区块的总数在传递到埃米特的下一个排放区之前将会喷出. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterEdgeZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterEdgeZoneConfig.js#L1)  
引入版本：3.0.0

---

## ParticleEmitterFrameConfig {#particleemitterframeconfig}

### \<static> ParticleEmitterFrameConfig {#static-particleemitterframeconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| frames | Array.\<number> \| Array.\<string> | Array.\<[Phaser.Textures.Frame](/api/class/textures-frame)> | 是 | 纹理框架的组合 。 |
| cycle | boolean | 是 | 纹理框架是连续(真)还是随机(假)指定. |
| quantity | number | 是 | 接收每个纹理框架的连续粒子数, 当 `cycle` 属实 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterFrameConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterFrameConfig.js#L1)  
引入版本：3.0.0

---

## ParticleEmitterOps {#particleemitterops}

### \<static> ParticleEmitterOps {#static-particleemitterops}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| accelerationX | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | accelerationX 喷雾器实例。这是 onEmit 和 onUpdate 的操作程序 。 |
| accelerationY | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | accelerationY 喷雾器实例。这是 onEmit 和 onUpdate 的操作程序 。 |
| alpha | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | α EmitterOp 实例。 这是 onEmit 和 onUpdate 的操作程序 。 |
| angle | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | 角度 EmitterOp 实例。 这只是一个 onEmit 操作程序 。 |
| bounce | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | 弹跳EmitterOp 实例。 这是 onEmit 和 onUpdate 的操作员 。 |
| color | [Phaser.GameObjects.Particles.EmitterColorOp](/api/class/gameobjects-particles-emittercolorop) | 否 | 颜色 EmitterColorOp 实例。 这是 onEmit 和 onUpdate 的操作员 。 |
| delay | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | 延迟 EmitterOp 实例。 仅此为 onEmit 操作程序 。 |
| hold | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | 搁置 EmitterOp 实例。 这只是一个 onEmit 操作程序 。 |
| lifespan | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | 寿命 EmitterOp 实例。 这只是一个 onEmit 操作程序 。 |
| maxVelocityX | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | maxVelocityX 喷雾器实例。这是 onEmit 和 onUpdate 的操作程序 。 |
| maxVelocityY | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | maxVelocityY 喷雾器实例。这是 onEmit 和 onUpdate 的操作程序 。 |
| moveToX | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | moveToX 喷雾器实例。这是 onEmit 和 onUpdate 的操作程序 。 |
| moveToY | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | moveToY 喷雾器实例。这是 onEmit 和 onUpdate 的操作程序 。 |
| quantity | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | 数量 EmitterOp 实例。 这只是一个 onEmit 操作器 。 |
| rotate | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | 旋转 EmitterOp 实例。 这是 onEmit 和 onUpdate 操作员 。 |
| scaleX | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | scaleX 喷雾器实例。这是 onEmit 和 onUpdate 的操作程序 。 |
| scaleY | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | scaleY 喷雾器实例。这是 onEmit 和 onUpdate 的操作程序 。 |
| speedX | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | speedX EmitterOp 实例。 这只是一个 onEmit 操作器 。 |
| speedY | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | speedY EmitterOp 实例。 这只是一个 onEmit 操作器 。 |
| tint | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | 锡式EmitterOp 实例。 这是 onEmit 和 onUpdate 的操作程序 。 |
| x | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | X EmitterOp 实例。 这是 onEmit 和 onUpdate 操作员 。 |
| y | [Phaser.GameObjects.Particles.EmitterOp](/api/class/gameobjects-particles-emitterop) | 否 | y EmitterOp 实例。 这是 onEmit 和 onUpdate 的操作员 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterOps.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterOps.js#L1)  
引入版本：3.60.0

---

## ParticleEmitterRandomZoneConfig {#particleemitterrandomzoneconfig}

### \<static> ParticleEmitterRandomZoneConfig {#static-particleemitterrandomzoneconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Types.GameObjects.Particles.RandomZoneSource](/api/typedef/types-gameobjects-particles#randomzonesource) | 否 | 代表区块的形状。 请见 XQLink Phaser.GameObjects.Particles.Zones.RandomZone# source}. |
| 类型 | string | 是 | 狂妄的风度 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleEmitterRandomZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleEmitterRandomZoneConfig.js#L1)  
引入版本：3.0.0

---

## ParticleSortCallback {#particlesortcallback}

### \<static> ParticleSortCallback {#static-particlesortcallback}

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/ParticleSortCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/ParticleSortCallback.js#L1)  
引入版本：3.60.0

---

## RandomZoneSource {#randomzonesource}

### \<static> RandomZoneSource {#static-randomzonesource}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| getRandomPoint | [Phaser.Types.GameObjects.Particles.RandomZoneSourceCallback](/api/typedef/types-gameobjects-particles#randomzonesourcecallback) | 否 | 一个函数修改其点参数 。 |

**类型**: object

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/RandomZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/RandomZoneSource.js#L1)  
引入版本：3.0.0

---

## RandomZoneSourceCallback {#randomzonesourcecallback}

### \<static> RandomZoneSourceCallback {#static-randomzonesourcecallback}

**类型**: function

**Member of**: Phaser.Types.GameObjects.Particles
> 源码：[src/gameobjects/particles/typedefs/RandomZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/typedefs/RandomZoneSourceCallback.js#L1)  
引入版本：3.0.0

---

---
