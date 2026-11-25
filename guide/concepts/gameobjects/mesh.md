# 网格（Mesh） {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/mesh)

Mesh游戏对象允许您制作一组纹理化的顶点,并操纵这些顶点的视图,如旋转,翻译或缩放.

包括支持从网格,模型数据或波前OBJ文件生成网格数据.

尽管您可以使用此来渲染3D对象, 但其主要用途是显示更复杂的Sprites, 或者Sprites, 您需要精细控制顶点位置才能在游戏中实现特殊效果。 请注意, 渲染仍然使用 Phaser的正图相机进行( 在通过 `projectionMesh` 转换后, 请参看 `setPerspective` 、 `setOrtho` 和 `panZ` 方法 ) 。 因此, 所有深度和面部测试都最终在正图空间进行 。

渲染过程会通过这个 Mesh 的面孔进行排列,并渲染出每个被认为在镜头中看到的面孔。没有使用深度缓冲,因此,你应该注意不要使用具有过多顶点的模型数据,或者重叠几何,或者你可能遇到z深度的战斗。 Mesh 的设计是为了允许更先进的2D布局,而不是显示3D对象,尽管它可以达到一定程度.

简言之,如果想要重制 Crysis,请使用3D引擎,而不是Mesh。但是,如果你想在游戏中轻松添加一些小的趣味的3D元素,或者创造一些涉及顶点拼写的特殊效果,这个对象对你是正确的。网格数据成为WebGL批次的一部分,就像标准Sprite一样,所以不会引入额外的遮阳器。因为网格像任何其他Sprite一样,在WebGL批次中产生顶点,所以也可以在网格上使用所有常见的Game Object组件,如定制管道,面具,混合模式或纹理等.

注意, Mesh 天体仅为 WebGL,没有 Canvas 对应的 。

网格起源总是0.5×0.5,不能改变.

## 基本使用 {#basic-usage}

1. 装入纹理

   ```js
   this.load.image(key, url);
   ```

1. 添加网格对象

   ```js
   var mesh = this.add.mesh(x, y, texture, frame);
   ```

   or

   ```js
   var mesh = this.make.mesh({
     x: 0,
     y: 0,
     add: true,

     key: null,
     frame: null,
   });
   ```

1. 设置视角或正交投影

   - 前景预测

     ```js
     mesh.setPerspective(width, height, fov);
     // mesh.setPerspective(width, height, fov, near, far);
     ```

     - `width`, `height`:投影矩阵的宽度/高度,一般与Mesh和/或Render相同.
     - `fov` :视域,以度数表示.
     - `near`, `far` : 视图的近/远值。默认值为 `0.01`/`1000`.

   - 直径投影

     ```js
     mesh.setOrtho(mesh.width / mesh.height, 1);
     // mesh.setOrtho(scaleX, scaleY, near, far);
     ```

     - `scaleX`,`scaleY`:与Mesh/Render维度相关的默认水平/垂直尺度.
     - `near`, `far` : 视图的近/远值。默认值为 `0.01`/`1000`.

1. 创建顶点网格

   ```js
   Phaser.Geom.Mesh.GenerateGridVerts({
     mesh: mesh,
     texture: textureKey,
     frame: frameName,
     width: 1,
     height: 1,
     widthSegments: 1,
     heightSegments: 1,

     // x: 0,
     // y: 0,
     // colors: 0xffffff,
     // alphas: 1,
     // tile: false,
     // isOrtho: false
   });
   ```

   - `mesh`:生成网格的顶点将添加到这个 Mesh 游戏对象中.
   - `texture` :用于此网格的纹理.
   - `frame`:纹理内框的名称或索引.
   - `width`,`height`:以3D单位表示的网格宽度/高度.

     ```js
     {
         // ...
         width: (frameWidth/frameHeight),
         height: (frameHeight/frameHeight)
         // ...
     }

     ```

   - `widthSegments`,`heightSegments`:将网格横向/纵向分割到的区段数.
   - `colors`:一个颜色阵列,每个顶点一个,或者适用于所有顶点的单一颜色值.
   - `alphas` 一组α值,每个顶点一个,或者一个单一的α值适用于所有顶点.
   - `tile` :
     - `false`: 显示为单一纹理。 默认值 。
     - `true`: 横跨网格段的纹理瓦片(重复).

## 型号 {#model}

1. 从 OBJ 文件装入3D 模型

   ```js
   this.load.obj(key, url, objURL, matURL);
   ```

   - `objURL`: 装入obj文件的URL.
   - `matURL`: 装入材料文件的URL.

1. 添加网格对象

   ```js
   var mesh = this.add.mesh(x, y);
   ```

   or

   ```js
   var mesh = this.make.mesh({
     x: 0,
     y: 0,
     add: true,
   });
   ```

1. 添加模型

   ```js
   mesh.addVerticesFromObj(
     key,
     scale,
     x,
     y,
     z,
     rotateX,
     rotateY,
     rotateZ,
     zIsUp
   );
   ```

   - `key`: OBJ缓存中模型数据要添加到这个 Mesh 中的密钥.
   - `scale`: 模型数据缩放的数值。默认为`1`。
   - `x`,`y`,`z`:用这个金额将型号x/y/z位置翻译.
   - `rotateX`,`rotateY`,`rotateZ`:用这个数值旋转x/y/z轴上的模型,以弧度表示.
   - `zIsUp` :
     - `true` : Z轴向上.
     - `false` :Y轴向上.

## 飞机 {#plane}

Plane Game Object 取了 Mesh Game Objects 并扩展其范围, 从而可以快速和轻松地创建 Planes 。 Plane 是一个单侧的单元格网格, 您可以指定每个维度的单元格数量。 Plane 可以是重复( 平面) 的纹理, 或者应用到全 Plane 上 。

然后,Plane可以被3D空间操纵,并跨3轴旋转.

这使得您可以创建无法使用正则 Sprites 的效应, 例如视角扭曲。 您也可以在每顶点的基础上调整顶点。 Plante 数据成为其中的一部分 。 WebGL 批量,就像标准Sprites一样,所以不会引入任何额外的遮蔽层。因为平面板只是产生顶点进入 WebGL 批量,与其他任何Sprite一样,也可以在Plane上使用所有常见的Game Object组件,如自定义管道,掩码,混合模式或纹理.

### 添加平面对象 {#add-plane-object}

```js
var plane = this.add.plane(x, y, key);
// var plane = this.add.plane(x, y, key, frame);
// var plane = this.add.plane(x, y, texture, frame, width, height, tile);
```

- `x`, `y` : 位置
- `key`,`frame`: 纹理键为
- `width`,`height`:本平面宽度/高度,**在单元格**,不像素.
- `tile` :纹理是否铺设?

从 JSON 添加平面

```js
var plane = this.make.plane({
  x: 0,
  y: 0,
  key: "",
  // frame: '',
  // width: 8,
  // height: 8,
  // tile: false,
  // checkerboard: null,
  // checkerboard: { color1, color2, alpha1, alpha2, height }

  // angle: 0,
  // alpha: 1,
  // scale : {
  //    x: 1,
  //    y: 1
  //},
  // origin: {x: 0.5, y: 0.5},

  add: true,
});
```

### 自定义类 {#custom-class}

- 定义类

  ```js
  class MyPlane extends Phaser.GameObjects.Plane {
    constructor(scene, x, y, texture, frame, width, height, tile) {
      super(scene, x, y, texture, frame, width, height, tile);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var plane = new MyPlane(scene, x, y, texture, frame, width, height, tile);
  ```

### 动画 {#animation}

Phaser中的动画可以属于全球动画管理器,也可以具体属于本Plane.

#### 播放动画 {#play-animation}

- 播放此 Plane 上的给定动画 。

  ```js
  plane.play(key);
  // plane.play(key, ignoreIfPlaying);
  ```

  - `key`:动画密钥字符串,或动画配置
    - 动画的字符串密钥
    - 动画配置, 以覆盖默认配置

      ```js
      {
        key,
          frameRate,
          duration,
          delay,
          repeat,
          repeatDelay,
          yoyo,
          showOnStart,
          hideOnComplete,
          startFrame,
          timeScale;
      }
      ```

- 反向播放

  ```js
  plane.playReverse(key);
  // plane.playReverse(key, ignoreIfPlaying);
  ```

  - `key`:动画密钥字符串,或动画配置
- 延迟后播放

  ```js
  plane.playAfterDelay(key, delay);
  ```

  - `key`:动画密钥字符串,或动画配置
- 重复后播放

  ```js
  plane.playAfterRepeat(key, repeatCount);
  ```

  - `key`:动画密钥字符串,或动画配置

#### 停下来 {#stop}

- 立刻停车

  ```js
  plane.stop();
  ```

- 延迟后停止

  ```js
  plane.stopAfterDelay(delay);
  ```

- 停止于边框

  ```js
  plane.stopOnFrame(frame);
  ```

  - `frame`:当前动画中的框架对象.

    ```js
    var currentAnim = plane.anims.currentAnim;
    var frame = currentAnim.getFrameAt(index);
    ```

- 重复后停止

  ```js
  plane.stopAfterRepeat(repeatCount);
  ```

#### 属性 {#properties}

- 已经开始

  ```js
  var hasStarted = plane.anims.hasStarted;
  ```

- 正在玩游戏

  ```js
  var isPlaying = plane.anims.isPlaying;
  ```

- 暂停

  ```js
  var isPaused = plane.anims.isPaused;
  ```

- 框架总数

  ```js
  var frameCount = plane.anims.getTotalFrames();
  ```

- Delay

  ```js
  var delay = plane.anims.delay;
  ```

- Repeat
  - 重复计数总数

    ```js
    var repeatCount = plane.anims.repeat;
    ```

  - 重复计数器

    ```js
    var repeatCount = plane.anims.repeatCounter;
    ```

  - 重复延迟

    ```js
    var repeatDelay = plane.anims.repeatDelay;
    ```

  - Yoyo

    ```js
    var repeatDelay = plane.anims.yoyo;
    ```

- 当前动画密钥

  ```js
  var key = plane.anims.getName();
  ```

  - `key` : 返回( E) `''` 如果没有播放任何动画。
- 当前框架名称

  ```js
  var frameName = plane.anims.getFrameName();
  ```

  - `frameName` : 返回( E) `''` 如果没有播放任何动画。
- 当前动画

  ```js
  var currentAnim = plane.anims.currentAnim;
  ```

- 当前框架

  ```js
  var currentFrame = plane.anims.currentFrame;
  ```

### 交互式 {#interactive}

测试指针是否出现在网格游戏对象的任意面.

```js
plane.setInteractive();
```

### 跳棋游戏 {#checkerboard}

创建基于给定颜色和α值的跳棋样式纹理,并将其应用到此 Plane, 替换它可能拥有的任何当前纹理 。

- Create

  ```js
  plane.createCheckerboard(color1, color2, alpha1, alpha2, height);
  ```

- Remove

  ```js
  plane.removeCheckerboard();
  ```

### 创建遮罩 {#create-mask}

```js
var mask = plane.createBitmapMask();
```

## 自定义网格类 {#custom-mesh-class}

- 定义类

  ```js
  class MyMesh extends Phaser.GameObjects.mesh {
    constructor(
      scene,
      x,
      y,
      texture,
      frame,
      vertices,
      uvs,
      indicies,
      containsZ,
      normals,
      colors,
      alphas
    ) {
      super(
        scene,
        x,
        y,
        texture,
        frame,
        vertices,
        uvs,
        indicies,
        containsZ,
        normals,
        colors,
        alphas
      );
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {
    //     super.preUpdate(time, delta);
    // }
  }
  ```

  - `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
    - 如果游戏对象使它成为了,它会被添加到显示列表中.
    - 如果它有`preUpdate`方法,它将被添加到更新列表中.

- 创建实例

  ```js
  var mesh = new MyMesh(scene, x, y, texture, frame);
  ```

## 控制器 {#control}

### 视图 {#view}

- 将这个 Mesh 在 x/y/z 轴上的视图位置按给定的量翻译。

  ```js
  mesh.panX(x);
  mesh.panY(y);
  mesh.panZ(z);
  ```

### 型号 {#model-1}

- Position

  ```js
  mesh.modelPosition.x = x;
  mesh.modelPosition.y = y;
  mesh.modelPosition.z = z;
  ```

  - `x`, `y`, `z` : 偏移位置。
    - `z+` 时间:
    - `z-` 远
    - `x-` 左侧
    - `x+` : 对
    - `y+` 上层
    - `y-` 下键 :

- Rotation

  ```js
  mesh.modelRotation.x = radiansX;
  mesh.modelRotation.y = radiansY;
  mesh.modelRotation.z = radiansZ;
  ```

  or

  ```js
  mesh.rotateX = degreesX;
  mesh.rotateY = degreesY;
  mesh.rotateZ = degreesZ;
  ```

  - `radiansX`,`radiansY`,`radiansZ`:旋转角度为弧度.
  - `degreesX`,`degreesY`,`degreesZ`:旋转角度以度计.

- Scale

  ```js
  mesh.modelScale.x = scaleX;
  mesh.modelScale.y = scaleY;
  mesh.modelScale.z = scaleZ;
  ```

  - `scaleX`,`scaleY`,`scaleZ`:比例值,`1`是起源大小.

## 面对面 {#backward-facing-faces}

- 隐藏向后面的面孔,默认行为.

  ```js
  mesh.hideCCW = true;
  ```

- 向后显示面孔

  ```js
  mesh.hideCCW = false;
  ```

## 面孔( 面孔) {#faces}

梅舍斯由三角形的面孔组成.

```js
var faces = mesh.faces;
```

### 包含 {#contains}

- 任何有点的面孔

  ```js
  var isHit = mesh.hasFaceAt(worldX, worldY);
  // var isHit = mesh.hasFaceAt(worldX, worldY, camera);
  ```

- 获得面部包含点

  ```js
  var face = mesh.getFaceAt(worldX, worldY);
  // var face = mesh.getFaceAt(worldX, worldY, camera);
  ```

### 属性 {#properties-1}

- Alpha

  - Get

    ```js
    var alpha = face.alpha;
    ```

  - Set

    ```js
    face.alpha = alpha;
    ```

- Angle

  - Rotate

    ```js
    Phaser.Geom.Mesh.RotateFace(face, radians);
    ```

- 中心位置

  - Get

    ```js
    var x = face.x;
    var y = face.y;
    ```

    - `x` : 0(左)~1(右) 键
    - `y`:1(上)~0(下)

  - Set

    ```js
    face.x = x;
    face.y = y;
    ```

    or

    ```js
    face.translate(x, y);
    ```

    - `x` : 0(左)~1(右) 键
    - `y`:1(上)~0(下)

## 维度 {#vertices}

每面各有三顶.

```js
var vertices = mesh.vertices;
```

- `vertices` :顶点阵列.

### 属性 {#properties-2}

- Alpha

  - Get

    ```js
    var alpha = vertex.alpha;
    ```

  - Set

    ```js
    vertex.alpha = alpha;
    ```

- Tint

  - Get

    ```js
    var color = vertex.color;
    ```

  - Set

    ```js
    vertex.color = color;
    ```

#### 更新属性 {#update-properties}

- 开始更新

  ```js
  mesh.ignoreDirtyCache = true;
  ```

- 停止更新

  ```js
  mesh.ignoreDirtyCache = false;
  ```

## 交互式 {#interactive-1}

测试指针是否位于此网格游戏对象的任意一面.

```js
mesh.setInteractive();
```

## 调试 {#debug}

1. 设置调试 [Graphics](/guide/concepts/gameobjects/graphics)

   ```js
   var debugGraphics = this.add.graphics();
   mesh.setDebug(debugGraphics);
   ```

1. 以`this.update()`方法更新[Graphics](/guide/concepts/gameobjects/graphics).

   ```js
   debugGraphics.clear();
   debugGraphics.lineStyle(1, 0x00ff00);
   ```

## 创建遮罩 {#create-mask-1}

```js
var mask = mesh.createBitmapMask();
```

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
