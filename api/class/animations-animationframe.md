# AnimationFrame {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/animations-animationframe)

动画序列中的单帧.

动画Frame 持有一个用于渲染的纹理帧的引用,与序列中上一个和下一个帧的链接,其位置索引,以及回放进度数据。它也可以携带一个可选的每个帧持续时间,它可以覆盖母动画的默认帧速率,并且可以被标记为标记序列中重要时刻的键框架.

动画Frames 由动画类自动创建和管理, 当动画通过动画管理器构建时。 您通常不会直接即时化动画Frame 。

**构造函数**

`new AnimationFrame(textureKey, textureFrame, index, frame, [isKeyFrame])`

**参数**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| textureKey | string | 否 |  | 纹理的键 此动画Frame 使用. |
| textureFrame | string \| number | 否 |  | 本动画Frame使用的纹理内框架的键 。 |
| index | number | 否 |  | 本动画Frame在动画序列中的索引. |
| frame | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 |  | 参照此动画Frame用于渲染的纹理帧 。 |
| isKeyFrame | boolean | 是 | false | 这个框架是动画中的关键框架吗? |

---


**作用域**: static

> 源码：[src/animations/AnimationFrame.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L9)  
引入版本：3.0.0

## 公开成员 {#public-members}

### duration {#duration}

#### duration: number {#duration-number}


**说明:**

动画的这个帧的长度,以ms表示.


> 源码：[src/animations/AnimationFrame.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L120)  
引入版本：3.0.0


---

### frame {#frame}

#### frame: [Phaser.Textures.Frame](/api/class/textures-frame) {#frame-phasertexturesframe}


**说明:**

参照此动画Frame用于渲染的纹理帧 。


> 源码：[src/animations/AnimationFrame.js#L67](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L67)  
引入版本：3.0.0


---

### index {#index}

#### index: number {#index-number}


**说明:**

本动画Frame在动画序列中的索引.


> 源码：[src/animations/AnimationFrame.js#L58](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L58)  
引入版本：3.0.0


---

### isFirst {#isFirst}

#### isFirst: boolean {#isfirst-boolean}


**说明:**

这是动画序列中的第一个框架吗?


> 源码：[src/animations/AnimationFrame.js#L76](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L76)  
引入版本：3.0.0


---

### isKeyFrame {#isKeyFrame}

#### isKeyFrame: boolean {#iskeyframe-boolean}


**说明:**

动画中是否包含此框架为 KeyFrame ?


> 源码：[src/animations/AnimationFrame.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L143)  
引入版本：3.50.0


---

### isLast {#isLast}

#### isLast: boolean {#islast-boolean}


**说明:**

这是动画序列中最后一个框吗?


> 源码：[src/animations/AnimationFrame.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L87)  
引入版本：3.0.0


---

### nextFrame {#nextFrame}

#### nextFrame: [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) {#nextframe-phaseranimationsanimationframe}


**说明:**

动画中这个之后的动画Frame的参考文献,如果有的话.


> 源码：[src/animations/AnimationFrame.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L109)  
引入版本：3.0.0


---

### prevFrame {#prevFrame}

#### prevFrame: [Phaser.Animations.AnimationFrame](/api/class/animations-animationframe) {#prevframe-phaseranimationsanimationframe}


**说明:**

动画中这个动画片之前的动画片的参考文献,如果有的话.


> 源码：[src/animations/AnimationFrame.js#L98](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L98)  
引入版本：3.0.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

动画内部此帧的正常进度, 范围为 0 到 1 , 值为 0 表示动画的开始, 1 表示结束。 此值是在此创建和缓存动画时计算出来的 。


> 源码：[src/animations/AnimationFrame.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L130)  
引入版本：3.0.0


---

### textureFrame {#textureFrame}

#### textureFrame: string, number {#textureframe-string-number}


**说明:**

本动画Frame使用的纹理内框架的键 。


> 源码：[src/animations/AnimationFrame.js#L49](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L49)  
引入版本：3.0.0


---

### textureKey {#textureKey}

#### textureKey: string {#texturekey-string}


**说明:**

纹理的键 此动画Frame 使用.


> 源码：[src/animations/AnimationFrame.js#L40](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L40)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### destroy {#destroy}

#### \<instance> destroy() {#instance-destroy}


**说明:**

删除外部资源的引用, 以此来毁灭此对象。


> 源码：[src/animations/AnimationFrame.js#L171](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L171)  
引入版本：3.0.0


---

### toJSON {#toJSON}

#### \<instance> toJSON() {#instance-tojson}


**说明:**

生成一个适合转换为JSON的JavaScript对象.


**返回值:** [Phaser.Types.Animations.JSONAnimationFrame](/api/typedef/types-animations#jsonanimationframe) - 动画Frame数据.


> 源码：[src/animations/AnimationFrame.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/animations/AnimationFrame.js#L153)  
引入版本：3.0.0


---

---
