# 纹理 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/textures)

纹理管理器的主要作用是创建和存储 Phaser纹理类的例。 纹理类包含 Phaser 内部使用纹理所需的全部数据。 例如, Sprite 包含一个既引用它使用的纹理又引用框架的参考物。 基础纹理存在于全局纹理管理器中。 这意味着多个游戏对象都非常常用相同的纹理实例 。

纹理是由一个或多个框架构成的。 您可以将一个框架视为纹理内部的长方形区域。 通过使用框架, 您可以将一个单一的纹理分割成多个不同的区域。 当告诉一个Sprite使用哪个纹理时, 您也可以告诉它从那个纹理中选择哪个框架使用。 如果您有包含着框架的纹理, 您可以告诉Sprite只使用其中的框 5 。

您可能以前听说过Sprite 工作表或纹理图集。 在 Phaser 中, 基础的图案表或图集将是一个单一的纹理实例, 它包含尽可能多的框架实例, 以表示工作表中的框架。 纹理管理器大多数的解析器的任务是拍摄图像和数据文件, 然后根据这些信息创建它所需要的所有框架 。

Frames的概念也是Phaser如何处理动画,通过按您定义的顺序,以给定的帧率"播放"这些帧.

纹理有更先进的类型,例如动态纹理和Canvas纹理,我们稍后会覆盖这些纹理。但从根本上来说,Phaser游戏对象大多使用纹理和框架来进行屏幕的渲染。

## 纹理 {#textures}

**纹理** 拥有密钥, 第一个帧名称, 帧图, 一个或多个源图像( 扫描、 图像、 视频) , 以及 0 或多个数据源图像( 正常地图 ) 。 有三个纹理类, [CanvasTexture](/api/class/textures-canvastexture)、 [DynamicTexture](/api/class/textures-dynamictexture)和 [Texture](/api/class/textures-texture) 。

最大纹理尺寸取决于设备;您可以检查`renderer.getMaxTextureSize()`. 移动的2048px和桌面的4096px应该安全.

### 默认纹理 {#default-textures}

- 默认 : `'__DEFAULT'`
- 失踪: `'__MISSING'`
- 4x4 白色: `'__WHITE'`

### 在管理器中获取纹理密钥 {#get-texture-keys-in-the-manager}

```js
const keys = this.textures.getTextureKeys(); // → ['mummy', 'bat', 'torch', …]
```

### 从管理器那里取出纹理 {#get-a-texture-from-the-manager}

`textures.get()` ** 总是** 返回一个纹理; 如果没有这样的密钥, 它将是 `__MISSING` 纹理。 所以您应该先使用 `textures.exists()` 。

```js
const texture = this.textures.exists("mummy")
  ? this.textures.get("mummy")
  : null;
```

### 从数组生成纹理 {#generate-texture-from-array}

```js
var config = {
  data: data,
  // 3x3:
  // [ '...',
  //   '...',
  //   '...' ]
  pixelWidth: 1, // pixel width of each data
  pixelHeight: 1, // pixel height of each data
  preRender: null, // callback, function(canvas, ctx) {}
  postRender: null, // callback, function(canvas, ctx) {}

  canvas: null, // create a canvas if null
  resizeCanvas: true,
  clearCanvas: true,
};
var texture = this.textures.generate(key, config);
```

#### 校验现有纹理 {#verify-existing-texture}

```js
var hasKey = this.textures.exists(key);
```

### 获取基座64 {#get-base64}

```js
var s = this.textures.getBase64(key); // type= 'image/png', encoderOptions= 0.92
// var s = this.textures.getBase64(key, frame, type, encoderOptions);
```

### 获取像素颜色 {#get-pixel-color}

```js
var color = this.textures.getPixel(x, y, key);
// var color = this.textures.getPixel(x, y, key, frame);
```

`color` 属性

- `r` : 0 ~ 255
- `g` : 0 ~ 255
- `b` : 0 ~ 255
- `a` : 0 ~ 255

```js
var alpha = this.textures.getPixelAlpha(x, y, key);
// var alpha = this.textures.getPixelAlpha(x, y, key, frame);
```

alpha : 0 ~ 255

如果坐标超出范围,则返回`null`。

### 删除纹理 {#remove-texture}

删除存储在纹理缓存中的纹理 。

```js
this.textures.remove(key);
```

### 装入图像用于纹理 {#loading-images-for-textures}

通常您不会直接创建纹理。 Phaser 会在您装入图像时为您创建纹理 。

- `load.image()`用单帧`__BASE`创建纹理.
- `load.spritesheet()`创建了一种纹理,框架命名为整数,从`0`开始,加上`__BASE`.
- `load.atlas()`或`load.unityAtlas()`创建了带有图集数据中命名的帧的纹理,加上`__BASE`.
- `load.multiatlas()` 创建相同, 并有多个源图像

在Phaser术语中,"Spritesheet"在行或列中具有统一的单元格,而"地图册"则在任意大小和位置上都有帧. Phaser可以加载由Texture Packer(任何"Phaser 3"格式)或Unity创建的地图册.

Phaser可以使用浏览器可以显示的[any image format](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types). SVG在造型时被光栅化(通过浏览器). Phaser v3.60支持[WebGL compressed textures](https://developer.nvidia.com/astc-texture-compression-for-game-assets#_Toc398571907).

- [How to create sprite sheets for Phaser 3 with TexturePacker](https://www.codeandweb.com/texturepacker/tutorials/how-to-create-sprite-sheets-for-phaser3)

#### 使用量 {#usage}

- 装入图像纹理

  ```js
  this.load.image(key, url);
  ```

- 通过基数64 装入图像纹理

  ```js
  this.textures.addBase64(key, data);
  ```

- 获取图像纹理

  ```js
  var texture = this.textures.get(key);
  var image = texture.getSourceImage();
  // var width = image.width;
  // var height = image.height;
  ```

- 从框架对象获取图像纹理

  ```js
  var texture = this.textures.get(frameObject);
  ```

### 完整图像的纹理 {#textures-from-complete-images}

如果您已经有一个完整的 [image](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement "HTMLImageElement") 或 [canvas](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement) , 您可以直接使用 `addImage()` 、 `addSpriteSheet()` 、 `addAtlas()` 等方法将其添加到纹理管理器中。 这些方法与相应的负载方法非常相似, 但是它们会采用 `sourceImage` 参数( 图像或画布) 而不是 URL 。

您可以用这种方式从同一个来源做第二个纹理, 如果您想创建不同的帧集 :

```js
this.textures.addImage(
  "mummyCopy",
  this.textures.get("mummy").getSourceImage()
);
```

### 画布纹理 {#canvas-texture}

罐装纹理有以[2d rendering context](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)为源的[canvas](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)。您可以使用其中的任何一种[Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)。您可以绘制其上的纹理框架,但不能绘制游戏对象(参见动态纹理) 。

您可以用 `createCanvas()` 创建空白画布纹理 :

`const texture = this.textures.createCanvas('key', width, height);`

或使用已有的画布 :

`const texture = this.textures.addCanvas('key', canvas);`

使用 `drawFrame()` 在 Canvas 纹理上绘制另一个纹理框架 :

`texture.drawFrame('mummy', 1, x, y);`

或 `draw()` 如果您有源图像( 不寻常) :

`texture.draw(sourceImage, x, y);`

如果您直接在画布上下文上工作, 完成时刷新纹理 :

```js
const ctx = texture.getContext();

// CanvasTexture has its own `width` and `height`.
// You could also read these from the base frame, as with the Texture class.
const { width, height } = texture;

ctx.fillStyle = "ghostwhite";
ctx.fillRect(0, 0, width, height);

texture.refresh();
```

`refresh()` 需要更新纹理以显示于 WebGL 渲染模式。不要调用 `refresh()` 之后 `draw()` 或 或 时 间 `drawFrame()`已经包括了

若在绘制后需要使用`getPixel()`或`getPixels()`,请拨打`update()`而不是`refresh()`.

#### 使用量 {#usage-1}

- 创建画布纹理

  ```js
  var texture = scene.textures.createCanvas(key, width, height);
  ```

- 获取画布元素

  ```js
  var canvas = texture.getCanvas();
  var context = texture.getContext();
  ```

  [Canvas api](https://www.w3schools.com/html/html5_canvas.asp)

- 绘制框架

  ```js
  texture.drawFrame(key, frame, x, y);
  // texture.drawFrame(key, frame, x, y, update);
  ```

  - `update`:更新内部的图像数据缓冲器和阵列。默认值为`true`。

- 绘制图像

  ```js
  texture.draw(x, y, source);
  // texture.draw(x, y, source, update);
  ```

  - `source`: HTML 图像元素,或 HTML 画幅的 Canvas 元素 。
  - `update`:更新内部的图像数据缓冲器和阵列。默认值为`true`。

- Clear

  ```js
  texture.clear();
  ```

  or

  ```js
  texture.clear(x, y, width, height);
  // // texture.clear(x, y, width, height, update);
  ```

  - `update`:更新内部的图像数据缓冲器和阵列。默认值为`true`。

- 刷新纹理

  ```js
  texture.refresh();
  ```

- 颜色纹理

  - 获取像素颜色

    ```js
    var color = texture.getPixel(x, y);
    // var color = texture.getPixel(x, y, color);
    ```

    ```js
    var colors = texture.getPixels(x, y, width, height);
    ```

    - `colors` : `[{x, y, color, alpha}, ...]`

  - 设置像素颜色

    ```js
    texture.setPixel(x, y, red, green, blue);
    // texture.setPixel(x, y, red, green, blue, alpha);
    ```

- 图像数据

  - 获取图像数据

    ```js
    var imageData = texture.getData(x, y, width, height);
    ```

  - 设定图像数据

    ```js
    texture.putData(imageData, x, y);
    ```

- 添加帧

  ```js
  texture.add(name, sourceIndex, x, y, width, height);
  ```

  - `name`: 此框架的名称。 名称在纹理内是独一无二的 。
  - `sourceIndex`:这个框架是其一部分的纹理源索引.
  - `x` : 此框架左上角的 x 坐标 。
  - `y` : 此框架左上角的y坐标 。
  - `width` : 此框架的宽度 。
  - `height` : 此框架的高度 。

### 动态纹理 {#dynamic-texture}

动态纹理(Dynamic Texture)是一种特殊的纹理,它允许您直接绘制纹理,帧和最类游戏对象.

#### 使用量 {#usage-2}

- 创建动态纹理

  ```js
  var texture = scene.textures.addDynamicTexture(key, width, height);
  ```

  如果此纹理不是Sprite游戏对象的基础纹理, 则禁用 `texture.isSpriteTexture` 。

  ```js
  texture.setIsSpriteTexture(false);
  // texture.isSpriteTexture = false;
  ```

- 设定大小

  ```js
  texture.setSize(width, height);
  ```

- 填充颜色

  ```js
  texture.fill(rgb);
  // texture.fill(rgb, alpha, x, y, width, height);
  ```

  - `rgb`: 以数字颜色填充此动态纹理 。
  - `alpha`:填充时使用的α值。默认值为`1`。
  - `x`,`y`,`width`,`height`:填充矩形的区域,默认行为是填充整块大小.

- Clear

  ```js
  texture.clear();
  ```

  ```js
  texture.clear(x, y, width, height);
  ```

- 绘制游戏对象

  ```js
  texture.draw(entries);
  // texture.draw(entries,x, y);
  // texture.draw(entries, x, y, alpha, tint);
  ```

  - `entries` :
    - 任意可渲染的游戏对象,例如Sprite,Text,Graphics或TileSprite.
    - 平面图层.
    - A组,内容将依次加以修改和绘制。
    - 集装箱,内装物将按顺序完全悬挂和抽取。
    - 一个场景显示列表,通过`Scene.children`来绘制整个列表.
    - 另一种动态纹理,或称Render纹理.
    - 纹理框架实例 。
    - 字符串。 用于从纹理管理器中查找纹理 。
  - `x`, `y`: 绘制框架的 x/y 位置,或对对象应用的偏移.
    - 如果物体是团体、集装箱或显示清单,则坐标为_在儿童位置上加_。
    - 对于所有其他类型的天体,坐标是准确的.
  - `alpha`,`tint`:只有纹理框架使用.
    - 游戏对象在绘制时使用自己的α和锡值.

- Erase

  ```js
  texture.erase(entries);
  // texture.erase(entries, x, y);
  ```

  - `entries` :
    - 任意可渲染的游戏对象,例如Sprite,Text,Graphics或TileSprite.
    - 平面图层.
    - A组,内容将依次加以修改和绘制。
    - 集装箱,内装物将按顺序完全悬挂和抽取。
    - 一个场景显示列表,通过`Scene.children`来绘制整个列表.
    - 另一种动态纹理,或称Render纹理.
    - 纹理框架实例 。
    - 字符串。 用于从纹理管理器中查找纹理 。
  - `x`, `y`: 绘制框架的 x/y 位置,或对对象应用的偏移.
    - 如果物体是团体、集装箱或显示清单,则坐标为_在儿童位置上加_。
    - 对于所有其他类型的天体,坐标是准确的.

- 绘制框架

  ```js
  texture.stamp(key, frame, x, y, {
    alpha: 1,
    tint: 0xffffff,
    angle: 0,
    rotation: 0,
    scale: 1,
    scaleX: 1,
    scaleY: 1,
    originX: 0.5,
    originY: 0.5,
    blendMode: 0,
    erase: false,
    skipBatch: false,
  });
  ```

  or

  ```js
  texture.drawFrame(key, frame, x, y);
  // texture.drawFrame(key, frame, x, y, alpha, tint);
  ```

  - `x`, `y` : 左上方位置

- 绘制重复框架

  - 重复装满大小的帧

    ```js
    texture.repeat(key, frame);
    ```

  - 在区域中重复

    ```js
    texture.repeat(key, frame, x, y, width, height);
    // texture.repeat(key, frame, x, y, width, height, alpha, tint, skipBatch);
    ```

- 添加帧

  ```js
  texture.add(name, sourceIndex, x, y, width, height);
  ```

  - `name`: 此框架的名称。 名称在纹理内是独一无二的 。
  - `sourceIndex`:这个框架是其一部分的纹理源索引.
  - `x` : 此框架左上角的 x 坐标 。
  - `y` : 此框架左上角的y坐标 。
  - `width` : 此框架的宽度 。
  - `height` : 此框架的高度 。

- 批量绘图

  1. Begin

     ```js
     texture.beginDraw();
     ```

  2. Draw

     - 绘制游戏对象

       ```js
       texture.batchDraw(entries, x, y, alpha, tint);
       ```

       - `entries` :
         - 任意可渲染的游戏对象,例如Sprite,Text,Graphics或TileSprite.
         - 平面图层.
         - A组,内容将依次加以修改和绘制。
         - 集装箱,内装物将按顺序完全悬挂和抽取。
         - 一个场景显示列表,通过`Scene.children`来绘制整个列表.
         - 另一种动态纹理,或称Render纹理.
         - 纹理框架实例 。
         - 字符串。 用于从纹理管理器中查找纹理 。

     - 绘制框架

       ```js
       texture.batchDrawFrame(key, frame, x, y, alpha, tint);
       ```

     - 绘制图像

       ```js
       texture.stamp(key, frame, x, y, {
         // ...
         skipBatch: true,
       });
       ```

     - 绘制重复图像

       ```js
       texture.repeat(key, frame, x, y, width, height, alpha, tint, true);
       ```

  3. End

     ```js
     texture.endDraw();
     ```

- 内部相机

  内部相机 `texture.camera`

  - 滚动( 抵销)

    ```js
    texture.camera.setScroll(x, y);
    ```

  - 缩放( 缩放)

    ```js
    texture.camera.setZoom(zoom);
    ```

  - Rotate

    ```js
    texture.camera.setAngle(angle); // angle in degrees
    ```

- Snapshot

  - 抓图区域

    ```js
    texture.snapshot(callback);
    // texture.snapshot(callback, type, encoderOptions);
    ```

    or

    ```js
    texture.snapshotArea(x, y, width, height, callback, type, encoderOptions);
    ```

    - `callback`:在快照图像创建后要引用的函数 。

      ```js
      function(imageElement) {
      }
      ```

      - `imageElement` : HTML ImageElement. 维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维基月球在线解说-维尔日报-维尔日报-维尔德·维尔曼.

    - `type`:图像创建的格式,通常为`'image/png'`或`'image/jpeg'`. 默认值为`'image/png'`.
    - `encoderOptions`: 图像质量,介于`0`和`1`之间,用于图像格式,具有失压缩,如`'image/jpeg'`,默认值为`0.92`.
    - `x`, `y`, `width`, `height` :快照区。

- 获取像素的颜色

  ```js
  texture.snapshotPixel(x, y, callback);
  ```

  - `x`,`y`:像素的x/y坐标来得到.
  - `callback`:在快照图像创建后要引用的函数 。

    ```js
    function(colorObject) {
    }
    ```

    - `colorObject` : 或 被抓取一个像素的颜色对象, 或 包含画布内容的快照的新图像 。

#### 纹理 {#render-texture}

成形纹理本质上是握有动态纹理的[Image](/api/class/gameobjects-image).

### 事件 {#events}

- 纹理管理器准备好了

  ```js
  this.textures.on("ready", function () {});
  ```

- 添加纹理

  ```js
  this.textures.on("addtexture", function (key) {});
  ```

  or

  ```js
  this.textures.on("addtexture-" + key, function () {});
  ```

- 添加纹理时出错

  ```js
  this.textures.on("onerror", function (key) {});
  ```

- 删除纹理

  ```js
  this.textures.on("removetexture", function (key) {});
  ```

  or

  ```js
  this.textures.on("removetexture-" + key, function () {});
  ```

## 框架 {#frames}

**框架** 框架有一个名称、位置、几个维度( `realWidth`和 `realHeight` 最重要) , 以及一个可选的自定义枢轴。 文件称框架名称为“ 名称”(用于地图集纹理) 和“ 索引”(用于图示表纹理) , 但它们都是相同的。 所有纹理都有一个特殊的框架, 名为“ `__BASE`”, 代表整个纹理 。

纹理储存在纹理管理器中, `this.textures` 现场或 `game.textures`。纹理游戏对象在它们中保留其当前纹理和框 `texture` 财务报告和已审计财务报表 `frame` 属性。

内置纹理有三种: 内置纹理: 内置纹理: `__DEFAULT` (32×32透明), `__MISSING` (32×32绿色斜箱),和 `__WHITE` (4×4白). 杭州市志·人物志·人物志·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物·人物

### 获取纹理框架名称 {#get-frame-names-for-a-texture}

```js
const frameNames = this.textures.get("mummy").getFrameNames(); // → [0, 1, 2, …]
```

- [Example: Get frame names from atlas texture](https://labs.phaser.io/edit.html?src=src/loader\texture%20atlas%20json\load%20texture%20atlas.js)

### 获取全部纹理密钥和框架名称 {#get-all-texture-keys-and-frame-names}

```js
for (const textureKey of this.textures.getTextureKeys()) {
  console.info(textureKey, this.textures.get(textureKey).getFrameNames(true));
}
```

### 从纹理中获取一个框架 {#get-a-frame-from-a-texture}

#### 使用量 {#usage-3}

- 从纹理中获取框架

```js
var frame = this.textures.getFrame(key, frame);
```

- 框架属性

  - `frame.source.image`:纹理源的图像.
  - `frame.cutX`:在源图像中X位置切除.
  - `frame.cutY`:Y在源图像中的位置从剪切.
  - `frame.cutWidth`:要剪切的源图像中区域宽度.
  - `frame.cutHeight`:要剪切的源图像中区域高度.

- Examples:

  ```js
  const mummyFrame1 = this.textures.getFrame("mummy", 1);
  // OR
  const mummyFrame1 = this.textures.get("mummy").get(1);
  ```

  纹理本身在技术上没有维度;对于您想要从基框读取的:

  ```js
  const { realWidth, realHeight } = this.textures.getFrame("mummy", "__BASE");
  ```

##### 设置纹理过滤模式 {#set-a-textures-filter-mode}

```js
// Nearest-neighbor filter (pixelated)
this.textures.get("mummy").setFilterMode(Phaser.Textures.FilterMode.NEAREST);

// Linear filter (antialiased)
this.textures.get("mummy").setFilterMode(Phaser.Textures.FilterMode.LINEAR);
```

##### 从游戏对象工作 {#working-from-a-game-object}

游戏对象的`texture`和`frame` 持有其当前纹理和帧,所以你可以在那里访问它们而不是从纹理管理器进入它们。只需记住你正在和共享对象合作.

```js
const mummy = this.add.sprite(0, 0, "mummy", 1);

console.log(mummy.texture.key); // → 'mummy'
console.log(mummy.frame.name); // → 1

const mummyFrame1 = mummy.texture.get(1);
```

### 设置自定义枢轴点( 来源) {#setting-custom-pivot-points-origin}

```js
for (const frame of Object.values(this.textures.get("sprites").frames)) {
  if (frame.name === "__BASE") {
    continue;
  }

  frame.customPivot = true;
  frame.pivotX = 0.5;
  frame.pivotY = 1;

  console.log(frame.texture.key, frame.name, frame.pivotX, frame.pivotY);
}
```

### 添加框架 {#add-frames}

`texture.add(frameName, sourceIndex, x, y, width, height);`

您可以使用数字或字符串框名. `sourceIndex`是单源纹理的 `0`.

框架可以被克隆,但您必须手动添加新框架对象 :

```js
// Clone frame 0 of texture "asp".
const aspFrame = this.textures.cloneFrame("asp", 0);

// Add it as frame 0 of the "bat" texture.
const batTexture = this.textures.get("bat");

batTexture.frames[aspFrame.name] = aspFrame;

batTexture.frameTotal += 1;
```

您可以在任意纹理中添加框架。 您可以在这里将单个框架的纹理“ 转换为多框架的纹理表 :

```js
this.load.image("example", "example.png");

this.load.once("filecomplete-image-example", () => {
  const texture = this.textures.get("image");

  texture.firstFrame = 0;

  texture.add(0 /* … */);
  texture.add(1 /* … */);
  texture.add(2 /* … */);

  texture.getFrameNames(); // -> [0, 1, 2]
});
```

在实践中,您通常会添加帧来创建多帧的Canvas纹理或动态纹理(见下文).

### 添加地图集 {#add-atlas}

```js
this.textures.addAtlas(key, HTMLImageElement, data);
// this.textures.addAtlas(key, HTMLImageElement, data, dataSource);
```

- `key`:纹理中独特的基于字符串的键.
- `HTMLImageElement`: HTML 图像元素/s.
- `data`:纹理图集数据/s.

  ```js
  {
      frames: [
          {
              // Location of frame image
              frame: {
                  x, y, w, h
              },

              // trimmed
              trimmed:
              sourceSize: {
                  w, h
              },
              spriteSourceSize: {
                  x, y, w, h
              },

              rotated:

              // Custom origin
              anchor:
              pivot: {
                  x, y
              },

              // Other custom properties of this frame ...
          }
      ],

      // Other custom properties of this texture ...
  }
  ```

- `dataSource`:一个可选的数据图像元素(正常地图).

or

```js
this.textures.addAtlas(undefined, texture, data);
// this.textures.addAtlas(undefined, texture, data, dataSource);
```

- `texture` : Phaser 纹理.

### 添加图示工作表 {#add-sprite-sheet}

```js
this.textures.addSpriteSheet(key, HTMLImageElement, config);
// this.textures.addAtlas(key, HTMLImageElement, config, dataSource);
```

- `key`:纹理中独特的基于字符串的键.
- `HTMLImageElement`: HTML 图像元素/s.
- `config`: 此Sprite工作表的配置对象 。

  ```js
  {
      frameWidth: ,
      frameHeight: ,
      startFrame: 0,
      endFrame: -1,
      margin: 0,
      spacing: 0
  }
  ```

- `dataSource`:一个可选的数据图像元素(正常地图).

or

```js
this.textures.addSpriteSheet(undefined, texture, config);
// this.textures.addSpriteSheet(undefined, texture, config, dataSource);
```

- `texture` : Phaser 纹理.

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)
- [samme](https://github.com/samme)

---
