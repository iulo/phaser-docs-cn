# Phaser.Input {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/input)

### CreateInteractiveObject {#CreateInteractiveObject}

#### \<static> CreateInteractiveObject(gameObject, hitArea, hitAreaCallback) {#static-createinteractiveobjectgameobject-hitarea-hitareacallback}


**说明:**

创建新的交互式对象。

交互式对象是一个普通数据对象,它存储了游戏对象的所有输入状态。这包括命中区域几何、拖动状态、局部指针坐标、摄像机和任何投放区目标的引用。它不是一个类实例,而是该函数返回的普通对象字面。

当您启用游戏对象进行输入时, 输入管理器会自动调用此功能 。

由此而来的互动对象被映射到游戏对象的`input`属性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此交互对象所约束的游戏对象 。 |
| hitArea | any | 否 | 此交互对象的命中区域。 通常是一个几何形状, 如矩形或圆形 。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 否 | 命中区形状将用来进行所有命中测试的“ 封装” 检查回调 。 |


**返回值:** [Phaser.Types.Input.InteractiveObject](/api/typedef/types-input#interactiveobject) - 新的交互式对象 。


> 源码：[src/input/CreateInteractiveObject.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/CreateInteractiveObject.js#L7)  
引入版本：3.0.0


### CreatePixelPerfectHandler {#CreatePixelPerfectHandler}

#### \<static> CreatePixelPerfectHandler(textureManager, alphaTolerance) {#static-createpixelperfecthandlertexturemanager-alphatolerance}


**说明:**

创建新的像素完美处理器功能。

像素完美地击中检测测试了特定像素在游戏对象纹理上相互作用的α值,而不是完全依赖其约束框或命中区域几何,这使得在指针和重叠检查时完全透明的图样区域会被正确忽略,而每次测试都要以纹理检查为代价.

访问通过 `InputPlugin.makePixelPerfect` 而不是直接打电话

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| textureManager | [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) | 否 | 纹理管理器的参考文献. |
| alphaTolerance | number | 否 | 像素必须位于或高于的α级,以算作成功的交互. |


**返回值:** function - 新的像素完美处理器功能 。


> 源码：[src/input/CreatePixelPerfectHandler.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/CreatePixelPerfectHandler.js#L7)  
引入版本：3.10.0


# Phaser.Input.InputPluginCache {#page-title-1}

### register {#register}

#### \<static> register(key, plugin, mapping, settingsKey, configKey) {#static-registerkey-plugin-mapping-settingskey-configkey}


**说明:**

由核心内部插件直接调用静态方法。 键是用于从输入插件缓存中获取插件的参考。 插件是创建插件的即时对象。 映射是插件注入输入插件( 如 `input`) 时所使用的属性键 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 从插件缓存中获取此插件的参考 。 |
| plugin | function | 否 | 要存储的插件。 应该是核心对象, 而不是即时对象 。 |
| mapping | string | 否 | 如果要将这个插件注入输入插件, 这就是所用的属性键 。 |
| settingsKey | string | 否 | 用于检查此插件是否安装的场景设置中的键 。 |
| configKey | string | 否 | 游戏配置中要检查此插件是否安装的键 。 |


> 源码：[src/input/InputPluginCache.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPluginCache.js#L19)  
引入版本：3.10.0


### getPlugin {#getPlugin}

#### \<static> getPlugin(key) {#static-getpluginkey}


**说明:**

根据给定的键,从缓存中返回输入插件对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要获取的输入插件的键 。 |


**返回值:** [Phaser.Types.Input.InputPluginContainer](/api/typedef/types-input#inputplugincontainer) - 输入插件对象 。


> 源码：[src/input/InputPluginCache.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPluginCache.js#L40)  
引入版本：3.10.0


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


### remove {#remove}

#### \<static> remove(key) {#static-removekey}


**说明:**

删除基于给定键的输入插件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的输入插件的键 。 |


> 源码：[src/input/InputPluginCache.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/InputPluginCache.js#L85)  
引入版本：3.10.0


# Phaser.Input.Keyboard {#page-title-2}

### AdvanceKeyCombo {#AdvanceKeyCombo}

#### \<static> AdvanceKeyCombo(event, combo) {#static-advancekeycomboevent-combo}


**说明:**

KeyCombo 类内部使用。 如果达到组合的尾声, 请返回 `true` 。 如果没有, 返回 `false` 。


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地键盘事件. |
| combo | [Phaser.Input.Keyboard.KeyCombo](/api/class/input-keyboard-keycombo) | 否 | KeyCombo 对象要推进 。 |


**返回值:** boolean - 如果它到达组合的尽头,则`true`,如果没有,则`false`.


> 源码：[src/input/keyboard/combo/AdvanceKeyCombo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/AdvanceKeyCombo.js#L7)  
引入版本：3.0.0


### ProcessKeyCombo {#ProcessKeyCombo}

#### \<static> ProcessKeyCombo(event, combo) {#static-processkeycomboevent-combo}


**说明:**

由KeyCombo课内部使用.


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| event | KeyboardEvent | 否 | 本地键盘事件. |
| combo | [Phaser.Input.Keyboard.KeyCombo](/api/class/input-keyboard-keycombo) | 否 | 要处理的 KeyCombo 对象 。 |


**返回值:** boolean - 如果组合匹配,则使用`true`,否则使用`false`.


> 源码：[src/input/keyboard/combo/ProcessKeyCombo.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/ProcessKeyCombo.js#L9)  
引入版本：3.0.0


### ResetKeyCombo {#ResetKeyCombo}

#### \<static> ResetKeyCombo(combo) {#static-resetkeycombocombo}


**说明:**

由KeyCombo课内部使用.


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| combo | [Phaser.Input.Keyboard.KeyCombo](/api/class/input-keyboard-keycombo) | 否 | 要重置的键盘Combo 。 |


**返回值:** [Phaser.Input.Keyboard.KeyCombo](/api/class/input-keyboard-keycombo) - 键盘哥布.


> 源码：[src/input/keyboard/combo/ResetKeyCombo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/combo/ResetKeyCombo.js#L7)  
引入版本：3.0.0


### DownDuration {#DownDuration}

#### \<static> DownDuration(key, [duration]) {#static-downdurationkey-duration}


**说明:**

返回值 `true` 如果按键在 `duration` 值,基于当前游戏时钟时间。或 `false` 如果不是没下来,或者比规定的时间更早被压下来。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 |  | 要测试的键对象 。 |
| duration | number | 是 | 50 | 时间长度,以毫秒计,其中键必须按下。 |


**返回值:** boolean - 如果钥匙在`duration`米前按下的话,就按`true`,否则按`false`.


> 源码：[src/input/keyboard/keys/DownDuration.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/DownDuration.js#L7)  
引入版本：3.0.0


### JustDown {#JustDown}

#### \<static> JustDown(key) {#static-justdownkey}


**说明:**

justDown值允许您测试是否刚刚按下此键 。

当你检查这个值时,如果键下,它会返回`true`,否则返回`false`.

您只能每按下一次 justDown。 它只能返回 `true`一次, 直到键被再次发布并按下。 这样您就可以在您想要检查此键是否在下方没有使用事件的情况下使用, 如在核心游戏循环中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 检查的钥匙 看看它是不是刚刚下来。 |


**返回值:** boolean - 如果按键是按的,那么就按`true`,否则按`false`.


> 源码：[src/input/keyboard/keys/JustDown.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/JustDown.js#L7)  
引入版本：3.0.0


### JustUp {#JustUp}

#### \<static> JustUp(key) {#static-justupkey}


**说明:**

justUp值允许您测试此键是否刚刚被发布 。

检查此值时, 将返回 `true` 如果钥匙是上,否则 `false`.

您只能每一次调用 JustUp 键。 它只能返回一次 `true`, 直到按下键并再次放出。 这样您就可以在您想要检查是否该键升起时使用它, 如在核心游戏循环中使用此键 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 | 检查的钥匙 看看是不是刚刚起步 |


**返回值:** boolean - 如果钥匙刚刚放出来,就用`true`,否则用`false`.


> 源码：[src/input/keyboard/keys/JustUp.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/JustUp.js#L7)  
引入版本：3.0.0


### UpDuration {#UpDuration}

#### \<static> UpDuration(key, [duration]) {#static-updurationkey-duration}


**说明:**

如果键在给定的 `duration` 值范围内释放, 则返回 `true`。 如果键尚未打开, 或者比给定的时钟时间早释放, 返回 `false` 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | [Phaser.Input.Keyboard.Key](/api/class/input-keyboard-key) | 否 |  | 要测试的键对象 。 |
| duration | number | 是 | 50 | 时间,以毫秒计,其中键必须已经放出. |


**返回值:** boolean - 如果钥匙在`duration` mss 之前就释放了,那么就用`true`,否则用`false`.


> 源码：[src/input/keyboard/keys/UpDuration.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/keyboard/keys/UpDuration.js#L7)  
引入版本：3.0.0

---
