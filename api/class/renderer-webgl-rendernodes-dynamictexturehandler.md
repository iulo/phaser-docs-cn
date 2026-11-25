# DynamicTextureHandler {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/renderer-webgl-rendernodes-dynamictexturehandler)

一个负责执行`DynamicTexture`记录绘图命令的RenderNode. A`DynamicTexture`将绘图操作(印章,重复,填充,清除,游戏对象绘图,回调,和捕获)累积到命令缓冲器中,每次使用这个处理器的`run`方法,它都会通过该缓冲器执行每个命令,并针对纹理的WebGL帧缓冲器执行.

操作器在执行过程中管理所有必要的 WebGL 状态: 它解开帧缓冲器自身的纹理,以防止反馈循环,配置剪刀盒,并创建或释放克隆绘图背景作为混合模式,并消除整个命令中模式的改变。当一个 Preserve 命令未显示时,在渲染后命令缓冲器被清除,准备下一帧的绘图调用 。

**构造函数**

`new DynamicTextureHandler(manager)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| manager | [Phaser.Renderer.WebGL.RenderNodes.RenderNodeManager](/api/class/renderer-webgl-rendernodes-rendernodemanager) | 否 | 这个RenderNode的经理 |

---


**作用域**: static


**继承**

> [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode)  



> 源码：[src/renderer/webgl/renderNodes/DynamicTextureHandler.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/DynamicTextureHandler.js#L13)  
引入版本：4.0.0

## 继承的成员 {#inherited-members}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [manager](/api/class/renderer-webgl-rendernodes-rendernode#manager)
 - [name](/api/class/renderer-webgl-rendernodes-rendernode#name)




---

## 公开成员 {#public-members}

### fillRectNode {#fillRectNode}

#### fillRectNode: [Phaser.Renderer.WebGL.RenderNodes.FillRect](/api/class/renderer-webgl-rendernodes-fillrect) {#fillrectnode-phaserrendererwebglrendernodesfillrect}


**说明:**

绘制填充矩形的RenderNode 。


> 源码：[src/renderer/webgl/renderNodes/DynamicTextureHandler.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/DynamicTextureHandler.js#L43)  
引入版本：4.0.0


---

## 继承的方法 {#inherited-methods}


**From [Phaser.Renderer.WebGL.RenderNodes.RenderNode](/api/class/renderer-webgl-rendernodes-rendernode):**


 - [onRunBegin](/api/class/renderer-webgl-rendernodes-rendernode#onRunBegin)
 - [onRunEnd](/api/class/renderer-webgl-rendernodes-rendernode#onRunEnd)
 - [setDebug](/api/class/renderer-webgl-rendernodes-rendernode#setDebug)




---

## 公开方法 {#public-methods}

### run {#run}

#### \<instance> run(dynamicTexture) {#instance-rundynamictexture}


**说明:**

处理给定的动态图案的指令缓冲器, 并针对其 WebGL 帧缓冲器执行每次记录的绘图操作。 其中包括印出纹理、 纹理图案、 填充矩形图案、 清除区域、 绘制任意游戏对象、 擦除模式、 引用自定义调用回调和捕获游戏对象到分区。 绘图背景会被克隆并发布, 并会改变所有命令的混合模式。 除非遇到 PRESERVE 命令, 命令缓冲器将被清除, POST_ RENDER 相机事件将被释放 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| dynamicTexture | [Phaser.Textures.DynamicTexture](/api/class/textures-dynamictexture) | 否 | 动态图案要渲染。 |


**Overrides:** Phaser.Renderer.WebGL.RenderNodes.RenderNode#运行


> 源码：[src/renderer/webgl/renderNodes/DynamicTextureHandler.js#L53](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/webgl/renderNodes/DynamicTextureHandler.js#L53)  
引入版本：4.0.0


---

---
