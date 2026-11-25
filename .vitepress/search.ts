const chineseSegmenter = typeof Intl.Segmenter === 'function'
  ? new Intl.Segmenter('zh-CN', { granularity: 'word' })
  : undefined

export function tokenizeSearch(text: string): string[] {
  const tokens: string[] = []

  for (const part of text.match(/\p{Script=Han}+|[a-z0-9_]+/giu) ?? []) {
    if (chineseSegmenter && /^\p{Script=Han}/u.test(part)) {
      for (const segment of chineseSegmenter.segment(part)) {
        if (segment.isWordLike) tokens.push(segment.segment)
      }
    } else {
      tokens.push(part)
    }
  }

  return tokens
}
