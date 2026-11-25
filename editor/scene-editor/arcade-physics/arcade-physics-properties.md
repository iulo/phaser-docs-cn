# Arcade 物理体属性 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/arcade-physics/arcade-physics-properties)

当您选择对象时, 检查器视图会显示编辑器, 用于编辑对象的弧形体 。

属性按下列各节分类:


## 拱门物理科 {#arcade-physics-body-section}

它允许将物理体类型更改为 [dynamic](/api/class/physics-arcade-body) 或 或 时 间 [static](/api/class/physics-arcade-staticbody)设置 [enable flag](/api/class/physics-arcade-body#enable):

![Arcade Physics Body section.](https://cdn.phaser.io/editor-docs/arcade-physics-body-properties-20221006.webp)


## Arcade 物理体几何部分 {#arcade-physics-body-geometry-section}

本节包含设置物理体偏移大小的属性。 您可以在 ** 图形** 参数中选择物理体形状。 如果物理体是长方形, 您可以更改其形状 。 [Size](/api/class/physics-arcade-body#setSize)。如果物理体是圆形,你可以改变它。 [Radius](/api/class/physics-arcade-body#setCircle)。在这两种情况下,您都可以更改 [Offset](/api/class/physics-arcade-body#setOffset).

![Arcade Physics Body Geometry section.](https://cdn.phaser.io/editor-docs/arcade-physics-body-geometry-properties-20221006.webp)

改变物理体的抵消和大小的另一种方法是激活[Arcade Physics Body Tool](/editor/scene-editor/manipulation-tools#arcade-physics-body-tool).

另外,在场景上下文菜单中,在**Arcade 物理**中,有**Center Body**和**Resize Body To Object Size**的选项。这些命令也可以在属性部分的三角菜单中找到:

![Arcade Physics Body Geometry section's menu.](https://cdn.phaser.io/editor-docs/arcade-physics-body-geaometry-properties-menu-20221006.webp)

** Center Arcade body ** 命令将物理体置于对象的中心。 ** 恢复对象大小** 命令中心并调整大小以填充整个对象。如果物体是圆形,则改变半径以填充对象的宽度。


## Arcade 物理体运动科 {#arcade-physics-body-movement-section}

本节包含所有与运动相关的物理体属性:

* [Move](/api/class/physics-arcade-body#moves)
* [Velocity](/api/class/physics-arcade-body#velocity)
* [Max Velocity](/api/class/physics-arcade-body#maxVelocity)
* [Max Speed](/api/class/physics-arcade-body#maxSpeed)
* [Allow Gravity](/api/class/physics-arcade-body#allowGravity)
* [Gravity](/api/class/physics-arcade-body#gravity)
* [Acceleration](/api/class/physics-arcade-body#acceleration)
* [Use Damping](/api/class/physics-arcade-body#useDamping)
* [Allow Drag](/api/class/physics-arcade-body#allowDrag)
* [Drag](/api/class/physics-arcade-body#drag)
* [Allow Rotation](/api/class/physics-arcade-body#allowRotation)
* [Angular Velocity](/api/class/physics-arcade-body#angularVelocity)
* [Angular Acceleration](/api/class/physics-arcade-body#angularAcceleration)
* [Angular Drag](/api/class/physics-arcade-body#angularDrag)
* [Max Angular](/api/class/physics-arcade-body#maxAngular)

![Arcade Physics Body Movement section.](https://cdn.phaser.io/editor-docs/arcade-physics-body-movement-properties-20221006.webp)


## Arcade 物理体碰撞部分 {#arcade-physics-body-collision-section}

本节载有与碰撞有关的物理体特性:

* [Pushable](/api/class/physics-arcade-body#pushable)
* [Immovable](/api/class/physics-arcade-body#immovable)
* [Mass](/api/class/physics-arcade-body#mass)
* [Bounce](/api/class/physics-arcade-body#bounce)
* [Friction](/api/class/physics-arcade-body#friction)
* [Overlap](/api/class/physics-arcade-body#overlapX)
* [OverlapR](/api/class/physics-arcade-body#overlapR)
* [Collide World Bounds](/api/class/physics-arcade-body#collideWorldBounds)
* [On World Bounds](/api/class/physics-arcade-body#onWorldBounds)
* [Check Collision](/api/class/physics-arcade-body#checkCollision)

![Arcade Physics Body Collision properties.](https://cdn.phaser.io/editor-docs/arcade-physics-body-collision-properties-20231205.webp)

---
