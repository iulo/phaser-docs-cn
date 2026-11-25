# Phaser.Types.Physics.Matter {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/types-physics-matter)

Scope: 
static
> 源码：[src/physics/matter-js/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/index.js#L7)  


## 静态函数 {#static-functions}

### MatterBody {#MatterBody}

#### MatterBody {#matterbody}


> 源码：[src/physics/matter-js/typedefs/MatterBody.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterBody.js#L1)  
引入版本：3.22.0


---

### MatterBodyConfig {#MatterBodyConfig}

#### MatterBodyConfig {#matterbodyconfig}


> 源码：[src/physics/matter-js/typedefs/MatterBodyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterBodyConfig.js#L1)  
引入版本：3.22.0


---

### MatterBodyRenderConfig {#MatterBodyRenderConfig}

#### MatterBodyRenderConfig {#matterbodyrenderconfig}


> 源码：[src/physics/matter-js/typedefs/MatterBodyRenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterBodyRenderConfig.js#L1)  
引入版本：3.22.0


---

### MatterBodyTileOptions {#MatterBodyTileOptions}

#### MatterBodyTileOptions {#matterbodytileoptions}


> 源码：[src/physics/matter-js/typedefs/MatterBodyTileOptions.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterBodyTileOptions.js#L1)  
引入版本：3.0.0


---

### MatterChamferConfig {#MatterChamferConfig}

#### MatterChamferConfig {#matterchamferconfig}


> 源码：[src/physics/matter-js/typedefs/MatterChamferConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterChamferConfig.js#L1)  
引入版本：3.22.0


---

### MatterCollisionData {#MatterCollisionData}

#### MatterCollisionData {#mattercollisiondata}


> 源码：[src/physics/matter-js/typedefs/MatterCollisionData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterCollisionData.js#L1)  
引入版本：3.22.0


---

### MatterCollisionFilter {#MatterCollisionFilter}

#### MatterCollisionFilter {#mattercollisionfilter}


**说明:**

指定此天体碰撞过滤特性的 `Object` 。

两个机构之间的碰撞将遵守以下规则:

- 如果两具尸体的无零值是`collisionFilter.group`的,

  如果数值是正值,它们总是会碰撞,它们永远不会碰撞

  如果数值为负数。

- 如果两个机构有不同的`collisionFilter.group`值或者一个

  (或两者)机构值为0,然后适用类别/任务规则如下:

每个天体属于一个碰撞类别, 由 `collisionFilter.category` 给出。 这个值被作为位域使用, 并且该类别只应该有一个位集, 这意味着这个属性的值是 [1, 2^31] 范围内的 2 个功率 。 因此, 有32 个不同的碰撞类别可用 。

每个机体还定义了`collisionFilter.mask`给出的碰撞位图,该位图规定了它与之碰撞的类别(值是所有这些类别的位元和值)。

使用类别/任务规则,两个机构 `A` 财务报告和已审计财务报表 `B` 如果两者在面具中包括对方的类别,即相互碰撞。 `(categoryA & maskB) !== 0` 财务报告和已审计财务报表 `(categoryB & maskA) !== 0` 都是真的 都一样


> 源码：[src/physics/matter-js/typedefs/MatterCollisionFilter.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterCollisionFilter.js#L1)  
引入版本：3.22.0


---

### MatterCollisionPair {#MatterCollisionPair}

#### MatterCollisionPair {#mattercollisionpair}


> 源码：[src/physics/matter-js/typedefs/MatterCollisionPair.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterCollisionPair.js#L1)  
引入版本：3.22.0


---

### MatterConstraintConfig {#MatterConstraintConfig}

#### MatterConstraintConfig {#matterconstraintconfig}


> 源码：[src/physics/matter-js/typedefs/MatterConstraintConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterConstraintConfig.js#L1)  
引入版本：3.22.0


---

### MatterConstraintRenderConfig {#MatterConstraintRenderConfig}

#### MatterConstraintRenderConfig {#matterconstraintrenderconfig}


> 源码：[src/physics/matter-js/typedefs/MatterConstraintRenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterConstraintRenderConfig.js#L1)  
引入版本：3.22.0


---

### MatterDebugConfig {#MatterDebugConfig}

#### MatterDebugConfig {#matterdebugconfig}


> 源码：[src/physics/matter-js/typedefs/MatterDebugConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterDebugConfig.js#L1)  
引入版本：3.22.0


---

### MatterRunnerConfig {#MatterRunnerConfig}

#### MatterRunnerConfig {#matterrunnerconfig}


**说明:**

物质物理运行器配置 。

只设置一个`fps`和`delta`.

`delta`是跑者固定时间步(一个物理更新)的大小,"帧三角洲"是自上一个游戏步骤以来的时间所经过的时间,根据帧三角洲的大小,跑者每个游戏步骤进行0或更多更新.


> 源码：[src/physics/matter-js/typedefs/MatterRunnerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterRunnerConfig.js#L1)  
引入版本：3.22.0


---

### MatterSetBodyConfig {#MatterSetBodyConfig}

#### MatterSetBodyConfig {#mattersetbodyconfig}


> 源码：[src/physics/matter-js/typedefs/MatterSetBodyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterSetBodyConfig.js#L1)  
引入版本：3.22.0


---

### MatterTileOptions {#MatterTileOptions}

#### MatterTileOptions {#mattertileoptions}


> 源码：[src/physics/matter-js/typedefs/MatterTileOptions.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterTileOptions.js#L1)  
引入版本：3.0.0


---

### MatterWalls {#MatterWalls}

#### MatterWalls {#matterwalls}


> 源码：[src/physics/matter-js/typedefs/MatterWalls.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterWalls.js#L1)  
引入版本：3.0.0


---

### MatterWorldConfig {#MatterWorldConfig}

#### MatterWorldConfig {#matterworldconfig}


> 源码：[src/physics/matter-js/typedefs/MatterWorldConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/typedefs/MatterWorldConfig.js#L1)  
引入版本：3.0.0


---

---
