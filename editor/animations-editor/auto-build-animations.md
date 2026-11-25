# 自动创建动画 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/animations-editor/auto-build-animations)

动画编辑器最强大的特点是动画的自动创作.

这是一个过程,通过选择所有动画所需的所有帧,让我们能够创建多个动画.

事情就是这样的:

* 在块视图中选择几个框架。 如果您选择了纹理图或图示表, 其所有框架也将被考虑。
  
  ![Auto build animations.](https://cdn.phaser.io/editor-docs/animations-auto-build-1.webp)

* 检查器视图中的 ** Auto Build Animation ** 部分显示可以创建的动画列表。按 **Build 动画** 按钮。
  
  ![Auto build animations.](https://cdn.phaser.io/editor-docs/animations-auto-build-2.webp)

或者,您可以拖动帧并将其丢入编辑器中.

* 它显示一个对话框, 请求在生成的动画中添加一个前缀, 这是可选的, 用于混淆。 例如, 如果添加的动画有 ** run **, ** walk **, ** jump ** , 您可以添加一个前缀, 如 ** player - ** 或 ** enemy - **, 因此动画中会包含 ** player - run**, ** player -walk **, ** ** player -jump ** 。
  
  ![Auto build animations.](https://cdn.phaser.io/editor-docs/animations-auto-build-3.webp)

* 所有动画都将用相同的参数(**frameRate**,**repeat**等)来创作,但您可以在督察视图中更改.
  
  ![Auto build animations.](https://cdn.phaser.io/editor-docs/animations-auto-build-4.webp)

用一个共同的前缀组合框架的过程非常简单。 要获得一个框架的前缀, 它会删除结尾的所有非阿尔法字符 :

**投入**

`acorn-1`
`acorn-2`
`acorn-3`
`ant-1`
`ant-2`
`ant-3`
`ant-4`
`ant-5`
`ant-6`

**产出**

* `acorn`动画
  * `acorn-1` 帧
  * `acorn-2` 帧
  * `acorn-3` 帧
* `ant`动画
  * `ant-2` 帧
  * `ant-3` 帧
  * `ant-4` 帧
  * `ant-5` 帧
  * `ant-6` 帧

一些纹理包装工具包括框名中的图像扩展,例如`ant-1.png`,它打破了提取框前缀的算法,因此,它首先要移除框名的所有图像扩展,如果是的话. 然后`ant-1.png`转换为`ant-1`,前缀将是`ant`.

---
