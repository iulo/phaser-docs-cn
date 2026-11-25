# Phaser.Plugins.PluginCache {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/plugins-plugincache)

Scope: 
static
> 源码：[src/plugins/PluginCache.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L17)  


## 静态函数 {#static-functions}

### destroyCorePlugins {#destroyCorePlugins}

#### \<static> destroyCorePlugins() {#static-destroycoreplugins}


**说明:**

删除所有核心插件。

这包括 Phaser 所需的所有内部系统插件, 如输入插件和资源加载器插件。 所以, 只有在您不想再次运行 Phaser 时, 请确定您只使用此插件 。


> 源码：[src/plugins/PluginCache.js#L166](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L166)  
引入版本：3.12.0


---

### destroyCustomPlugins {#destroyCustomPlugins}

#### \<static> destroyCustomPlugins() {#static-destroycustomplugins}


**说明:**

删除所有自定义插件。

这可以删除开发者通过插件管理器注册的任何插件,但不影响Phaser需要运行的核心内部插件.


> 源码：[src/plugins/PluginCache.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L186)  
引入版本：3.12.0


---

### getCore {#getCore}

#### \<static> getCore(key) {#static-getcorekey}


**说明:**

根据给定的键,从缓存中返回核心插件对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要获取的核心插件的键 。 |


**返回值:** [Phaser.Types.Plugins.CorePluginContainer](/api/typedef/types-plugins#coreplugincontainer) - 核心插件对象 。


> 源码：[src/plugins/PluginCache.js#L88](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L88)  
引入版本：3.8.0


---

### getCustom {#getCustom}

#### \<static> getCustom(key) {#static-getcustomkey}


**说明:**

根据给定的键从缓存中返回自定义插件对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要获取的自定义插件的键 。 |


**返回值:** [Phaser.Types.Plugins.CustomPluginContainer](/api/typedef/types-plugins#customplugincontainer) - 自定义插件对象 。


> 源码：[src/plugins/PluginCache.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L103)  
引入版本：3.8.0


---

### getCustomClass {#getCustomClass}

#### \<static> getCustomClass(key) {#static-getcustomclasskey}


**说明:**

从基于给定键的自定义插件缓存返回插件构造器功能, 如果不存在该键的条目, 则返回 `null` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要获取的自定义插件的键 。 |


**返回值:** function - 自定义插件对象 。


> 源码：[src/plugins/PluginCache.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L118)  
引入版本：3.8.0


---

### hasCore {#hasCore}

#### \<static> hasCore(key) {#static-hascorekey}


**说明:**

检查是否在核心插件缓存中已经使用给定的键 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 钥匙要检查。 |


**返回值:** boolean - 如果键已经在核心缓存中使用,则使用`true`,否则使用`false`.


> 源码：[src/plugins/PluginCache.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L58)  
引入版本：3.8.0


---

### hasCustom {#hasCustom}

#### \<static> hasCustom(key) {#static-hascustomkey}


**说明:**

检查自定义插件缓存中是否已经使用给定的键 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 钥匙要检查。 |


**返回值:** boolean - 如果键已经在自定义缓存中使用,则使用`true`,否则使用`false`.


> 源码：[src/plugins/PluginCache.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L73)  
引入版本：3.8.0


---

### register {#register}

#### \<static> register(key, plugin, mapping, [custom]) {#static-registerkey-plugin-mapping-custom}


**说明:**

注册一个带有插件缓存的核心插件。 设置时, Phaser 的内部核心插件直接使用此插件。 该插件作为源构建器存储, 且在此阶段不被即时处理 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 从插件缓存中获取此插件的参考 。 |
| plugin | function | 否 |  | 要存储的插件。 应该是核心对象, 而不是即时对象 。 |
| mapping | string | 否 |  | 如果要将此插件注入 Scene 系统, 这就是所用的属性键映射 。 |
| custom | boolean | 是 | false | 核心场景插件还是自定义场景插件 ? |


> 源码：[src/plugins/PluginCache.js#L21](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L21)  
引入版本：3.8.0


---

### registerCustom {#registerCustom}

#### \<static> registerCustom(key, plugin, mapping, data) {#static-registercustomkey-plugin-mapping-data}


**说明:**

将自定义插件存储在全局插件缓存中。键必须是独一无二的,属于缓存范围。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从插件缓存中获取此插件的参考 。 |
| plugin | function | 否 | 要存储的插件。 应该是核心对象, 而不是即时对象 。 |
| mapping | string | 否 | 如果要将此插件注入 Scene 系统, 这就是所用的属性键映射 。 |
| data | any | 否 | 将传递到插件的 `init` 方法的值 。 |


> 源码：[src/plugins/PluginCache.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L41)  
引入版本：3.8.0


---

### remove {#remove}

#### \<static> remove(key) {#static-removekey}


**说明:**

删除基于给定键的核心插件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的核心插件的键 。 |


> 源码：[src/plugins/PluginCache.js#L134](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L134)  
引入版本：3.8.0


---

### removeCustom {#removeCustom}

#### \<static> removeCustom(key) {#static-removecustomkey}


**说明:**

删除基于给定键的自定义插件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的自定义插件的键 。 |


> 源码：[src/plugins/PluginCache.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/PluginCache.js#L150)  
引入版本：3.8.0


---

---
