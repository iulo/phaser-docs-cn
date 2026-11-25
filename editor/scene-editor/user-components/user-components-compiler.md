# 用户组件编译器 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/user-components/user-components-compiler)

用户组件被配置在 `*.components`文件, 并被 Scene Editor 使用。 它是 Phaser 编辑器的概念, 不是 Phaser。 所以我们使用相同的 Scene Editer 哲学, 它将我们的自定义配置编译成 pull, 可读, 完全 Phaser 兼容的代码 。

接下来,看看**Horizontal Move**组件是如何编译成JavaScript的。

构成部分信息:

![Component metadata.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-editor-info-20221101.webp)

组件的属性 :

![The properties](https://cdn.phaser.io/editor-docs/scene-editor-user-components-props-20221101.webp)

**水平速度**

![Horizaontal move property.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-prop-1-20221101.webp)

**民进 X**

![Min position X](https://cdn.phaser.io/editor-docs/scene-editor-user-components-prop-2-20221101.webp)

**最大值 X**

![Max position Y.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-prop-3-20221101.webp)

生成的代码 :

```javascript
// You can write more code here

/* START OF COMPILED CODE */

class HorizontalMove extends BaseComponent {

    constructor(gameObject) {
        gameObject["__HorizontalMove"] = this;

        /** @type {Phaser.GameObjects.Image} */
        this.gameObject = gameObject;
        /** @type {number} */
        this.horizVelocity = 0;
        /** @type {number} */
        this.minX = 0;
        /** @type {number} */
        this.maxX = 3070;

        /* START-USER-CTR-CODE */
        // Write your code here.
        /* END-USER-CTR-CODE */
    }

    /** @returns {HorizontalMove} */
    static getComponent(gameObject) {
        return gameObject["__HorizontalMove"];
    }

    /* START-USER-CODE */
    // Write your code here.
    /* END-USER-CODE */
}

/* END OF COMPILED CODE */
// You can write more code here
```

生成的类非常简单,接下来我们逐个解释:


## 超级阶级 {#the-super-class}

如果将一个值(在此情况下为 `BaseComponent`)设定为 ** 超级类** 参数。然后类代码会像这样生成 :

```javascript
class HorizontalMove extends BaseComponent {
    ...
}
```

一个超级类允许创建某些组件共同的行为,或者提供辅助方法。这是在[Starting and updating the User Components](/editor/scene-editor/user-components/user-components-start-update-methods)部分中解释的** UserComponent**类的情况。

## 构造器 {#the-constructor}

组件有一个构造器,所有属性都初始化,您也可以添加初始化代码 。

![The constructor code.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-ctr-code-07292020.webp)

构建器用于创建组件并添加到游戏对象中:

```javascript
const enemy = this.add.image(...);
const enemyMove = new HorizontalMove(enemyMove);
enemyMove.maxX = 400;
```


## 组件存取器方法 {#the-component-accessor-method}

`getComponent()`方法从游戏对象获得组件,如果存在的话:

```javascript
class HorizontalMove {

    ...

    /** @returns {HorizontalMove} */
    static getComponent(gameObject) {
        return gameObject["__HorizontalMove"];
    }
}

// in a random part of the game
const enemy = ...;
const horizMove = HorizontalMove.getComponent(enemy);
horizMove.minX = 10;
```


## 构成部分的用户成员 {#the-user-members-of-the-component}

加入组件类,请在`/* STAR-USER-CODE */`和`/* END-USER-CODE */`评论中写入.

可能,你希望写一个** start**和**update**的方法,就像[Starting and updating components](/editor/scene-editor/user-components/user-components-start-update-methods)部分解释的那样.


## 编译器设置 {#compiler-settings}

用户组件编译器支持两个 JavaScript和 TypeScript 两种输出语言。 当未选择组件时, 您可以在检查器视图中选择此语言。 另外, 您也可以选择插入缩进的空格、 标签大小或 ES 模块的自动导出/导入 :

![Selecting compiler settings.](https://cdn.phaser.io/editor-docs/scene-editor-user-components-compiler-settings.webp)

设置有默认值,但如果有其他场景文件或用户组件文件,默认值将从最新的修改文件(如果没有组件文件,则会取自).

当 ** 输出类(ES Module) ** 参数打开时,编译器包括 `export default` 类修改器.

当 ** Auto 导入(ES Module) ** 参数打开时, 编译器会添加“ 导入” 语句, 用于导入代码生成不同部分所使用的类型。 用户编写的代码不处理。 如果您使用其他类型, 您应该手动导入 。

---
