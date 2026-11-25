# Types.GameObjects.PathFollower {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-pathfollower)

## PathConfig {#pathconfig}

### \<static> PathConfig {#static-pathconfig}


路径跟踪器的设置 。

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| duration | number | 是 | 1000 | 路径持续时间以毫秒计。 必须是 `> 0` 。 |
| from | number | 是 | 0 | 路径的起始位置在0到1之间,必须小于`to`. |
| to | number | 是 | 1 | 路径的端位置在0到1之间,必须超过`from`. |
| positionOnPath | boolean | 是 | false | 是否使用路径偏移将路径跟踪器定位在路径上 。 |
| rotateToPath | boolean | 是 | false | 路径跟踪器是否应该自动旋转以指向路径的方向 ? |
| rotationOffset | number | 是 | 0 | 如果路径跟踪器正在旋转以匹配路径,则该值会被添加到旋转值中。这允许您旋转对象到路径中,但也可以控制旋转角度。 |
| startAt | number | 是 | 0 | 路径的当前起始位置,必须介于`from`和`to`之间. |

**类型**: object

**Member of**: Phaser.Types.GameObjects.PathFollower
> 源码：[src/gameobjects/pathfollower/typedefs/PathConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/pathfollower/typedefs/PathConfig.js#L1)  
引入版本：3.0.0

---

---
