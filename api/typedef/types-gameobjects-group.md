# Types.GameObjects.Group {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/typedef/types-gameobjects-group)

## GroupCallback {#groupcallback}

### \<static> GroupCallback {#static-groupcallback}

**类型**: function

**所属**: Phaser.Types.GameObjects.Group
> 源码：[src/gameobjects/group/typedefs/GroupCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupCallback.js#L1)  
引入版本：3.0.0

---

## GroupClassTypeConstructor {#groupclasstypeconstructor}

### \<static> GroupClassTypeConstructor {#static-groupclasstypeconstructor}

**类型**: function

**所属**: Phaser.Types.GameObjects.Group
> 源码：[src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupClassTypeConstructor.js#L1)  
引入版本：3.0.0

---

## GroupConfig {#groupconfig}

### \<static> GroupConfig {#static-groupconfig}

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| classType | function | 是 | "Sprite" | 设置 QQlink 选项 Phaser.GameObjects.Group#classType}. |
| 名称 | string | 是 | "''" | 设置 QQLink Phaser.GameObjects.Group#name}. |
| active | boolean | 是 | true | 设定为QQlink Phaser.GameObjects.Group#Action}. |
| maxSize | number | 是 | -1 | 设置 QQlink 选项 Phaser.GameObjects.Group#maxSize}. |
| defaultKey | string | 是 | null | 设置 QQlink 选项 Phaser.GameObjects.Group#defaultKey}. |
| defaultFrame | string \| number | 是 | null | 设置 QQlink 选项 Phaser.GameObjects.Group#defaultFrame}. |
| runChildUpdate | boolean | 是 | false | 设置 QQlink 选项 Phaser.GameObjects.Group#runChildUpdate}. |
| createCallback | [Phaser.Types.GameObjects.Group.GroupCallback](/api/typedef/types-gameobjects-group#groupcallback) | 是 | null | 设置 QQlink 选项 Phaser.GameObjects.Group#createCallback}. |
| removeCallback | [Phaser.Types.GameObjects.Group.GroupCallback](/api/typedef/types-gameobjects-group#groupcallback) | 是 | null | 设置 QQlink 选项 Phaser.GameObjects.Group#removeCallback}. |
| createMultipleCallback | [Phaser.Types.GameObjects.Group.GroupMultipleCreateCallback](/api/typedef/types-gameobjects-group#groupmultiplecreatecallback) | 是 | null | 设置 QQlink 选项 Phaser.GameObjects.Group#createMultipleCallback}. |

**类型**: object

**所属**: Phaser.Types.GameObjects.Group
> 源码：[src/gameobjects/group/typedefs/GroupConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupConfig.js#L1)  
引入版本：3.0.0

---

## GroupCreateConfig {#groupcreateconfig}

### \<static> GroupCreateConfig {#static-groupcreateconfig}


创建对象的总数将

    key.length * frame.length * frameQuantity * (yoyo ? 2 : 1) * (1 + repeat)

如果`max`是非零的,那么创建的总数量不会超过`max`.

`key` 需要。 QQlink 链接 Phaser.GameObjects.Group#defaultKey}没有被使用。

| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| Array.\<string> | 否 |  | 每个新游戏对象的纹理键。 必须为非提供对象创建 。 |
| classType | function | 是 |  | 每个新游戏对象的类. |
| frame | string \| Array.\<string> | number | Array.\<number> | 是 | null | 每个新游戏对象的纹理帧. |
| quantity | number | 是 | false | 要创建的游戏对象数。 如果设定, 则会覆盖 `frameQuantity` 值。 使用 `frameQuantity` 来进行更高级的控制 。 |
| visible | boolean | 是 | true | 每个新游戏对象的可见状态. |
| active | boolean | 是 | true | 每个新游戏对象的活跃状态 。 |
| repeat | number | 是 | 0 | 每个`key`×`frame`组合的次数将*重复*(在第一次组合之后). |
| randomKey | boolean | 是 | false | 随机选择 `key` 。 |
| randomFrame | boolean | 是 | false | 随机选择 `frame` 。 |
| yoyo | boolean | 是 | false | 通过`key`和`frame`向前移动后向后移动,选择键和帧. |
| frameQuantity | number | 是 | 1 | 每一次`frame`的次数应加一个`key`. |
| max | number | 是 | 0 | 创建新游戏对象的最大数量. 0 并非最大. |
| setXY | object | 是 |  | 选项在QQlink Phaser.Actions.SetXY} 中命名 。 |
| setRotation | object | 是 |  | 选项在QQlink Phaser.Actions.SetRotation} 中命名 。 |
| setScale | object | 是 |  | 选项在QQlink Phaser.Actions.SetScale} 中命名 。 |
| setOrigin | object | 是 |  | 选项在QQlink Phaser.Actions.SetOrigin} 中命名 。 |
| setAlpha | object | 是 |  | 选项在QQlink Phaser.Actions.SetAlpha} 中命名 。 |
| setDepth | object | 是 |  | 选项在QQlink Phaser.Actions.SetDepth} 中命名 。 |
| setScrollFactor | object | 是 |  | 选项在QQlink Phaser.Actions.SetScrollFactor} 中命名 。 |
| hitArea | * | 是 |  | 定义游戏对象的命中区域的一种几何形状. |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](/api/typedef/types-input#hitareacallback) | 是 |  | 当游戏对象被交互时要引用的回调 。 |
| gridAlign | false \| [Phaser.Types.Actions.GridAlignConfig](/api/typedef/types-actions#gridalignconfig) | 是 | false | 使用这些设置在网格中调整新的游戏对象 。 |

**类型**: object

**所属**: Phaser.Types.GameObjects.Group
> 源码：[src/gameobjects/group/typedefs/GroupCreateConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupCreateConfig.js#L1)  
引入版本：3.0.0

---

## GroupMultipleCreateCallback {#groupmultiplecreatecallback}

### \<static> GroupMultipleCreateCallback {#static-groupmultiplecreatecallback}

**类型**: function

**所属**: Phaser.Types.GameObjects.Group
> 源码：[src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/group/typedefs/GroupMultipleCreateCallback.js#L1)  
引入版本：3.0.0

---

---
