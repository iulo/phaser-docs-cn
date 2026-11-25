# 缓存 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/loader/cache)

当一个文件被加载器下载时, 它几乎总是被存储在内部的 Phaser 缓存中。 对于不同的文件类型, 会有不同的缓存。 例如, JSON 文件被存储在 JSON 缓存中, 二进制缓存 等 。 这些缓存在 Phaser 游戏实例开始时会自动创建 。 文件被存储在其中, 使用独特的字符串键。 如果文件来自加载器, 它会使用您使用的同样键, 保存在缓存中 。

Phaser缓存不同于浏览器本身可能维护的任何缓存,因为它只持续到游戏持续期间。一旦您的游戏被直接破坏,或者通过页面导航,Phaser缓存就被清除。与浏览器缓存不同,您可以随意添加和删除任何 Phaser缓存中的项目 。

存储在 Phaser 缓存中的项目是全局的, 这意味着它们可以从游戏中任意一个景点访问。 景点并不保存自己的缓存集, 而是它们都共享相同的全局集。 这很重要, 因为这意味着如果您在一个景点中加载一个文件, 其它景点中也会有它 。

大部分情况下,你不需要担心与Phaser缓存的交互。它主要是内置系统,用于存储和检索数据,例如加载器。然而,有时你可能想要直接与它交互,它有一个公开的API来完成这个任务。

## 使用量 {#usage}

- 获取缓存数据

  ```js
  var cache = scene.cache.text;
  var data = cache.get(key);
  ```

- 添加缓存数据

  ```js
  var cache = scene.cache.text;
  var data = cache.add(key);
  ```

- 删除缓存数据

  ```js
  var cache = scene.cache.text;
  cache.remove(key);
  ```

- 正在验证缓存数据

  ```js
  var cache = scene.cache.text;
  var hasData = cache.exists(key);
  // var hasData = cache.has(key);
  ```

## 事件 {#events}

- 添加项目

  ```js
  cache.events.on("add", function (cache, key, item) {});
  ```

- 删除项目

  ```js
  cache.events.on("remove", function (cache, key, item) {});
  ```

---
