# Phaser.Math {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/math)

Scope: 
static
> 源码：[src/math/index.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/index.js#L10)  


## 静态函数 {#static-functions}

- [Euler](/api/class/math-euler)
- [Matrix3](/api/class/math-matrix3)
- [Matrix4](/api/class/math-matrix4)
- [Quaternion](/api/class/math-quaternion)
- [RandomDataGenerator](/api/class/math-randomdatagenerator)
- [Vector2](/api/class/math-vector2)
- [Vector3](/api/class/math-vector3)
- [Vector4](/api/class/math-vector4)
## 静态函数 {#static-functions-1}

- [Angle](/api/namespace/math-angle)
- [Distance](/api/namespace/math-distance)
- [Easing](/api/namespace/math-easing)
- [Fuzzy](/api/namespace/math-fuzzy)
- [Interpolation](/api/namespace/math-interpolation)
- [Pow2](/api/namespace/math-pow2)
- [Snap](/api/namespace/math-snap)
## 静态函数 {#static-functions-2}

### Average {#Average}

#### \<static> Average(values) {#static-averagevalues}


**说明:**

计算给定值的平均值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| values | Array.\<number> | 否 | 值为平均值. |


**返回值:** number - 平均值。


> 源码：[src/math/Average.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Average.js#L7)  
引入版本：3.0.0


---

### Bernstein {#Bernstein}

#### \<static> Bernstein(n, i) {#static-bernsteinn-i}


**说明:**

计算伯恩施泰因基础多诺系数,作为贝塞尔曲线计算中的加权系数。结果为二元系数n / (i! * (n-i)!),它决定了`i`在学位-`n`贝塞尔曲线上的影响力点。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| n | number | 否 | 伯恩斯坦多诺米亚的学位 |
| i | number | 否 | 基础函数的索引. |


**返回值:** number - 伯恩斯坦基准系数: 系数(n)/系数(i)/系数(n-i)。


> 源码：[src/math/Bernstein.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Bernstein.js#L9)  
引入版本：3.0.0


---

### Between {#Between}

#### \<static> Between(min, max) {#static-betweenmin-max}


**说明:**

计算 `min`值和 `max`值之间的随机整数,包含在内.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 最低值。 。 |
| max | number | 否 | 最大值( 最大值 ) 。 |


**返回值:** number - 随机整数.


> 源码：[src/math/Between.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Between.js#L7)  
引入版本：3.0.0


---

### CatmullRom {#CatmullRom}

#### \<static> CatmullRom(t, p0, p1, p2, p3) {#static-catmullromt-p0-p1-p2-p3}


**说明:**

使用0.5的百分位α计算出从给定控制点推导的 Catmull-Rom 值。插值发生在 `p1` 财务报告和已审计财务报表 `p2`,与 `p0` 财务报告和已审计财务报表 `p3` 提供段段每一端的正切上下文。 `t = 0` 结果等于 `p1`; 时间 `t = 1` 结果等于 `p2`.

此函数被Phaser的Speline曲线执行器内部使用,生成通过每个控制点的平滑,连续的曲线.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| t | number | 否 | 插值因子,一般在0到1之间. |
| p0 | number | 否 | 第一个控制点(影响`p1`的切合点). |
| p1 | number | 否 | 第二控制点(插座段的起始). |
| p2 | number | 否 | 第三控制点(插座段的结束). |
| p3 | number | 否 | 第四控制点(影响`p2`的切值). |


**返回值:** number - 插值为`p1`和`p2`之间的Catmull-Rom值.


> 源码：[src/math/CatmullRom.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/CatmullRom.js#L7)  
引入版本：3.0.0


---

### CeilTo {#CeilTo}

#### \<static> CeilTo(value, [place], [base]) {#static-ceiltovalue-place-base}


**说明:**

赛尔斯给一个特定的值 最近的倍数的`base` 升到`place`的功率。

电话 `place` 由适用于下列权利来代表: `base` 。例如,默认基准为 10, a `place` 以 0 舍入到最接近的整数中,a `place` 以1  至最接近的0.1  为单位,a `place` 1 头到10头。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 值为  . |
| place | number | 是 | 0 | 盖之所至. |
| base | number | 是 | 10 | 切入的基数。 十进制默认为十进制 。 |


**返回值:** number - 彩色值。 。


> 源码：[src/math/CeilTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/CeilTo.js#L7)  
引入版本：3.0.0


---

### Clamp {#Clamp}

#### \<static> Clamp(value, min, max) {#static-clampvalue-min-max}


**说明:**

强制在边界内一个值, 把它夹在`min`,`max`的射程上。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 被夹住的值 。 |
| min | number | 否 | 最小界限。 |
| max | number | 否 | 最大界限。 |


**返回值:** number - 夹着的值。


> 源码：[src/math/Clamp.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Clamp.js#L7)  
引入版本：3.0.0


---

### DegToRad {#DegToRad}

#### \<static> DegToRad(degrees) {#static-degtoraddegrees}


**说明:**

从度转换给定角度, 以弧度转换为等角 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| degrees | number | 否 | 角度( 以度计) 转换为弧度 。 |


**返回值:** number - 给定的角度转换成弧度.


> 源码：[src/math/DegToRad.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/DegToRad.js#L9)  
引入版本：3.0.0


---

### Difference {#Difference}

#### \<static> Difference(a, b) {#static-differencea-b}


**说明:**

计算两个给定数字的正差。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | number | 否 | 计算中的第一个数字。 |
| b | number | 否 | 算法中第二数. |


**返回值:** number - 两者的正差 给定的数字。


> 源码：[src/math/Difference.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Difference.js#L7)  
引入版本：3.0.0


---

### Factorial {#Factorial}

#### \<static> Factorial(value) {#static-factorialvalue}


**说明:**

计算一个数值的因数,以表示大于 0 的整数。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 计算因子的正整数 。 |


**返回值:** number - 给定数的因子.


> 源码：[src/math/Factorial.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Factorial.js#L7)  
引入版本：3.0.0


---

### FloatBetween {#FloatBetween}

#### \<static> FloatBetween(min, max) {#static-floatbetweenmin-max}


**说明:**

生成两个给定界限之间的随机浮点数,最小包容性,最大独占性.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| min | number | 否 | 下界为浮,含之. |
| max | number | 否 | 上界为浮,独行. |


**返回值:** number - 任意浮动在给定范围内 。


> 源码：[src/math/FloatBetween.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/FloatBetween.js#L7)  
引入版本：3.0.0


---

### FloorTo {#FloorTo}

#### \<static> FloorTo(value, [place], [base]) {#static-floortovalue-place-base}


**说明:**

与`base`相比,某个地方的楼层,十进制位数为10。

`place`代表的是`base`应用的电源,以获得那个位置.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 价值到地板。 |
| place | number | 是 | 0 | 地上到楼下的地方 |
| base | number | 是 | 10 | 底部到底部。 十进制默认为十进制 。 |


**返回值:** number - 底价 额


> 源码：[src/math/FloorTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/FloorTo.js#L7)  
引入版本：3.0.0


---

### FromPercent {#FromPercent}

#### \<static> FromPercent(percent, min, [max]) {#static-frompercentpercent-min-max}


**说明:**

返回基于 `min` 和 `max` 之间的范围以及给出的百分比的值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| percent | number | 否 | 代表百分比的值,介于0到1之间,在此范围以外的值被夹住。 |
| min | number | 否 | 最低值。 。 |
| max | number | 是 | 最大值( 最大值 ) 。 |


**返回值:** number - 值是`percent`% 在`min`和`max`之间。


> 源码：[src/math/FromPercent.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/FromPercent.js#L9)  
引入版本：3.0.0


---

### GetCentroid {#GetCentroid}

#### \<static> GetCentroid(points, [out]) {#static-getcentroidpoints-out}


**说明:**

获取平面图的中间或几何中心(图中所有点的算术平均位置),非正式地,它是在针尖上切除形状时完全平衡的点。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 否 | 一组像矢量2一样的物体,以获得几何中心。 |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 用于存储输出坐标的矢量2 对象。 如果未给出, 则创建新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 代表给定点几何中心的一个矢量2天体。


> 源码：[src/math/GetCentroid.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/GetCentroid.js#L9)  
引入版本：4.0.0


---

### GetSpeed {#GetSpeed}

#### \<static> GetSpeed(distance, time) {#static-getspeeddistance-time}


**说明:**

计算在特定时间覆盖特定距离所需的速度 。

距离被假定为像素,时间被给出为秒,结果以像素每毫秒返回.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| distance | number | 否 | 旅行的距离,以像素表示. |
| time | number | 否 | 允许的时段 覆盖距离,以秒计。 |


**返回值:** number - 所需速度,以每毫秒像素计.


> 源码：[src/math/GetSpeed.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/GetSpeed.js#L7)  
引入版本：3.0.0


---

### GetVec2Bounds {#GetVec2Bounds}

#### \<static> GetVec2Bounds(points, [out]) {#static-getvec2boundspoints-out}


**说明:**

从数组点计算轴对齐的边框(或abb)。

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| points | Array.\<[Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like)> | 否 | 用于获取 AABB 的矢量2类似对象的阵列 。 |
| out | [Phaser.Geom.Rectangle](/api/class/geom-rectangle) | 是 | 一个用于存储结果的矩形对象。如果不给出,则创建新的矩形实例。 |


**返回值:** [Phaser.Geom.Rectangle](/api/class/geom-rectangle) - 矩形对象,为给定点持有 AABB 值。


> 源码：[src/math/GetVec2Bounds.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/GetVec2Bounds.js#L9)  
引入版本：4.0.0


---

### Hash {#Hash}

#### \<static> Hash(vector, [algorithm]) {#static-hashvector-algorithm}


**说明:**

挂载数字或数字列表.

散列是输入的不可预测的转换,它总是从相同的输入返回相同的输出。它对于以可预测的方式生成随机数据是有用的。

例如,您可以用散列来将物体放置在某个场景周围。由于输入相同,物体总是出现在同一个地方,尽管这些地方是随机的。

此函数以1-4数字作为输入,并从0-1返回一个单数.

免责声明: 此功能旨在高效生成视觉多样性, 并非用于加密。 不要用于安全/ 认证/ 加密目的。 使用一个合适的工具 。

性能说明:一个16ms帧有足够的时间产生数万或数十万个散列值,这取决于系统和其他活动.

您可以从不同的散列算法中选择 。

- 0: TRIG. 这使用正弦函数和点产品来散开输入.

- 1: PCG. 这使用一个穿透的相容发生器来将输入进行散列,

  ,但仅限于整数输入。

- 2: PCG_FLOAT. PCG的这个变体接受浮点输入.

TRIG 是 Phaser 4 噪声对象和亲缘关系中使用的相同算法。 它产生像样的品种, 并且接受任意数字作为输入。 它的精度是32位。 如果大于 32位( 4294967296) , 它的输入值可能会失去区分 。 它的输出值不能超过 1/ 4294967296。 这个算法旨在对图形硬件工作, 因为它缺乏位移能力, 并且不是最先进的 。

PCG 是 Permuted Congrusic 生成器。 有关该理论的更多信息, 请参看 [https://www.pcg-random.org/](https://www.pcg-random.org/) 。 这个算法更现代, 被认为质量更高。 它运行的稍快于TRIG。 它只接受全数( integers) 作为输入, 它的精度为32位, 如果大于32位( 4294967296) , 它的输入值可能会失去区分 。 它的输出值不能超过 1/4294967296 。

PCG_FLOAT 工作与 PCG 相同, 但接受浮点输入。 这个转换过程使其运行速度略慢于 TRIG 。 同样的精度关切也适用 。

如果您的散列值开始集群, 您可能会在安全区域之外使用值, 精确度比特不足。 您可以通过循环路径的采样来将值保持在安全区域。 这就是为什么输入的多个维度是有用的 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vector | number \| Array.\<number> | 否 |  | 散列编号或编号列表 1到4 个数字. |
| algorithm | number | 是 | 0 | 使用的算法. 0是TRIG. 1是PCG. 2是PCG_FLOAT. |


**返回值:** number - - 0 -1的号码


> 源码：[src/math/Hash.js#L11](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Hash.js#L11)  
引入版本：4.0.0


---

### HashCell {#HashCell}

#### \<static> HashCell(vector, [config]) {#static-hashcellvector-config}


**说明:**

将数字或数字列表显示为细胞噪声值 。

散列是输入的不可预测的转换,它总是从相同的输入返回相同的输出。它对于以可预测的方式生成随机数据是有用的。

细胞噪声使用散列来扭曲一个网格,在连续模式中创建独特的“细胞”。虽然结果仍然是随机的,但它是连续的:非常相似的输入输出非常相似(尽管细胞之间可能有一些轻微的不连续)。结果有一个明显的突起模式。这是Game Objects的NoiseCell2D家族所使用的算法,有时它被称为Worley或Voronia噪声。

例如,您可以使用蜂窝噪声来创造一系列跨越程序地形的山脊。每次生成同一个区域,它就会看起来是一样的。

此函数以1-4 数字作为输入,返回一个数字。返回数的范围随着输入数的增加而增加。它是从输入矢量到最近的扭曲单元格中心的距离。在更高的维度中,可能的距离更大。

注意: 如果您在配置参数中指定了维度属性, 请至少确保它们与输入向量相同。 缺少值会损坏结果 。

免责声明: 此功能旨在高效生成视觉多样性, 并非用于加密。 不要用于安全/ 认证/ 加密目的。 使用一个合适的工具 。

性能说明:一个16ms帧有足够的时间产生几百个散列值,这取决于设备与工作量.

关于散列算法的更多信息,请参见[Phaser.Math.Hash](/api/namespace/math#Hash).

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vector | number \| Array.\<number> | 否 | 输入矢量为散列数。 1 至 4 个数字 。 |
| config | [Phaser.Types.Math.HashCellConfig](/api/typedef/types-math#hashcellconfig) | 是 | 噪声细胞场的配置. |


**返回值:** number - 散列细胞噪声值。 范围随着输入维度的增多而增加, 因为它代表了距离最近的扭曲细胞中心。


> 源码：[src/math/HashCell.js#L3](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/HashCell.js#L3)  
引入版本：4.0.0


---

### HashSimplex {#HashSimplex}

#### \<static> HashSimplex(vector, [config]) {#static-hashsimplexvector-config}


**说明:**

将数字或数字列表排列为简单的x噪声值 。

散列是输入的不可预测的转换,它总是从相同的输入返回相同的输出。它对于以可预测的方式生成随机数据是有用的。

输出范围为−1至1.

您可以设置配置对象来控制输出。 您可以添加八进制的细节, 添加一个动荡曲折的曲折, 调整梯度流, 并设置随机性种子 。

Simplex噪声是Perlin噪声的一种演化,两者都是Ken Perlin发明的,是一种梯度噪声的形式,它形成了一个平滑连续的场:非常相似的输入输出非常相似,尽管场本身仍然是随机的.

Simplex噪声通过指定任意的渐变点在网格上,将空间分割成网格细胞(使用最小的三角形状称为simplex),识别输入的网格细胞属于哪个网格,以及该网格的梯度之间的混合.

此版本使用流参数来动画噪声字段。流值会旋转所处的梯度,从而形成周期性移位模式。

此执行会刻意复制 `NoiseSimplex2D` 和 `NoiseSimplex3D` 游戏对象的阴影。 它们的行为类似, 配置对象也非常相似。 HashSimplex 不支持值因子/ add/ power 术语, 因为您可以自己处理输出 。

HashSimprex 也支持一维输入。 这自动添加到2维。

Simplex 性能因八进制和曲速设置而异。您可能根据设备及工作量计算每毫秒一千或多少散列。

注意: 如果您在配置参数中指定了维度属性, 请至少确保它们与输入向量相同。 缺少值会损坏结果 。

免责声明: 此功能旨在高效生成视觉多样性, 并非用于加密。 不要用于安全/ 认证/ 加密目的。 使用一个合适的工具 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vector | number \| Array.\<number> | 否 | 输入矢量为散列数。 1 到 3 个数字 。 |
| config | [Phaser.Types.Math.HashSimplexConfig](/api/typedef/types-math#hashsimplexconfig) | 是 | 噪声场的配置. |


**返回值:** number - 噪声值在 - 1 到 1 之间 。


> 源码：[src/math/HashSimplex.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/HashSimplex.js#L1)  
引入版本：4.0.0


---

### IsEven {#IsEven}

#### \<static> IsEven(value) {#static-isevenvalue}


**说明:**

检查某个值是否为偶数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 用来检查的号码 。 |


**返回值:** boolean - 数数是否均.


> 源码：[src/math/IsEven.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/IsEven.js#L7)  
引入版本：3.0.0


---

### IsEvenStrict {#IsEvenStrict}

#### \<static> IsEvenStrict(value) {#static-isevenstrictvalue}


**说明:**

使用严格的类型检查检查给定的值是否为偶数 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 用来检查的号码 。 |


**返回值:** boolean - 数数是否均.


> 源码：[src/math/IsEvenStrict.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/IsEvenStrict.js#L7)  
引入版本：3.0.0


---

### Linear {#Linear}

#### \<static> Linear(p0, p1, t) {#static-linearp0-p1-t}


**说明:**

在两个值之间进行线性插值,返回该值 `t` 中间的% `p0` 财务报告和已审计财务报表 `p1`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| p0 | number | 否 | 第一义. |
| p1 | number | 否 | 第二义. |
| t | number | 否 | p0和p1之间返回的百分比,为0和1之间的数字。 |


**返回值:** number - p0和p1之间的插值,位于位置t.


> 源码：[src/math/Linear.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Linear.js#L7)  
引入版本：3.0.0


---

### LinearXY {#LinearXY}

#### \<static> LinearXY(vector1, vector2, [t]) {#static-linearxyvector1-vector2-t}


**说明:**

将两个给定的矢量,并在它们之间返回一个新的矢量.

不得修改任何经过的矢量。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vector1 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 |  | 开始的矢量2从中插出. |
| vector2 | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 |  | 终结的矢量2 插到。 |
| t | number | 是 | 0 | 向量1和向量2之间的返回百分比,以0到1之间的数字表示。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 向量1 和向量2 之间的步骤 t% 。


> 源码：[src/math/LinearXY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/LinearXY.js#L7)  
引入版本：3.60.0


---

### MaxAdd {#MaxAdd}

#### \<static> MaxAdd(value, amount, max) {#static-maxaddvalue-amount-max}


**说明:**

将`amount`加到`value`上,将最大结果限制在`max`上.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 增益之值. |
| amount | number | 否 | 拟加之数. |
| max | number | 否 | 返回的最大值 。 |


**返回值:** number - 由此而来的价值.


> 源码：[src/math/MaxAdd.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/MaxAdd.js#L7)  
引入版本：3.0.0


---

### Median {#Median}

#### \<static> Median(values) {#static-medianvalues}


**说明:**

计算给定值的中值。这些值被排序,中间值被返回。如果值数为偶数,则返回两个中间值的平均值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| values | Array.\<number> | 否 | 查找中位数的值 。 |


**返回值:** number - 中值(一说为"中值").


> 源码：[src/math/Median.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Median.js#L7)  
引入版本：3.54.0


---

### MinSub {#MinSub}

#### \<static> MinSub(value, amount, min) {#static-minsubvalue-amount-min}


**说明:**

从`value`中减掉一个`amount`,将最小结果限制在`min`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 要从中减去的值 。 |
| amount | number | 否 | 减之数. |
| min | number | 否 | 最小值返回。 |


**返回值:** number - 由此而来的价值.


> 源码：[src/math/MinSub.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/MinSub.js#L7)  
引入版本：3.0.0


---

### Percent {#Percent}

#### \<static> Percent(value, min, [max], [upperMax]) {#static-percentvalue-min-max-uppermax}


**说明:**

确定百分比 `value` 位于 `min` 财务报告和已审计财务报表 `max`。如果 `max` 默认为 `min + 1`,给出宽度 1 的单位范围,起始于 `min`.

您可以选择指定一个 `upperMax` 值, 即代表100% 的 范围的中点, 之后% 开始再次降至 0 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 确定百分比的值。 |
| min | number | 否 | 最低值。 。 |
| max | number | 是 | 最大值( 最大值 ) 。 |
| upperMax | number | 是 | 代表100%的射程中点. |


**返回值:** number - 数值在0至1之间,代表百分比。


> 源码：[src/math/Percent.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Percent.js#L7)  
引入版本：3.0.0


---

### RadToDeg {#RadToDeg}

#### \<static> RadToDeg(radians) {#static-radtodegradians}


**说明:**

将给定的弧度角度转换为等角度角度.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| radians | number | 否 | 弧度的角度转换成度. |


**返回值:** number - 给定的角度转换为度 。


> 源码：[src/math/RadToDeg.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RadToDeg.js#L9)  
引入版本：3.0.0


---

### RandomXY {#RandomXY}

#### \<static> RandomXY(vector, [scale]) {#static-randomxyvector-scale}


**说明:**

计算随机单位矢量。

计算到 -1 和 1 之间的向量随机值,用于表示方向。

可选接受一个比例值来缩放所产生的矢量 。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vector | [Phaser.Math.Vector2](/api/class/math-vector2) | 否 |  | 用于计算随机值的矢量。 |
| scale | number | 是 | 1 | 随机值的尺度 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 给定的矢量。


> 源码：[src/math/RandomXY.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RandomXY.js#L7)  
引入版本：3.0.0


---

### RandomXYZ {#RandomXYZ}

#### \<static> RandomXYZ(vec3, [radius]) {#static-randomxyzvec3-radius}


**说明:**

计算给定半径球体表面的随机位置矢量。

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vec3 | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 |  | 用于计算随机值的矢量。 |
| radius | number | 是 | 1 | 球体的半径. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 给定的矢量。


> 源码：[src/math/RandomXYZ.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RandomXYZ.js#L7)  
引入版本：3.0.0


---

### RandomXYZW {#RandomXYZW}

#### \<static> RandomXYZW(vec4, [scale]) {#static-randomxyzwvec4-scale}


**说明:**

计算随机四维矢量.

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| vec4 | [Phaser.Math.Vector4](/api/class/math-vector4) | 否 |  | 用于计算随机值的矢量。 |
| scale | number | 是 | 1 | 随机值的尺度 。 |


**返回值:** [Phaser.Math.Vector4](/api/class/math-vector4) - 给定的矢量。


> 源码：[src/math/RandomXYZW.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RandomXYZW.js#L7)  
引入版本：3.0.0


---

### Rotate {#Rotate}

#### \<static> Rotate(point, angle) {#static-rotatepoint-angle}


**说明:**

绕原点(0,0)绕一个特定角度旋转一个定点,反时针方向.

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 所要旋转之点. |
| angle | number | 否 | 旋转角度,以弧度表示,呈逆时针方向. |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 给定点,由给定角度在逆时针方向旋转.


> 源码：[src/math/Rotate.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Rotate.js#L7)  
引入版本：3.0.0


---

### RotateAround {#RotateAround}

#### \<static> RotateAround(point, x, y, angle) {#static-rotatearoundpoint-x-y-angle}


**说明:**

旋转 a `point` 环绕 `x` 财务报告和已审计财务报表 `y` 由给定的 `angle`在同一距离上 , 在同一距离上 。

在极性标记中,这个图将一个点从(r, t)到(r, t + 角度),对应于起源(x, y).

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 所要旋转之点. |
| x | number | 否 | 横向坐标旋转. |
| y | number | 否 | 垂直坐标旋转。 |
| angle | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 给定的点。


> 源码：[src/math/RotateAround.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RotateAround.js#L7)  
引入版本：3.0.0


---

### RotateAroundDistance {#RotateAroundDistance}

#### \<static> RotateAroundDistance(point, x, y, angle, distance) {#static-rotatearounddistancepoint-x-y-angle-distance}


**说明:**

旋转 a `point` 环绕 `x` 财务报告和已审计财务报表 `y` 由给定的 `angle` 财务报告和已审计财务报表 `distance`.

在极性标记中,这个图将一个点从(r, t)到(距离, t + 角度),对应于起源(x, y).

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 所要旋转之点. |
| x | number | 否 | 横向坐标旋转. |
| y | number | 否 | 垂直坐标旋转。 |
| angle | number | 否 | 弧度旋转的角度. |
| distance | number | 否 | 距离(x,y)将点放在位置. |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 给定的点。


> 源码：[src/math/RotateAroundDistance.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RotateAroundDistance.js#L7)  
引入版本：3.0.0


---

### RotateTo {#RotateTo}

#### \<static> RotateTo(point, x, y, angle, distance) {#static-rotatetopoint-x-y-angle-distance}


**说明:**

立场a `point` 给定的 `angle` 财务报告和已审计财务报表 `distance` 改为(a)`x`, `y`).

**标签:**

 - generic

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| point | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 否 | 位置的点。 |
| x | number | 否 | 水平坐标从位置。 |
| y | number | 否 | 垂直坐标从位置。 |
| angle | number | 否 | 弧度旋转的角度. |
| distance | number | 否 | 距离(x,y)将点放在位置. |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 给定的点。


> 源码：[src/math/RotateTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RotateTo.js#L7)  
引入版本：3.24.0


---

### RotateVec3 {#RotateVec3}

#### \<static> RotateVec3(vec, axis, radians) {#static-rotatevec3vec-axis-radians}


**说明:**

以轴角旋转一个矢量。

这与轴角四角线变换一个点相同,但精度更高.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vec | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 向量要旋转 。 |
| axis | [Phaser.Math.Vector3](/api/class/math-vector3) | 否 | 轴以旋转. |
| radians | number | 否 | 弧度旋转的角度. |


**返回值:** [Phaser.Math.Vector3](/api/class/math-vector3) - 给定的向量.


> 源码：[src/math/RotateVec3.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RotateVec3.js#L15)  
引入版本：3.0.0


---

### RoundAwayFromZero {#RoundAwayFromZero}

#### \<static> RoundAwayFromZero(value) {#static-roundawayfromzerovalue}


**说明:**

绕一个给定的数字,使它离零更远。也就是说,正数被四舍五入,负数被四舍五入。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 数至圆. |


**返回值:** number - 圆数,从零舍去.


> 源码：[src/math/RoundAwayFromZero.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RoundAwayFromZero.js#L7)  
引入版本：3.0.0


---

### RoundTo {#RoundTo}

#### \<static> RoundTo(value, [place], [base]) {#static-roundtovalue-place-base}


**说明:**

圆向给定精度的值 。

例如:

```javascript
RoundTo(123.456, 0) = 123
RoundTo(123.456, 1) = 120
RoundTo(123.456, 2) = 100
```

以负的 `place` 键绕小数,即圆至精度:

```javascript
RoundTo(123.456789, 0) = 123
RoundTo(123.456789, -1) = 123.5
RoundTo(123.456789, -2) = 123.46
RoundTo(123.456789, -3) = 123.457
```

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| value | number | 否 |  | 值为圆. |
| place | number | 是 | 0 | 圆形位置 圆形单位 负形单位 圆形单位 圆形单位 圆形单位 圆形单位 圆形单位 圆形单位 |
| base | number | 是 | 10 | 圆形的底部。 十进制默认为十进制 。 |


**返回值:** number - 圆数.


> 源码：[src/math/RoundTo.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/RoundTo.js#L7)  
引入版本：3.0.0


---

### SmootherStep {#SmootherStep}

#### \<static> SmootherStep(x, min, max) {#static-smootherstepx-min-max}


**说明:**

计算比较平滑的插值百分比 `x` 介于 `min` 财务报告和已审计财务报表 `max`.

函数接收到编号`x`作为参数,如果`x`小于或等于左边缘,如果`x`大于或等于右边缘,则返回0,如果使用一个赫米特多诺米法,则返回1,否则返回0。

产生比[Phaser.Math.SmoothStep](/api/namespace/math#SmoothStep)更平滑的插值.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 输入值. |
| min | number | 否 | 最小值,又称"左边",假定比"右边"小. |
| max | number | 否 | 最大值,又称"右边缘",假定值大于"左边缘". |


**返回值:** number - 插值的百分比,在0到1之间.


> 源码：[src/math/SmootherStep.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/SmootherStep.js#L7)  
引入版本：3.0.0


---

### SmoothStep {#SmoothStep}

#### \<static> SmoothStep(x, min, max) {#static-smoothstepx-min-max}


**说明:**

计算平滑插值百分比 `x` 介于 `min` 财务报告和已审计财务报表 `max`.

函数接收到编号`x`作为参数,如果`x`小于或等于左边缘,如果`x`大于或等于右边缘,则返回0,如果使用一个赫米特多诺米法,则返回1,否则返回0。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 输入值. |
| min | number | 否 | 最小值,又称"左边",假定比"右边"小. |
| max | number | 否 | 最大值,又称"右边缘",假定值大于"左边缘". |


**返回值:** number - 插值的百分比,在0到1之间.


> 源码：[src/math/SmoothStep.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/SmoothStep.js#L7)  
引入版本：3.0.0


---

### ToXY {#ToXY}

#### \<static> ToXY(index, width, height, [out]) {#static-toxyindex-width-height-out}


**说明:**

返回一个矢量2,其中包含给定索引在 a 中的 x 和 y 位置 `width` ưμ㼯A `height` 大小网格.

例如,在6×4格子中,指数16等于x:4y:2.

如果给定的索引超出范围,则返回一个带有x和y设置为0的矢量2。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| index | number | 否 | 网格内的位置以获取 x/y 值 。 |
| width | number | 否 | 网格的宽度. |
| height | number | 否 | 网格的高度. |
| out | [Phaser.Math.Vector2](/api/class/math-vector2) | 是 | 保存结果的可选矢量2。 如果不给出, 将会创建一个新的矢量2 实例 。 |


**返回值:** [Phaser.Math.Vector2](/api/class/math-vector2) - 包含从给定索引中衍生出来的x和y网格坐标的矢量2。


> 源码：[src/math/ToXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/ToXY.js#L9)  
引入版本：3.19.0


---

### TransformXY {#TransformXY}

#### \<static> TransformXY(x, y, positionX, positionY, rotation, scaleX, scaleY, [output]) {#static-transformxyx-y-positionx-positiony-rotation-scalex-scaley-output}


**说明:**

取`x`和`y`坐标并将其转换为指定位置、旋转和比例值定义的局部坐标空间。这进行反向转换,将一个点从世界空间转换成游戏对象或其他变形实体的等效局部空间坐标。当您需要确定一个世界空间点位于变形对象局部坐标系统之内时,这可用于命中测试或指针输入。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 将转换的x坐标 。 |
| y | number | 否 | 调和Y要转换。 |
| positionX | number | 否 | 变点的水平位置 。 |
| positionY | number | 否 | 变点的垂直位置 。 |
| rotation | number | 否 | 变点旋转,以弧度表示. |
| scaleX | number | 否 | 变位点的横向尺度 。 |
| scaleY | number | 否 | 变点的垂直尺度。 |
| output | [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) | 是 | 翻译坐标的输出矢量、点或对象。 |


**返回值:** [Phaser.Types.Math.Vector2Like](/api/typedef/types-math#vector2like) - 译之点.


> 源码：[src/math/TransformXY.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/TransformXY.js#L9)  
引入版本：3.0.0


---

### Within {#Within}

#### \<static> Within(a, b, tolerance) {#static-withina-b-tolerance}


**说明:**

检查这两个值是否在对方给定的 `tolerance` 内 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| a | number | 否 | 计算中使用的第一个值。 |
| b | number | 否 | 计算中使用的第二个值。 |
| tolerance | number | 否 | 耐受性:任何等于或小于这一数值的,均视为在幅度之内。 |


**返回值:** boolean - 如果`a`和`b`的绝对差小于或等于`tolerance`,则返回`true`.


> 源码：[src/math/Within.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Within.js#L7)  
引入版本：3.0.0


---

### Wrap {#Wrap}

#### \<static> Wrap(value, min, max) {#static-wrapvalue-min-max}


**说明:**

包起来给定 `value` 介于 `min` (包括)和 `max` (排他性).

当值超过`max`时,它会绕回`min`,当值低于`min`时,它就会绕到`max`以下。 这对通过一个范围循环有用,如将一个角度保持在0-360度以内,或者在砖块内循环一个瓦片索引。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| value | number | 否 | 包装值 。 |
| min | number | 否 | 最小范围(包括). |
| max | number | 否 | 范围的最大约束(排他性). |


**返回值:** number - 包裹值,保证在`[min, max)`内.


> 源码：[src/math/Wrap.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/Wrap.js#L7)  
引入版本：3.0.0


---

## 静态函数 {#static-functions-3}

### DEG_TO_RAD {#DEG_TO_RAD}

#### DEG_TO_RAD: number {#deg_to_rad-number}


**说明:**

度到弧度的换算系数(PI / 180). 乘以此常数的度值,以获得其等值的弧度值.


> 源码：[src/math/const.js#L36](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/const.js#L36)  
引入版本：3.0.0


---

### EPSILON {#EPSILON}

#### EPSILON: number {#epsilon-number}


**说明:**

用于浮点比较和近零检查的小型epsilon值(1.0e-6),以避免精度错误.


> 源码：[src/math/const.js#L27](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/const.js#L27)  
引入版本：3.0.0


---

### MAX_SAFE_INTEGER {#MAX_SAFE_INTEGER}

#### MAX_SAFE_INTEGER: number {#max_safe_integer-number}


**说明:**

浏览器支持的最大安全整数。 我们使用一个 const 来进行与旧浏览器的反向兼容 。


> 源码：[src/math/const.js#L74](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/const.js#L74)  
引入版本：3.21.0


---

### MIN_SAFE_INTEGER {#MIN_SAFE_INTEGER}

#### MIN_SAFE_INTEGER: number {#min_safe_integer-number}


**说明:**

此浏览器支持的最低安全整数。 我们使用一个 const 来进行与旧浏览器的反向兼容 。


> 源码：[src/math/const.js#L64](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/const.js#L64)  
引入版本：3.21.0


---

### PI_OVER_2 {#PI_OVER_2}

#### PI_OVER_2: number {#pi_over_2-number}


**说明:**

PI / 2 或 90 度的值,以弧度表示.


> 源码：[src/math/const.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/const.js#L18)  
引入版本：3.0.0


---

### RAD_TO_DEG {#RAD_TO_DEG}

#### RAD_TO_DEG: number {#rad_to_deg-number}


**说明:**

弧度转换系数为度(180 / PI),用这个常数乘以一个弧度值以获得等值的度.


> 源码：[src/math/const.js#L45](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/const.js#L45)  
引入版本：3.0.0


---

### RND {#RND}

#### RND: [Phaser.Math.RandomDataGenerator](/api/class/math-randomdatagenerator) {#rnd-phasermathrandomdatagenerator}


**说明:**

随机数生成器的示例。 游戏靴子才会设置此选项 。


> 源码：[src/math/const.js#L54](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/const.js#L54)  
引入版本：3.0.0


---

### TAU {#TAU}

#### TAU: number {#tau-number}


**说明:**

PI * 2的值代表弧度的全圆(360度).


> 源码：[src/math/const.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/math/const.js#L9)  
引入版本：4.0.0


---

---
