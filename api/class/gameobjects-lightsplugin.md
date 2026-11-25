# LightsPlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-lightsplugin)

一个场景插件,提供[Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager)用于以动态照明渲染对象.

现场内部通过`this.lights`提供.

使用 [Phaser.GameObjects.LightsManager#addLight](/api/class/gameobjects-lightsmanager#addLight) 方法添加灯光 :

```javascript
// Enable the Lights Manager because it is disabled by default
this.lights.enable();

// Create a Light at [400, 300] with a radius of 200
this.lights.addLight(400, 300, 200);
```

要让游戏对象在渲染时受到灯光的影响,您需要设置它们来使用这样的照明:

```javascript
sprite.setLighting(true);
```

**构造函数**

`new LightsPlugin(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 显示此灯插件属于的场景 。 |

---


**作用域**: static


**继承**

> [Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager)  



> 源码：[src/gameobjects/lights/LightsPlugin.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsPlugin.js#L12)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager):**


 - [active](/api/class/gameobjects-lightsmanager#active)
 - [ambientColor](/api/class/gameobjects-lightsmanager#ambientColor)
 - [lights](/api/class/gameobjects-lightsmanager#lights)
 - [maxLights](/api/class/gameobjects-lightsmanager#maxLights)
 - [visibleLights](/api/class/gameobjects-lightsmanager#visibleLights)




---

## 公开成员 {#public-members}

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

引用此 Lights 插件所属的场景 。


> 源码：[src/gameobjects/lights/LightsPlugin.js#L50](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsPlugin.js#L50)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考史氏系统.


> 源码：[src/gameobjects/lights/LightsPlugin.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsPlugin.js#L59)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.GameObjects.LightsManager](/api/class/gameobjects-lightsmanager):**


 - [addLight](/api/class/gameobjects-lightsmanager#addLight)
 - [addPointLight](/api/class/gameobjects-lightsmanager#addPointLight)
 - [disable](/api/class/gameobjects-lightsmanager#disable)
 - [enable](/api/class/gameobjects-lightsmanager#enable)
 - [getLightCount](/api/class/gameobjects-lightsmanager#getLightCount)
 - [getLights](/api/class/gameobjects-lightsmanager#getLights)
 - [getMaxVisibleLights](/api/class/gameobjects-lightsmanager#getMaxVisibleLights)
 - [removeLight](/api/class/gameobjects-lightsmanager#removeLight)
 - [setAmbientColor](/api/class/gameobjects-lightsmanager#setAmbientColor)
 - [shutdown](/api/class/gameobjects-lightsmanager#shutdown)
 - [sortByDistance](/api/class/gameobjects-lightsmanager#sortByDistance)




---

## 公开方法 {#public-methods}

### boot {#boot}

#### \<instance> boot() {#instance-boot}


**说明:**

从 Scene 事件 Emitter 处理启动事件, 签名到 Scene 的 `shutdown` 和 `destroy` 事件, 这样插件可以在 Scene 停止或破坏时清理它的资源 。


> 源码：[src/gameobjects/lights/LightsPlugin.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsPlugin.js#L76)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

摧毁灯光插件 。

清净一切参引.


**Overrides:** Phaser.GameObjects.LightsManager#销毁


> 源码：[src/gameobjects/lights/LightsPlugin.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/lights/LightsPlugin.js#L92)  
引入版本：3.0.0


---

---
