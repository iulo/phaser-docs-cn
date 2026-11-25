# DOM 元素 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/dom-element)

DOM Element Game Objects 是控制并操纵HTML Elements在游戏顶端的一种方法.

DOM 元素要显示, 您必须加入以下游戏配置对象, 才能显示 :

```js
dom {
  createContainer: true
}
```

也得有个 `parent` 容器,用于 Phaser中。此选项由 `parent` 属性在游戏配置中。当添加这两个东西时, Phaser 将自动创建一个位于游戏画布顶端的 DOM 容器 div 。此画布大小与画布相匹配,如果画布大小发生变化,则由于在缩放管理器内设置,则对画布容器进行相应的调整。不提供 `parent`,则将不创建 DOM 容器。

您可以通过`DOMStrings`来创建 DOM 元素, 或者通过一个引用当前元素的条目来创建, 您希望将其置于Phaser的控制之下。 例如 :

```js
this.add.dom(x, y, 'div', 'background-color: lime; width: 220px; height: 100px; font: 48px Arial', 'Phaser');
```

上述代码将在给定的x/y坐标处将一个 div 元素插入 DOM 容器。 DOMSTring 在 4 参数中设置了 div 的初始 CSS 样式, 最终参数是内文本。 在这种情况下, 它将创建一个 石灰色 div, 大小为 220px 乘 100px, 其文本为 Phaser, 字体为 Arial 字体 。

您几乎应该毫无例外地使用明确大小的 HTML 元素,以便完全控制元素在常规游戏内容旁边的对齐和定位.

与其直接指定 CSS 和 HTML , 您可以使用 `load.html` 文件加载器将其加载到缓存中, 然后使用 `createFromCache` 方法。 您也可以使用 `createFromHTML` 和该类中可用的其他各种方法来帮助构建您的要素 。

一旦元素被创建, 您就可以像其他游戏对象一样控制它。 您可以设定它的位置、 尺度、 旋转、 α 等属性。 它会随着主要场景相机的移动而移动, 并在画布的边缘被剪辑。 必须记住 DOM 元素的一些限制: 显而易见的是它们出现在您的游戏画布上或下方。 您不能把它们混入显示列表, 也就是说您不能有一个 DOM 元素, 然后是 Sprite, 然后是另一个 DOM 元素。

无法启用它们来输入。 要做到这一点, 您必须使用 `addListener` 方法直接添加本地事件听器。 最后的限制是使用相机。 DOM 容器大小可以完全匹配游戏布, 并相应剪辑。 DOM Elements 尊重相机滚动和 scrollFactor 设置, 但是如果您改变相机的大小, 从而与画布的大小不再匹配, 就不会相应剪辑 。

DOM 游戏对象可以添加到 Phaser 容器中, 但是您只应该将其嵌入** 深一层**。 任何更深的链条都会忽略所有根容器属性 。

此外,所有DOM元素都插入到同一个DOM容器中,不管它们是在哪个场景中创建的.

注意您只应该在带有 _ single_ 相机的场景中设置 DOM Elements。 如果您需要多个相机, 请使用平行的场景来达到此目的 。

DOM Elements 是将本地 HTML 与您的 Phaser 游戏对象对齐的有力方法。 例如, 您可以在您的标题屏幕中直接插入多人游戏的登录表。 或者是高分表的文本输入框。 或者是来自 3rd 派对服务的横幅广告。 或者您想用它们来高分辨率文本显示和UI 。 选择权在你, 请记住您正在处理标的 HTML 和 CSS 浮在游戏顶部, 并应该相应处理它 。

## 配置 {#configuration}

- 将 `parent` 设定为 divId
- 将`dom.createContainer`设定为`true`.

```javascript
var config = {
    // ...
    parent: divId,
    // fullscreenTarget: divId, // For fullscreen
    dom: {
        createContainer: true
    },
    input: {
        mouse: {
            target: divId
        },
        touch: {
            target: divId
        },
    },
    // ...
}
var game = new Phaser.Game(config);
```

## 添加 DOM 元素对象 {#add-dom-element-object}

### 添加 html 字符串 {#add-html-string}

1. 在预装阶段装入 html 字符串

    ```javascript
    this.load.html(key, url);
    ```

    参考文献: [load html](/guide/concepts/loader#html)
1. 从缓存中添加带有 html 字符串的 DOM 元素对象

    ```javascript
    var domElement = this.add.dom(x, y).createFromCache(key);  // elementType = 'div'
    // var domElement = this.add.dom(x, y).createFromCache(key, elementType);
    ```

   - 添加 html 字符串的 DOM 元素对象

    ```javascript
    var domElement = this.add.dom(x, y).createFromHTML(htmlString);  // elementType = 'div'
    // var domElement = this.add.dom(x, y).createFromHTML(htmlString, elementType);
    ```

    - `elementType`: 插入所有 html 的元素的标记名称。 默认为普通的 div 标记 。

### 创建元素 {#create-element}

```javascript
this.add.dom(x, y).createElement(tagName);
// this.add.dom(x, y).createElement(tagName, style, innerText);
```

- `tagName` : 指定要创建的元素类型的一种字符串。 例如, `'div'`
- `style` : 要么是持有 CSS 样式用于创建元素的 DOMSTring , 要么是样式将来自的对象。 可选 。
- `innerText`: 一种DOMSTring,它持有将设定为创建元素的innerText的文本。可选。

### 添加已有的 DOM {#add-existing-dom}

1. 创建 DOM 元素

    ```javascript
    var el = document.createElement('div');
    // el.style = '...';
    // el.innerText = '...';
    ```

1. 添加到场景

   ```javascript
   var domElement = this.add.dom(x, y, el);
   // var domElement = this.add.dom(x, y, el, style, innerText);
   ```

## 自定义类 {#custom-class}

```javascript
class MyDOMElement extends Phaser.GameObjects.DOMElement {
    constructor(scene, x, y, element, style, innerText) {
        super(scene, x, y, element, style, innerText);
        // ...
        this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {
    //     super.preUpdate(time, delta);
    // }
}
```

- `this.add.existing(gameObject)`: 将已有的游戏对象添加到此场景中.
  - 如果游戏对象使它成为了,它会被添加到显示列表中.
  - 如果它有`preUpdate`方法,它将被添加到更新列表中.

示例

```javascript
var domElement = new MyDOMElement(scene, x, y, element);
```

## DOM 元素发生 {#event-of-dom-element}

- 添加听觉

    ```javascript
    domElement.addListener(eventName);
    ```

  - `eventName`:事件名称
    - 单弦,前`'click'`
    - 事件名称与 `' '` 合并
- 添加事件处理器

    ```javascript
    var callback = function(event) {
        // event.target.name
    };
    domElement.on(eventName, callback, scope);
    // domElement.once(eventName, callback, scope);
    ```

    参考文献: [event emitter](/guide/concepts/events#the-event-emitter)
- 删除收听器

    ```javascript
    domElement.removeListener(eventName);
    ```

  - `eventName`:事件名称
    - 单弦,前`'click'`
    - 事件名称与 `' '` 合并

## 带孩子 {#get-child}

- 取个名字的孩子

    ```javascript
    var child = domElement.getChildByName(name)
    ```

- 以身份证明孩子

    ```javascript
    var child = domElement.getChildByID(id)
    ```

- 以财产方式带孩子

    ```javascript
    var child = domElement.getChildByProperty(property, value)
    ```

## 设置内置 html 字符串 {#set-inner-html-string}

```javascript
this.setHTML(html);
```

or

```javascript
this.setText(html);
```

## DOM 元素 {#dom-element}

每个DOM元素对象都有一个DOM元素.

- Set

   ```javascript
   domElement.setElement(el);
   // domElement.setElement(el, style, innerText);
   ```

- Get

   ```javascript
   var el = domElement.node;
   ```

## 深度 {#depth}

```javascript
domElement.setDepth(value);
```

## 设定大小 {#set-size}

```javascript
var style = domElement.node.style;
style.width = width + 'px';
style.height = height + 'px';
domElement.updateSize();
```

## 扭曲 {#skew}

```javascript
domElement.setSkew(x, y);
```

or

```javascript
domElement.skewX = x;
domElement.skewY = y;
```

## 旋转 3d {#rotate-3d}

旋转3d() CSS 函数定义了在3D空间中围绕固定轴旋转一个元素的转换,而不使其变形.

```javascript
domElement.rotate3d.set(x, y, z, a);
```

or

```javascript
domElement.rotate3d.x = x;
domElement.rotate3d.y = y;
domElement.rotate3d.z = z;
domElement.rotate3d.w = a;
```

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d)

## 与其他游戏对象的互动 {#interactive-with-other-game-objects}

1. DOM游戏对象总是放在游戏布上方,即DOM游戏对象会制作出高于任何其他种类的游戏对象.
1. DOM游戏对象即使不是第一个触摸的游戏对象,也会收到触摸事件.
1. P3的`'pointerdown'`,`'pointerup'`事件将在DOM游戏对象上方/下发射.
1. P3的`'pointermove'`事件不会在DOM游戏对象上方/下发射,除了.
    - 设置 DOM 游戏对象为 invisilbe 。
    - 指定输入( mouse) , 游戏配置的目标参数 。
1. DOM游戏对象只能通过主相机显示,即Dom游戏对象不能添加到其他相机中.

## 其他属性 {#other-properties}

见[game object](/guide/concepts/gameobjects)

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
