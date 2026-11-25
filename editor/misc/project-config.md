# 项目配置 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/misc/project-config)

任何文件夹都是有效的 Phaser编辑器项目。 然而, 创建 `phasereditor2d.config.json` 项目配置文件是方便的, 它是项目文件夹的根 。

每个Phaser编辑器的项目模板都包含这个文件,所以你可能不必自己创建它.

这些是项目配置支持的设置 :

| 名称      | 数值                                                                                              |
|-----------|----------------------------------------------------------------------------------------------------|
| `skip`    | 带有[filtering the project resources](/editor/misc/resources-filtering)图案的阵列.        |
| `plugins` | 带有[user plugins](/editor/misc/plugins)路径的阵列.                                            |
| `flags`   | 带[server options](/editor/misc/server-options)的阵列.                                           |
| `playUrl` | 当您执行 Play 命令( `F12` 或 `F10`) 时, 可以在浏览器中打开地址的字符串 。 |
| `settings` | 和[UI settings parameters](/editor/workbench/settings)一起的物体.

举例来说:

```bash
{
    "skip": ["dist/", "editor-plugins/"],
    "settings": {
        "phasereditor2d.scene.enablePixelArt": true
    },
    "plugins":
        [
            "editor-plugins/my-fonts-plugins",
            "editor-plugins/my-awesome-plugins"
        ],
    "flags": ["-port", "7171"],
    "playUrl": "http://localhost:4200"
}
```

---
