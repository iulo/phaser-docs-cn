# 粒子发射器（ParticleEmitter） {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/game-objects/particle-emitter-object)

[ParticleEmitter](/api/class/gameobjects-particles-particleemitter)游戏对象是Phaser的惊人而大型的特征.

它允许你创作粒子动画, 从液体到爆炸.

Phaser编辑器支持在现场添加粒子发射器,调整其属性,并预览它们。由于它使用相同的PhaserZ API,所以在场景编辑器中获得的动画与游戏中获得的动画相同.

## 创建粒子 Emitter 游戏对象 {#create-a-particle-emitter-game-object}

您可以从块视图中丢弃一个内置类型, 从而创建粒子 Emitter 对象。 它与其他游戏对象相同 :

![Drop a particle emitter to the scene](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-create-1-20240611.webp)

将粒子 Emitter 块放下后立即打开对话框来选择发射方的帧。 您可以从纹理图集中选择图像纹理或多个帧 :

![Select frames](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-create-select-frames-20240611.webp)

按下 ** 选择 ** 后, 粒子 Emitter 会在现场创建 :

![Fresh particle emitter in the scene](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-create-done-20240611.webp)

下一步是更改编辑器的任何属性。 您可以在 ** 督察** 视图中更改它们。 为了这个例子, 我们将将 ** 描述** 属性修改为 200 :

![Change the speed](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-change-speed-20240611.webp)


### 播放和刷新场景 {#play-and-refresh-the-scene}

更改速度后, 您可以看到场景编辑器的更改。 但是您需要移动一点场景。 默认情况下, 场景编辑器不会运行游戏的更新循环, 这样您可以得到一个静态的发射器图片。 要移动并看到粒子动画, 您可以在场景底部的场景工具栏中按下 ** Play** 按钮。 在 ** Play ** 按钮旁边, 您可以看到 ** Refresh** 按钮。 您可以用它来重建场景, 并看到来自其新状态的发射器。 有些行为你可以设定给一个发射器, 如** duration**, 只能通过刷新/ 重现场景来重复:

![Play and re-create the scene](https://cdn.phaser.io/editor-docs/scene-editor-particle-emitter-scene-toolbar-20240611.webp)


### 代码生成 {#code-generation}

当向现场添加粒子发射器时,[scene compiler](/editor/scene-editor/scene-compiler)生成这样的代码: .

```javascript
this.add.particles(305, 343, "flares", {frame: ["red", "white"], speed: 200});
```

您设置给发射器的所有属性都作为`particles`方法配置参数的一部分传递.
和其他游戏对象一样,你可以使用粒子发射器的[create a prefab](/editor/scene-editor/prefabs).

---
