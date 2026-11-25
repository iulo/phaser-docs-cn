# Textures {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/constant/textures)

### CLAMP_TO_EDGE {#CLAMP_TO_EDGE}

#### CLAMP_TO_EDGE: number {#clamp_to_edge-number}


**说明:**

粘贴到边缘包模式. 位于[0, 1] 范围的紫外线坐标被夹在纹理最近的边缘上,这样可以将边缘像素向外伸展而不是重复纹理,是Phaser中大多数纹理的默认包模式.


> 源码：[src/textures/const-wrap.js#L20](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/const-wrap.js#L20)  
引入版本：4.0.0


### REPEAT {#REPEAT}

#### REPEAT: number {#repeat-number}


**说明:**

重复包模式。 当紫外线坐标超过[ 0, 1] 范围时, 纹理瓦片在双向无缝状态下。 用于重复背景图案或平面。 请注意, 纹理维度必须是两个功率, 才能在 WebGL 中正确工作 。


> 源码：[src/textures/const-wrap.js#L33](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/const-wrap.js#L33)  
引入版本：4.0.0


### MIRRORED_REPEAT {#MIRRORED_REPEAT}

#### MIRRORED_REPEAT: number {#mirrored_repeat-number}


**说明:**

镜像的重复包装模式。 类似于 `REPEAT`, 但每次重复时纹理都会被翻转( mirrored) 。 例如, 横跨 UV 0– 1 的纹理会从 1– 2 、 正常 2– 3 等处出现镜像。 这样可以通过消除瓦片边界的可见缝来产生更光滑的纹理。


> 源码：[src/textures/const-wrap.js#L46](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/const-wrap.js#L46)  
引入版本：4.0.0


### LINEAR {#LINEAR}

#### LINEAR: number {#linear-number}


**说明:**

线性(bilinear)滤波器类型。 缩放时在相邻像素之间插插, 产生混合的、 反异名的结果, 从而平滑纹理。 适合高分辨率的艺术, 但会在像素艺术上显得模糊 。


> 源码：[src/textures/const.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/const.js#L18)  
引入版本：3.0.0


### NEAREST {#NEAREST}

#### NEAREST: number {#nearest-number}


**说明:**

最接近的邻居过滤器类型。 在缩放、 保存硬边缘和产生脆性、 块状结果时, 标注最接近的像素。 理想的像素艺术游戏, 纹理尖锐度很重要 。


> 源码：[src/textures/const.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/const.js#L29)  
引入版本：3.0.0


### LINEAR {#LINEAR-1}

#### LINEAR: number {#linear-number-1}


**说明:**

线性滤波器类型 。


> 源码：[src/textures/index.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/index.js#L15)  
引入版本：3.0.0


### NEAREST {#NEAREST-1}

#### NEAREST: number {#nearest-number-1}


**说明:**

最接近的过滤器类型。


> 源码：[src/textures/index.js#L24](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/index.js#L24)  
引入版本：3.0.0

---
