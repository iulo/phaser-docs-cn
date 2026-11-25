# Phaser.Textures.Parsers {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/function/textures)

### AtlasXML {#AtlasXML}

#### \<static> AtlasXML(texture, sourceIndex, xml) {#static-atlasxmltexture-sourceindex-xml}


**说明:**

分析一个 XML 纹理图集对象,并将所有框架添加到纹理中。


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 添加框架的纹理 。 |
| sourceIndex | number | 否 | 纹理源的索引. |
| xml | * | 否 | XML 数据 。 |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/AtlasXML.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/AtlasXML.js#L7)  
引入版本：3.7.0


### Canvas {#Canvas}

#### \<static> Canvas(texture, sourceIndex) {#static-canvastexture-sourceindex}


**说明:**

将 Canvas 元素添加到纹理中。


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 添加框架的纹理 。 |
| sourceIndex | number | 否 | 纹理源的索引. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/Canvas.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/Canvas.js#L7)  
引入版本：3.0.0


### Image {#Image}

#### \<static> Image(texture, sourceIndex) {#static-imagetexture-sourceindex}


**说明:**

将图像元素添加到纹理中。


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 添加框架的纹理 。 |
| sourceIndex | number | 否 | 纹理源的索引. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/Image.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/Image.js#L7)  
引入版本：3.0.0


### JSONArray {#JSONArray}

#### \<static> JSONArray(texture, sourceIndex, json) {#static-jsonarraytexture-sourceindex-json}


**说明:**

分析一个纹理图集 JSON 矩阵, 并将框架添加到纹理中. JSON 格式预计匹配纹理包包定义的, 框架属性包含一个框架阵列.


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 添加框架的纹理 。 |
| sourceIndex | number | 否 | 纹理源的索引. |
| json | object | 否 | JSON数据. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/JSONArray.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/JSONArray.js#L9)  
引入版本：3.0.0


### JSONHash {#JSONHash}

#### \<static> JSONHash(texture, sourceIndex, json) {#static-jsonhashtexture-sourceindex-json}


**说明:**

解析一个纹理 Atlas JSON Hash 并添加到纹理中. JSON格式预计匹配纹理包包定义的,与包含一个框架对象的框属性相匹配.


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 添加框架的纹理 。 |
| sourceIndex | number | 否 | 纹理源的索引. |
| json | object | 否 | JSON数据. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/JSONHash.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/JSONHash.js#L9)  
引入版本：3.0.0


### KTXParser {#KTXParser}

#### \<static> KTXParser(data) {#static-ktxparserdata}


**说明:**

解析一个 KTX (Khronos texture) 格式的压缩纹理文件,并提取上传到WebGL所需的纹理数据. KTX是GPU压缩纹理的容器格式,支持ETC,ASTC,S3TC,和PVRTC等格式.

解析器验证了12字节的KTX文件标识符,确认纹理使用压缩格式(未压缩的KTX文件不支持),然后读取图像维度,内部GL格式,以及所有从二进制数据中可用的MIPMAP级别.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | ArrayBuffer | 否 | KTX 文件的原始二进制矩阵缓冲器, 由压缩的纹理文件加载器装入 。 |


**返回值:** [Phaser.Types.Textures.CompressedTextureData](/api/typedef/types-textures#compressedtexturedata) - 一个包含 mipmap 级别,维度,以及内部 GL 格式的压缩TextureData 对象,准备上传WebGL .


> 源码：[src/textures/parsers/KTXParser.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/KTXParser.js#L7)  
引入版本：3.60.0


### PCT {#PCT}

#### \<static> PCT(texture, decoded) {#static-pcttexture-decoded}


**说明:**

分析一个 Phaser 压缩纹理图集(PCT)数据对象,并将框架添加到纹理中。

电话 `decoded` 参数是生成的对象 `Phaser.Textures.Parsers.PCTDecode` (或等效的,预解码结构). 它必须包含 `pages`, `folders`,和 `frames` 字段。框架将使用 `page` 与匹配索引相对应的每个边框上的索引 `TextureSource` 纹理上。

解码数据中的页面和文件夹元数据也在`pct`键下复制到Texture的`customData`,因此可以在运行时检查.

这个parser由`Phaser.Textures.TextureManager#addAtlasPCT`调用,一般不直接引用.


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 添加框架的纹理 。 |
| decoded | object | 否 | 解码的PCT数据,由`Phaser.Textures.Parsers.PCTDecode`生产. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/PCT.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/PCT.js#L7)  
引入版本：4.0.0


### PCTDecode {#PCTDecode}

#### \<static> PCTDecode(text) {#static-pctdecodetext}


**说明:**

解码一个 Phaser 压缩纹理图集文件(PCT),从原始文本表达式变为结构化对象.

这是 PCT 地图集加载器和 `PCT` 纹理解析器所使用的独立辅助器。 它将面向行的 PCT 文本格式转换成包含 `pages` 阵列( 每页一个条目) 、 `folders` 字典 和 `frames` 地图, 并带有完全解析的框架名称和位置。 Framme `page` 索引地图直接到 `pages` 阵列 。

该函数验证版本头并拒绝带有不支持的主版本或缺失的`PCT:`头的文件,在记录警告后返回这些情况下的`null`。未来小版本中引入的未知行前缀会按规格要求默不作声地跳过。

完整描述返回对象的格式和语义,请参见Phaser压缩纹理图集格式规格文档.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| text | string | 否 | `.pct`文件的原始文本内容 。 |


**返回值:** Object - 解码的PCT结构,或者如果输入无效,则使用`null`.


> 源码：[src/textures/parsers/PCTDecode.js#L129](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/PCTDecode.js#L129)  
引入版本：4.0.0


### PVRParser {#PVRParser}

#### \<static> PVRParser(data) {#static-pvrparserdata}


**说明:**

解析一个PVR格式的压缩纹理文件,并从中生成适合WebGL的纹理数据.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | ArrayBuffer | 否 | 由压缩纹理文件加载器提供的 PVR 文件的原始二进制矩阵缓冲器 。 |


**返回值:** [Phaser.Types.Textures.CompressedTextureData](/api/typedef/types-textures#compressedtexturedata) - 一个解析的压缩纹理数据对象,包含mipmap级别,基维度,WebGL内部格式,以及显示其压缩的旗帜,不需要mipmap生成.


> 源码：[src/textures/parsers/PVRParser.js#L236](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/PVRParser.js#L236)  
引入版本：3.60.0


### SpriteSheet {#SpriteSheet}

#### \<static> SpriteSheet(texture, sourceIndex, x, y, width, height, config, config.frameWidth, [config.frameHeight], [config.startFrame], [config.endFrame], [config.margin], [config.spacing]) {#static-spritesheettexture-sourceindex-x-y-width-height-config-configframewidth-configframeheight-configstartframe-configendframe-configmargin-configspacing}


**说明:**

分析一个 精灵表, 并将框架添加到纹理中 。

在Phaser术语中,Sprite Sheet是一个包含不同框架的纹理,但每个框架的大小完全相同,不能修剪或旋转.


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 |  | 添加框架的纹理 。 |
| sourceIndex | number | 否 |  | 纹理源的索引. |
| x | number | 否 |  | 斯普林特工作表的左上角坐标。默认为零。从地图集提取工作表时使用。 |
| y | number | 否 |  | 斯普林特工作表的左上角坐标。默认为零。从地图集提取工作表时使用。 |
| width | number | 否 |  | 源图像的宽度 。 |
| height | number | 否 |  | 源头图像的高度. |
| config | object | 否 |  | 描述如何解析精灵表的对象 。 |
| config.frameWidth | number | 否 |  | 以精灵表中单个框架的像素显示的宽度。 |
| config.frameHeight | number | 是 |  | 显示图纸中单个框架的像素高度。 如果未提供, 默认为 frameWidth 。 |
| config.startFrame | number | 是 | 0 | 开始提取的框架。默认为零。 |
| config.endFrame | number | 是 | -1 | 完成提取的帧。 默认为 - 1, 表示“ 所有帧 ” 。 |
| config.margin | number | 是 | 0 | 如果框架已绘制了边距, 请在此指定金额 。 |
| config.spacing | number | 是 | 0 | 如果画框之间有间隔,请在此指定金额。 |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/SpriteSheet.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/SpriteSheet.js#L9)  
引入版本：3.0.0


### SpriteSheetFromAtlas {#SpriteSheetFromAtlas}

#### \<static> SpriteSheetFromAtlas(texture, frame, config, config.frameWidth, [config.frameHeight], [config.startFrame], [config.endFrame], [config.margin], [config.spacing]) {#static-spritesheetfromatlastexture-frame-config-configframewidth-configframeheight-configstartframe-configendframe-configmargin-configspacing}


**说明:**

分析一个 精灵表,并将框架添加到文字中,其中 精灵表作为框架存储在 Atlas 中。

在Phaser术语中,Sprite Sheet是一个包含不同框架的纹理,但每个框架的大小完全相同,不能修剪或旋转.


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 默认值 | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 |  | 添加框架的纹理 。 |
| frame | [Phaser.Textures.Frame](/api/class/textures-frame) | 否 |  | 包含 精灵表的框架 。 |
| config | object | 否 |  | 描述如何解析精灵表的对象 。 |
| config.frameWidth | number | 否 |  | 以精灵表中单个框架的像素显示的宽度。 |
| config.frameHeight | number | 是 |  | 显示图纸中单个框架的像素高度。 如果未提供, 默认为 frameWidth 。 |
| config.startFrame | number | 是 | 0 | 锦标板中起始框架索引 |
| config.endFrame | number | 是 | -1 | 显示图纸中尾框的索引。 -1 表示所有框架的其余部分 |
| config.margin | number | 是 | 0 | 如果框架已绘制了边距, 请在此指定金额 。 |
| config.spacing | number | 是 | 0 | 如果画框之间有间隔,请在此指定金额。 |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/SpriteSheetFromAtlas.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/SpriteSheetFromAtlas.js#L9)  
引入版本：3.0.0


### UnityYAML {#UnityYAML}

#### \<static> UnityYAML(texture, sourceIndex, yaml) {#static-unityyamltexture-sourceindex-yaml}


**说明:**

解析一个 Unity YAML 文件,并在纹理中创建框架。关于Sprite Meta 数据的更多细节,请参见 [https://docs.unity3d.com/ScriptReference/SpriteMetaData.html](https://docs.unity3d.com/ScriptReference/SpriteMetaData.html)


**访问权限:** 私有

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| texture | [Phaser.Textures.Texture](/api/class/textures-texture) | 否 | 添加框架的纹理 。 |
| sourceIndex | number | 否 | 纹理源的索引. |
| yaml | object | 否 | YAML数据. |


**返回值:** [Phaser.Textures.Texture](/api/class/textures-texture) - 纹理由此解析器修改 。


> 源码：[src/textures/parsers/UnityYAML.js#L38](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/UnityYAML.js#L38)  
引入版本：3.0.0


### verifyCompressedTexture {#verifyCompressedTexture}

#### \<static> verifyCompressedTexture(data) {#static-verifycompressedtexturedata}


**说明:**

验证给定的压缩纹理数据是否有效 。

将每个 mip 层的尺寸与该特定格式的规则进行比较。

假设在解析时Mip层大小被计算正确 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| data | [Phaser.Types.Textures.CompressedTextureData](/api/typedef/types-textures#compressedtexturedata) | 否 | 压缩的纹理数据进行校验. |


**返回值:** boolean - 压缩的纹理数据是否有效 。


> 源码：[src/textures/parsers/VerifyCompressedTexture.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/VerifyCompressedTexture.js#L9)  
引入版本：3.80.0

---
