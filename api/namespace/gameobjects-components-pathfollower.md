# Phaser.GameObjects.Components.PathFollower {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-pathfollower)

Scope: 
static
> 源码：[src/gameobjects/components/PathFollower.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L13)  
引入版本：3.17.0

## 静态函数 {#static-functions}

### path {#path}

#### path: [Phaser.Curves.Path](/api/class/curves-path) {#path-phasercurvespath}


**说明:**

此路径跟踪器遵循的路径。 它只能一次遵循一个路径 。


> 源码：[src/gameobjects/components/PathFollower.js#L25](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L25)  
引入版本：3.0.0


---

### pathRotationOffset {#pathRotationOffset}

#### pathRotationOffset: number {#pathrotationoffset-number}


**说明:**

如果路径跟踪器正在旋转以匹配路径( @ 见 Phaser.GameObjects.Components.PathFollower# rotateToPath), 此值会被添加到旋转值中, 以度计。 这样您就可以旋转对象到路径, 但也可以控制旋转角度 。


> 源码：[src/gameobjects/components/PathFollower.js#L44](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L44)  
引入版本：3.0.0


---

### rotateToPath {#rotateToPath}

#### rotateToPath: boolean {#rotatetopath-boolean}


**说明:**

路径跟踪器是否应该自动旋转以指向路径的方向 ?


> 源码：[src/gameobjects/components/PathFollower.js#L34](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L34)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### isFollowing {#isFollowing}

#### \<instance> isFollowing() {#instance-isfollowing}


**说明:**

这个路径跟踪器是否在积极遵循路径 ?

要被视为`isFollowing`,它必须目前沿着路径前进,而不是停顿.


**返回值:** boolean - 如果此路径跟踪器正在积极遵循路径,则使用`true`,否则使用`false`.


> 源码：[src/gameobjects/components/PathFollower.js#L169](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L169)  
引入版本：3.0.0


---

### pathUpdate {#pathUpdate}

#### \<instance> pathUpdate() {#instance-pathupdate}


**说明:**

将路径跟踪器沿路径推进的内部更新处理器 。

由场景步骤自动调用,一般不应直接调用.


> 源码：[src/gameobjects/components/PathFollower.js#L352](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L352)  
引入版本：3.17.0


---

### pauseFollow {#pauseFollow}

#### \<instance> pauseFollow() {#instance-pausefollow}


**说明:**

暂停此路径跟踪器。 它会继续渲染, 但会在您暂停它时的路径点上保持无动静 。


**返回值:** [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower) - 此游戏对象 。


> 源码：[src/gameobjects/components/PathFollower.js#L287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L287)  
引入版本：3.3.0


---

### resumeFollow {#resumeFollow}

#### \<instance> resumeFollow() {#instance-resumefollow}


**说明:**

恢复先前暂停的路径跟踪器 。

如果路径跟踪器没有被暂停, 则没有效果 。


**返回值:** [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower) - 此游戏对象 。


> 源码：[src/gameobjects/components/PathFollower.js#L308](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L308)  
引入版本：3.3.0


---

### setPath {#setPath}

#### \<instance> setPath(path, [config]) {#instance-setpathpath-config}


**说明:**

设定此路径跟踪器应该遵循的路径 。

可选接受[Phaser.Types.GameObjects.PathFollower.PathConfig](/api/typedef/types-gameobjects-pathfollower#pathconfig)设置.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| path | [Phaser.Curves.Path](/api/class/curves-path) | 否 | 此路径跟踪器遵循的路径。 它只能一次遵循一个路径 。 |
| config | number \| [Phaser.Types.GameObjects.PathFollower.PathConfig](/api/typedef/types-gameobjects-pathfollower#pathconfig) | [Phaser.Types.Tweens.NumberTweenBuilderConfig](/api/typedef/types-tweens#numbertweenbuilderconfig) | 是 | 路径跟踪器的设置 。 |


**返回值:** [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower) - 此游戏对象 。


> 源码：[src/gameobjects/components/PathFollower.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L113)  
引入版本：3.0.0


---

### setRotateToPath {#setRotateToPath}

#### \<instance> setRotateToPath(value, [offset]) {#instance-setrotatetopathvalue-offset}


**说明:**

设定路径跟踪器是否应该自动旋转以指向路径的方向 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 否 |  | 路径跟踪器是否应该自动旋转, 以指向路径的方向 。 |
| offset | number | 是 | 0 | 旋转乘以度数. |


**返回值:** [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower) - 此游戏对象 。


> 源码：[src/gameobjects/components/PathFollower.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L147)  
引入版本：3.0.0


---

### startFollow {#startFollow}

#### \<instance> startFollow([config], [startAt]) {#instance-startfollowconfig-startat}


**说明:**

沿着给定路径启动此路径跟踪器。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| config | number \| [Phaser.Types.GameObjects.PathFollower.PathConfig](/api/typedef/types-gameobjects-pathfollower#pathconfig) | [Phaser.Types.Tweens.NumberTweenBuilderConfig](/api/typedef/types-tweens#numbertweenbuilderconfig) | 是 | "{}" | 以下的长度,或路径跟踪配置对象。 |
| startAt | number | 是 | 0 | 后续的可选起始位置,在0到1之间. |


**返回值:** [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower) - 此游戏对象 。


> 源码：[src/gameobjects/components/PathFollower.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L186)  
引入版本：3.3.0


---

### stopFollow {#stopFollow}

#### \<instance> stopFollow() {#instance-stopfollow}


**说明:**

停止此路径跟踪器继续跟踪路径 。

这将引用路径上可能存在的任何“ 停止” 条件, 或为后续者 。


**返回值:** [Phaser.GameObjects.Components.PathFollower](/api/namespace/gameobjects-components-pathfollower) - 此游戏对象 。


> 源码：[src/gameobjects/components/PathFollower.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/PathFollower.js#L330)  
引入版本：3.3.0


---

---
