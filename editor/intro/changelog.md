# 更新日志 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/intro/changelog)

## v5.0.1 - 2026年5月11日(昭和2年5月11日) {#v501---may-11-2026}

* 修复无害环境管理模块中缺少的 Phaser导入。
* 修复 Phaser v4 的 Spine 导入 。
* 修复项目模板中的 Phaser v4 导入.

## v5.0.0 - 2026年4月15日 - 2026年6月15日,纽约 {#v500---apr-15-2026}

**已添加**

* 添加支持到 Phaser 4 过滤器(Phaser 3中的前 FX)中.
* 添加支持到斯宾恩4.2.
* 服务器:从依赖性中发现项目脚本库.
* 添加新过滤器:键、维格内特、擦拭、图像灯、全景Blur、Blocky。
* 添加 MCP 支持到新过滤器中。
* 允许配置粒子 Emitter 的动画 。
* 脚本节点限制.
* 用户组件限制.
* 新建游戏对象参考用户属性.
* 组件和预制体的新矩阵型用户属性 。
* 新建 Spine Event 用户属性类型 。
* 新建 JSON 用户属性类型 。
* 新建 Spine Slot 名称用户属性类型 。
* 新建仅针对用户属性的编辑器参数 。
* 新建 `Deprecated` 用户属性参数。 已耗尽的属性在检查器视图中隐藏, 除非解锁 。
* 包含游戏对象和预fab描述的新描述部分.
* Spine 窗口显示动画事件数据.
* 场景编译器:为类界面添加一个新的用户区段.
* 场景编译器:为类修饰器添加新的用户部分.
* 在查看器中展开所有节点的新命令( `E` 键) 。
* 控制场景编辑器中对象的渲染:
    - 仅编辑器参数和命令(`H`)在场景编辑器中渲染或不渲染对象.
    - 设置编辑器的命令 。
    - 在“大纲”视图中显示一个图标,以切换对象的编辑器渲染。
* 在查看器中显示项目工具提示 。
* 向所有观众添加列表/网格视图图标.
* 添加预制体图自定义颜色。
* 用于显示/隐藏大纲视图中的用户组件的新设置 。
* 在每一个进步对话框的步号中显示描述信息 。
* 向图版编辑器添加一个新的 Tileset Info 工具。
* 播放对话框:显示要复制的按钮, 并显示游戏有未处理错误时的错误 。
* Play Dialog:添加一个刷新按钮,并听项目更改自动重新装入游戏.
* 添加新参数到设置对话框中 :
    - 编译器设置 。
    - Spine 模块名称.
    - 启用缩略图 。
    - 启动前预装 Scene 缩略图 。
* 添加新的调试命令到“ 在场景中查找复制对象 ” 。
* 添加广泛的 MCP 工具集( 镜像、 对象、 过滤器、 砖瓦、 丝绸、 纹理、 截图)
    - 添加 MCP 视图以显示 MCP 消息日志 。
* 添加光标代码编辑器的支持 :
    - 在 Phaser 编辑器设置中: 配置光标为默认代码编辑器的新选项 。
    - 在配置 MCP 服务器对话框中,有一个选项可以将Phaser编辑器 mcp 添加到工程配置中.
* 添加新的 AI 聊天视图, 以向 Phaser 编辑器代理聊天器聊天 。
* 将圆形属性添加到矩形游戏对象中。
* 添加新日志视图以显示应用程序日志消息 。
* 添加 Unbox 预制体命令 。
* [#91](https://github.com/playson-games/phaser-editor/issues/91) 块视图:允许通过内部/外部组合块.
* AI聊天:添加对场景文件附件的支持.
* AI聊天:显示附件工具提示.
* MCP服务器:新增AI主菜单,并配有AI相关快捷键.
* 现在,MCP 服务器是编辑器桌面应用程序的一部分。编辑器提供了MCP 服务器配置对话框,以获取MCP服务器信息以及自动配置克劳德桌面,光标和VSCode。配置中还包括规则文件。
* 将“扩展”全部选项添加到查看器菜单中。
* 探测到共鸣循环
* 执行macOS和Windows桌面应用的自动更新。
* [#99](https://github.com/playson-games/phaser-editor/issues/99) 允许从最近的项目列表中删除一个项目。 突出显示不存在的项目 。
* [#102](https://github.com/playson-games/phaser-editor/issues/102) JSON属性Schema验证.

**已更改**

* 将所有项目模板都 Migrates all project 模板到 Phaser 4 .
* 更新脚本节点库到 Phaser 4 。
* 更新 Chat 的 LLMs 预设到最新版本 。
* 添加运行Intel的架构警告,以苹果硅Macs为基础构建.
* 米拉特斯Go和Node到最新的稳定版本.
* 使用现代的基于蟒蛇的脚本来创建DMG(mac snurger).
* 将 Migrates 切换到新的 TintFill 模式 。
* 编辑脚本节点预制体场景时, 不包括Snaping, B边框和 Box2D 视图。 一开始显示预制体区段 。
* 大纲视图以自然顺序显示脚本节点的孩子.
* 场景编辑器否认复制或剪切嵌入的预fab实例.
* 场景编辑器将副本/粘贴操作与系统剪贴板整合.
* 场景编辑器在粘贴内容前需要预先加装和用户组件验证.
* 改进Arcade 物理体序列化, 并加装所有相关属性的`body.`前缀, 它将现有的Phaser编辑器 4 场景迁移到新的属性名称 。
* 改善大场面的加载和节省时间.
* 允许将资源文件直接从文件视图导入到活动的资源包编辑器。
* 最新电源更新.

**固定**

* 修复编辑器桌面平线连接到编辑器服务器。
* 修复斯宾尼Game Object未使用的进口代码生成.
* 解决子对象处置和制造巢式预制体滤波器的情况。
* 修复递增数的场事件处理。
* 修复在现场处理的图案动画.
* 修复 particleBringToTop 属性的默认值。
* 修复对象列表中嵌入式预fab变量的代码生成.
* 解决无本地压倒性数据的UUID生成嵌套预制体实例。
* 修复复杂嵌套预制体器的 Spine Object 资源装载。
* 修复粒子发射框部分。
* 修复用户属性中引用对象的可变代码生成。
* [#78](https://github.com/phaserjs/phaser-editor-issues/issues/78) 修复Box2D "updateWorld" 类型。
* [#47](https://github.com/playson-games/phaser-editor/issues/47)在游戏对象参考物属性类型中逐项搜索固定.
* 修复嵌套预制体实例的复制/粘贴。
* 修复可编辑图版和可编辑图版层的复制/粘贴.
* 修复元素嵌入前法布实例时的对象列表类型推论 。
* 修复打开 Prefab 命令( `F` 键), 当选择为嵌入式 Prefab 实例时打开 。
* [#63](https://github.com/playson-games/phaser-editor/issues/63) 测量检查官的角值(如`-60`).
* 在场景编辑大纲视图中加快过滤.
* [#89](https://github.com/playson-games/phaser-editor/issues/89) 修复位图字体按钮锁状态.
* [#86](https://github.com/playson-games/phaser-editor/issues/86)设定矩形默认为0.

## v4.11.1 - 2025年3月24日,纽约 {#v4111---mar-24-2025}

* 在检查器视图中修复复选框布局 。
* 修复禁用按钮上的 Phaser Studio 颜色主题 。
* 修复检查器视图显示嵌套预制体变体属性.

[Release notes](https://phaser.io/news/2025/03/phaser-editor-4110-released)

## v4.11.0 - 2025年3月17日(中文(简体) ). {#v4110---mar-17-2025}

* 在 Start 页面中显示 Phaser 新闻和编辑器教程 。
* 在“启动”页面中显示每个工程的缩略图图像 。
* 在"开工"页面中显示"恢复你的工程"部分.
* 编辑器不会自动打开最新的工程,在Start页面中会突出显示.
* 删除聊天窗口。
* 添加 Phaser Studio 色彩主题开始桌面版屏幕.
* 将 Phaser Studio 色彩主题添加到工作台, 默认设置 。
* 将主题部分添加到设置对话框中。
* 添加遥测.
* 检测项目是否为 Phaser 4 项目。如果项目为 Phaser 4,则禁用 FX 和 Spine 特性 。

[Release notes](https://phaser.io/news/2025/03/phaser-editor-4110-released)

## v4.1.0 - 2025年3月10日 (中文(简体) ). {#v4100---mar-10-2025}

[Release notes](https://phaser.io/news/2025/03/phaser-editor-4100-released)

* 更新模板为 Phaser 3.88.2.
* 添加场景 Spine 动画预览 。
* 允许设置“ 资源包” 编辑器中脊椎资源预览地图集键 。
* 修复嵌套预制体序列中的bugs.
* 允许编辑Box2D体和形状的嵌套预制体式.
* 允许编辑Spine 法布斯和巢预法布斯的骨架.
* 以默认的 blendMode 代码生成器修复错误,用于容器,层,和脊椎物体.
* 将对象添加到容器或层中,从而修复回归错误。
* 添加新参数以包含/排除用户组件中`this.gameObject`字段的代码生成.

## v4.9.0 - 2025年2月18日 (中文(简体) ). {#v490---feb-18-2025}

[Release notes](https://phaser.io/news/2025/02/phaser-editor-490-released)

* 删除桌面版中的确认对话框 。
* 添加支持到 Box2D 中。
* 编辑器获得焦点时, 将“ 鬼” 对象的选择问题修复为错误 。

## v4.8.1 - 2024年12月18日 (中文(简体) ). {#v481---dec-18-2024}

[Release notes](https://phaser.io/news/2024/12/phaser-editor-481-released)

* 修正查看器渲染回归。

## v4.8.0 - 2024年12月16日 (中文(简体) ). {#v480---dec-16-2024}

[Release notes](https://phaser.io/news/2024/12/phaser-editor-481-released)

* 添加到压缩纹理中的支持 。
* 永远不要同时显示资源预览和图像文件预览.
* 在 setSizeToFrame 方法中修复错误,用于内置的图示动画.
* [#53](https://github.com/phaserjs/phaser-editor-issues/issues/52)编译器的JavaScript输出增加了冗余的代码行.
* [#54](https://github.com/phaserjs/phaser-editor-issues/issues/54)在Glow FX对象中添加了`quality`和`distance`参数的支持.
* [#58](https://github.com/phaserjs/phaser-editor-issues/issues/58) 添加混合模式支持.
* [#55](https://github.com/phaserjs/phaser-editor-issues/issues/55)(Fix) 大纲视图中的箭头键移动选定的对象。
* [#21](https://github.com/phaserjs/phaser-editor-issues/issues/21) A命令打开OS终端.
* [#26](https://github.com/phaserjs/phaser-editor-issues/issues/26) 删除文件操作现在将文件发送到回收站(Desktop版).
* [#33](https://github.com/phaserjs/phaser-editor-issues/issues/33) 将“ 可见” 参数添加到“ 资源包” 编辑器中。 允许在场景工具中隐藏/显示资源 。
* [#2](https://github.com/phaserjs/phaser-editor-issues/issues/2) Fixs scene 编辑器网格渲染,当浏览器的系数有巨大的缩放时.

## v4.7.1 - 2024年12月2日 (中文(简体) ). {#v471---dec-2-2024}

[Release notes](https://phaser.io/news/2024/11/phaser-editor-v470-released)

* [#50](https://github.com/phaserjs/phaser-editor-issues/issues/50) 修复层层的序列化在一个层或容器内. 

## v4.7.0 - 2024年11月27日 (中文(简体) ). {#v470---nov-27-2024}

[Release notes](https://phaser.io/news/2024/11/phaser-editor-v470-released)

* 删除可启用/可禁用像素艺术命令 。
* 删除设置的画布上下文到 WebGL/Canvas 类型命令 。
* 欢迎新的设置 UI( 默认应用程序、 键盘快捷键、 场景设置) 。
* [#49](https://github.com/phaserjs/phaser-editor-issues/issues/49) 修补在深度顺序操作时意外删除图片.
* 更新内部编辑器至Phaser 3.87.
* 添加字体加载器支持到资源包和场景编辑器中.

## 4.6.1 - 2024年11月10日 (中文(简体) ). {#461---nov-10-2024}

[Release notes](https://phaser.io/news/2024/11/phaser-editor-v460-released)

* 以文本对象代码生成来修复回归错误 。

## 4.6.0 - 2024年11月7日(半天) {#460---nov-7-2024}

[Release notes](https://phaser.io/news/2024/11/phaser-editor-v460-released)

* 可编辑的图纸支持 。
* [#44](https://github.com/phaserjs/phaser-editor-issues/issues/44) 向ArcadeSprite对象添加了图案动画支持.
* [#46](https://github.com/phaserjs/phaser-editor-issues/issues/46) 添加分辨率属性到文本对象中 。
* [#43](https://github.com/phaserjs/phaser-editor-issues/issues/43)更新所有帮助链接到新的帮助网站.

## v4.5.1 - 2024年10月13日 (中文(简体) ). {#v451---oct-13-2024}

[Release notes](https://phaser.io/news/2024/10/phaser-editor-451-released)

* 最新消息为Phaser 3.86.
* 修复场景编辑器中的图列马普像素圆形问题.
* 桌面: 显示编辑器服务器启动时需要等待的新页面 。
* 桌面: 配置代理时修正 npm 安装, 但禁用 。
* [#41](https://github.com/phaserjs/phaser-editor-issues/issues/41) 修复变量名称生成.

## v4.5.0 - 2024年9月26日 (中文(简体) ). {#v450---sep-26-2024}

[Release notes](https://phaser.io/news/2024/09/phaser-editor-v45-released)

* 场景编译器不会从"摄像机"模块导入Phaser.
* 删除基本的打字模板。
* 将添加脚本对话框中的脚本节点按文件夹分组 。
* 以文件夹组合 Go To 对话框中的脚本节点 。
* 将代码Mirror编辑器替换为摩纳哥编辑器,以更好地进行编码。
* 允许在 macOS 的端口图标中丢弃文件夹 。
* 允许在桌面编辑器的启动页面中丢弃文件夹 。
* 不包括编辑器在浏览器中运行时的桌面插件(递归).

## v4.4.1 - 2024年9月23日 (中文(简体) ). {#v441---sep-23-2024}

[Release notes](https://phaser.io/news/2024/09/phaser-editor-v44-released)

* 修正代理服务器后面的用户认证 。

## v4.4.0 - 2024年9月17日 (中文(简体) ). {#v440---sep-17-2024}

[Release notes](https://phaser.io/news/2024/09/phaser-editor-v44-released)

* 斯匹克动画的内景预览.
* Go To Scene 对话框使用“ find” 按钮 。
* 新建 Go To 对话框取代 Go To Scene 对话框。 它包括资源包和用户组件 。
* 将排序命令添加到场景工具窗格中。
* 在主工具栏(`Ctrl+Alt+E`)中添加“在外部编辑器中打开”动作。
* 使"在外部编辑器中打开"动作足够智能,可以打开源代码文件(shenes,用户组件).
* 与 Phaser Studio 支持团队添加聊天.
* Workbench: 固定默认场景设置计算.
* 更新为3.85.2.

## 2024年9月9日,第4.3.0号 {#v430---sep-9-2024}

[Release notes](https://phaser.io/news/2024/09/phaser-editor-v43-released)

* 重修上传文件的工作流程 。
    * 在文件视图中使用“ 添加文件” 而不是“ 上载文件 ” 。
    * 改进检查器视图中的“ 添加文件” 部分( 前“ 上载文件 ” ) 。 它显示一个空投区域及添加文件按钮 。
    * 允许为工程添加外部文件夹 。
* 在“文件”视图中选择地图集或图像文件时,在“检查器”视图中显示资源图像框架。
* "有新更新"的消息,现在打开Phaser下载,如果点击的话.
* 工作台: 在有活动对话框时修正拖曳分割的窗体 。
* 执行一个试验时间或编辑器。
* 在主工具栏中添加“打开场景”按钮。
* 修正屏幕对一个图层对象的计算。
* [30](https://github.com/phaserjs/phaser-editor-issues/issues/30) 修复复制脚本节点和容器的命令.
* 最新消息为Phaser 3.85.
* 工作本库:在 Go To Scene 对话框的结尾显示脚本节点 。
* Workbench:在启动IDE窗口时随选择而解决问题.
* 工作台:鼠标出来后修复场景平整.

## v4.2.0 - 2024年8月6日 (中文(简体) ). {#v420---aug-6-2024}

[Release notes](https://phaser.io/news/2024/08/phaser-editor-v420-released)

* 添加重复命令。
* 更新电源到v31.2.0.
* 添加代理配置支持。 包括 Phaser 编辑桌面中的代理配置页面 。
* 修复了使用已禁用的 CORS 运行的 dev 服务器 。
* 添加取消到 Go To Scene 对话框中的按钮 。
* 检查选中的目录在创建工程前是否为空 。
* 添加电子游戏对象。
* 添加视频和音频文件及资源预览部分。
* 将 Pan 工具添加到 Scene 编辑器的主工具栏中 。
* [#24](https://github.com/phaserjs/phaser-editor-issues/issues/24)通过`super()`呼叫中的多边形点.
* [#23](https://github.com/phaserjs/phaser-editor-issues/issues/23) 启动 Dev 服务器,在Mac上带有Vite配置.
* [#29](https://github.com/phaserjs/phaser-editor-issues/issues/29)工作台:固定的套装按住对象大小命令.
* 请用户在启动应用程序前确认Phaser EULA.
* 更新标志赢得欢迎页面 。
* 将初学者指南链接添加到欢迎页面。

## v4.1.0 - 2024年7月11日 - 2024年6月11日 (中文(简体) ). {#v410---jul-11-2024}

[Release notes](https://phaser.io/news/2024/07/phaser-editor-v410-released)

* 添加 ParticleEmitter 游戏对象支持 。
* 修复比边框值小的九思切对象的序列化.
* [#7](https://github.com/phaserjs/phaser-editor-issues/issues/7) 添加到更多音频格式中的支持.
* 记录所有服务器和桌面消息以及错误到`server.log`和`desktop.log`.
* 服务器:向WEBP图像支持添加支持.
* \[[#1](https://github.com/phaserjs/phaser-editor/issues/1)\]在导入多个图像时,在检查器视图中修正不良布局.
* 桌面:改进市场模板的采集、组织和过滤。
* 桌面:添加了新的Vite内置项目模板.
* 桌面: 自动安装工程依赖性 。
* 桌面: 在运行游戏前启动开发服务器。 必要时它会安装依赖性 。
* 桌面: 如果未安装 npm , 则显示引导 UI 。
* 桌面: 删除遗留( Gumroad) 许可键支持 。
* 桌面:点击配置图或名称打开浏览器中的Phaser账户.

### v4.02 - 2024年5月20日 (中文(简体) ). {#v402---may-20-2024}

[Release notes](https://phaser.io/news/2024/05/phaser-editor-v402-released)

* 将场景编辑器上下文菜单的“ Layout - > 显示布局工具”选项移动到“ Tools - > 显示场景工具”。
* 改进 Spritesheet 预览部分 。
* 在 SceneEditor 中选择对象时显示 Spritesheet 预览部分。
* 使用对象范围来选择一个位图Text。
* 修复 ColorMatrix FX 代码生成.
* [#1](https://github.com/phaserjs/phaser-editor-issues/issues/1) 固定兼容问题与v3配置文件和`-max-number-files`旗.

## v4.0.1 - 3034年5月4日(中文(简体) ). {#v401---may-4-3034}

* 更新欢迎页面中的问题重播的链接。
* [#3](https://github.com/phaserjs/phaser-editor-issues/issues/3) Fixes在Windows 11中确认对话框.

### 在线 {#online}

* 允许同时在多个项目中工作.

## v4.0.0 - 2024年4月29日,农历四月二十九日 互联网档案馆的存档,存档日期2013-09-02. {#v400---apr-29-2024}

* 显示欢迎页。
* [#314](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/314):(Fix) 粘贴多个脚本节点会改变它们的顺序.
* [#316](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/251):(Fix)在预制体实例中隐藏用户组件.
* 删除文件限制的数量。
* 需要Phaser.io用户的认证.
* 桌面版本没有免费模式。
* 新图标。
* 工作台:在有欢迎页时,修正`openfile`命令.
* 从文件视图中删除子章节。
* 添加支持到多个窗口布局中。
* 最新摩纳哥编辑的更新v0.47.

## v3.67.0, 2月22日, 纽约 {#v3670-feb-22}

* 最新TypeScript 5.3.3的更新。
* 最新代码Mirror 5.66.16的更新.
* 添加支持为Phaser 3.80.
* 当用户执行 Play 命令时保存所有编辑器 。
* 深度命令现在与Mac键盘一起工作,并配有数字垫,在其默认配置中.
* 打开多个上下文菜单修复错误 。
* 颜色拾取器显示颜色的实时预览.
* 允许用鼠标轮更改数值。
* 允许用上下键更改数值。如果按下 Shift,则会递增 10 。
* 允许通过拖曳标签来改变数值 。
* 添加对Shader Effects对象, Glow 和 Shadow 的支持.
* 使用文本的内部画布来渲染大纲视图中的文本对象。
* 默认使用九思乐和三思乐的__MISSING纹理.

## v3.66.0 - 2024年1月11日,第6页 {#v3660---jan-11-2024}

* 允许设置游戏对象的显示名称。
* 显示名称格式化表达式 `#{x}` 扩展为"x".
* 显示名称格式显示 `TargetActionComp.target` 值, 如果存在的话 。
* 复制游戏对象树时修复名称碰撞.
* 修复复制树本/纸板上的子对象对象。
* 修复了巢状预制体的用户组件.
* 允许用户组件对象格式化 。
* 允许只读编辑器 。
* 将只读设定为节点文件的编辑器 。

## v3.65.0 - 2024年12月13日(昭和2年12月1日) {#v3650---dec-13-2024}

* 允许使用节点模块的预制体和用户组件.
* 允许将文件夹标记为“ 复制” 库, 并带有 `library.txt` 文件 。
* 将onWorldBounds属性添加到Arcade物理体.
* 添加脚本节点对话框按文件夹和节点模块组合脚本.
* 块视图按文件夹和节点模块对脚本进行分组.
* 允许自定义显示预制体实例的格式,使用`${}`和`#{}`表达式.
* 显示带有预制体属性信息的工具提示 。
* 允许设置场景显示名称 。
* 允许设置用户组件的显示名称 。
* Migrates 将所有项目模板都放到新的脚本库中.

## v3.64.0 - 2023年11月10日(中文) 互联网档案馆的存档,存档日期2013-09-02. {#v3640---nov-10-2023}

* 修复了单层预制体图的缩略图.
* 允许合并“资源包”条目中的导入和打开按钮。
* [#251](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/251) 修复器在动画编辑器中的图案定位.
* [#209](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/209)改进场景边框画.
* 改进动画预览 UI :
    - 新建动画预览部分.
    - 新动画预览部分.
    - 在动画键用户属性中显示预览按钮。
* 将新的动画部分添加到 Sprite 游戏对象中。 它即将自动启动一个 Sprite 动画 。
* 将 `showBeforeDelay` 添加到动画编辑器中.
* 在 Scene 编辑器的块视图中显示 Sprite 动画块 。
* 星际迷航动画支持.
* 新建代码片段场景元素 。
* 优化WEBGL背景集合.
* [#295](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/295) 修补 tilemapLayer 无效的方法工厂。

## v3.63.0 - 2023年9月30日 (中文(简体) ). {#v3630---sep-30-2023}

* 打开 `openfile` URL 搜索参数中给出的文件。就像 `?openfile=some/file` 中的文件。
* 在装入工作台前显示溅射 。
* 助推负载速度:将编辑器的图标从单文件迁移到纹理图集.
* 加速负载速度:将所有 IDE 文本资源捆绑到一个单一的res.json 文件.
* 改进浏览器缓存管理。 在云中运行时, 装入速度更快 。
* 在预制体属性区显示属性快捷键。
* 当选择属性时, 也会显示 Prefab 属性 。
* 在事件属性对话框中显示事件图标 。
* 允许从 Phaser 编辑 2D 网站下载所有 v3 文件 。
* [249](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/249) Auto编译场景文件时创建.
* 添加支持到Spine 动画中.
* 将脊椎工程模板添加到市场.
* [#289](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/289) 固定器在巢容器上计算出撞击区域.

## v3.62.2, Jul 2, 2023年7月2日 {#v3622-jul-2-2023}

* 修复预制体中导出用户组件 。

## v3.62.1, June 30, 2023 (英语). {#v3621-jun-30-2023}

* 修复 KeyCode 用户属性编辑器 。

## v3.62.0, 2023年6月29日, 纽约 {#v3620-jun-29-2023}

* 新事件用户属性 。
* [#284](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/284) 固定器命中区域域渲染容器。
* 显示对话框的新添加 Prefab 属性命令 。
* 替换编辑移动命令的对象深度命令。
* 以编辑器移动命令取代对象列表排序命令。
* 允许使用“编辑”移动命令更改预制体属性。从“预制体属性”区域菜单中删除“移动”选项。
* 允许复制/剪切/粘贴预制体属性.
* 允许复制/剪切/粘贴键盘键 。
* 在对象变量用户属性对话框中显示键盘. Key and Object List 对象 。
* 添加新的键代码用户属性。
* 修复了区域序列化。
* 删除用户组件部分, 并显示用户组件属性为单个部分 :
    * 将脚本上下文菜单重命名为脚本,并包括:
        - 添加用户组件( `M` 键)
        - 浏览用户组件( `Shift+M` 键)
* 从“大纲”视图中删除用户组件节点。
* 删除 Prefabexact 一节,将 Prefabex 用户属性显示为单个段落 。
* 替换纹理帧命令响应 `F` 键 。
* 修复在所有选定的游戏对象中添加脚本节点.
[#223](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/222) 固定标签焦点为用户属性的DOM元素.

## v3.61.0 - 2023年5月18日 (中文(简体) ). {#v3610---may-18-2023}

* 检查一个场景文件是否由编辑器中较新的和不兼容的版本生成.
* 在大纲视图中显示对象列表项目。允许命令这些项目使用上、下、上、下命令。
* 一个新的游戏对象范围: LOCAL. LOCAL范围现在是对象的默认范围,并且与之前的 M方法OD 范围有相同的含义,现在 M方法OD 的范围强制为对象创建变量.
* 自动计算中私密的巢穴预制体,不需要声明巢穴预制体的母体为巢穴预制体. 
* 改进大纲元素标记。它使用tahs 类似 `#prefab_inst` `#nested_prefab_inst` `#scope_local` `#scope_nested_prefab`...你可以在大纲过滤框中搜索它。
* 允许在对象中输入 。
* 将名称参数添加到嵌入的预fab实例的变量部分。
* [#282](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/282)在用户对象变量属性中使用完整的嵌入式预fab路径.
* 在编辑非标点点景时,将脚本节点预制体排除在块视图之外.

## v3.60.3 - 2023年4月27日,农历四月二十七日 {#v3603---apr-27-2023}

* 用 Play 命令修复回归错误。

## v3.60.2 - 2023年4月27日(昭和2年4月27日) {#v3602---apr-27-2023}

* 修复创建带有选定容器或层的预制体层。
* 更新带有错误修正的脚本节点资源。
* [#129](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/129)添加了预览场景命令(Ctrl+0),它在浏览器中运行游戏并传递`start=<scene-name>`参数.

## v3.60.1 - 2023年4月21日,纽约 {#v3601---apr-21-2023}

* 修复普通对象序列化(键盘键,碰撞器,...).

## v3.60.0 - 2023年4月16日(农历四月十六日) {#v3600---apr-16-2023}

* 修复检查器视图中大小部分的标签。
* 场景编译器:修复类场声明.
* 场景编译器:修复巢状的预fab varname分辨率.
* 改进文件夹图标 。
* 添加启用/ 无法像素艺术渲染模式的命令 。
* 新游戏对象支持:NineSlice和TreeSlice.
* 删除父部分 。
* 支持新的脚本节点对象。
* 更新应用程序图标。
* 最新消息为Phaser 3.60.
* 更新allInOne内置模板,支持Phaser 3.60和脚本节点.

## v3.36.2 - 2022年12月14日,纽约 {#v3362---dec-14-2022}

* 从 Core 获取最新消息 : 
    * 用许可证管理器生成的许可证键修复电子邮件通知 。

## v3.36.1 - 2022年12月12日 (中文(简体) ). {#v3361---dec-12-2022}

* 从Core那里得到最新更改。

## v3.36.0 - 2022年11月15日(中文) 互联网档案馆的存档,存档日期2013-09-02. {#v3360---nov-15-2022}

* 动画编辑器:允许以单帧制作动画.
* 动画编辑器:允许将动画键编译为JavaScript/TypeScript常数.
* 场景编辑器:添加键盘. Key对象支持.

## v3.35.2 - 2022年11月10日 (中文(简体) ). {#v3352---nov-10-2022}

* 已重建的迁移进程。 在创建场景缩略图时会修正迁移程序 。
* 添加 `Text.align` 属性的迁移 。
* 打开命令调色板时修复错误, 没有编辑器打开 。
* 添加一个 **Migrate 并编译全部 Sceeles ** 命令。
* [#250](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/250): 修补在缩放对象中添加物理体.

## v3.35.1 - 2022年11月3日(中文(简体) ). {#v3351---nov-3-2022}

* 删除检查器区域中的额外 collideWorldBounds 参数。
* 在大纲视图中将预制体属性显示为独立元素。
* 用户组件编辑器:将属性显示为独立的实体并编辑.
* 臭虫修复:在将其转换为预制体时,不会将用户共振器留在对象中.
* 修复“新更新可用”通知的背景。如果单击通知面板,则打开`https://phasereditor2d.com/downloads`页。
* 显示“大纲”视图中对象的子节点“用户组件”。
* 在预制体对象的用户组件中新增导出参数 。

## v3.35.0 - 2022年10月14日,日内瓦 {#v3350---oct-14-2022}

* 允许将对象附加到预制体实例中。
* 修复用户组件文件序列化。 Name `app` 字段为 `Phaser Editor 2D - User Components Editor`,则 `contentType` 字段为 `phasereditor2d.core.scene.UserComponents`.
* 删除基于摩纳哥的编辑器。
* 检查器视图中 XY 标签的使用颜色 。
* 添加对Arcade物理的支持。 Arcade Image & Sprite 和身体工具。
* 将 AppLE_M1_README.txt 文件添加到 All-in-One/macOS-arm dist 中.
* 以替换类型命令修复错误: 错误解锁位置属性 。

## v3.34.0 - 2022年8月12日(中文) 互联网档案馆的存档,存档日期2013-09-02. {#v3340---aug-12-2022}

* 将来自另一场景的一层/容器预装粘贴时修复资源预装.
* 从命令的标签中删除 `Key`和 `Digit` 前缀.
* 场景编辑器:用缩放的图像修正布局操作.
* 场景编辑器: 改进布局工具栏。 添加源代码动作 。
* [#229](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/229) 固定图片层的序列化,作为容器和层层的孩子.
* [#227](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/227) 添加多边形的游戏对象.

## v3.33.2 - 2022年5月31日 (中文(简体) ). {#v3332---may-31-2022}

* 改进大小工具修饰器。
* 避免缓存插件资源 。
* 场景编辑器:在粘贴操作后跳过刷新场景,修复对象的加载器扩展. 
* 导出 Tint 属性到插件 。
* 起源工具允许自定义起源属性(如在九边形容器中).
* 改进对第三方游戏对象插件的支持.
* 将 Alpha 组件添加到容器游戏对象中.
* 修正自定义源对象的布局命令。
* 修复图版的场码生成.
* 修复图版的层层选择在现场.

## v3.33.1 - 2022年5月10日 (中文(简体) ). {#v3331---may-10-2022}

* [#210](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/210) 缺少变量窗格。 删除与检查器视图部分相关的每条字段 。
* [#212](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/212) 新的对象构造器用户属性类型 。
* [#216](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/216) 使用组件时,没有可用于选择的纹理窗口的纹理。

## v3.33.0 - 2022年4月18日 (中文(简体) ). {#v3330---april-18-2022}

### 已添加 {#added}

* [#195](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/195) 新GO名称参数.
* [#144](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/144)场景编辑器:允许贴纸到位.
* 场景编辑器:支持新的场景键用户属性类型.
* 场景编辑器:支持新的对象变量用户属性类型.
* [#181](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/181)场景编辑器:支持新的 Color用户属性类型.

### 已更改 {#changed}

* 场景编辑器:从检查器视图中删除细节子 Tab.
* 场景编辑器:重置的缩放按钮恢复了镜头的缩放和位置(0,0). 
* [#182](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/182) macOS 错误:执行:"代码":在$PATH中找不到可执行文件.
* [#185](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/185)允许使用上传对话框上传超过10MB的文件.

### 修补 {#fixes}

* 场景编辑器: 修正 CANVAS 模式下的 TileSprite 命中区域计算。 围绕此模式的作品 Phaser温德图尔的虫子shapnshotPixel 方法。 。 方法。
* 场景编辑器: 修正场景缩略图制作器, 不包含隐形容器/ 层 。
* 场景编辑器: 修正0宽/ 高的物体的查看器渲染。 如文字游戏对象, 值为 `""` 。
* 场景编辑器:在隐藏的父母下修正对象的采摘.
* 场景编辑器:在移动到新父时修正对象的顺序 。
* 场景编辑器:在macOS上防止滚动整个页面,启用滚动惯性.
* 场景编辑器:指针接近翻译工具处理器时用ALT键修正平板.
* 场景编辑器:在使用ALT键平整时修改选择时修改.
* 场景编辑器:为打开macOS(XQO)中场景文件而修正命令.
* [#200](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/200)比特玛普Text对齐导致NaN位置.
* 场景编辑器:在Scooker视图中修正文本内容的文本区域参数.
* 场景编辑器:将加载消息位置调整到 DPR 。
* 场景编辑器:添加缺失的 `light/bitmapfont-type@2x.png` 图标.
* [#29](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/29) Fixs拖放图像在Safari中.
* 工作台:防止Safari将地址栏包含在标签/焦点顺序中.
* [#149](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/149) 粘贴容器时重命名子对象,在新名称中修改编号的修饰。
* 编辑器标签:在Safari中修正光标类型.
* 以 DPR > 1. 修正屏幕中查看器的单元格大小 。

## v3.32.1 - 2022年2月27日 (中文(简体) ). {#v3321---feb-27-2022}

* 场景编译器:如果场景也是场景,则生成场景的超类的导入.
* [#190](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/190) 构造生成的代码,这样vscode就不会在被覆盖的区段添加导入.
* [#185](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/185) 您的项目超过了允许的文件的最大数量 。
* [#183](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/183)组件选项类型卷轴问题.

## 2022年1月12日,第3.32.0号 {#v3320---jan-12-2022}

* 以新的 `phasereditor2d.config.json` 文件自定义编辑器 。
* [#168](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/168) 命令调色板中的下箭头关闭调色板,在场景编辑器中移动选中的图像.
* [#171](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/pull/171) 在整个编辑中一致使用"导入".
* [#169](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/pull/169) Ctrl+Digit2 - > Ctrl+2 外观为 Ctrl+3 和 Ctrl+4 .

## v3.31.2 - 2021年12月14日, 纽约 {#v3312---dec-14-2021}

* 更新版本.

## v3.31.1 - 2021年12月14日,纽约 {#v3311---dec-14-2021}

### 修补 {#fixes-1}

* 启动模板: Webpack 分割块 。
* 修复海滩上一天的网络包装
* 摩纳哥编辑器装入 Phaser内置型号的defs,不需要从项目中读取 `.d.ts`文件.
* 属性部分: 修正显示三点菜单并崩溃 。

## v3.31.0 - 2021年11月29日 (中文(简体) ). {#v3310---nov-29-2021}

### 已添加 {#added-1}

* [#145](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/145):位图Text:新增支持`maxWidth`属性.
* 场景编辑器:用于设置默认渲染类型的命令.

### 已更改 {#changed-1}

* AllInOne: Play Project命令打开默认浏览器.
* 场景编译器:格式为文本风格的JSON,具有VSCode相似格式.

### 固定 {#fixed}

* 场景编辑器: 修正断开父命令 。
* [#143](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/143)在从其他场景粘贴一个位图文字对象时会固定位图字体加载.
* [#154](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/154) 位置值不正确,在巢状预制体的衍生类中传递给超级调用.
* [150](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/150)编辑器不正确表示:未锁的巢状前发性格不适用于前发性格的例.
* 修复文本和比特地图Text对象中默认的源值的序列化。它现在在那些情况下使用 `(0, 0)` 。
* 总是在现场序列化和代码生成中包含一个解锁属性的值.
* 场景编辑器:允许改变容器预制体实例的原产地,并带有未解锁的位置.
* 场景编辑器:修复巢状前发型的 var 名称.

## v3.30.0 - 2021年9月18日 (中文(简体) ). {#v3300---sep-18-2021}

### 已添加 {#added-2}

* 代码Mirror文本编辑器.
* allInOne命令:打开项目,关闭项目.

### 更新 {#updated}

* 摩纳哥编辑器总是采用高级模式。
* 最新版Phaser3.5.5.2更新版.

### 删除 {#remove}

* 删除所有与创建和加载工程相关的功能。 它现在显示一个单一的工程。

## v3.20.0 - 2021年8月23日 (中文(简体) ). {#v3200---aug-23-2021}

### 已添加 {#added-3}

* 内脏预制体:
    * 涅盘预法供养.
    * 预制体构造器中使用无源操作器(`??`)。
    * 允许解锁预制体实例的位置。 此更改引入了与编辑器以前的版本不兼容的新场景格式 。
* 再见`prefab-awake`&`components-awake`事件 欢迎`scene-awake`
    * 更新 `UserComponent.js`模板.
* 场景编辑器:子对象部分中新的“大纲中的子对象”参数。
* [#136](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/136) 预告 : `generateAwakeHandler`.
* 编译器: 添加 ** Fields in Constructionor (JS) ** 旗。 允许在构造器中生成字段初始化代码, 且不作为类字段。 有些转写器不支持类字段 。
* 九点点游戏对象支持,作为Phaser编辑器2D Extras项目的一部分.

### 更新 {#updated-1}

* [#140](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/140) Scene编译器生成与VS代码兼容的格式代码,它不创建不需要的git diffs.
* 场景编辑器:更改纹理命令允许自动解锁纹理属性.
* 场景编辑器:布局操作允许自动解锁纹理属性.
* 场景编辑器:将容器部分替换为子对象部分,对图层对象也适用.
* [#139](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/139)\[Feature Request\]在打字符中为方法添加类型.
* [#136](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/136) Prefabs:构造器订购自定义道具和START-USER-CTR-CODE.

### 固定 {#fixed-1}

* 场景编辑器(BitmapText):当字体数据在缓存中无法获取时修正错误.
* [#134](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/134) 在编辑器中创建列表,结果生成了生成代码中的初始化阵列.
* [#135](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/135) 文字包宽度不正确
* 场景编辑器:在预制体场景的背景中修正移动到父对话框 。
* 场景编辑器:当显示预制体文件实例时,修正场景部分布局.
* [#142](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/142)动画编辑器:修正改变同一动画的多个属性.

### 删除 {#removed}

* 删除 Parcel 模板。

## v3.1.5.0 - 2021年7月11日 {#v3150---jul-11-2021}

### 固定 {#fixed-2}

* 抓取项目资源预装器错误 。
* [#127](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/127) 固定:默认打开一个区域时滚动高度是错误的.
* 动画编辑器:允许设置浮点数到`frameRate`.

### 已添加 {#added-4}

* 场景编辑器:选择子对象命令.
* 场景编辑器:布局动作:对齐,对齐到边框,网格.
* 场景编辑器:切换可见度指令自动解锁预制体的可见属性.
* [#132](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/132)场景编辑器:自定义属性定义.
* 场景编译器:在预制体情况下发出"预制体觉"事件.
* [#131](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/131)场景编辑器:支持文本文字包装属性.

## 更新 {#update}

* 摩纳哥编辑器更新为v0.25.2. 改进JavaScript工人装载。
* 更新 Webpack 项目模板。现在它使用 [Phaser Asset Pack Hashing tool](https://github.com/PhaserEditor2D/phaser-asset-pack-hashing) 来分发文件 。

## v3.1.4.0 - 2021年5月29日 (中文(简体) ). {#v3140---may-29-2021}

### 已添加 {#added-5}

* 场景编辑器 : ** Add 组件 ** 按钮打开对话框。 组件由容器文件分组 。
* 场景编辑器:在上下文菜单的场景菜单中添加设置选项.
* 资源包编辑器: 添加块属性部分。 它显示一个选项, 用于显示块视图中的所有文件 。
* 资源包编辑器:在上下文菜单中显示设置选项 。
* 场景编辑器: 当启用一个工具( 如缩放工具) 时, 它会要求解锁选定对象的缩放属性。 这适用于旋转工具、 缩放工具、 来源工具、 大小工具 。

### 更新 {#updated-2}

* 查看器: 优化内部结构, 并使用油漆信息。 渲染速度现在要快得多 。
* 查看器:自动隐藏滚动条.
* 主菜单:显示非官方的Phaser帮助中心选项.

### 固定 {#fixed-3}

* 上下文菜单项上的固定无位图图标。
* 查看器:当所有段落崩溃时修正卷轴 。
* 资源包编辑器: 如果启用了旗子, 则添加资源对话框 。
* 从解锁对话框中固定获取许可证按钮 。
* 资源键属性:在选择对话框中修正动画的渲染.
* 场景编辑器: `removeFromDisplayList()`和 `removeFromUpdateList()`没有在 `Phaser.GameObjects.Layer`中出现,跳过它.
* 场景编辑器:修正副本/粘贴层对象.
* 场景编译器:修复"组件-醒"事件,排放预制体性的孩子.
* 场景编译器:当`publicroot`文件出现时,会修正资源包文件url.
* 探长:修复了许多图像查看器.
* [#89](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/89)场景编辑器:打开时记得最后选定的对象.
* 菜单:项目显示鼠标悬浮上的负图标 。
* 菜单:在按钮和类似元素上固定定位.
* 菜单:在鼠标悬浮时修正“ 检查” 图标的颜色 。

## v3.13.0 - 2021年4月2日,纽约 {#v3130---apr-2-2021}

### 已添加 {#added-6}

* 代码编辑器:启用ES模块(exportClass,autoImport设置和代码生成).
* 新的“ public root” 概念。 您可以在工程内配置不同的公共文件夹。 现在根据包含 pack 文件的公共根计算一个 pack 文件的url 。
* 文件视图:突出显示"公有根"文件和容器文件夹.
* 用户组件:组件的**Game对象类型** & **Super class**字段的选项按钮.
* 用户组件:新`UserComponent.(js|ts)`级生成器.
* 用于JavaScript和TypeScript的Webpack项目模板.
* 用于JavaScript和TypeScript的 Parcel项目模板.

### 更新 {#updated-3}

* 更新为Phaser v3.54.0.
* 探长视图:在Dark主题中改进颜色按钮样式.
* 代码生成器: 总是使用类字段。 输入声明中的所有字段。 不再使用构造器中的输入 。
* 默认用户组件文件有 `Behaviors.components` 名称 。
* 替换类型对话框: 组内置类型在段落中: 纹理、 字符串、 形状...
* 默认情况下,新场景中`editorCreate()`作为"创造方法"的名称,用户代码是生成器,在手写`create()`方法内调用`editorCreate()`.
* 用户组件编译器:启用`strict`模式时修正TypeScript错误.
* 组织新工程对话框, 显示新类别: ** Basic **, **Game Demos **, **Parcel **, 和 ** Webpack **.
* 更新了基本项目模板,其行为与网页包和包裹模板相似.

## v3.12.0 - 2021年3月12日 (中文(简体) ). {#v3120---mar-12-2021}

### 已添加 {#added-7}

* 视图:标签区段可折叠.
* 去场景对话框:场景文件由Phaser类型分组.
* 场景编辑器块:当选择了Prefabs tab-section时,预制体片按照Phaser类型进行分组.
* 文件视图:设计和资源部分。

### 更新 {#updated-4}

* 获取最新Phaser v3.53.1.
* 查看器: 改进单元格渲染器。 它默认总是正方形 。
* 资源查看器:改进了BitmapFont单元格渲染器.
* 默认设置暗主题 。

### 修补 {#fixes-2}

* 资源包编辑器:修正重复的上下文菜单.
* 场景编辑器: 使用 Alt 键平面正在光标下选择对象。 固定 。
* 块视图部分: 崩溃部分更改标签的标签高度。 固定 。

## v3.11.0 - 2021年3月5日,纽约 {#v3110---mar-5-2021}

### 已添加 {#added-8}

* 场景编辑器:命令`V`切换选定对象的能见度.
* 场景编辑器:非可见对象在大纲视图标签中以"隐藏"后缀显示.
* 场景编辑器: 更改纹理对话框按类型对项目进行分组.
* 场景编辑器:支持Blocks视图中的SVG资源.
* 场景编辑器:在资源包编辑器中显示打开对象纹理的选项.
* 场景编辑器:允许改变一个对象的纹理帧(`M`).
* [#90](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/90)场景编辑器:在上下文菜单中显示添加对象子菜单.
* [#90](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/90)场景编辑器: 显示添加对象对话框。 您可以用 `A` 快捷键打开它 。
* 场景编辑器:通过按下`Alt+MouseLeftButton`来允许平整场景.
* [#105](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/105)场景编辑器:选择的纹理对话框允许按照类型,资源包或位置对资源进行分组.
* 添加键绑定( `Ctrl+Alt+E`) , 用于命令打开配置的外部编辑器中的输出文件。 此命令可在 Scene 编辑器和用户组件编辑器中获取 。
* 场景编辑器:打开场景文件的新命令(`Ctrl+Alt+O`).
* 场景编辑器:通过视图的标签区块来屏蔽内容过滤.
* 资源包编辑器:允许设定 SVG 资源的规模.
* 动画编辑器:允许按类型,包和位置对块进行分组.
* 查看器: 默认进行高级过滤。 允许匹配不同的单词 。
* 查看器:过滤器并非在每个键上触发.
* [#103](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/103):用鼠标中间按钮关闭编辑器的标签.
* 允许将选中对象添加到新对象列表中。
* 资源包编辑器:块按文件夹分组.
* [#109](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/109):双击文件夹扩展.
* 查看器:默认上下文菜单和三个点按钮.

### 固定 {#fixed-4}

* 场景编辑器: 更改纹理对话框允许双击选择纹理.
* 场景编辑器:`Text.lineSpacing`在代码生成中,当它有默认值(`0`)时会被忽略.
* 场景编辑器:改变纹理时保持原产地不变.
* 场景编辑器:对空对象列表使用`Array<any>`作为类型.
* 场景编辑器:修复文本的`lineSpacing`属性的代码生成.
* 场景编辑器: 修正改变纹理命令 。 D*oesn 不适用于非纹理对象。 选择新图像时会修正( 而不是地图框) 。
* 查看器:当浏览器滚动时,会修正全部的折叠命令.
* 查看器:当浏览器滚动时,修正折叠/扩展分支命令.
* [#112](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/112) 资源包:从图示表跳过帧.

## v3.10.2 - 2021年1月17日 (中文(简体) ). {#v3102---jan-17-2021}

* 场景编辑器:在从JSON数据创建对象时改进错误处理.
* 场景编辑器:在找不到比特玛普Text字体键时修复场景创建.
* 文件视图: 在打开文件的上下文菜单时修正错误, 无需注册编辑器 。
* Go To File 对话框显示文件路径 。
* 命令对话框:突出显示键。
* [#99](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/99)场景编辑器:字符串用户属性允许多行文本.
* 更新为Phaser 3.52.0.

## v3.10.1 - 2021年1月7日 (中文(简体) ). {#v3101---january-7-2021}

### 更新 {#updated-5}

* 主题恢复由 colibri 平台管理。 这不是向后兼容的, 您的保存的主题 id 将在您第一次运行此版本编辑器时被忽略 。
* 将`phasereditor2d.inspector`插件移至`colibri.inspector`.
* 获取 Phaser v3.51.0.

## v3.10.0 - 2020年12月22日 (中文(简体) ). {#v3100---dec-22-2020}

### 已添加 {#added-9}

* 场景编辑器:支持所有图片定向.
* 场景编辑器:位图文本阴影属性.
* 场景编辑器:层对象.

### 更新 {#updated-6}

* 采用Phaser v3.50 号机车.
* 场景编辑器:使用WEBGL来制作场景缩略图.
* 场景编辑器:设置的源指令现在使用Ctrl+Numpad代替Shift+Numpad.
* 项目模板 :
    * 将Sunny Land模板改编为Phaser v3.50.
* 在以 `-dev` 模式运行服务器时, 不要使用 Monaco 编辑器 dev 文件。 使用时, 此选项将修改 `-dev` 选项 。

### 固定 {#fixed-5}

* 编辑器标签上下文菜单错误拼写"关闭到右侧".
* 场景编辑器:验证一个图版的图案组没有外部来源.
* 场景编辑器: 在访问本地文件存储缩略图图像时捕获错误 。

## 3.9.2 - 2020年12月7日,纽约 {#version-392---dec-7-2020}

* 观景器:渲染性能的大规模改进.
* 查看器:在过滤的查看器中修正布局请求.
* 基于查看器的对话框:允许打开一个带有 Enter 键的项目 。
* 场景编辑器:本地浏览器索引DB中的缓存场景文件缩略图. 
* 场景编辑器:更精确地掌握了缩略图生成基于容器的预制体文件.
* 恢复自定义“ 提醒” 信件对话框 。

## 版本3.9.1 - 2020年11月30日 {#version-391---nov-30-2020}

* 检查启动时是否有新版本可用 。
* *Check For Updates * 是主菜单中的新选项。如果有新版本,则显示消息。

## 3.9.0 - 2020年11月24日版本 {#version-390---nov-24-2020}

### 已添加 {#added-10}

* 场景编辑器: 支持新形状对象 :
    * Rectangle.
    * Ellipse.
    * Triangle.
* 场景编辑器:蒂勒马普图层图层 细胞渲染器绘制层.
* 场景编辑器:按类别分类的组内置类型,在Blocks视图中.
* Electron:
    * 允许更改工作空间 。
* 当编辑器在应用模式下运行时,解锁它的主菜单选项.
* 在标题栏和About 对话框中显示许可激活状态 。

### 已修改 {#modified}

* **Reisze TileSprite工具** 被重新命名为 **Resisize Tool**,它也允许修改形状对象的大小。 

### 固定 {#fixed-6}

* 修正在观看器中进行回归图集帧排序.

## 3.8.1 - 2020年11月1日,纽约 {#version-381---nov-1-2020}

### 固定 {#fixed-7}

* 当地图集 URL 指向缺失的文件时, 将图集缩略图生成。

## 3.8.0版本 - 2020年10月30日 {#version-380---oct-30-2020}

### 已添加 {#added-11}

* 用户属性:纹理配置类型显示纹理为搜索-按钮图标.
* 用户属性:动画键类型显示中间帧为搜索-按钮图标.
* 用户属性: 搜索对话框打开时, 资源键( 和衍生) 属性会显示当前值 。
* 场景编辑器的块视图显示内置类型块,准备投放到场景中.
* 文件视图:如果没有其他编辑器可用,则用默认编辑器打开文件.
* 文件视图:在上下文菜单中显示“打开带”选项。
* 启动时打开文件时记得编辑器类型 。
* 用户组件编辑器: 在上下文菜单中完成编译器菜单。 带有打开输出文件的命令 。
* 用户组件编辑器:在大纲视图中显示上下文菜单.
* 场景编辑器:允许在属性字段中写一个表达式.
* 以斜拉图为基础的新阳光土地项目模板.
* 场景编辑器:Tilemap,StaticTilemapLayer和动态TilemapLayer支持.

### 删除 {#removed-1}

* 删除了添加对象对话框。 相反, 您应该使用块视图 。
* 删除旧的黑暗主题 将 Dark Plus 主题重命名为 Dark 。

### 已修改 {#modified-1}

* 提高地图集资源的查看器单元格渲染器的性能.
* 改进蓝色主题中的一些颜色:场景编辑器,按钮和工具栏项目.
* 允许向上传对话框添加更多文件 。
* 场景编辑器:在上下文菜单的编译器部分组编译器命令.
* 场景编辑器:在改变对象时,提高检查器视图更新的性能.

### 修补 {#fixes-3}

* 固定检查干事部分标题的点击区域。
* 当快速编辑对话框激活时修复 `Ctrl+S` 。
* 场景编辑器:在用图示表框架创建的对象上使用图示表名称.
* 场景编辑器: 打开快速编辑器对话框时显示消息, 但还没有生成输出文件 。
* 场景编辑器:在检查器视图的纹理部分修正图像预览的布局.
* 场景编辑器: 修正对翻转对象的选择 。
* 查看器:固定过滤,现在它不会扩展不匹配的母项.
* JavaScript编辑器:修复文件重命名操作处理.

## 3.7.1 - 2020年9月22日,第3版,第3页 {#version-371---sep-22-2020}

### 修补 {#fixes-4}

* 动画编辑器:根据简单的图像文件来修正动画的显示和序列化.

## 3.7.0 - 2020年9月19日版本 {#version-370---sep-19-2020}

### 已添加 {#added-12}

* 场景编辑器: 添加更多用户属性类型 :
    * 纹理配置
    * 动画键
    * 音频键。
    * 资源键
* 场景编辑器:允许更改变量区段所选对象的类型.
* 场景编辑器:允许更改用户属性的类型.
* 资源包编辑器: 添加对脚本资源类型的支持。 要以可预测的顺序加载多个脚本 。

### 已修改 {#modified-2}

* 一些图标更新了 。
* 删除命令被映射到 `Backspace` 键( 除了 `Delete` 的一) 。 它对于 macOS 用户更为友好 。

### 固定 {#fixed-8}

* 查看器:如果鼠标升起事件是来源于查看器外,则忽略它.
* 资源:将图示表框的限度提高到1000。
* 动画编辑器:处理资源缺失错误.
* 场景编辑器: 不排序添加对象对话框的内容 。
* 键:在macOS中,`Command`和`Ctrl`的键作为同一个键处理.
* 代码编辑器:当活动时,`Ctrl+P`键打开Go To File对话框,而不是打印对话框.
* 固定:即使一个对话框打开,场景编辑器也会捕获键命令.

## 2020年9月7日3.6.0版 互联网档案馆的存档,存档日期2013-09-02. {#version-360-sep-7-2020}

### 已添加 {#added-13}

* "动画编辑".

### 固定 {#fixed-9}

* [#71](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/71)文件视图: 修正文件排序, 文件夹先走 。
* 查看器:在选择远端元素时滚动.
* 场景编辑器:更好的场景缩略图生成.
* 查看器视图中的查看器: 与父视图更新查看器大小时, 清除延迟 。

### 已修改 {#modified-3}

* 查看器: 带 `0` 字符串显示图示表格框的标签。 有助于排序 : `001`, `002`,...,`126`.

## 2020年8月19日3.5.0版 互联网档案馆的存档,存档日期2013-09-02. {#version-350-aug-19-2020}

### 已添加 {#added-14}

* 场景编辑器:当多个文件共享同一场景 ID 时显示错误对话框 。
* [#63](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/63)场景编辑器:**Fix重复的场景ID**命令为较新的场景文件指派新的ID.
* 场景编辑器: ** Duplex Scene 文件 ** 命令,可用场景编辑器 > 上下文菜单 > Scene.
* [#65](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/65) 场景编辑器: ** Insert Spaces ** 和 ** Tab Size ** 参数。要将制表符转换为编译器输出中的空格 。
* 场景编辑器:新创建的场景将从最新修改的场景中获得以下参数值: **compilerOutputLanguage**,**compilerInsertSpaces**, **compilerTabSize**, **borderWidth**, **borderHeight**, **borderX**, **borderY**.
* 场景编辑器:潘场景工具.
* 场景编辑器:允许上下移动用户组件.
* 用户组件编辑器: **Insert Spaces **和 **Tab Size **参数.
* 保存视图,编辑器,对话框等所有观众的缩放状态.
* [#59](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/59) 选择将目录排除在项目之外.

### 已修改 {#modified-4}

* [#61](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/61)  Alphabetic 排序查看器内容.
* [#47](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/47) 检查器视图: 清除一个数字字段的内容, 将其重置到默认值 。

### 修补 {#fixes-5}

* 场景编辑器:以`null`作为默认值来修正用户编号属性的序列化.
* 场景编辑器:粘贴容器对象时修正ID生成.
* [#62](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/63)场景编辑器:在纹理为空时修正预制体构造器代码生成.

## 3.4.0 - 2020年8月4日版本 {#version-340---aug-4-2020}

### 已添加 {#added-15}

* 用户组件编辑器.
* 场景编辑器:在Prefabext 一节中,在每个预制体旁边显示一个菜单,以选择所有预制体实例.
* 场景编辑器:添加布尔类型的用户属性.
* 场景编辑器: 添加了编译工程命令, 它汇编了工程的所有可编译文件( 镜像, 组件) 。
* 火山项目模板.

### 删除 {#removed-2}

* **用户输入方法** 参数和 ** 编译器 Prefab 设置 ** 部分。现在您可以在预制体文件的构建器中直接插入代码。
* 在检查器视图中显示图像、地图册框架和图示表框架的大小信息。
* 场景编辑器:纹理部分显示图像大小.
* 场景编辑器: 删除了 Compile scenses 命令。 编译项目命令汇编包括场景在内的所有文件 。
* 飞龙项目模板.

### 已修改 {#modified-5}

* 场景编辑器:对象列表首先作为时间变量创建,如果范围是CLASS或Public,则生成一个字段.
* 场景编辑器:在预制体场景中,大纲视图以透明的方式显示非预制体对象.
* 场景编辑器:在预制体场景中,当预制体场景对象被选中时,可变区段不显示在检查器视图中.
* 场景编辑器:如果选择了容器或者其中的孩子,则在容器中添加新的对象.
* 场景编辑器:在预制体场景中,如果一个对象是容器,则在根对象上添加,否则将创建一个新的容器,以包扎根对象和新添加的对象.
* 检查员视图:各节标题和副标题使用四舍五入的背景。

### 固定 {#fixed-10}

* 场景编辑器: 修正命令以创建带有选定对象的预制体。 新的预制体定位为 `0,0` 。
* 场景编辑器:当场景是预制体时,会修正场景缩略图生成器,并带有包装物体的容器.

## 3.3.1 - 2020年7月15日 {#version-331---july-15-2020}

### 已添加 {#added-16}

* Phaser 3.24.1 支持。

### 固定 {#fixed-11}

* [#52](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/52) 移动带有箭头键的对象不会更新检查器视图中的属性 。
* [#54](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/54) 资源包编辑器:用上下文菜单修正删除项目 删除选项 。
* 在 ** 编译器场景设置中修复资源包文件选择对话框**.
* 文件编辑器在外部编辑器中修改文件时清除历史。

### 版本3.3.0 - 2020年7月1日. {#version-330---july-1-2020}

### 已添加 {#added-17}

* 资源包:允许将 SVG 文件导入为 HTML 图像.
* 资源包:在文件键部分添加一个打开按钮.
* 资源包:在检查部门菜单中显示帮助链接。
* 在输入字段中按 ENDER 时,关闭一些输入对话框(新文件、新工程、重命名文件)。
* **转到文件** 命令`Ctrl+P`。 命令ZZ0XZ。
* 查看器对话框选择带有 ENTER 键的可见(或选中)项目 。
* 过滤查看器:允许按 Up/Down 键,以聚焦过滤文本或查看器.
* 过滤查看器: 显示缩放按钮 。
* 上传对话框:允许丢弃文件 。
* 场景编辑器:选择区域工具.
* 场景编辑器:如果使用 Scale 工具时按下 `Shift` 键,则按比例缩放.
* 场景编辑器: 箭头键命令改变对象的位置。 按 `Shift` 表示 10x。 它尊重坐标值 。
* 场景编辑器: 允许复制/ 贴上跨场景对象 。
* 场景编辑器:检查器视图部分显示一个菜单,并附有帮助项目和相关命令.
* 场景编辑器:在预制体场景中自动创建根容器.
* 场景编辑器:在预制体场景中,非预制体体是透明化的渲染器.
* [#41](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/41)场景编辑器:放大进出按钮.


### 已修改 {#modified-6}

* 改进了检查员查看的资源包文件部分。
* [#44](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/44) 工作台: 如果根文件夹中存在 `index.html` 文件, 则不验证 。

### 固定 {#fixed-12}

* 当顶部空间很少时, 将修改菜单垂直位置 。
* 场景编辑器: 找不到预制体文件时显示消息 。
* 场景编辑器:在未提供初始值时修正用户属性声明.
* [#59](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/59)场景编辑器:编译器在JavaScript输出中跳过字段声明。在Safari中不支持此选项 。
* 场景编辑器:在输出文件被格式化器修改时,将场景编译器代码合并,将标签字符替换为空格.
* 场景编辑器: 点击 Safari 修正鼠标轮 。

## 3.2.0 - 2020年6月14日版本 {#version-320---june-14-2020}

### 已添加 {#added-18}

* [#32](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/32) In-App更新。通过`PhaserEditor2D -update`,服务器下载最新版本,并将旧文件替换为新文件。通过`PhaserEditor2D -download`,服务器下载最新的版本zip,您可以手动安装。
* 预制体的用户属性。 您可以在预制体的用户属性中添加预制体的用户属性, 并更改预制体实例中的值 。
* 场景编辑器:用选中的对象创建一个预制体文件.
* 场景编辑器:新建命令(带有键`Q`),以打开快速编辑器对话框,编辑编译器输出文件.
* 场景编辑器:以 VS 代码打开编译器输出文件。当 IDE 运行于桌面模式时启用 。
* 场景编辑器:替换类型对话框提供了“保留原始纹理”选项,当您将对象形态化为预制体型时使用。
* 场景编辑器:删除生成代码中的额外空白行.
* 主菜单中打开视觉工作室代码命令, 连接到 `Ctrl+Alt+U` 键 。
* 注释对话框(`Ctrl+Alt+Space`),用于在演示文稿或录像中写信息.

### 已修改 {#modified-7}

* 文件视图: 上下文菜单 ** New** 选项不打开 ** 新文件** 对话框。 现在它是带有快捷键的子菜单, 用于创建任何支持的内容类型的新文件 。
* 场景编辑器:翻译和旋转操纵器将整数设定为对象.
* 场景编辑器:在预制体场景中,非预制体对象以透明方式渲染,在"大纲"中查看.
* 场景编辑器:在预制体场景中,如果选中的对象是预制体对象,则不显示检查视图的变量和列表部分.
* 场景编辑器:当在预制体场景中添加新对象时,自动创建容器.
* 场景编辑器:删除场景文件序列化中的冗余`sceneType`属性.

### 固定 {#fixed-13}

* 点击关闭按钮时不要激活编辑器.
* 图像编辑器:注册正确的内容类型协会.
* 摩纳哥编辑器:在模型更改上,如果模型内容与文件内容相同,那么编辑器就不会被标记为脏(未保存).
* 场景编辑器:修正空对象列表的类型推论.
* 预装上传文件的内容类型 。

## 3.1.1 - 2020年5月25日 {#version-311---may-25-2020}

### 固定 {#fixed-14}

* [#33](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/33) 错误的位图Text默认来源 。
* [#32](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/32) 服务器检查是否有新版本可用 。 
* 摩纳哥(代码)编辑器只有在设置了`-enable-advanced-js-editor`旗的情况下才用外部修改来更新内容,现在它总是更新.
* [#37](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/37) TypeScript项目模板首次打开README文件,并附有运行项目的指示. 
* 场景编辑器:如果输出文件在脏(未保存)编辑器中打开,则不编译场景.

## 3.1.0 - 2020年5月24日版本 {#version-310---may-24-2020}

### 已添加 {#added-19}

* 场景编辑器:为督察视图中的色彩属性使用一个色标.
* 场景编辑器: 源代码操纵器。 要选择它, 请按 `O` 或选择上下文菜单或工具栏中的内容, 它也支持容器 。
* 场景编辑器:丁属性.
* 场景编辑器: 转换的两个范围: 局部和全局。 您可以在上下文菜单( Coords - > Global) 中选择它, 默认是局部的 。
* 服务器: 显示有用的欢迎消息 。
* 坚持检查人员视图部分的崩溃状态。

### 删除 {#removed-3}

* TypeScript模板不包括编译器输出文件(`game.js`). 用户在播放前应当先编译项目.

### 已修改 {#modified-8}

* 场景编辑器: **Set Origin To**命令修改对象的起源,但保持其全局位置.
* 将事件目标替换为自定义事件发送器 。

### 固定 {#fixed-15}

* 场景编辑器:当物体是变形容器的子时,修正翻译操纵器.
* 深巢菜单闭合良好.
* 子菜单不与母菜单重叠 。
* [#26](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/26):在Windows中上传文件.
* 场景编辑器: 修复容器预制体实例的选择 。
* 场景编辑器: 在“ 父属性” 部分修正父对话框。 现在它不显示容器预制体实例 。

### 兼容性 {#compatibility}

* Safari 浏览器: 事件目标不作为构建器支持。 我们用自定义事件发送器( colibri.ui. controls. list) 替换它 。

## 3.0.1版本 - 2020年5月16日 {#version-301---may-16-2020}

### 错误修正 {#bug-fixes}

* [#15](https://github.com/PhaserEditor2D/PhaserEditor2D-v3/issues/15): 灰文本在HiDPI屏幕上.
* 场景编辑器:改进对象的选取.
* 场景编辑器:改进了 BitmapText 对象的大纲视图渲染.
* 检查器视图:在标题中隐藏溢出文本。

## 3.0.0版本 - 2020年5月5日 {#version-300---may-5-2020}

[First public release](https://phasereditor2d.com/blog/2020/05/phaser-editor-v3-released-for-the-public-new-online-service-play-phaser-editor-2d)

---
