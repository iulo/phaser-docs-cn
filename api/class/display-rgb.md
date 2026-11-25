# RGB {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/display-rgb)

RGB类拥有一个单一的颜色值,表示为正态的红色,绿色,蓝色的组件,每个组件在0到1之间,内部被WebGL管道和其他需要高效跟踪颜色状态的Phaser系统使用. 任何组件的更改自动设置`dirty`旗并引用一个可选的`onChangeCallback`,使得无需人工投票即可直接对颜色突变作出反应.

**构造函数**

`new RGB([red], [green], [blue])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| red | number | 是 | 0 | 红色值,数字在 0 到 1 之间 。 |
| green | number | 是 | 0 | 绿色的颜色值,数字在0到1之间. |
| blue | number | 是 | 0 | 蓝色的颜色值,数字在 0 到 1 之间 。 |

---


**作用域**: static

> 源码：[src/display/RGB.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L10)  
引入版本：3.50.0

## 公开成员 {#public-members}

### b {#b}

#### b: number {#b-number}


**说明:**

蓝色的颜色值,在0到1之间.

更改此属性将标记此 RGB 对象为脏, 如果设置的话, 并引用 `onChangeCallback` 。


> 源码：[src/display/RGB.js#L180](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L180)  
引入版本：3.50.0


---

### dirty {#dirty}

#### dirty: boolean {#dirty-boolean}


**说明:**

颜色脏吗?


> 源码：[src/display/RGB.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L55)  
引入版本：3.50.0


---

### g {#g}

#### g: number {#g-number}


**说明:**

绿色的颜色值,在 0 到 1 之间 。

更改此属性将标记此 RGB 对象为脏, 如果设置的话, 并引用 `onChangeCallback` 。


> 源码：[src/display/RGB.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L155)  
引入版本：3.50.0


---

### onChangeCallback {#onChangeCallback}

#### onChangeCallback: function {#onchangecallback-function}


**说明:**

每次RGB的颜色值改变时都会引用这个调用.

回调收到红,绿,蓝三个单独的数值参数,每个值在0到1之间.


> 源码：[src/display/RGB.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L43)  
引入版本：3.50.0


---

### r {#r}

#### r: number {#r-number}


**说明:**

红色值,在0到1之间。

更改此属性将标记此 RGB 对象为脏, 如果设置的话, 并引用 `onChangeCallback` 。


> 源码：[src/display/RGB.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L130)  
引入版本：3.50.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

取消 `onChangeCallback` 引用, 释放此对象所持有的任何外部听器, 以此来破坏 RGB 实例 。


> 源码：[src/display/RGB.js#L205](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L205)  
引入版本：3.50.0


---

### equals {#equals}

#### \<instance> equals(red, green, blue) {#instance-equalsred-green-blue}


**说明:**

将给定的rgb参数与该对象中的参数进行比较,如果值相等,则返回布尔的 `true`值,否则它返回 `false`值。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| red | number | 否 | 与此对象进行比较的红色值 。 |
| green | number | 否 | 与此对象比较的绿色值 。 |
| blue | number | 否 | 与此对象比较的蓝色值 。 |


**返回值:** boolean - 如果给定的值与此对象中的值相符,则`true`,否则则`false`.


> 源码：[src/display/RGB.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L93)  
引入版本：3.50.0


---

### onChange {#onChange}

#### \<instance> onChange() {#instance-onchange}


**说明:**

更改处理器的内置。 设置此对象为脏, 然后引用 `onChangeCallback`, 如果设置的话, 将传递到新的 RGB 值中 。


> 源码：[src/display/RGB.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L113)  
引入版本：3.50.0


---

### set {#set}

#### \<instance> set([red], [green], [blue]) {#instance-setred-green-blue}


**说明:**

设置此 RGB 对象的红色、 绿色和蓝色值, 标记为脏, 然后引用 `onChangeCallback`, 如果设定 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| red | number | 是 | 0 | 红色值,数字在 0 到 1 之间 。 |
| green | number | 是 | 0 | 绿色的颜色值,数字在0到1之间. |
| blue | number | 是 | 0 | 蓝色的颜色值,数字在 0 到 1 之间 。 |


**返回值:** [Phaser.Display.RGB](/api/class/display-rgb) - 这个RGB的例子。


> 源码：[src/display/RGB.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/display/RGB.js#L67)  
引入版本：3.50.0


---

---
