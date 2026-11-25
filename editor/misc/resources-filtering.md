# 资源过滤 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/misc/resources-filtering)

Phaser编辑器是典型的网页应用程序,具有服务器层和客户端(浏览器)层。由于浏览器无法直接访问项目文件,编辑器会加载Z[many resources in memory](/editor/misc/resources-caching)。为此,您必须在项目中保留少量文件。通常,HTML5游戏需要几个文件,但您可能包括第三方工具的文件或游戏服务器侧的文件.

如果您无法改变工程的结构, 您可以将文件从 QQ 中排除出去 。 Phaser 编辑器工程, 使用 `.skip` 文件。它类似于您如何将文件从 Git 仓库中排除,使用 `.gitignore` 文档。

您可以在工程的文件夹中创建 `.skip` 文件, 并写入您想要排除的文件名模式 。

这是`.skip`文件的一个例子:

```bash

# exclude all node_modules folders in the project.
**/node_modules


# exclude a single file in the current directory
my-private-secret.data


# exclude all files in the form @2x.png, @2x.json,...
**/*@2x.*
```

如果 `.skip` 文件为空, 那么编辑器会假设它有 `*` 模式。 这意味着它会排除文件夹的所有内容。 我们这样做是为了与编辑器的旧版本的反向兼容 。

除了您在每个工程中创建的 `.skip`文件外, 您还可以编辑放置在 Phaser 编辑器安装目录中的 `default-skip`文件。 文件定义的图案将适用于所有工程。 默认情况下, 它包括跳过所有 dor( `.`) 开始的文件的图案、 所有 `node_modules` 文件夹和所有 `__MACOSX` 文件 。

过滤文件的另一种方法是使用[project configuration file](/editor/misc/project-config)的`skip`设置。 您可以设置一组“ 抽取规则”, 与`.skip` 文件中使用的相同 :

```bash
// phasereditor2d.config.json

{
    "skip": ["my-private-secret.data", "**/*@2x.*"]
}
```


## 模式 {#patterns}

我们使用[doublestart](https://github.com/bmatcuk/doublestar#patterns)项目进行模式匹配。以下是该项目文件的一部分:

模式中的特殊术语:

| 特别条款   | 含义                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------|
| `*`             | 匹配任何非路径分离的序列                                               |
| `**`            | 匹配任意字符序列,包括路径分隔符                             |
| `?`             | 匹配任何单一的非路径分隔字符                                           |
| `[class]`       | 匹配任何单一的非路径分隔字符与一个字符类别(见下文) |
| `{alt1,...}`    | 如果一个逗号分隔的选项匹配, 匹配字符序列       |

字符类支持如下:

| 类      | 含义                                                       |
|------------|---------------------------------------------------------------|
| `[abc]`    | 匹配集中的任何单个字符                   |
| `[a-z]`    | 匹配区域内的任何单个字符                     |
| `[^class]` | 匹配任何一个字符, 匹配该类的 * 不匹配 * |

---
