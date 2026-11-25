# 代理配置 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/misc/proxy)

Phaser编辑器使用不同的技术: Go, Electron, NodeJS. 为它们设置一个代理可能具有挑战性,而你们中有些人正在公司网络中工作. v4.2.0. 我们引入了一个新的UI来设置一个统一的代理配置.

当您打开编辑器时, 它会显示一个页面来登录您的 Phaser 账户。 在下/左角有一个链接来打开代理设置 :

![change proxy](https://cdn.phaser.io/editor-docs/change-proxy-link-projects.webp)

如果您已经登录, 您可以在工程页面的设置中找到链接 :

![change proxy link](https://cdn.phaser.io/editor-docs/change-proxy-link.webp)

它打开了代理配置页面。 您可以在此设置不同的参数并保存。 要让代理设置有效, 您应该重新启动编辑器 。

![proxy configuration page](https://cdn.phaser.io/editor-docs/proxy-settings.webp)

代理参数存储在 `<user-home>/.phasereditor2d/settings.json` 文件。 它是 JSON 文件, 包含以下代理域 :

```json
{
    "proxy": "http://myuser:mypassword@proxy.mycompany.com:8080",
}
```

它是一个与代理服务器的 URL 的单一字符串。 URL 可以包含用户和密码以及端口。 您可以随意更改它, 但您应该重新启动编辑器, 以使更改有效 。

还有 `proxyDisabled` 字段。 这是一个布尔值, 表示代理是否被启用。 如果您想要禁用该代理, 您可以将这个字段设置为 `false` 。

```json
{
    "proxyDisabled": true
}
```

---
