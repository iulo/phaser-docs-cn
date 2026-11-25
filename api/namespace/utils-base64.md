# Phaser.Utils.Base64 {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/utils-base64)

Scope: 
static
> 源码：[src/utils/base64/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/base64/index.js#L7)  


## 静态函数 {#static-functions}

### ArrayBufferToBase64 {#ArrayBufferToBase64}

#### \<static> ArrayBufferToBase64(arrayBuffer, [mediaType]) {#static-arraybuffertobase64arraybuffer-mediatype}


**说明:**

将矩阵缓冲转换为碱性64字符串。

如果提供`mediaType`参数,由此产生的字符串可以可选为数据uri.

详情请见[https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| arrayBuffer | ArrayBuffer | 否 | 编程缓冲器编码 。 |
| mediaType | string | 是 | 一个可选的介质类型,即`audio/ogg`或`image/jpeg`。如果包含由此产生的字符串,则将是一个数据 URI。 |


**返回值:** string - 基座64编码为Array Buffer.


> 源码：[src/utils/base64/ArrayBufferToBase64.js#L10](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/base64/ArrayBufferToBase64.js#L10)  
引入版本：3.18.0


---

### Base64ToArrayBuffer {#Base64ToArrayBuffer}

#### \<static> Base64ToArrayBuffer(base64) {#static-base64toarraybufferbase64}


**说明:**

将一个带或没有数据uri的基数64字符串转换成矩阵缓冲器。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| base64 | string | 否 | 要解码的基数64字符串。 可以选择包含一个数据 URI 头, 在解码前会剥离它 。 |


**返回值:** ArrayBuffer - 由基数64数据解码的 ArrayBuffer 。


> 源码：[src/utils/base64/Base64ToArrayBuffer.js#L18](https://github.com/phaserjs/phaser/blob/v4.1.0/src/utils/base64/Base64ToArrayBuffer.js#L18)  
引入版本：3.18.0


---

---
