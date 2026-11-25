# 其他 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/misc)

## 预览活动场景 {#preview-active-scene}

场景编辑器在它内部运行一个 Phaser 场景,这意味着,它向您展示了您正在创建的场景的像素完美图像。 但有时您想要看到场景在动作中, 包括物理,输入,动画。 为此, 有一种技巧: **Preview Scene**( `Ctrl+0`) 命令 。

此命令打开默认( 或配置) 浏览器中的游戏, 但将起始参数添加到 URL 中, 并将当前场景的名称设定为值 。 如果当前场景是预制体场景, 那么它会使用最后一个有效的场景 。

例如,如果您正在编辑 ** Level 完成 ** 场景, 并且运行 **Preview Scene** 命令, 编辑器会启动浏览器并打开 URL :

`http://localhost:<port>/start=LevelCompleted`

现在,在游戏的代码中,您必须读取起始参数的值,然后用同名的开始场景。这是您必须手动编码的东西,但是,内置的PhaserZ编辑器项目模板包含了读取`start`参数的代码。它看起来是这样的:

```javascript
if (process.env.NODE_ENV === "development") {

    const start = new URLSearchParams(location.search).get("start");

    if (start) {

        console.log(`Development: jump to ${start}`);
        this.scene.start(start);
        return;
    }
}
```

`process.env.NODE_ENV === "development"`表达法在编译时被[webpack](https://webpack.js.org)取代,在您正在开发或生产建设时被`true`或`false`取代。

您可以在设置一个一致的游戏状态后,将该代码放置在**预装机**场景或任何其他场景中.

## 数字输入字段 {#numeric-input-field}

您可以以不同方式改变数字输入字段的值:

- 通过在输入字段中写入新值.
- 将鼠标轮子滚过输入字段.
- 通过拖动鼠标到输入字段的标签上 。

在最后两种方法中,值会增加或减少一定的金额,金额取决于与输入字段相关的属性值的域。例如,如果属性为0至1之间的浮点,则值会增加或减少0.01,如果属性为整数,则值会增加或者减少1。

## 场景工具面板 {#scene-tools-panel}

场景底部有一个带有工具快捷键的面板,以及场景的其他功能:

![Scene tools pane](https://cdn.phaser.io/editor-docs/misc-scene-tools-panel-20240917.webp)

从左到右:

- 电话 [align tools](/editor/scene-editor/layout-tools/layout-tools-align).
- 电话 [align to border tools](/editor/scene-editor/layout-tools/layout-tools-align-to-border).
- 电话 [origin tools](/editor/scene-editor/layout-tools/layout-tools-origin).
- 电话 [sorting tools](/editor/scene-editor/layout-tools/layout-tools-sorting).
- 电话 [grid tools](/editor/scene-editor/layout-tools/layout-tools-grid).

其他特殊按钮如下:

### 播放场景更新循环 {#play-scene-update-loop}

Phaser场景中常见的是运行一个循环来更新和渲染场景。 然而, Scene编辑器并不默认运行该循环, 否则它只在用户修改时更新/ 交付场景。 这在大多数情况下都有效, 但有些游戏对象可以实时进行动画, 如Sprite动画、 Particle Emiters、 Spine动画或 Video 对象。 对于这些案例, 您可以点击播放按钮来启动该循环。 此按钮启动场景循环, 使动画得到顺利更新。 您可以再次点击按钮来暂停循环 。

### 场景刷新按钮 {#scene-refresh-button}

刷新按钮再次创建场景。 您可以用它来重置一个复杂的动画到它的第一状态, 就像在粒子发射器中一样 。

### 音频哑弹按钮 {#audio-mute-button}

音频哑巴按钮会变哑场景的所有声音。当您预览电子游戏对象时,它就适用 。

## 转到对话框 {#go-to-dialog}

内 Phaser 编辑器 您创建场景、 预制体文件、 脚本节点、 用户组件、 资源包、 动画... 您日常工作流程中的一个重要部分是浏览这些文件。 ** Go To 对话框** 是帮助您找到和打开项目中任何文件的强大工具。 当您打开此对话框时, 它会显示所有相关文件和定义, 您可以快速搜索您正在寻找的文件。 您可以打开对话框 。 `Ctrl+Alt+O` (`Cmd+Opt+O` 打开 macOS快捷键,或单击主工具栏中的 ** Go To** 按钮。

![Open the Go To dialog](https://cdn.phaser.io/editor-docs/misc-go-to-dialog-open-20240918.webp)

您可以按住 `Shift` 键并滚动鼠标轮子, 以缩放对话框的内容。 您也可以点击对话框的下/ 右角的缩放按钮 。

![Zoom in/out](https://cdn.phaser.io/editor-docs/misc-go-to-dialog-zoom-20240918.webp)

---
