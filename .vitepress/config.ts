import { defineConfig } from 'vitepress'
import guidePages from './guide-sidebar.json'

const apiSections = [
  ['类', 'classes'], ['命名空间', 'namespaces'], ['事件', 'events'],
  ['函数', 'functions'], ['常量', 'constants'], ['类型定义', 'typedefs'],
]

export default defineConfig({
  lang: 'zh-CN',
  title: 'Phaser 4 中文文档',
  description: 'Phaser 4 的简体中文指南与 API 参考。',
  cleanUrls: true,
  srcExclude: ['README.md'],
  themeConfig: {
    nav: [
      { text: '指南', link: '/guide/', activeMatch: '^/guide/' },
      { text: 'API 参考', link: '/api/', activeMatch: '^/api/' },
      { text: '搜索', link: '/search' },
    ],
    sidebar: {
      '/guide/': [
        { text: '入门', items: guidePages.filter(page => page.link.startsWith('/guide/getting-started/')) },
        { text: '核心概念', collapsed: false, items: guidePages.filter(page => page.link.startsWith('/guide/concepts/')) },
        {
          text: '补充指南',
          items: [
            { text: '从 Phaser 3 迁移', link: '/guide/migration' },
            { text: '着色器指南', link: '/guide/shaders' },
          ],
        },
      ],
      '/api/': [{
        text: 'Phaser v4.1.0 API',
        items: [
          { text: 'API 索引', link: '/api/' },
          { text: '游戏对象', link: '/api/gameobjects' },
          { text: '物理系统', link: '/api/physics' },
          ...apiSections.map(([text, anchor]) => ({ text, link: `/api/#${anchor}` })),
        ],
      }],
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
  },
})
