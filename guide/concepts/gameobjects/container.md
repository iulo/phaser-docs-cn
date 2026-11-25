# 容器 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/container)

容器（Container）可以包含其他游戏对象。对象加入容器后，由容器负责渲染。默认情况下，对象会从场景的显示列表移到容器的内部列表，坐标也会变为相对于容器的局部坐标。

容器的变换原点固定为局部坐标 `[0, 0]`。添加子对象时，可以此原点为中心，为子对象设置正坐标或负坐标。

渲染容器时，会按内部列表的顺序渲染子对象。可以用 `moveUp`、`moveDown` 和 `sendToBack` 等方法调整顺序。修改容器的 `x`、`rotation` 等变换属性时，子对象也会受到影响。容器还可以嵌套。

容器可以设置遮罩，也可以作为遮罩使用。容器的子对象不应用单独的遮罩。只有位于显示列表根层的容器才会应用自己的遮罩，嵌套遮罩不会叠加。

容器可以接收输入。容器本身没有纹理，启用交互时需显式提供一个形状作为命中区域。子对象也可以独立启用输入。给子对象启用交互时，同时调整原点和使用负缩放可能造成命中区域错位。

可在使用 Arcade、Impact 或 Matter 物理时为容器添加物理体。物理引擎计算子对象的物理体时不会计入父容器的变换。如果父容器或更上层容器的位置偏离 `[0, 0]`，子对象的物理体可能出现偏移。

每层容器都会增加子对象的处理开销，输入事件尤其如此。子对象的渲染深度也受容器内部排序限制。需要统一变换多个对象时，使用容器更方便。

## 添加容器 {#add-container}

```javascript
var container = this.add.container(x, y);
// var container = this.add.container(x, y, children); // children: an array of game object
```

## 自定义类 {#custom-class}

- 定义类

    ```javascript
    class MyContainer extends Phaser.GameObjects.Container {
        constructor(scene, x, y, children) {
            super(scene, x, y, children);
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

- 创建实例

    ```javascript
    var container = new MyContainer(scene, x, y, children);
    ```

## 销毁容器 {#destroy-container}

```javascript
container.destroy();
```

也摧毁所有子游戏对象。

## 设置属性 {#set-properties}

参考 [game object](/guide/concepts/gameobjects),用于设置位置,角度,可见,α等...

## 设定大小 {#set-size}

```javascript
container.setSize(width, height);
```

默认`width`和`height`为0.

## 设置滚动因子 {#set-scroll-factor}

```javascript
container.setScrollFactor(x, y);
```

对所有容器儿童适用这个scrollFactor。

```javascript
container.setScrollFactor(x, y, true);
```

## 命中区域 {#hit-area}

```javascript
container.setInteractive(new Phaser.Geom.Circle(0, 0, radius), Phaser.Geom.Circle.Contains);
// container.setInteractive(false); // disable
```

指定带有圆形的命中区域.

## 非独占模式 {#non-exclusive}

```javascript
container.setExclusive(false);
```

允许多次添加到容器中的游戏对象.

## 子对象 {#children}

### 添加子对象 {#add-child}

```javascript
container.add(child);  // child: a game object or an array of game objects
```

```javascript
container.addAt(child, index);
```

### 检查容器中是否有该子对象 {#child-exists-in-container}

```javascript
var hasChild = container.exists(child);
```

### 获取子对象 {#get-child}

```javascript
var firstChild = container.first;
var nextChild = container.next;
var prevChild = container.previous;
var lastChild = container.last;
```

```javascript
var child = container.getByName(name);
```

```javascript
var child = container.getRandom(startIndex, length);
```

```javascript
var child = container.getFirst(property, value, startIndex, endIndex);
// value: the value to test the property against. Must pass a strict (`===`) comparison check.
```

```javascript
var children = container.getAll(property, value, startIndex, endIndex);
// value: the value to test the property against. Must pass a strict (`===`) comparison check.
```

```javascript
var amount = container.count(property, value, startIndex, endIndex);
// value: the value to test the property against. Must pass a strict (`===`) comparison check.
```

### 子对象排序 {#sort-children}

排序此容器的内容, 使项目根据给定属性排列。 例如: `sort('alpha')` 会根据它们的α属性值排序元素 。

```javascript
container.sort(property);
```

```javascript
container.sort(property, function(childA, childB){
    return 0; // 0, 1, -1
});
```

### 移除子对象 {#remove-child}

```javascript
container.remove(child);
// container.remove(child, true);  // remove child object and destroy it
```

```javascript
container.removeAt(index);
// container.removeAt(index, true);  // remove child object and destroy it
```

```javascript
container.removeBetween(startIndex, endIndex);
// container.removeBetween(startIndex, endIndex, true);  // remove children objects and destroy them
```

```javascript
container.removeAll();
// container.removeAll(true);  // remove all children objects and destroy them
```

将孩子从容器中移除而不销毁,会重新放回现场的显示列表中.

### 子对象的排列顺序 {#order-of-child}

```javascript
container.moveTo(child, index);
```

```javascript
container.bringToTop(child);
```

```javascript
container.sendToBack(child);
```

```javascript
container.moveUp(child);
```

```javascript
container.moveDown(child);
```

```javascript
container.moveAbove(child1, child2);  // Move child1 above child2
```

```javascript
container.moveBelow(child1, child2);  // Move child1 below child2
```

```javascript
container.swap(child1, child2);
```

```javascript
container.reverse();
```

```javascript
container.shuffle();
```

### 替换子对象 {#replace-child}

```javascript
container.replace(oldChild, newChild);
// container.replace(oldChild, newChild, true);  // destroy oldChild
```

### 设置属性 {#set-properties-1}

```javascript
container.setAll(property, value, startIndex, endIndex);
```

### 遍历子对象 {#for-each-child}

- 现有子对象列表

    ```javascript
    container.iterate(callback);
    // container.iterate(callback, context);
    // container.iterate(callback, context, arg0, arg1, ...);
    ```

  - `callback` :

        ```javascript
        function(child, arg0, arg1, ...) {

        }
        ```

- 分发一份现有子对象列表

    ```javascript
    container.each(callback);
    // container.each(callback, context);
    // container.each(callback, context, arg0, arg1, ...);
    ```

  - `callback` :

        ```javascript
        function(child, arg0, arg1, ...) {

        }
        ```

### 获取世界坐标中的位置、旋转与缩放 {#get-world-position-rotation-scale}

```javascript
var matrix = child.getWorldTransformMatrix();
var x = matrix.tx;
var y = matrix.ty;
var rotation = matrix.rotation;
var scaleX = matrix.scaleX;
var scaleY = matrix.scaleY;
```

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 创建遮罩 {#create-mask}

```javascript
var mask = container.createBitmapMask();
```

见[mask](/guide/concepts/display#masks)

## 着色器效果 {#shader-effects}

支持 [postFX effects](/guide/concepts/gameobjects/shader) 软件

!!! note
    无 preFX 效果支持

## 与 [group object](/guide/concepts/gameobjects/group) 比较 {#compare-with-group-object}

- 容器和团体物品都有子对象列表。
- 容器有位置,角度,α,可见,.etc,但组没有.
- 容器控制儿童属性(位置,角度,α,可见,.etc),但组不会.
- 游戏对象可以添加到许多组中,但只能添加到一个容器中(`exclusive`模式).

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
