# 预制体 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/scene-editor/prefabs)

预制体（Prefab）是场景编辑器中可复用的对象模板，借鉴了 [Unity](https://unity.com) 的预制体概念。

同一关卡中可能有多只外观和行为相同的敌人，金币可能共用拾取动画和音效，玩家对象也可能在多个关卡中复用。可以先为每种对象创建预制体，再把预制体的多个实例放进场景。

[场景编译器](/editor/scene-editor/scene-compiler)会把预制体场景编译成一个类。这个类可以继承 Phaser 内置类型、脚本节点或另一个预制体类。场景中的预制体对象是这个类的实例。

可以为单个实例修改属性。修改预制体的默认属性时，所有尚未覆盖该属性的实例都会继承新值。要了解继承、组合和属性覆盖的具体行为，可以查看场景编译器生成的代码。
