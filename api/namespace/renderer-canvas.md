# Phaser.Renderer.Canvas {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/renderer-canvas)

Scope: 
static
> 源码：[src/renderer/canvas/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/index.js#L7)  


## 静态函数 {#static-functions}

- [CanvasRenderer](/api/class/renderer-canvas-canvasrenderer)
## 静态函数 {#static-functions-1}

### GetBlendModes {#GetBlendModes}

#### \<static> GetBlendModes() {#static-getblendmodes}


**说明:**

返回一个阵列, 将默认混合模式映射到支持 Canvas 混合模式 。

如果浏览器不支持混合模式,它会默认为普通的`source-over`混合模式.


**返回值:** array - 彩色混合模式对应的就是默认的 Phaser 混合模式。


> 源码：[src/renderer/canvas/utils/GetBlendModes.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/utils/GetBlendModes.js#L10)  
引入版本：3.0.0


---

### SetTransform {#SetTransform}

#### \<static> SetTransform(renderer, ctx, src, camera, [parentMatrix]) {#static-settransformrenderer-ctx-src-camera-parentmatrix}


**说明:**

引用 Canvas 渲染器、 Canvas 渲染上下文、 游戏对象、 摄像机和母矩阵, 然后执行以下步骤 :

1. 检查源的α与摄像机α结合。 如果 0 或 更小, 则中止 。

2. 使用摄像机和游戏对象矩阵,并把它们乘以,如果给出的话,与母矩阵结合。

3. 设置上下文的混合模式,以作为游戏对象所使用的模式。

4. 设定上下文的α值,以游戏对象与摄像机结合使用。

5. 保存上下文状态。

6. 通过 setTransform 将最终矩阵值设置到上下文中。

7. 如果游戏对象有纹理帧, imageSmoothingEnabled 以帧. source 设置。scaleMode.

8. 如果游戏对象没有纹理帧,imageSmoothingEnabled则基于Render.antalias设定.

此功能仅用于内部, 大部分Canvas Renderer 类都使用它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](/api/class/renderer-canvas-canvasrenderer) | 否 | 参考当前活跃的Canvas渲染器. |
| ctx | CanvasRenderingContext2D | 否 | 设置转换的画布上下文 。 |
| src | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 正在渲染游戏对象。 可以是扩展基类的任意类型 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 正在制作游戏对象的摄像机 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 父变换矩阵,在渲染前应用到 Game Object 上. |


**返回值:** boolean - 如果设定了游戏对象上下文,则使用`true`,否则使用`false`.


> 源码：[src/renderer/canvas/utils/SetTransform.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/canvas/utils/SetTransform.js#L9)  
引入版本：3.12.0


---

---
