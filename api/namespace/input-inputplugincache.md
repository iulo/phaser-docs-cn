# Phaser.Input.InputPluginCache {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/input-inputplugincache)

Scope: 
static
> 源码：[src/input/InputPluginCache.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPluginCache.js#L13)  


## 静态函数 {#static-functions}

### getPlugin {#getPlugin}

#### \<static> getPlugin(key) {#static-getpluginkey}


**说明:**

根据给定的密钥,从缓存中返回输入插件对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要获取的输入插件的密钥 。 |


**返回值:** [Phaser.Types.Input.InputPluginContainer](/api/typedef/types-input#inputplugincontainer) - 输入插件对象 。


> 源码：[src/input/InputPluginCache.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPluginCache.js#L40)  
引入版本：3.10.0


---

### install {#install}

#### \<static> install(target) {#static-installtarget}


**说明:**

将所有注册的输入插件安装到给定目标中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| target | [Phaser.Input.InputPlugin](/api/class/input-inputplugin) | 否 | 目标输入器将安装插件输入 。 |


> 源码：[src/input/InputPluginCache.js#L56](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPluginCache.js#L56)  
引入版本：3.10.0


---

### register {#register}

#### \<static> register(key, plugin, mapping, settingsKey, configKey) {#static-registerkey-plugin-mapping-settingskey-configkey}


**说明:**

由核心内部插件直接调用静态方法。 密钥是用于从输入插件缓存中获取插件的参考。 插件是创建插件的即时对象。 映射是插件注入输入插件( 如 `input`) 时所使用的属性密钥 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从插件缓存中获取此插件的参考 。 |
| plugin | function | 否 | 要存储的插件。 应该是核心对象, 而不是即时对象 。 |
| mapping | string | 否 | 如果要将这个插件注入输入插件, 这就是所用的属性密钥 。 |
| settingsKey | string | 否 | 用于检查此插件是否安装的场景设置中的密钥 。 |
| configKey | string | 否 | 游戏配置中要检查此插件是否安装的密钥 。 |


> 源码：[src/input/InputPluginCache.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPluginCache.js#L19)  
引入版本：3.10.0


---

### remove {#remove}

#### \<static> remove(key) {#static-removekey}


**说明:**

删除基于给定密钥的输入插件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的输入插件的密钥 。 |


> 源码：[src/input/InputPluginCache.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPluginCache.js#L85)  
引入版本：3.10.0


---

---
