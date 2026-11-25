# Phaser.Types.Input {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/types-input)

Scope: 
static
> 源码：[src/input/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/index.js#L7)  


## 静态函数 {#static-functions}

- [Gamepad](/api/namespace/types-input-gamepad)
- [Keyboard](/api/namespace/types-input-keyboard)
## 静态函数 {#static-functions-1}

### EventData {#EventData}

#### EventData {#eventdata}


**说明:**

一个 Phaser 输入事件数据对象.

此对象将传递给已注册的事件的监听器, 并允许您停止任何进一步的传播 。


> 源码：[src/input/typedefs/EventData.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/EventData.js#L7)  
引入版本：3.15.1


---

### HitAreaCallback {#HitAreaCallback}

#### HitAreaCallback {#hitareacallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| hitArea | any | 否 | 命中区物体. |
| x | number | 否 | 命中测试事件的翻译 x 坐标 。 |
| y | number | 否 | 命中测试事件的翻译 y 坐标 。 |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 引用命中测试的游戏对象 。 |


**返回值:** boolean - `true` 如果坐标位于 hitArea,否则 `false`.


> 源码：[src/input/typedefs/HitAreaCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/HitAreaCallback.js#L1)  
引入版本：3.0.0


---

### InputConfiguration {#InputConfiguration}

#### InputConfiguration {#inputconfiguration}


> 源码：[src/input/typedefs/InputConfiguration.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/InputConfiguration.js#L1)  
引入版本：3.0.0


---

### InputPluginContainer {#InputPluginContainer}

#### InputPluginContainer {#inputplugincontainer}


> 源码：[src/input/typedefs/InputPluginContainer.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/InputPluginContainer.js#L1)  
引入版本：3.0.0


---

### InteractiveObject {#InteractiveObject}

#### InteractiveObject {#interactiveobject}


> 源码：[src/input/typedefs/InteractiveObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/InteractiveObject.js#L1)  
引入版本：3.0.0


---

---
