# AnimationManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/animations-animationmanager)

动画管理器是一个全球系统,负责定义、存储和管理您 Phaser游戏中的所有动画。 它是Game 实例拥有的单调,意思是它在所有的Scenes中坚持,并且不与任何单一Scene的生命周期挂钩。

您通过 `this.anims.create()`( 或 A`this.anims.createFromAseprite()` 用于 Aseprite 输出) 制作过动画, 这些动画随后可以提供给每个有动画组件的Sprite 或 Game Object, 遍及每个场景 。

动画管理器处理帧排序,计时,以及播放的配置. 单个游戏对象通过动画状态组件各自保持自己的播放状态(当前帧,重复计数等),但帧数据和计时定义在此居住.

您可以通过 `this.anims` 从任意场景访问动画管理器 。

**构造函数**

`new AnimationManager(game)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 参考Phaser.Game案例. |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/animations/AnimationManager.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L19)  
引入版本：3.0.0

## 公开成员 {#public-members}

### anims {#anims}

#### anims: Phaser.Structs.Map.\<string, [Phaser.Animations.Animation](/api/class/animations-animation)> {#anims-phaserstructsmapstring-phaseranimationsanimation}


**说明:**

动画在动画管理器中注册.

此地图应随动画管理器的[#add](#add)和[#create](#create)方法而修改.


**访问权限:** 受保护


> 源码：[src/animations/AnimationManager.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L85)  
引入版本：3.0.0


---

### game {#game}

#### game: [Phaser.Game](/api/class/game) {#game-phasergame}


**说明:**

参考Phaser.Game案例.


**访问权限:** 受保护


> 源码：[src/animations/AnimationManager.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L53)  
引入版本：3.0.0


---

### globalTimeScale {#globalTimeScale}

#### globalTimeScale: number {#globaltimescale-number}


**说明:**

动画管理器的全球时标.

这在两个帧之间缩放时间三角洲,从而影响动画管理器的时间速度.


> 源码：[src/animations/AnimationManager.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L73)  
引入版本：3.0.0


---

### mixes {#mixes}

#### mixes: Phaser.Structs.Map.\<string, [Phaser.Animations.Animation](/api/class/animations-animation)> {#mixes-phaserstructsmapstring-phaseranimationsanimation}


**说明:**

动画混音时间列表.

详见[#setMix](https://phaser.io/oss/docs/api-documentation/class/animations-animationmanager#setMix)方法.


> 源码：[src/animations/AnimationManager.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L97)  
引入版本：3.50.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

此动画管理器的名称.


> 源码：[src/animations/AnimationManager.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L118)  
引入版本：3.0.0


---

### paused {#paused}

#### paused: boolean {#paused-boolean}


**说明:**

动画管理器是否随其所有动画一起暂停.


> 源码：[src/animations/AnimationManager.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L108)  
引入版本：3.0.0


---

### textureManager {#textureManager}

#### textureManager: [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) {#texturemanager-phasertexturestexturemanager}


**说明:**

纹理管理器的参考文献.


**访问权限:** 受保护


> 源码：[src/animations/AnimationManager.js#L63](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L63)  
引入版本：3.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)
 - [shutdown](/api/class/events-eventemitter#shutdown)




---

## 公开方法 {#public-methods}

### add {#add}

#### \<instance> add(key, animation) {#instance-addkey-animation}


**说明:**

将已有的动画添加到动画管理器中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 添加动画的键。 动画将随其更新, 必须是独一无二的 。 |
| animation | [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 动画管理器中应当添加的动画. |


**返回值:** [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) - 此动画管理器.


**触发事件:** [Phaser.Animations.Events#event:ADD_ANIMATION](/api/event/animations-events#add_animation)


> 源码：[src/animations/AnimationManager.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L282)  
引入版本：3.0.0


---

### addMix {#addMix}

#### \<instance> addMix(animA, animB, delay) {#instance-addmixanima-animb-delay}


**说明:**

将两个动画加成混合。

混合可以指定动画对齐之间独特的延迟.

在游戏对象上播放动画A时,如果再播放动画B,并存在混音,则会等待指定的延迟结束后再播放动画B.

这使得您可以自定义不同类型动画之间的平滑,比如在闲置状态和行走状态之间混合,或者运行状态和射击状态.

请注意, 混合只有在使用 `Sprite.play` 方法时才会使用。 如果您选择使用 `playAfterRepeat` 或 `playAfterDelay` , 则这些方法优先使用, 混合延迟不会使用 。

要更新现有的组合,只需用新的延迟调用这种方法.

要移除混合配对,请参见`removeMix`方法.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animA | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 基于字符串的键,或称动画A的例子. |
| animB | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 以字符串为基础的键,或称动画B的例子. |
| delay | number | 否 | 延迟,以毫秒计,等待从动画A到B的过渡时. |


**返回值:** [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) - 此动画管理器.


> 源码：[src/animations/AnimationManager.js#L144](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L144)  
引入版本：3.50.0


---

### boot {#boot}

#### \<instance> boot() {#instance-boot}


**说明:**

游戏靴后注册事件监听器.


> 源码：[src/animations/AnimationManager.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L130)  
引入版本：3.0.0


---

### create {#create}

#### \<instance> create(config) {#instance-createconfig}


**说明:**

创建新动画并添加到动画管理器中.

动画是全球性的。 动画一旦创建, 您可以在游戏中任意场景中使用, 而不是特定场景 。

如果给定了一个无效的键, 此方法将返回 `false` 。

如果您通过动画管理器中已经存在的动画的键,该动画将被返回.

只有在键有效且尚未使用时,才会创建全新的动画.

如果您希望重新使用已有的键, 请先拨打 `AnimationManager.remove`, 然后拨打这种方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.Animations.Animation](/api/typedef/types-animations#animation) | 否 | 动画的配置设置 。 |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation), false - 创建的动画, 或者如果键已经使用的话, `false` 。


**触发事件:** [Phaser.Animations.Events#event:ADD_ANIMATION](/api/event/animations-events#add_animation)


> 源码：[src/animations/AnimationManager.js#L498](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L498)  
引入版本：3.0.0


---

### createFromAseprite {#createFromAseprite}

#### \<instance> createFromAseprite(key, [tags], [target]) {#instance-createfromasepritekey-tags-target}


**说明:**

从装入的 Aseprite JSON 文件创建一个或多个动画 。

Aseprite是一个强大的动画图案编辑器和像素艺术工具.

您可以在 [https://www.aseprite.org/](https://www.aseprite.org/) 找到更多细节

要在 Aseprite 中导出兼容的 JSON 文件, 请做以下操作 :

1. 转到“ 文件 - 导出工作表”

2. 标签上写着:

2a. 设置“ 套座类型” 为“ 套座”

2b 设置"约束"为"无".

2c. 请检查date=中的日期值 (帮助) "Morge Reverses" 复本复选框

3. 标签上:

3a. 将“ 线条” 设置为“ 可见层 ”

3b. 将“ Frames” 设定为“ 所有框架”,除非您仅希望导出一组子标签

4. 在**边界**标签上:

4a. 请检查date=中的日期值 (帮助) "Trim Sprite"和"Trim Cells"选项

4b. 确保“边境铺设”、“间隔”和“内部铺设”均大于0(1通常足够)

5. 在**产出**标签上:

5a. 检查“ 输出文件” , 给您图像一个名称, 并确保您选择“ png 文件” 作为文件类型

5b. 检查"JSON Data",并给您的Json文件一个名字

5c. JSON Data类型可以是哈什或阵列,Phaser不介意.

5d. 确保“ Tags” 在 Meta 选项中被检查

5e. 在“项目文件名” 输入框中,请确保只写“ {frame} ” , 仅此而已 。

6. 单击导出

测试时采用了Aeprite 1.2.25.

这将导出一个 png 和 json 文件, 您可以使用 Aseprite 资源加载器装入, 即 :

```javascript
function preload ()
{
    this.load.path = 'assets/animations/aseprite/';
    this.load.aseprite('paladin', 'paladin.png', 'paladin.json');
}
```

一旦装入,您可以从“ atlas” 键的场景内调用这种方法 :

```javascript
this.anims.createFromAseprite('paladin');
```

JSON中定义的任何动画现在都可以在Phaser中使用,您通过他们的标签名称来播放。例如,如果您在您的Aseprite时间表中有名为“战争哭”的动画,您可以使用该标签名称在Phaser中播放:

```javascript
this.add.sprite(400, 300).play('War Cry');
```

在调用此方法时, 您可以选择提供一系列标记名称, 只有这些动画才会被创建 。 例如 :

```javascript
this.anims.createFromAseprite('paladin', [ 'step', 'War Cry', 'Magnum Break' ]);
```

这将只创建定义的 3 个动画。 请注意, 标记名称是区分大小写 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 装入的 Aseprite 地图集的键。 它一定是在调用此方法之前装入的 。 |
| tags | Array.\<string> | 是 | 标记名称的数组。 如果提供了, 将只创建此数组中的动画 。 |
| target | [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) \| [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 是 | 创建此目标 Sprite 上的动画。 如果不给出, 将在此动画管理器中在全球创建 。 |


**返回值:** Array.\<[Phaser.Animations.Animation](/api/class/animations-animation)> - 成功创建的动画实例数组 。


> 源码：[src/animations/AnimationManager.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L329)  
引入版本：3.50.0


---

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

销毁此动画管理器并清理动画定义和对其他对象的引用。 这种方法不应直接调用。 它将自动调用, 作为对 Phaser.Game 实例中的 `destroy` 事件的回应 。


**重写:** Phaser.Events.EventEmitter#销毁


> 源码：[src/animations/AnimationManager.js#L1056](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L1056)  
引入版本：3.0.0


---

### exists {#exists}

#### \<instance> exists(key) {#instance-existskey}


**说明:**

检查是否在动画管理器内已经使用给定的键 。

动画是全局的。 一个场景中创建的键可以从游戏中的任何其他场景中使用, 它们不是场景特定 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 动画的钥匙来检查. |


**返回值:** boolean - `true`如果动画在动画管理器中已经存在,或者如果有键,则`false`.


> 源码：[src/animations/AnimationManager.js#L312](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L312)  
引入版本：3.16.0


---

### fromJSON {#fromJSON}

#### \<instance> fromJSON(data, [clearCurrentAnimations]) {#instance-fromjsondata-clearcurrentanimations}


**说明:**

从 JSON 对象装入此动画管理器的动画和设置 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | string \| [Phaser.Types.Animations.JSONAnimations](/api/typedef/types-animations#jsonanimations) | [Phaser.Types.Animations.JSONAnimation](/api/typedef/types-animations#jsonanimation) | 否 |  | JSON反对分析. |
| clearCurrentAnimations | boolean | 是 | false | 如果设置为 `true`, 则将删除当前动画( `anims.clear()`) 。 如果设置为 `false`( 默认) , 则将添加 `data` 中的动画 。 |


**返回值:** Array.\<[Phaser.Animations.Animation](/api/class/animations-animation)> - 包含所有因此调用而创建的动画对象的阵列.


> 源码：[src/animations/AnimationManager.js#L546](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L546)  
引入版本：3.0.0


---

### generateFrameNames {#generateFrameNames}

#### \<instance> generateFrameNames(key, [config]) {#instance-generateframenameskey-config}


**说明:**

从纹理键和配置对象生成 [Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe) 对象的阵列 。

生成基于字符串的框架名称的对象,由给定的 [Phaser.Types.Animations.GenerateFrameNames](/api/typedef/types-animations#generateframenames) 配置.

这是一个帮助方法,旨在方便您从纹理图集中提取所有框架名称.

如果你用一个精灵表工作, 请参看 `generateFrameNumbers` 方法。

Example:

如果你有一个纹理图集,叫做`gems`, 里面有6个框架,叫做`ruby_0001`,`ruby_0002`等等, 你可以使用:`this.anims.generateFrameNames('gems', { prefix: 'ruby_', start: 1, end: 6, zeroPad: 4 })`来称呼这个方法。

`end`值告诉它选择帧 1 到 6, 递增编号, 全部从前缀 `ruby_`开始。 `zeroPad`值告诉它有多少零 将数字固定在外。 要用这种方法创建动画, 您可以:

```javascript
this.anims.create({
  key: 'ruby',
  repeat: -1,
  frames: this.anims.generateFrameNames('gems', {
    prefix: 'ruby_',
    end: 6,
    zeroPad: 4
  })
});
```

详情请参见动画示例.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 包含动画帧的纹理的键. |
| config | [Phaser.Types.Animations.GenerateFrameNames](/api/typedef/types-animations#generateframenames) | 是 | 动画框架名称的配置对象. |


**返回值:** Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> - [Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)物体的阵列。


> 源码：[src/animations/AnimationManager.js#L595](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L595)  
引入版本：3.0.0


---

### generateFrameNumbers {#generateFrameNumbers}

#### \<instance> generateFrameNumbers(key, [config]) {#instance-generateframenumberskey-config}


**说明:**

从纹理键和配置对象生成 [Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe) 对象的阵列 。

生成带有编号框架名称的物体, 由给定的 [Phaser.Types.Animations.GenerateFrameNumbers](/api/typedef/types-animations#generateframenumbers) 配置 。

如果你正在用纹理图集工作,请参见`generateFrameNames`方法.

这是一种帮助方法,旨在方便您从精灵表提取帧.

Example:

如果您有一个名为`explosion`的精灵表,其中包含12帧,那么您就可以使用下列方法调用这种方法:

`this.anims.generateFrameNumbers('explosion', { start: 0, end: 11 })`.

`end`值11表示在12帧加成后停止,因为其开始时间为0.

要使用这种方法创建动画,你可以:

```javascript
this.anims.create({
  key: 'boom',
  frames: this.anims.generateFrameNumbers('explosion', {
    start: 0,
    end: 11
  })
});
```

注意`start`是可选的,如果动画从帧0开始,则不需要包含.

要指定反向动画, 请将 `start` 和 `end` 值互换 。

如果帧不是顺序的,您可以通过一个帧数组,例如:

`this.anims.generateFrameNumbers('explosion', { frames: [ 0, 1, 2, 1, 2, 3, 4, 0, 1, 2 ] })`

请参看动画示例和 `GenerateFrameNumbers` 配置文件,以了解更多细节。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 包含动画帧的纹理的键. |
| config | [Phaser.Types.Animations.GenerateFrameNumbers](/api/typedef/types-animations#generateframenumbers) | 是 | 动画框架的配置对象 。 |


**返回值:** Array.\<[Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)> - [Phaser.Types.Animations.AnimationFrame](/api/typedef/types-animations#animationframe)物体的阵列。


> 源码：[src/animations/AnimationManager.js#L695](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L695)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get(key) {#instance-getkey}


**说明:**

以键向动画管理器获取动画.

如果没有给定的键动画存在, 返回 `undefined` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 动画的钥匙要取回. |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 动画.


> 源码：[src/animations/AnimationManager.js#L799](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L799)  
引入版本：3.0.0


---

### getAnimsFromTexture {#getAnimsFromTexture}

#### \<instance> getAnimsFromTexture(key) {#instance-getanimsfromtexturekey}


**说明:**

返回使用给定的纹理的所有动画键的数组。结果中将包含的只有至少一个使用此纹理的动画Frame条目的动画。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Textures.Texture](/api/class/textures-texture) | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 | 纹理,或纹理,或框架实例中唯一基于字符串的键 。 |


**返回值:** Array.\<string> - 具有给定纹理特征的动画键阵列。


> 源码：[src/animations/AnimationManager.js#L816](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L816)  
引入版本：3.60.0


---

### getMix {#getMix}

#### \<instance> getMix(animA, animB) {#instance-getmixanima-animb}


**说明:**

返回两个动画之间的混合延迟。

如果没有设置混音,此方法将返回0.

如果您想要创建或更新新的组合,请使用 `addMix` 方法。如果想要删除组合,请使用 `removeMix` 方法。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animA | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 基于字符串的键,或称动画A的例子. |
| animB | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 以字符串为基础的键,或称动画B的例子. |


**返回值:** number - 混合时间, 如果没有混合, 则为零 。


> 源码：[src/animations/AnimationManager.js#L247](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L247)  
引入版本：3.50.0


---

### pauseAll {#pauseAll}

#### \<instance> pauseAll() {#instance-pauseall}


**说明:**

将 `paused` 旗子设置为 `true` , 暂停动画管理器中的所有动画。 这影响到全球所有正在播放动画的游戏对象。 如果动画管理器已经暂停, 则没有效果 。


**返回值:** [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) - 此动画管理器.


**触发事件:** [Phaser.Animations.Events#event:PAUSE_ALL](/api/event/animations-events#pause_all)


> 源码：[src/animations/AnimationManager.js#L856](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L856)  
引入版本：3.0.0


---

### play {#play}

#### \<instance> play(key, children) {#instance-playkey-children}


**说明:**

在给定的游戏对象上播放具有动画组件的动画.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| children | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 | 游戏对象阵列可以播放动画。 它们必须有动画组件 。 |


**返回值:** [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) - 此动画管理器.


> 源码：[src/animations/AnimationManager.js#L879](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L879)  
引入版本：3.0.0


---

### remove {#remove}

#### \<instance> remove(key) {#instance-removekey}


**说明:**

根据给定的键,从此动画管理器中删除动画 。

这是一个全球动作。 一旦动画被移除, 游戏对象无法继续使用它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 要删除的动画键 。 |


**返回值:** [Phaser.Animations.Animation](/api/class/animations-animation) - 动画管理器中被删除的动画实例.


**触发事件:** [Phaser.Animations.Events#event:REMOVE_ANIMATION](/api/event/animations-events#remove_animation)


> 源码：[src/animations/AnimationManager.js#L971](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L971)  
引入版本：3.0.0


---

### removeMix {#removeMix}

#### \<instance> removeMix(animA, [animB]) {#instance-removemixanima-animb}


**说明:**

删除两个动画的混合。

混合可以指定动画对齐之间独特的延迟.

调用这种方法可以删除这些配对。 您可以在 `animA` 和 `animB` 之间删除, 或者不提供 `animB` 参数, 它会删除所有 `animA` 组合 。

如果您想更新已有的混音, 请使用新的延迟调用 `addMix` 方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| animA | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | 否 | 基于字符串的键,或称动画A的例子. |
| animB | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | 是 | 基于字符串键,或称动画B的例子。如果不给出,动画A的所有混音都会被删除。 |


**返回值:** [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) - 此动画管理器.


> 源码：[src/animations/AnimationManager.js#L197](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L197)  
引入版本：3.50.0


---

### resumeAll {#resumeAll}

#### \<instance> resumeAll() {#instance-resumeall}


**说明:**

将动画管理器中的所有暂停动画都恢复为 `paused` 旗下 `false` 。 如果动画管理器目前没有暂停, 则无效 。


**返回值:** [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) - 此动画管理器.


**触发事件:** [Phaser.Animations.Events#event:RESUME_ALL](/api/event/animations-events#resume_all)


> 源码：[src/animations/AnimationManager.js#L1001](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L1001)  
引入版本：3.0.0


---

### staggerPlay {#staggerPlay}

#### \<instance> staggerPlay(key, children, stagger, [staggerFirst]) {#instance-staggerplaykey-children-stagger-staggerfirst}


**说明:**

使用一系列具有动画组件的游戏对象,然后开始在它们上播放给定的动画。每个游戏对象的起始时间由`stagger`金额递增抵消。

例如,如果通过一个有4个孩子的阵列,并交错时间为1000,则延迟将是:

儿童1:1000ms 延迟 儿童2:2000ms 延迟 儿童3:3000ms 延迟 儿童4:4000ms 延迟 儿童:4000ms 延迟 儿童:4000ms 延迟 儿童:4000ms 延迟 儿童:4000m 延迟 儿童:4000m 延迟 儿童:4000m 延迟 儿童:4000m 延迟 儿童:4000m 延迟 儿童:4000m 延迟 儿童:4000m 延迟 儿童:4,3000 m 延迟 儿童:4000m 延迟 儿童:4000m 延迟 儿童:4000 m 延迟 儿童:4,4 000 m 延迟 儿童:4 000 m 延迟 延迟 延迟 儿童: 儿童:

如果你把`staggerFirst`参数设置到`false`,它们将是:

儿童1:0 ms 延迟 儿童2:1000 ms 延迟 儿童3:2000 ms 延迟 儿童4:3000 ms 延迟 儿童4:3000 ms 延迟 儿童4:3000 ms 延迟 儿童4:3000 ms 延迟 儿童4:3000 ms 延迟 儿童4:3000 ms 延迟 延迟 儿童4:3:3:3000 m 延迟 延迟 儿童4:3000 ms 延迟 儿童4:3000 ms 延迟 延迟 儿童4:3000 ms 延迟 延迟 儿童4:3000 ms 延迟 延迟 儿童4:3:3 000 ms 延迟 延迟 延迟 延迟 儿童3: 延迟 –3: 1: 1,0 ms 延迟 延迟 儿童3: 延迟 儿童3 000 ms 延迟 延迟 延迟 儿童3: 延迟 儿童3: 延迟 儿童3: 儿童3 000 ms 延迟 延迟 延迟 儿童3: 儿童4: 儿童4: 儿童4:

您也可以将 `stagger` 设置为负值。 如果为 -1000, 则以上为 :

儿童1:3000ms 延迟 儿童2:2000ms 延迟 儿童3:1000ms 延迟 儿童4:0ms 延迟 儿童4:0ms 延迟 儿童4:0 ms 延迟 儿童4:0 ms 延迟 儿童4:0 ms 延迟 儿童4:0 ms 延迟 儿童4:0 ms 延迟 延迟 儿童4:0 ms 延迟 延迟 儿童4:0 ms 延迟 延迟 儿童4:0 ms 延迟 延迟 儿童4:0 ms 延迟 延迟 儿童4:0 ms 延迟 延迟 儿童4:0 ms 延迟 延迟 儿童3:1000 ms 延迟 儿童4: 延迟 儿童4:0 ms 延迟 延迟 儿童4:0 ms 延迟 延迟 儿童4:0 ms 延迟 延迟 儿童4: 延迟 儿童4:0 m 延迟 儿童3: 延迟 延迟 延迟 延迟 儿童3: 儿童3 000 ms 延迟 延迟 延迟 儿童3: 延迟 儿童3 000 ms 延迟 儿童3: 延迟 儿童3: 儿童3: 儿童3 m m m m 延迟 儿童3: 儿童3 m 儿童3 延迟 延迟 儿童3: 延迟 儿童3 延迟 儿童3 000 ms 延迟 儿童3 儿童3 儿童3 儿童3 ms 延迟 延迟 儿童3 ms 儿童 儿童 延迟 儿童 儿童3 延迟 儿童 儿童3 儿童3: 延迟 延迟 儿童3 儿童 延迟 儿童3 儿童 儿童3: 儿童3: 儿童3 儿童 儿童 儿童 儿童 儿童3 儿童3 000 ms 延迟 儿童 延迟 儿童3 儿童3 儿童3 儿童 儿童3 儿童3 儿童3 儿童3 儿童3 儿童3: 儿童3 儿童3

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Animations.Animation](/api/class/animations-animation) | [Phaser.Types.Animations.PlayAnimationConfig](/api/typedef/types-animations#playanimationconfig) | 否 |  | 动画要播放的字符串键,或动画实例,或`PlayAnimationConfig`对象. |
| children | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) \| Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 游戏对象阵列可以播放动画。 它们必须有动画组件 。 |
| stagger | number | 否 |  | 时间的长度, 以毫秒表示, 以每场游戏的时间抵消。 如果给出负值, 则按反向顺序适用于孩子们 。 |
| staggerFirst | boolean | 是 | true | 是否也应错开第一个孩子的间隔? |


**返回值:** [Phaser.Animations.AnimationManager](/api/class/animations-animationmanager) - 此动画管理器.


> 源码：[src/animations/AnimationManager.js#L905](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L905)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON([key]) {#instance-tojsonkey}


**说明:**

返回基于给定键的动画数据为 JavaScript 对象。或者,如果没有定义键,它会返回所有动画的数据为对象的数组。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 是 | 要从 JSON 动画数据获取的动画。 如果不提供, 所有动画都将作为一个阵列返回 。 |


**返回值:** [Phaser.Types.Animations.JSONAnimations](/api/typedef/types-animations#jsonanimations) - 由此而来的 JSON 动画格式化对象 。


> 源码：[src/animations/AnimationManager.js#L1023](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationManager.js#L1023)  
引入版本：3.0.0


---

---
