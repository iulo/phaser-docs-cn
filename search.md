---
title: 搜索文档
outline: false
---

<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import { withBase } from 'vitepress'

const loading = ref(true)
const unavailable = ref(false)
let search

onMounted(async () => {
  const css = withBase('/pagefind/pagefind-ui.css')
  if (!document.querySelector(`link[href="${css}"]`)) {
    const link = document.createElement('link')
    link.rel = 'stylesheet'
    link.href = css
    document.head.append(link)
  }

  try {
    if (!window.PagefindUI) {
      await new Promise((resolve, reject) => {
        const script = document.createElement('script')
        script.src = withBase('/pagefind/pagefind-ui.js')
        script.onload = resolve
        script.onerror = reject
        document.head.append(script)
      })
    }
    if (document.getElementById('docs-search')) {
      search = new window.PagefindUI({
        element: '#docs-search',
        showImages: false,
        showSubResults: true,
        translations: { placeholder: '搜索中文或 Phaser API 名称' },
      })
    }
  } catch {
    unavailable.value = true
  } finally {
    loading.value = false
  }
})

onUnmounted(() => search?.destroy?.())
</script>

<style>
#docs-search {
  --pagefind-ui-primary: var(--vp-c-brand-1);
  --pagefind-ui-text: var(--vp-c-text-1);
  --pagefind-ui-background: var(--vp-c-bg);
  --pagefind-ui-border: var(--vp-c-divider);
  --pagefind-ui-tag: var(--vp-c-bg-soft);
  --pagefind-ui-font: var(--vp-font-family-base);
}
</style>

# 搜索文档

<div id="docs-search" data-pagefind-ignore></div>
<p v-if="loading" role="status">正在加载搜索索引…</p>
<p v-else-if="unavailable" role="status">搜索索引暂不可用。请先构建站点，再打开预览。</p>
