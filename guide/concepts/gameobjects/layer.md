# 层 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/layer)

层是游戏对象的特殊类型, 其作用是显示列表。 您可以像对场景一样, 将任意类型的游戏对象添加到层中。 层可以用来将游戏对象的“ 层” 组合在一起 :

```js
const spaceman = this.add.sprite(150, 300, 'spaceman');
const bunny = this.add.sprite(400, 300, 'bunny');
const elephant = this.add.sprite(650, 300, 'elephant');

const layer = this.add.layer();

layer.add([ spaceman, bunny, elephant ]);
```

上面的例子中的3个图案现在将由它们被添加的图层管理。 因此, 如果您设置 `layer.setVisible(false)` , 它们都会从显示中消失 。

您也可以控制图层内游戏对象的深度。 例如, 使用一个图层的孩子的 `setDepth` 方法, 您可以调整该孩子在图层内, 而不是整个场景的深度。 图层也可以设定其深度 。

层类还提供了许多不同的操纵列表的方法,例如方法 `moveUp`, `moveDown`, `sendToBack`, `bringToTop` 。这些可以让您更改图层子的显示列表位置, 从而调整其显示顺序。 使用 `setDepth` 在一个孩子上,你可以 推翻这个。

层可以设置Post FX管道,这样可以方便地使一个覆盖整个一系列儿童的Post管道能够运行,而根据效果,这种管道通常可以更有效率地按每个孩子的频率运行.

层在空间中没有位置或大小。 这意味着您无法允许层用于物理或输入, 或改变层的位置、 旋转或尺度。 它们也没有滚动因子、 纹理、 锡、 来源、 裁剪或边框 。

如果需要这些特性,您应该使用一个容器。容器可以添加到层中,但是不能添加到层中。

然而, 您可以设置一个层的 Alpha, 混合模式, 深度, 遮罩和可见状态。 这些设置会影响所有由层制成的孩子 。

## 添加图层 {#add-layer}

  ```javascript
  var layer = this.add.layer();
  // var layer = this.add.layer(children);
  ```

- `children`: 游戏对象的阵列添加到此层.

## 自定义类 {#custom-class}

```javascript
class MyLayer extends Phaser.GameObjects.Layer {
    constructor(scene, children) {
        super(scene, children);
        // ...
        this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
}
```

- `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
  - 如果游戏对象使它成为了,它会被添加到显示列表中.
  - 如果它有`preUpdate`方法,它将被添加到更新列表中.

示例

```javascript
var layer = new MyLayer(scene, children);
```

## 添加子项目 {#add-child}

- 添加子项目

  ```javascript
  layer.add(gameObject);
  // layer.add(gameObjects);
  ```

  - `gameObject`:一个游戏对象,或一系列游戏对象.
- 添加孩子的时间

  ```javascript
  layer.addAt(gameObject, index);
  ```

- 替换子

  ```javascript
  layer.replace(oldGameObject, newGameObject);
  ```

## 删除子 {#remove-child}

- 删除子

  ```javascript
  var removed = layer.remove(gameObject);
  ```

- 删除子 :

  ```javascript
  var removed = layer.removeAt(index);
  ```

- 删除索引之间的子

  ```javascript
  var removed = layer.removeBetween(startIndex, endIndex);
  ```

- 删除所有的孩子

  ```javascript
  layer.removeAll();
  ```

删除的游戏对象不会添加到显示场景列表中, 使用

```javascript
gameObject.addToDisplayList();
```

将其添加到场景显示列表中。

## 带孩子 {#get-child}

- 带孩子去

  ```javascript
  var gameObject = layer.getAt(index);
  ```

- 取第一个孩子的名字

  ```javascript
  var gameObject = layer.getByName(name);
  ```

- 以财产方式获得第一个孩子

  ```javascript
  var gameObject = layer.getFirst(property, value);
  // var gameObject = layer.getFirst(property, value, startIndex, endIndex);
  ```

- 随机取孩子

  ```javascript
  var gameObject = layer.getRandom();
  // var gameObject = layer.getRandom(startIndex, length);
  ```

- 带孩子去

  ```javascript
  var gameObjects = layer.getAll();
  ```

- 获取孩子索引

  ```javascript
  var index = layer.getIndex(gameObject);
  ```

- 计数孩子

  ```javascript
  var count = layer.count(property, value);
  ```

- 计提全部孩子

  ```javascript
  var count = layer.length;
  ```

- 生过孩子

  ```javascript
  var hasChild = layer.exists(gameObject);
  ```

### 斜体 {#iterate}

- 获取第一个孩子( 设置重排索引为 0)

  ```javascript
  var gameObject = layer.first;
  ```

- 获取最后一个孩子( 设置重排索引为最后一个)

  ```javascript
  var gameObject = layer.last;
  ```

- 获取下一个孩子( 增加转发器索引, 直至最后)

  ```javascript
  var gameObject = layer.next;
  ```

- 获取上一个孩子( 减少延展指数, 直到 0)

  ```javascript
  var gameObject = layer.previous;
  ```

## 移动子 {#move-child}

- Swap

  ```javascript
  layer.swap(gameObject1, gameObject2);
  ```

- 移动到

  ```javascript
  layer.moveTo(gameObject, index);
  ```

- 带到顶端

  ```javascript
  layer.bringToTop(gameObject);
  ```

- 发送到后面

  ```javascript
  layer.sendToBack(gameObject);
  ```

- 上移( E)

  ```javascript
  layer.moveUp(gameObject);
  ```

- 向下移动

  ```javascript
  layer.moveDown(gameObject);
  ```

- 将孩子1 移动到孩子2 上方
  
  ```javascript
  layer.moveAbove(child1, child2);
  ```

- 将孩子1 移动到孩子2 下方

  ```javascript
  layer.moveBelow(child1, child2);
  ```

- Sort

  ```javascript
  layer.sort(property);
  ```

  or

  ```javascript
  layer.sort('', function(gameObject1, gameObject2) { 
      return 1; // 0, or -1
  });
  ```

- Reverse

  ```javascript
  layer.reverse();
  ```

- Shuffle

  ```javascript
  layer.shuffle();
  ```

注意,按深度排序
    儿童游戏对象也按深度排序.

## 每名儿童 {#for-each-child}

```javascript
layer.each(function(gameObject) {

}, scope);
```

## 设置属性 {#set-property}

```javascript
layer.setAll(property, value);
// layer.setAll(property, value, startIndex, endIndex);
```

## 事件 {#events}

- 添加游戏对象时

  ```javascript
  layer.events.on('addedtoscene', function(gameObject, scene) {

  })
  ```

- 删除游戏对象时

  ```javascript
  layer.events.on('removedfromscene', function(gameObject, scene) {

  })
  ```

`layer.events`参考`this.events`.

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = layer.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 阴影效果 {#shader-effects}

支持 [postFX effects](/guide/concepts/gameobjects/shader) 软件

!!! note
    无 preFX 效果支持

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
