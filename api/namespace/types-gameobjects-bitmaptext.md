# Phaser.Types.GameObjects.BitmapText {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/types-gameobjects-bitmaptext)

Scope: 
static
> 源码：[src/gameobjects/bitmaptext/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/index.js#L7)  


## 静态函数 {#static-functions}

### BitmapFontCharacterData {#BitmapFontCharacterData}

#### BitmapFontCharacterData {#bitmapfontcharacterdata}


**说明:**

位图字体的单个字符的字体数据。

描述角色的位置,大小,偏移和克宁.

至3.50版本为止,它还包括WebGL纹理uv数据.


> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapFontCharacterData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapFontCharacterData.js#L1)  
引入版本：3.0.0


---

### BitmapFontData {#BitmapFontData}

#### BitmapFontData {#bitmapfontdata}


**说明:**

位图字体数据,可以被一个位图Text游戏对象使用.


> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapFontData.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapFontData.js#L1)  
引入版本：3.0.0


---

### BitmapTextCharacter {#BitmapTextCharacter}

#### BitmapTextCharacter {#bitmaptextcharacter}


**说明:**

`BitmapTextSize`字符阵列的单个条目.

位置和维度会考虑字体大小,但不会被翻译为游戏对象本身的局部空间.


> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextCharacter.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextCharacter.js#L1)  
引入版本：3.50.0


---

### BitmapTextConfig {#BitmapTextConfig}

#### BitmapTextConfig {#bitmaptextconfig}


> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextConfig.js#L1)  
引入版本：3.0.0


---

### BitmapTextLines {#BitmapTextLines}

#### BitmapTextLines {#bitmaptextlines}


**说明:**

详细介绍`BitmapTextSize`对象中的行数据.


> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextLines.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextLines.js#L1)  
引入版本：3.50.0


---

### BitmapTextSize {#BitmapTextSize}

#### BitmapTextSize {#bitmaptextsize}


> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextSize.js#L1)  
引入版本：3.0.0


---

### BitmapTextWord {#BitmapTextWord}

#### BitmapTextWord {#bitmaptextword}


**说明:**

有关`BitmapTextSize`对象字数组中单个世界条目的详情.


> 源码：[src/gameobjects/bitmaptext/typedefs/BitmapTextWord.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/BitmapTextWord.js#L1)  
引入版本：3.50.0


---

### DisplayCallback {#DisplayCallback}

#### DisplayCallback {#displaycallback}

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| display | [Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig](/api/typedef/types-gameobjects-bitmaptext#displaycallbackconfig) | 否 | 即将渲染的字符设置 。 |


**返回值:** [Phaser.Types.GameObjects.BitmapText.DisplayCallbackConfig](/api/typedef/types-gameobjects-bitmaptext#displaycallbackconfig) - 即将渲染的字符的改变位置、尺度和旋转值。


> 源码：[src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L17](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L17)  



---

### DisplayCallbackConfig {#DisplayCallbackConfig}

#### DisplayCallbackConfig {#displaycallbackconfig}


> 源码：[src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/DisplayCallbackConfig.js#L1)  
引入版本：3.0.0


---

### GlobalBitmapTextSize {#GlobalBitmapTextSize}

#### GlobalBitmapTextSize {#globalbitmaptextsize}


**说明:**

结合游戏对象的尺度和世界位置,将比图文本在全球空间中的位置和大小.


> 源码：[src/gameobjects/bitmaptext/typedefs/GlobalBitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/GlobalBitmapTextSize.js#L1)  
引入版本：3.0.0


---

### JSONBitmapText {#JSONBitmapText}

#### JSONBitmapText {#jsonbitmaptext}


> 源码：[src/gameobjects/bitmaptext/typedefs/JSONBitmapText.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/JSONBitmapText.js#L1)  
引入版本：3.0.0


---

### LocalBitmapTextSize {#LocalBitmapTextSize}

#### LocalBitmapTextSize {#localbitmaptextsize}


**说明:**

本地空间中位图文本的位置和大小, 仅考虑字体大小 。


> 源码：[src/gameobjects/bitmaptext/typedefs/LocalBitmapTextSize.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/LocalBitmapTextSize.js#L1)  
引入版本：3.0.0


---

### RetroFontConfig {#RetroFontConfig}

#### RetroFontConfig {#retrofontconfig}


> 源码：[src/gameobjects/bitmaptext/typedefs/RetroFontConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/RetroFontConfig.js#L1)  
引入版本：3.6.0


---

### TintConfig {#TintConfig}

#### TintConfig {#tintconfig}


> 源码：[src/gameobjects/bitmaptext/typedefs/TintConfig.js#L1](https://github.com/phaserjs/phaser/blob/v4.1.0/src/gameobjects/bitmaptext/typedefs/TintConfig.js#L1)  
引入版本：3.0.0


---

---
