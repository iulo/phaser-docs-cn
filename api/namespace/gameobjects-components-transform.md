# Phaser.GameObjects.Components.Transform {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/gameobjects-components-transform)

Scope: 
static
> 源码：[src/gameobjects/components/Transform.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L17)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### angle {#angle}

#### angle: number {#angle-number}


**说明:**

以度表示的此游戏对象的角度 。

Phaser采用右手顺时针旋转系统,其中0为右转,90为下转,180/-180为左转,-90为上转.

如果你喜欢在弧度工作, 参见`rotation`属性。


> 源码：[src/gameobjects/components/Transform.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L211)  
引入版本：3.0.0


---

### hasTransformComponent {#hasTransformComponent}

#### hasTransformComponent: boolean {#hastransformcomponent-boolean}


**说明:**

显示游戏对象有此组件的属性 。


> 源码：[src/gameobjects/components/Transform.js#L26](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L26)  
引入版本：3.60.0


---

### rotation {#rotation}

#### rotation: number {#rotation-number}


**说明:**

弧度中的此游戏对象角度 。

Phaser使用右手顺时针旋转系统,其中0为右,PI/2为下,+-PI为左,-PI/2为上.

如果你喜欢用学位工作,请参见`angle`属性.


> 源码：[src/gameobjects/components/Transform.js#L238](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L238)  
引入版本：3.0.0


---

### scale {#scale}

#### scale: number {#scale-number}


**说明:**

这是一个特殊的设置器, 允许您同时将游戏对象的横向和纵向尺度设置为相同的值。 当读取此值时, 返回的结果是 `(scaleX + scaleY) / 2` 。

使用此属性意味着您希望水平和垂直的尺度是平等的。 如果不是, 请使用 `scaleX` 或 `scaleY` 属性 。


> 源码：[src/gameobjects/components/Transform.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L113)  
引入版本：3.18.0


---

### scaleX {#scaleX}

#### scaleX: number {#scalex-number}


**说明:**

此游戏对象的横向尺度 。


> 源码：[src/gameobjects/components/Transform.js#L149](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L149)  
引入版本：3.0.0


---

### scaleY {#scaleY}

#### scaleY: number {#scaley-number}


**说明:**

此游戏对象的垂直尺度 。


> 源码：[src/gameobjects/components/Transform.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L180)  
引入版本：3.0.0


---

### w {#w}

#### w: number {#w-number}


**说明:**

此游戏对象的w位置 。


> 源码：[src/gameobjects/components/Transform.js#L103](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L103)  
引入版本：3.0.0


---

### x {#x}

#### x: number {#x-number}


**说明:**

此游戏对象的 x 位置 。


> 源码：[src/gameobjects/components/Transform.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L70)  
引入版本：3.0.0


---

### y {#y}

#### y: number {#y-number}


**说明:**

此游戏对象的y 位置 。


> 源码：[src/gameobjects/components/Transform.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L80)  
引入版本：3.0.0


---

### z {#z}

#### z: number {#z-number}


**说明:**

此游戏对象的z位置 。

注意: Z 位置不控制 2D 游戏对象的渲染顺序,而是使用 [Phaser.GameObjects.Components.Depth#depth](/api/namespace/gameobjects-components-depth#depth) 。


> 源码：[src/gameobjects/components/Transform.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L90)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-1}

### copyPosition {#copyPosition}

#### \<instance> copyPosition(source) {#instance-copypositionsource}


**说明:**

复制一个对象的坐标到此 Game Object 的位置 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) \| [Phaser.Types.Math.Vector3Like](/api/typedef/types-math#vector3like) | [Phaser.Types.Math.Vector4Like](/api/typedef/types-math#vector4like) | 否 | 带有数字“ x”、“ y”、“ z” 或“ w” 属性的对象。 未定义的值不被复制 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L293](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L293)  
引入版本：3.50.0


---

### getLocalPoint {#getLocalPoint}

#### \<instance> getLocalPoint(x, y, [point], [camera]) {#instance-getlocalpointx-y-point-camera}


**说明:**

取给定的 `x` 和 `y` 坐标, 并将其转换为此游戏对象的本地空间, 同时考虑到父和本地的变换, 以及显示源 。

返回的矢量2 包含其属性中的翻译点.

需要提供相机来处理修改的滚动因子。 如果没有指定相机, 它将使用来自此游戏对象所属景色的 `main` 相机 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 翻译的 x 位置 。 |
| y | number | 否 | 翻译的y位置. |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 一个矢量2,或指向对象,以存储结果. |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 是 | 正在测试的相机。 如果不给它, 将会使用场景默认相机 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 译之点.


> 源码：[src/gameobjects/components/Transform.js#L551](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L551)  
引入版本：3.50.0


---

### getLocalTransformMatrix {#getLocalTransformMatrix}

#### \<instance> getLocalTransformMatrix([tempMatrix]) {#instance-getlocaltransformmatrixtempmatrix}


**说明:**

获取此游戏对象的本地变换矩阵 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 包含来自此 Game Object 的值的矩阵 。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 人口变化矩阵.


> 源码：[src/gameobjects/components/Transform.js#L484](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L484)  
引入版本：3.4.0


---

### getParentRotation {#getParentRotation}

#### \<instance> getParentRotation() {#instance-getparentrotation}


**说明:**

获得游戏对象所有母容器的总旋转总和.

返回的值以弧度表示, 如果此游戏对象没有母容器, 则为零 。


**返回值:** number - 这个游戏对象的所有母容器的总旋转量, 以弧度表示。


> 源码：[src/gameobjects/components/Transform.js#L635](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L635)  
引入版本：3.18.0


---

### getWorldPoint {#getWorldPoint}

#### \<instance> getWorldPoint([point], [tempMatrix], [parentMatrix]) {#instance-getworldpointpoint-tempmatrix-parentmatrix}


**说明:**

获得此游戏对象的世界位置, 将任何母容器中的内容计为 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 矢量2,或点状对象,以存储结果. |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 一个临时矩阵来持有游戏对象的值. |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 临时矩阵,用于持有父值 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 此游戏对象的世界位置 。


> 源码：[src/gameobjects/components/Transform.js#L601](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L601)  
引入版本：3.88.0


---

### getWorldTransformMatrix {#getWorldTransformMatrix}

#### \<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix]) {#instance-getworldtransformmatrixtempmatrix-parentmatrix}


**说明:**

获取此游戏对象的世界变换矩阵, 将任何母容器都计为元素 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 包含来自此 Game Object 的值的矩阵 。 |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) | 是 | 计算时持有母值的临时矩阵 。 |


**返回值:** [Phaser.GameObjects.Components.TransformMatrix](/api/class/gameobjects-components-transformmatrix) - 人口变化矩阵.


> 源码：[src/gameobjects/components/Transform.js#L501](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L501)  
引入版本：3.4.0


---

### setAngle {#setAngle}

#### \<instance> setAngle([degrees]) {#instance-setangledegrees}


**说明:**

设置此游戏对象的视角。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| degrees | number | 是 | 0 | 此游戏对象的旋转, 以度计 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L364)  
引入版本：3.0.0


---

### setPosition {#setPosition}

#### \<instance> setPosition([x], [y], [z], [w]) {#instance-setpositionx-y-z-w}


**说明:**

设置此游戏对象的位置。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 此游戏对象的 x 位置 。 |
| y | number | 是 | "x" | 此游戏对象的y位置。 如果不设定, 则会使用 `x` 值 。 |
| z | number | 是 | 0 | 此游戏对象的z位置 。 |
| w | number | 是 | 0 | 此游戏对象的w位置 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L265](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L265)  
引入版本：3.0.0


---

### setRandomPosition {#setRandomPosition}

#### \<instance> setRandomPosition([x], [y], [width], [height]) {#instance-setrandompositionx-y-width-height}


**说明:**

将此游戏对象的位置设置为指定区域范围内的随机位置。

如果没有指定区域,则使用0 x 0 之间的随机位置,取而代之的是游戏宽度 x 高度。

该位置不考虑此游戏对象的大小,也就是说只有源头才保证在区域内.

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 0 | 随机区域左上角的 x 位置 。 |
| y | number | 是 | 0 | 随机区域左上方的y位置。 |
| width | number | 是 |  | 随机区域的宽度 。 |
| height | number | 是 |  | 随机区域高度. |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L313](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L313)  
引入版本：3.8.0


---

### setRotation {#setRotation}

#### \<instance> setRotation([radians]) {#instance-setrotationradians}


**说明:**

设置此游戏对象的旋转。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| radians | number | 是 | 0 | 此游戏对象的旋转, 以弧度表示 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L345](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L345)  
引入版本：3.0.0


---

### setScale {#setScale}

#### \<instance> setScale([x], [y]) {#instance-setscalex-y}


**说明:**

设置游戏对象的大小。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| x | number | 是 | 1 | 此游戏对象的横向尺度 。 |
| y | number | 是 | "x" | 此游戏对象的垂直比例。 如果不设定, 将使用 `x` 值 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L383](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L383)  
引入版本：3.0.0


---

### setW {#setW}

#### \<instance> setW([value]) {#instance-setwvalue}


**说明:**

设置此游戏对象的w位置。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 此游戏对象的w位置 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L465](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L465)  
引入版本：3.0.0


---

### setX {#setX}

#### \<instance> setX([value]) {#instance-setxvalue}


**说明:**

设置此游戏对象的 x 位置。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 此游戏对象的 x 位置 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L405](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L405)  
引入版本：3.0.0


---

### setY {#setY}

#### \<instance> setY([value]) {#instance-setyvalue}


**说明:**

设置此游戏对象的y 位置。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 此游戏对象的y 位置 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L424](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L424)  
引入版本：3.0.0


---

### setZ {#setZ}

#### \<instance> setZ([value]) {#instance-setzvalue}


**说明:**

设置此游戏对象的z位置。

注意: Z 位置不控制 2D 游戏对象的渲染顺序,而是使用 [Phaser.GameObjects.Components.Depth#setDepth](/api/namespace/gameobjects-components-depth#setDepth) 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 是 | 0 | 此游戏对象的z位置 。 |


**返回值:** [Phaser.GameObjects.Components.Transform](/api/namespace/gameobjects-components-transform) - 此游戏对象实例 。


> 源码：[src/gameobjects/components/Transform.js#L443](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/components/Transform.js#L443)  
引入版本：3.0.0


---

---
