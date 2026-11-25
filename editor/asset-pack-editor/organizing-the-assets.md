# 组织资源包文件 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/asset-pack-editor/organizing-the-assets)

您可以将一个“ 资源包” 文件放在任何文件夹中, 但是, 我们建议将这些文件夹放在专门用于游戏资源的文件夹中, 例如: `assets/pack.json` 。

通常需要多个[Asset Pack file](/editor/asset-pack-editor/asset-pack-file):至少一个用于预装机场景,另一个用于游戏场景的其余部分.

有时,您需要使用场景编辑器中的“帮助”资源,这些资源是您在场景编辑器中作为参考使用,但并不包括在游戏中。您可以将所有这些资源与自己的资源包文件合并到单独的文件夹中,并将文件夹排除在游戏构建之外。

这也许是你项目的结构:

```bash
assets/
   preload/
     preload-pack.json
     ... # preloader assets
   levels/
     levels-pack.json
     ... # level assets
   helpers/
     helper-pack.json
     ... # helper assets
```

电话 [Asset Pack Editor](/editor/asset-pack-editor/intro) 搜索文件夹内包含以下内容的文件 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file),如果项目的结构安排得当,则可以提高项目的效率。

[Learn how to add entries to an Asset Pack file](/editor/asset-pack-editor/add-file)

## 类似皮肤的资源 {#skin-like-assets}

如果您的游戏有不同皮肤的字符或对象, 您可以将资源组织起来, 使其易于在皮肤之间切换。 例如, 您可以为每个皮肤创建文件夹, 并将资源放置在其中。 然后, 您可以为每个皮肤创建一个资源包文件。 在 QSet Pack 设置中, 您可以将一个资源包打开可见或看不见, 这样您可以通过启用或失效资源包文件来在皮肤之间切换 。 ** 资源包可见** 参数仅适用于编辑器工具, 因为游戏中您仍然可以装入所有皮肤( asset pack 文件) 。 “ 可见” 属性只是让编辑器中过滤器资源的一种诡计 :

![Asset pack visible](https://cdn.phaser.games/oss-docs/assets/bb85c7280253b541-asset-pack-visible-parameter-20241216.webp)

** 套装包设置** 在检查器视图中显示,当资源包编辑器中未选择对象时。

---
