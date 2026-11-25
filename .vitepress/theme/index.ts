import { inBrowser, type DefaultTheme, type Theme } from 'vitepress'
import defaultTheme from 'vitepress/theme'
import { tokenizeSearch } from '../search'

export default {
  extends: defaultTheme,
  enhanceApp({ siteData }) {
    const themeConfig = siteData.value.themeConfig as DefaultTheme.Config
    const search = themeConfig.search
    if (!inBrowser || search?.provider !== 'local') return

    // VitePress 1.x omits functions from the site data sent to the browser.
    siteData.value = {
      ...siteData.value,
      themeConfig: {
        ...themeConfig,
        search: {
          ...search,
          options: {
            ...search.options,
            miniSearch: {
              ...search.options?.miniSearch,
              options: { ...search.options?.miniSearch?.options, tokenize: tokenizeSearch },
            },
          },
        },
      },
    }
  },
} satisfies Theme
