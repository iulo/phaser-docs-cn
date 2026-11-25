# 为 Box2D 物理准备场景 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/box2d-physics/box2d-physics-prepare-scene)

Box2D不是原生的Phaser API,所以需要一些额外的步骤来准备项目和我们创建Box2D世界的场景.

## 准备项目 {#preparing-the-project}

要在 Phaser 工程中使用 Box2D, 您必须先在工程中添加 Box2D 库。 要做到这一点, 您必须获得 [the `PhaserBox2D.js` file from its repository](https://github.com/phaserjs/phaser-box2d/tree/main/dist), 然后复制到您的工程中 。

重要的是,您要保留`PhaserBox2D.js`文件的同名,因为Phaser编辑器会使用它来导入生成的所有代码中的库.

以Box2D和Phaser编辑器开始的一个简单方法是,使用**Box2D Starter**项目模板,或**Angry Balls**实例模板创建一个项目,可用Phaser编辑器的桌面版本.

![Box2D project templates](https://cdn.phaser.games/oss-docs/assets/729be528814554c2-box2d-project-templates-20250218.webp)

## 摆平场景 {#setting-up-the-scene}

要获得Box2D的物理体, 您必须首先创建一个存在这些体的世界。 由于Box2D 是独立于Phaser的API, 您还必须运行一些常规来将物理体与PhaserZ视觉物体同步 。

所有此代码都是由 Phaser 编辑器生成的, 您只需要启用相应的参数。 在检查者看来, 显示的** Box2D** 部分 :

![Box2D scene parameters](https://cdn.phaser.games/oss-docs/assets/6457b6c63f103d23-box2d-scene-parameters-20250213.webp)

默认情况下,场景不会生成创建世界的代码,因此第一步是启用**Generate Box2D World Code**参数.

一旦启用,您就可以验证您现场的世界的创建:

```javascript
// Box2D world creation
SetWorldScale(40);
const world = CreateWorld({ worldDef: { 
    ...b2DefaultWorldDef()
}});
this.worldId = world.worldId;
```

一旦您启用了世界代码生成, 检查官就会出现一个新的段落, 您可以在此配置世界参数 :

![World settings](https://cdn.phaser.games/oss-docs/assets/2134bade861660a8-box2d-world-parameters-20250213.webp)


### 更新方法 {#the-update-method}

Box2D 世界必须在每个框中更新。 要做到这一点, 您必须启用 ** Generate Box2D 更新世界代码** 参数。 这将生成代码, 以 `update` 方法更新世界 :

```javascript
update(time, delta) {

	WorldStep({ worldId: this.worldId, deltaTime: delta });
	UpdateWorldSprites(this.worldId);
}
```

然而,您可能需要写出自己的更新方法,这样您就可以禁用此参数并手动写入代码。在这种情况下,编辑器会生成一个`updateWorld()`方法,您可以从您的自定义的`update`方法调用它。

这是编辑器生成的方法 :

```javascript
updateWord(time, delta) {

	WorldStep({ worldId: this.worldId, deltaTime: delta });
	UpdateWorldSprites(this.worldId);
}
```

由此,你可以从你的定制 `update`方法中称之为:

```javascript
update(time, delta) {

    this.updateWorld(time, delta);

    // your custom code here
}
```

### 调试绘图 {#the-debug-draw}

在物理游戏中,将物理体可视化非常有用。您有两种参数与调试绘图相关。第一个参数是启用编辑器中的调试绘图,第二个参数是启用游戏中的调试绘图(生成代码).

所以,当你启用 **Debug Box2D 在编辑器**时,场景将会显示编辑器中的物理体:

![Enable box2d editor debug](https://cdn.phaser.games/oss-docs/assets/ccb41e40e467dddb-box2d-enable-editor-debug-20250214.webp)


如果您启用参数**Generate Box2D调试码**, 编辑器将生成代码来绘制游戏中的物理实体。 在此问题上, 您必须复制项目中的 `PhaserDebugDraw.js`文件, 因为其中包含所有调试绘图程序。 您可以使用 [get it from its repository](https://github.com/phaserjs/box2d-examples/blob/main/examples/phaser/PhaserDebugDraw.js) 。

---
