import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-CN',
  title: 'Phaser 4 中文文档',
  description: 'Phaser 4 简体中文社区文档，涵盖版本迁移与 WebGL 着色器。',
  srcExclude: ['README.md'],
  themeConfig: {
    nav: [
      { text: '指南', link: '/guide/migration', activeMatch: '^/guide/' },
      { text: '官方 API', link: 'https://www.phaser.io/oss/docs/api-documentation/api-documentation' },
    ],
    sidebar: {
      '/guide/': [
        {
          text: 'Phaser 4 指南',
          items: [
            { text: '从 Phaser 3 迁移', link: '/guide/migration' },
            { text: '着色器指南', link: '/guide/shaders' },
          ],
        },
      ],
    },
    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '文档菜单',
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
    footer: {
      message: '社区翻译 · <a href="/license.txt">上游 MIT 许可证</a>',
    },
    search: {
      provider: 'local',
      options: {
        miniSearch: {
          options: {
            tokenize: (text) => {
              const tokens: string[] = []
              const segmenter = typeof Intl.Segmenter === 'function'
                ? new Intl.Segmenter('zh-CN', { granularity: 'word' })
                : undefined

              for (const part of text.match(/\p{Script=Han}+|[a-z0-9_]+/gi) ?? []) {
                if (/^\p{Script=Han}/u.test(part) && segmenter) {
                  for (const segment of segmenter.segment(part)) {
                    if (segment.isWordLike) tokens.push(segment.segment)
                  }
                } else {
                  tokens.push(part)
                }
              }

              return tokens
            },
          },
        },
        translations: {
          button: {
            buttonText: '搜索文档',
            buttonAriaLabel: '搜索文档',
          },
          modal: {
            displayDetails: '显示详细结果',
            resetButtonTitle: '清空搜索',
            backButtonTitle: '关闭搜索',
            noResultsText: '未找到结果',
            footer: {
              selectText: '选择',
              navigateText: '切换',
              closeText: '关闭',
            },
          },
        },
      },
    },
  },
})
