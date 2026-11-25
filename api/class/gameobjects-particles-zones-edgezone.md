# EdgeZone {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-particles-zones-edgezone)

边缘区域是粒子辐射器的发射区,它依次将发射的粒子置于形状边缘。形状由提供`getPoints(quantity, stepRate)`方法的源对象所定义,例如Phaser曲线、路径或任何相容的几何对象。

每一个粒子都排出后, 它会沿着形状边缘的下一个点定位, 依次循环通过所有点。 如果启用 `yoyo`, 则在到达任一端时, 转盘反向, 产生回向和反向效果。 如果启用 `seamless`, 将移除重复的端点, 以避免在形状循环返回时在连接点堆叠粒子 。

使用这个区域,当您想要粒子追踪或勾画一个形状时——例如,沿着铁丝网运行的火花,绕路径运行的粒子,或者沿着几何图的边界发生的效果.

**构造函数**

`new EdgeZone(source, quantity, [stepRate], [yoyo], [seamless], [total])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| source | [Phaser.Types.GameObjects.Particles.EdgeZoneSource](/api/typedef/types-gameobjects-particles#edgezonesource) | 否 |  | 具有 `getPoints(quantity, stepRate)` 方法的天体实例返回数组点 。 |
| quantity | number | 否 |  | 将粒子数放置在源边上。 设定为 0 , 改为使用 `stepRate` 。 |
| stepRate | number | 是 |  | 每个粒子之间的距离。 设定时, `quantity` 表示并设定为 0 。 |
| yoyo | boolean | 是 | false | 粒子是否从始至终被放置,然后从始至终被放置. |
| seamless | boolean | 是 | true | 如果一个终点与另一个终点完全相同,是否将去除. |
| total | number | 是 | -1 | 这个区域在传递到埃米特的下一个排放区之前, 粒子的总数将会喷出。 - 1 表示它永远不会传递出去, 您必须使用 `setEmitZone`来改变它 。 |

---


**作用域**: static

> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L9)  
引入版本：3.0.0

## 公开成员 {#public-members}

### counter {#counter}

#### counter: number {#counter-number}


**说明:**

用于延展边疆区积分的计数器.


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L94](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L94)  
引入版本：3.0.0


---

### points {#points}

#### points: Array.\<[Phaser.Math.Vector2](/api/class/math-vector2)> {#points-arrayphasermathvector2}


**说明:**

位于源边的点数.


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L57)  
引入版本：3.0.0


---

### quantity {#quantity}

#### quantity: number {#quantity-number}


**说明:**

将粒子数放置在源边上。 设定为 0 , 改为使用 `stepRate` 。


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L67)  
引入版本：3.0.0


---

### seamless {#seamless}

#### seamless: boolean {#seamless-boolean}


**说明:**

如果一个终点与另一个终点完全相同,是否将去除.


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L104)  
引入版本：3.0.0


---

### source {#source}

#### source: [Phaser.Types.GameObjects.Particles.EdgeZoneSource](/api/typedef/types-gameobjects-particles#edgezonesource), [Phaser.Types.GameObjects.Particles.RandomZoneSource](/api/typedef/types-gameobjects-particles#randomzonesource) {#source-phasertypesgameobjectsparticlesedgezonesource-phasertypesgameobjectsparticlesrandomzonesource}


**说明:**

具有 `getPoints(quantity, stepRate)` 方法的天体实例返回数组点 。


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L48](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L48)  
引入版本：3.0.0


---

### stepRate {#stepRate}

#### stepRate: number {#steprate-number}


**说明:**

每个粒子之间的距离。 设定时, `quantity` 表示并设定为 0 。


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L76)  
引入版本：3.0.0


---

### total {#total}

#### total: number {#total-number}


**说明:**

这一区块的总数将在排放区清单中将控制转移到下一个区之前释放出来。

默认是 - 1 , 也就是说它永远不会从此区域传递到另一个区域。 您可以调用 `ParticleEmitter.setEmitZone` 方法来更改它, 或者通过配置设置此值到其它的值, 或者在运行时直接 。

1的值将意味着区间按顺序旋转,但可以设定为任意整数.


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L137)  
引入版本：3.60.0


---

### yoyo {#yoyo}

#### yoyo: boolean {#yoyo-boolean}


**说明:**

粒子是否从始至终被放置,然后从始至终被放置.


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L85)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### changeSource {#changeSource}

#### \<instance> changeSource(source) {#instance-changesourcesource}


**说明:**

更改边角的源头, 用新形状取代已有的形状。 新源头必须提供 `getPoints(quantity, stepRate)` 方法。 在源头被替换后, `updateSource` 自动调用, 以重新生成边缘点并相应重设内部状态 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Types.GameObjects.Particles.EdgeZoneSource](/api/typedef/types-gameobjects-particles#edgezonesource) | 否 | 具有 `getPoints(quantity, stepRate)` 方法的天体实例返回数组点 。 |


**返回值:** [Phaser.GameObjects.Particles.Zones.EdgeZone](/api/class/gameobjects-particles-zones-edgezone) - 边区


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L198](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L198)  
引入版本：3.0.0


---

### getPoint {#getPoint}

#### \<instance> getPoint(particle) {#instance-getpointparticle}


**说明:**

获取"区"中的下一个点,并将其坐标设定在给定的粒子上.

点按顺序排列。当点列表的结尾到达时,计数器会将点列表反向包装到起始位置,或者如果启用 `yoyo`,则反向。每次发射新粒子时,都会由粒子 Emitter 自动调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| particle | [Phaser.GameObjects.Particles.Particle](/api/class/gameobjects-particles-particle) | 否 | 粒子 粒子 粒子 粒子 |


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L218)  
引入版本：3.0.0


---

### updateSource {#updateSource}

#### \<instance> updateSource() {#instance-updatesource}


**说明:**

更新边缘[Phaser.GameObjects.Particles.Zones.EdgeZone#points](/api/class/gameobjects-particles-zones-edgezone#points) 从边缘[Phaser.GameObjects.Particles.Zones.EdgeZone#source](/api/class/gameobjects-particles-zones-edgezone#source)。

同时更新内部属性.


**返回值:** [Phaser.GameObjects.Particles.Zones.EdgeZone](/api/class/gameobjects-particles-zones-edgezone) - 边区


> 源码：[src/gameobjects/particles/zones/EdgeZone.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/particles/zones/EdgeZone.js#L158)  
引入版本：3.0.0


---

---
