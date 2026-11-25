# Phaser.Physics.Matter.PhysicsEditorParser {#page-title}

Phaser v4.1.0 · [英文原文](https://phaser.io/oss/docs/api-documentation/namespace/physics-matter-physicseditorparser)

Scope: 
static
> 源码：[src/physics/matter-js/PhysicsEditorParser.js#L15](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsEditorParser.js#L15)  
引入版本：3.10.0

## 静态函数 {#static-functions}

### parseBody {#parseBody}

#### \<static> parseBody(x, y, config, [options]) {#static-parsebodyx-y-config-options}


**说明:**

解析物理编辑器导出的物理体配置,并从中创建复合 Matter.js body。组合中的每个固定定义都被解析并转换成一个儿童物理体(圆形或凸起多边形),所有儿童物理体被组合成一个位于指定世界坐标的单一复合体。额外的 Matter.j 物理体属性可以通过`options`参数提供,并将合并到物理体配置中。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| x | number | 否 | 物理体的横向世界位置. |
| y | number | 否 | 物理体的垂直世界位置. |
| config | object | 否 | 物理编辑器导出的物理体配置和固定(儿童物理体)定义。 |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** MatterJS.BodyType - 复合物 物质JS体。


> 源码：[src/physics/matter-js/PhysicsEditorParser.js#L29](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsEditorParser.js#L29)  
引入版本：3.10.0


---

### parseFixture {#parseFixture}

#### \<static> parseFixture(fixtureConfig) {#static-parsefixturefixtureconfig}


**说明:**

从物理编辑器导出的“固定”列表中解析一个单个固定条目。固定选项可以描述圆(由中心位置和半径定义)或一组凸起多边形顶点列表。适当的 Matter.js 的机体或机体被创建并作为数组返回,以便由调用器将它们组合成复合机体。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| fixtureConfig | object | 否 | 固定对象来分析。 |


**返回值:** Array.\<MatterJS.BodyType> - - 一系列物质JS机构。


> 源码：[src/physics/matter-js/PhysicsEditorParser.js#L79](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsEditorParser.js#L79)  
引入版本：3.10.0


---

### parseVertices {#parseVertices}

#### \<static> parseVertices(vertexSets, [options]) {#static-parseverticesvertexsets-options}


**说明:**

解析物理编辑器导出的一个或多个顶点设置,并为每个集合创建 Matter.js 物理体。在创建每个物理体之前,顶点按顺时针风向顺序排序,并且将物理体定位在顶点设置的中间体。在所有物理体创建后,标记相邻部分之间的巧合边缘,以便 Matter.j在碰撞探测时正确处理它们。

**参数:**
| 名称 | 类型 | 可选 | 说明 |
| ---- | ---- | -------- | ----------- |
| vertexSets | array | 否 | 顶点列表来分析. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](/api/typedef/types-physics-matter#matterbodyconfig) | 是 | 一个可选的 body 配置对象,用于设定创建时的初始 body 属性 。 |


**返回值:** Array.\<MatterJS.BodyType> - - 一系列物质JS机构。


> 源码：[src/physics/matter-js/PhysicsEditorParser.js#L116](https://github.com/phaserjs/phaser/blob/v4.1.0/src/physics/matter-js/PhysicsEditorParser.js#L116)  
引入版本：3.10.0


---

---
