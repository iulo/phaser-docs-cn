# AI 聊天 {#page-title}

Phaser Editor v5 · [英文原文](https://phaser.io/oss/docs/phaser-editor/ai/chat)

最先进的融合方式 Phaser 带有AI代理的编辑器是通过一个 [MCP server](/editor/ai/mcp-server)。MCP服务器允许其他具有强大AI代理的工具与控制器交互 Phaser 编辑.

然而,我们往往只是希望与AI代理快速互动,以完成非常具体的任务。对于这些案例,我们实施了自己的AI代理,您可以通过Phaser编辑器中包含的聊天窗口与之互动。

要打开聊天窗口,请点击主菜单旁边的聊天图标:

![Open the AI Chat](https://cdn.phaser.games/oss-docs/assets/655f7902a26f5f85-ai-chat-window-20260112.webp)

## 聊天设置 {#chat-settings}

Phaser编辑器支持一些最流行的AI模型:双子座,克劳德,以及兼容OpenAI的模型. 用户必须在AI模型提供者注册,并获得配置编辑器的必要信息,这些信息包括API键和模型ID.

在编辑器设置对话框中, 您可以找到 AI Chat 标签 :

![AI chat settings](https://cdn.phaser.games/oss-docs/assets/4d97c0912331bc5b-ai-chat-settings-20260112.webp)

在此您必须配置至少一个模型, 其 API 键和模型名称 。 您还必须选择最终在聊天中使用的模型( ** Active Model **) 。

您可以写模型的名称, 或者从预定义列表中选择 :

![Ai chat settings](https://cdn.phaser.games/oss-docs/assets/bbaad37e7ae702d5-at-chat-settings-models-20260112.webp)

除了设置对话框,您还可以在聊天窗口设置菜单中直接选择活动模式 :

![settings menu](https://cdn.phaser.games/oss-docs/assets/25420bd0b6bd0c49-ai-chat-settings-button-20260112.webp)

该菜单还允许清除或修剪聊天历史。 “ 修剪” 命令将历史缩小为一半 。

聊天窗口左侧的历史按钮显示, 消息消耗了多少模式上下文 :

![Context usage](https://cdn.phaser.games/oss-docs/assets/3659ad11f7a22a46-ai-chat-context-usage-20260112.webp)

## 提示上下文 {#prompt-context}

给AI代理给出指令的一个重要部分是提供正确的上下文. 例如,如果我们想要创建具有特定纹理的游戏对象,我们需要准确的描述该纹理的名称.

聊天窗口包括一个附加元素的章节, 以提供上下文以备及时。 进程很简单: 用户从编辑器中拖动一个元素并将其降入聊天窗口。 所有附加元素都将在一个专用的段落中显示, 用户可以附加更多的元素或者删除已经附加的元素 。

![Drop texture in context section](https://cdn.phaser.games/oss-docs/assets/e69ba34303d40945-ai-chat-attach-texture-context-20260114.webp)

目前,用户可以在此上下文部分添加三种元素: 用户可以使用用户的功能,可以使用用户的功能.

- 资源: 您可以从块视图拖曳资源 。
- 场景文件:您可以从块视图(prefabs)或文件视图中拖曳场景文件.
- 游戏对象:您可以从场景编辑器的大纲视图中拖曳一个游戏对象.

用户界面将显示每个附件的名称, 但如果您想要看到在提示中使用的准确文本, 您可以在附件上徘徊鼠标, 工具提示会显示您的全部信息 。

![Attachment tooltip](https://cdn.phaser.games/oss-docs/assets/b2e7ac5d6cb26343-ai-chat-context-attachment-tooltip-20260.webp)

---
