# ImageCollection {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/class/tilemaps-imagecollection)

图像集是一个特殊的图案集,每个条目都是完整的单个图像,而不是从更大的图案表中切成的瓦片。与标准图案集不同的是,收藏中的每个图像都是自己独立的资产,以独特的全球ID(GID)为参考。

图像收藏通常在加载平面图数据时自动创建。 当平面图使用“ 图像的集合” 的瓦片集类型而不是标准单像片集类型时, 您将会遇到它们 。

**构造函数**

`new ImageCollection(name, firstgid, [width], [height], [margin], [spacing], [properties])`

**参数**
| 名称 | 类型 | 可选 | default | 说明 |
| ---- | ---- | -------- | ------- | ----------- |
| 名称 | string | 否 |  | 地图数据中图像收集的名称. |
| firstgid | number | 否 |  | 此图像收藏包含的第一个图像索引 。 |
| width | number | 是 | 32 | 宽度最宽的图像( 像素) 。 |
| height | number | 是 | 32 | 高高的图像高度( 像素) 。 |
| margin | number | 是 | 0 | 集合中所有图像的边距( 像素) 。 |
| spacing | number | 是 | 0 | 收藏中每个图像之间的间隔(以像素计). |
| properties | object | 是 | "{}" | 自定义图像收藏属性 。 |

---


**作用域**: static

> 源码：[src/tilemaps/ImageCollection.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L9)  
引入版本：3.0.0

## 公开成员 {#public-members}

### firstgid {#firstgid}

#### firstgid: number {#firstgid-number}


**说明:**

斜线首加值。 这是图像收藏中的第一个图像索引的起始索引 。


> 源码：[src/tilemaps/ImageCollection.js#L52](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L52)  
引入版本：3.0.0


---

### imageHeight {#imageHeight}

#### imageHeight: number {#imageheight-number}


**说明:**

最高的图像的高度(以像素表示).


> 源码：[src/tilemaps/ImageCollection.js#L72](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L72)  
引入版本：3.0.0


---

### imageMargin {#imageMargin}

#### imageMargin: number {#imagemargin-number}


**说明:**

收藏中的图像周围的边距( 像素) 。


> 源码：[src/tilemaps/ImageCollection.js#L82](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L82)  
引入版本：3.0.0


---

### images {#images}

#### images: array {#images-array}


**说明:**

属于此收藏的缓存图像 。


> 源码：[src/tilemaps/ImageCollection.js#L111](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L111)  
引入版本：3.0.0


---

### imageSpacing {#imageSpacing}

#### imageSpacing: number {#imagespacing-number}


**说明:**

收藏中每个图像之间的间隔(以像素计).


> 源码：[src/tilemaps/ImageCollection.js#L92](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L92)  
引入版本：3.0.0


---

### imageWidth {#imageWidth}

#### imageWidth: number {#imagewidth-number}


**说明:**

宽度最宽的图像( 像素) 。


> 源码：[src/tilemaps/ImageCollection.js#L62](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L62)  
引入版本：3.0.0


---

### name {#name}

#### name: string {#name-string}


**说明:**

影像集名.


> 源码：[src/tilemaps/ImageCollection.js#L43](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L43)  
引入版本：3.0.0


---

### properties {#properties}

#### properties: object {#properties-object}


**说明:**

图像收藏的特性,一般在平面编辑器中定义.


> 源码：[src/tilemaps/ImageCollection.js#L102](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L102)  
引入版本：3.0.0


---

### total {#total}

#### total: number {#total-number}


**说明:**

图像收藏中的图像总数.


> 源码：[src/tilemaps/ImageCollection.js#L121](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L121)  
引入版本：3.0.0


---

## 公开方法 {#public-methods}

### addImage {#addImage}

#### \<instance> addImage(gid, image, width, height) {#instance-addimagegid-image-width-height}


**说明:**

向此图像收藏添加图像 。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| gid | number | 否 | 图像收藏中图像的基调 。 |
| image | string | 否 | 图像收藏和缓存中图像的密钥 。 |
| width | number | 否 | 图像收藏中的图像宽度 。 |
| height | number | 否 | 图像收藏中图像的高度. |


**返回值:** [Phaser.Tilemaps.ImageCollection](/api/class/tilemaps-imagecollection) - 此图像收集对象 。


> 源码：[src/tilemaps/ImageCollection.js#L147](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L147)  
引入版本：3.0.0


---

### containsImageIndex {#containsImageIndex}

#### \<instance> containsImageIndex(imageIndex) {#instance-containsimageindeximageindex}


**说明:**

如果且只有在图像收藏中包含给定的图像索引时,才能返回真实性。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| imageIndex | number | 否 | 要搜索的图像索引 。 |


**返回值:** boolean - 如果此图像收藏包含给定索引, 则为真 。


> 源码：[src/tilemaps/ImageCollection.js#L132](https://github.com/phaserjs/phaser/blob/v4.1.0/src/tilemaps/ImageCollection.js#L132)  
引入版本：3.0.0


---

---
