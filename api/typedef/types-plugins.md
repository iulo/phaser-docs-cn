# Types.Plugins {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-plugins)

## CorePluginContainer {#coreplugincontainer}

### \<static> CorePluginContainer {#static-coreplugincontainer}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 核心插件缓存中此插件的独有名称 。 |
| plugin | function | 否 |  | 要存储的插件。 应该是源对象, 而不是即时对象 。 |
| mapping | string | 是 |  | 如果要将此插件注入 Scene 系统, 这就是所用的属性键映射 。 |
| custom | boolean | 是 | false | 核心场景插件还是自定义场景插件 ? |

**类型**: object

**所属**: Phaser.Types.Plugins
> 源码：[src/plugins/typedefs/CorePluginContainer.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/typedefs/CorePluginContainer.js#L1)  
引入版本：3.8.0

---

## CustomPluginContainer {#customplugincontainer}

### \<static> CustomPluginContainer {#static-customplugincontainer}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 自定义插件缓存中此插件的独有名称 。 |
| plugin | function | 否 | 要存储的插件。 应该是源对象, 而不是即时对象 。 |

**类型**: object

**所属**: Phaser.Types.Plugins
> 源码：[src/plugins/typedefs/CustomPluginContainer.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/typedefs/CustomPluginContainer.js#L1)  
引入版本：3.8.0

---

## GlobalPlugin {#globalplugin}

### \<static> GlobalPlugin {#static-globalplugin}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 插件缓存中此插件的独有名称 。 |
| plugin | function | 否 | 插件的示例 。 |
| active | boolean | 是 | 插件是否在活动 ? |
| mapping | string | 是 | 如果要将此插件注入 Scene 系统, 这就是所用的属性键映射 。 |

**类型**: object

**所属**: Phaser.Types.Plugins
> 源码：[src/plugins/typedefs/GlobalPlugin.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/plugins/typedefs/GlobalPlugin.js#L1)  
引入版本：3.0.0

---

---
