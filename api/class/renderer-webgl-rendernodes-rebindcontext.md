# RebindContext {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-rebindcontext)

RebindContext是一个RenderNode,它将WebGL上下文设置为默认状态,重置了可能已被外部渲染器改变的重要属性.

此功能在渲染后被Extern Game Object 使用。 它是 YieldContext 的对应功能 。

**构造函数**

`new RebindContext(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/RebindContext.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RebindContext.js#L11)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(displayContext) {#instance-rundisplaycontext}


**说明:**

在外部渲染器完成渲染后, 将 WebGL 上下文重置为默认状态。 这可以清除当前帧缓冲器的速率和深度渲染器, 用无效资源重新组合 WebGL 状态, 并解封所有纹理单元, 强制在下次使用时重新绑定 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| displayContext | [Phaser.Renderer.WebGL.DrawingContext](/api/class/renderer-webgl-drawingcontext) | 否 | 当前绘图背景 。 |


**重写:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/RebindContext.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/RebindContext.js#L57)  
引入版本：4.0.0


---

---
