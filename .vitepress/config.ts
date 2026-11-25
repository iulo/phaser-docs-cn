import { defineConfig } from 'vitepress'
import guidePages from './guide-sidebar.json'
import editorPages from './editor-sidebar.json'

const apiSections = [
  ['类', 'classes'], ['命名空间', 'namespaces'], ['事件', 'events'],
  ['函数', 'functions'], ['常量', 'constants'], ['类型定义', 'typedefs'],
]

const editorSections = [
  ['简介', 'intro'], ['快速入门', 'first-steps'], ['工作台', 'workbench'],
  ['资源包编辑器', 'asset-pack-editor'], ['场景编辑器', 'scene-editor'],
  ['动画编辑器', 'animations-editor'], ['代码编辑器', 'code-editor'],
  ['AI', 'ai'], ['其他', 'misc'],
]

const sceneEditorSections = [
  ['游戏对象', 'game-objects'], ['Arcade 物理', 'arcade-physics'], ['Box2D 物理', 'box2d-physics'],
  ['Spine 动画', 'spine-animations'], ['预制体', 'prefabs'], ['脚本节点', 'script-node'],
  ['用户组件', 'user-components'], ['布局工具', 'layout-tools'],
]

const editorSidebar = editorSections.map(([text, section]) => {
  const prefix = `/editor/${section}/`
  const pages = editorPages.filter(page => page.link.startsWith(prefix))
  const items = pages.filter(page => !page.link.slice(prefix.length).includes('/'))
  if (section !== 'scene-editor') return { text, items, collapsed: true }

  return {
    text,
    collapsed: true,
    items: items.map(page => {
      const nested = sceneEditorSections.find(([, slug]) => page.link === `${prefix}${slug}`)
      if (!nested) return page

      return {
        ...page,
        text: nested[0],
        collapsed: true,
        items: pages.filter(child => child.link.startsWith(`${page.link}/`)),
      }
    }),
  }
})

export default defineConfig({
  lang: 'zh-CN',
  title: 'Phaser 4 中文文档',
  description: 'Phaser 4 的简体中文指南、API 参考与 Phaser Editor v5 手册。',
  cleanUrls: true,
  srcExclude: ['README.md'],
  themeConfig: {
    nav: [
      { text: '指南', link: '/guide/', activeMatch: '^/guide/' },
      { text: 'API 参考', link: '/api/', activeMatch: '^/api/' },
      { text: 'Editor 手册', link: '/editor/', activeMatch: '^/editor/' },
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
      '/editor/': [{ text: 'Phaser Editor v5', link: '/editor/' }, ...editorSidebar],
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
