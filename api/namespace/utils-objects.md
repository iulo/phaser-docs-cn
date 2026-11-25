# Phaser.Utils.Objects {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/utils-objects)

Scope: 
static
> 源码：[src/utils/object/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/index.js#L7)  


## 静态函数 {#static-functions}

### Clone {#Clone}

#### \<static> Clone(obj) {#static-cloneobj}


**说明:**

浅色对象克隆,不会克隆嵌套对象.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| obj | object | 否 | 克隆对象 。 |


**返回值:** object - 与输入对象具有相同属性的新对象。


> 源码：[src/utils/object/Clone.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/Clone.js#L7)  
引入版本：3.0.0


---

### DeepCopy {#DeepCopy}

#### \<static> DeepCopy(inObject) {#static-deepcopyinobject}


**说明:**

递归深复制给定对象或阵列, 返回带有所有嵌入对象和阵列的全新实例。 原始对象不修改。 如果传递非对象值( 如字符串、 数字、 布尔值或无效值) , 则返回为正值 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| inObject | object | 否 | 要复制的对象或阵列 。 |


**返回值:** object - 原始对象或阵列的深层复制件。


> 源码：[src/utils/object/DeepCopy.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/DeepCopy.js#L7)  
引入版本：3.50.0


---

### Extend {#Extend}

#### \<static> Extend([args]) {#static-extendargs}


**说明:**

将一个或多个源对象的属性合并到目标对象中,返回修改的目标。这是稍作修改的[jQuery.extend](http://api.jquery.com/jQuery.extend/)。

函数接受一个 variadic 参数列表。 如果第一个参数是布尔 `true`, 则执行一个深( 复验) 副本, 第二个参数则作为目标处理。 否则, 第一个参数是目标, 并且所有后续参数都是源对象。 每个源对象的属性会被复制到目标上, 顺序是; 后一个源覆盖了同一键的早期属性。 Nested 平原对象和数组在深副本中被克隆而不是引用, 防止原物的突变。 `undefined` 值永远不会被复制到目标上 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| args | * | 是 | 深复制模式的可选引线布尔,然后是目标对象,然后是一个或多个其属性将合并到目标中的源对象. |


**返回值:** object - 扩展对象 。


> 源码：[src/utils/object/Extend.js#L13](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/Extend.js#L13)  
引入版本：3.0.0


---

### GetAdvancedValue {#GetAdvancedValue}

#### \<static> GetAdvancedValue(source, key, defaultValue) {#static-getadvancedvaluesource-key-defaultvalue}


**说明:**

从对象中获取一个值。 扩展 `GetValue` , 支持动态和随机化的值类型, 使其对配置对象有用, 在那里值可以固定、 程序化, 或者在使用点随机选择( 例如粒子发射配置或组配置) 。

已获取属性的值类型支持如下:

明确价值:

{

    x: 4

}

函数——以属性键作为论据;其返回值用于:

{

    x: function (key) { return 4; }

}

矩阵——从矩阵中随机选择一个元素:

{

    x: [a, b, c, d, e, f]

}

分钟和最大值之间的随机整数( 包括) :

{

    x: { randInt: [min, max] }

}

分钟至最大值之间的随机浮点 :

{

    x: { randFloat: [min, max] }

}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 取回该值的对象 。 |
| key | string | 否 | 从对象中获取的属性名称。如果一个属性被嵌入,则其先前属性的名称应当用点分隔(`.`) - `banner.hideBanner` 返回该值的值 `hideBanner` 中存储对象的属性 `banner` 属性的损益 `source` 对象。 |
| defaultValue | * | 否 | 如果 `key` 在 `source` 对象中找不到, 返回值 。 |


**返回值:** * - 请求的键值 。


> 源码：[src/utils/object/GetAdvancedValue.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/GetAdvancedValue.js#L10)  
引入版本：3.0.0


---

### GetFastValue {#GetFastValue}

#### \<static> GetFastValue(source, key, [defaultValue]) {#static-getfastvaluesource-key-defaultvalue}


**说明:**

从源对象的顶级获取给定的键值。如果源不是对象(即是虚构的,数字的,或字符串),或者如果源上不存在键,则返回defaultValue。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 搜索对象 |
| key | string | 否 | 源属性的键。 必须在源对象的顶端存在( 无周期) |
| defaultValue | * | 是 | 如果键不存在, 则使用默认值 。 |


**返回值:** * - 如果找到值; 否则, defaultValue( 如果未提供则取消)


> 源码：[src/utils/object/GetFastValue.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/GetFastValue.js#L7)  
引入版本：3.0.0


---

### GetMinMaxValue {#GetMinMaxValue}

#### \<static> GetMinMaxValue(source, key, min, max, defaultValue) {#static-getminmaxvaluesource-key-min-max-defaultvalue}


**说明:**

使用给定的键从源对象中获取一个数值,然后将其夹到 `min`和 `max` 定义的包容性范围。如果该属性不存在于源对象上,则使用 `defaultValue` 。通过将键名称与点分隔,可以访问 Nested 属性。返回的值总是在指定的界限内。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 取回该值的对象 。 |
| key | string | 否 | 从对象中获取的属性名称。如果一个属性被嵌入,则其前几个属性的名称应该用点(`.`)来分隔。 |
| min | number | 否 | 可返回的最小值 。 |
| max | number | 否 | 可返回的最大值 。 |
| defaultValue | number | 否 | 如果属性不存在, 返回值会默认为 `min` 。 也受给定的界限限制 。 |


**返回值:** number - `source`对象的夹值.


> 源码：[src/utils/object/GetMinMaxValue.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/GetMinMaxValue.js#L10)  
引入版本：3.0.0


---

### GetValue {#GetValue}

#### \<static> GetValue(source, key, defaultValue, [altSource]) {#static-getvaluesource-key-defaultvalue-altsource}


**说明:**

从对象或替代对象获取一个值,如果找不到,则会降至备份默认值。

键是弦,可以根据周期字符的用法进行分割.

例如:

```javascript
const source = {
  lives: 3,
  render: {
    screen: {
      width: 1024
    }
  }
}

const lives = GetValue(source, 'lives', 1);
const width = GetValue(source, 'render.screen.width', 800);
const height = GetValue(source, 'render.screen.height', 600);
```

上面的代码, `lives` 将3,因为它的定义 在顶级 `source`。该词 `width` 值将为 1024,因为它可以在 `render.screen` 对象。 `height` 值将为 600, 默认值, 因为它从 `render.screen` 对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 试图从中获取值的主对象。 如果在此找不到, 则选中 `altSource` 。 |
| key | string | 否 | 从对象中获取的属性名称。如果一个属性被嵌入,则其先前属性的名称应当用点分隔(`.`) - `banner.hideBanner` 返回该值的值 `hideBanner` 中存储对象的属性 `banner` 属性的损益 `source` 对象。 |
| defaultValue | * | 否 | 如果 `key` 在 `source` 对象中找不到, 返回值 。 |
| altSource | object | 是 | 用于从中获取值的替代对象。 如果属性存在于 `source` 中, 那么 `altSource` 将不使用 。 |


**返回值:** * - 请求的键值 。


> 源码：[src/utils/object/GetValue.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/GetValue.js#L7)  
引入版本：3.0.0


---

### HasAll {#HasAll}

#### \<static> HasAll(source, keys) {#static-hasallsource-keys}


**说明:**

验证一个对象是否包含所有请求的键

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 用于检查键存在的对象 。 |
| keys | Array.\<string> | 否 | 用于确保源对象包含的键数组 。 |


**返回值:** boolean - 如果源对象包含所有键,则`true`,否则则`false`.


> 源码：[src/utils/object/HasAll.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/HasAll.js#L7)  
引入版本：3.0.0


---

### HasAny {#HasAny}

#### \<static> HasAny(source, keys) {#static-hasanysource-keys}


**说明:**

验证对象至少包含一个请求的键

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 用于检查键存在的对象 。 |
| keys | Array.\<string> | 否 | 搜索对象的键数组 。 |


**返回值:** boolean - 如果源对象至少包含一个键,则`true`,否则则`false`.


> 源码：[src/utils/object/HasAny.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/HasAny.js#L7)  
引入版本：3.0.0


---

### HasValue {#HasValue}

#### \<static> HasValue(source, key) {#static-hasvaluesource-key}


**说明:**

确定源对象是否拥有自己的属性和指定的键。 这在内部使用 `hasOwnProperty`, 因此只检查拥有( 非继承) 属性 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 要检查的源对象 。 |
| key | string | 否 | 对象内部要检查的属性 。 |


**返回值:** boolean - 如果提供的`key`存在于`source`物体上,则`true`,否则`false`.


> 源码：[src/utils/object/HasValue.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/HasValue.js#L7)  
引入版本：3.0.0


---

### IsPlainObject {#IsPlainObject}

#### \<static> IsPlainObject(obj) {#static-isplainobjectobj}


**说明:**

这是稍作修改的版本 jQuery.isPlainObject。平面对象是一个物体,其内部[[类]]属性是 `[object Object]`,表示它是通过 `{}`, `new Object()`,或 ,或 , `Object.create(null)`中,例如 DOM 节点、 `window` 对象,自定义类的例不被视为普通对象,并将导致此函数返回 `false`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| obj | object | 否 | 检查对象。 |


**返回值:** boolean - 如果物体是平面的,则使用`true`,否则使用`false`.


> 源码：[src/utils/object/IsPlainObject.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/IsPlainObject.js#L7)  
引入版本：3.0.0


---

### Merge {#Merge}

#### \<static> Merge(obj1, obj2) {#static-mergeobj1-obj2}


**说明:**

执行两个平面对象的浅析合并, 返回一个包含全部属性的全新的对象。 输入对象都不被修改。 当两个对象中都存在相同的键时, obj1 值优先于obj2 值 。

仅此为浅复制。 深嵌嵌套件不会被克隆, 所以请确定只使用此功能于单个嵌套级的物体 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| obj1 | object | 否 | 基对象。 在发生键冲突时, 它的属性优先 。 |
| obj2 | object | 否 | 次要对象。结果中添加了此对象特有的属性。 |


**返回值:** object - 包含obj1和obj2合并属性的新对象.


> 源码：[src/utils/object/Merge.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/Merge.js#L9)  
引入版本：3.0.0


---

### MergeRight {#MergeRight}

#### \<static> MergeRight(obj1, obj2) {#static-mergerightobj1-obj2}


**说明:**

通过克隆 `obj1`来创建新对象,然后使用"右胜"策略将 `obj2` 的值合并到其中.

仅包含在 `obj1` 考虑。对于每个键在 `obj2` 中也存在 `obj1`,从 `obj2` 覆盖克隆值。在 `obj2` 但缺席 `obj1` 完全忽略。这与标准合并不同,在 `obj2` 无法引入新键——它只能覆盖已有的键。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| obj1 | object | 否 | 第一个合并对象 。 |
| obj2 | object | 否 | 第二个要合并的对象。 此对象的键也存在于 `obj1` 中, 将会复制到 `obj1` 。 |


**返回值:** object - 合并对象。 `obj1`和 `obj2` 都没有修改 。


> 源码：[src/utils/object/MergeRight.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/MergeRight.js#L9)  
引入版本：3.0.0


---

### Pick {#Pick}

#### \<static> Pick(object, keys) {#static-pickobject-keys}


**说明:**

返回只包含在所提供对象上发现的 `keys` 的新对象。如果找不到 `keys` ,则返回空对象。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| object | object | 否 | 选择所提供键的对象 。 |
| keys | array | 否 | 从提供的对象获取的一系列属性 。 |


**返回值:** object - 一个只包含在提供对象上发现的 `keys` 的新对象。 如果找不到 `keys` , 则返回空对象 。


> 源码：[src/utils/object/Pick.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/Pick.js#L9)  
引入版本：3.18.0


---

### SetValue {#SetValue}

#### \<static> SetValue(source, key, value) {#static-setvaluesource-key-value}


**说明:**

在对象中设置一个值,允许点标记来控制属性的深度。

例如:

```javascript
var data = {
  world: {
    position: {
      x: 200,
      y: 100
    }
  }
};

SetValue(data, 'world.position.y', 300);

console.log(data.world.position.y); // 300
```

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| source | object | 否 | 设置值的对象 。 |
| key | string | 否 | 对象中的属性名称。 如果一个属性被嵌入, 其前几个属性的名称应该用点( `.`) 分隔 。 |
| value | any | 否 | 如果在源对象中找到, 设置到属性的值 。 |


**返回值:** boolean - 如果属性键有效且值设定,则使用`true`,否则使用`false`.


> 源码：[src/utils/object/SetValue.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/object/SetValue.js#L7)  
引入版本：3.17.0


---

---
