import DefaultTheme from 'vitepress/theme'
import ArcadeLayout from './ArcadeLayout.vue'
import './arcade.css'

export default {
  extends: DefaultTheme,
  Layout: ArcadeLayout,
}
