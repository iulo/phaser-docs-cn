# Phaser.DOM {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/dom)

Scope: 
static
> 源码：[src/dom/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/index.js#L7)  


## 静态函数 {#static-functions}

- [RequestAnimationFrame](/api/class/dom-requestanimationframe)
## 静态函数 {#static-functions-1}

### AddToDOM {#AddToDOM}

#### \<static> AddToDOM(element, [parent]) {#static-addtodomelement-parent}


**说明:**

将给定元素添加到 DOM 中。 如果提供了父元素, 元素会作为父元素的子元素添加, 要么通过将字符串ID传递到 `getElementById` 或直接使用 HTMLElement 来解决。 如果未给出父元素, 而元素已经拥有了 `parentElement` , 或者 `parent` 明确为 `null` , 则元素会立即返回, 不修改 。 如果无法解决有效的目标父元素, 元素会被附加到 `document.body` 中作为反向 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| element | HTMLElement | 否 | 要添加到 DOM 中的元素。 通常是一个 Canvas 对象 。 |
| parent | string \| HTMLElement | 是 | 添加元素的父进程。 可以是传递到 `getElementById` 或实际 DOM 对象的字符串 。 |


**返回值:** HTMLElement - 传递到此函数的元素 。


> 源码：[src/dom/AddToDOM.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/AddToDOM.js#L7)  
引入版本：3.0.0


---

### CreateDOMContainer {#CreateDOMContainer}

#### \<static> CreateDOMContainer(game) {#static-createdomcontainergame}


**说明:**

创建 DOM 容器的 div 元素,用于 DOM 游戏对象。

容器是绝对定位的潜水器,可以覆盖游戏画布,与其尺寸匹配,并添加到游戏的母元素中,它有按照游戏配置设置的指针事件,并作为任何添加到场景中的DOM Element Game Objects的父事件.

如果游戏配置同时具有`parent`元素和`domCreateContainer`设定为`true`,则此功能在游戏启动时自动称为.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | Phaser游戏实例创建 DOM 容器. |


> 源码：[src/dom/CreateDOMContainer.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/CreateDOMContainer.js#L9)  
引入版本：3.12.0


---

### DOMContentLoaded {#DOMContentLoaded}

#### \<static> DOMContentLoaded(callback) {#static-domcontentloadedcallback}


**说明:**

检查文档的 readyState 。 如果文档已经完整或交互, 它会立即引用给定的调用符。 如果不是, 它会注册事件听众在文档准备完毕时检测。 在 Cordova 环境中, 它会为 `deviceready` 事件收听; 否则它会为 `DOMContentLoaded` 和窗口的 `load` 事件收看, 并首先引用调用调用符。 如果文档主体尚未可用, 则会回到短时间后再引用调用符。 自动由 Phaser.Game 实例调用。 通常不应该直接访问 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| callback | ContentLoadedCallback | 否 | 当设备准备就绪并装入DOM内容时,要引用的回调 。 |


> 源码：[src/dom/DOMContentLoaded.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/DOMContentLoaded.js#L15)  
引入版本：3.0.0


---

### GetInnerHeight {#GetInnerHeight}

#### \<static> GetInnerHeight(iOS) {#static-getinnerheightios}


**说明:**

尝试确定跨越 iOS和标准设备的文档内高。 在非 iOS设备上, 仅返回 `window.innerHeight`。 在 iOS上, Safari 的动态浏览器铬( 如显示或隐藏在滚动上) 会导致 `window.innerHeight` 报告不准确的值。 要围绕此点开展工作, 将一个大小为 `100vh`的临时固定位置元素注入 DOM, 使用它测量的高度, 并立即删除该元素。 其结果也根据 Z`window.orientation`的代码调整了 。 由 @ tylerjpeterson 编辑 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| iOS | boolean | 否 | 这是在运行iOS? |


**返回值:** number - 观光门内高,以像素为单位.


> 源码：[src/dom/GetInnerHeight.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/GetInnerHeight.js#L7)  
引入版本：3.16.0


---

### GetScreenOrientation {#GetScreenOrientation}

#### \<static> GetScreenOrientation(width, height) {#static-getscreenorientationwidth-height}


**说明:**

尝试使用一系列浏览器API确定屏幕方向,如果没有的话,则回落到比较视图的维度.

它检查了屏幕方向 API( 屏幕方向 ) 。`screen.orientation`, `screen.mozOrientation`, `screen.msOrientation`),遗产 `window.orientation` 财产(在 iOS),该 `window.matchMedia` API,最后作为最后手段,简单进行宽度比高比较.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| width | number | 否 | 观音门的宽度. |
| height | number | 否 | 观音高处. |


**返回值:** string - 或 `Phaser.Scale.PORTRAIT` 或 `Phaser.Scale.LANDSCAPE` 字符串常数,或由屏幕方向 API 返回的原始方向类型字符串 。


> 源码：[src/dom/GetScreenOrientation.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/GetScreenOrientation.js#L9)  
引入版本：3.16.0


---

### GetTarget {#GetTarget}

#### \<static> GetTarget(element) {#static-gettargetelement}


**说明:**

尝试根据给定值获取目标 DOM 元素, 可以是字符串, 也可以是元素节点, 如果找不到, 则返回文档的引用 。 body 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| element | HTMLElement | 否 | 要查找的 DOM 元素。 可以是字符串, 也可以是元素ID, 通过 `document.getElementById` 查找, 或者直接引用 HTMLElement 节点 。 |


**返回值:** HTMLElement - 匹配给定的ID或节点引用的DOM元素,或者如果找不到有效目标,则`document.body`.


> 源码：[src/dom/GetTarget.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/GetTarget.js#L7)  
引入版本：3.16.0


---

### ParseXML {#ParseXML}

#### \<static> ParseXML(data) {#static-parsexmldata}


**说明:**

将给定的数据串作为 XML 解析。 首先尝试使用窗口. DOMParser , 如果失败则返回到 Microsoft. XMLDOM 。 解析的 XML 对象被返回, 如果在解析数据时出错则返回 `null` 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | string | 否 | XML 源存储在一个字符串中. |


**返回值:** XMLDocument - 解析的 XML 数据, 或 如果无法解析数据, 则解析为 `null` 。


> 源码：[src/dom/ParseXML.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/ParseXML.js#L7)  
引入版本：3.0.0


---

### RemoveFromDOM {#RemoveFromDOM}

#### \<static> RemoveFromDOM(element) {#static-removefromdomelement}


**说明:**

试图从DOM中的parentNode中移除元素.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| element | HTMLElement | 否 | 将主节点删除的 DOM 元素 。 |


> 源码：[src/dom/RemoveFromDOM.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/dom/RemoveFromDOM.js#L7)  
引入版本：3.0.0


---

---
