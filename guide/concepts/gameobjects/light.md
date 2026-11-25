# 光源 {#page-title}

Phaser 4 指南 · [英文原文](https://phaser.io/oss/docs/phaser/concepts/gameobjects/light)

由`Phaser.GameObjects.LightsManager`创造的2D光,通过`this.lights`从场景内部可以获取.

任何使用Light2D管道的游戏对象,只要有正常的地图,就会受到这些Lights的影响.

也可以简单地用来代表你自己的目的的点光.

警告我,我警告你,我警告你,你该死WebGL 仅此而已"
    灯光不能添加到容器中,它们被设计成存在于场景的根部。

警告我,我警告你,我警告你,你该死WebGL 仅此而已"
    只在WebGL渲染模式下有效.

## 灯光管理器 {#lights-manager}

### 启用灯光管理器 {#enable-lights-manager}

- Enable

    ```javascript
    this.lights.enable();
    ```

- Disable

    ```javascript
    this.lights.disable();
    ```

    or

    ```javascript
    this.lights.active = false;
    ```

### 环境颜色 {#ambient-color}

```javascript
this.lights.setAmbientColor(color);
```

- `color` :整数的颜色值.

### 让灯光管理员管理所有灯光 {#get-all-lights-managed-by-this-lights-manager}

```javascript
    var lightsCount = this.lights.getLightCount();
```

### 照亮所有灯光 {#get-all-lights-seen-by-the-given-camera}

```javascript
    var visibleLights = this.lights.getLights(camera);
```

- `camera` 摄像机可以把灯光烧掉

### 获取允许显示的最大灯光数 {#get-maximum-number-of-lights-allowed-to-appear}

```javascript
    var maxVisibleLights = this.lights.getMaxVisibleLights();
```

### 关灯管理器 {#shut-down-the-lights-manager}

回收所有活动灯光进入灯池,重新调整环境灯色,并清除灯光和阴光的列表.

```javascript
    this.lights.shutdown();
```

## 光滑游戏对象 {#light-game-object}

- Add

    ```javascript
    var light = this.lights.addLight(x, y, radius);
    // var light = this.lights.addLight(x, y, radius, color, intensity);
    ```

  - `x`,`y`:光线的横向/垂直位置,默认为0.
  - `radius` :光线半径,默认值为128. 默认值为0.
  - `color`:光线的整数RGB颜色,默认为`0xffffff`.
  - `intensity` : 光线的强度,默认值为1.
- 添加点亮
  - 点光游戏对象提供了一种在游戏中添加点光效果的方法,而不需要传统的光游戏对象的昂贵的遮光处理要求. 它使定制的遮光器在游戏中给人以点光源,可变半径,强度和颜色的印象. 然而,它与光游戏对象不同,它不会影响其他游戏对象,或者用普通的地图进行计数,这使得它们与光相比,制作速度极快,并适合特殊效果,如闪光灯或口哨闪光.

    ```javascript
    var light = this.lights.addPointLight(x, y, color, radius, intensity, attenuation);
    ```

  - `x`,`y`:光线的横向/垂直位置.
  - `color`:光线的整数RGB颜色,默认为`0xffffff`.
  - `radius` :光线半径,默认值为128.
  - `intensity` : 光线的强度,默认值为1.
  - `attenuation`:点光的衰减。这是从中心点的光的衰减。默认值为0.1。
- Remove

    ```javascript
    this.lights.removeLight(light);
    ```

- Destroy

    ```javascript
    this.lights.destroy();
    ```

### 职位 {#position}

- Set

    ```javascript
    light.setPosition(x, y);
    ```

    or

    ```javascript
    light.x = x;
    light.y = y;
    ```

- Get

    ```javascript
    var x = light.x;
    var y = light.y;
    ```

### 颜色 {#color}

- Set
  - 红、绿、蓝

    ```javascript
    light.color.set(red, green, blue);
    ```

    or

    ```javascript
    light.color.r = red;
    light.color.g = green;
    light.color.b = blue;
    ```

  - 整数

    ```javascript
    light.setColor(colorInteger);
    ```

- Get
  - 红、绿、蓝

    ```javascript
    var red = light.color.r;
    var green = light.color.g;
    var blue = light.color.b;
    ```

### 大小 {#size}

- Set

    ```javascript
    light.setRadius(radius);
    // light.radius = radius;
    ```

    or

    ```javascript
    light.diameter = diameter;
    // light.width = diameter;
    // light.height = diameter;
    // light.displayWidth = diameter;
    // light.displayHeight = diameter;
    ```

- Get

    ```javascript
    var radius = light.radius;
    ```

    or

    ```javascript
    var diameter = light.diameter;
    // var diameter = light.displayWidth;
    // var diameter = light.displayHeight;
    // var diameter = light.width;
    // var diameter = light.height;
    ```

### 强度 {#intensity}

- Set

    ```javascript
    light.setIntensity(intensity);
    ```

    or

    ```javascript
    light.intensity = intensity;
    ```

- Get

    ```javascript
    var intensity = light.intensity;
    ```

## 游戏对象 {#game-object}

### 装入正常地图的纹理 {#load-texture-with-normal-map}

```javascript
this.load.image(key, [url, normalMapUrl]);
```

- `url` : 脏脏脏腑.
- `url` : 脏脏脏腑.
- `normalMapUrl` : 正常地图的Url.

### 应用轻管 {#apply-light-pipeline}

```javascript
gameObject.setPipeline('Light2D');
```

## 作者的信用额度 {#author-credits}

本页的内容包括下列工作:

- [RexRainbow](https://github.com/rexrainbow)

---
