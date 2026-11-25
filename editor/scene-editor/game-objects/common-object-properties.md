# 游戏对象通用属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/common-object-properties)

对象的属性在 [Inspector view](/editor/scene-editor/inspector-view) 中列出和分组。在此视图中,您可以修改选定对象的属性。

在本章中,我们涵盖不同游戏对象常见的属性.

## 可变属性 {#variable-properties}

可变属性由场景编辑器引入,用于大纲视图和[scene compiler](/editor/scene-editor/scene-compiler).

### 名称属性 {#name-property}

此名称是由编辑器生成的自动 :

![Name property in Inspector view.](https://cdn.phaser.io/editor-docs/scene-editor-name-prop-1-202203281224.webp)

它被用作大纲视图中的标签:

![Name property in Outline.](https://cdn.phaser.io/editor-docs/scene-editor-name-prop-2-202203281224.webp)

作为生成代码中的变量名称:

![Name property in code.](https://cdn.phaser.io/editor-docs/scene-editor-name-prop-3-202203281224.webp)

### 显示名称属性 {#display-name-property}

您可以设置  **Display Name ** 属性, 更改大纲视图中游戏对象的默认文本。 此显示名称仅由 UI 使用 。

![Display Name property](https://cdn.phaser.io/editor-docs/scene-editor-variable-display-name-20240109.webp)![Display name in Outline view.](https://cdn.phaser.io/editor-docs/scene-editor-variable-display-name-outline-20240109.webp)

### 游戏对象名称属性 {#game-object-name-property}

**GO 名称** 属性表示是否将上一个** 名称** 属性的价值设定为[Game Object’s name property](/api/class/gameobjects-gameobject#name)的价值。

请检查**GO名称** 属性 :

![Enables setting the Game Object's name property.](https://cdn.phaser.io/editor-docs/scene-editor-go-name-prop-3-202203281224.webp)

用于生成代码中的 `name`值 :

![Set the variable name as the GO name's value.](https://cdn.phaser.io/editor-docs/scene-editor-go-name-code-prop-3-202203281224.webp)

### 类型属性 {#type-property}

此属性显示选中对象的类型。 如果是预制体, 它显示预制体的名称和作为预制体根的 Phaser 类型。 例如: `prefab PlayButton (Image)` 。

另外,还可以点击类型名称来更改选定对象的类型。它打开了 [Replace Type dialog](/editor/scene-editor/game-objects/replace-object-type):

![Replace Type dialog.](https://cdn.phaser.io/editor-docs/scene-editor-variable-type-prop-09182020.webp)

### 范围属性 {#scope-property}

范围属性是指引用对象的变量的词典范围。可能的值是:

* `LOCAL`: 变量是本地到对象创建的。 它是可选的, 如果对象属性被修改, 编译器可以生成或不生成 。
* `METHOD`:该变量在方法的范畴中可以找到。
* `CLASS`:变量被分配到一个私有类域。该对象可以从该类的任何其他方法中访问。
* `PUBLIC`: 类似于`CLASS`范围,但它被一个公共字段引用。该对象可以被该类的任何客户端访问 。
* `NESTED_PREFAB`:类似`PUBLIC`,但对象也可以作为Scen Editor中的[nested prefab](/editor/scene-editor/prefabs/prefab-nested)实例使用,这意味着,您可以使用场景编辑器更改其属性.

默认情况下, 范围被设定为 `LOCAL`。 在以前的版本编辑器中, 默认值是 `METHOD`, 但现在我们正使用 `METHOD`来保证 [scene compiler](/editor/scene-editor/scene-compiler) 为对象生成变量 。

## 描述属性 {#description-property}

您可以用 **Description ** 属性在对象上添加一个描述。 这可用于记录对象在现场的目的。

如果对象是预制体实例,则本节显示[description of the prefab scenes](/editor/scene-editor/scene-properties#scene-display-properties).

![object description section](https://cdn.phaser.games/oss-docs/assets/904aa9075948d1e5-object-description-property-20251124.webp)

## 列出属性 {#lists-properties}

[Lists](#lists-properties) 属性不是 Phaser API 的一部分。 它是 Scene 编辑器用于将对象添加到列表中的属性。 它是对象的“ 父列表 ” 。

正如您在 [Object List](/editor/scene-editor/object-list) 部分所了解的那样,编辑器允许将对象分组到列表中.

属性旁边的按钮显示对象所属列表。 您可以单击按钮以 :

* 将对象添加到另一个列表中。
* 从列表中删除对象。

![Lists property.](https://cdn.phaser.io/editor-docs/scene-editor-lists-prop-04122020.webp)

## 父母属性 {#parent-properties}

父属性显示所选对象的父属性( [Container](/editor/scene-editor/game-objects/container-object), 一种 [Layer](/editor/scene-editor/game-objects/layer-object), 或场景 ) 。

您可以点击按钮将对象移动到新父程序 。

当改变对象的母体时,对象的局部位置会修改,以保持相同的绝对位置.

![image](https://cdn.phaser.io/editor-docs/parent-container-prop-12172020.webp)

另外,您还可以打开[Move To Parent](/editor/scene-editor/working-with-parent-objects#moving-an-object-to-a-parent)命令的这个对话框.

## 子对象属性 {#children-properties}

[containers](/editor/scene-editor/game-objects/container-object)和[layers](/editor/scene-editor/game-objects/layer-object)是与子对象一起的物体,并共享基于子对象的属性。

**子对象** 属性不属于Phaser API,它们只在编辑器设计时使用。

** Allow Picking Children in Scene** 属性允许在现场选择一个孩子。如果该属性被禁用,则无法在现场点击来选择孩子。如果您想要操纵父容器(或层)和作为单个对象的子对象,此选项将有所帮助 。

** 显示大纲中的子对象** 参数相似,可以显示大纲视图中的容器或层层子对象。

![The Children properties.](https://cdn.phaser.io/editor-docs/scene-editor-children-properties-20221004.webp)

** Allow 附加子对象** 参数表示此图层或容器允许在预制体情况下添加新子对象。此参数只有在对象有嵌入预制体范围时才有意义。 [Learn more about adding children to a prefab instance](/editor/scene-editor/prefabs/prefab-instance-children)。

## 变形属性 {#transform-properties}

物体的[transform properties](#transform-properties)可以在督察视图中修改,也可以使用[manipulation tools](/editor/scene-editor/manipulation-tools)修改.

![Transformation properties.](https://cdn.phaser.io/editor-docs/scene-editor-transform-props-04132020.webp)
* 位置的[X](/api/namespace/gameobjects-components-transform#x)和[Y](/api/namespace/gameobjects-components-transform#x),参见[position manipulation tool](/editor/scene-editor/manipulation-tools#translate-tool).
* 电话 [scaleX](/api/namespace/gameobjects-components-transform#scaleX) 财务报告和已审计财务报表 [scaleY](/api/namespace/gameobjects-components-transform#scaleY)。默认值是 `1`。参见 [scale manipulation tool](/editor/scene-editor/manipulation-tools#scale-tool).
* [angle](/api/namespace/gameobjects-components-transform#angle),以度计,默认值为`0`,参见[rotate manipulation tool](/editor/scene-editor/manipulation-tools#rotate-tool).

## 原产地属性 {#origin-properties}

检查者认为对象的[origin properties](/api/namespace/gameobjects-components-origin#setOrigin)可以修改:

![Origin properties.](https://cdn.phaser.io/editor-docs/scene-editor-origin-props-04132020.webp)

有一些命令可以将来源更改为预设值。 这些命令可以在场景上下文菜单中使用, 或者按下键快捷键:

![Origin commands.](https://cdn.phaser.io/editor-docs/scene-editor-origin-context-menu-12182020.webp)

另外,还可以用[origin manipulator tool](/editor/scene-editor/manipulation-tools#origin-tool)或[origin layout tool](/editor/scene-editor/layout-tools/layout-tools-origin)改变物体的起源.

## 大小属性 {#size-properties}

对象的大小属性可以在检查器视图中修改,也可以使用[manipulation tools](/editor/scene-editor/manipulation-tools)修改.

![Size properties.](https://cdn.phaser.io/editor-docs/scene-editor-size-props-20230208.webp)

这些属性,**Width**和**Height**,可供游戏对象使用,如: [TileSprite](/editor/scene-editor/game-objects/tile-sprite-object), [Rectangle](/editor/scene-editor/game-objects/shape-rectangle-object), [Ellipse](/editor/scene-editor/game-objects/shape-ellipse-object),则 [NineSlice](/editor/scene-editor/game-objects/nine-slice-object)还有其他的

除了将值写入属性编辑器之外,您还可以使用 [Resize manipulator tool](/editor/scene-editor/manipulation-tools#resize-tool) (`Z`)用于改变场景中物体的大小.

## 翻转属性 {#flip-properties}

物体的[flipX](/api/namespace/gameobjects-components-flip#flipX)和[flipY](/api/namespace/gameobjects-components-flip#flipY)属性.
 
![Flip properties.](https://cdn.phaser.io/editor-docs/scene-editor-flip-prop-04132020.webp)

## 可见属性 {#visibility-properties}

对象的 [visible](/api/namespace/gameobjects-components-visible#visible) 属性表示对象在现场显示的时间。 它是 Phaser 内置属性。 您可以使用 ** Toggle 可见度** 命令( `V`) 来切换在现场中选定对象的可见度 。

**编辑器中的 redder ** 属性是控制对象是否在现场编辑器中被制成的仅编辑器属性。 它对于隐藏仅在运行时使用的对象, 如产卵点, 触发点等, 很有用。 您可以使用 ** Toggle 编辑器 reder** 命令 (`H`) 来切换此属性, 以及 ** Set All Render ** 命令来启用该属性在现场所有对象中 。

![visible section](https://cdn.phaser.games/oss-docs/assets/333d5d7a8456283a-scene-editor-visible-properties-20251125.webp)

除了参数和命令,大纲视图还显示一个在沟槽中切换对象的**Render**属性的图标:

![render in editor](https://cdn.phaser.games/oss-docs/assets/f0998ed6c2fad781-scene-editor-render-icon-viewer-20251125.webp)

## 阿尔法属性 {#alpha-properties}

这些属性可以设置对象的透明度 。

电话 [alpha](/api/namespace/gameobjects-components-alpha#alpha) 属性设置对象的全球透明。 `alphaTopLeft`, `alphaTopRight`, `alphaBottomLeft` 财务报告和已审计财务报表 `alphaBottomRight` 属性 [Alpha component](/api/namespace/gameobjects-components-alpha) 在对象的角上添加插孔透明。

![Alpha properties.](https://cdn.phaser.io/editor-docs/scene-editor-alpha-props-04132020.webp)

## 阿尔法单属性 {#alpha-single-property}

[alpha](/api/namespace/gameobjects-components-alphasingle#alpha)属性设定了对象的全球透明性.

![Global alpha property.](https://cdn.phaser.io/editor-docs/scene-editor-alpha-single-property-20230208.webp)

## 混合模式属性 {#blend-mode-properties}

[blendMode](https://phaser.io/oss/docs/phaser/blend-mode.md)属性设定游戏对象与后面对象的混合.

## 丁字属性 {#tint-properties}

物体的[tint properties](/api/namespace/gameobjects-components-tint#tintTopLeft)在检查员意见的**Tint**部分中显示:

![Origin properties](https://cdn.phaser.io/editor-docs/scene-editor-origin-props-05242020.webp)

默认情况下, [tint properties](/api/namespace/gameobjects-components-tint#tintTopLeft)的默认值为 `#FFFFFF` 。 要将其重置到默认值, 您可以在文本字段删除它。 您可以写入任何 CSS 有效的颜色格式( `#ff0000` 、 `red` 、 `rgb(255, 0, 0)` ) 。
在代码生成时,值会按照[tint properties](/api/namespace/gameobjects-components-tint#tintTopLeft)的要求转换成整数.

## 纹理属性 {#texture-property}

场景编辑器支持有纹理的几类对象:

* [Image](/editor/scene-editor/game-objects/image-object)
* 精灵
* [Tile Sprite](/editor/scene-editor/game-objects/tile-sprite-object)

场景编辑器提供了一个检查器视图部分,以设定对象的纹理:

![Texture property.](https://cdn.phaser.io/editor-docs/scene-editor-text-prop-02232021.webp)

它显示一个带有[Asset Pack file](/editor/asset-pack-editor/asset-pack-file)图像键的按钮。 如果纹理是从纹理图或图示表中取来的, 那么它也显示该键 。

要改变对象的纹理,请单击按钮,它会打开 ** 选择纹理** 对话框。该对话框显示 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file) 中所有可用的纹理,您可以选择对象的新纹理 。

![Texture dialog.](https://cdn.phaser.io/editor-docs/scene-editor-texture-dialog-02232021.webp)

您可以打开对话框 。 将 Texture ** 命令替换为 。 此命令可以通过按下 `X` 键, 在上下文菜单或 [Command Palette](/editor/workbench/command-palette) 中选择它来执行 。

** 替换纹理帧** (`M`) 是允许您为对象选择不同纹理帧的特殊命令。 这意味着, 它会显示同一图集(或图示表)的所有框架 :

![Select texture's frame.](https://cdn.phaser.io/editor-docs/scene-editor-texture-frame-dialog-02232021.webp)

上下文菜单还显示 ** 选择全部与同一纹理** 命令。 此命令选择所有纹理与选定对象纹理相等的对象。 它可以帮助您用一个场景所有对象的新纹理替换旧纹理 。

![Texture menu.](https://cdn.phaser.io/editor-docs/scene-editor-select-with-same-texture-02232021.webp)

** 资源包编辑器中的显示纹理** 选项打开了定义纹理的“资源包文件”。

## 动画属性 {#animation-properties}

动画属性部分包含Sprite游戏对象[play()](/api/class/gameobjects-sprite#play)方法的参数: 动画主题 :

![Animation properties](https://cdn.phaser.io/editor-docs/scene-editor-animations-props-20240917.webp)

** 动画预览** 参数允许您在场景编辑器中实时播放动画。 它默认是禁用。 当启用时, 它会启动 [scene's update loop](/editor/scene-editor/misc#play-scene-update-loop), 并在场景编辑器中显示动画 :

** Action** 参数表示播放动画的方法:

* **无** (默认):不调用任何方法,也不播放任何动画。
* **游戏**: 呼叫[play()](/api/class/gameobjects-sprite#play)方法。
* **玩过**: 呼叫[playReverse()](/api/class/gameobjects-sprite#playReverse)方法。

![Select the Phaser API method to play the animation.](https://cdn.phaser.io/editor-docs/scene-editor-animations-props-action-param.webp)

**动画键**参数包含要播放的动画键:

![Animation Key parameter.](https://cdn.phaser.io/editor-docs/scene-editor-animations-props-animation-key-param-20231027.webp)

键名旁边有两个按钮。 打开动画键选择对话框的按钮和预览所选动画的按钮 。

动画键选择对话框 :

![A dialog for selecting the animation key.](https://cdn.phaser.io/editor-docs/prefab-user-props-animation-key-dialog-20231027.webp)

动画预览对话框 :

![Animation key preview.](https://cdn.phaser.io/editor-docs/prefab-user-props-animation-key-preview-dialog-20231027.webp)

此对话框搜索动画定义于 a [Phaser animations file](/editor/animations-editor/intro) 或其中 [Aseprite](/editor/scene-editor/sprite-animations#aseprite-animation-support) 列入一项资源 [Asset Pack file](/editor/asset-pack-editor/asset-pack-file).

这是[scene compiler](/editor/scene-editor/scene-compiler)为播放动画而生成的代码:

```javascript
dragon.play("dragon - dragon/Moving Forward");
```

或者,如果你选择了 **PLAY_REVERSE** 动作:

```javascript
dragon.playReverse("dragon - dragon/Moving Forward");
```

当定义 [Animations Editor](/editor/animations-editor/intro) 或 Asesprite 中的动画时, 您会配置重复、 持续时间、 方向等参数... 然而, 在现场, 您可以通过自定义配置到 [play()](/api/class/gameobjects-sprite#play) 方法。 要在 Scen 编辑器中做到这一点, 您必须检查 ** Custom Config ** 参数 。

如果选中了 ** Custom 配置** 参数, 则显示 ** Animation 配置** 部分。 它显示您可以设置到动画的所有参数 :

![Custom configuration.](https://cdn.phaser.io/editor-docs/scene-editor-animations-props-custom-config-20231027.webp)

当设置自定义配置时, [scene compiler](/editor/scene-editor/scene-compiler) 生成此代码:

```javascript
dragon.play({
    "key": "dragon - dragon/Moving Forward"
    "frameRate": 10,
    "repeat": -1
});
```

## 文本属性 {#text-property}

Phaser中有几类对象用于显示文本。目前,Scene Editor支持BitmapText和Text类型。

文本属性可在检查员意见的** 文本内容** 部分编辑。

![Text property.](https://cdn.phaser.io/editor-docs/scene-editor-text-prop-04162020.webp)

---
