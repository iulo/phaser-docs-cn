# Types.Core {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-core)

## AudioConfig {#audioconfig}

### \<static> AudioConfig {#static-audioconfig}


包含各种声音设置的配置对象。

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| disableWebAudio | boolean | 是 | false | 使用 HTML5 音频代替 Web Audio 。 |
| context | AudioContext | 是 |  | 已有的Web音频上下文 。 |
| noAudio | boolean | 是 | false | 禁用所有音频输出 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/AudioConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/AudioConfig.js#L1)  
引入版本：3.0.0

---

## BannerConfig {#bannerconfig}

### \<static> BannerConfig {#static-bannerconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| hidePhaser | boolean | 是 | false | 欧米特Phaser的名字和版本来自旗下. |
| text | string | 是 | "'#ffffff'" | 旗语文字的颜色. |
| background | Array.\<string> | 是 |  | 旗下背景颜色. |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/BannerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/BannerConfig.js#L1)  
引入版本：3.0.0

---

## BootCallback {#bootcallback}

### \<static> BootCallback {#static-bootcallback}

**类型**: function

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/BootCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/BootCallback.js#L1)  
引入版本：3.0.0

---

## CallbacksConfig {#callbacksconfig}

### \<static> CallbacksConfig {#static-callbacksconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| preBoot | [Phaser.Types.Core.BootCallback](/api/typedef/types-core#bootcallback) | 是 | "Phaser.Types.Core.NOOP" | 启动序列开始时运行的函数 。 |
| postBoot | [Phaser.Types.Core.BootCallback](/api/typedef/types-core#bootcallback) | 是 | "Phaser.Types.Core.NOOP" | 启动序列结束时运行的函数。 此时, 所有游戏系统都已经启动, 插件已经装入 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/CallbacksConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/CallbacksConfig.js#L1)  
引入版本：3.0.0

---

## DOMContainerConfig {#domcontainerconfig}

### \<static> DOMContainerConfig {#static-domcontainerconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| createContainer | boolean | 是 | false | 游戏是否要创建 div 元素来作为 DOM 容器 ? 只有在您使用 DOM 元素对象时才能启用。 如果您使用此特性, 您必须提供父对象 。 |
| behindCanvas | boolean | 是 | false | 创建的 DOM 容器( 如果 `dom.createContainer` 是真的) 是放在游戏画布的后面( 真实的) 还是放在上面( 假的, 默认的) ? |
| pointerEvents | string | 是 | "'none'" | DOM容器上的默认 `pointerEvents`属性设置. |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/DOMContainerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/DOMContainerConfig.js#L1)  
引入版本：3.12.0

---

## FPSConfig {#fpsconfig}

### \<static> FPSConfig {#static-fpsconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| min | number | 是 | 5 | 最小可接受渲染率, 以每秒帧计 。 |
| target | number | 是 | 60 | 最佳渲染率, 以帧每秒为单位。 这不会强制执行 fps 率, 它只是告诉 Phaser 哪些率被认为是此游戏的最佳 。 |
| limit | number | 是 | 0 | 执行 fps 的游戏步骤运行的速率限制, 不论浏览器频率如何. 0 表示“ 无限制 ” 。 这只可用于人为降低帧率以获得反转效果。 浏览器将永远无法比显示刷新率更快更新游戏 。 |
| forceSetTimeOut | boolean | 是 | false | 使用setTimeout代替requestAnimationFrame来运行游戏循环. |
| deltaHistory | number | 是 | 10 | 从这连续许多帧间隔计算平均帧三角形. |
| panicMax | number | 是 | 120 | 时间步数的帧数在我们再次信任三角洲值之前算数. |
| smoothStep | boolean | 是 | true | 在游戏更新时应用三角洲平滑来帮助避免悬崖? |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/FPSConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/FPSConfig.js#L1)  
引入版本：3.0.0

---

## GameConfig {#gameconfig}

### \<static> GameConfig {#static-gameconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number \| string | 是 | 1024 | 游戏的宽度,在游戏像素中. |
| height | number \| string | 是 | 768 | 游戏的高度,在游戏像素中. |
| zoom | number | 是 | 1 | 游戏画布上应用的简单尺度. 2为双尺寸,0.5为半尺寸等. |
| 类型 | number | 是 | "CONST.AUTO" | 哪个制造器可以使用 Phaser.AUTO, Phaser.CANVAS, Phaser.HEADLESS,或 ,或 , Phaser.WEBGL. AUTO选择WEBGL(如果有的话),否则CANVAS. |
| stableSort | number \| boolean | 是 | -1 | `true`或`1`=使用内置的SturnSort(旧浏览器需要),`false`或`0`=Rely上ES2019 Array.sort是稳定的(仅现代浏览器),或`-1`=根据浏览器检查来尝试和自动确定(不能保证工作,在小心的侧面有错误). |
| parent | HTMLElement \| string | null | 是 |  | 包含游戏画布的 DOM 元素, 或它的 `id`。 如果未定义, 或命名的元素不存在, 游戏画布将附加到文档正文中。 如果 `null` 将不使用父版, 您负责将画布添加到 dom 中 。 |
| canvas | HTMLCanvasElement | 是 | null | 提供您自己的 Canvas 元素用于 Phaser 而不是创建 。 |
| canvasStyle | string | 是 | null | CSS样式适用于游戏画布,而不是Sprivers默认样式. |
| customEnvironment | boolean | 是 | false | Phaser是否在自定义( 非本地网络) 环境中运行? 如果是的话, 请设置为 `true` 以跳过内部特性检测 。 如果 `true` , 则 `renderType` 无法作为 `AUTO` 保存 。 |
| context | CanvasRenderingContext2D | 是 |  | 提供您自己的 Canvas 上下文供 Phaser 使用, 而不是创建一个 。 |
| scene | [Phaser.Types.Scenes.SceneType](/api/typedef/types-scenes#scenetype) \| Array.\<[Phaser.Types.Scenes.SceneType](/api/typedef/types-scenes#scenetype)> | 是 | null | 游戏中要添加的场景或场景。 如果给出了多个场景, 则开始第一个场景; 其余场景只有在有 `{ active: true }`时才会开始。 请参看 `Phaser.Scenes.SceneManager#add`中的 `sceneConfig` 参数 。 |
| seed | Array.\<string> | 是 |  | 种子为随机数生成器. |
| title | string | 是 | "''" | 游戏标题,在浏览器控制台显示. |
| url | string | 是 | "'https://phaser.io'" | 游戏的URL。 在浏览器控制台中显示 。 |
| version | string | 是 | "''" | 游戏版本,在浏览器控制台上显示. |
| autoFocus | boolean | 是 | true | 当游戏靴子时自动调用窗口. 焦点() 。 通常, 如果游戏处于单独的框架, 需要捕捉输入事件 。 |
| input | boolean \| [Phaser.Types.Core.InputConfig](/api/typedef/types-core#inputconfig) | 是 |  | 输入配置,或`false`来禁用所有游戏输入. |
| disableContextMenu | boolean | 是 | false | 禁用浏览器默认的“ 文本菜单” 事件( 通常是由右键鼠标点击触发 ) 。 |
| banner | boolean \| [Phaser.Types.Core.BannerConfig](/api/typedef/types-core#bannerconfig) | 是 | false | 游戏开始时浏览器控制台打印的横幅配置. |
| dom | [Phaser.Types.Core.DOMContainerConfig](/api/typedef/types-core#domcontainerconfig) | 是 |  | DOM 容器配置对象 。 |
| fps | [Phaser.Types.Core.FPSConfig](/api/typedef/types-core#fpsconfig) | 是 |  | 游戏循环配置. |
| render | [Phaser.Types.Core.RenderConfig](/api/typedef/types-core#renderconfig) | 是 |  | 游戏渲染器配置. |
| callbacks | [Phaser.Types.Core.CallbacksConfig](/api/typedef/types-core#callbacksconfig) | 是 |  | 游戏启动前或启动后可选的回调运行. |
| loader | [Phaser.Types.Core.LoaderConfig](/api/typedef/types-core#loaderconfig) | 是 |  | 装弹机配置 。 |
| images | [Phaser.Types.Core.ImagesConfig](/api/typedef/types-core#imagesconfig) | 是 |  | 图像配置 。 |
| physics | [Phaser.Types.Core.PhysicsConfig](/api/typedef/types-core#physicsconfig) | 是 |  | 物理配置. |
| plugins | [Phaser.Types.Core.PluginObject](/api/typedef/types-core#pluginobject) \| Array.\<[Phaser.Types.Core.PluginObjectItem](/api/typedef/types-core#pluginobjectitem)> | 是 |  | 要安装的插件 。 |
| scale | [Phaser.Types.Core.ScaleConfig](/api/typedef/types-core#scaleconfig) | 是 |  | 缩放管理器配置 。 |
| audio | [Phaser.Types.Core.AudioConfig](/api/typedef/types-core#audioconfig) | 是 |  | 音频配置对象 。 |
| backgroundColor | string \| number | 是 | "0x000000" | 游戏画布的背景颜色, 默认为黑色 。 |
| antialias | boolean | 是 | true | `true`设定为ZZ时,WebGL使用线性插图绘制缩放或旋转纹理,使外观平滑. `false`设定为ZG2Z时,WebGL使用近邻插图,使外观更加简洁. `false`还禁止游戏画布本身的反异化,如果浏览器支持,则在游戏画布缩放时. |
| antialiasGL | boolean | 是 | true | 设置 `antialias` 属性, 当创建 WebGL 上下文时。 设置此值不会影响随后创建的纹理或画布样式属性 。 |
| desynchronized | boolean | 是 | false | 当设定为 `true` 时, 它将为 2D 和 WebGL 创建一个非同步上下文。 详情请参见 https://developers.google.com/web/updates/2019/05/desynchronized 。 |
| pixelArt | boolean | 是 | false | 设置 `antialias` 以假表示, `roundPixels` 以真表示。 这是像素艺术游戏的最佳设定 。 |
| smoothPixelArt | boolean | 是 | false | WebGL 仅此设定 。 `antialias` 真实的和 `pixelArt` 。基于纹理的游戏对象使用特殊遮蔽设置,以保存块状像素,但平滑像素之间的边缘。这只有在对象被放大时才可见;否则, `antialias` 简单点 |
| roundPixels | boolean | 是 | false | 仅在整装位置绘制基于纹理的游戏对象。没有纹理的游戏对象,如图形,忽略了此属性。 |
| selfShadow | boolean | 是 | false | 在有照明的纹理物体上,这可以使基于扩散图的自我阴影化。 |
| pathDetailThreshold | number | 是 | 1 | 在图形对象的 WebGL 渲染器中将点组合成单一路径的门槛值。在图形对象级别上,可以覆盖此参数 。 |
| transparent | boolean | 是 | false | 游戏画布是否透明。 布尔表示画布是否包含一个α 通道。 如果设置为虚假, 浏览器现在知道背景总是不透明, 它可以加快绘制透明的内容和图像 。 |
| clearBeforeRender | boolean | 是 | true | 游戏画布是否在每个渲染框架之间被清除 。 |
| preserveDrawingBuffer | boolean | 是 | false | 如果数值是真实的,则WebGL缓冲将不会被清除,并且将在作者清除或覆盖之前保留其数值。 |
| premultipliedAlpha | boolean | 是 | true | 在WebGL模式中,绘图缓冲器包含带有预多倍倍的α的颜色. |
| skipUnreadyShaders | boolean | 是 | false | 阴影编译过程中的向导在支持的地方进行平行的阴影编译。 请求尚未准备好的阴影对象将不会被绘制。 这将防止结巴, 但可能导致对象的“ 流行” , 除非您使用前触控策略 。 |
| failIfMajorPerformanceCaveat | boolean | 是 | false | 如果浏览器判断性能,则让它中止创建 WebGL 上下文,这是不可接受的。 |
| powerPreference | string | 是 | "'default'" | "高性能","低功率"或"默认",向浏览器提示游戏可能使用多少设备功率. |
| batchSize | number | 是 | 16384 | 默认 WebGL 批量大小。 表示可添加到单个批量中的 _quads_ 数目 。 |
| maxLights | number | 是 | 10 | 光机座单相机范围内允许可见的灯光最大数量. |
| maxTextures | number | 是 | -1 | WebGL模式下,此模式设置了GPU纹理的最大使用数量。默认的 -1将使用所有可用的单位。 WebGL1 spec表示所有浏览器应提供最小的8个. |
| mipmapFilter | string | 是 | "'LINEAR'" | 用于创建 WebGL纹理的 mipmap magFilter 。 |
| mipmapRegeneration | boolean | 是 | false | 是否为帧布重新生成缩写 。 |
| autoMobileTextures | boolean | 是 | true | 如果检测到iOS或Android, 请自动限制WebGL每批使用1个纹理。 这可以帮助某些设备的性能 。 |
| expandParent | boolean | 是 | true | 是否允许比例表管理器调整母体和/或文档机构的CSS高度属性为100%? |
| mode | [Phaser.Scale.ScaleModeType](/api/typedef/scale#scalemodetype) | 是 | "Phaser.Scale.ScaleModes.NONE" | 缩放模式 。 |
| min | WidthHeight | 是 |  | 帆布最小宽度和高度可以缩小到. |
| max | WidthHeight | 是 |  | 画布的最大宽度可以扩大至. |
| autoRound | boolean | 是 | false | 自动绕过画布的显示和样式大小。 这样做有助于在低功率设备中实现性能 。 |
| autoCenter | [Phaser.Scale.CenterType](/api/typedef/scale#centertype) | 是 | "Phaser.Scale.Center.NO_CENTER" | 自动将画布放在父目录中吗 ? |
| resizeInterval | number | 是 | 500 | 检查浏览器大小是否改变之前, 需要花多少 ms ? |
| fullscreenTarget | HTMLElement \| string | 是 |  | 将发送到全屏幕模式的 DOM 元素, 或其 `id`。 如果未定义的 Phaser 将创建自己的隐藏, 并在进入全屏幕模式时将画布插入其中 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/GameConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/GameConfig.js#L1)  
引入版本：3.0.0

---

## GamepadInputConfig {#gamepadinputconfig}

### \<static> GamepadInputConfig {#static-gamepadinputconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | * | 是 | "window" | Gamepad 管理器在其中监听游戏板输入事件. |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/GamepadInputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/GamepadInputConfig.js#L1)  
引入版本：3.0.0

---

## ImagesConfig {#imagesconfig}

### \<static> ImagesConfig {#static-imagesconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| default | string \| undefined | null | 是 | 一个 Base64 编码的图像文件, 用作“ 默认” 纹理 。 |
| missing | string \| undefined | null | 是 | 一个 Base64 编码的图像文件, 用作“ 缺失” 纹理 。 |
| white | string \| undefined | null | 是 | 一个基础64编码的图像文件,用作“ 白色” 纹理 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/ImagesConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/ImagesConfig.js#L1)  
引入版本：3.0.0

---

## InputConfig {#inputconfig}

### \<static> InputConfig {#static-inputconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| keyboard | boolean \| [Phaser.Types.Core.KeyboardInputConfig](/api/typedef/types-core#keyboardinputconfig) | 是 | true | 键盘输入配置. `true`使用默认配置,`false`则禁用键盘输入. |
| mouse | boolean \| [Phaser.Types.Core.MouseInputConfig](/api/typedef/types-core#mouseinputconfig) | 是 | true | 鼠标输入配置. `true`使用默认配置, `false`则禁用鼠标输入. |
| touch | boolean \| [Phaser.Types.Core.TouchInputConfig](/api/typedef/types-core#touchinputconfig) | 是 | true | 触摸输入配置. `true`使用默认配置,`false`禁用触摸输入. |
| gamepad | boolean \| [Phaser.Types.Core.GamepadInputConfig](/api/typedef/types-core#gamepadinputconfig) | 是 | false | Gamepad 输入配置. `true` 启用 gamepad 输入. |
| activePointers | number | 是 | 1 | 触点数最大值。 请参看 QQlink Phaser.Input.InputManager# pointers } |
| smoothFactor | number | 是 | 0 | 指针运动时应用的平滑因子。 请见 QQlink Phaser.Input.Pointer# smoothFactor} 。 |
| windowEvents | boolean | 是 | true | Phaser是否要聆听窗口上的输入事件? 如果您禁用此选项, “ POPER_ UP_ OUTSIDE” 这样的事件将不再开火 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/InputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/InputConfig.js#L1)  
引入版本：3.0.0

---

## KeyboardInputConfig {#keyboardinputconfig}

### \<static> KeyboardInputConfig {#static-keyboardinputconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | * | 是 | "window" | 键盘管理器在其中监听键盘输入事件. |
| capture | Array.\<number> | 是 |  | `preventDefault` 将调用此数组中每个未修改的密钥, 默认为空 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/KeyboardInputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/KeyboardInputConfig.js#L1)  
引入版本：3.0.0

---

## LoaderConfig {#loaderconfig}

### \<static> LoaderConfig {#static-loaderconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| baseURL | string | 是 |  | 用于解析加载器路径的 URL。 例如 : “ http://labs.phaser.io/assets/'. ” |
| path | string | 是 |  | 用于解析给加载器的相对路径的 URL 路径。 例如 : “ 图像/ 粘贴 / ” 。 |
| maxParallelDownloads | number | 是 | 32 | 装载器将立即开始装载的最大资源数量 。 |
| crossOrigin | string \| undefined | 是 |  | “匿名”、“用户证书”或“`undefined`”。如果你没有提出跨源请求,请将此保留为“`undefined`”。见“XQlink https://developer.mozilla.org/en-US/docs/Web/HTML/CORS_settings_attributes}.”。 |
| responseType | string | 是 |  | XHR请求的响应类型,如`blob`,`text`等. |
| async | boolean | 是 | true | XHR请求是否使用同步? |
| user | string | 是 |  | XHR 的所有请求的可选用户名 。 |
| password | string | 是 |  | XHR 的所有请求都可以选择密码 。 |
| timeout | number | 是 | 0 | 可选 XHR 超时值, 以毫秒计. |
| localScheme | Array.\<string> | 是 |  | 装入器认为属于“ 本地” 文件的可选方案。 如果未指定, 默认为: `[ 'file://', 'capacitor://' ]` 。 |
| withCredentials | boolean | 是 | false | 备选XHR withCredentials值. |
| imageLoadType | string | 是 | "'XHR'" | 图像的可选负载类型, `XHR`是默认的,或者 `HTMLImageElement`是轻量级方式的. |
| maxRetries | number | 是 | 2 | 如果文件负载失败, 重试的次数 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/LoaderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/LoaderConfig.js#L1)  
引入版本：3.0.0

---

## MouseInputConfig {#mouseinputconfig}

### \<static> MouseInputConfig {#static-mouseinputconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | * | 是 | null | 鼠标管理器在其中监听鼠标输入事件。 默认是游戏布 。 |
| preventDefaultDown | boolean | 是 | true | 如果`true`,DOM `mousedown`事件将设置`preventDefault`. |
| preventDefaultUp | boolean | 是 | true | 如果`true`,DOM `mouseup`事件将设置`preventDefault`. |
| preventDefaultMove | boolean | 是 | true | 如果`true`,DOM `mousemove`事件将设置`preventDefault`. |
| preventDefaultWheel | boolean | 是 | true | 如果`true`,DOM `wheel`事件将设置`preventDefault`. |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/MouseInputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/MouseInputConfig.js#L1)  
引入版本：3.0.0

---

## NOOP {#noop}

### \<static> NOOP {#static-noop}


这种回调类型是完全空的,是无操作的.

**类型**: function

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/NOOP.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/NOOP.js#L1)  
引入版本：3.0.0

---

## PhysicsConfig {#physicsconfig}

### \<static> PhysicsConfig {#static-physicsconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| default | string | 是 | 默认物理系统。 它会为每个场景启动。 Phaser 提供“ arcade ”、“ 影响 ” 和“ matter ” 。 |
| arcade | [Phaser.Types.Physics.Arcade.ArcadeWorldConfig](/api/typedef/types-physics-arcade#arcadeworldconfig) | 是 | 拱门物理配置. |
| matter | [Phaser.Types.Physics.Matter.MatterWorldConfig](/api/typedef/types-physics-matter#matterworldconfig) | 是 | 物质物理配置. |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/PhysicsConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/PhysicsConfig.js#L1)  
引入版本：3.0.0

---

## PluginObject {#pluginobject}

### \<static> PluginObject {#static-pluginobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| global | Array.\<[Phaser.Types.Core.PluginObjectItem](/api/typedef/types-core#pluginobjectitem)> | 是 | 要安装的全局插件 。 |
| scene | Array.\<[Phaser.Types.Core.PluginObjectItem](/api/typedef/types-core#pluginobjectitem)> | 是 | 要安装的场景插件 。 |
| default | Array.\<string> | 是 | 默认的场景插件集( names) 。 |
| defaultMerge | Array.\<string> | 是 | 插件到 * 添加 * 到默认的场景插件集 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/PluginObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/PluginObject.js#L1)  
引入版本：3.8.0

---

## PluginObjectItem {#pluginobjectitem}

### \<static> PluginObjectItem {#static-pluginobjectitem}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 是 | 在插件管理器中识别插件的密钥 。 |
| plugin | * | 是 | 插件本身。 通常为类/ 构造器 。 |
| start | boolean | 是 | 是否自动启动插件 。 |
| systemKey | string | 是 | 对于场景插件,请在此键下添加该插件到场景的系统对象(`this.sys.KEY`,从场景). |
| sceneKey | string | 是 | 对于场景插件,请在此密钥下添加该插件到场景对象(`this.KEY`,从场景). |
| mapping | string | 是 | 如果要将此插件注入 Scene 系统, 这就是所用的属性密钥映射 。 |
| data | * | 是 | 任意数据传递到插件的 init() 方法 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/PluginObjectItem.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/PluginObjectItem.js#L1)  
引入版本：3.8.0

---

## RenderConfig {#renderconfig}

### \<static> RenderConfig {#static-renderconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| antialias | boolean | 是 | true | `true`设定为ZZ时,WebGL使用线性插图绘制缩放或旋转纹理,使外观平滑. `false`设定为ZG2Z时,WebGL使用近邻插图,使外观更加简洁. `false`还禁止游戏画布本身的反异化,如果浏览器支持,则在游戏画布缩放时. |
| antialiasGL | boolean | 是 | true | 设置 `antialias` 属性, 当创建 WebGL 上下文时。 设置此值不会影响随后创建的纹理或画布样式属性 。 |
| desynchronized | boolean | 是 | false | 当设定为 `true` 时, 它将为 2D 和 WebGL 创建一个非同步上下文。 详情请参见 https://developers.google.com/web/updates/2019/05/desynchronized 。 |
| pixelArt | boolean | 是 | false | 设置 `antialias` 以假表示, `roundPixels` 以真表示。 这是像素艺术游戏的最佳设定 。 |
| smoothPixelArt | boolean | 是 | false | WebGL 仅此设定 。 `antialias` 真实的和 `pixelArt` 。基于纹理的游戏对象使用特殊遮蔽设置,以保存块状像素,但平滑像素之间的边缘。这只有在对象被放大时才可见;否则, `antialias` 简单点 |
| roundPixels | boolean | 是 | false | 仅在整装位置绘制基于纹理的游戏对象。没有纹理的游戏对象,如图形,忽略了此属性。 |
| selfShadow | boolean | 是 | false | 在有照明的纹理物体上,这可以使基于扩散图的自我阴影化。 |
| pathDetailThreshold | number | 是 | 1 | 在图形对象的 WebGL 渲染器中将点组合成单一路径的门槛值。在图形对象级别上,可以覆盖此参数 。 |
| transparent | boolean | 是 | false | 游戏画布是否透明。 布尔表示画布是否包含一个α 通道。 如果设置为虚假, 浏览器现在知道背景总是不透明, 它可以加快绘制透明的内容和图像 。 |
| clearBeforeRender | boolean | 是 | true | 游戏画布是否在每个渲染框架之间被清除 。 |
| preserveDrawingBuffer | boolean | 是 | false | 如果数值是真实的,则WebGL缓冲将不会被清除,并且将在作者清除或覆盖之前保留其数值。 |
| premultipliedAlpha | boolean | 是 | true | 在WebGL模式中,绘图缓冲器包含带有预多倍倍的α的颜色. |
| skipUnreadyShaders | boolean | 是 | false | 阴影编译过程中的向导在支持的地方进行平行的阴影编译。 请求尚未准备好的阴影对象将不会被绘制。 这将防止结巴, 但可能导致对象的“ 流行” , 除非您使用前触控策略 。 |
| failIfMajorPerformanceCaveat | boolean | 是 | false | 如果浏览器判断性能,则让它中止创建 WebGL 上下文,这是不可接受的。 |
| powerPreference | string | 是 | "'default'" | "高性能","低功率"或"默认",向浏览器提示游戏可能使用多少设备功率. |
| batchSize | number | 是 | 16384 | 默认 WebGL 批量大小。 表示可添加到单个批量中的 _quads_ 数目 。 |
| maxLights | number | 是 | 10 | 光机座单相机范围内允许可见的灯光最大数量. |
| maxTextures | number | 是 | -1 | WebGL模式下,此模式设置了GPU纹理的最大使用数量。默认的 -1将使用所有可用的单位。 WebGL1 spec表示所有浏览器应提供最小的8个. |
| mipmapFilter | string | 是 | "''" | 创建 WebGL 纹理时使用的 MIPmap magFilter 。 除非您想要创建 MIPmaps 。 请不要设置 。 设置为以下之一 : “ NEAREST ” 、 “ LINEST_ MIPMAP_ NEAREST” 、 “ LinEAR_ MIPMAp_ NEARET ” 、 “ NEARET_ MIPMAF_ NEAREP” 、 “ NEAREST_ MIPMEP_ LINEAR ” 或 “ LINEAR_ MIAPPMAP_ LINEER ” 。 |
| mipmapRegeneration | boolean | 是 | false | 是否为帧布设重生 mipmaps 。 如果这是假的, 帧布设者不会使用 mipmaps 。 如果是真假, 帧布设人员会使用 `mipmapFilter`Z 设置, 如果重画, 则重生 mipmas 。 这会影响过滤器和动态图案。 Mipmap 生成成本昂贵( 每条纹理10微秒或更多秒), 所以请小心此设置 。 |
| autoMobileTextures | boolean | 是 | true | 如果检测到iOS或Android, 请自动限制WebGL每批使用1个纹理。 这可以帮助某些设备的性能 。 |
| renderNodes | Object.\<[Phaser.Types.Core.RenderNodesConfig](/api/typedef/types-core#rendernodesconfig)> | 是 |  | 将自定义 Render 节点地图添加到 WebGL 渲染器中。 数值将被添加到 Render Node Manager 中, 以密钥作为名称 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/RenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/RenderConfig.js#L1)  
引入版本：3.0.0

---

## RenderNodesConfig {#rendernodesconfig}

### \<static> RenderNodesConfig {#static-rendernodesconfig}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 是 | 用作RenderNode名称的密钥 。 |
| function | * | 是 | 朗德节点本身可以运行. |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/RenderNodesConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/RenderNodesConfig.js#L1)  
引入版本：4.0.0

---

## ScaleConfig {#scaleconfig}

### \<static> ScaleConfig {#static-scaleconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number \| string | 是 | 1024 | 游戏的基宽度。 可以是整数或字符串 : “ 100% ” 。 如果字符串已经设置了大小的父元素, 则它只能工作 。 |
| height | number \| string | 是 | 768 | 游戏的基部高度。 可以是一个整数或字符串 : “ 100% ” 。 如果一个字符串, 只有在您设置了有大小的父元素时才会有效 。 |
| zoom | [Phaser.Scale.ZoomType](/api/typedef/scale#zoomtype) \| number | 是 | 1 | 游戏画布的缩放值 。 |
| parent | HTMLElement \| string | 是 |  | 包含游戏画布的 DOM 元素, 或它的 `id`。 如果未定义, 或命名元素不存在, 游戏画布直接插入到文档正文中。 如果 `null` 将不使用父版, 您负责将画布添加到您的环境中 。 |
| expandParent | boolean | 是 | true | 是否允许比例表管理器调整母体和/或文档机构的CSS高度属性为100%? |
| mode | [Phaser.Scale.ScaleModeType](/api/typedef/scale#scalemodetype) | 是 | "Phaser.Scale.ScaleModes.NONE" | 缩放模式 。 |
| min | WidthHeight | 是 |  | 帆布最小宽度和高度可以缩小到. |
| max | WidthHeight | 是 |  | 画布的最大宽度可以扩大至. |
| snap | WidthHeight | 是 |  | 设置缩放管理器在调整画布大小时使用的抓取值。 详情请参见 `ScaleManager.setSnap` 。 |
| autoRound | boolean | 是 | false | 自动绕过画布的显示和样式大小。 这样做有助于在低功率设备中实现性能 。 |
| autoCenter | [Phaser.Scale.CenterType](/api/typedef/scale#centertype) | 是 | "Phaser.Scale.Center.NO_CENTER" | 自动将画布放在父目录中吗 ? |
| resizeInterval | number | 是 | 500 | 检查浏览器大小是否改变之前, 需要花多少 ms ? |
| fullscreenTarget | HTMLElement \| string | 是 |  | 将发送到全屏幕模式的 DOM 元素, 或其 `id`。 如果未定义的 Phaser 将创建自己的隐藏, 并在进入全屏幕模式时将画布插入其中 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/ScaleConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/ScaleConfig.js#L1)  
引入版本：3.16.0

---

## TimeStepCallback {#timestepcallback}

### \<static> TimeStepCallback {#static-timestepcallback}

**类型**: function

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/TimeStepCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/TimeStepCallback.js#L1)  
引入版本：3.0.0

---

## TouchInputConfig {#touchinputconfig}

### \<static> TouchInputConfig {#static-touchinputconfig}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| target | * | 是 | null | 触摸管理器在听触摸输入事件的地方,默认是游戏画布. |
| capture | boolean | 是 | true | 触摸输入事件是否使用 preventDefault () 调用它们 。 |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/TouchInputConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/TouchInputConfig.js#L1)  
引入版本：3.0.0

---

## WidthHeight {#widthheight}

### \<static> WidthHeight {#static-widthheight}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| width | number | 是 | 0 | 宽度。 |
| height | number | 是 | 0 | 高处. |

**类型**: object

**Member of**: Phaser.Types.Core
> 源码：[src/core/typedefs/WidthHeight.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/typedefs/WidthHeight.js#L1)  
引入版本：3.16.0

---

---
