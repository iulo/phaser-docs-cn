# Time.Events {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/event/time-events)

## COMPLETE {#complete}


**说明:** 时间线完成事件.

本次活动在全部活动进行时,按时间表发出。

使用 `Timeline.on('complete', listener)` 的时光网上的视频,即:

```javascript
const timeline = this.add.timeline();
timeline.on('complete', listener);
timeline.play();
```

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| timeline | [Phaser.Time.Timeline](/api/class/time-timeline) | 否 | 引用事件发射时间线 。 |

**所属:** [Phaser.Time.Events](/api/namespace/time-events)
> 源码：[src/time/events/COMPLETE_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/time/events/COMPLETE_EVENT.js#L7)  
引入版本：3.70.0

---
