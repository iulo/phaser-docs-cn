# Types.Renderer.Snapshot {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-renderer-snapshot)

## SnapshotCallback {#snapshotcallback}

### \<static> SnapshotCallback {#static-snapshotcallback}

**类型**: function

**Member of**: Phaser.Types.Renderer.Snapshot
> 源码：[src/renderer/snapshot/typedefs/SnapshotCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/snapshot/typedefs/SnapshotCallback.js#L1)  
引入版本：3.16.1

---

## SnapshotState {#snapshotstate}

### \<static> SnapshotState {#static-snapshotstate}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](/api/typedef/types-renderer-snapshot#snapshotcallback) | 否 |  | 抓取到快照后调用功能 。 |
| 类型 | string | 是 | "'image/png'" | 图像创建的格式,通常为`image/png`或`image/jpeg`. |
| encoderOptions | number | 是 | 0.92 | 图像质量,介于0到1. 用于图像格式,具有失速压缩,例如`image/jpeg`. |
| x | number | 是 | 0 | 启动快照的x坐标 。 |
| y | number | 是 | 0 | 启动快照的Y坐标 |
| width | number | 是 |  | 截图的宽度 。 |
| height | number | 是 |  | 画面的高度。 |
| getPixel | boolean | 是 | false | 这是一张像素的快照 还是一个区域? |
| isFramebuffer | boolean | 是 | false | 这是从帧缓冲器或画布上抓取的快照吗? |
| bufferWidth | number | 是 |  | 帧缓冲器的宽度,如果是帧缓冲器抓取的话. |
| bufferHeight | number | 是 |  | 帧缓冲器的高度,如果是帧缓冲器抓取. |
| unpremultiplyAlpha | boolean | 是 |  | 是否应该在返回之前将快照进行不重复? WebGL 仅此而已。 |

**类型**: object

**Member of**: Phaser.Types.Renderer.Snapshot
> 源码：[src/renderer/snapshot/typedefs/SnapshotState.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/renderer/snapshot/typedefs/SnapshotState.js#L1)  
引入版本：3.16.1

---

---
