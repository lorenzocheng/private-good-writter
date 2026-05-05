const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat,
  HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageNumber, ImageRun, PageBreak
} = require("docx");

// Read markdown content
const mdContent = fs.readFileSync("drafts/20260505_股东月度简报_v3.md", "utf-8");

const FONT_CN = "SimSun";
const FONT_EN = "Arial";
const FONT_SIZE = 24; // 12pt in half-points
const COLOR_BLACK = "000000";

// Parse sections
function parseMarkdown(md) {
  md = md.replace(/^---[\s\S]*?---\n/, "");

  const lines = md.split("\n");
  const children = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    if (line.includes('<div class="signature">')) {
      i++;
      let name = "", date = "";
      while (i < lines.length) {
        const ln = lines[i].trim();
        if (ln.startsWith("</div>")) break;
        if (ln && !name) name = ln;
        else if (ln && name && !date) date = ln;
        i++;
      }
      children.push(new Paragraph({ spacing: { before: 2000 }, children: [] }));
      children.push(new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { after: 60 },
        children: [new TextRun({ text: name, font: FONT_CN, size: FONT_SIZE })],
      }));
      children.push(new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: date, font: FONT_CN, size: FONT_SIZE })],
      }));
      i++;
      continue;
    }

    if (line.trim() === "") { i++; continue; }

    if (line.startsWith("## ")) {
      children.push(new Paragraph({
        spacing: { before: 360, after: 120 },
        children: [new TextRun({
          text: line.replace("## ", ""),
          font: FONT_CN,
          size: FONT_SIZE + 4,
          bold: true,
          color: COLOR_BLACK,
        })],
      }));
      i++;
      continue;
    }

    if (line.startsWith("|")) {
      const rows = [];
      while (i < lines.length && lines[i].startsWith("|")) {
        if (!lines[i].includes("---")) {
          const cells = lines[i].split("|").filter(c => c.trim());
          rows.push(cells);
        }
        i++;
      }

      if (rows.length >= 2) {
        const border = { style: BorderStyle.SINGLE, size: 1, color: "333333" };
        const borders = { top: border, bottom: border, left: border, right: border };
        const cellMargins = { top: 60, bottom: 60, left: 100, right: 100 };

        const headerRow = rows[0];
        const dataRows = rows.slice(1);
        const colWidth = Math.floor(9026 / headerRow.length);

        const tableRows = [
          new TableRow({
            children: headerRow.map(h => new TableCell({
              borders,
              width: { size: colWidth, type: WidthType.DXA },
              shading: { fill: "e0e0e0", type: ShadingType.CLEAR },
              margins: cellMargins,
              children: [new Paragraph({
                alignment: AlignmentType.CENTER,
                children: [new TextRun({ text: h.trim(), font: FONT_CN, size: 22, bold: true, color: COLOR_BLACK })],
              })],
            }))
          }),
          ...dataRows.map(row => new TableRow({
            children: row.map(cell => new TableCell({
              borders,
              width: { size: colWidth, type: WidthType.DXA },
              margins: cellMargins,
              children: [new Paragraph({
                children: [new TextRun({ text: cell.trim(), font: FONT_CN, size: 22, color: COLOR_BLACK })],
              })],
            }))
          }))
        ];

        children.push(new Table({
          width: { size: 9026, type: WidthType.DXA },
          columnWidths: Array(headerRow.length).fill(colWidth),
          rows: tableRows,
        }));
      }
      continue;
    }

    children.push(new Paragraph({
      spacing: { after: 120 },
      indent: { firstLine: 480 },
      children: [new TextRun({
        text: line,
        font: FONT_CN,
        size: FONT_SIZE,
        color: COLOR_BLACK,
      })],
    }));
    i++;
  }

  return children;
}

const content = parseMarkdown(mdContent);

const openingLines = [
  new Paragraph({
    spacing: { after: 200 },
    children: [new TextRun({ text: "各位股东：", font: FONT_CN, size: FONT_SIZE, color: COLOR_BLACK })],
  }),
  new Paragraph({
    spacing: { after: 200 },
    children: [new TextRun({ text: "见信好。", font: FONT_CN, size: FONT_SIZE, color: COLOR_BLACK })],
  }),
];

const allContent = [...openingLines, ...content];

const logoData = fs.readFileSync(".logo/LOGO.png");

const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: FONT_CN, size: FONT_SIZE, color: COLOR_BLACK }
      },
    },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({
        children: [
          new Paragraph({
            alignment: AlignmentType.RIGHT,
            children: [
              new ImageRun({
                type: "png",
                data: logoData,
                transformation: { width: 120, height: 35 },
                altText: { title: "毅湃科技", description: "毅湃科技 Logo", name: "Logo" },
              }),
            ],
          }),
        ],
      }),
    },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({ text: "第 ", font: FONT_EN, size: 18, color: COLOR_BLACK }),
              new TextRun({ children: [PageNumber.CURRENT], font: FONT_EN, size: 18, color: COLOR_BLACK }),
              new TextRun({ text: " 页", font: FONT_EN, size: 18, color: COLOR_BLACK }),
            ],
          }),
        ],
      }),
    },
    children: allContent,
  }],
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("output/20260505_毅湃科技近期进展汇报.docx", buffer);
  console.log("DOCX generated: output/20260505_毅湃科技近期进展汇报.docx");
});
