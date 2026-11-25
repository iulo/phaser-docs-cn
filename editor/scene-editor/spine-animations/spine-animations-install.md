# 在游戏中安装 Spine 插件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/spine-animations/spine-animations-install)

[Spine Phaser runtime](https://esotericsoftware.com/spine-phaser)是一个第三方库,默认情况下它不包含在Phaser中.

Phaser编辑器默认提供 [Spine](https://esotericsoftware.com)工具, 您不需要在编辑器中使用 [Spine](https://esotericsoftware.com) 做任何额外的步骤。 然而, 您应该在游戏中安装 [Spine](https://esotericsoftware.com) 插件 。

您可以通过国家防范机制安装:

```bash
npm install @esotericsoftware/spine-phaser
```

或使用游戏中`script`文件的`index.html`标记:

```html
<script src="https://unpkg.com/@esotericsoftware/spine-phaser@4.1.*/dist/iife/spine-phaser.js">
</script>
```

下一步, 将 Spine 场景插件添加到您的 Phaser 游戏配置中 :

```javascript
const config = {
  ...
  plugins: {
      scene: [{
          key: "spine.SpinePlugin",
          plugin: spine.SpinePlugin,
          mapping: "spine"
        }]
    }
  }

new Phaser.Game(config);
```

[Learn more about installing Phaser Spine in your game](https://esotericsoftware.com/spine-phaser#Installation)


## Spine 启动模板 {#spine-starter-template}

然而,安装 [Spine Phaser runtime](https://esotericsoftware.com/spine-phaser)并不复杂, 我们提供一个带有基本配置的启动模板。 如果您要启动一个新项目, 那么我们建议您使用此项目模板 。

可在**Phaser编辑器桌面**模板页面中查阅:

![Spine project template.](https://cdn.phaser.io/editor-docs/spine-animations-project-template-20230928.webp)

---
