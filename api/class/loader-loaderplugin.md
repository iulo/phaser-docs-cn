# LoaderPlugin {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/loader-loaderplugin)

装入器处理所有外部内容, 如图像、 声音、 纹理图集和数据文件。 您通常会通过 S`this.load` 在您的场景中与之交互。 Scenes 拥有一个 `preload` 方法, 它总是在 Scenes `create` 方法之前被调用, 允许您预先装入该场景可能需要的资产 。

如果您从 `Scene.preload` 以外的任何 `this.load` 方法调用, 您需要通过调用 `Loader.start()` 来启动装入器。 它只在 Scene 预装时自动启动 。

加载器使用标签加载(如音频元素)和XHR的组合,并提供进度和完成事件。文件默认同时加载。并行连接的数量可以在游戏配置中控制。

一旦装入器开始加载, 您仍然可以添加文件。 这些文件可以被加载器事件、 装入的文件类型( 如包文件) 或其他外部事件所注入。 只要装入器没有完成仅仅添加新文件, 运行时, 就可以确保它被添加到当前队列中 。

每个场景都有自己加载器的实例,它们被绑定在创建它们的场景。 但是, 加载器加载的资产被放置到全局游戏级别缓存中。 例如, 加载一个 XML 文件会将该文件放置在`Game.cache.xml` 中, 该文件可以从游戏中的每一场景中访问, 不管谁负责加载它。 纹理也是一样。 一个场景加载的纹理会立即提供给游戏中的其他所有场景 。

装入器使用自定义文件类型工作。 这些存储在文件类型管理器中, 即时将它们注入装入器中。 您可以通过扩展文件或多文件类创建自定义文件类型。 请查看这些文件的更多细节 。

**构造函数**

`new LoaderPlugin(scene)`

**参数**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| scene | [Phaser.Scene](/api/class/scene) | 否 | 拥有这个装入器实例的场景 。 |

---


**作用域**: static


**继承**

> [Phaser.Events.EventEmitter](/api/class/events-eventemitter)  



> 源码：[src/loader/LoaderPlugin.js#L19](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L19)  
引入版本：3.0.0

## 继承的方法 {#inherited-methods}


**From [Phaser.Events.EventEmitter](/api/class/events-eventemitter):**


 - [addListener](/api/class/events-eventemitter#addListener)
 - [emit](/api/class/events-eventemitter#emit)
 - [eventNames](/api/class/events-eventemitter#eventNames)
 - [listenerCount](/api/class/events-eventemitter#listenerCount)
 - [listeners](/api/class/events-eventemitter#listeners)
 - [off](/api/class/events-eventemitter#off)
 - [on](/api/class/events-eventemitter#on)
 - [once](/api/class/events-eventemitter#once)
 - [removeAllListeners](/api/class/events-eventemitter#removeAllListeners)
 - [removeListener](/api/class/events-eventemitter#removeListener)




---

## 公开方法 {#public-methods}

### addFile {#addFile}

#### \<instance> addFile(file) {#instance-addfilefile}


**说明:**

将文件或文件数组添加到负载队列中。

文件必须是 `Phaser.Loader.File` 实例, 或扩展它的一个类。 装入器将检查文件所用的密钥不会与加载器、 飞行队列或目标缓存中的任何其他密钥发生冲突。 如果允许的话, 则将文件添加到待决列表中, 准备开始装入。 或者, 如果装入已经开始, 准备从列表中拖动到飞行队列的下一批文件 。

您通常不应该直接调用这种方法, 而是使用一个装入器方法, 如 `image` 或 `atlas` 。 但是, 只要给它的文件已经形成, 您就可以调用它 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) \| Array.\<[Phaser.Loader.File](/api/class/loader-file)> | 否 | 要添加到负载队列中的文件, 或文件的数组 。 |


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/LoaderPlugin.js#L515](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L515)  
引入版本：3.0.0


---

### addPack {#addPack}

#### \<instance> addPack(pack, [packKey]) {#instance-addpackpack-packkey}


**说明:**

使用一个很好、 完全解析的包文件对象并将其条目添加到负载队列中。 通常您不直接调用这种方法, 而是使用 `Loader.pack` 并提供一个拥有包数据的 JSON 文件的路径。 但是, 如果您已经准备好数据, 您可以把它传递到这种方法 。

您也可以提供可选的密钥。 如果可以, 它只会从包的这一部分添加到负载队列中。 如果不指定, 它会添加它找到的所有条目。 有关包文件格式的更多细节请参见 `LoaderPlugin.pack` 方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| pack | any | 否 | 要解析的 Pack 文件数据, 并包含每个条目在负载队列中 。 |
| packKey | string | 是 | 包文件数据中可选使用的密钥 。 |


**返回值:** boolean - 如果队列中添加了任何文件,则使用`true`,否则使用`false`.


> 源码：[src/loader/LoaderPlugin.js#L617](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L617)  
引入版本：3.7.0


---

### animation {#animation}

#### \<instance> animation(key, [url], [dataKey], [xhrSettings]) {#instance-animationkey-url-datakey-xhrsettings}


**说明:**

在当前负载队列中添加动画 JSON 数据文件,或动画 JSON 文件的数组.

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.animation('baddieAnims', 'files/BaddieAnims.json');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局 JSON 缓存中。 密钥在装入文件和JSON 缓存已显示的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从 JSON 缓结中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.animation({
    key: 'baddieAnims',
    url: 'files/BaddieAnims.json'
});
```

详见`Phaser.Types.Loader.FileTypes.JSONFileConfig`的文件.

一旦文件装入完成, 将自动传递到全局动画管理器的 `fromJSON` 方法。 这将分析所有 JSON 数据, 并从中创建动画数据。 这一过程发生在装入器的端部, 完成所有装入队列中的其他文件。 这样做的理由是允许您同时装入动画数据以及它在同一装入调用中依赖的图像 。

动画数据一经解析,您就可以使用该数据播放动画。请参见动画管理器 `fromJSON`方法,了解格式和播放的更多细节 。

您也可以使用其密钥访问其缓存中的原始动画数据 :

```javascript
this.load.animation('baddieAnims', 'files/BaddieAnims.json');
// and later in your game ...
var data = this.cache.json.get('baddieAnims');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将准备到此文件密钥 。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Waves` , 则最后的密钥是 `LEVEL1.Waves`, 这就是您从 JSON 缓存中获取文本时所使用的 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ 数据 ” 而未给出 URL, 那么装入器将设置 URL 为“ data.json ” 。 它会总是添加 `.json` 作为扩展, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不希望此动作, 那么提供 URL 。

您也可以选择提供 `dataKey` 使用。 这使得您只能提取 JSON 的一部分并将其存储在缓存中, 而不是整个文件。 例如, 如果您的 JSON 数据有这样的结构 :

```json
{
    "level1": {
        "baddies": {
            "aliens": {},
            "boss": {}
        }
    },
    "level2": {},
    "level3": {}
}
```

如果你只想从`boss`数据中创建动画,那么你可以通过`level1.baddies.boss`作为`dataKey`.

注意: 只有在JSON 文件类型已建入 Phaser 时, 才能具备装入这类文件的能力。 它在默认构建中可用, 但可以排除在自定义构建之外 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.JSONFileConfig](/api/typedef/types-loader-filetypes#jsonfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.JSONFileConfig](/api/typedef/types-loader-filetypes#jsonfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.json`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. json" 。 |
| dataKey | string | 是 | 当动画 JSON 文件加载时,只有此属性会存储在缓存中,并用于创建动画数据. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/AnimationJSONFile.js#L77](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AnimationJSONFile.js#L77)  
引入版本：3.0.0


---

### aseprite {#aseprite}

#### \<instance> aseprite(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings]) {#instance-asepritekey-textureurl-atlasurl-texturexhrsettings-atlasxhrsettings}


**说明:**

Aseprite是一个强大的动画图案编辑器和像素艺术工具.

您可以在 [https://www.aseprite.org/](https://www.aseprite.org/) 找到更多细节

在当前负载队列中添加基于 JSON 的 Aseprite 动画,或动画阵列.

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.aseprite('gladiator', 'images/Gladiator.png', 'images/Gladiator.json');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

要在 Aseprite 中导出兼容的 JSON 文件, 请做以下操作 :

1. 转到“ 文件 - 导出工作表”

2. 标签上写着:

2a. 设置“ 套座类型” 为“ 套座”

2b 设置"约束"为"无".

2c. 请检查date=中的日期值 (帮助) "Morge Reverses" 复本复选框

3. 标签上:

3a. 将“ 线条” 设置为“ 可见层 ”

3b. 将“ Frames” 设定为“ 所有框架”,除非您仅希望导出一组子标签

4. 在**边界**标签上:

4a. 请检查date=中的日期值 (帮助) "Trim Sprite"和"Trim Cells"选项

4b. 确保“边境铺设”、“间隔”和“内部铺设”均大于0(1通常足够)

5. 在**产出**标签上:

5a. 检查“ 输出文件” , 给您图像一个名称, 并确保您选择“ png 文件” 作为文件类型

5b. 检查"JSON Data",并给您的Json文件一个名字

5c. JSON Data类型可以是哈什或阵列,Phaser不介意.

5d. 确保“ Tags” 在 Meta 选项中被检查

5e. 在“项目文件名” 输入框中,请确保只写“ {frame} ” , 仅此而已 。

6. 单击导出

测试时采用了Aeprite 1.2.25.

这将导出一个 png 和 json 文件, 您可以使用 Aseprite 载入器 来加载 。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.aseprite({
    key: 'gladiator',
    textureURL: 'images/Gladiator.png',
    atlasURL: 'images/Gladiator.json'
});
```

详见`Phaser.Types.Loader.FileTypes.AsepriteFileConfig`的文件.

而不是通过一个JSON数据的URL,你也可以在一个形成良好的JSON对象中通过.

一旦装入,您可以从“ atlas” 键的场景内调用这种方法 :

```javascript
this.anims.createFromAseprite('paladin');
```

JSON中定义的任何动画现在都可以在Phaser中使用,您通过他们的标签名称来播放。例如,如果您在您的Aseprite时间表中有名为“战争哭”的动画,您可以使用该标签名称在Phaser中播放:

```javascript
this.add.sprite(400, 300).play('War Cry');
```

在调用此方法时, 您可以选择提供一系列标记名称, 只有这些动画才会被创建 。 例如 :

```javascript
this.anims.createFromAseprite('paladin', [ 'step', 'War Cry', 'Magnum Break' ]);
```

这将只创建定义的 3 个动画。 请注意, 标记名称是区分大小写 。

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ alien” 且没有给定 URL, 那么装入器会设置 URL 为“ alien. png ” 。 它会总是添加 `.png` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想这样做, 那么就提供 URL 。

注意: 只有在将 Aseprite 文件类型构建为 Phaser 时, 才能装入这类文件。 默认构建中可使用, 但可排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.AsepriteFileConfig](/api/typedef/types-loader-filetypes#asepritefileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AsepriteFileConfig](/api/typedef/types-loader-filetypes#asepritefileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| textureURL | string \| Array.\<string> | 是 | 装入纹理图像文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| atlasURL | object \| string | 是 | 从中加载纹理地图集 json 数据文件的绝对或相对 URL。 如果未定义或 `null` , 则它将被设定为 `<key>.json`, 即如果 `key` 是"外国人" , 那么 URL 将是 "alien.json" 。 或者, 一个已形成良好的 JSON 对象 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集图像文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集 json 文件的 XHR 设置配置对象。 用于替换加载器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/AsepriteFile.js#L114](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AsepriteFile.js#L114)  
引入版本：3.50.0


---

### atlas {#atlas}

#### \<instance> atlas(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings]) {#instance-atlaskey-textureurl-atlasurl-texturexhrsettings-atlasxhrsettings}


**说明:**

在当前负载队列中添加基于 JSON 的纹理图集,或图集阵列。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.atlas('mainmenu', 'images/MainMenu.png', 'images/MainMenu.json');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

Phaser期望在JSON文件中提供地图集数据,使用JSON Hash或JSON阵列格式.

这些文件是通过软件创建的,例如:

* [Texture Packer](https://www.codeandweb.com/texturepacker/tutorials/how-to-create-sprite-sheets-for-phaser3?source=photonstorm)

* [Shoebox](https://renderhjs.net/shoebox/)

* [Gamma Texture Packer](https://gammafp.com/tool/atlas-packer/)

* [Adobe Flash / Animate](https://www.adobe.com/uk/products/animate.html)

* [Free Texture Packer](http://free-tex-packer.com/)

* [Leshy SpriteSheet Tool](https://www.leshylabs.com/apps/sstool/)

如果您正在使用Texture Packer并启用了多图集支持,那么请使用Phaser多图集加载器,而不是这个.

Phaser可以装入所有常见的图像类型: png,jpg,gif以及浏览器可以本土处理的任何其他格式.

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.atlas({
    key: 'mainmenu',
    textureURL: 'images/MainMenu.png',
    atlasURL: 'images/MainMenu.json'
});
```

详见`Phaser.Types.Loader.FileTypes.AtlasJSONFileConfig`的文件.

而不是通过一个地图集JSON数据的URL,你也可以在一个形成良好的JSON对象中通过.

一旦地图集装入完毕,您可以通过引用游戏对象的键,将图像框用作其纹理:

```javascript
this.load.atlas('mainmenu', 'images/MainMenu.png', 'images/MainMenu.json');
// and later in your game ...
this.add.image(x, y, 'mainmenu', 'background');
```

要在地图集中找到所有可用框架的清单,请查阅您的文字图集软件。

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ alien” 且没有给定 URL, 那么装入器会设置 URL 为“ alien. png ” 。 它会总是添加 `.png` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想这样做, 那么就提供 URL 。

Phaser还支持自动加载相关的普通地图。如果您有一张普通地图可以随此图像一起运行,那么您可以通过提供一个阵列来指定它,作为`url`,其中第二个元素是普通地图:

```javascript
this.load.atlas('mainmenu', [ 'images/MainMenu.png', 'images/MainMenu-n.png' ], 'images/MainMenu.json');
```

或者,如果使用配置对象使用 `normalMap` 属性:

```javascript
this.load.atlas({
    key: 'mainmenu',
    textureURL: 'images/MainMenu.png',
    normalMap: 'images/MainMenu-n.png',
    atlasURL: 'images/MainMenu.json'
});
```

普通地图文件在路径,baseURL,CORS和XHR设置方面与图像文件条件相同. 普通地图只是WebGL的特性.

注意: 只有将 Atlas JSON 文件类型建入 Phaser 时, 才能装入这类文件。 默认的构建中可以使用, 但可以排除自定义构建中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.AtlasJSONFileConfig](/api/typedef/types-loader-filetypes#atlasjsonfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AtlasJSONFileConfig](/api/typedef/types-loader-filetypes#atlasjsonfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| textureURL | string \| Array.\<string> | 是 | 装入纹理图像文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| atlasURL | object \| string | 是 | 从中加载纹理地图集 json 数据文件的绝对或相对 URL。 如果未定义或 `null` , 则它将被设定为 `<key>.json`, 即如果 `key` 是"外国人" , 那么 URL 将是 "alien.json" 。 或者, 一个已形成良好的 JSON 对象 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集图像文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集 json 文件的 XHR 设置配置对象。 用于替换加载器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/AtlasJSONFile.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AtlasJSONFile.js#L109)  
引入版本：3.0.0


---

### atlasPCT {#atlasPCT}

#### \<instance> atlasPCT(key, [atlasURL], [path], [baseURL], [atlasXhrSettings]) {#instance-atlaspctkey-atlasurl-path-baseurl-atlasxhrsettings}


**说明:**

在当前负载队列中添加 Phaser 压缩纹理图集,或其中的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.atlasPCT('level1', 'images/Level1.pct');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

Phaser期望地图集数据以Phaser压缩纹理格式(PCT)提供。这是紧凑的面向行的文字格式,通常比等效的JSON地图集描述器小90-95%,但运行时仍可以略微解析。一个`.pct`文件可以描述一个或多个地图集页(纹理图像)。请参看Phaser压缩纹理图集格式规格,以完整描述格式。

它的内部工作方式是您为 PCT 数据文件提供 URL。 Phaser 载入了此文件,解码了它,提取了它需要从页面记录中加载的哪些纹理文件,并排队了每个引用的图像。当所有图像都加载了时,地图集被组装为文本管理器中的单一多源纹理,解码的PCT数据被存储在Atlas缓存的同一密钥下.

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.atlasPCT({
    key: 'level1',
    atlasURL: 'images/Level1.pct'
});
```

详见`Phaser.Types.Loader.FileTypes.PCTAtlasFileConfig`的文件.

一旦地图集装入完毕,您可以通过引用游戏对象的键,将图像框用作其纹理:

```javascript
this.load.atlasPCT('level1', 'images/Level1.pct');
// and later in your game ...
this.add.image(x, y, 'level1', 'background');
```

解码的PCT数据(包括页面、文件夹和框架元数据)也可从Atlas缓存中获取:

```javascript
var data = this.cache.atlas.get('level1');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器会从中取下该密钥并创建文件名。 例如, 如果密钥是“ alien” 而未给出 URL, 那么装入器会设置 URL 为“ alien. pct ” 。 它会总是添加 `.pct` , 尽管如果使用对象而不是方法参数, 则会覆盖它 。 如果您不想使用此动作, 那么就提供 URL 。

注意: 只有在将 PCT Atlas 文件类型建入 Phaser 时, 才能装入这类文件。 它在默认的构建中可用, 但可以从自定义构建中排除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.PCTAtlasFileConfig](/api/typedef/types-loader-filetypes#pctatlasfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.PCTAtlasFileConfig](/api/typedef/types-loader-filetypes#pctatlasfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| atlasURL | string | 是 | 装入 PCT 数据文件的绝对或相对 URL。 如果未定义或 `null` , 则它将被设定为 `<key>.pct`, 即如果 `key` 是"外国人", 那么 URL 将是 "alien. pct" 。 |
| path | string | 是 | 装入PCT数据中定义的纹理时可选用的路径 。 |
| baseURL | string | 是 | 装入PCT数据中定义的纹理时要使用的可选基址 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | PCT 数据文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/PCTAtlasFile.js#L251](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PCTAtlasFile.js#L251)  
引入版本：4.0.0


---

### atlasXML {#atlasXML}

#### \<instance> atlasXML(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings]) {#instance-atlasxmlkey-textureurl-atlasurl-texturexhrsettings-atlasxhrsettings}


**说明:**

在当前负载队列中添加基于 XML 的纹理图集,或数组地图集。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.atlasXML('mainmenu', 'images/MainMenu.png', 'images/MainMenu.xml');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

Phaser期望以 XML 文件格式提供地图集数据。 这些文件由诸如Shoebox 和 Adobe Flash / Animate 等软件创建 。

Phaser可以装入所有常见的图像类型: png,jpg,gif以及浏览器可以本土处理的任何其他格式.

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.atlasXML({
    key: 'mainmenu',
    textureURL: 'images/MainMenu.png',
    atlasURL: 'images/MainMenu.xml'
});
```

详见`Phaser.Types.Loader.FileTypes.AtlasXMLFileConfig`的文件.

一旦地图集装入完毕,您可以通过引用游戏对象的键,将图像框用作其纹理:

```javascript
this.load.atlasXML('mainmenu', 'images/MainMenu.png', 'images/MainMenu.xml');
// and later in your game ...
this.add.image(x, y, 'mainmenu', 'background');
```

要在地图集中找到所有可用框架的清单,请查阅您的文字图集软件。

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ alien” 且没有给定 URL, 那么装入器会设置 URL 为“ alien. png ” 。 它会总是添加 `.png` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想这样做, 那么就提供 URL 。

Phaser还支持自动加载相关的普通地图。如果您有一张普通地图可以随此图像一起运行,那么您可以通过提供一个阵列来指定它,作为`url`,其中第二个元素是普通地图:

```javascript
this.load.atlasXML('mainmenu', [ 'images/MainMenu.png', 'images/MainMenu-n.png' ], 'images/MainMenu.xml');
```

或者,如果使用配置对象使用 `normalMap` 属性:

```javascript
this.load.atlasXML({
    key: 'mainmenu',
    textureURL: 'images/MainMenu.png',
    normalMap: 'images/MainMenu-n.png',
    atlasURL: 'images/MainMenu.xml'
});
```

普通地图文件在路径,baseURL,CORS和XHR设置方面与图像文件条件相同. 普通地图只是WebGL的特性.

注意: 只有在将 Atlas XML 文件类型建入 Phaser 时, 才能具备装入这类文件的能力。 默认的构建中可以使用, 但可以排除自定义构建中的内容 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.AtlasXMLFileConfig](/api/typedef/types-loader-filetypes#atlasxmlfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AtlasXMLFileConfig](/api/typedef/types-loader-filetypes#atlasxmlfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| textureURL | string \| Array.\<string> | 是 | 装入纹理图像文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| atlasURL | string | 是 | 从中加载纹理图集 xml 数据文件的绝对或相对的 URL 。 如果未定义或 `null` , 则它将被设定为 `<key>.xml` , 即如果 `key` 是"外国人" , 那么 URL 将是 "alien. xml" 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集图像文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于替换加载器默认 XHR 设置的 XHR 设置对象 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/AtlasXMLFile.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AtlasXMLFile.js#L111)  
引入版本：3.7.0


---

### audio {#audio}

#### \<instance> audio(key, [urls], [config], [xhrSettings]) {#instance-audiokey-urls-config-xhrsettings}


**说明:**

在当前负载队列中添加音频或HTML5Audio文件,或音频文件的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.audio('title', [ 'music/Title.ogg', 'music/Title.mp3', 'music/Title.m4a' ]);
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在装入成功时将文件添加到全局音频缓存。 密钥在装入文件和音频缓存中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换一个已有文件, 请在装入新文件之前先从音频缓存中删除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.audio({
    key: 'title',
    url: [ 'music/Title.ogg', 'music/Title.mp3', 'music/Title.m4a' ]
});
```

详见`Phaser.Types.Loader.FileTypes.AudioFileConfig`的文件.

URL可以是相对的或绝对的。如果URL是相对的,则`Loader.baseURL`和`Loader.path`的值会被预设为它们.

由于支持不同音频文件类型的浏览器不同,您通常应该以多种格式提供音频文件。 ogg、 mp3 和 m4a 是最常见的。 如果您提供了一系列 URL, 装入器将根据浏览器支持来确定要加载的_ 1_ 文件 。

如果在游戏中音频已被禁用,或者通过游戏配置,或者设备缺乏支持,那么就不会加载音频.

注意: 只有在将音频文件类型构建为 Phaser 时, 才能具备装入这类文件的能力。 它在默认的构建中可用, 但可以排除在自定义构建之外 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.AudioFileConfig](/api/typedef/types-loader-filetypes#audiofileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AudioFileConfig](/api/typedef/types-loader-filetypes#audiofileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| urls | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AudioFileURLConfig](/api/typedef/types-loader-filetypes#audiofileurlconfig)> | 是 | 绝对或相对的URL来从中加载音频文件. |
| config | any | 是 | 包含 HTML5Audio 的 `instances` 属性的对象。默认为 1 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/AudioFile.js#L221](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioFile.js#L221)  
引入版本：3.0.0


---

### audioSprite {#audioSprite}

#### \<instance> audioSprite(key, jsonURL, [audioURL], [audioConfig], [audioXhrSettings], [jsonXhrSettings]) {#instance-audiospritekey-jsonurl-audiourl-audioconfig-audioxhrsettings-jsonxhrsettings}


**说明:**

在当前负载队列中添加基于 JSON 的音频Sprite, 或音频sprite 的数组 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.audioSprite('kyobi', 'kyobi.json', [
        'kyobi.ogg',
        'kyobi.mp3',
        'kyobi.m4a'
    ]);
}
```

音频Sprites是音频文件与JSON配置的组合. JSON遵循[https://github.com/tonistiigi/audiosprite](https://github.com/tonistiigi/audiosprite)创建的格式.

如果 JSON 文件包含一个“ 资源” 对象, 您可以让 Phaser 分析它, 并自动根据它的内容加载音频文件。 要做到这一点, 音频 URL 将排除于负载中 :

```javascript
function preload ()
{
    this.load.audioSprite('kyobi', 'kyobi.json');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

密钥必须是独一无二的字符串。 它用于在装入成功时将文件添加到全局音频缓存。 密钥在装入文件和音频缓存中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换一个已有文件, 请在装入新文件之前先从音频缓存中删除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.audioSprite({
    key: 'kyobi',
    jsonURL: 'audio/Kyobi.json',
    audioURL: [
        'audio/Kyobi.ogg',
        'audio/Kyobi.mp3',
        'audio/Kyobi.m4a'
    ]
});
```

详见`Phaser.Types.Loader.FileTypes.AudioSpriteFileConfig`的文件.

而不是通过一个用于音频 JSON 数据的 URL,你也可以通过一个 井中的 JSON 对象代替。

一旦音频装入完成,您就可以使用它通过引用其密钥创建音频Sprite:

```javascript
this.load.audioSprite('kyobi', 'kyobi.json');
// and later in your game ...
var music = this.sound.addAudioSprite('kyobi');
music.play('title');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将准备到此文件的密钥。 例如, 如果前缀是 `MENU.` 而密钥是 `Background`, 则最后的密钥将是 `MENU.Background`, 这就是您从音频缓存中获取音频图示 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

由于支持不同音频文件类型的浏览器不同,您通常应该以多种格式提供音频文件。 ogg、 mp3 和 m4a 是最常见的。 如果您提供了一系列 URL, 装入器将根据浏览器支持来确定要加载的_ 1_ 文件 。

如果在游戏中音频已被禁用,或者通过游戏配置,或者设备缺乏支持,那么就不会加载音频.

注意: 只有在将音频 Sprite 文件类型建入 Phaser 时, 才能装入这类文件。 默认的构建中可以使用, 但可以排除自定义构建中的内容 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.AudioSpriteFileConfig](/api/typedef/types-loader-filetypes#audiospritefileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.AudioSpriteFileConfig](/api/typedef/types-loader-filetypes#audiospritefileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或一系列对象 。 |
| jsonURL | string | 否 | 绝对或相对的 URL 来从 json 文件装入。 或者一个 良好形成的 JSON 对象来代替 。 |
| audioURL | string \| Array.\<string> | 是 | 装入音频文件的绝对或相对 URL。 如果是空的, 则通过解析 JSON 文件来获取 。 |
| audioConfig | any | 是 | 音频配置选项 。 |
| audioXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 音频文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| jsonXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于 json 文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/AudioSpriteFile.js#L143](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/AudioSpriteFile.js#L143)  
引入版本：3.0.0


---

### binary {#binary}

#### \<instance> binary(key, [url], [dataType], [xhrSettings]) {#instance-binarykey-url-datatype-xhrsettings}


**说明:**

在当前负载队列中添加二进制文件或二进制文件阵列。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.binary('doom', 'files/Doom.wad');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 用于在成功加载时将文件添加到全局二进制缓存。 密钥在装入文件和二进制缓存中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换一个已有文件, 请在装入新文件之前先从二进制缓存中删除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.binary({
    key: 'doom',
    url: 'files/Doom.wad',
    dataType: Uint8Array
});
```

详见`Phaser.Types.Loader.FileTypes.BinaryFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.binary('doom', 'files/Doom.wad');
// and later in your game ...
var data = this.cache.binary.get('doom');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将准备到此文件密钥 。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Data` , 则最后的密钥是 `LEVEL1.Data`, 您会用它从二进制缓存中获取文本 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 未指定, 装入器将取下密钥并创建文件名。 例如, 如果密钥是“ doom” 而未给出 URL, 装入器会设置 URL 为“ doom. bin ” 。 它会总是将 `.bin` 添加为扩展名, 尽管如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想使用此动作, 那么就提供 URL 。

注意: 只有在二进制文件类型已建入 Phaser 时, 才有装入这类文件的能力。 它在默认构建中可用, 但可以排除自定义构建中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.BinaryFileConfig](/api/typedef/types-loader-filetypes#binaryfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.BinaryFileConfig](/api/typedef/types-loader-filetypes#binaryfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.bin`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. bin" 。 |
| dataType | any | 是 | 可选类型将二进制文件投放到一次装入。 例如, `Uint8Array` 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/BinaryFile.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/BinaryFile.js#L96)  
引入版本：3.0.0


---

### bitmapFont {#bitmapFont}

#### \<instance> bitmapFont(key, [textureURL], [fontDataURL], [textureXhrSettings], [fontDataXhrSettings]) {#instance-bitmapfontkey-textureurl-fontdataurl-texturexhrsettings-fontdataxhrsettings}


**说明:**

在当前负载队列中添加基于 XML 的位图字体,或字体数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.bitmapFont('goldenFont', 'images/GoldFont.png', 'images/GoldFont.xml');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

Phaser期望以 XML 文件格式提供字体数据。这些文件由[Angelcode Bitmap Font Generator](http://www.angelcode.com/products/bmfont/),[Littera](http://kvazars.com/littera/)或[Glyph Designer](https://71squared.com/glyphdesigner)等软件创建.

Phaser可以装入所有常见的图像类型: png,jpg,gif以及浏览器可以本土处理的任何其他格式.

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.bitmapFont({
    key: 'goldenFont',
    textureURL: 'images/GoldFont.png',
    fontDataURL: 'images/GoldFont.xml'
});
```

详见`Phaser.Types.Loader.FileTypes.BitmapFontFileConfig`的文件.

位图字体完成加载后,可以在创建位图文字游戏对象时使用其键:

```javascript
this.load.bitmapFont('goldenFont', 'images/GoldFont.png', 'images/GoldFont.xml');
// and later in your game ...
this.add.bitmapText(x, y, 'goldenFont', 'Hello World');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将被预设为此文件密钥 。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则 最终密钥是 `MENU.Background`, 这就是您创建位图文本对象时将使用的内容 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ alien” 且没有给定 URL, 那么装入器会设置 URL 为“ alien. png ” 。 它会总是添加 `.png` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想这样做, 那么就提供 URL 。

Phaser还支持自动加载相关的普通地图。如果您有一张普通地图可以随此图像一起运行,那么您可以通过提供一个阵列来指定它,作为`url`,其中第二个元素是普通地图:

```javascript
this.load.bitmapFont('goldenFont', [ 'images/GoldFont.png', 'images/GoldFont-n.png' ], 'images/GoldFont.xml');
```

或者,如果使用配置对象使用 `normalMap` 属性:

```javascript
this.load.bitmapFont({
    key: 'goldenFont',
    textureURL: 'images/GoldFont.png',
    normalMap: 'images/GoldFont-n.png',
    fontDataURL: 'images/GoldFont.xml'
});
```

普通地图文件在路径,baseURL,CORs和XHR设置方面与图像文件条件相同. 普通地图只是WebGL的特性.

注意: 只有在将 Bitmap 字体文件类型建入 Phaser 时, 才具备装入这类文件的能力。 默认的构建中可以使用, 但可以排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.BitmapFontFileConfig](/api/typedef/types-loader-filetypes#bitmapfontfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.BitmapFontFileConfig](/api/typedef/types-loader-filetypes#bitmapfontfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| textureURL | string \| Array.\<string> | 是 | 装入字体图像文件的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| fontDataURL | string | 是 | 装入字体 xml 数据文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.xml`, 即如果 `key` 是"外国人", 那么 URL 将是 "alien. xml" 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 字体图像文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| fontDataXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 字体数据 xml 文件的设置对象。 用于替换装入器默认的 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/BitmapFontFile.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/BitmapFontFile.js#L113)  
引入版本：3.0.0


---

### css {#css}

#### \<instance> css(key, [url], [xhrSettings]) {#instance-csskey-url-xhrsettings}


**说明:**

在当前负载队列中添加 CSS 文件,或 CSS 文件的数组 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.css('headers', 'styles/headers.css');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串, 并且还没有被装入器中的另一个文件使用 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.css({
    key: 'headers',
    url: 'styles/headers.css'
});
```

详见`Phaser.Types.Loader.FileTypes.CSSFileConfig`的文件.

装入文件完成后, 将会通过 `document.createElement('style')` 自动转换成样式 DOM 元素。 它会将其 `defer` 属性设置为假, 然后生成的元素会附加到 `document.head` 中。 然后将 CSS 样式应用到当前文档中 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 没有指定, 装入器会从中取下密钥并创建文件名。 例如, 如果密钥是“ alien” 且没有给出 URL, 那么装入器会设置 URL 为“ alien. css ” 。 它会总是添加 `.css`z , 但是如果使用对象而不是方法参数, 则会覆盖它 。 如果您不想这样做, 那么就提供 URL 。

注意: 只有在将 CSS 文件类型构建为 Phaser 时, 才能具备装入这类文件的能力。 它在默认构建中可以使用, 但可以排除在自定义构建之外 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.CSSFileConfig](/api/typedef/types-loader-filetypes#cssfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.CSSFileConfig](/api/typedef/types-loader-filetypes#cssfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.css`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. css" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/CSSFile.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/CSSFile.js#L93)  
引入版本：3.17.0


---

### fileProcessComplete {#fileProcessComplete}

#### \<instance> fileProcessComplete(file) {#instance-fileprocesscompletefile}


**说明:**

一种内部方法,在文件完成处理后被自动调用.

如果进程成功,且文件不属于多文件的一部分,则其`addToCache`方法称为.

然后从队列中移除它。 如果没有更多文件可以装入 `loadComplete` , 则调用 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 已完成处理的文件 。 |


> 源码：[src/loader/LoaderPlugin.js#L1068](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L1068)  
引入版本：3.7.0


---

### flagForRemoval {#flagForRemoval}

#### \<instance> flagForRemoval(file) {#instance-flagforremovalfile}


**说明:**

将文件添加到待删除的队列中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 装入器完成后要排队删除的文件 。 |


> 源码：[src/loader/LoaderPlugin.js#L1162](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L1162)  
引入版本：3.7.0


---

### font {#font}

#### \<instance> font(key, [url], [format], [descriptors], [xhrSettings]) {#instance-fontkey-url-format-descriptors-xhrsettings}


**说明:**

在当前负载队列中添加字体文件或字体文件的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.font('Nokia', 'assets/nokia.ttf', 'truetype');
}
```

如果字体文件是打开类型的,则可以指定格式:

```javascript
function preload ()
{
    this.load.font('Nokia', 'assets/nokia.otf', 'opentype');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串, 并且还没有被装入器中的另一个文件使用 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.font({
    key: 'Nokia',
    url: 'assets/nokia.ttf',
    format: 'truetype',
    descriptors: { style: 'normal', weight: '400' }
});
```

详见`Phaser.Types.Loader.FileTypes.FontFileConfig`的文件.

关于描述词的细节,请参看[https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace#descriptors](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace#descriptors)的MDN文档。

当这个文件由加载器处理时,它会为此创建一个新的Font Face DOM元素,并添加到文档中.

您应该使用文本对象中字体的相同键,例如:

```javascript
this.add.text(x, y, 'Hello World', { fontFamily: 'Nokia', fontSize: 48 });
```

详情请见[https://developer.mozilla.org/en-US/docs/Web/API/FontFace](https://developer.mozilla.org/en-US/docs/Web/API/FontFace)。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将取下该密钥并创建文件名。 例如, 如果密钥是“ alien ” 而未给出 URL, 那么装入器将设置 URL 成为“ alien. ttf ” 。 它会总是添加 `.ttf` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想这样做, 那么就提供 URL 。

注意: 只有在字体文件类型已建入 Phaser 时, 才有装入这类文件的能力。 它在默认的构建中可用, 但可以排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.FontFileConfig](/api/typedef/types-loader-filetypes#fontfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.FontFileConfig](/api/typedef/types-loader-filetypes#fontfileconfig)> | 否 |  | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 |  | 装入此文件的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.ttf`, 即如果 `key` 是" 外国人", 那么 URL 将是" alien. ttf" 。 |
| format | string | 是 | "'truetype'" | 字体类型。 应该是字符串, 如“ truetype ” 或“ opentype ” 。 |
| descriptors | object | 是 |  | 含有字体面部字体描述符的可选对象。 详见 https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace#descriptors 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/FontFile.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/FontFile.js#L135)  
引入版本：3.87.0


---

### glsl {#glsl}

#### \<instance> glsl(key, [url], [xhrSettings]) {#instance-glslkey-url-xhrsettings}


**说明:**

在当前负载队列中添加 GLSL 文件, 或 GLSL 文件的数组。 在 Phaser 3 GLSL 文件中, 仅仅是包含源代码的纯文本文件 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.glsl('plasma', 'shaders/Plasma.glsl');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局阴影缓存。 密钥在装入的文件和在阴影缓存中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从阴影缓存中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.glsl({
    key: 'plasma',
    url: 'shaders/Plasma.glsl'
});
```

详见`Phaser.Types.Loader.FileTypes.GLSLFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.glsl('plasma', 'shaders/Plasma.glsl');
// and later in your game ...
var data = this.cache.shader.get('plasma');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将预设为此文件的密钥。 例如, 如果前缀为 `FX.` , 而密钥为 `Plasma` , 最后的密钥为 `FX.Plasma` , 您将使用此来从 Shader 缓存中获取文本 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 指定不在此指定, 装入器将取下该密钥并创建文件名。 例如, 如果密钥是“ plasma ” 而未给出 URL , 那么装入器将设置 URL 为“ plasma. glsl ” 。 它会总是添加 `.glsl`z 作为扩展名, 尽管如果使用对象而不是方法参数, 则可以覆盖它。 如果您不希望此动作, 请提供 URL 。

注意: 只有在将 GLSL 文件类型构建为 Phaser 时, 才具有装入这类文件的能力。 它在默认构建中可用, 但可以排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.GLSLFileConfig](/api/typedef/types-loader-filetypes#glslfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.GLSLFileConfig](/api/typedef/types-loader-filetypes#glslfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.glsl`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. glsl" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/GLSLFile.js#L105](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/GLSLFile.js#L105)  
引入版本：3.0.0


---

### html {#html}

#### \<instance> html(key, [url], [xhrSettings]) {#instance-htmlkey-url-xhrsettings}


**说明:**

在当前负载队列中添加 HTML 文件,或 HTML 文件的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.html('story', 'files/LoginForm.html');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局 HTML 缓存。 密钥在装入的文件和 HTML 缓缓存中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从 HTML 缓处理中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.html({
    key: 'login',
    url: 'files/LoginForm.html'
});
```

详见`Phaser.Types.Loader.FileTypes.HTMLFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.html('login', 'files/LoginForm.html');
// and later in your game ...
var data = this.cache.html.get('login');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将被预设为此文件密钥。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Story` , 则最后的密钥将是 `LEVEL1.Story` , 这就是您从 HTML 缓存中获取 html 的用法 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并创建文件名。 例如, 如果密钥是“ 故事 ” 而未给出 URL, 那么装入器将设置 URL 为“ story. html ” 。 它将总是添加 `.html` 作为扩展, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不希望此动作, 那么提供 URL 。

注意: 只有在HTML 文件类型已建入 Phaser 时, 才能装入这类文件。 默认的构建中可以使用, 但可以排除自定义构建中的内容 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.HTMLFileConfig](/api/typedef/types-loader-filetypes#htmlfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.HTMLFileConfig](/api/typedef/types-loader-filetypes#htmlfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.html`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. html" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/HTMLFile.js#L89](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTMLFile.js#L89)  
引入版本：3.12.0


---

### htmlTexture {#htmlTexture}

#### \<instance> htmlTexture(key, [url], [width], [height], [xhrSettings]) {#instance-htmltexturekey-url-width-height-xhrsettings}


**说明:**

在当前负载队列中添加 HTML 文件,或 HTML 文件的数组。 文件装入后, 将被渲染成纹理, 并存储在纹理管理器中 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.htmlTexture('instructions', 'content/intro.html', 256, 512);
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.htmlTexture({
    key: 'instructions',
    url: 'content/intro.html',
    width: 256,
    height: 512
});
```

详见`Phaser.Types.Loader.FileTypes.HTMLTextureFileConfig`的文件.

文件装入完成后,您可以通过引用游戏对象的密钥,将其作为游戏对象的纹理:

```javascript
this.load.htmlTexture('instructions', 'content/intro.html', 256, 512);
// and later in your game ...
this.add.image(x, y, 'instructions');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将取下密钥并创建文件名。 例如, 如果密钥是“ alien” 而未给出 URL, 那么装入器将设置 URL 为“ alien. html ” 。 它会总是将 `.html` 添加为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想使用此动作, 那么就提供 URL 。

宽度和高度是 HTML 将显示的纹理大小。 无法自动确定这些大小, 因此您需要作为参数或文件配置对象提供这些大小。 当 HTML 文件装入了一个新的 SVG 元素时, 将设置一个大小和视图框, 以给出的宽度和高度。 SVG 文件添加了一个机构标记, 其中包括 HTML 文件内容。 然后调用它 。 `window.Blob` 上,如果成功添加到纹理管理器中,则处理失败。所渲染的 HTML 的整体质量取决于您的浏览器,其中一些甚至可能不支持使用的 svg / blob 进程。请注意, HTML 可能包含在 SVG 内部的特性有局限性。 您可以在此找到更多细节 。 [Mozilla MDN entry](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Drawing_DOM_objects_into_a_canvas).

注意: 只有在HTMLTextureFile文件类型已建入 Phaser 时, 才能装入这类文件。 默认的构建中可以使用, 但可以排除自定义构建中的内容 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.HTMLTextureFileConfig](/api/typedef/types-loader-filetypes#htmltexturefileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.HTMLTextureFileConfig](/api/typedef/types-loader-filetypes#htmltexturefileconfig)> | 否 |  | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 |  | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.html`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. html" 。 |
| width | number | 是 | 512 | HTML 的纹理宽度将被渲染到 。 |
| height | number | 是 | 512 | HTML 的纹理高度将被渲染到 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/HTMLTextureFile.js#L158](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/HTMLTextureFile.js#L158)  
引入版本：3.12.0


---

### image {#image}

#### \<instance> image(key, [url], [xhrSettings]) {#instance-imagekey-url-xhrsettings}


**说明:**

在当前负载队列中添加图像,或图像阵列。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.image('logo', 'images/phaserLogo.png');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

Phaser可以装入所有常见的图像类型: png, jpg, gif 和浏览器可以本地处理的任何其他格式。 如果您尝试装入动画的 gif , 将只提供第一个帧。 浏览器不会在本地支持将动画的 gifs 播放到 Canvas 元素 。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.image({
    key: 'logo',
    url: 'images/AtariLogo.png'
});
```

详见`Phaser.Types.Loader.FileTypes.ImageFileConfig`的文件.

文件装入完成后,您可以通过引用游戏对象的密钥,将其作为游戏对象的纹理:

```javascript
this.load.image('logo', 'images/AtariLogo.png');
// and later in your game ...
this.add.image(x, y, 'logo');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ alien” 且没有给定 URL, 那么装入器会设置 URL 为“ alien. png ” 。 它会总是添加 `.png` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想这样做, 那么就提供 URL 。

Phaser还支持自动加载相关的普通地图。如果您有一张普通地图可以随此图像一起运行,那么您可以通过提供一个阵列来指定它,作为`url`,其中第二个元素是普通地图:

```javascript
this.load.image('logo', [ 'images/AtariLogo.png', 'images/AtariLogo-n.png' ]);
```

或者,如果使用配置对象使用 `normalMap` 属性:

```javascript
this.load.image({
    key: 'logo',
    url: 'images/AtariLogo.png',
    normalMap: 'images/AtariLogo-n.png'
});
```

普通地图文件在路径,baseURL,CORS和XHR设置方面与图像文件条件相同. 普通地图只是WebGL的特性.

Phaser 3.60 中新增了属性, 允许您控制图像的加载方式。 默认情况下, 图像会通过 XHR 作为 Blobs 装入。 然而, 您可以在游戏配置中设置 `loader.imageLoadType: "HTMLImageElement"`, 而装入器会通过图像标记装入所有图像 。

注意: 只有在图像文件类型已建入 Phaser 时, 才能装入这类文件。 它在默认构建中可用, 但可以排除在自定义构建之外 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.ImageFileConfig](/api/typedef/types-loader-filetypes#imagefileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.ImageFileConfig](/api/typedef/types-loader-filetypes#imagefileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string \| Array.\<string> | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/ImageFile.js#L241](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/ImageFile.js#L241)  
引入版本：3.0.0


---

### isLoading {#isLoading}

#### \<instance> isLoading() {#instance-isloading}


**说明:**

装入器是正在装入, 还是正在处理装入的文件 ?


**返回值:** boolean - `true` 如果装货机忙于装货或处理,否则 `false`.


> 源码：[src/loader/LoaderPlugin.js#L873](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L873)  
引入版本：3.0.0


---

### isReady {#isReady}

#### \<instance> isReady() {#instance-isready}


**说明:**

装货机准备好开始新的载荷了吗?


**返回值:** boolean - 如果装货机准备好开始新的负载,则`true`,否则则`false`.


> 源码：[src/loader/LoaderPlugin.js#L886](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L886)  
引入版本：3.0.0


---

### json {#json}

#### \<instance> json(key, [url], [dataKey], [xhrSettings]) {#instance-jsonkey-url-datakey-xhrsettings}


**说明:**

在当前负载队列中添加 JSON 文件,或 JSON 文件的数组 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.json('wavedata', 'files/AlienWaveData.json');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局 JSON 缓存中。 密钥在装入文件和JSON 缓存已显示的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从 JSON 缓结中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.json({
    key: 'wavedata',
    url: 'files/AlienWaveData.json'
});
```

详见`Phaser.Types.Loader.FileTypes.JSONFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.json('wavedata', 'files/AlienWaveData.json');
// and later in your game ...
var data = this.cache.json.get('wavedata');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将准备到此文件密钥 。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Waves` , 则最后的密钥是 `LEVEL1.Waves`, 这就是您从 JSON 缓存中获取文本时所使用的 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ 数据 ” 而未给出 URL, 那么装入器将设置 URL 为“ data.json ” 。 它会总是添加 `.json` 作为扩展, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不希望此动作, 那么提供 URL 。

您也可以选择提供 `dataKey` 使用。 这使得您只能提取 JSON 的一部分并将其存储在缓存中, 而不是整个文件。 例如, 如果您的 JSON 数据有这样的结构 :

```json
{
    "level1": {
        "baddies": {
            "aliens": {},
            "boss": {}
        }
    },
    "level2": {},
    "level3": {}
}
```

而你只想把`boss`的数据存储在缓存中,然后就可以通过`level1.baddies.boss`作为`dataKey`.

注意: 只有在JSON 文件类型已建入 Phaser 时, 才能具备装入这类文件的能力。 它在默认构建中可用, 但可以排除在自定义构建之外 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.JSONFileConfig](/api/typedef/types-loader-filetypes#jsonfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.JSONFileConfig](/api/typedef/types-loader-filetypes#jsonfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | object \| string | 是 | 装入此文件的绝对或相对的 URL。 如果未定义或 `null` , 它将设定为 `<key>.json`, 即如果 `key` 是“ 外国人 ” 那么 URL 将是“ 外国人 . json ” 。 或者, 可以是完全形成的 JSON 对象 。 |
| dataKey | string | 是 | 当 JSON 文件加载时, 将只存储此属性到缓存 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/JSONFile.js#L135](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/JSONFile.js#L135)  
引入版本：3.0.0


---

### keyExists {#keyExists}

#### \<instance> keyExists(file) {#instance-keyexistsfile}


**说明:**

检查给定文件的密钥和类型, 以查看它是否会与缓存、 纹理管理器、 列表或飞行队列中的任何内容冲突 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 检查密钥的文件 。 |


**返回值:** boolean - `true`如果添加此文件将引起缓存或队列冲突,否则`false`.


> 源码：[src/loader/LoaderPlugin.js#L560](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L560)  
引入版本：3.7.0


---

### loadComplete {#loadComplete}

#### \<instance> loadComplete() {#instance-loadcomplete}


**说明:**

当负载队列已用尽且所有文件已装入或错误时, 呼叫结束。 到此点, 每个已装入的文件都将处于其相关缓存中, 并准备使用 。

也清除 Sets, 将进度设置为 1 并清除删除队列 。


**Fires:** [Phaser.Loader.Events#event:COMPLETE](/api/event/loader-events#complete), [Phaser.Loader.Events#event:POST_PROCESS](/api/event/loader-events#post_process)


> 源码：[src/loader/LoaderPlugin.js#L1126](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L1126)  
引入版本：3.7.0


---

### multiatlas {#multiatlas}

#### \<instance> multiatlas(key, [atlasURL], [path], [baseURL], [atlasXhrSettings]) {#instance-multiatlaskey-atlasurl-path-baseurl-atlasxhrsettings}


**说明:**

在当前负载队列中添加多纹理图集,或多图集的阵列。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.multiatlas('level1', 'images/Level1.json');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

Phaser期望在JSON文件中提供地图集数据,数据来自4.6.3或以上版本的Texture Packer应用程序,您已经保证使用Phaser 3导出选项。

它的内部工作方式是您为 JSON 文件提供 URL。 Phaser 然后装入 JSON, 解析并提取它还需要装入的纹理文件来完成这一过程。 如果 JSON 也定义了普通的地图, Phaser 也会装入这些文件 。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.multiatlas({
    key: 'level1',
    atlasURL: 'images/Level1.json'
});
```

详见`Phaser.Types.Loader.FileTypes.MultiAtlasFileConfig`的文件.

而不是通过一个地图集JSON数据的URL,你也可以在一个形成良好的JSON对象中通过.

一旦地图集装入完毕,您可以通过引用游戏对象的键,将图像框用作其纹理:

```javascript
this.load.multiatlas('level1', 'images/Level1.json');
// and later in your game ...
this.add.image(x, y, 'level1', 'background');
```

要在地图集中找到所有可用框架的清单,请查阅您的文字图集软件。

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 没有指定, 装入器将取下密钥并创建文件名。 例如, 如果密钥是“ alien” 且没有给出 URL, 那么装入器会设置 URL 为“ alien. json ” 。 它会总是将 `.json` 添加为扩展名, 尽管如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想使用此动作, 那么就提供 URL 。

注意: 只有在多图集文件类型已建入 Phaser 时, 才能装入这类文件。 它在默认的构建中可用, 但可以从自定义构建中排除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.MultiAtlasFileConfig](/api/typedef/types-loader-filetypes#multiatlasfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.MultiAtlasFileConfig](/api/typedef/types-loader-filetypes#multiatlasfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| atlasURL | string | 是 | 装入纹理地图集 json 数据文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.json`, 即 `key` 是"外国人", 那么 URL 将是 " alien.json" 。 |
| path | string | 是 | 装入地图集数据中定义的纹理时可选使用路径 。 |
| baseURL | string | 是 | 装入地图集数据中定义的纹理时使用的可选基址 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集 json 文件的 XHR 设置配置对象。 用于替换加载器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/MultiAtlasFile.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/MultiAtlasFile.js#L220)  
引入版本：3.7.0


---

### nextFile {#nextFile}

#### \<instance> nextFile(file, success) {#instance-nextfilefile-success}


**说明:**

属于文件的 XHR Loader 自动调用的内部方法 。

这种方法会从飞行集中移除给定的文件并更新负载进度。 如果文件成功, 则使用 `onProcess` 方法, 否则它会被添加到删除队列中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| file | [Phaser.Loader.File](/api/class/loader-file) | 否 | 刚刚装入完的文件, 或在装入时出错的文件 。 |
| success | boolean | 否 | 如果文件成功装入,则使用`true`,否则使用`false`. |


**Fires:** [Phaser.Loader.Events#event:FILE_LOAD](/api/event/loader-events#file_load), [Phaser.Loader.Events#event:FILE_LOAD_ERROR](/api/event/loader-events#file_load_error)


> 源码：[src/loader/LoaderPlugin.js#L1020](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L1020)  
引入版本：3.0.0


---

### pack {#pack}

#### \<instance> pack(key, [url], [dataKey], [xhrSettings]) {#instance-packkey-url-datakey-xhrsettings}


**说明:**

在当前负载队列中添加 JSON 文件包,或数组包。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.pack('level1', 'data/Level1Files.json');
}
```

文件包是一个JSON文件(或对象),包含其他文件的细节,应当添加到加载器中。这里是一个小的例子:

```json
{
   "test1": {
       "files": [
           {
               "type": "image",
               "key": "taikodrummaster",
               "url": "assets/pics/taikodrummaster.jpg"
           },
           {
               "type": "image",
               "key": "sukasuka-chtholly",
               "url": "assets/pics/sukasuka-chtholly.png"
           }
       ]
   },
   "meta": {
       "generated": "1401380327373",
       "app": "Phaser 3 Asset Packer",
       "url": "[https://phaser.io](https://phaser.io)",
       "version": "1.0",
       "copyright": "Photon Storm Ltd. 2018"
   }
}
```

包可以分成几个部分。 在上方的例子中, 您可以看到一个叫做 `test1` 的区段。 您可以告诉 `load.pack` 方法只分析一个包的某个特定区段。 该包存储在 JSON 缓存中, 这样您就可以把它传递给加载器, 以便按照游戏中的需求处理额外的区段, 或者您可以一次性装入所有区段, 而无需指定任何内容 。

包文件可以包含一个Phaser可以加载的任意类型的文件的条目。 对象结构完全匹配文件类型配置, 文件类型配置中所有可用的属性也可以在包文件中使用。 条目的`type`是将加载它的方法的名称, 例如“ 图像 ” 。

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局 JSON 缓存中。 密钥在装入文件和JSON 缓存已显示的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从 JSON 缓结中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.pack({
    key: 'level1',
    url: 'data/Level1Files.json'
});
```

详见`Phaser.Types.Loader.FileTypes.PackFileConfig`的文件.

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将准备到此文件密钥 。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Waves` , 则最后的密钥是 `LEVEL1.Waves`, 这就是您从 JSON 缓存中获取文本时所使用的 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ 数据 ” 而未给出 URL, 那么装入器将设置 URL 为“ data.json ” 。 它会总是添加 `.json` 作为扩展, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不希望此动作, 那么提供 URL 。

您也可以选择提供 `dataKey` 使用。 这使得您只能提取 JSON 的一部分并将其存储在缓存中, 而不是整个文件。 例如, 如果您的 JSON 数据有这样的结构 :

```json
{
    "level1": {
        "baddies": {
            "aliens": {},
            "boss": {}
        }
    },
    "level2": {},
    "level3": {}
}
```

而你只想把`boss`的数据存储在缓存中,然后就可以通过`level1.baddies.boss`作为`dataKey`.

注意: 只有在将 Pack 文件类型构建为 Phaser 时, 才有装入这类文件的能力。 默认构建中可使用, 但可排除自定义构建中的内容 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.PackFileConfig](/api/typedef/types-loader-filetypes#packfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.PackFileConfig](/api/typedef/types-loader-filetypes#packfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.json`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. json" 。 |
| dataKey | string | 是 | 当 JSON 文件加载时, 将只存储此属性到缓存 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/PackFile.js#L85](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PackFile.js#L85)  
引入版本：3.7.0


---

### plugin {#plugin}

#### \<instance> plugin(key, [url], [start], [mapping], [xhrSettings]) {#instance-pluginkey-url-start-mapping-xhrsettings}


**说明:**

在当前负载队列中添加插件脚本文件,或插件文件的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.plugin('modplayer', 'plugins/ModPlayer.js');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串, 并且还没有被装入器中的另一个文件使用 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.plugin({
    key: 'modplayer',
    url: 'plugins/ModPlayer.js'
});
```

详见`Phaser.Types.Loader.FileTypes.PluginFileConfig`的文件.

装入文件完成后, 将自动通过 `document.createElement('script')` 转换为脚本元素。 它的语言将设置为 JavaScript , `defer` 将设定为假, 由此生成的元素将附加到 `document.head` 。 脚本中的任何代码都会执行。 然后传递到 Phaser 插件Cache. register 方法 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 没有指定, 装入器将取下密钥并创建文件名。 例如, 如果密钥是“ alien” 且没有给出 URL, 那么装入器将设置 URL 以“ alien. js ” 。 它会总是添加 `.js` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它 。 如果您不希望此动作, 那么就提供 URL 。

注意: 只有在插件文件类型已建入 Phaser 时, 才有装入这类文件的能力。 默认的构建中可以使用, 但可以排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.PluginFileConfig](/api/typedef/types-loader-filetypes#pluginfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.PluginFileConfig](/api/typedef/types-loader-filetypes#pluginfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string \| function | 是 | 装入此文件的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.js`, 即如果 `key` 是“ 外国人 ” , 那么 URL 将是“ 外国人 . js ” 。 或者, 插件功能 。 |
| start | boolean | 是 | 装入后自动启动插件吗 ? |
| mapping | string | 是 | 如果要将此插件注入到场景中, 这就是所用的属性密钥 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/PluginFile.js#L137](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/PluginFile.js#L137)  
引入版本：3.0.0


---

### removePack {#removePack}

#### \<instance> removePack(packKey, [dataKey]) {#instance-removepackpackkey-datakey}


**说明:**

删除资产包中列出的资源。

这将动画从动画管理器中移除, 纹理管理器中移除, 而将其它所有资产从各自的缓存中移除。 如果 Pack 存在, 它不会从 JSON 缓存中移除它本身 。 如果 Pack 包含另一个 Pack, 其资源也将被移除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| packKey | string \| object | 否 | JSON 缓存中的资产包的密钥, 或 Pack 文件数据 。 |
| dataKey | string | 是 | Pack 数据中的一个键, 如果您想要处理其中的一节 。 |


> 源码：[src/loader/LoaderPlugin.js#L699](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L699)  
引入版本：3.85.0


---

### reset {#reset}

#### \<instance> reset() {#instance-reset}


**说明:**

重装装货机 。

这将清除所有列表并重置基础 URL,路径和前缀 。

警告:如果装入器正在下载文件,或者其队列中有文件,它们将被中止.


> 源码：[src/loader/LoaderPlugin.js#L1227](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L1227)  
引入版本：3.0.0


---

### save {#save}

#### \<instance> save(data, [filename], [filetype]) {#instance-savedata-filename-filetype}


**说明:**

导致浏览器将给定的数据保存为默认下载文件夹的文件.

创建 DOM 级主锚链接, 指定它为 `download` 锚, 设定 href 为一个基于给定数据的 ObjectURL, 然后引用点击事件 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | * | 否 |  | 数据将被保存。 将会通过 URL. createObjectURL 传递 。 |
| filename | string | 是 | "file.json" | 要保存文件为的文件名 。 |
| filetype | string | 是 | "application/json" | 保存文件时要使用的文件类型。 默认为 JSON 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 此装入器插件 。


> 源码：[src/loader/LoaderPlugin.js#L1193](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L1193)  
引入版本：3.0.0


---

### saveJSON {#saveJSON}

#### \<instance> saveJSON(data, [filename]) {#instance-savejsondata-filename}


**说明:**

将给定的 JavaScript 对象转换为 JSON 并触发浏览器下载,以便在当地保存.

数据必须是可以通过`JSON.stringify`序列化的普通的JavaScript对象。不要通过预先串联的JSON字符串。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| data | * | 否 |  | JSON的数据, 已解析完毕. |
| filename | string | 是 | "file.json" | 保存 JSON 文件的名称为 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 此装入器插件 。


> 源码：[src/loader/LoaderPlugin.js#L1175](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L1175)  
引入版本：3.0.0


---

### sceneFile {#sceneFile}

#### \<instance> sceneFile(key, [url], [xhrSettings]) {#instance-scenefilekey-url-xhrsettings}


**说明:**

在当前负载队列中添加外部 Scene 文件,或 Scene 文件的数组 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.sceneFile('Level1', 'src/Level1.js');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局场景管理器中 。

对于场景文件来说,关键是密钥要与JavaScript文件中的类名相匹配.

例如这里是源文件 :

```javascript
class ExternalScene extends Phaser.Scene {

    constructor ()
    {
        super('myScene');
    }

}
```

因为类叫做`ExternalScene`, 和你装入时必须用的完全一样的密钥:

```javascript
function preload ()
{
    this.load.sceneFile('ExternalScene', 'src/yourScene.js');
}
```

在场景管理器内使用的密钥可以设置为同一键,也可以在场景构造器中进行重置,如我们在上面的例子中所做的那样,场景密钥被修改为`myScene`.

键在正在装入的文件和在 Scene 管理器中已经存在的 Scases 中都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换一个已有的文件, 请在装入新文件之前先从 Scene 管理程式中删除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.sceneFile({
    key: 'Level1',
    url: 'src/Level1.js'
});
```

详见`Phaser.Types.Loader.FileTypes.SceneFileConfig`的文件.

文件装入完成后, 将添加到场景管理器中 。

```javascript
this.load.sceneFile('Level1', 'src/Level1.js');
// and later in your game ...
this.scene.start('Level1');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将预设为此文件密钥。 例如, 如果前缀是 `WORLD1.` , 而密钥是 `Story`, 最后的密钥是 `WORLD1.Story`, 您会用它从 Scene 管理器中获取文本 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ 故事 ” 而未给出 URL, 那么装入器会设置 URL 为“ story.js ” 。 它会总是添加 `.js` 作为扩展, 但是如果使用对象而不是方法参数, 则会覆盖它 。 如果您不希望此动作, 则会提供 URL 。

注意: 只有当 Scene 文件类型已建入 Phaser 时, 才能装入这类文件。 默认的构建中可以使用, 但可以排除自定义构建中的内容 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.SceneFileConfig](/api/typedef/types-loader-filetypes#scenefileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.SceneFileConfig](/api/typedef/types-loader-filetypes#scenefileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.js`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. js" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/SceneFile.js#L109](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/SceneFile.js#L109)  
引入版本：3.16.0


---

### scenePlugin {#scenePlugin}

#### \<instance> scenePlugin(key, [url], [systemKey], [sceneKey], [xhrSettings]) {#instance-scenepluginkey-url-systemkey-scenekey-xhrsettings}


**说明:**

在当前负载队列中添加一个场景插件脚本文件,或插件文件的阵列。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.scenePlugin('ModPlayer', 'plugins/ModPlayer.js', 'modPlayer', 'mods');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串, 并且还没有被装入器中的另一个文件使用 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.scenePlugin({
    key: 'modplayer',
    url: 'plugins/ModPlayer.js'
});
```

详见`Phaser.Types.Loader.FileTypes.ScenePluginFileConfig`的文件.

一旦文件装入完成, 将自动通过 `document.createElement('script')` 转换成脚本元素。 它的语言将设置为 JavaScript, `defer` , 将设定为假, 由此生成的元素将附加到 `document.head` 。 脚本中的任何代码都会执行。 然后使用文件密钥从全局的 `window` 对象中检索, 并通过使用 `installScenePlugin` 的插件管理器安装到场景 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 没有指定, 装入器将取下密钥并创建文件名。 例如, 如果密钥是“ alien” 且没有给出 URL, 那么装入器将设置 URL 以“ alien. js ” 。 它会总是添加 `.js` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它 。 如果您不希望此动作, 那么就提供 URL 。

注意: 只有在将脚本文件类型构建为 Phaser 时, 才有装入这类文件的能力。 它在默认构建中可用, 但可以排除在自定义构建中 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.ScenePluginFileConfig](/api/typedef/types-loader-filetypes#scenepluginfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.ScenePluginFileConfig](/api/typedef/types-loader-filetypes#scenepluginfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string \| function | 是 | 装入此文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.js`, 即如果 `key` 是“ 外国人 ” , 那么 URL 将是“ 外国人 . js ” 。 或者, 设置为插件功能 。 |
| systemKey | string | 是 | 如果要将此插件添加到 Scene.Systems 中, 此插件的属性密钥 。 |
| sceneKey | string | 是 | 如果要将此插件添加到场景中, 这是它属性的密钥 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/ScenePluginFile.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/ScenePluginFile.js#L129)  
引入版本：3.8.0


---

### script {#script}

#### \<instance> script(key, [url], [type], [xhrSettings]) {#instance-scriptkey-url-type-xhrsettings}


**说明:**

在当前负载队列中添加脚本文件,或脚本文件的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.script('aliens', 'lib/aliens.js');
}
```

如果脚本文件包含一个模块,那么您应该指定使用“类型”参数:

```javascript
function preload ()
{
    this.load.script('aliens', 'lib/aliens.js', 'module');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串, 并且还没有被装入器中的另一个文件使用 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.script({
    key: 'aliens',
    url: 'lib/aliens.js',
    type: 'script' // or 'module'
});
```

详见`Phaser.Types.Loader.FileTypes.ScriptFileConfig`的文件.

一旦文件装入完成, 它将通过 `document.createElement('script')` 自动转换成脚本元素。 它的语言将被设定为 JavaScript , `defer` 会被设定为虚假, 然后产生的元素将被附加到 `document.head` 中。 脚本中的任何代码都会被执行 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 没有指定, 装入器将取下密钥并创建文件名。 例如, 如果密钥是“ alien” 且没有给出 URL, 那么装入器将设置 URL 以“ alien. js ” 。 它会总是添加 `.js` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它 。 如果您不希望此动作, 那么就提供 URL 。

注意: 只有在将脚本文件类型构建为 Phaser 时, 才有装入这类文件的能力。 它在默认构建中可用, 但可以排除在自定义构建中 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.ScriptFileConfig](/api/typedef/types-loader-filetypes#scriptfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.ScriptFileConfig](/api/typedef/types-loader-filetypes#scriptfileconfig)> | 否 |  | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 |  | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.js`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. js" 。 |
| 类型 | string | 是 | "'script'" | 脚本类型。 如果文件包含导出模块, 则应该为经典 JavaScript 的“ 标语 ” , 或“ 模块 ” 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/ScriptFile.js#L100](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/ScriptFile.js#L100)  
引入版本：3.0.0


---

### scripts {#scripts}

#### \<instance> scripts(key, [url], [extension], [xhrSettings]) {#instance-scriptskey-url-extension-xhrsettings}


**说明:**

在当前负载队列中添加脚本文件的数组。

与 `ScriptFile` 文件类型的区别在于您给此方法提供了一系列脚本, 然后按此顺序处理脚本 _ 准确_ 这样您就可以装入一组可能互相依赖的脚本, 而不用担心传统脚本加载的同位素性质 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.scripts('PostProcess', [
        'libs/shaders/CopyShader.js',
        'libs/postprocessing/EffectComposer.js',
        'libs/postprocessing/RenderPass.js',
        'libs/postprocessing/MaskPass.js',
        'libs/postprocessing/ShaderPass.js',
        'libs/postprocessing/AfterimagePass.js'
   ]);
}
```

在以上代码中,脚本文件都将平行加载,但只按数组给出的确切顺序处理(即引用).

文件是 ** not ** 立即装入。 装入器启动时, 或者已经运行时, 当下一个免费装入槽可用时, 将添加到准备装入的队列中。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。由于文件被排队,这意味着您无法在调用此方法后立即使用文件,但必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串, 并且还没有被装入器中的另一个文件使用 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.scripts({
    key: 'PostProcess',
    url: [
        'libs/shaders/CopyShader.js',
        'libs/postprocessing/EffectComposer.js',
        'libs/postprocessing/RenderPass.js',
        'libs/postprocessing/MaskPass.js',
        'libs/postprocessing/ShaderPass.js',
        'libs/postprocessing/AfterimagePass.js'
       ]
});
```

详见`Phaser.Types.Loader.FileTypes.MultiScriptFileConfig`的文件.

一旦所有文件装入完毕, 将自动通过 `document.createElement('script')` 转换成脚本元素。 它们的语言将设置为 JavaScript , `defer` 会被设定为虚假, 然后生成的元素将附加到 `document.head` 。 脚本中的任何代码都会被执行。 这样做的顺序是url 阵列中指定文件的确切顺序 。

URL可以是相对的或绝对的。如果URL是相对的,则`Loader.baseURL`和`Loader.path`的值会被预设为它们.

注意: 只有在多脚本文件类型已建入 Phaser 时, 才能装入这类文件。 默认的构建中可以使用, 但可以排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.MultiScriptFileConfig](/api/typedef/types-loader-filetypes#multiscriptfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.MultiScriptFileConfig](/api/typedef/types-loader-filetypes#multiscriptfileconfig)> | 否 |  | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | Array.\<string> | 是 |  | 一组绝对或相对的 URL 来从中加载脚本文件。它们按数组中给出的顺序处理 。 |
| extension | string | 是 | "'js'" | 如果没有提供 URL , 则使用默认文件扩展名 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 |  | 专门为这些文件设置额外的 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/MultiScriptFile.js#L113](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/MultiScriptFile.js#L113)  
引入版本：3.17.0


---

### setBaseURL {#setBaseURL}

#### \<instance> setBaseURL([url]) {#instance-setbaseurlurl}


**说明:**

如果您想要在此设置任何资产路径之前附加一个 URL 。

如果允许在游戏代码外配置资产库 URL, 则有用 。

一旦设置了一个基础 URL, 它会影响装入器从该点开始加载的每个文件。 它会_ not_ 更改任何文件_ 已经加载 。 要重设它, 请使用这个没有参数的调用方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| url | string | 是 | 要使用的 URL。 留空以重置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 此加载器对象 。


> 源码：[src/loader/LoaderPlugin.js#L398](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L398)  
引入版本：3.0.0


---

### setCORS {#setCORS}

#### \<instance> setCORS([crossOrigin]) {#instance-setcorscrossorigin}


**说明:**

设置在装入文件时使用的交叉来源资源共享值 。

文件可以通过在文件配置中指定一个替代的`crossOrigin`值,在每份文件的基础上覆盖这个值.

一旦设定了 COR , 它将会影响装入器从此加载的每个文件, 只要它们没有自己的 COR 设置。 要重设它, 请使用这个没有参数的调用 。

有关COR的更多详情,请参见[https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| crossOrigin | string | 是 | 负载请求中用于 `crossOrigin` 属性的值 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 此加载器对象 。


> 源码：[src/loader/LoaderPlugin.js#L491](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L491)  
引入版本：3.0.0


---

### setPath {#setPath}

#### \<instance> setPath([path]) {#instance-setpathpath}


**说明:**

`path`的值如果设定,则放在给定的 _ relative_ 文件路径之前。例如:

```javascript
this.load.setPath("images/sprites/");
this.load.image("ball", "ball.png");
this.load.image("tree", "level1/oaktree.png");
this.load.image("boom", "[http://server.com/explode.png](http://server.com/explode.png)");
```

将会从 `images/sprites/ball.png` 装入 `ball` 文件, 从树上装入 `images/sprites/level1/oaktree.png` 但文件 `boom` 将会从给定的 URL 装入,因为它是一个绝对的 URL 。

请注意,路径在文件名前添加,但 * 在 * 之后的 baseURL(如果设置了) 。

一旦设置了路径, 它将影响从此开始添加到加载器的每个文件。 它会_ not_ 改变负载队列中的任何文件_ alady_。 要重设它, 请使用这个没有参数的调用方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| path | string | 是 | 使用路径。 留空以重置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 此加载器对象 。


> 源码：[src/loader/LoaderPlugin.js#L427](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L427)  
引入版本：3.0.0


---

### setPrefix {#setPrefix}

#### \<instance> setPrefix([prefix]) {#instance-setprefixprefix}


**说明:**

一个可选的前缀,它自动准备到每个文件密钥的开始.

如果前缀是`MENU.`,你用键“背景”加载一个图像,那么产生的键将是`MENU.Background`。

一旦设置了前缀, 它将影响从此添加到加载器的每个文件。 它确实_ not_ 改变负载队列中的任何文件_ alady_。 要重设它, 请使用这个没有参数的调用方法 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| prefix | string | 是 | 使用的前缀。 留空以重置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 此加载器对象 。


> 源码：[src/loader/LoaderPlugin.js#L467](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L467)  
引入版本：3.7.0


---

### spritesheet {#spritesheet}

#### \<instance> spritesheet(key, [url], [frameConfig], [xhrSettings]) {#instance-spritesheetkey-url-frameconfig-xhrsettings}


**说明:**

在当前负载队列中添加一个 Sprite 工作表图像,或 Sprite 工作表图像的阵列。

Phaser中的“ Sprite Sheet” 一词是指固定大小的工作表。工作表中的每个框架都与数字完全相同,而您使用数字而不是框架名称来引用这些框架。这与文字图集不同,因为其包装方式占用的空间最小,而不是数字。有些文章和软件使用“ Sprite Sheard”一词来表示文字图集,所以请了解您正在实际装入的文件类型。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.spritesheet('bot', 'images/robot.png', { frameWidth: 32, frameHeight: 38 });
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

Phaser可以装入所有常见的图像类型: png, jpg, gif 和浏览器可以本地处理的任何其他格式。 如果您尝试装入动画的 gif , 将只提供第一个帧。 浏览器不会在本地支持将动画的 gifs 播放到 Canvas 元素 。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.spritesheet({
    key: 'bot',
    url: 'images/robot.png',
    frameConfig: {
        frameWidth: 32,
        frameHeight: 38,
        startFrame: 0,
        endFrame: 8
    }
});
```

详见`Phaser.Types.Loader.FileTypes.SpriteSheetFileConfig`的文件.

文件装入完成后,您可以通过引用游戏对象的密钥,将其作为游戏对象的纹理:

```javascript
this.load.spritesheet('bot', 'images/robot.png', { frameWidth: 32, frameHeight: 38 });
// and later in your game ...
this.add.image(x, y, 'bot', 0);
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `PLAYER.` , 而密钥是 `Running` , 则最后的密钥是 `PLAYER.Running`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ alien” 且没有给定 URL, 那么装入器会设置 URL 为“ alien. png ” 。 它会总是添加 `.png` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想这样做, 那么就提供 URL 。

Phaser还支持自动加载相关的普通地图。如果您有一张普通地图可以随此图像一起运行,那么您可以通过提供一个阵列来指定它,作为`url`,其中第二个元素是普通地图:

```javascript
this.load.spritesheet('logo', [ 'images/AtariLogo.png', 'images/AtariLogo-n.png' ], { frameWidth: 256, frameHeight: 80 });
```

或者,如果使用配置对象使用 `normalMap` 属性:

```javascript
this.load.spritesheet({
    key: 'logo',
    url: 'images/AtariLogo.png',
    normalMap: 'images/AtariLogo-n.png',
    frameConfig: {
        frameWidth: 256,
        frameHeight: 80
    }
});
```

普通地图文件在路径,baseURL,CORS和XHR设置方面与图像文件条件相同. 普通地图只是WebGL的特性.

注意: 只有在Sprite工作表文件类型已建入 Phaser 时, 才能装入这类文件。 它在默认的构建中可用, 但可以从自定义构建中排除 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.SpriteSheetFileConfig](/api/typedef/types-loader-filetypes#spritesheetfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.SpriteSheetFileConfig](/api/typedef/types-loader-filetypes#spritesheetfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](/api/typedef/types-loader-filetypes#imageframeconfig) | 是 | 帧配置对象,至少应该有`frameWidth`属性. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/SpriteSheetFile.js#L87](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/SpriteSheetFile.js#L87)  
引入版本：3.0.0


---

### start {#start}

#### \<instance> start() {#instance-start}


**说明:**

启动装入器运行。 这将重置进度和总和, 然后释放一个 `start` 事件。 如果队列中没有任何内容, 装入器将立即完成, 否则它会开始装入第一批文件 。

如果队列被您所使用 `preload` 方法所覆盖, 装入器将自动启动 。

然而,除此之外,你需要叫这个方法来开始它.

如果装入器已经在运行此方法, 将简单地返回 。


**Fires:** [Phaser.Loader.Events#event:START](/api/event/loader-events#start)


> 源码：[src/loader/LoaderPlugin.js#L899](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L899)  
引入版本：3.0.0


---

### svg {#svg}

#### \<instance> svg(key, [url], [svgConfig], [xhrSettings]) {#instance-svgkey-url-svgconfig-xhrsettings}


**说明:**

在当前负载队列中添加 SVG 文件, 或 SVG 文件的数组。 当文件被装入时, 将将其渲染成位图纹理并存储在纹理管理器中 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.svg('morty', 'images/Morty.svg');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.svg({
    key: 'morty',
    url: 'images/Morty.svg'
});
```

详见`Phaser.Types.Loader.FileTypes.SVGFileConfig`的文件.

文件装入完成后,您可以通过引用游戏对象的密钥,将其作为游戏对象的纹理:

```javascript
this.load.svg('morty', 'images/Morty.svg');
// and later in your game ...
this.add.image(x, y, 'morty');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 指定不在此指定, 装入器将取下密钥并创建文件名。 例如, 如果密钥是“ alien” 且没有给出 URL, 那么装入器将设置 URL 为“ alien. svg ” 。 它会总是添加 `.svg` , 但它会使用对象而不是方法参数来覆盖它。 如果您不想这样做, 那么就提供 URL 。

您可以在装入 SVG 文件时选择通过 SVG 调整配置对象。 默认情况下, SVG 将变成 SVG 文件属性中定义的相同大小的纹理。 但是, 这并不总是可取的。 您可能希望将 SVG ( 下或上) 的大小调整, 以提高纹理清晰度, 或降低纹理内存消耗 。 您可以指定一个精确的宽度和高度, 将 SVG 的大小调整为:

```javascript
function preload ()
{
    this.load.svg('morty', 'images/Morty.svg', { width: 300, height: 600 });
}
```

或当使用配置对象时 :

```javascript
this.load.svg({
    key: 'morty',
    url: 'images/Morty.svg',
    svgConfig: {
        width: 300,
        height: 600
    }
});
```

或者,您可以只提供一个比例系数:

```javascript
function preload ()
{
    this.load.svg('morty', 'images/Morty.svg', { scale: 2.5 });
}
```

或当使用配置对象时 :

```javascript
this.load.svg({
    key: 'morty',
    url: 'images/Morty.svg',
    svgConfig: {
        scale: 2.5
    }
});
```

如果所有标度,宽度和高度值都给出,则标度具有优先级,宽度和高度值被忽略.

注意: 只有在SVG 文件类型已建入 Phaser 时, 才能装入这类文件。 默认构建中已有此功能, 但可排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.SVGFileConfig](/api/typedef/types-loader-filetypes#svgfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.SVGFileConfig](/api/typedef/types-loader-filetypes#svgfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL 。 如果未定义或 `null` , 则会设置为 `<key>.svg`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. svg" 。 |
| svgConfig | [Phaser.Types.Loader.FileTypes.SVGSizeConfig](/api/typedef/types-loader-filetypes#svgsizeconfig) | 是 | svg 大小配置对象 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/SVGFile.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/SVGFile.js#L202)  
引入版本：3.0.0


---

### text {#text}

#### \<instance> text(key, [url], [xhrSettings]) {#instance-textkey-url-xhrsettings}


**说明:**

在当前负载队列中添加文本文件或文本文件的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.text('story', 'files/IntroStory.txt');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局文本缓存。 密钥在装入的文件和文本缓存中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从文本缓存中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.text({
    key: 'story',
    url: 'files/IntroStory.txt'
});
```

详见`Phaser.Types.Loader.FileTypes.TextFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.text('story', 'files/IntroStory.txt');
// and later in your game ...
var data = this.cache.text.get('story');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将被预设为此文件密钥。 例如, 如果前缀为 `LEVEL1.` 而密钥为 `Story`, 最后的密钥为 `LEVEL1.Story`, 您会用此来从文本缓存中获取文本 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 指定不 , 装入器 将取下 URL 并创建文件名。 例如, 如果密钥是 “ 故事 ” 而未给出 URL , 那么装入器 将 URL 设置为 “ story. txt ” 。 它会总是添加 `.txt`Z 以作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它 。 如果您不想使用此操作, 那么就提供 URL 。

注意: 只有在文本文件类型已建入 Phaser 时, 才有装入这类文件的能力。 它在默认的构建中可用, 但可以排除在自定义构建之外 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.TextFileConfig](/api/typedef/types-loader-filetypes#textfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.TextFileConfig](/api/typedef/types-loader-filetypes#textfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 装入此文件的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.txt`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. txt" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/TextFile.js#L95](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TextFile.js#L95)  
引入版本：3.0.0


---

### texture {#texture}

#### \<instance> texture(key, [url], [xhrSettings]) {#instance-texturekey-url-xhrsettings}


**说明:**

在当前负载队列中添加压缩纹理文件。 此特性仅为 WebGL 。

这种方法需要一个密钥和一个配置对象,它列出了与之相关的不同格式和文件.

纹理格式对象应当以GPU优先级顺序排序,以IMG为最后一个条目.

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
preload ()
{
    this.load.texture('yourPic', {
        ASTC: { type: 'PVR', textureURL: 'pic-astc-4x4.pvr' },
        PVRTC: { type: 'PVR', textureURL: 'pic-pvrtc-4bpp-rgba.pvr' },
        S3TC: { type: 'PVR', textureURL: 'pic-dxt5.pvr' },
        IMG: { textureURL: 'pic.png' }
    });
```

如果您想要装入纹理图集, 请提供 `atlasURL` 属性 :

```javascript
preload ()
{
    const path = 'assets/compressed';

    this.load.texture('yourAtlas', {
        'ASTC': { type: 'PVR', textureURL: `${path}/textures-astc-4x4.pvr`, atlasURL: `${path}/textures.json` },
        'PVRTC': { type: 'PVR', textureURL: `${path}/textures-pvrtc-4bpp-rgba.pvr`, atlasURL: `${path}/textures-pvrtc-4bpp-rgba.json` },
        'S3TC': { type: 'PVR', textureURL: `${path}/textures-dxt5.pvr`, atlasURL: `${path}/textures-dxt5.json` },
        'IMG': { textureURL: `${path}/textures.png`, atlasURL: `${path}/textures.json` }
    });
}
```

如果您希望从Texture Packer Pro 中导出一个多图集,则使用 `multiAtlasURL` 属性:

```javascript
preload ()
{
    const path = 'assets/compressed';

    this.load.texture('yourAtlas', {
        'ASTC': { type: 'PVR', multiAtlasURL: `${path}/textures.json`, multiPath: `${path}` },
        'PVRTC': { type: 'PVR', multiAtlasURL: `${path}/textures-pvrtc-4bpp-rgba.json`, multiPath: `${path}` },
        'S3TC': { type: 'PVR', multiAtlasURL: `${path}/textures-dxt5.json`, multiPath: `${path}` },
        'IMG': { multiAtlasURL: `${path}/textures.json`, multiPath: `${path}` }
    });
}
```

在装入多图集时, 您不需要指定 `textureURL` 属性, 因为将从 JSON 文件读取 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.texture({
    key: 'yourPic',
    url: {
        ASTC: { type: 'PVR', textureURL: 'pic-astc-4x4.pvr' },
        PVRTC: { type: 'PVR', textureURL: 'pic-pvrtc-4bpp-rgba.pvr' },
        S3TC: { type: 'PVR', textureURL: 'pic-dxt5.pvr' },
        IMG: { textureURL: 'pic.png' }
   }
});
```

详见`Phaser.Types.Loader.FileTypes.CompressedTextureFileConfig`的文件.

您为此功能提供的格式数量由您决定, 但您应当确保您酌情覆盖主平台 。

如果浏览器无法装入提交到此功能的其他格式, “IMG” 条目会倒置到 JPG 或 PNG 。 您应该始终包含此内容, 尽管它是可选的 。

Phaser支持同时加载PVR和KTX容器格式。在这些格式中,它可以解析以下纹理压缩格式:

ETC ETC1 ATC ATC ABTC PVTC PVRTC S3TC S3TCSRGB 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联赛 中超联 中超联 中超联赛 中超联 中超联赛 中超联赛 中超联赛 中超联 中超联 中超联赛 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联 中超联

有关压缩纹理的好处的更多信息,请参见以下文章: 压缩纹理的优点,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹理的纹理,指由压缩纹的纹理,指由压缩纹纹理的纹理,指由压缩纹理的纹理,指由压缩纹纹纹的纹素,指由压缩的纹理,指由压缩纹纹纹的纹素,指由压缩的纹的纹素,指由纹的纹理组成的纹理组成的纹理,指由纹纹纹素,指由纹纹的纹的纹的,指由纹的纹的纹的纹的,指由纹的,指由纹的纹的,指的纹的纹的纹的,指的,指的纹的,指的,指的纹的,指的纹的,指的纹的,指由色的,指的,指由纹的,指的,指由纹的纹的,指的,指的纹的,指的,指的,指的纹的,指的,指的,指的.的,指的,指的: : : : : : : : : 纹的纹的纹的: : : 纹的纹的纹的纹的纹的纹的纹的纹的纹的,指纹的纹的纹的,指的,指的,指的纹的,指的,指的纹的,指的,指的,指的,指的,指的,指的,

2020年纹理压缩(图).https://aras-p.info/blog/2020/12/08/Texture-Compression-in-2020/) 压缩的 GPU 纹理格式( Namehttps://themaister.net/blog/2020/08/12/compressed-gpu-texture-formats-a-review-and-compute-shader-decoders-part-1/)

要创建压缩纹理文件,使用第三方应用程序,例如:

纹理包装器( Namehttps://www.codeandweb.com/texturepacker/tutorials/how-to-create-sprite-sheets-for-phaser3?utm_source=ad&utm_medium=banner&utm_campaign=phaser-2018-10-16) PVRTex工具( 光电图)https://developer.imaginationtech.com/pvrtextool/) - 可供视窗使用, macOS 和 Linux. ATC 编码器( 自动编码器)https://github.com/ARM-software/astc-encoder)

压缩纹理会比普通纹理显得更暗。 这是因为Web使用sRGB色空间, 但压缩纹理被取样为线性色空间。 在压缩前, 您必须调整纹理, 以更轻一些 。 请参看 [https://imagemagick.org/Usage/color_basics/#srgb](https://imagemagick.org/Usage/color_basics/#srgb) 。 您可以使用 ImageMagick (https://imagemagick.org/index.php)) 来完成此任务 :

`magick input.png -set colorspace RGB -colorspace sRGB output.png`

您必须确保压缩纹理符合WebGL和Phaser的下列标准: 1.

- PVRTC必须具有2个宽度和高度的功率.

- MIMPMap如果存在,必须具有2个宽度和高度的功率.

- S3TC,S3TCSRGB,RGTC,以及BPTC必须具有宽度和高度可分辨为4的高度.

- ASTC 必须有无符号的常态字节( UNorm) 的通道类型。 事实上, 所有压缩纹理都应该是 UNorm, 但 ASTC 提供了许多其他选项 。

如果怀疑,两个决议的力量总是安全下注。

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件的密钥。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Data` , 最后的密钥是 `LEVEL1.Data` , 您会用它从 纹理 管理器 中获取文本 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

与Phaser中的其他文件加载器不同,URL必须包含文件扩展名.

注意: 只有压缩的纹理文件类型已建入 Phaser , 才能装入这类文件。 默认的构建中可以使用, 但可以排除自定义构建中的内容 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.CompressedTextureFileConfig](/api/typedef/types-loader-filetypes#compressedtexturefileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.CompressedTextureFileConfig](/api/typedef/types-loader-filetypes#compressedtexturefileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | [Phaser.Types.Loader.FileTypes.CompressedTextureFileConfig](/api/typedef/types-loader-filetypes#compressedtexturefileconfig) | 是 | 压缩纹理配置对象。 如果通过一个配置对象作为 `key` 参数, 则不需要 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/CompressedTextureFile.js#L357](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/CompressedTextureFile.js#L357)  
引入版本：3.60.0


---

### tilemapCSV {#tilemapCSV}

#### \<instance> tilemapCSV(key, [url], [xhrSettings]) {#instance-tilemapcsvkey-url-xhrsettings}


**说明:**

在当前负载队列中添加 CSV Tilemap 文件,或 CSV 文件的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.tilemapCSV('level1', 'maps/Level1.csv');
}
```

Tilemap CSV数据可以在文本编辑器中创建,也可以在第三方的app中以CSV的形式输出.

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局 Tilemap 缓存。 密钥在装入文件和已经存在于 Tilemap 补存的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从 Tilemap  快取中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.tilemapCSV({
    key: 'level1',
    url: 'maps/Level1.csv'
});
```

详见`Phaser.Types.Loader.FileTypes.TilemapCSVFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.tilemapCSV('level1', 'maps/Level1.csv');
// and later in your game ...
var map = this.make.tilemap({ key: 'level1' });
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将准备到此文件密钥。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Story` , 最后的密钥将是 `LEVEL1.Story`, 这就是您从 Tilemap 缓存中获取文本时所使用的 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器会从中取下此键并创建文件名。 例如, 如果密钥是“ 级别 ” 而未给出 URL, 那么装入器会设置 URL 为“ 级别 . csv ” 。 它会总是将 `.csv` 添加为扩展名, 尽管如果使用对象而不是方法参数, 则可以覆盖它 。 如果您不想要此动作, 则提供 URL 。

注意: 只有在将 Tilemap CSV 文件类型构建为 Phaser 时, 才有装入这类文件的能力。 默认的构建中可以使用, 但可以排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.TilemapCSVFileConfig](/api/typedef/types-loader-filetypes#tilemapcsvfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.TilemapCSVFileConfig](/api/typedef/types-loader-filetypes#tilemapcsvfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则会设置为 `<key>.csv`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. csv" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/TilemapCSVFile.js#L104](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TilemapCSVFile.js#L104)  
引入版本：3.0.0


---

### tilemapImpact {#tilemapImpact}

#### \<instance> tilemapImpact(key, [url], [xhrSettings]) {#instance-tilemapimpactkey-url-xhrsettings}


**说明:**

在当前负载队列中添加一个 impact.js Tilemap 文件,或地图文件的数组 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.tilemapImpact('level1', 'maps/Level1.json');
}
```

影响Tilemap数据由名为Weltmeister的Information.js地图编辑器创建.

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局 Tilemap 缓存。 密钥在装入文件和已经存在于 Tilemap 补存的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从 Tilemap  快取中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.tilemapImpact({
    key: 'level1',
    url: 'maps/Level1.json'
});
```

详见`Phaser.Types.Loader.FileTypes.TilemapImpactFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.tilemapImpact('level1', 'maps/Level1.json');
// and later in your game ...
var map = this.make.tilemap({ key: 'level1' });
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将准备到此文件密钥。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Story` , 最后的密钥将是 `LEVEL1.Story`, 这就是您从 Tilemap 缓存中获取文本时所使用的 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 没有指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ 级别” , 而未给出 URL, 那么装入器将设置 URL 为“ 级别 。 json ” 。 它会总是将 `.json` 添加为扩展名, 但是如果使用对象而不是方法参数, 则会覆盖它。 如果您不想这样做, 那么就提供 URL 。

注意: 只有在将 Tilemap 撞击文件类型构建为 Phaser 时, 才能具备装入这类文件的能力。 默认构建中可使用, 但可排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.TilemapImpactFileConfig](/api/typedef/types-loader-filetypes#tilemapimpactfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.TilemapImpactFileConfig](/api/typedef/types-loader-filetypes#tilemapimpactfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.json`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. json" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/TilemapImpactFile.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TilemapImpactFile.js#L61)  
引入版本：3.7.0


---

### tilemapTiledJSON {#tilemapTiledJSON}

#### \<instance> tilemapTiledJSON(key, [url], [xhrSettings]) {#instance-tilemaptiledjsonkey-url-xhrsettings}


**说明:**

在当前负载队列中添加一个 Tiled JSON Tilemap 文件,或地图文件的数组。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.tilemapTiledJSON('level1', 'maps/Level1.json');
}
```

Tilemap数据是使用Tiled映射编辑器创建的,并选择JSON作为导出格式.

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局 Tilemap 缓存。 密钥在装入文件和已经存在于 Tilemap 补存的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从 Tilemap  快取中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.tilemapTiledJSON({
    key: 'level1',
    url: 'maps/Level1.json'
});
```

详见`Phaser.Types.Loader.FileTypes.TilemapJSONFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.tilemapTiledJSON('level1', 'maps/Level1.json');
// and later in your game ...
var map = this.make.tilemap({ key: 'level1' });
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将预设为此文件密钥。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Story`, 最后的密钥是 `LEVEL1.Story`, 您将会用此从 Tilemap 缓存中获取地图 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 没有指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ 级别” , 而未给出 URL, 那么装入器将设置 URL 为“ 级别 。 json ” 。 它会总是将 `.json` 添加为扩展名, 但是如果使用对象而不是方法参数, 则会覆盖它。 如果您不想这样做, 那么就提供 URL 。

注意: 只有将 Tilemap JSON 文件类型建入 Phaser 时, 才能具备装入这类文件的能力。 默认的构建中可以使用, 但可以排除自定义构建 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.TilemapJSONFileConfig](/api/typedef/types-loader-filetypes#tilemapjsonfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.TilemapJSONFileConfig](/api/typedef/types-loader-filetypes#tilemapjsonfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | object \| string | 是 | 从此文件加载的绝对或相对的 URL。 如果未定义或 `null` , 则它将被设定为 `<key>.json`, 即如果 `key` 是“ 外国人 ” 那么 URL 将是“ 外国人. json ” 。 或者, 一个 已形成好的 JSON 对象 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/TilemapJSONFile.js#L61](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/TilemapJSONFile.js#L61)  
引入版本：3.0.0


---

### unityAtlas {#unityAtlas}

#### \<instance> unityAtlas(key, [textureURL], [atlasURL], [textureXhrSettings], [atlasXhrSettings]) {#instance-unityatlaskey-textureurl-atlasurl-texturexhrsettings-atlasxhrsettings}


**说明:**

在当前负载队列中添加基于Unity YAML 的纹理图集,或图集阵列。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.unityAtlas('mainmenu', 'images/MainMenu.png', 'images/MainMenu.meta');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

如果您在 `preload` 之外调用此选项, 您负责在之后启动装货机, 并监视其事件, 以了解何时安全使用该资产。 请查看 Phaser.Loader.LoaderPlugin 的分类 。

Phaser期望地图集数据以YAML格式化文本文件提供,以Unity导出.

Phaser可以装入所有常见的图像类型: png,jpg,gif以及浏览器可以本土处理的任何其他格式.

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局纹理管理器。 密钥在装入文件和纹理管理器中已经显示的文件方面都应该是独一无二的。 使用已经取入的密钥装入文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件之前先从纹理管理器中移除它 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.unityAtlas({
    key: 'mainmenu',
    textureURL: 'images/MainMenu.png',
    atlasURL: 'images/MainMenu.meta'
});
```

详见`Phaser.Types.Loader.FileTypes.UnityAtlasFileConfig`的文件.

一旦地图集装入完毕,您可以通过引用游戏对象的键,将图像框用作其纹理:

```javascript
this.load.unityAtlas('mainmenu', 'images/MainMenu.png', 'images/MainMenu.meta');
// and later in your game ...
this.add.image(x, y, 'mainmenu', 'background');
```

要在地图集中找到所有可用框架的清单,请查阅您的文字图集软件。

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix` , 此值将预设到此文件密钥。 例如, 如果前缀是 `MENU.` , 而密钥是 `Background` , 则最后的密钥是 `MENU.Background`, 您会用它从纹理管理器中获取图像 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 尚未指定, 装入器将带走密钥并从中创建文件名。 例如, 如果密钥是“ alien” 且没有给定 URL, 那么装入器会设置 URL 为“ alien. png ” 。 它会总是添加 `.png` 作为扩展名, 但是如果使用对象而不是方法参数, 则可以覆盖它。 如果您不想这样做, 那么就提供 URL 。

Phaser还支持自动加载相关的普通地图。如果您有一张普通地图可以随此图像一起运行,那么您可以通过提供一个阵列来指定它,作为`url`,其中第二个元素是普通地图:

```javascript
this.load.unityAtlas('mainmenu', [ 'images/MainMenu.png', 'images/MainMenu-n.png' ], 'images/MainMenu.meta');
```

或者,如果使用配置对象使用 `normalMap` 属性:

```javascript
this.load.unityAtlas({
    key: 'mainmenu',
    textureURL: 'images/MainMenu.png',
    normalMap: 'images/MainMenu-n.png',
    atlasURL: 'images/MainMenu.meta'
});
```

普通地图文件在路径,baseURL,CORs和XHR设置方面与图像文件条件相同. 普通地图只是WebGL的特性.

注意: 只有在将Unity Atlas文件类型构建为 Phaser 时, 才能装入这类文件。 默认的构建中可以使用, 但可以排除自定义构建中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.UnityAtlasFileConfig](/api/typedef/types-loader-filetypes#unityatlasfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.UnityAtlasFileConfig](/api/typedef/types-loader-filetypes#unityatlasfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| textureURL | string \| Array.\<string> | 是 | 装入纹理图像文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.png`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. png" 。 |
| atlasURL | string | 是 | 装入纹理图集数据文件的绝对或相对的 URL。 如果未定义或 `null` , 它将被设定为 `<key>.txt`, 即如果 `key` 是“ 外国人” , 那么 URL 将是“ 外国人. txt ” 。 |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集图像文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | 用于地图集数据文件的 XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/UnityAtlasFile.js#L107](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/UnityAtlasFile.js#L107)  
引入版本：3.0.0


---

### update {#update}

#### \<instance> update() {#instance-update}


**说明:**

在装入器处于LOADING状态时,每个游戏步骤自动调用一次。检查飞行队列中是否有容量,如果有的话,请调用`checkLoadQueue`,将更多文件从待决列表中移动到活动加载中。


> 源码：[src/loader/LoaderPlugin.js#L964](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L964)  
引入版本：3.10.0


---

### updateProgress {#updateProgress}

#### \<instance> updateProgress() {#instance-updateprogress}


**说明:**

在加载过程中自动调用。 它更新了 `progress` 值, 然后释放出一个进度事件, 您可以在游戏中显示加载栏 。


**Fires:** [Phaser.Loader.Events#event:PROGRESS](/api/event/loader-events#progress)


> 源码：[src/loader/LoaderPlugin.js#L948](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L948)  
引入版本：3.0.0


---

### video {#video}

#### \<instance> video(key, [urls], [noAudio]) {#instance-videokey-urls-noaudio}


**说明:**

在当前负载队列中添加视频文件或视频文件阵列。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.video('intro', [ 'video/level1.mp4', 'video/level1.webm', 'video/level1.mov' ]);
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局视频缓存。 密钥在装入的文件和已出现在视频缓存的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从视频缓存中删除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.video({
    key: 'intro',
    url: [ 'video/level1.mp4', 'video/level1.webm', 'video/level1.mov' ],
    noAudio: true
});
```

详见`Phaser.Types.Loader.FileTypes.VideoFileConfig`的文件.

URL可以是相对的或绝对的。如果URL是相对的,则`Loader.baseURL`和`Loader.path`的值会被预设为它们.

由于支持不同视频文件类型的浏览器不同,您通常应该以多种格式提供您的视频文件. mp4, mov和webm是最常见的。 如果您提供了一系列URL, 装入器将根据浏览器支持来确定要加载的_ 1_ 文件, 从数组中的第一个开始, 并推进到尾端 。

与大多数资产类型不同,视频不需要_需要_ 预装。 您可以创建一个视频游戏对象, 然后调用其 `loadURL` 方法, 以便在运行时而不是提前装入视频 。

注意: 只有当视频文件类型已建为 Phaser 时, 才能装入这类文件。 它在默认的构建中可用, 但可以排除自定义构建中。

**参数:**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.VideoFileConfig](/api/typedef/types-loader-filetypes#videofileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.VideoFileConfig](/api/typedef/types-loader-filetypes#videofileconfig)> | 否 |  | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| urls | string \| Array.\<string> | [Phaser.Types.Loader.FileTypes.VideoFileURLConfig](/api/typedef/types-loader-filetypes#videofileurlconfig) | Array.\<[Phaser.Types.Loader.FileTypes.VideoFileURLConfig](/api/typedef/types-loader-filetypes#videofileurlconfig)> | 是 |  | 绝对或相对的URL从中加载视频文件. |
| noAudio | boolean | 是 | false | 视频是否有音频音轨? 如果您不能, 您可以启用自动播放 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/VideoFile.js#L117](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/VideoFile.js#L117)  
引入版本：3.20.0


---

### xml {#xml}

#### \<instance> xml(key, [url], [xhrSettings]) {#instance-xmlkey-url-xhrsettings}


**说明:**

在当前负载队列中添加 XML 文件,或 XML 文件的数组 。

您可以在您所在的 S`preload` 中调用这种方法, 以及您想要加载的任何其他文件 :

```javascript
function preload ()
{
    this.load.xml('wavedata', 'files/AlienWaveData.xml');
}
```

文件是 ** not ** 立即装入。 它会添加到准备装入的队列中, 要么是装入器启动时, 要么是已经运行, 要么是下一个空载槽可用时。 如果您从场景内调用此选项, 则会自动发生 。 `preload` 方法,或相关的调回。因为文件排队,这意味着您不能在调用此方法后立即使用文件,而是必须等待文件完成。 Phaser 场景是您在场景中装入资产 `preload` 方法,然后当场景 `create` 方法被称作你保证所有这些资产都已经准备好使用并装入。

密钥必须是独一无二的字符串。 它用于在成功加载时将文件添加到全局 XML 缓存中。 密钥在装入的文件和已经出现在 XML 缓缓存中的文件方面都应该是独一无二的。 使用已经取入的密钥加载文件将会导致警告。 如果您想要替换已有文件, 请在装入新文件前先从 XML 缓处理中移除 。

您可以不通过参数而通过配置对象, 例如:

```javascript
this.load.xml({
    key: 'wavedata',
    url: 'files/AlienWaveData.xml'
});
```

详见`Phaser.Types.Loader.FileTypes.XMLFileConfig`的文件.

文件装入完成后, 您可以使用它的缓存键访问它 :

```javascript
this.load.xml('wavedata', 'files/AlienWaveData.xml');
// and later in your game ...
var data = this.cache.xml.get('wavedata');
```

如果您在加载器中指定了前缀, 通过 `Loader.setPrefix`, 此值将被预设为此文件密钥。 例如, 如果前缀是 `LEVEL1.` , 而密钥是 `Waves`, 则 最终密钥是 `LEVEL1.Waves`, 您将使用此来从 XML 缓存中获取文本 。

URL可以是相对的或绝对的。 如果URL是相对的, 则`Loader.baseURL` 和 `Loader.path` 的值将会被预设到它 。

如果 URL 未指定, 装入器将取下密钥并创建文件名。 例如, 如果密钥是“ 数据 ” 而未给出 URL, 那么装入器将设置 URL 为“ data. xml ”。 它会总是添加 `.xml` , 但它会使用对象而不是方法参数来覆盖它。 如果您不希望此动作, 则提供 URL 。

注意: 只有在 XML 文件类型已建入 Phaser 时, 才能装入这类文件。 默认构建中已有, 但可排除自定义构建中的内容 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string \| [Phaser.Types.Loader.FileTypes.XMLFileConfig](/api/typedef/types-loader-filetypes#xmlfileconfig) | Array.\<[Phaser.Types.Loader.FileTypes.XMLFileConfig](/api/typedef/types-loader-filetypes#xmlfileconfig)> | 否 | 此文件使用的密钥, 或文件配置对象, 或其中的数组 。 |
| url | string | 是 | 装入此文件的绝对或相对 URL。 如果未定义或 `null` , 则会设置为 `<key>.xml`, 即如果 `key` 是"外国人", 那么 URL 将是"外国人. xml" 。 |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) | 是 | XHR 设置配置对象。 用于替换装入器默认 XHR 设置 。 |


**返回值:** [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) - 装弹机的例子。


**Fires:** [Phaser.Loader.Events#event:ADD](/api/event/loader-events#add)


> 源码：[src/loader/filetypes/XMLFile.js#L96](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/filetypes/XMLFile.js#L96)  
引入版本：3.0.0


---

## 公开成员 {#public-members}

### baseURL {#baseURL}

#### baseURL: string {#baseurl-string}


**说明:**

如果您想要在此设置任何资产路径之前附加一个 URL 。

如果允许在游戏代码外配置资产库 URL, 则有用 。

如果您直接设置此属性, 请用“ /” 结尾 。 或者, 拨打 `setBaseURL()` 并为你做 。


> 源码：[src/loader/LoaderPlugin.js#L153](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L153)  
引入版本：3.0.0


---

### cacheManager {#cacheManager}

#### cacheManager: [Phaser.Cache.CacheManager](/api/class/cache-cachemanager) {#cachemanager-phasercachecachemanager}


**说明:**

参考全球缓存管理器 。


> 源码：[src/loader/LoaderPlugin.js#L84](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L84)  
引入版本：3.7.0


---

### crossOrigin {#crossOrigin}

#### crossOrigin: string {#crossorigin-string}


**说明:**

crossOrigin 值适用于装入的图像。 通常需要设置为“ 无名” 。


> 源码：[src/loader/LoaderPlugin.js#L202](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L202)  
引入版本：3.0.0


---

### imageLoadType {#imageLoadType}

#### imageLoadType: string {#imageloadtype-string}


**说明:**

图像文件的可选负载类型。 `XHR` 是默认的。 设定为 `HTMLImageElement` , 使用图像标记加载图像 。


> 源码：[src/loader/LoaderPlugin.js#L211](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L211)  
引入版本：3.60.0


---

### inflight {#inflight}

#### inflight: Set.\<[Phaser.Loader.File](/api/class/loader-file)> {#inflight-setphaserloaderfile}


**说明:**

文件在装入过程中会存储在本集中.

成功后,它们被移到`queue` Set。

到装入过程结束时,此集将空出 。


> 源码：[src/loader/LoaderPlugin.js#L269](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L269)  
引入版本：3.0.0


---

### list {#list}

#### list: Set.\<[Phaser.Loader.File](/api/class/loader-file)> {#list-setphaserloaderfile}


**说明:**

文件通过`addFile`加入装入器时,会放在此集中.

开始装入时,它们被移到`inflight` Set,并假设成功装入,然后移到`queue` Set,以便进一步处理.

到装入过程结束时,此集将空出 。


> 源码：[src/loader/LoaderPlugin.js#L255](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L255)  
引入版本：3.0.0


---

### localSchemes {#localSchemes}

#### localSchemes: Array.\<string> {#localschemes-arraystring}


**说明:**

装入器认为属于“ 本地” 的所有方案组 。

这包含 `Phaser.Core.Config#loaderLocalScheme` 游戏配置设置和默认为 `[ 'file://', 'capacitor://' ]` 。 可以根据需要在此阵列中添加额外的本地方案 。


> 源码：[src/loader/LoaderPlugin.js#L220](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L220)  
引入版本：3.60.0


---

### maxParallelDownloads {#maxParallelDownloads}

#### maxParallelDownloads: number {#maxparalleldownloads-number}


**说明:**

尝试并同时获取的并行/平行资源数量 。

旧浏览器每个域限制6个请求;现代浏览器,尤其是那些拥有HTTP/2的浏览器完全不限制.

默认值为 32, 但您可以在您的 Game Config 中更改此选项, 或者在装入器启动前更改此属性 。


> 源码：[src/loader/LoaderPlugin.js#L173](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L173)  
引入版本：3.0.0


---

### maxRetries {#maxRetries}

#### maxRetries: number {#maxretries-number}


**说明:**

在文件失败前重试一个文件的次数 。

此属性由 `File` 对象在创建时读取, 并设定为同名的内部属性, 由装入器本身不使用 。

您可以通过 Game Config 设置此值, 或者您可以在装入器启动后的任何时间调整此属性。 但是, 它不会适用于已经添加到装入器的文件, 仅适用于该值被更改后添加的文件 。


> 源码：[src/loader/LoaderPlugin.js#L349](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L349)  
引入版本：3.85.0


---

### path {#path}

#### path: string {#path-string}


**说明:**

`path`的值如果设定,则放在给定的 _ relative_ 文件路径之前。例如:

```javascript
this.load.path = "images/sprites/";
this.load.image("ball", "ball.png");
this.load.image("tree", "level1/oaktree.png");
this.load.image("boom", "[http://server.com/explode.png](http://server.com/explode.png)");
```

将会从 `images/sprites/ball.png` 装入 `ball` 文件, 从树上装入 `images/sprites/level1/oaktree.png` 但文件 `boom` 将会从给定的 URL 装入,因为它是一个绝对的 URL 。

请注意,路径在文件名前添加,但 * 在 * 之后的 baseURL(如果设置了) 。

如果您直接设置此属性, 请用“ /” 结尾 。 或者, 拨打 `setPath()` 并为你做 。


> 源码：[src/loader/LoaderPlugin.js#L128](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L128)  
引入版本：3.0.0


---

### prefix {#prefix}

#### prefix: string {#prefix-string}


**说明:**

一个可选的前缀, 自动准备到每个文件密钥的开始。 如果前缀是 `MENU.`, 而您加载了密钥“ 背景” 的图像, 则生成的密钥是 `MENU.Background`。 您可以直接设置此选项, 或者调用 `Loader.setPrefix()`。 然后它会影响从此添加到加载器的每个文件 。 它会执行 _ 不_ 更改任何已经载入载重队列的文件 。


> 源码：[src/loader/LoaderPlugin.js#L115](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L115)  
引入版本：3.7.0


---

### progress {#progress}

#### progress: number {#progress-number}


**说明:**

当前负载队列的进展, 作为0到1之间的浮点值, 该文件完成加载后会自动更新。 请注意, 如果您在加载时将内容添加到当前负载队列中, 此值有可能再次下移 。


> 源码：[src/loader/LoaderPlugin.js#L243](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L243)  
引入版本：3.0.0


---

### queue {#queue}

#### queue: Set.\<[Phaser.Loader.File](/api/class/loader-file)> {#queue-setphaserloaderfile}


**说明:**

文件在处理过程中会存储在本集中.

如果程序成功,它们会被移到最终目的地,这可以是缓存或纹理管理器。

装入过程结束时, 此集将空 。


> 源码：[src/loader/LoaderPlugin.js#L282](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L282)  
引入版本：3.0.0


---

### scene {#scene}

#### scene: [Phaser.Scene](/api/class/scene) {#scene-phaserscene}


**说明:**

拥有这个装入器实例的场景 。


> 源码：[src/loader/LoaderPlugin.js#L66](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L66)  
引入版本：3.0.0


---

### sceneManager {#sceneManager}

#### sceneManager: [Phaser.Scenes.SceneManager](/api/class/scenes-scenemanager) {#scenemanager-phaserscenesscenemanager}


**说明:**

参考全球场景管理器.


**Access:** 保护


> 源码：[src/loader/LoaderPlugin.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L102)  
引入版本：3.16.0


---

### state {#state}

#### state: number {#state-number}


**说明:**

装弹机的当前状态 。


> 源码：[src/loader/LoaderPlugin.js#L329](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L329)  
引入版本：3.0.0


---

### systems {#systems}

#### systems: [Phaser.Scenes.Systems](/api/class/scenes-systems) {#systems-phaserscenessystems}


**说明:**

参考景区系统.


> 源码：[src/loader/LoaderPlugin.js#L75](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L75)  
引入版本：3.0.0


---

### textureManager {#textureManager}

#### textureManager: [Phaser.Textures.TextureManager](/api/class/textures-texturemanager) {#texturemanager-phasertexturestexturemanager}


**说明:**

参考全球纹理管理器.


> 源码：[src/loader/LoaderPlugin.js#L93](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L93)  
引入版本：3.7.0


---

### totalComplete {#totalComplete}

#### totalComplete: number {#totalcomplete-number}


**说明:**

在最近加载时成功加载的文件总数。 调用 `Loader.start` 时, 此值会被重置 。


> 源码：[src/loader/LoaderPlugin.js#L318](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L318)  
引入版本：3.7.0


---

### totalFailed {#totalFailed}

#### totalFailed: number {#totalfailed-number}


**说明:**

在最近的加载中未加载的文件总数。 调用 `Loader.start` 时会重置此值 。


> 源码：[src/loader/LoaderPlugin.js#L307](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L307)  
引入版本：3.7.0


---

### totalToLoad {#totalToLoad}

#### totalToLoad: number {#totaltoload-number}


**说明:**

要加载的文件总数。 不一定总是准确, 因为加载过程中您可能会加入加载器, 尤其是如果您加载一个 Pack 文件。 因此, 这个值会改变, 但在大多数情况下仍然是静止的 。


> 源码：[src/loader/LoaderPlugin.js#L232](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L232)  
引入版本：3.0.0


---

### xhr {#xhr}

#### xhr: [Phaser.Types.Loader.XHRSettingsObject](/api/typedef/types-loader#xhrsettingsobject) {#xhr-phasertypesloaderxhrsettingsobject}


**说明:**

与 XHR 相关的全球设置(每个文件可以覆盖)


> 源码：[src/loader/LoaderPlugin.js#L186](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/LoaderPlugin.js#L186)  
引入版本：3.0.0


---

---
