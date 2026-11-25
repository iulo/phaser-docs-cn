# Phaser.Types.Scenes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/types-scenes)

Scope: 
static
> 源码：[src/scene/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/index.js#L7)  


## 静态函数 {#static-functions}

### CreateSceneFromObjectConfig {#CreateSceneFromObjectConfig}

#### CreateSceneFromObjectConfig {#createscenefromobjectconfig}


> 源码：[src/scene/typedefs/CreateSceneFromObjectConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/CreateSceneFromObjectConfig.js#L1)  
引入版本：3.17.0


---

### SceneCreateCallback {#SceneCreateCallback}

#### SceneCreateCallback {#scenecreatecallback}


**说明:**

可以自定义 Scases 。 使用它来创建游戏对象。 场景开始时, 由 Scase 管理器调用此方法, 由 `init()` 和 `preload()` 之后的 Scase 。 如果资源加载器 Plugin 是从 `preload()` 之后开始的, 那么只有在装入完成后才调用此方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 否 | 任何通过`ScenePlugin.add()`或`ScenePlugin.start()`传递的数据,与场景设定数据相同. |


> 源码：[src/scene/typedefs/SceneCreateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneCreateCallback.js#L1)  
引入版本：3.0.0


---

### SceneInitCallback {#SceneInitCallback}

#### SceneInitCallback {#sceneinitcallback}


**说明:**

可以在您自己的情景下定义。 这种方法在情景开始时, 在 `preload()` 和 `create()` 之前, 由情景管理器调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | object | 否 | 任何通过`ScenePlugin.add()`或`ScenePlugin.start()`传递的数据,与场景设定数据相同. |


> 源码：[src/scene/typedefs/SceneInitCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneInitCallback.js#L1)  
引入版本：3.0.0


---

### ScenePreloadCallback {#ScenePreloadCallback}

#### ScenePreloadCallback {#scenepreloadcallback}


**说明:**

可以在您自己的屏幕上定义。 使用它来装入资源。 这种方法由场景管理器调用, 仅当场景有加载器普卢金时, 才会使用 `init()` 和 `create()` 之前。 完成此方法后, 如果加载器普卢京的队列不是空的, 则加载器普卢琴将自动启动 。


> 源码：[src/scene/typedefs/ScenePreloadCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/ScenePreloadCallback.js#L1)  
引入版本：3.0.0


---

### SceneTransitionConfig {#SceneTransitionConfig}

#### SceneTransitionConfig {#scenetransitionconfig}


> 源码：[src/scene/typedefs/SceneTransitionConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneTransitionConfig.js#L1)  
引入版本：3.5.0


---

### SceneTransitionOnStartCallback {#SceneTransitionOnStartCallback}

#### SceneTransitionOnStartCallback {#scenetransitiononstartcallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fromScene | [Phaser.Scene](/api/class/scene) | 否 | 场景实例向过渡 从。 |
| toScene | [Phaser.Scene](/api/class/scene) | 否 | 向 切换到 。 |


> 源码：[src/scene/typedefs/SceneTransitionStartCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneTransitionStartCallback.js#L1)  
引入版本：3.60.0


---

### SceneType {#SceneType}

#### SceneType {#scenetype}


> 源码：[src/scene/typedefs/SceneType.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneType.js#L1)  
引入版本：3.60.0


---

### SceneUpdateCallback {#SceneUpdateCallback}

#### SceneUpdateCallback {#sceneupdatecallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 当前的时间。 如果来自请求动画框架, 则使用高分辨率定时器值, 或者使用 SetTimeout 。 |
| delta | number | 否 | 自上一个帧以来的三角洲时间( ms) 。 这是一个平滑和上限的数值, 基于 FPS 速率 。 |


> 源码：[src/scene/typedefs/SceneUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneUpdateCallback.js#L1)  
引入版本：3.0.0


---

### SettingsConfig {#SettingsConfig}

#### SettingsConfig {#settingsconfig}


> 源码：[src/scene/typedefs/SettingsConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SettingsConfig.js#L1)  
引入版本：3.0.0


---

### SettingsObject {#SettingsObject}

#### SettingsObject {#settingsobject}


> 源码：[src/scene/typedefs/SettingsObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SettingsObject.js#L1)  
引入版本：3.0.0


---

---
