// 毅湃科技文档模板
#set page(
  paper: "a4",
  margin: (x: 2.5cm, y: 2.5cm),
  header: context {
    place(top + right, image("/.logo/LOGO.png", width: 35mm))
  },
  footer: context {
    [#counter(page).display() / #counter(page).final().first()]
  },
)

#set text(
  font: ("Liberation Sans", "Noto Serif CJK SC"),
  size: 11pt,
  lang: "zh",
)

#set par(
  justify: true,
  leading: 0.8em,
  first-line-indent: 2em,
)

// 标题样式
#show heading.where(level: 2): it => {
  set text(size: 14pt, weight: "bold", fill: rgb("#0066cc"))
  v(1em)
  it
  v(0.3em)
}

#show heading.where(level: 3): it => {
  set text(size: 12pt, weight: "bold")
  v(0.8em)
  it
  v(0.2em)
}

// 表格样式
#set table(
  stroke: 0.5pt + black,
  align: (start, start),
)

#show table.cell.where(y: 0): set text(weight: "bold")

// 链接样式
#show link: set text(fill: rgb("#0066cc"))

// 强调样式
#show strong: set text(weight: "bold")

// 签名样式
#let signature(name, date) = {
  set align(right)
  set par(first-line-indent: 0em)
  v(2cm)
  [#name \ #date]
}
