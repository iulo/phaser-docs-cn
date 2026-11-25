# Core {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/constant/core)

### width {#width}

#### width: number, string {#width-number-string}


**说明:**

底画布的宽度,以像素表示.


> 源码：[src/core/Config.js#L55](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L55)  



### height {#height}

#### height: number, string {#height-number-string}


**说明:**

底画布的高度,以像素表示.


> 源码：[src/core/Config.js#L60](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L60)  



### zoom {#zoom}

#### zoom: [Phaser.Scale.ZoomType](/api/typedef/scale#zoomtype), number {#zoom-phaserscalezoomtype-number}


**说明:**

缩放因子, 缩放管理器使用 。


> 源码：[src/core/Config.js#L65](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L65)  



### parent {#parent}

#### parent: * {#parent-1}


**说明:**

将渲染器创建的画布注入到父 DOM 元素中。


> 源码：[src/core/Config.js#L70](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L70)  



### scaleMode {#scaleMode}

#### scaleMode: [Phaser.Scale.ScaleModeType](/api/typedef/scale#scalemodetype) {#scalemode-phaserscalescalemodetype}


**说明:**

缩放管理器使用的缩放模式。 默认为零, 而不是缩放 。


> 源码：[src/core/Config.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L75)  



### expandParent {#expandParent}

#### expandParent: boolean {#expandparent-boolean}


**说明:**

是否允许比例管理器调整母公司的CSS高度属性为100%?


> 源码：[src/core/Config.js#L80](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L80)  



### autoRound {#autoRound}

#### autoRound: boolean {#autoround-boolean}


**说明:**

自动绕过画布的显示和样式大小。 这样做有助于在低功率设备中实现性能 。


> 源码：[src/core/Config.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L85)  



### autoCenter {#autoCenter}

#### autoCenter: [Phaser.Scale.CenterType](/api/typedef/scale#centertype) {#autocenter-phaserscalecentertype}


**说明:**

自动将画布放在父目录中吗 ?


> 源码：[src/core/Config.js#L90](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L90)  



### resizeInterval {#resizeInterval}

#### resizeInterval: number {#resizeinterval-number}


**说明:**

检查浏览器大小是否改变之前, 需要花多少 ms ?


> 源码：[src/core/Config.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L95)  



### fullscreenTarget {#fullscreenTarget}

#### fullscreenTarget: HTMLElement, string {#fullscreentarget-htmlelement-string}


**说明:**

将发送到全屏幕模式的 DOM 元素, 或其 `id`。 如果未定义的 Phaser 将创建自己的隐藏, 并在进入全屏幕模式时将画布插入其中 。


> 源码：[src/core/Config.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L100)  



### minWidth {#minWidth}

#### minWidth: number {#minwidth-number}


**说明:**

最小宽度, 以像素表示, 画布将缩放到最小值。 0 值表示没有最小值 。


> 源码：[src/core/Config.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L105)  



### maxWidth {#maxWidth}

#### maxWidth: number {#maxwidth-number}


**说明:**

最大宽度, 以像素表示, 画布将放大到最大。 数值为 0 表示没有最大值 。


> 源码：[src/core/Config.js#L110](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L110)  



### minHeight {#minHeight}

#### minHeight: number {#minheight-number}


**说明:**

最小高度, 以像素计, 画布会缩小到最小高度。 0 值意味着没有最小值 。


> 源码：[src/core/Config.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L115)  



### maxHeight {#maxHeight}

#### maxHeight: number {#maxheight-number}


**说明:**

最大高度, 以像素计, 画布将放大到最大。 0 值表示没有最大值 。


> 源码：[src/core/Config.js#L120](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L120)  



### snapWidth {#snapWidth}

#### snapWidth: number {#snapwidth-number}


**说明:**

当缩放管理器重新调整大小时, 水平值可以按下画布。 0 值意味着不按下 。


> 源码：[src/core/Config.js#L125](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L125)  



### snapHeight {#snapHeight}

#### snapHeight: number {#snapheight-number}


**说明:**

当缩放管理器重新调整大小时, 垂直的量可以按下画布。 0 值意味着不按下 。


> 源码：[src/core/Config.js#L130](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L130)  



### renderType {#renderType}

#### renderType: number {#rendertype-number}


**说明:**

强制 Phaser使用特定的渲染器。可以是 `CONST.CANVAS`, `CONST.WEBGL`, `CONST.HEADLESS` 或 `CONST.AUTO`( 默认)


> 源码：[src/core/Config.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L135)  



### canvas {#canvas}

#### canvas: HTMLCanvasElement {#canvas-htmlcanvaselement}


**说明:**

强制 Phaser使用自己的 Canvas 元素而不是创建一个.


> 源码：[src/core/Config.js#L140](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L140)  



### context {#context}

#### context: CanvasRenderingContext2D, WebGLRenderingContext {#context-canvasrenderingcontext2d-webglrenderingcontext}


**说明:**

强制 Phaser 使用自己的 Canvas 上下文, 而不是创建上下文 。


> 源码：[src/core/Config.js#L145](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L145)  



### canvasStyle {#canvasStyle}

#### canvasStyle: string {#canvasstyle-string}


**说明:**

由渲染器创建的画布对象上设定的可选 CSS 属性 。


> 源码：[src/core/Config.js#L150](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L150)  



### customEnvironment {#customEnvironment}

#### customEnvironment: boolean {#customenvironment-boolean}


**说明:**

Phaser是否在自定义( 非本地网络) 环境中运行? 如果是的话, 请设置为 `true` 以跳过内部特性检测 。 如果 `true` , 则 `renderType` 无法作为 `AUTO` 保存 。


> 源码：[src/core/Config.js#L155](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L155)  



### sceneConfig {#sceneConfig}

#### sceneConfig: object {#sceneconfig-object}


**说明:**

默认场景配置对象 。


> 源码：[src/core/Config.js#L160](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L160)  



### seed {#seed}

#### seed: Array.\<string> {#seed-arraystring}


**说明:**

随机数据生成器将使用的种子。 如果不给定, 则使用基于时间的动态种子 。


> 源码：[src/core/Config.js#L165](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L165)  



### gameTitle {#gameTitle}

#### gameTitle: string {#gametitle-string}


**说明:**

游戏标题.


> 源码：[src/core/Config.js#L172](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L172)  



### gameURL {#gameURL}

#### gameURL: string {#gameurl-string}


**说明:**

游戏的URL.


> 源码：[src/core/Config.js#L177](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L177)  



### gameVersion {#gameVersion}

#### gameVersion: string {#gameversion-string}


**说明:**

游戏的版本.


> 源码：[src/core/Config.js#L182](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L182)  



### autoFocus {#autoFocus}

#### autoFocus: boolean {#autofocus-boolean}


**说明:**

如果 `true` 窗口将自动被赋予焦点, 并关注任何未来的鼠标下移事件 。


> 源码：[src/core/Config.js#L187](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L187)  



### stableSort {#stableSort}

#### stableSort: number, boolean {#stablesort-number-boolean}


**说明:**

`false`或`0`=使用内置的SturnSort(旧浏览器需要),`true`或`1`=Rely上ES2019 Array.sort是稳定的(仅现代浏览器),或`-1`=根据浏览器检查来尝试和自动确定(不能保证工作,在小心的侧面有错误).


> 源码：[src/core/Config.js#L192](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L192)  



### domCreateContainer {#domCreateContainer}

#### domCreateContainer: boolean {#domcreatecontainer-boolean}


**说明:**

游戏是否要创建 div 元素来作为 DOM 容器 ? 只有在您使用 DOM 元素对象时才能启用。 如果您使用此特性, 您必须提供父对象 。


> 源码：[src/core/Config.js#L206](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L206)  



### domPointerEvents {#domPointerEvents}

#### domPointerEvents: string {#dompointerevents-string}


**说明:**

DOM容器上的默认 `pointerEvents`属性设置.


> 源码：[src/core/Config.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L211)  



### inputKeyboard {#inputKeyboard}

#### inputKeyboard: boolean {#inputkeyboard-boolean}


**说明:**

启用键盘插件。 在不需要键盘输入的游戏中可以禁用 。


> 源码：[src/core/Config.js#L218](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L218)  



### inputKeyboardEventTarget {#inputKeyboardEventTarget}

#### inputKeyboardEventTarget: * {#inputkeyboardeventtarget}


**说明:**

DOM 目标可以打开键盘事件。 如果未指定默认为 `window` 。


> 源码：[src/core/Config.js#L223](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L223)  



### inputKeyboardCapture {#inputKeyboardCapture}

#### inputKeyboardCapture: Array.\<number> {#inputkeyboardcapture-arraynumber}


**说明:**

`preventDefault` 将调用此数组中每个有密钥代码的非修改密钥。默认情况下,该密钥为空。


> 源码：[src/core/Config.js#L228](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L228)  



### inputMouse {#inputMouse}

#### inputMouse: boolean, object {#inputmouse-boolean-object}


**说明:**

启用鼠标插件。 在不需要鼠标输入的游戏中可以禁用此插件 。


> 源码：[src/core/Config.js#L233](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L233)  



### inputMouseEventTarget {#inputMouseEventTarget}

#### inputMouseEventTarget: * {#inputmouseeventtarget}


**说明:**

打开鼠标事件 DOM 目标。 如果未指定, 默认为游戏布景 。


> 源码：[src/core/Config.js#L238](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L238)  



### inputMousePreventDefaultDown {#inputMousePreventDefaultDown}

#### inputMousePreventDefaultDown: boolean {#inputmousepreventdefaultdown-boolean}


**说明:**

是否应该`mousedown` DOM事件 已经`preventDefault`呼叫他们?


> 源码：[src/core/Config.js#L243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L243)  



### inputMousePreventDefaultUp {#inputMousePreventDefaultUp}

#### inputMousePreventDefaultUp: boolean {#inputmousepreventdefaultup-boolean}


**说明:**

是否应该`mouseup` DOM事件 已经`preventDefault`呼叫他们?


> 源码：[src/core/Config.js#L248](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L248)  



### inputMousePreventDefaultMove {#inputMousePreventDefaultMove}

#### inputMousePreventDefaultMove: boolean {#inputmousepreventdefaultmove-boolean}


**说明:**

是否应该`mousemove` DOM事件 已经`preventDefault`呼叫他们?


> 源码：[src/core/Config.js#L253](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L253)  



### inputMousePreventDefaultWheel {#inputMousePreventDefaultWheel}

#### inputMousePreventDefaultWheel: boolean {#inputmousepreventdefaultwheel-boolean}


**说明:**

是否应该`wheel` DOM事件 已经`preventDefault`呼叫他们?


> 源码：[src/core/Config.js#L258](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L258)  



### inputTouch {#inputTouch}

#### inputTouch: boolean {#inputtouch-boolean}


**说明:**

启用触摸插件。 可以在不需要触摸输入的游戏中禁用 。


> 源码：[src/core/Config.js#L263](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L263)  



### inputTouchEventTarget {#inputTouchEventTarget}

#### inputTouchEventTarget: * {#inputtoucheventtarget}


**说明:**

DOM 目标可以监听触摸事件。 如果未指定, 默认为游戏布景 。


> 源码：[src/core/Config.js#L268](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L268)  



### inputTouchCapture {#inputTouchCapture}

#### inputTouchCapture: boolean {#inputtouchcapture-boolean}


**说明:**

触摸事件应该被抓住吗?


> 源码：[src/core/Config.js#L273](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L273)  



### inputActivePointers {#inputActivePointers}

#### inputActivePointers: number {#inputactivepointers-number}


**说明:**

默认创建的指针对象数。 在只鼠标或非多触摸游戏中, 您可以将此保留为 1 。


> 源码：[src/core/Config.js#L278](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L278)  



### inputSmoothFactor {#inputSmoothFactor}

#### inputSmoothFactor: number {#inputsmoothfactor-number}


**说明:**

指针运动时要应用的平滑因子。 见 [Phaser.Input.Pointer#smoothFactor](/api/class/input-pointer#smoothFactor) 。


> 源码：[src/core/Config.js#L283](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L283)  



### inputWindowEvents {#inputWindowEvents}

#### inputWindowEvents: boolean {#inputwindowevents-boolean}


**说明:**

Phaser是否要聆听窗口上的输入事件? 如果您禁用此选项, “ POPER_ UP_ OUTSIDE” 这样的事件将不再开火 。


> 源码：[src/core/Config.js#L288](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L288)  



### inputGamepad {#inputGamepad}

#### inputGamepad: boolean {#inputgamepad-boolean}


**说明:**

启用 Gamepad 插件。 在不需要 gamepad 输入的游戏中, 可能会禁用此插件 。


> 源码：[src/core/Config.js#L293](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L293)  



### inputGamepadEventTarget {#inputGamepadEventTarget}

#### inputGamepadEventTarget: * {#inputgamepadeventtarget}


**说明:**

DOM 目标可以监听游戏板事件。 如果未指定默认为 `window` 。


> 源码：[src/core/Config.js#L298](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L298)  



### disableContextMenu {#disableContextMenu}

#### disableContextMenu: boolean {#disablecontextmenu-boolean}


**说明:**

设定为 `true` 以禁用右键上下文菜单 。


> 源码：[src/core/Config.js#L303](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L303)  



### audio {#audio}

#### audio: [Phaser.Types.Core.AudioConfig](/api/typedef/types-core#audioconfig) {#audio-phasertypescoreaudioconfig}


**说明:**

音频配置对象 。


> 源码：[src/core/Config.js#L308](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L308)  



### hideBanner {#hideBanner}

#### hideBanner: boolean {#hidebanner-boolean}


**说明:**

不要将横幅线写到控制台.log。请参看 `Phaser.Types.Core.BannerConfig` 的详情 。


> 源码：[src/core/Config.js#L315](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L315)  



### hidePhaser {#hidePhaser}

#### hidePhaser: boolean {#hidephaser-boolean}


**说明:**

欧米特Phaser的名字和版本来自旗下.


> 源码：[src/core/Config.js#L320](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L320)  



### bannerTextColor {#bannerTextColor}

#### bannerTextColor: string {#bannertextcolor-string}


**说明:**

旗语文字的颜色.


> 源码：[src/core/Config.js#L325](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L325)  



### bannerBackgroundColor {#bannerBackgroundColor}

#### bannerBackgroundColor: Array.\<string> {#bannerbackgroundcolor-arraystring}


**说明:**

旗下背景颜色.


> 源码：[src/core/Config.js#L330](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L330)  



### fps {#fps}

#### fps: [Phaser.Types.Core.FPSConfig](/api/typedef/types-core#fpsconfig) {#fps-phasertypescorefpsconfig}


**说明:**

框架速率配置对象, 由时间步类解析 。


> 源码：[src/core/Config.js#L340](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L340)  



### autoMobileTextures {#autoMobileTextures}

#### autoMobileTextures: boolean {#automobiletextures-boolean}


**说明:**

如果检测到iOS或Android, 请自动限制WebGL每批使用1个纹理。 这可以帮助某些设备的性能 。


> 源码：[src/core/Config.js#L349](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L349)  



### antialias {#antialias}

#### antialias: boolean {#antialias-boolean}


**说明:**

`true`设定为ZZ时,WebGL使用线性插图绘制缩放或旋转纹理,使外观平滑. `false`设定为ZG2Z时,WebGL使用近邻插图,使外观更加简洁. `false`还禁止游戏画布本身的反异化,如果浏览器支持,则在游戏画布缩放时.


> 源码：[src/core/Config.js#L354](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L354)  



### antialiasGL {#antialiasGL}

#### antialiasGL: boolean {#antialiasgl-boolean}


**说明:**

设置 `antialias` 属性, 当创建 WebGL 上下文时。 设置此值不会影响随后创建的纹理或画布样式属性 。


> 源码：[src/core/Config.js#L359](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L359)  



### mipmapFilter {#mipmapFilter}

#### mipmapFilter: string {#mipmapfilter-string}


**说明:**

设置缩写 magFilter 用于创建时 WebGL 纹理。 除非您想要创建 mipmaps , 请不要设置。 设置为以下之一 : “ NearEST ” 、 “ LINEAR ” 、 “ NEAREST_ MIPMAP_ NEAREST ” , “ NEARE斯特_ MIPMAp_ LINEAR ”, 或 “ LINEAR_ MIPMAPR_ LINEAR” 。


> 源码：[src/core/Config.js#L364](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L364)  



### mipmapRegeneration {#mipmapRegeneration}

#### mipmapRegeneration: boolean {#mipmapregeneration-boolean}


**说明:**

- 是否为帧布设重生 mipmaps 。 如果这是假的, 帧布设者不会使用 mipmaps 。 如果是真假, 帧布设人员会使用 `mipmapFilter`Z 设置, 如果重画, 则重生 mipmas 。 这会影响过滤器和动态图案。 Mipmap 生成成本昂贵( 每条纹理10微秒或更多秒), 所以请小心此设置 。


> 源码：[src/core/Config.js#L369](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L369)  



### desynchronized {#desynchronized}

#### desynchronized: boolean {#desynchronized-boolean}


**说明:**

当设定为 `true` 时, 它将为 2D 和 WebGL 创建一个非同步上下文。 详情请参见 [https://developers.google.com/web/updates/2019/05/desynchronized](https://developers.google.com/web/updates/2019/05/desynchronized) 。


> 源码：[src/core/Config.js#L374](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L374)  



### roundPixels {#roundPixels}

#### roundPixels: boolean {#roundpixels-boolean}


**说明:**

仅在整装位置绘制基于纹理的游戏对象。没有纹理的游戏对象,如图形,忽略了此属性。


> 源码：[src/core/Config.js#L379](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L379)  



### selfShadow {#selfShadow}

#### selfShadow: boolean {#selfshadow-boolean}


**说明:**

在有照明的纹理物体上,这可以使基于扩散图的自我阴影化。


> 源码：[src/core/Config.js#L384](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L384)  



### pathDetailThreshold {#pathDetailThreshold}

#### pathDetailThreshold: number {#pathdetailthreshold-number}


**说明:**

在图形对象的 WebGL 渲染器中将点组合成单一路径的门槛值。在图形对象级别上,可以覆盖此参数 。


> 源码：[src/core/Config.js#L389](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L389)  



### pixelArt {#pixelArt}

#### pixelArt: boolean {#pixelart-boolean}


**说明:**

防止像素艺术在缩放时变得模糊。 它将保持简洁( 切换到 WebGL 使用最近邻域过滤器模式自动创建纹理的渲染器。启用时,此选项也会设置 `antialias` 财务报告和已审计财务报表 `antialiasGL` 改为: `false` 财务报告和已审计财务报表 `roundPixels` 改为: `true`.


> 源码：[src/core/Config.js#L394](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L394)  



### smoothPixelArt {#smoothPixelArt}

#### smoothPixelArt: boolean {#smoothpixelart-boolean}


**说明:**

WebGL 仅此设定 。 `antialias` 真实的和 `pixelArt` 。基于纹理的游戏对象使用特殊遮蔽设置,以保存块状像素,但平滑像素之间的边缘。这只有在对象被放大时才可见;否则, `antialias` 简单点


> 源码：[src/core/Config.js#L406](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L406)  



### transparent {#transparent}

#### transparent: boolean {#transparent-boolean}


**说明:**

游戏画布是否具有透明的背景 。


> 源码：[src/core/Config.js#L418](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L418)  



### clearBeforeRender {#clearBeforeRender}

#### clearBeforeRender: boolean {#clearbeforerender-boolean}


**说明:**

游戏画布是否在每个渲染框架之间被清除。 如果您有全屏背景图像或游戏对象, 您可以禁用此内容 。


> 源码：[src/core/Config.js#L423](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L423)  



### preserveDrawingBuffer {#preserveDrawingBuffer}

#### preserveDrawingBuffer: boolean {#preservedrawingbuffer-boolean}


**说明:**

如果数值是真实的,则WebGL缓冲将不会被清除,并且将在作者清除或覆盖之前保留其数值。


> 源码：[src/core/Config.js#L428](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L428)  



### premultipliedAlpha {#premultipliedAlpha}

#### premultipliedAlpha: boolean {#premultipliedalpha-boolean}


**说明:**

在WebGL模式中,设定绘图缓冲器包含带有预多倍倍α的颜色.


> 源码：[src/core/Config.js#L433](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L433)  



### skipUnreadyShaders {#skipUnreadyShaders}

#### skipUnreadyShaders: boolean {#skipunreadyshaders-boolean}


**说明:**

阴影编译过程中的向导在支持的地方进行平行的阴影编译。 请求尚未准备好的阴影对象将不会被绘制。 这将防止结巴, 但可能导致对象的“ 流行” , 除非您使用前触控策略 。


> 源码：[src/core/Config.js#L438](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L438)  



### failIfMajorPerformanceCaveat {#failIfMajorPerformanceCaveat}

#### failIfMajorPerformanceCaveat: boolean {#failifmajorperformancecaveat-boolean}


**说明:**

如果浏览器判断性能,则让它中止创建 WebGL 上下文,这是不可接受的。


> 源码：[src/core/Config.js#L443](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L443)  



### powerPreference {#powerPreference}

#### powerPreference: string {#powerpreference-string}


**说明:**

"高性能","低功率"或"默认",向浏览器提示游戏可能使用多少设备功率.


> 源码：[src/core/Config.js#L448](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L448)  



### batchSize {#batchSize}

#### batchSize: number {#batchsize-number}


**说明:**

默认的 WebGL 批次大小。 代表可添加到单个批次中的 _quads_ 数目 。


> 源码：[src/core/Config.js#L453](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L453)  



### maxTextures {#maxTextures}

#### maxTextures: number {#maxtextures-number}


**说明:**

WebGL模式下,此模式设置了GPU纹理的最大使用数量。默认的 -1将使用所有可用的单位。 WebGL1 spec表示所有浏览器应提供最小的8个.


> 源码：[src/core/Config.js#L458](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L458)  



### maxLights {#maxLights}

#### maxLights: number {#maxlights-number}


**说明:**

光机座单相机范围内允许可见的灯光最大数量.


> 源码：[src/core/Config.js#L463](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L463)  



### renderNodes {#renderNodes}

#### renderNodes: Object.\<[Phaser.Types.Core.RenderNodesConfig](/api/typedef/types-core#rendernodesconfig)> {#rendernodes-objectphasertypescorerendernodesconfig}


**说明:**

将自定义 Render 节点地图添加到 WebGL 渲染器中。 数值将被添加到 Render Node Manager 中, 以密钥作为名称 。


> 源码：[src/core/Config.js#L468](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L468)  



### backgroundColor {#backgroundColor}

#### backgroundColor: [Phaser.Display.Color](/api/namespace/display-color) {#backgroundcolor-phaserdisplaycolor}


**说明:**

游戏画布的背景颜色。 默认为黑色。 如果 `transparent` 设置为 `true` , 此值会被忽略 。


> 源码：[src/core/Config.js#L475](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L475)  



### preBoot {#preBoot}

#### preBoot: [Phaser.Types.Core.BootCallback](/api/typedef/types-core#bootcallback) {#preboot-phasertypescorebootcallback}


**说明:**

Phaser靴前呼叫。 用于初始化任何与Phaser无关的, 用于Phaser 启动时可能需要的 。


> 源码：[src/core/Config.js#L486](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L486)  



### postBoot {#postBoot}

#### postBoot: [Phaser.Types.Core.BootCallback](/api/typedef/types-core#bootcallback) {#postboot-phasertypescorebootcallback}


**说明:**

启动序列结束时运行的函数。 此时, 所有游戏系统都已经启动, 插件已经装入 。


> 源码：[src/core/Config.js#L491](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L491)  



### physics {#physics}

#### physics: [Phaser.Types.Core.PhysicsConfig](/api/typedef/types-core#physicsconfig) {#physics-phasertypescorephysicsconfig}


**说明:**

物理配置对象 。


> 源码：[src/core/Config.js#L496](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L496)  



### defaultPhysicsSystem {#defaultPhysicsSystem}

#### defaultPhysicsSystem: boolean, string {#defaultphysicssystem-boolean-string}


**说明:**

默认物理系统。 它将为每个场景启动。 要么是“ arcade” , 要么是“ matter ” 。


> 源码：[src/core/Config.js#L501](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L501)  



### loaderBaseURL {#loaderBaseURL}

#### loaderBaseURL: string {#loaderbaseurl-string}


**说明:**

用于解析给加载器的路径的 URL。 例如 : “ [http://labs.phaser.io/assets/](http://labs.phaser.io/assets/) ” 。


> 源码：[src/core/Config.js#L506](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L506)  



### loaderPath {#loaderPath}

#### loaderPath: string {#loaderpath-string}


**说明:**

用于解析给加载器的相对路径的 URL 路径。 例如 : “ 图像/ 粘贴 / ” 。


> 源码：[src/core/Config.js#L511](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L511)  



### loaderMaxParallelDownloads {#loaderMaxParallelDownloads}

#### loaderMaxParallelDownloads: number {#loadermaxparalleldownloads-number}


**说明:**

装入器将尝试平行下载文件的最大数量 。 默认为32 或 6 在 Android 上并行连接受到更多限制 。


> 源码：[src/core/Config.js#L516](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L516)  



### loaderCrossOrigin {#loaderCrossOrigin}

#### loaderCrossOrigin: string, undefined {#loadercrossorigin-string-undefined}


**说明:**

匿名,用户证明,或 `undefined`。如果你没有提出跨源请求, 请留此作为 `undefined`。见 QQlink [https://developer.mozilla.org/en-US/docs/Web/HTML/CORS_settings_attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/CORS_settings_attributes)}.


> 源码：[src/core/Config.js#L521](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L521)  



### loaderResponseType {#loaderResponseType}

#### loaderResponseType: string {#loaderresponsetype-string}


**说明:**

XHR请求的响应类型,如`blob`,`text`等.


> 源码：[src/core/Config.js#L526](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L526)  



### loaderAsync {#loaderAsync}

#### loaderAsync: boolean {#loaderasync-boolean}


**说明:**

XHR请求是否使用同步?


> 源码：[src/core/Config.js#L531](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L531)  



### loaderUser {#loaderUser}

#### loaderUser: string {#loaderuser-string}


**说明:**

XHR 的所有请求的可选用户名 。


> 源码：[src/core/Config.js#L536](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L536)  



### loaderPassword {#loaderPassword}

#### loaderPassword: string {#loaderpassword-string}


**说明:**

XHR 的所有请求都可以选择密码 。


> 源码：[src/core/Config.js#L541](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L541)  



### loaderTimeout {#loaderTimeout}

#### loaderTimeout: number {#loadertimeout-number}


**说明:**

可选 XHR 超时值, 以毫秒计.


> 源码：[src/core/Config.js#L546](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L546)  



### loaderMaxRetries {#loaderMaxRetries}

#### loaderMaxRetries: number {#loadermaxretries-number}


**说明:**

如果文件负载失败, 重试的次数 。


> 源码：[src/core/Config.js#L551](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L551)  



### loaderWithCredentials {#loaderWithCredentials}

#### loaderWithCredentials: boolean {#loaderwithcredentials-boolean}


**说明:**

备选XHR withCredentials值.


> 源码：[src/core/Config.js#L556](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L556)  



### loaderImageLoadType {#loaderImageLoadType}

#### loaderImageLoadType: string {#loaderimageloadtype-string}


**说明:**

图像的可选负载类型, `XHR`是默认的,或者 `HTMLImageElement`是轻量级方式的.


> 源码：[src/core/Config.js#L561](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L561)  



### loaderLocalScheme {#loaderLocalScheme}

#### loaderLocalScheme: Array.\<string> {#loaderlocalscheme-arraystring}


**说明:**

装入器认为属于“ 本地” 文件的一系列方案。 默认为: `[ 'file://', 'capacitor://' ]` 。


> 源码：[src/core/Config.js#L569](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L569)  



### glowQuality {#glowQuality}

#### glowQuality: number {#glowquality-number}


**说明:**

Glow 过滤器的质量( 默认为 10)


> 源码：[src/core/Config.js#L574](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L574)  



### glowDistance {#glowDistance}

#### glowDistance: number {#glowdistance-number}


**说明:**

格洛过滤器的距离( 默认为 10)


> 源码：[src/core/Config.js#L579](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L579)  



### installGlobalPlugins {#installGlobalPlugins}

#### installGlobalPlugins: any {#installglobalplugins-any}


**说明:**

一组要安装的全局插件 。


> 源码：[src/core/Config.js#L602](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L602)  



### installScenePlugins {#installScenePlugins}

#### installScenePlugins: any {#installsceneplugins-any}


**说明:**

要安装的场景级别插件阵列 。


> 源码：[src/core/Config.js#L607](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L607)  



### defaultPlugins {#defaultPlugins}

#### defaultPlugins: any {#defaultplugins-any}


**说明:**

插件安装到每个场景(除了CoreScene和Global).


> 源码：[src/core/Config.js#L638](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L638)  



### defaultImage {#defaultImage}

#### defaultImage: string {#defaultimage-string}


**说明:**

一个基数64编码的PNG,将用作默认的空白纹理.


> 源码：[src/core/Config.js#L646](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L646)  



### missingImage {#missingImage}

#### missingImage: string {#missingimage-string}


**说明:**

一个基码64的PNG,当指定了缺失或未加载的纹理时,它将作为默认纹理使用.


> 源码：[src/core/Config.js#L651](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L651)  



### whiteImage {#whiteImage}

#### whiteImage: string {#whiteimage-string}


**说明:**

一个基码64的PNG作为默认的固态白色纹理使用,这个小的4x4白色图像由Phaser内部用于彩色游戏对象和涂料.


> 源码：[src/core/Config.js#L656](https://github.com/phaserjs/phaser/blob/v4.1.0/src/core/Config.js#L656)

---
