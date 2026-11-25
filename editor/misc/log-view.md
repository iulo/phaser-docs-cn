# 日志视图 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/misc/log-view)

编辑器正在积极开发中,作为任何软件,它可能包含bug. 当一个bug被发现时,向开发团队报告它很重要,因此它可以在未来的发行中固定,为此,我们在Workbench中添加了一个新的**Log视图**.

此视图将显示编辑器生成的日志消息, 包括错误消息、 警告和信息信息。 此视图仅在错误或警告被记录时显示, 因此不会干扰编辑器的正常工作流程 。

![log view](https://cdn.phaser.games/oss-docs/assets/892abd36e6f26859-misc-log-view-20251126.webp)

日志视图的要点是:

- **清除** 按钮:清除日志信息。
- **脱硫工具** 按钮:打开编辑器的开发工具。这对高级用户和开发者检查编辑器的内部状态有用,因为编辑器是基于Electron,它基于Chrimium浏览器。
- **过滤器** 区域:允许选择要显示的信息类型:错误、警告和信息。

---
