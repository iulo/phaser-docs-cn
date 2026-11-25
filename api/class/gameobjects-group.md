# Group {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/gameobjects-group)

A组是您创建,操纵,或回收类似游戏对象的一种方法.

组通常用于执行对象池,在游戏前方创建一组固定的游戏对象,然后通过将它们的`active`和`visible`状态进行循环,避免重复构造和垃圾收集的间接性。这种模式对经常产卵的对象,如子弹、颗粒或敌人特别有用。

团体成员不是专属的,游戏对象可以属于多个团体,一个团体,也可以是无团体.

团体本身是无法显示的,不能被定位,旋转,缩放,或隐藏.

**构造函数**

`new Group(scene, [children], [config])`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 剧组所属的场景. |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> \| [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) | [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 要添加到此组的游戏对象; 或 `config` 参数 。 |
| config | [Phaser.Types.GameObjects.Group.GroupConfig](/api/typedef/types-gameobjects-group#groupconfig) \| [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 是 | 此组的设置。 如果设置了 `key`, 则使用这些设置调用 Phaser.GameObjects.Group# createMultiple 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/gameobjects/group/Group.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L19)  
引入版本：3.0.0

## 公开成员 {#public-members}

### active {#active}

#### active: boolean {#active-boolean}


**说明:**

此组是否运行其 [Phaser.GameObjects.Group#preUpdate](/api/class/gameobjects-group#preUpdate) 方法( 它可能更新任何成员) 。


> 源码：[src/gameobjects/group/Group.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L153)  
引入版本：3.0.0


---

### children {#children}

#### children: Set.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> {#children-setphasergameobjectsgameobject}


**说明:**

集团成员.


> 源码：[src/gameobjects/group/Group.js#L99](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L99)  
引入版本：3.0.0


---

### classType {#classType}

#### classType: function {#classtype-function}


**说明:**

创建新团体成员的班级从.

构造器参数必须匹配 `(scene, x, y, texture, frame)` 。


> 源码：[src/gameobjects/group/Group.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L129)  
引入版本：3.0.0


---

### createCallback {#createCallback}

#### createCallback: [Phaser.Types.GameObjects.Group.GroupCallback](/api/typedef/types-gameobjects-group#groupcallback) {#createcallback-phasertypesgameobjectsgroupgroupcallback}


**说明:**

添加或创建组成员时要调用的一个函数 。


> 源码：[src/gameobjects/group/Group.js#L204](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L204)  
引入版本：3.0.0


---

### createMultipleCallback {#createMultipleCallback}

#### createMultipleCallback: [Phaser.Types.GameObjects.Group.GroupMultipleCreateCallback](/api/typedef/types-gameobjects-group#groupmultiplecreatecallback) {#createmultiplecallback-phasertypesgameobjectsgroupgroupmultiplecreatecallback}


**说明:**

当同时创建多个组成员时要调用的一个函数 。


> 源码：[src/gameobjects/group/Group.js#L222](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L222)  
引入版本：3.0.0


---

### defaultFrame {#defaultFrame}

#### defaultFrame: string, number {#defaultframe-string-number}


**说明:**

创建新组成员时使用的默认纹理帧 。


> 源码：[src/gameobjects/group/Group.js#L184](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L184)  
引入版本：3.0.0


---

### defaultKey {#defaultKey}

#### defaultKey: string {#defaultkey-string}


**说明:**

创建新组成员时要使用的默认纹理键 。

用于[Phaser.GameObjects.Group#create](/api/class/gameobjects-group#create),但用于[Phaser.GameObjects.Group#createMultiple](/api/class/gameobjects-group#createMultiple).


> 源码：[src/gameobjects/group/Group.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L172)  
引入版本：3.0.0


---

### isParent {#isParent}

#### isParent: boolean {#isparent-boolean}


**说明:**

标记为组合此对象。


> 源码：[src/gameobjects/group/Group.js#L108](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L108)  
引入版本：3.0.0


---

### maxSize {#maxSize}

#### maxSize: number {#maxsize-number}


**说明:**

此组的最大大小, 如果用作池。 - 1 并不限制 。


> 源码：[src/gameobjects/group/Group.js#L162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L162)  
引入版本：3.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

此组的名称。 默认情况下是空的, 并且从未被 Phaser 所覆盖, 留给开发者使用 。


> 源码：[src/gameobjects/group/Group.js#L142](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L142)  
引入版本：3.18.0


---

### removeCallback {#removeCallback}

#### removeCallback: [Phaser.Types.GameObjects.Group.GroupCallback](/api/typedef/types-gameobjects-group#groupcallback) {#removecallback-phasertypesgameobjectsgroupgroupcallback}


**说明:**

删除组成员时要调用的函数 。


> 源码：[src/gameobjects/group/Group.js#L213](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L213)  
引入版本：3.0.0


---

### runChildUpdate {#runChildUpdate}

#### runChildUpdate: boolean {#runchildupdate-boolean}


**说明:**

是否调用任何成员的更新方法 。


> 源码：[src/gameobjects/group/Group.js#L193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L193)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

这个剧组属于这个场景


> 源码：[src/gameobjects/group/Group.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L90)  
引入版本：3.0.0


---

### type {#type}

#### type: string {#type-string}


**说明:**

此游戏对象的文字表达。 内部由 Phaser 使用, 但可供您自定义的类使用 。


> 源码：[src/gameobjects/group/Group.js#L118](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L118)  
引入版本：3.21.0


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

#### \<instance> add(child, [addToScene]) {#instance-addchild-addtoscene}


**说明:**

将游戏对象添加到此组。

电话 [Phaser.GameObjects.Group#createCallback](/api/class/gameobjects-group#createCallback).

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 要添加的游戏对象 。 |
| addToScene | boolean | 是 | false | 还将游戏对象添加到场景中. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L588](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L588)  
引入版本：3.0.0


---

### addedToScene {#addedToScene}

#### \<instance> addedToScene() {#instance-addedtoscene}


**说明:**

当此组被添加到场景中时调用。 将本组与场景更新列表注册, 这样其`preUpdate` 方法就被称为每个游戏步骤 。


> 源码：[src/gameobjects/group/Group.js#L267](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L267)  
引入版本：3.0.0


---

### addMultiple {#addMultiple}

#### \<instance> addMultiple(children, [addToScene]) {#instance-addmultiplechildren-addtoscene}


**说明:**

将多个游戏对象添加到此组。

电话 [Phaser.GameObjects.Group#createCallback](/api/class/gameobjects-group#createCallback).

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| children | Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> | 否 |  | 要添加的游戏对象 。 |
| addToScene | boolean | 是 | false | 同时在现场添加游戏对象. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 这个团体。


> 源码：[src/gameobjects/group/Group.js#L633](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L633)  
引入版本：3.0.0


---

### angle {#angle}

#### \<instance> angle(value, [step]) {#instance-anglevalue-step}


**说明:**

将给定的值添加到每个组成员的角度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 以度数表示的加角值。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1403](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1403)  
引入版本：3.21.0


---

### clear {#clear}

#### \<instance> clear([removeFromScene], [destroyChild]) {#instance-clearremovefromscene-destroychild}


**说明:**

移除此组的所有成员,并选择将其从场景中移除和/或摧毁.

不叫[Phaser.GameObjects.Group#removeCallback](/api/class/gameobjects-group#removeCallback)。 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| removeFromScene | boolean | 是 | false | 可选地将每个组成员从场景中移除. |
| destroyChild | boolean | 是 | false | 逐一向被除名的集团成员发出毁灭信号 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 这个团体。


> 源码：[src/gameobjects/group/Group.js#L712](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L712)  
引入版本：3.0.0


---

### contains {#contains}

#### \<instance> contains(child) {#instance-containschild}


**说明:**

测试游戏对象是否是此组的成员 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 一个游戏对象。 |


**返回值:** boolean - 如果游戏对象是这个组的成员, 则为真 。


> 源码：[src/gameobjects/group/Group.js#L752](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L752)  
引入版本：3.0.0


---

### countActive {#countActive}

#### \<instance> countActive([value]) {#instance-countactivevalue}


**说明:**

计算活动(或非活动)组成员的数目。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 是 | true | 计数活动( true)或不活动(假)组成员. |


**返回值:** number - 与 `active` 参数匹配的活跃状态的组成员数 。


> 源码：[src/gameobjects/group/Group.js#L1133](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1133)  
引入版本：3.0.0


---

### create {#create}

#### \<instance> create([x], [y], [key], [frame], [visible], [active]) {#instance-createx-y-key-frame-visible-active}


**说明:**

创建新的游戏对象并添加到此组, 除非该组为 [is](/api/class/gameobjects-group#isFull) 。

电话 [Phaser.GameObjects.Group#createCallback](/api/class/gameobjects-group#createCallback).

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 新的游戏对象在世界的横向位置. |
| y | number | 是 | 0 | 新的游戏对象在世界的垂直位置. |
| key | string | 是 | "defaultKey" | 新游戏对象的纹理键 。 |
| frame | string \| number | 是 | "defaultFrame" | 新游戏对象的纹理帧. |
| visible | boolean | 是 | true | QQlink Phaser.GameObjects.Components.Visible#可见] 新游戏对象状态. |
| active | boolean | 是 | true | QQlink Phaser.GameObjects.GameObject#Active}新游戏对象状态. |


**返回值:** any - 新的游戏对象(通常是Sprite等).


> 源码：[src/gameobjects/group/Group.js#L291](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L291)  
引入版本：3.0.0


---

### createFromConfig {#createFromConfig}

#### \<instance> createFromConfig(options) {#instance-createfromconfigoptions}


**说明:**

帮[Phaser.GameObjects.Group#createMultiple](/api/class/gameobjects-group#createMultiple)的助手.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| options | [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) | 否 | 创建设置 。 |


**返回值:** Array.\<any> - 新创建的游戏对象.


> 源码：[src/gameobjects/group/Group.js#L377](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L377)  
引入版本：3.0.0


---

### createMultiple {#createMultiple}

#### \<instance> createMultiple(config) {#instance-createmultipleconfig}


**说明:**

创建多个游戏对象并添加到此组中。

如果组成为[Phaser.GameObjects.Group#isFull](/api/class/gameobjects-group#isFull),则不再创建游戏对象.

呼叫[Phaser.GameObjects.Group#createMultipleCallback](/api/class/gameobjects-group#createMultipleCallback)和[Phaser.GameObjects.Group#createCallback](/api/class/gameobjects-group#createCallback)。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| config | [Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig) \| Array.\<[Phaser.Types.GameObjects.Group.GroupCreateConfig](/api/typedef/types-gameobjects-group#groupcreateconfig)> | 否 | 创建设置。 这可能是一个单一的配置对象或此类对象的数组, 将依次应用 。 |


**返回值:** Array.\<any> - 新创建的游戏对象.


> 源码：[src/gameobjects/group/Group.js#L336](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L336)  
引入版本：3.0.0


---

### destroy {#destroy}

#### \<instance> destroy([destroyChildren], [removeFromScene]) {#instance-destroydestroychildren-removefromscene}


**说明:**

利用这个群体 所有儿童,并把它从场景中移除。

不叫[Phaser.GameObjects.Group#removeCallback](/api/class/gameobjects-group#removeCallback)。 。

此组的子将_ not_通过调用此方法从场景中移除, 除非您指定 `removeFromScene` 参数 。

此组的子也会通过调用此方法被销毁_ not_, 除非您指定 `destroyChildren` 参数 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| destroyChildren | boolean | 是 | false | 也来点小菜一碟 Phaser.GameObjects.GameObject每一个集团成员。 |
| removeFromScene | boolean | 是 | false | 可选地将每个组成员从场景中移除. |


**重写:** Phaser.Events.EventEmitter#销毁


> 源码：[src/gameobjects/group/Group.js#L1725](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1725)  
引入版本：3.0.0


---

### get {#get}

#### \<instance> get([x], [y], [key], [frame], [visible]) {#instance-getx-y-key-frame-visible}


**说明:**

扫描第一个拥有[Phaser.GameObjects.GameObject#active](/api/class/gameobjects-gameobject#active)状态设定为`false`的成员的组,指定`x`和`y`,并返回该成员.

如果找不到不活跃的成员, 且组不满, 那么它将会使用 `x`, `y`, `key`, `frame`,和 `visible`。新的游戏对象将设定其活动状态为 `true`除非设立新成员, `key`, `frame`,和 `visible` 被忽略了,我们没有被忽略。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 |  | 游戏对象在世界的横向位置. |
| y | number | 是 |  | 游戏对象在世界的垂直位置. |
| key | string | 是 | "defaultKey" | 指定给新游戏对象的纹理键( 如果创建了) 。 |
| frame | string \| number | 是 | "defaultFrame" | 指定给新游戏对象的纹理帧(如果创建了). |
| visible | boolean | 是 | true | QQlink Phaser.GameObjects.Components.Visible#可见的] 新游戏对象状态(如果创建了). |


**返回值:** any - 第一个不活跃的组成员,或新创建的成员,或无效.


> 源码：[src/gameobjects/group/Group.js#L1022](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1022)  
引入版本：3.0.0


---

### getChildren {#getChildren}

#### \<instance> getChildren() {#instance-getchildren}


**说明:**

全体众生.


**返回值:** Array.\<[Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject)> - 集团成员.


> 源码：[src/gameobjects/group/Group.js#L767](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L767)  
引入版本：3.0.0


---

### getFirst {#getFirst}

#### \<instance> getFirst([state], [createIfNull], [x], [y], [key], [frame], [visible]) {#instance-getfirststate-createifnull-x-y-key-frame-visible}


**说明:**

从上到下扫描组,以查找第一个具有[Phaser.GameObjects.GameObject#active](/api/class/gameobjects-gameobject#active)状态的符合参数的组,指定`x`和`y`,并返回该组成员.

如果没有找到匹配的成员, `createIfNull` 真实, 且组不全, 然后它将使用 `x`, `y`, `key`, `frame`,和 `visible`除非设立新成员, `key`, `frame`,和 `visible` 被忽略了,我们没有被忽略。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | boolean | 是 | false | QQlink Phaser.GameObjects.GameObject#Action} 值匹配 。 |
| createIfNull | boolean | 是 | false | 如果找不到匹配的成员, 则使用以下参数创建新的 Game Object 。 |
| x | number | 是 |  | 游戏对象在世界的横向位置. |
| y | number | 是 |  | 游戏对象在世界的垂直位置. |
| key | string | 是 | "defaultKey" | 指定给新游戏对象的纹理键( 如果创建了) 。 |
| frame | string \| number | 是 | "defaultFrame" | 指定给新游戏对象的纹理帧(如果创建了). |
| visible | boolean | 是 | true | QQlink Phaser.GameObjects.Components.Visible#可见的] 新游戏对象状态(如果创建了). |


**返回值:** any - 第一个匹配组成员,或新创建的成员,或无效.


> 源码：[src/gameobjects/group/Group.js#L817](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L817)  
引入版本：3.0.0


---

### getFirstAlive {#getFirstAlive}

#### \<instance> getFirstAlive([createIfNull], [x], [y], [key], [frame], [visible]) {#instance-getfirstalivecreateifnull-x-y-key-frame-visible}


**说明:**

扫描第一个拥有[Phaser.GameObjects.GameObject#active](/api/class/gameobjects-gameobject#active)状态设定为`true`的成员的组,指定`x`和`y`,并返回该成员.

如果找不到活跃成员, `createIfNull` 谓 `true` 组员不满 然后将用 `x`, `y`, `key`, `frame`,和 `visible`除非设立新成员, `key`, `frame`,和 `visible` 被忽略了,我们没有被忽略。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| createIfNull | boolean | 是 | false | 如果找不到匹配的成员, 则使用以下参数创建新的 Game Object 。 |
| x | number | 是 |  | 游戏对象在世界的横向位置. |
| y | number | 是 |  | 游戏对象在世界的垂直位置. |
| key | string | 是 | "defaultKey" | 指定给新游戏对象的纹理键( 如果创建了) 。 |
| frame | string \| number | 是 | "defaultFrame" | 指定给新游戏对象的纹理帧(如果创建了). |
| visible | boolean | 是 | true | QQlink Phaser.GameObjects.Components.Visible#可见的] 新游戏对象状态(如果创建了). |


**返回值:** any - 第一个活跃的团体成员,或新创建的成员,或无效.


> 源码：[src/gameobjects/group/Group.js#L1046](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1046)  
引入版本：3.0.0


---

### getFirstDead {#getFirstDead}

#### \<instance> getFirstDead([createIfNull], [x], [y], [key], [frame], [visible]) {#instance-getfirstdeadcreateifnull-x-y-key-frame-visible}


**说明:**

扫描第一个拥有[Phaser.GameObjects.GameObject#active](/api/class/gameobjects-gameobject#active)状态设定为`false`的成员的组,指定`x`和`y`,并返回该成员.

如果没有非活动成员, `createIfNull` 谓 `true` 组员不满 然后将用 `x`, `y`, `key`, `frame`,和 `visible`。新的游戏对象将设置一个活动状态,以 `true`除非设立新成员, `key`, `frame`,和 `visible` 被忽略了,我们没有被忽略。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| createIfNull | boolean | 是 | false | 如果找不到匹配的成员, 则使用以下参数创建新的 Game Object 。 |
| x | number | 是 |  | 游戏对象在世界的横向位置. |
| y | number | 是 |  | 游戏对象在世界的垂直位置. |
| key | string | 是 | "defaultKey" | 指定给新游戏对象的纹理键( 如果创建了) 。 |
| frame | string \| number | 是 | "defaultFrame" | 指定给新游戏对象的纹理帧(如果创建了). |
| visible | boolean | 是 | true | QQlink Phaser.GameObjects.Components.Visible#可见的] 新游戏对象状态(如果创建了). |


**返回值:** any - 第一个不活跃的组成员,或新创建的成员,或无效.


> 源码：[src/gameobjects/group/Group.js#L1070](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1070)  
引入版本：3.0.0


---

### getFirstNth {#getFirstNth}

#### \<instance> getFirstNth(nth, [state], [createIfNull], [x], [y], [key], [frame], [visible]) {#instance-getfirstnthnth-state-createifnull-x-y-key-frame-visible}


**说明:**

从上到下扫描组,以查找与参数匹配的[Phaser.GameObjects.GameObject#active](/api/class/gameobjects-gameobject#active)状态的第n个成员,指定`x`和`y`,并返回该成员。

如果没有找到匹配的成员, `createIfNull` 真实, 且组不全, 然后它将使用 `x`, `y`, `key`, `frame`,和 `visible`除非设立新成员, `key`, `frame`,和 `visible` 被忽略了,我们没有被忽略。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| nth | number | 否 |  | Nth匹配组成员要搜索 。 |
| state | boolean | 是 | false | QQlink Phaser.GameObjects.GameObject#Action} 值匹配 。 |
| createIfNull | boolean | 是 | false | 如果找不到匹配的成员, 则使用以下参数创建新的 Game Object 。 |
| x | number | 是 |  | 游戏对象在世界的横向位置. |
| y | number | 是 |  | 游戏对象在世界的垂直位置. |
| key | string | 是 | "defaultKey" | 指定给新游戏对象的纹理键( 如果创建了) 。 |
| frame | string \| number | 是 | "defaultFrame" | 指定给新游戏对象的纹理帧(如果创建了). |
| visible | boolean | 是 | true | QQlink Phaser.GameObjects.Components.Visible#可见的] 新游戏对象状态(如果创建了). |


**返回值:** any - nth匹配组成员,或新创建的成员,或无效.


> 源码：[src/gameobjects/group/Group.js#L842](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L842)  
引入版本：3.6.0


---

### getLast {#getLast}

#### \<instance> getLast([state], [createIfNull], [x], [y], [key], [frame], [visible]) {#instance-getlaststate-createifnull-x-y-key-frame-visible}


**说明:**

扫描最后一个具有匹配参数的 [Phaser.GameObjects.GameObject#active](/api/class/gameobjects-gameobject#active) 状态的成员的组,指定 `x` 和 `y`,并返回该成员。

如果没有找到匹配的成员, `createIfNull` 真实, 且组不全, 然后它将使用 `x`, `y`, `key`, `frame`,和 `visible`除非设立新成员, `key`, `frame`,和 `visible` 被忽略了,我们没有被忽略。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| state | boolean | 是 | false | QQlink Phaser.GameObjects.GameObject#Action} 值匹配 。 |
| createIfNull | boolean | 是 | false | 如果找不到匹配的成员, 则使用以下参数创建新的 Game Object 。 |
| x | number | 是 |  | 游戏对象在世界的横向位置. |
| y | number | 是 |  | 游戏对象在世界的垂直位置. |
| key | string | 是 | "defaultKey" | 指定给新游戏对象的纹理键( 如果创建了) 。 |
| frame | string \| number | 是 | "defaultFrame" | 指定给新游戏对象的纹理帧(如果创建了). |
| visible | boolean | 是 | true | QQlink Phaser.GameObjects.Components.Visible#可见的] 新游戏对象状态(如果创建了). |


**返回值:** any - 最后一个匹配组成员,或新创建的成员,或无效.


> 源码：[src/gameobjects/group/Group.js#L868](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L868)  
引入版本：3.6.0


---

### getLastNth {#getLastNth}

#### \<instance> getLastNth(nth, [state], [createIfNull], [x], [y], [key], [frame], [visible]) {#instance-getlastnthnth-state-createifnull-x-y-key-frame-visible}


**说明:**

扫描最后一个 N 成员组 [Phaser.GameObjects.GameObject#active](/api/class/gameobjects-gameobject#active) 状态与参数匹配,指定 `x` 财务报告和已审计财务报表 `y`,然后返回成员。

如果没有找到匹配的成员, `createIfNull` 真实, 且组不全, 然后它将使用 `x`, `y`, `key`, `frame`,和 `visible`除非设立新成员, `key`, `frame`,和 `visible` 被忽略了,我们没有被忽略。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| nth | number | 否 |  | Nth匹配组成员要搜索 。 |
| state | boolean | 是 | false | QQlink Phaser.GameObjects.GameObject#Action} 值匹配 。 |
| createIfNull | boolean | 是 | false | 如果找不到匹配的成员, 则使用以下参数创建新的 Game Object 。 |
| x | number | 是 |  | 游戏对象在世界的横向位置. |
| y | number | 是 |  | 游戏对象在世界的垂直位置. |
| key | string | 是 | "defaultKey" | 指定给新游戏对象的纹理键( 如果创建了) 。 |
| frame | string \| number | 是 | "defaultFrame" | 指定给新游戏对象的纹理帧(如果创建了). |
| visible | boolean | 是 | true | QQlink Phaser.GameObjects.Components.Visible#可见的] 新游戏对象状态(如果创建了). |


**返回值:** any - nth匹配组成员(从尾部搜索),或新创建的成员,或无效.


> 源码：[src/gameobjects/group/Group.js#L893](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L893)  
引入版本：3.6.0


---

### getLength {#getLength}

#### \<instance> getLength() {#instance-getlength}


**说明:**

组员人数.


**返回值:** number - 本组成员总数.


> 源码：[src/gameobjects/group/Group.js#L780](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L780)  
引入版本：3.0.0


---

### getMatching {#getMatching}

#### \<instance> getMatching([property], [value], [startIndex], [endIndex]) {#instance-getmatchingproperty-value-startindex-endindex}


**说明:**

返回这个小组中符合基于`property`和`value`参数的指定标准的所有儿童。

例如:`getMatching('visible', true)`只将拥有`visible`属性的孩子们送回.

可选的, 您可以指定一个起始和结束索引。 例如, 如果 Group 具有100 个元素, 您将 `startIndex` 设置为 0, `endIndex` 设置为 50, 它只会从前50 个返回匹配 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| property | string | 是 | 在每个阵列元素上测试的属性 。 |
| value | * | 是 | 对照属性测试值。 必须进行严格的( `===`) 比较检查 。 |
| startIndex | number | 是 | 搜索对象的可选起始索引 。 |
| endIndex | number | 是 | 要搜索的可选端索引 。 |


**返回值:** Array.\<any> - 一组匹配的 Group 成员。 如果无匹配的话, 阵列将空 。


> 源码：[src/gameobjects/group/Group.js#L793](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L793)  
引入版本：3.50.0


---

### getTotalFree {#getTotalFree}

#### \<instance> getTotalFree() {#instance-gettotalfree}


**说明:**

[Phaser.GameObjects.Group#maxSize](/api/class/gameobjects-group#maxSize)与活跃的团体成员数量之差.

这是在达到尺寸限制之前可以创建或重新启用的组成员数量.


**返回值:** number - maxSize减去活动组成员数;或大数(如果maxSize是−1).


> 源码：[src/gameobjects/group/Group.js#L1173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1173)  
引入版本：3.0.0


---

### getTotalUsed {#getTotalUsed}

#### \<instance> getTotalUsed() {#instance-gettotalused}


**说明:**

计算使用中的(活动)组成员数。


**返回值:** number - 活动状态为真实状态的团体成员数量.


> 源码：[src/gameobjects/group/Group.js#L1160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1160)  
引入版本：3.0.0


---

### incX {#incX}

#### \<instance> incX(value, [step]) {#instance-incxvalue-step}


**说明:**

将给定的值添加到每个组成员的x。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 将增加的`x`属性金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1325](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1325)  
引入版本：3.21.0


---

### incXY {#incXY}

#### \<instance> incXY(x, [y], [stepX], [stepY]) {#instance-incxyx-y-stepx-stepy}


**说明:**

将给定的值添加到每个组成员的x,y。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 将增加的`x`属性金额。 |
| y | number | 是 | "x" | `y` 属性的加法。如果 `undefined` 或 `null` ,则使用 `x` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`x`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`y`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1361](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1361)  
引入版本：3.21.0


---

### incY {#incY}

#### \<instance> incY(value, [step]) {#instance-incyvalue-step}


**说明:**

将给定的值添加到每个组成员的y。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 将增加的`y`属性金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1343](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1343)  
引入版本：3.21.0


---

### isFull {#isFull}

#### \<instance> isFull() {#instance-isfull}


**说明:**

这个组的大小是否达到[maximum](/api/class/gameobjects-group#maxSize).


**返回值:** boolean - 如果成员数等于[Phaser.GameObjects.Group#maxSize](/api/class/gameobjects-group#maxSize),则属实.


> 源码：[src/gameobjects/group/Group.js#L1113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1113)  
引入版本：3.0.0


---

### kill {#kill}

#### \<instance> kill(gameObject) {#instance-killgameobject}


**说明:**

解除这个团体的成员资格.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 某甲此组. |


> 源码：[src/gameobjects/group/Group.js#L1658](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1658)  
引入版本：3.0.0


---

### killAndHide {#killAndHide}

#### \<instance> killAndHide(gameObject) {#instance-killandhidegameobject}


**说明:**

解除并隐藏这个团体的一名成员.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 某甲此组. |


> 源码：[src/gameobjects/group/Group.js#L1674](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1674)  
引入版本：3.0.0


---

### playAnimation {#playAnimation}

#### \<instance> playAnimation(key, [startFrame]) {#instance-playanimationkey-startframe}


**说明:**

[Plays](/api/class/animations-animationstate#play)是本组所有成员的动画.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 动画要播放的基于字符串的键. |
| startFrame | string | 是 | 0 | 选择从此帧索引开始播放动画. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1095](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1095)  
引入版本：3.0.0


---

### preUpdate {#preUpdate}

#### \<instance> preUpdate(time, delta) {#instance-preupdatetime-delta}


**说明:**

如果启用 [Phaser.GameObjects.Group#runChildUpdate](/api/class/gameobjects-group#runChildUpdate) , 则更新任何组成员 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| time | number | 否 | 现时时标. |
| delta | number | 否 | 三角洲时间已经过去 自上个框架。 |


> 源码：[src/gameobjects/group/Group.js#L563](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L563)  
引入版本：3.0.0


---

### propertyValueInc {#propertyValueInc}

#### \<instance> propertyValueInc(key, value, [step], [index], [direction]) {#instance-propertyvalueinckey-value-step-index-direction}


**说明:**

将给定值添加到每个组成员的`key`中定义的属性。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 需要更新的属性 。 |
| value | number | 否 |  | 增属性之数. |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1248)  
引入版本：3.21.0


---

### propertyValueSet {#propertyValueSet}

#### \<instance> propertyValueSet(key, value, [step], [index], [direction]) {#instance-propertyvaluesetkey-value-step-index-direction}


**说明:**

将每个组成员的 `key` 定义属性设定为给定值。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string | 否 |  | 需要更新的属性 。 |
| value | number | 否 |  | 设定属性的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1227](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1227)  
引入版本：3.21.0


---

### remove {#remove}

#### \<instance> remove(child, [removeFromScene], [destroyChild]) {#instance-removechild-removefromscene-destroychild}


**说明:**

删除此组的成员,并选择将其从场景中移除和/或将其销毁.

电话 [Phaser.GameObjects.Group#removeCallback](/api/class/gameobjects-group#removeCallback).

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| child | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 |  | 要删除的游戏对象 。 |
| removeFromScene | boolean | 是 | false | 可选地将组成员从所属场馆中移除. |
| destroyChild | boolean | 是 | false | 选择性地呼叫被移除的Group成员进行销毁. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L661](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L661)  
引入版本：3.0.0


---

### removedFromScene {#removedFromScene}

#### \<instance> removedFromScene() {#instance-removedfromscene}


**说明:**

取消此组在 Scene 更新列表中的注册, 使其 `preUpdate` 方法不再称为每个游戏步骤 。


> 源码：[src/gameobjects/group/Group.js#L279](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L279)  
引入版本：3.0.0


---

### rotate {#rotate}

#### \<instance> rotate(value, [step]) {#instance-rotatevalue-step}


**说明:**

设定每个组成员的旋转。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 将旋转设为弧度的金额。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1421](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1421)  
引入版本：3.21.0


---

### rotateAround {#rotateAround}

#### \<instance> rotateAround(point, angle) {#instance-rotatearoundpoint-angle}


**说明:**

按给定角度围绕给定点旋转每个组成员。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 任何具有公共`x`和`y`属性的天体. |
| angle | number | 否 | 旋转的角度,用弧度表示。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1439](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1439)  
引入版本：3.21.0


---

### rotateAroundDistance {#rotateAroundDistance}

#### \<instance> rotateAroundDistance(point, angle, distance) {#instance-rotatearounddistancepoint-angle-distance}


**说明:**

将每个组成员围绕给定点按给定角度和距离旋转。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 任何具有公共`x`和`y`属性的天体. |
| angle | number | 否 | 旋转的角度,用弧度表示。 |
| distance | number | 否 | 以像素表示的旋转点距离. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1457](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1457)  
引入版本：3.21.0


---

### scaleX {#scaleX}

#### \<instance> scaleX(value, [step]) {#instance-scalexvalue-step}


**说明:**

设定每个组成员的 scaleX 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 设定属性的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1534](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1534)  
引入版本：3.21.0


---

### scaleXY {#scaleXY}

#### \<instance> scaleXY(scaleX, [scaleY], [stepX], [stepY]) {#instance-scalexyscalex-scaley-stepx-stepy}


**说明:**

设定每个组成员的scaleX,scaleY.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| scaleX | number | 否 |  | 设定 `scaleX` 属性的金额 。 |
| scaleY | number | 是 |  | 设置 `scaleY` 属性的金额。 如果 `undefined` 或 `null` , 它使用 `scaleX` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`scaleX`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`scaleY`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1570](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1570)  
引入版本：3.21.0


---

### scaleY {#scaleY}

#### \<instance> scaleY(value, [step]) {#instance-scaleyvalue-step}


**说明:**

设定每个组成员的 scaleY 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 设定属性的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1552](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1552)  
引入版本：3.21.0


---

### setActive {#setActive}

#### \<instance> setActive(value) {#instance-setactivevalue}


**说明:**

设置此组的 `active` 属性。 当活动时, 本组将运行其 `preUpdate` 方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | boolean | 否 | 如果这个集团被设定为活跃的,如果不是虚假的,那么它就是真的。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1191](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1191)  
引入版本：3.24.0


---

### setAlpha {#setAlpha}

#### \<instance> setAlpha(value, [step]) {#instance-setalphavalue-step}


**说明:**

设置每个组成员的α。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 设定α到的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1476](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1476)  
引入版本：3.21.0


---

### setBlendMode {#setBlendMode}

#### \<instance> setBlendMode(value) {#instance-setblendmodevalue}


**说明:**

设定每个组成员的 blendMode 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 要设置的混合模式值。 有效值请参见 `Phaser.BlendModes` 。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1608](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1608)  
引入版本：3.21.0


---

### setDepth {#setDepth}

#### \<instance> setDepth(value, [step]) {#instance-setdepthvalue-step}


**说明:**

设定每个组成员的深度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 设定属性的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1590](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1590)  
引入版本：3.0.0


---

### setHitArea {#setHitArea}

#### \<instance> setHitArea(hitArea, hitAreaCallback) {#instance-sethitareahitarea-hitareacallback}


**说明:**

将所有组成员传递到输入管理器,以便他们能够输入相同的区域并调回调用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| hitArea | * | 否 | 输入配置对象,或者定义游戏对象的命中区域的几何形状。如果不指定矩形,则会使用。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 否 | 当游戏对象被交互时, 将引用回调。 如果您提供了形状, 您也必须提供回调 。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1625](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1625)  
引入版本：3.21.0


---

### setName {#setName}

#### \<instance> setName(value) {#instance-setnamevalue}


**说明:**

设定 `name` 。该组的属性。 `name` 属性不为 Phaser 并呈上供你们使用。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | string | 否 | 给这个小组取名。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1209](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1209)  
引入版本：3.24.0


---

### setOrigin {#setOrigin}

#### \<instance> setOrigin(originX, [originY], [stepX], [stepY]) {#instance-setoriginoriginx-originy-stepx-stepy}


**说明:**

设定每个组成员的originX,originY.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| originX | number | 否 |  | 设定 `originX` 属性的金额 。 |
| originY | number | 是 |  | 设置 `originY` 属性的金额。 如果 `undefined` 或 `null` , 它使用 `originX` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`originX`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`originY`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1514](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1514)  
引入版本：3.21.0


---

### setTint {#setTint}

#### \<instance> setTint(topLeft, [topRight], [bottomLeft], [bottomRight]) {#instance-settinttopleft-topright-bottomleft-bottomright}


**说明:**

设置每个组成员的锡。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| topLeft | number | 否 | 正在应用到项目左上角的锡。 如果给其他参数没有值, 此锡将应用到整个项目 。 |
| topRight | number | 是 | 用于项目右上角的锡。 |
| bottomLeft | number | 是 | 用于项目左下角的锡。 |
| bottomRight | number | 是 | 用于项目右下角的锡。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1494](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1494)  
引入版本：3.21.0


---

### setVisible {#setVisible}

#### \<instance> setVisible(value, [index], [direction]) {#instance-setvisiblevalue-index-direction}


**说明:**

设定每个组成员的可见度。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | boolean | 否 |  | 设置属性的值 。 |
| index | number | 是 | 0 | 选择的偏移, 开始从项目数组中查找 。 |
| direction | number | 是 | 1 | 向上通过阵列的方向 。 1 从头到尾, - 1 从头到尾。 |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1691](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1691)  
引入版本：3.21.0


---

### setX {#setX}

#### \<instance> setX(value, [step]) {#instance-setxvalue-step}


**说明:**

设置每个组成员的x。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 设定属性的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1269](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1269)  
引入版本：3.21.0


---

### setXY {#setXY}

#### \<instance> setXY(x, [y], [stepX], [stepY]) {#instance-setxyx-y-stepx-stepy}


**说明:**

设置每个组成员的 x, y 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | 设定 `x` 属性的金额 。 |
| y | number | 是 | "x" | 设置 `y` 属性的金额。 如果 `undefined` 或 `null` , 它使用 `x` 值 。 |
| stepX | number | 是 | 0 | 这一点被加到`x`的金额中,乘以迭代计数器. |
| stepY | number | 是 | 0 | 这一点被加到`y`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1305](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1305)  
引入版本：3.21.0


---

### setY {#setY}

#### \<instance> setY(value, [step]) {#instance-setyvalue-step}


**说明:**

设定每个组成员的y。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 设定属性的金额 。 |
| step | number | 是 | 0 | 这一点被加到`value`的金额中,乘以迭代计数器. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1287](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1287)  
引入版本：3.21.0


---

### shiftPosition {#shiftPosition}

#### \<instance> shiftPosition(x, y, [direction]) {#instance-shiftpositionx-y-direction}


**说明:**

通过组成员将每个元素的位置改为数组中其面前的元素的位置(如果方向=1)

第一个组成员位置设定为x/y.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 否 |  | x 坐标将第一个项目放在数组中 。 |
| y | number | 否 |  | y 坐标将第一个项目放在数组中。 |
| direction | number | 是 | 0 | 迭代方向. 0=先到最后,1=最后到最后. |


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1381](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1381)  
引入版本：3.21.0


---

### shuffle {#shuffle}

#### \<instance> shuffle() {#instance-shuffle}


**说明:**

将组员们排好队


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1643](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1643)  
引入版本：3.21.0


---

### toggleVisible {#toggleVisible}

#### \<instance> toggleVisible() {#instance-togglevisible}


**说明:**

切换( flips) 此组中每个成员的可见状态 。


**返回值:** [Phaser.GameObjects.Group](/api/class/gameobjects-group) - 此组对象 。


> 源码：[src/gameobjects/group/Group.js#L1710](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/Group.js#L1710)  
引入版本：3.0.0


---

---
