# GameObject {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-gameobject)

Phaser中所有游戏对象扩展的基类.

一个游戏对象是任何可以添加到Scene显示列表中并被渲染到屏幕上的东西,例如Sprite,Image,Text,或Graphics对象. Game Objects是每个Phaser游戏的构件——它们代表生活在Scene的视觉实体,可以被定位,缩放,旋转,并与它们互动.

本类提供所有游戏对象使用的核心共享功能:生命周期管理(主动/销毁),通过数据管理器存储数据,输入处理,物理体附件,显示列表和更新列表成员,以及事件排放.

您不直接即时使用 `GameObject`。 相反, 使用它作为您自定义的游戏对象类型的基础类, 方法是通过 Phaser的 `Class` 工具扩展它, 或者简单地使用 Phaser 提供的众多内置游戏对象类型之一 。

**构造函数**

`new GameObject(scene, type)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 此游戏对象所属景点 。 |
| 类型 | string | 否 | 游戏对象类型文字表达,即`sprite`. |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  
> [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters)  
> [Phaser.GameObjects.Components.RenderSteps](/api/namespace/gameobjects-components-rendersteps)  



> 源码：[src/gameobjects/GameObject.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L15)  
引入版本：3.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters):**


 - [filterCamera](/api/namespace/gameobjects-components-filters#filterCamera)
 - [filters](/api/namespace/gameobjects-components-filters#filters)
 - [filtersAutoFocus](/api/namespace/gameobjects-components-filters#filtersAutoFocus)
 - [filtersFocusContext](/api/namespace/gameobjects-components-filters#filtersFocusContext)
 - [filtersForceComposite](/api/namespace/gameobjects-components-filters#filtersForceComposite)
 - [maxFilterSize](/api/namespace/gameobjects-components-filters#maxFilterSize)
 - [renderFilters](/api/namespace/gameobjects-components-filters#renderFilters)




---

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

此游戏对象的活跃状态。 一个活动状态为 `true` 的游戏对象, 如果添加到其中, 则由 Scens 更新列表处理。 一个活动对象就是正在更新其逻辑和内部系统 。


> 源码：[src/gameobjects/GameObject.js#L133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L133)  
引入版本：3.0.0


---

### body {#body}

#### body: [Phaser.Physics.Arcade.Body](/api/class/physics-arcade-body), [Phaser.Physics.Arcade.StaticBody](/api/class/physics-arcade-staticbody), MatterJS.BodyType {#body-phaserphysicsarcadebody-phaserphysicsarcadestaticbody-matterjsbodytype}


**说明:**

如果启用此游戏对象用于Arcade或Matter 物理, 那么此属性将包含一个物理实体的引用 。


> 源码：[src/gameobjects/GameObject.js#L235](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L235)  
引入版本：3.0.0


---

### cameraFilter {#cameraFilter}

#### cameraFilter: number {#camerafilter-number}


**说明:**

如果此游戏对象是否由摄像机绘制, 控制此位码。 通常不直接设定, 而是直接调用 `Camera.ignore`, 但是您可以直接使用摄像机设置此属性 。 id 属性 :


> 源码：[src/gameobjects/GameObject.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L180)  
引入版本：3.0.0


---

### data {#data}

#### data: [Phaser.Data.DataManager](/api/class/data-datamanager) {#data-phaserdatadatamanager}


**说明:**

数据管理器。 它允许您存储、 查询和获取此游戏对象特有的键/ 值配对信息。 `null` 默认情况下, 如果您使用 `getData` 或 `setData` 或 `setDataEnabled` , 将自动创建 。


> 源码：[src/gameobjects/GameObject.js#L156](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L156)  
引入版本：3.0.0


---

### displayList {#displayList}

#### displayList: [Phaser.GameObjects.DisplayList](/api/class/gameobjects-displaylist), [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) {#displaylist-phasergameobjectsdisplaylist-phasergameobjectslayer}


**说明:**

持有包含此游戏对象的显示列表的引用。

当此游戏对象被添加到场景或层中时,此设定会自动设定 。

你应该把这地产当做只读


> 源码：[src/gameobjects/GameObject.js#L73](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L73)  
引入版本：3.50.0


---

### ignoreDestroy {#ignoreDestroy}

#### ignoreDestroy: boolean {#ignoredestroy-boolean}


**说明:**

此游戏对象会忽略所有针对其毁灭方法的呼叫, 如果此旗被设定为 `true` 的话。 包括来自 Group、 Controol 或 Scene 本身的呼叫。 虽然它允许您在 Scenes 上坚持一个游戏对象, 请理解您完全负责对游戏对象的引用和引用的管理 。


> 源码：[src/gameobjects/GameObject.js#L245](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L245)  
引入版本：3.5.0


---

### input {#input}

#### input: [Phaser.Types.Input.InteractiveObject](/api/typedef/types-input#interactiveobject) {#input-phasertypesinputinteractiveobject}


**说明:**

如果启用此游戏对象输入, 此属性将包含一个交互式对象实例。 通常不直接设置。 相反, 请调用 `GameObject.setInteractive()` 。


> 源码：[src/gameobjects/GameObject.js#L224](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L224)  
引入版本：3.0.0


---

### isDestroyed {#isDestroyed}

#### isDestroyed: boolean {#isdestroyed-boolean}


**说明:**

是否此游戏对象已被销毁 。 请检查此属性, 以避免在已销毁的游戏对象上调用方法导致的错误, 例如在 Tween 或 Timer 中 。

这是游戏对象被破坏时自动设置为 `true` 的只读属性。 您不应该直接设置此属性。 它被设定在 `preDestroy` 调用或 DESTROY 事件被发布之前 。


> 源码：[src/gameobjects/GameObject.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L258)  
引入版本：4.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

此游戏对象的名称。 默认情况下是空的, 并且从未被 Phaser 所覆盖, 留给开发者使用 。


> 源码：[src/gameobjects/GameObject.js#L122](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L122)  
引入版本：3.0.0


---

### parentContainer {#parentContainer}

#### parentContainer: [Phaser.GameObjects.Container](/api/class/gameobjects-container) {#parentcontainer-phasergameobjectscontainer}


**说明:**

如果有, 此游戏对象的父容器 。


> 源码：[src/gameobjects/GameObject.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L113)  
引入版本：3.4.0


---

### renderFlags {#renderFlags}

#### renderFlags: number {#renderflags-number}


**说明:**

对比 `RENDER_MASK` 的旗帜来确定此游戏对象是否渲染。 位点分别为 0001 \ 0010\ 0100\ 1000, 由组件可视、 Alpha、 变形和纹理设置。 如果您的自定义类没有使用这些组件, 您可以随意使用此位图 。


> 源码：[src/gameobjects/GameObject.js#L168](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L168)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

引用此游戏对象所属的景色 。

游戏对象只能属于一个场景.

您应该将此属性视为只读。 您不能简单地更改它, 而将游戏对象移动到另一个场景 。


> 源码：[src/gameobjects/GameObject.js#L59](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L59)  
引入版本：3.0.0


---

### state {#state}

#### state: number, string {#state-number-string}


**说明:**

此游戏对象的当前状态 。

Phaser本身永远不会修改这个值,尽管插件可能这样做.

使用此属性来跟踪游戏对象在存在期间的状态。 例如, 它可以从“ 移动” 状态变为“ 攻击” 状态, 变为“ 死亡 ” 状态值应该是一个整数( 理想地映射到游戏代码中的常数) , 或者一个字符串。 这些属性被推荐来保持它轻而易举, 并进行快速的比较 。 如果您需要存储关于游戏对象的复杂数据, 请查看数据组件的使用情况 。


> 源码：[src/gameobjects/GameObject.js#L97](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L97)  
引入版本：3.16.0


---

### tabIndex {#tabIndex}

#### tabIndex: number {#tabindex-number}


**说明:**

游戏对象的标签索引。 保留给插件和输入管理器用于未来使用 。


> 源码：[src/gameobjects/GameObject.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L145)  
引入版本：3.0.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

这个游戏对象的文字代表, 即 `sprite`。 由 Phaser 内部使用, 但可供您自定义的类使用 。


> 源码：[src/gameobjects/GameObject.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L87)  
引入版本：3.0.0


---

### vertexRoundMode {#vertexRoundMode}

#### vertexRoundMode: string {#vertexroundmode-string}


**说明:**

此游戏对象的当前顶点圆形模式。 用于确定圆形位置的 WebGL 渲染器。 它可以有多个值 :

- `off` - 不采用四舍五入法。

- `safe` - 如果对象是"安全",则采用圆形.

- `safeAuto` - 如果对象是"安全",且摄像机已启用`roundPixels`,则采用圆形.

- `full` - 圆圈式总是应用.

- `fullAuto` - 如果摄像机启用了`roundPixels`,则总是采用圆形.

A'safe' 对象是渲染时不会被任何变换矩阵旋转或缩放的对象。 有效的变换是一个简单的翻译。 在这种情况下, 舍入会同样影响所有顶点 。

使用全圆可以引起顶点摇动,因为它们可能不会与像素网格对齐. 全圆可以使一个简基看起来像PS1游戏.

如果您想要创建自己的自定义四舍五入模式,您可以使用其他值 。


> 源码：[src/gameobjects/GameObject.js#L195](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L195)  
引入版本：4.0.0


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





**From [Phaser.GameObjects.Components.Filters](/api/namespace/gameobjects-components-filters):**


 - [enableFilters](/api/namespace/gameobjects-components-filters#enableFilters)
 - [focusFilters](/api/namespace/gameobjects-components-filters#focusFilters)
 - [focusFiltersOnCamera](/api/namespace/gameobjects-components-filters#focusFiltersOnCamera)
 - [focusFiltersOverride](/api/namespace/gameobjects-components-filters#focusFiltersOverride)
 - [renderWebGLFilters](/api/namespace/gameobjects-components-filters#renderWebGLFilters)
 - [setFiltersAutoFocus](/api/namespace/gameobjects-components-filters#setFiltersAutoFocus)
 - [setFiltersFocusContext](/api/namespace/gameobjects-components-filters#setFiltersFocusContext)
 - [setFiltersForceComposite](/api/namespace/gameobjects-components-filters#setFiltersForceComposite)
 - [setFilterSize](/api/namespace/gameobjects-components-filters#setFilterSize)
 - [setRenderFilters](/api/namespace/gameobjects-components-filters#setRenderFilters)
 - [willRenderFilters](/api/namespace/gameobjects-components-filters#willRenderFilters)





**From [Phaser.GameObjects.Components.RenderSteps](/api/namespace/gameobjects-components-rendersteps):**


 - [addRenderStep](/api/namespace/gameobjects-components-rendersteps#addRenderStep)
 - [renderWebGLStep](/api/namespace/gameobjects-components-rendersteps#renderWebGLStep)




---

## 公开方法 {#public-methods}

### addedToScene {#addedToScene}

#### \<instance> addedToScene() {#instance-addedtoscene}


**说明:**

当游戏对象添加到场景时,会引用此调用 。

可以被自定义的游戏对象所覆盖,但要注意一些会使用此功能的游戏对象,如Sprites,将自己添加到更新列表中.

您也可以从此游戏对象中收听 `ADDED_TO_SCENE` 事件 。


> 源码：[src/gameobjects/GameObject.js#L635](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L635)  
引入版本：3.50.0


---

### addToDisplayList {#addToDisplayList}

#### \<instance> addToDisplayList([displayList]) {#instance-addtodisplaylistdisplaylist}


**说明:**

将此游戏对象添加到指定的显示列表。

如果没有指定显示列表,它将默认为本游戏对象所属景点所拥有的显示列表.

游戏对象只能在任何特定时间存在于一个显示列表上,但可以在它们之间自由移动.

如果在调用此方法时此游戏对象已经出现在另一个显示列表中, 则首先从中移除, 然后再添加到新列表中 。

您可以通过查看 `Phaser.GameObjects.GameObject#displayList` 属性来查询它正在运行的列表 。

如果游戏对象不在任何显示列表中, 它将不会被渲染。 如果您只是希望暂时禁用它来渲染, 请考虑使用 `setVisible` 方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| displayList | [Phaser.GameObjects.DisplayList](/api/class/gameobjects-displaylist) \| [Phaser.GameObjects.Layer](/api/class/gameobjects-layer) | 是 | 显示列表将添加。 默认为场景显示列表 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 此游戏对象 。


**触发事件:** [Phaser.Scenes.Events#event:ADDED_TO_SCENE](/api/event/scenes-events#added_to_scene), [Phaser.GameObjects.Events#event:ADDED_TO_SCENE](/api/event/gameobjects-events#added_to_scene)


> 源码：[src/gameobjects/GameObject.js#L816](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L816)  
引入版本：3.53.0


---

### addToUpdateList {#addToUpdateList}

#### \<instance> addToUpdateList() {#instance-addtoupdatelist}


**说明:**

将此游戏对象添加到属于 Scene 的更新列表中。

当游戏对象被添加到更新列表中时, 它会拥有其`preUpdate`方法, 称为每个游戏框。 这个方法会通过两个参数: `time`和 `delta` 。

如果您想在 `preUpdate` 中运行自己的逻辑,那么您应该总是在其中调用 `super.preUpdate(time, delta)`, 或者它可能无法处理所需的操作, 如 Sprite 动画 。


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 此游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L867](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L867)  
引入版本：3.53.0


---

### destroy {#destroy}

#### \<instance> destroy([fromScene]) {#instance-destroyfromscene}


**说明:**

销毁此游戏对象从“ 显示列表” 和更新列表中移除, 并切除与父资源的所有链接 。

如果先前启用, 也会从输入管理器和物理管理器中移除自己 。

如果您再也没有计划使用, 请用此程序从游戏中移除一个对象。 只要您自己的代码中不存在任何提及, 浏览器就应该可以免费收集垃圾 。

如果您只是想要暂时禁用一个对象, 那么请看看使用游戏对象池而不是销毁它, 因为已销毁的对象无法复活 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| fromScene | boolean | 是 | false | `True` 如果游戏对象被场景所破坏, `false` 如果不是的话。 |


**重写:** Phaser.Events.EventEmitter#销毁


**触发事件:** [Phaser.GameObjects.Events#event:DESTROY](/api/event/gameobjects-events#destroy)


> 源码：[src/gameobjects/GameObject.js#L987](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L987)  
引入版本：3.0.0


---

### disableInteractive {#disableInteractive}

#### \<instance> disableInteractive([resetCursor]) {#instance-disableinteractiveresetcursor}


**说明:**

如果此游戏对象之前已启用可输入, 这将禁用它 。

一个被禁用用于输入的对象会停止处理或被考虑用于输入事件,但可以随时通过简单地拨打`setInteractive()`而再次恢复,而无需提供参数.

如果想要完全删除此游戏对象的交互,则使用`removeInteractive`来代替.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| resetCursor | boolean | 是 | false | 当前活动的输入光标( 如果有的话) 是否应该重置到默认光标上 ? |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L567](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L567)  
引入版本：3.7.0


---

### getData {#getData}

#### \<instance> getData(key) {#instance-getdatakey}


**说明:**

获取此游戏对象数据管理器中给定的键的值, 或者如果不存在, 则未定义 。

您也可以通过 `values` 对象访问值。 例如, 如果您有名为 `gold` 的键, 您也可以这样做 :

```javascript
sprite.getData('gold');
```

或者直接访问值 :

```javascript
sprite.data.values.gold;
```

您也可以在一系列键中通过,在这种情况下,返回一系列的值:

```javascript
sprite.getData([ 'gold', 'armor', 'health' ]);
```

这种方法对ES6中的分解数组有用.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| Array.\<string> | 否 | 要检索的值的键, 或一系列键 。 |


**返回值:** * - 属于给定键的值,或一系列值,其顺序将匹配输入数组.


> 源码：[src/gameobjects/GameObject.js#L489](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L489)  
引入版本：3.0.0


---

### getDisplayList {#getDisplayList}

#### \<instance> getDisplayList() {#instance-getdisplaylist}


**说明:**

返回包含此游戏对象的显示列表_array_的参考,如果有,该列表将要么是Scene的显示列表,要么是属于其父容器的内部列表。

如果此游戏对象不在显示列表或容器中,则会返回 `null`.

您应该非常小心地使用这种方法, 并且明白它返回了对“ 显示列表” 所使用的内部数组的直接引用。 直接改变这个数组会给游戏中的各种微妙和难解的问题带来各种调试问题 。


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 游戏对象的内部显示列表阵列,或`null`.


> 源码：[src/gameobjects/GameObject.js#L955](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L955)  
引入版本：3.85.0


---

### getIndexList {#getIndexList}

#### \<instance> getIndexList() {#instance-getindexlist}


**说明:**

返回包含此游戏对象的显示列表索引的数组, 或者如果它有一个, 其父容器。 然后它会通过所有父容器进行移动, 直到它击中显示列表的根( 返回的数组中为索引 0) 。

输入程序内部使用, 但如果您想要找到此游戏对象及其所有祖先的显示深度, 也会有用 。


**返回值:** Array.\<number> - 显示列表位置索引的数组 。


> 源码：[src/gameobjects/GameObject.js#L767](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L767)  
引入版本：3.4.0


---

### incData {#incData}

#### \<instance> incData(key, [amount]) {#instance-incdatakey-amount}


**说明:**

增加此游戏对象数据管理器中给定的键的值。 如果键在数据管理器中不存在, 则在增加前以 0 的值创建 。

如果游戏对象尚未启用数据( 通过 `setDataEnabled`), 那么在设定值前将启用 。

如果键在数据管理器中不存在,则它被创建.

当值首次设定时, 将会从此游戏对象中释放 `setdata` 事件 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 更改值的键 。 |
| amount | number | 是 | 1 | 将给定的键增加的金额。 传递负值来减少键 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L430](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L430)  
引入版本：3.23.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

当游戏对象从场景中移除时, 将引用此调用 。

可以被自定义的游戏对象覆盖,但要知道一些游戏对象会使用此功能,例如Sprites,从更新列表中去除自己.

您也可以从此游戏对象中收听 `REMOVED_FROM_SCENE` 事件 。


> 源码：[src/gameobjects/GameObject.js#L650](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L650)  
引入版本：3.50.0


---

### removeFromDisplayList {#removeFromDisplayList}

#### \<instance> removeFromDisplayList() {#instance-removefromdisplaylist}


**说明:**

从当前显示列表中删除此游戏对象。

一个游戏对象在任何特定时间只能在一个显示列表上存在,但可以在稍后阶段被自由删除并添加回来.

您可以通过查看 `Phaser.GameObjects.GameObject#displayList` 属性来查询它正在运行的列表 。

如果游戏对象不在任何显示列表中, 则不会被渲染。 如果您只是希望暂时禁用它来渲染, 请考虑使用 `setVisible` 方法 。


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 此游戏对象 。


**触发事件:** [Phaser.Scenes.Events#event:REMOVED_FROM_SCENE](/api/event/scenes-events#removed_from_scene), [Phaser.GameObjects.Events#event:REMOVED_FROM_SCENE](/api/event/gameobjects-events#removed_from_scene)


> 源码：[src/gameobjects/GameObject.js#L892](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L892)  
引入版本：3.53.0


---

### removeFromUpdateList {#removeFromUpdateList}

#### \<instance> removeFromUpdateList() {#instance-removefromupdatelist}


**说明:**

从场景更新列表中删除此游戏对象。

当游戏对象出现在更新列表中时, 它会使用它的 `preUpdate` 方法来调用每个游戏框。 调用这种方法会从列表中移除它, 防止它 。

从更新列表中删除游戏对象将停止大多数内部功能的工作。 例如, 从更新列表中删除一个 Sprite 将阻止它运行动画 。


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 此游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L930](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L930)  
引入版本：3.53.0


---

### removeInteractive {#removeInteractive}

#### \<instance> removeInteractive([resetCursor]) {#instance-removeinteractiveresetcursor}


**说明:**

如果此游戏对象之前已启用输入, 则会排队删除, 使其不再具有交互性。 删除发生在下一个游戏步骤上, 并不是立即的 。

分配给此游戏对象的交互对象将被销毁,从输入管理器中删除,并从此游戏对象清除.

如果您想在稍后日期重新启用此游戏对象, 您需要再次拨打 `setInteractive` 来重新创建其交互对象 。

如果您只希望暂时停止一个对象接收输入, 那么使用 `disableInteractive` 来代替, 因为这样会切换交互状态, 因为它会完全擦除它 。

如果您想要调整一个命中区域的大小, 请不要删除, 然后设定为交互。 相反, 直接访问命中区域对象并更改正在使用的形状大小 。 例如: `sprite.input.hitArea.setSize(width, height)`( 假设形状是矩形, 默认是矩形 。)

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| resetCursor | boolean | 是 | false | 当前活动的输入光标( 如果有的话) 是否应该重置到默认光标上 ? |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L592](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L592)  
引入版本：3.7.0


---

### setActive {#setActive}

#### \<instance> setActive(value) {#instance-setactivevalue}


**说明:**

设置此游戏对象的 `active` 属性, 并返回此游戏对象进行进一步的链路化。 游戏对象及其 `active` 属性将设置为 `true` 的属性, 由 Scens 更新列表更新 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 如果此游戏对象被设定为活动对象, 如果不是, 则为虚假 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L289](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L289)  
引入版本：3.0.0


---

### setData {#setData}

#### \<instance> setData(key, [value]) {#instance-setdatakey-value}


**说明:**

允许您在此游戏对象数据管理器中存储键值对 。

如果游戏对象尚未启用数据( 通过 `setDataEnabled`), 那么在设定值前将启用 。

如果键在数据管理器中不存在,则它被创建.

```javascript
sprite.setData('name', 'Red Gem Stone');
```

您也可以在键值对的对象中通过,作为第一个参数:

```javascript
sprite.setData({ name: 'Red Gem Stone', level: 2, owner: 'Link', gold: 50 });
```

为了重新获得一个值,你可以叫`getData`:

```javascript
sprite.getData('gold');
```

或者你可以直接通过`values`属性访问该值,在那里它像其他变量一样工作:

```javascript
sprite.data.values.gold += 50;
```

当值首次设定时, 将会从此游戏对象中释放 `setdata` 事件 。

如果键已经存在, 则会沿着以键命名的事件释放 `changedata`事件。 例如, 如果您更新了一个名为 `PlayerLives` 的现有键, 它会释放该事件 `changedata-PlayerLives`。 这些事件将会释放, 无论您使用这种方法设置值, 或直接的 `values` 设置器 。

请注意, 数据键是区分大小写, 必须有效 JavaScript 对象属性字符串。 这意味着, 数据管理器内将键 `gold` 和 `Gold` 视为两个独特的值 。

**标签:**

 - generic
 - genericUse

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| object | 否 | 设置值的键。 或者按键值对的对象。 如果对象忽略 `data` 参数 。 |
| value | * | 是 | 给定键设置的值。 如果一个对象作为键提供, 此参数将被忽略 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L368](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L368)  
引入版本：3.0.0


---

### setDataEnabled {#setDataEnabled}

#### \<instance> setDataEnabled() {#instance-setdataenabled}


**说明:**

将数据管理器组件添加到此游戏对象。


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L349](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L349)  
引入版本：3.0.0


---

### setInteractive {#setInteractive}

#### \<instance> setInteractive([hitArea], [callback], [dropZone]) {#instance-setinteractivehitarea-callback-dropzone}


**说明:**

将此游戏对象传递给输入管理器, 以启用它进行输入 。

输入通过使用命中区域来工作,这些几乎总是几何形状,如矩形或圆形,它们充当游戏对象的命中区域。但是,如果你想处理一些更先进的输入检测,你可以提供自己的命中区域形状和回调。

如果没有提供参数,它将尝试根据游戏对象使用的纹理帧创建矩形命中区域。如果这不是一个纹理约束对象,如图形或比特玛普Text对象,则会失败,需要提供它使用的具体形状。

您也可以提供输入配置对象作为这种方法的唯一参数。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| hitArea | [Phaser.Types.Input.InputConfiguration](/api/typedef/types-input#inputconfiguration) \| any | 是 |  | 输入配置对象, 或定义游戏对象的命中区域的几何形状。 如果不给定, 则会尝试根据纹理帧创建矩形 。 |
| callback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 |  | 用于确定指针是否在 Hit 区域形状之内的调用。 如果您提供了形状, 您也必须提供调用 。 |
| dropZone | boolean | 是 | false | 这个游戏对象是否应该被当作一个投放区目标? |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L529](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L529)  
引入版本：3.0.0


---

### setName {#setName}

#### \<instance> setName(value) {#instance-setnamevalue}


**说明:**

设置此游戏对象的 `name` 属性, 并返回此游戏对象进行进一步链路化。 `name` 属性没有 Phaser 的内含, 并提交您使用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | string | 否 | 给此游戏对象的名称 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L307)  
引入版本：3.0.0


---

### setState {#setState}

#### \<instance> setState(value) {#instance-setstatevalue}


**说明:**

设置此游戏对象的当前状态。

Phaser本身永远不会修改游戏对象的状态,尽管插件可能这样做.

例如,一个游戏对象可能会从“移动”状态变为“攻击”状态,变为“死亡”。状态值通常应该是整数(理想地映射到游戏代码中的常数),但也可以是字符串。建议保持其轻便和简单。如果需要存储关于游戏对象的复杂数据,请查看使用数据组件。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number \| string | 否 | 游戏对象的状态. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L325](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L325)  
引入版本：3.16.0


---

### setVertexRoundMode {#setVertexRoundMode}

#### \<instance> setVertexRoundMode(mode) {#instance-setvertexroundmodemode}


**说明:**

设定此游戏对象的顶点圆模式。 此模式被 WebGL 渲染器用于确定如何绕圆顶位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| mode | string | 否 | 要设定的顶点圆形模式。 可以是“ 关闭 ” 、 “ 安全 ” 。safeAuto', 'full' 或 '' 的词fullAuto'. |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L750](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L750)  
引入版本：4.0.0


---

### toggleData {#toggleData}

#### \<instance> toggleData(key) {#instance-toggledatakey}


**说明:**

切换此游戏对象数据管理器中给定的键的布尔值。 如果键在数据管理器中不存在, 则在切换到 `true` 之前, 将创建该键的值为 `false` 。

如果游戏对象尚未启用数据( 通过 `setDataEnabled`), 那么在设定值前将启用 。

如果键在数据管理器中不存在,则它被创建.

当值首次设定时, 将会从此游戏对象中释放 `setdata` 事件 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 切换值的关键 。 |


**返回值:** [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) - 这个游戏对象 。


> 源码：[src/gameobjects/GameObject.js#L460](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L460)  
引入版本：3.23.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

返回游戏对象的 JSON 表示式。


**返回值:** [Phaser.Types.GameObjects.JSONGameObject](/api/typedef/types-gameobjects#jsongameobject) - 游戏对象的JSON代表.


> 源码：[src/gameobjects/GameObject.js#L683](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L683)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update([args]) {#instance-updateargs}


**说明:**

覆盖此方法在您自定义的游戏对象中执行每帧更新逻辑。 如果游戏对象位于每款游戏框上的游戏对象, 则此方法会被Scene的更新列表所调用。 它不是自动调用 。 游戏对象必须通过 `addToUpdateList` 或拥有 `preUpdate` 方法添加到更新列表中 。

此基础执行是有意的空的,允许在对象池中使用游戏对象,而不需要任何更新逻辑.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| args | * | 是 | 任何被传递到更新方法的参数 。 |


> 源码：[src/gameobjects/GameObject.js#L665](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L665)  
引入版本：3.0.0


---

### willRender {#willRender}

#### \<instance> willRender(camera) {#instance-willrendercamera}


**说明:**

将 renderMask 和 renderFlags 比较,看看此游戏对象是否渲染。 还可以根据给定的摄像机排除列表检查游戏对象 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用于检查此游戏对象的摄像机 。 |


**返回值:** boolean - 如果游戏对象应该被渲染, 否则会弄虚作假 。


> 源码：[src/gameobjects/GameObject.js#L696](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L696)  
引入版本：3.0.0


---

### willRoundVertices {#willRoundVertices}

#### \<instance> willRoundVertices(camera, onlyTranslated) {#instance-willroundverticescamera-onlytranslated}


**说明:**

检查此游戏对象是否应该根据给定的摄像机和此游戏对象的`vertexRoundMode`来绕圆顶。 WebGL 渲染器使用此方法来决定如何绕圆顶位置 。

您可以在自定义的游戏对象类中覆盖这种方法,为顶点四舍五入提供自定义逻辑.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 用于检查此游戏对象的摄像机 。 |
| onlyTranslated | boolean | 否 | 如果为真,则对象只翻译,不缩放或旋转. |


**返回值:** boolean - 如果游戏对象应该被四舍五入, 否则是虚假的 。


> 源码：[src/gameobjects/GameObject.js#L714](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L714)  
引入版本：4.0.0


---

## 常量 {#constants}

## 公开成员 {#public-members-1}

### RENDER_MASK {#RENDER_MASK}

#### RENDER_MASK: number {#render_mask-number}


**说明:**

`GameObject.renderFlags` 的比特掩码用于确定游戏对象是否渲染.


> 源码：[src/gameobjects/GameObject.js#L1066](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/GameObject.js#L1066)  



---

---
