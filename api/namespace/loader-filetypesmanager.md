# Phaser.Loader.FileTypesManager {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/loader-filetypesmanager)

Scope: 
static
> 源码：[src/loader/FileTypesManager.js#L9](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/FileTypesManager.js#L9)  


## 静态函数 {#static-functions}

### destroy {#destroy}

#### \<static> destroy() {#static-destroy}


**说明:**

删除所有相关文件类型。


> 源码：[src/loader/FileTypesManager.js#L57](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/FileTypesManager.js#L57)  
引入版本：3.0.0


---

### install {#install}

#### \<static> install(loader) {#static-installloader}


**说明:**

当Lader Plugin创建时, 使用静态方法调用 。

循环通过本地类型对象,并将所有对象作为属性注入LaderPlugin实例。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| loader | [Phaser.Loader.LoaderPlugin](/api/class/loader-loaderplugin) | 否 | 资源加载器 Plugin 以安装类型 。 |


> 源码：[src/loader/FileTypesManager.js#L22](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/FileTypesManager.js#L22)  
引入版本：3.0.0


---

### register {#register}

#### \<static> register(key, factoryFunction) {#static-registerkey-factoryfunction}


**说明:**

由文件类型直接调用的稳定方法.

键是用来通过资源加载器加载文件的函数的参考,即`image`.

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| key | string | 否 | 将用作加载器Plugin中方法名的键 。 |
| factoryFunction | function | 否 | 当LaugerPlugin.key被引用时,将调用函数 。 |


> 源码：[src/loader/FileTypesManager.js#L41](https://github.com/phaserjs/phaser/blob/v4.1.0/src/loader/FileTypesManager.js#L41)  
引入版本：3.0.0


---

---
