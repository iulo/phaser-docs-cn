<script setup lang="ts">
import { onMounted } from 'vue'
import { withBase } from 'vitepress'
import DefaultTheme from 'vitepress/theme'

const sections = [
  { name: '开发指南', description: '场景、精灵、输入、渲染与物理', path: '/guide/', icon: '◫' },
  { name: 'API 参考', description: 'Phaser v4.1.0 的类、事件与类型', path: '/api/', icon: '{ }' },
  { name: 'Editor 手册', description: 'Phaser Editor v5 的工作台、资源与预制体', path: '/editor/', icon: '▤' },
]

// The dev server can serve the index from the last local build.
const searchAssets = withBase(import.meta.env.DEV ? '/.vitepress/dist/pagefind/' : '/pagefind/')

onMounted(() => {
  if (document.querySelector('script[data-pagefind-ui]')) return

  const stylesheet = document.createElement('link')
  stylesheet.rel = 'stylesheet'
  stylesheet.href = searchAssets + 'pagefind-component-ui.css'

  const script = document.createElement('script')
  script.type = 'module'
  script.src = searchAssets + 'pagefind-component-ui.js'
  script.setAttribute('data-pagefind-ui', '')
  document.head.append(stylesheet, script)
})
</script>

<template>
  <DefaultTheme.Layout>
    <template #nav-bar-content-before>
      <div class="arcade-nav-search">
        <pagefind-modal-trigger placeholder="搜索文档"></pagefind-modal-trigger>
      </div>
    </template>

    <template #home-hero-before>
      <main class="arcade-home">
        <div class="arcade-hero">
          <p class="arcade-version">Phaser 4</p>
          <h1>简体中文文档</h1>
          <p class="arcade-description">开发指南、API 参考和 Phaser Editor v5 手册。</p>
          <div class="arcade-actions">
            <a class="arcade-button primary" :href="withBase('/guide/')">阅读指南</a>
            <a class="arcade-button" :href="withBase('/guide/concepts/scenes')">浏览场景示例</a>
          </div>
        </div>
        <div class="arcade-directory">
          <a v-for="section in sections" :key="section.path" :href="withBase(section.path)">
            <span class="arcade-symbol" aria-hidden="true">{{ section.icon }}</span>
            <h2>{{ section.name }}</h2>
            <p>{{ section.description }}</p>
          </a>
        </div>
      </main>
    </template>

    <template #layout-bottom>
      <pagefind-config :bundle-path="searchAssets" :base-url="withBase('/')"></pagefind-config>
      <pagefind-modal>
        <pagefind-modal-header>
          <pagefind-input placeholder="搜索中文或 Phaser API 名称"></pagefind-input>
        </pagefind-modal-header>
        <pagefind-modal-body>
          <pagefind-summary></pagefind-summary>
          <pagefind-results></pagefind-results>
        </pagefind-modal-body>
        <pagefind-modal-footer>
          <pagefind-keyboard-hints></pagefind-keyboard-hints>
        </pagefind-modal-footer>
      </pagefind-modal>
    </template>
  </DefaultTheme.Layout>
</template>
