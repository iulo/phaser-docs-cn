# Types.Input {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-input)

## EventData {#eventdata}

### \<static> EventData {#static-eventdata}


一个 Phaser 输入事件数据对象.

此对象将传递给已注册的事件的听众, 并允许您停止任何进一步的传播 。

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| cancelled | boolean | 是 | false | 本次事件取消状态 。 |
| stopPropagation | function | 否 |  | 调用这种方法来阻止事件在事件链中的任何进一步传递. |

**类型**: object

**Member of**: Phaser.Types.Input
> 源码：[src/input/typedefs/EventData.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/EventData.js#L7)  
引入版本：3.15.1

---

## HitAreaCallback {#hitareacallback}

### \<static> HitAreaCallback {#static-hitareacallback}

**类型**: function

**Member of**: Phaser.Types.Input
> 源码：[src/input/typedefs/HitAreaCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/HitAreaCallback.js#L1)  
引入版本：3.0.0

---

## InputConfiguration {#inputconfiguration}

### \<static> InputConfiguration {#static-inputconfiguration}

| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| hitArea | any | 是 |  | 要用作 Hit 区域的对象/ 形状。 如果不给出, 将尝试根据纹理框架创建矩形 。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 |  | 用于确定指针是否在 Hit 区域形状内的回调 。 |
| draggable | boolean | 是 | false | 如果 `true` 交互式对象将被设定为可拖动并释放拖动事件 。 |
| dropZone | boolean | 是 | false | 如果 `true` 交互式对象将被设定为可拖动对象的跳动区 。 |
| useHandCursor | boolean | 是 | false | 如果 `true` 交互式对象会在指针上方设置 `pointer`手游标。 这是设置 `cursor: 'pointer'` 的短剪 。 |
| cursor | string | 是 |  | 当光标覆盖此交互对象时使用的 CSS 字符串 。 |
| pixelPerfect | boolean | 是 | false | 如果 `true` 将设置一个像素完美的函数, 用于命中区域调用。 只能使用基于图像纹理的游戏对象, 而不是 Render 纹理 。 |
| alphaTolerance | number | 是 | 1 | 如果设置了 `pixelPerfect`, 则此值为调用时使用的α容忍阈值。 255 的值将只匹配完全不透明像素 。 |

**类型**: object

**Member of**: Phaser.Types.Input
> 源码：[src/input/typedefs/InputConfiguration.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/InputConfiguration.js#L1)  
引入版本：3.0.0

---

## InputPluginContainer {#inputplugincontainer}

### \<static> InputPluginContainer {#static-inputplugincontainer}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 此插件在输入插件缓存中独有的名称 。 |
| plugin | function | 否 | 要存储的插件。 应该是源对象, 而不是即时对象 。 |
| mapping | string | 是 | 如果要将此插件注入输入插件, 则此为所用的属性密钥映射 。 |

**类型**: object

**Member of**: Phaser.Types.Input
> 源码：[src/input/typedefs/InputPluginContainer.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/InputPluginContainer.js#L1)  
引入版本：3.0.0

---

## InteractiveObject {#interactiveobject}

### \<static> InteractiveObject {#static-interactiveobject}

| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gameObject | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 此交互对象所约束的游戏对象 。 |
| enabled | boolean | 否 | 是否当前启用了输入事件的互动对象 ? |
| draggable | boolean | 否 | 交互对象可拖动吗 ? 启用 `InputPlugin.setDraggable` 。 |
| dropZone | boolean | 否 | 此交互式对象是否为拖放目标区? 当对象创建时设定 。 |
| cursor | boolean \| string | 否 | 此交互式对象是否在结束时更改光标( 通过 css) ? (只使用桌面) |
| target | [Phaser.GameObjects.GameObject](/api/class/gameobjects-gameobject) | 否 | 可拖动的交互式对象的可选的投放目标 。 |
| camera | [Phaser.Cameras.Scene2D.Camera](/api/class/cameras-scene2d-camera) | 否 | 正在测试的最新相机针对此交互对象 。 |
| hitArea | any | 否 | 此交互对象的命中区域。 通常是一个几何形状, 如矩形或圆形 。 |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 否 | 命中区形状将用来进行所有命中测试的“ 封装” 检查回调 。 |
| hitAreaDebug | [Phaser.GameObjects.Shape](/api/class/gameobjects-shape) | 否 | 如果启用此交互式对象以调试, 则通过 `InputPlugin.enableDebug` 然后,这个属性保持它的调试形状。 |
| customHitArea | boolean | 否 | 用于此交互对象的 hitArea 是基于纹理大小( 假) , 还是自定义形状 ? (真) |
| localX | number | 否 | 指针与此对象交互的x坐标,相对于游戏对象的左上方位置. |
| localY | number | 否 | 指针与此对象交互的y坐标,相对于游戏对象的左上方位置. |
| dragState | 0 \| 1 | 2 | 否 | 此交互对象的当前拖曳状态. 0 = 不被拖曳, 1 = 被选中拖曳, 或 2 = 被积极拖曳 。 |
| dragStartX | number | 否 | 拖曳开始时拥有此交互对象的游戏对象的x坐标 。 |
| dragStartY | number | 否 | 拖曳开始时拥有此交互式对象的游戏对象的 y 坐标 。 |
| dragStartXGlobal | number | 否 | 指针开始拖动此交互对象的x坐标 。 |
| dragStartYGlobal | number | 否 | 指针开始拖动此交互对象的 Y 坐标 。 |
| dragX | number | 否 | 正在拖动此交互对象的 x 坐标 。 |
| dragY | number | 否 | 正在拖动此交互对象的 y 坐标 。 |

**类型**: object

**Member of**: Phaser.Types.Input
> 源码：[src/input/typedefs/InteractiveObject.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/input/typedefs/InteractiveObject.js#L1)  
引入版本：3.0.0

---

---
