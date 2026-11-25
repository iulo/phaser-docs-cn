# Phaser.Core {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/core)

Scope: 
static
> 源码：[src/core/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/index.js#L7)  


## 静态函数 {#static-functions}

- [Config](/api/class/core-config)
- [TimeStep](/api/class/core-timestep)
## 静态函数 {#static-functions-1}

### CreateRenderer {#CreateRenderer}

#### \<static> CreateRenderer(game) {#static-createrenderergame}


**说明:**

由Phaser.Game自动调用,负责创建它将使用的渲染器.

检查游戏配置以确定合适的渲染类型(WebGL,Canvas,或Headless),验证所选渲染器由当前设备支持,设置画布元素(要么采用游戏配置中提供的,要么从CanvasPool创建新的),应用任何画布 CSS风格和像素艺术插图设置,然后即时化,将渲染器指定为`game.renderer`.

使用两个 Webpack 全球旗, `WEBGL_RENDERER` 和 `CANVAS_RENDERER` , 它们是在构建时定义的, 并被内嵌到编译时常数的捆绑中。 它们不能作为运行时变量提供, 并且确定构建中包含哪些渲染器类 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 用于设定渲染器的 Phaser.Game 实例 。 |


> 源码：[src/core/CreateRenderer.js#L12](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/CreateRenderer.js#L12)  
引入版本：3.0.0


---

### DebugHeader {#DebugHeader}

#### \<static> DebugHeader(game) {#static-debugheadergame}


**说明:**

自动调用 Phaser.Game 初始化时, 向浏览器控制台输出一个样式化的横幅。 横幅显示 Phaser 版本编号, 活动渲染器( Q) :WebGL, Canvas, 或 Headles),正在使用的音频系统(Web Audio, HTML5 Audio, 或无Audio),以及任意配置的游戏标题、版本和URL。在支持CSS控制台样式的浏览器中,旗标的颜色会按照游戏配置中定义的颜色来渲染;在IE中,它会倒回到纯文本日志中。当全部跳过时,横幅会全部跳过 。 `config.hideBanner` 谓 `true`.

您可以通过 Game Config 对象自定义或禁用标题 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 输出此调试头的 Phaser.Game 实例 。 |


> 源码：[src/core/DebugHeader.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/DebugHeader.js#L9)  
引入版本：3.0.0


---

### VisibilityHandler {#VisibilityHandler}

#### \<static> VisibilityHandler(game) {#static-visibilityhandlergame}


**说明:**

可见度处理器负责监听文档级别可见度变化事件和窗口模糊/焦点事件,然后通过游戏事件Emitter重新发布,以便框架的其余部分能够作出适当的反应——比如玩家在切换标签或最小化浏览器窗口时会跳出游戏循环,并在返回时恢复.

它可以听标准 `visibilitychange` 支持,并回到供应商前置等价物(`webkitvisibilitychange`, `mozvisibilitychange`, `msvisibilitychange`)用于旧浏览器。窗口级别 `blur` 财务报告和已审计财务报表 `focus` 事件也被捕获,用于处理标签仍然可见但窗口失去焦点的情况。

如果游戏配置启用了`autoFocus`,处理器也会在设置时调用`window.focus()`,以确保游戏在装入时立即抓取键盘输入.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| game | [Phaser.Game](/api/class/game) | 否 | 可见度处理器正在研究的游戏实例 。 |


**触发事件:** [Phaser.Core.Events#event:BLUR](/api/event/core-events#blur), [Phaser.Core.Events#event:FOCUS](/api/event/core-events#focus), [Phaser.Core.Events#event:HIDDEN](/api/event/core-events#hidden), [Phaser.Core.Events#event:VISIBLE](/api/event/core-events#visible)


> 源码：[src/core/VisibilityHandler.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/VisibilityHandler.js#L9)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-2}

- [Events](/api/namespace/core-events)

---
