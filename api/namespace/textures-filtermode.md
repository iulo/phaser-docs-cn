# Phaser.Textures.FilterMode {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/textures-filtermode)

Scope: 
static
> 源码：[src/textures/const.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/const.js#L7)  
引入版本：3.0.0

## 静态函数 {#static-functions}

### LINEAR {#LINEAR}

#### LINEAR: number {#linear-number}


**说明:**

线性(bilinear)滤波器类型。 缩放时在相邻像素之间插插, 产生混合的、 反异名的结果, 从而平滑纹理。 适合高分辨率的艺术, 但会在像素艺术上显得模糊 。


> 源码：[src/textures/const.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/const.js#L18)  
引入版本：3.0.0


---

### NEAREST {#NEAREST}

#### NEAREST: number {#nearest-number}


**说明:**

最接近的邻居过滤器类型。 在缩放、 保存硬边缘和产生脆性、 块状结果时, 标注最接近的像素。 理想的像素艺术游戏, 纹理尖锐度很重要 。


> 源码：[src/textures/const.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/const.js#L29)  
引入版本：3.0.0


---

---
