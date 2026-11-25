# Types.Scenes {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-scenes)

## CreateSceneFromObjectConfig {#createscenefromobjectconfig}

### \<static> CreateSceneFromObjectConfig {#static-createscenefromobjectconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| init | [Phaser.Types.Scenes.SceneInitCallback](/api/typedef/types-scenes#sceneinitcallback) | 是 | 现场是回电 |
| preload | [Phaser.Types.Scenes.ScenePreloadCallback](/api/typedef/types-scenes#scenepreloadcallback) | 是 | 现场预装回调. |
| create | [Phaser.Types.Scenes.SceneCreateCallback](/api/typedef/types-scenes#scenecreatecallback) | 是 | 现场的创作回调. |
| update | [Phaser.Types.Scenes.SceneUpdateCallback](/api/typedef/types-scenes#sceneupdatecallback) | 是 | 现场更新回调,见QQlink Phaser.Scene#update]. |
| extend | any | 是 | 任何额外的属性,在创建后会被复制到景区(`data`或`sys`除外). |
| extend.data | any | 是 | 任意值,这些值将被合并到Scene的数据管理器商店中. |

**类型**: object

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/CreateSceneFromObjectConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/CreateSceneFromObjectConfig.js#L1)  
引入版本：3.17.0

---

## SceneCreateCallback {#scenecreatecallback}

### \<static> SceneCreateCallback {#static-scenecreatecallback}


可以在您自己的屏幕上定义。 使用它来创建您的游戏对象 。
这种方法在现场开始时由场景管理者调用,在`init()`和`preload()`之后.
如果装入器Plugin在`preload()`之后开始,那么这种方法只有在装入完成后才被调用.

**类型**: function

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/SceneCreateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneCreateCallback.js#L1)  
引入版本：3.0.0

---

## SceneInitCallback {#sceneinitcallback}

### \<static> SceneInitCallback {#static-sceneinitcallback}


可以用你自己的场景来定义。
这种方法在现场开始时由场景管理者调用,在`preload()`和`create()`之前.

**类型**: function

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/SceneInitCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneInitCallback.js#L1)  
引入版本：3.0.0

---

## ScenePreloadCallback {#scenepreloadcallback}

### \<static> ScenePreloadCallback {#static-scenepreloadcallback}


可以用自己的场景定义。 使用它来装入资产 。
这种方法由场景管理器调用,在`init()`之后和`create()`之前,只有在场景有加载器普鲁金的情况下才使用.
此方法完成后,如果加载器Plugin的队列不是空的,加载器Plugin会自动启动.

**类型**: function

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/ScenePreloadCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/ScenePreloadCallback.js#L1)  
引入版本：3.0.0

---

## SceneTransitionConfig {#scenetransitionconfig}

### \<static> SceneTransitionConfig {#static-scenetransitionconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | string | 否 |  | 向中转的场景关键 。 |
| duration | number | 是 | 1000 | 过渡期,以毫秒计。 |
| sleep | boolean | 是 | false | 负责过渡的场景在完成时会被送入睡眠(`true`),还是停止? (`false`). |
| remove | boolean | 是 | false | 过渡完成后负责过渡的场景是否从场景管理器中移除?. |
| allowInput | boolean | 是 | false | 图片输入系统能否在过渡期间处理事件? |
| moveAbove | boolean | 是 |  | 在过渡开始前将目标景移到此景之上 。 |
| moveBelow | boolean | 是 |  | 在过渡开始前将目标景移到此景下方 。 |
| onUpdate | function | 是 |  | 在过渡期间,每个框架都引用这种回调。 |
| onUpdateScope | any | 是 |  | 引用回调时的上下文 。 |
| onStart | [Phaser.Types.Scenes.SceneTransitionOnStartCallback](/api/typedef/types-scenes#scenetransitiononstartcallback) | 是 |  | 过渡开始时会引用此调用 。 |
| onStartScope | any | 是 |  | 引用回调时的上下文 。 |
| data | any | 是 |  | 包含任何数据的对象,您希望被传递到目标场景的init / 创建方法(如果睡眠是虚假的),或者被传递到目标场面的醒悟事件召回(如果睡眠是真实的). |

**类型**: object

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/SceneTransitionConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneTransitionConfig.js#L1)  
引入版本：3.5.0

---

## SceneTransitionOnStartCallback {#scenetransitiononstartcallback}

### \<static> SceneTransitionOnStartCallback {#static-scenetransitiononstartcallback}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 1000 | 过渡期,以毫秒计。 |

**类型**: function

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/SceneTransitionStartCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneTransitionStartCallback.js#L1)  
引入版本：3.60.0

---

## SceneType {#scenetype}

### \<static> SceneType {#static-scenetype}

**类型**: [Phaser.Scene](/api/class/scene) | [Phaser.Types.Scenes.SettingsConfig](/api/typedef/types-scenes#settingsconfig) | [Phaser.Types.Scenes.CreateSceneFromObjectConfig](/api/typedef/types-scenes#createscenefromobjectconfig) | function

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/SceneType.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneType.js#L1)  
引入版本：3.60.0

---

## SceneUpdateCallback {#sceneupdatecallback}

### \<static> SceneUpdateCallback {#static-sceneupdatecallback}

**类型**: function

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/SceneUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SceneUpdateCallback.js#L1)  
引入版本：3.0.0

---

## SettingsConfig {#settingsconfig}

### \<static> SettingsConfig {#static-settingsconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 是 |  | 此场景的独特密钥。 必须在游戏的全部实例中独有 。 |
| active | boolean | 是 | false | 场景是否以活动开始? 活动场景更新每个步骤 。 |
| visible | boolean | 是 | true | 场景的开始是否是可见的? 可见的场景使每个步骤都成形 。 |
| pack | false \| [Phaser.Types.Loader.FileTypes.PackFileSection](/api/typedef/types-loader-filetypes#packfilesection) | 是 | false | 场景开始前要加载的文件 。 |
| cameras | [Phaser.Types.Cameras.Scene2D.CameraConfig](/api/typedef/types-cameras-scene2d#cameraconfig) \| Array.\<[Phaser.Types.Cameras.Scene2D.CameraConfig](/api/typedef/types-cameras-scene2d#cameraconfig)> | 是 | null | 相机配置对象可选 。 |
| map | Object.\<string, string> | 是 |  | 覆盖一个场景的默认注射映射。 |
| mapAdd | Object.\<string, string> | 是 |  | 将注入图扩展为场景 。 |
| physics | [Phaser.Types.Core.PhysicsConfig](/api/typedef/types-core#physicsconfig) | 是 | "{}" | 场景的物理配置对象 。 |
| loader | [Phaser.Types.Core.LoaderConfig](/api/typedef/types-core#loaderconfig) | 是 | "{}" | 场景的加载器配置对象 。 |
| plugins | false \| * | 是 | false | 场景的插件配置对象 。 |

**类型**: object

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/SettingsConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SettingsConfig.js#L1)  
引入版本：3.0.0

---

## SettingsObject {#settingsobject}

### \<static> SettingsObject {#static-settingsobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| status | number | 否 | 场景的当前状态 映射到场景常数. |
| key | string | 否 | 此场景的独特密钥。 在整个游戏实例中独一无二 。 |
| active | boolean | 否 | 此场景的活跃状态。 活动场景更新了每个步骤 。 |
| visible | boolean | 否 | 此场景的可见状态。 可见的场景使每个步骤都成为了 。 |
| isBooted | boolean | 否 | 场景是否完成了启动? |
| isTransition | boolean | 否 | 场景是否处于过渡状态? |
| transitionFrom | [Phaser.Scene](/api/class/scene) | 否 | 此场景正在从中过渡, 如果设置 。 |
| transitionDuration | number | 否 | 如果设定了过渡期,则需要过渡期。 |
| transitionAllowInput | boolean | 否 | 此场景是否允许在过渡期间接收输入 ? |
| data | object | 否 | 由场景管理器传送到此场景的数据捆绑 。 |
| pack | false \| [Phaser.Types.Loader.FileTypes.PackFileSection](/api/typedef/types-loader-filetypes#packfilesection) | 否 | 场景开始前要加载的文件 。 |
| cameras | [Phaser.Types.Cameras.Scene2D.CameraConfig](/api/typedef/types-cameras-scene2d#cameraconfig) \| Array.\<[Phaser.Types.Cameras.Scene2D.CameraConfig](/api/typedef/types-cameras-scene2d#cameraconfig)> | 否 | 相机配置对象. |
| map | Object.\<string, string> | 否 | 景德镇注入图. |
| physics | [Phaser.Types.Core.PhysicsConfig](/api/typedef/types-core#physicsconfig) | 否 | 场景的物理配置对象 。 |
| loader | [Phaser.Types.Core.LoaderConfig](/api/typedef/types-core#loaderconfig) | 否 | 场景的加载器配置对象 。 |
| plugins | false \| * | 否 | 场景的插件配置对象 。 |

**类型**: object

**Member of**: Phaser.Types.Scenes
> 源码：[src/scene/typedefs/SettingsObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/scene/typedefs/SettingsObject.js#L1)  
引入版本：3.0.0

---

---
