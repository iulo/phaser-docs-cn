# Phaser.Textures.Parsers {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/textures-parsers)

Scope: 
static
> 源码：[src/textures/parsers/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/textures/parsers/index.js#L7)  


## 静态函数 {#static-functions}

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


---

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


---

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


---

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

---
