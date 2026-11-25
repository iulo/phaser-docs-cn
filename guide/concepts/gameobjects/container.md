# 容器 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/container)

容器,如其名称所暗示的,可以“包含”其他类型的游戏对象。当一个游戏对象被添加到容器中时,容器将承担渲染责任。默认它将从显示列表中删除,而是添加到容器内部列表中。

游戏对象的位置会自动与容器的位置相对.

容器的变换原点固定为局部坐标 `[0, 0]`。添加子对象时，以这个原点为容器的中心，按需要为子对象设置正坐标或负坐标。

集装箱建成后,其所有儿童也按照集装箱内存在的顺序被改造,集装箱儿童可以采用诸如MoveUp、MoveDown和SendToBack等方法重新定位。

如果修改集装箱的变换财产,如Contain.x或Contain.rotation,那么它也会自动影响所有儿童。

集装箱可以包括用于深层嵌入式变压器的其他集装箱.

集装箱上可以设置口罩,也可以用作口罩。 但是, 集装箱儿童不能被遮盖。 口罩不会“ 装入” 。 只有显示列表根部的集装箱才会使用其口罩 。

容器可以允许输入。由于它们没有纹理,所以需要提供形状,以便用作攻击区。集装箱儿童也可以允许输入,独立于集装箱。

如果输入可以使孩子成为可能,则不应同时设定儿童的起源和负比例因素,或输入区域会变得不匹配。

集装箱可以被赋予一个物理体,用于弧形物理、撞击物理或物质物理。但是,如果集装箱儿童能够用于物理,那么如果集装箱本身或其祖先在除0x0以外的任何地方被定位,则可能会得到意外的结果,例如抵消体。 由于需要过多的额外计算,集装箱儿童不会在集装箱中被考虑。 请安排游戏围绕此进行。

了解使用集装箱的影响很重要。它们会给每个孩子增加额外的处理费用。你越是窝住他们,成本就越高。对于输入事件,尤其如此。你也会松动将集装箱儿童的显示深度设置在与那些不在集装箱内的儿童相同的灵活方式上。简言之,不要为了它而使用集装箱。每次你创建一个容器,都要付出小的代价,尽量在可能时避免这样做。

## 添加容器( E) {#add-container}

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

也摧毁所有儿童游戏的物体。

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

对所有集装箱儿童适用这个scrollFactor。

```javascript
container.setScrollFactor(x, y, true);
```

## 命中区域 {#hit-area}

```javascript
container.setInteractive(new Phaser.Geom.Circle(0, 0, radius), Phaser.Geom.Circle.Contains);
// container.setInteractive(false); // disable
```

指定带有圆形的命中区域.

## 非排他性 {#non-exclusive}

```javascript
container.setExclusive(false);
```

允许多次添加到容器中的游戏对象.

## 儿童 {#children}

### 添加子项目 {#add-child}

```javascript
container.add(child);  // child: a game object or an array of game objects
```

```javascript
container.addAt(child, index);
```

### 容器中存在儿童 {#child-exists-in-container}

```javascript
var hasChild = container.exists(child);
```

### 带孩子 {#get-child}

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

### 排序孩子 {#sort-children}

排序此容器的内容, 使项目根据给定属性排列。 例如: `sort('alpha')` 会根据它们的α属性值排序元素 。

```javascript
container.sort(property);
```

```javascript
container.sort(property, function(childA, childB){
    return 0; // 0, 1, -1
});
```

### 删除子 {#remove-child}

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

### 子女顺序 {#order-of-child}

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

### 替换子 {#replace-child}

```javascript
container.replace(oldChild, newChild);
// container.replace(oldChild, newChild, true);  // destroy oldChild
```

### 设置属性 {#set-properties-1}

```javascript
container.setAll(property, value, startIndex, endIndex);
```

### 每名儿童 {#for-each-child}

- 现有儿童名单

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

- 分发一份现有儿童名单

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

### 获得世界位置、旋转、比例 {#get-world-position-rotation-scale}

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

## 阴影效果 {#shader-effects}

支持 [postFX effects](/guide/concepts/gameobjects/shader) 软件

!!! note
    无 preFX 效果支持

## 与 [group object](/guide/concepts/gameobjects/group) 比较 {#compare-with-group-object}

- 集装箱和团体物品都有儿童名单。
- 容器有位置,角度,α,可见,.etc,但组没有.
- 容器控制儿童属性(位置,角度,α,可见,.etc),但组不会.
- 游戏对象可以添加到许多组中,但只能添加到一个容器中(`exclusive`模式).

## 作者署名 {#author-credits}

本页包含以下作者贡献的内容。

- [RexRainbow](https://github.com/rexrainbow)

---
