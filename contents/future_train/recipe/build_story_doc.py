from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "publish" / "manuscript_rewrite.md"
OUTPUT = ROOT / "publish" / "미래로_가는_기차_단편_초고.docx"

FONT = "Noto Serif CJK KR"


def set_font(style, size, bold=False):
    style.font.name = FONT
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.color.rgb = RGBColor(0, 0, 0)
    r_pr = style.element.get_or_add_rPr()
    r_fonts = r_pr.rFonts
    if r_fonts is None:
        r_fonts = OxmlElement("w:rFonts")
        r_pr.insert(0, r_fonts)
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        r_fonts.set(qn(f"w:{key}"), FONT)


def add_page_number(paragraph):
    paragraph.add_run("— ")
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    paragraph._p.append(field)
    paragraph.add_run(" —")


def set_cell_background(cell, color):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), color)


def set_table_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.find(qn("w:tblBorders"))
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        node = borders.find(qn(f"w:{edge}"))
        if node is None:
            node = OxmlElement(f"w:{edge}")
            borders.append(node)
        node.set(qn("w:val"), "single")
        node.set(qn("w:sz"), "4")
        node.set(qn("w:color"), "D9D9D9")


def add_table(doc, markdown_rows):
    rows = [
        [part.strip() for part in line.strip().strip("|").split("|")]
        for line in markdown_rows
        if not set(line.replace("|", "").strip()) <= {"-", ":", " "}
    ]
    if not rows:
        return
    cols = max(len(row) for row in rows)
    table = doc.add_table(rows=len(rows), cols=cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    widths = [Inches(x) for x in ([0.85, 1.15, 1.25, 3.15] if cols == 4 else [6.4 / cols] * cols)]
    for j, column in enumerate(table.columns):
        column.width = widths[j]
    for i, values in enumerate(rows):
        row = table.rows[i]
        tr_pr = row._tr.get_or_add_trPr()
        no_split = OxmlElement("w:cantSplit")
        tr_pr.append(no_split)
        if i == 0:
            tbl_header = OxmlElement("w:tblHeader")
            tbl_header.set(qn("w:val"), "true")
            tr_pr.append(tbl_header)
        for j in range(cols):
            cell = row.cells[j]
            cell.width = widths[j]
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if i == 0:
                set_cell_background(cell, "EDEDED")
            p = cell.paragraphs[0]
            p.paragraph_format.first_line_indent = 0
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.18
            run = p.add_run(values[j] if j < len(values) else "")
            run.font.name = FONT
            run.font.size = Pt(8.5)
            run.bold = i == 0


def main():
    doc = Document()
    doc.core_properties.title = "미래로 가는 기차"
    doc.core_properties.subject = "단편소설 초고"
    doc.core_properties.author = ""

    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(0.85)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(1.03)
    section.right_margin = Inches(1.03)
    section.header_distance = Inches(0.3)
    section.footer_distance = Inches(0.4)

    styles = doc.styles
    normal = styles["Normal"]
    set_font(normal, 10.5)
    normal.paragraph_format.line_spacing = 1.57
    normal.paragraph_format.space_after = Pt(3.5)
    normal.paragraph_format.first_line_indent = Inches(0.21)

    title_style = styles["Title"]
    set_font(title_style, 20, bold=True)
    title_style.paragraph_format.space_before = Pt(14)
    title_style.paragraph_format.space_after = Pt(5)
    title_style.paragraph_format.keep_with_next = True
    # Word's built-in Title style may carry an inherited blue bottom rule.
    title_ppr = title_style.element.get_or_add_pPr()
    for border in list(title_ppr.findall(qn("w:pBdr"))):
        title_ppr.remove(border)

    heading_style = styles["Heading 1"]
    set_font(heading_style, 12, bold=False)
    heading_style.paragraph_format.space_before = Pt(20)
    heading_style.paragraph_format.space_after = Pt(16)
    heading_style.paragraph_format.keep_with_next = True

    subheading_style = styles["Heading 2"]
    set_font(subheading_style, 11, bold=True)
    subheading_style.paragraph_format.space_before = Pt(14)
    subheading_style.paragraph_format.space_after = Pt(8)
    subheading_style.paragraph_format.keep_with_next = True

    foot = section.footer.paragraphs[0]
    foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    foot.style = styles["Normal"]
    foot.paragraph_format.first_line_indent = 0
    foot.paragraph_format.space_after = 0
    foot.paragraph_format.line_spacing = 1
    for run in foot.runs:
        run.font.size = Pt(8)
    add_page_number(foot)

    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    idx = 0
    while idx < len(lines):
        value = lines[idx].strip()
        idx += 1
        if not value:
            continue
        if value.startswith("|") and value.endswith("|"):
            table_lines = [value]
            while idx < len(lines) and lines[idx].strip().startswith("|"):
                table_lines.append(lines[idx].strip())
                idx += 1
            add_table(doc, table_lines)
            continue
        if value.startswith("# "):
            p = doc.add_paragraph(value[2:], style="Title")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.first_line_indent = 0
        elif value.startswith("## "):
            p = doc.add_paragraph(value[3:], style="Heading 1")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.first_line_indent = 0
            if value[3:] == "부록":
                p.paragraph_format.page_break_before = True
        elif value.startswith("### "):
            p = doc.add_paragraph(value[4:], style="Heading 2")
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.first_line_indent = 0
        elif value == "＊":
            p = doc.add_paragraph("＊")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(12)
            p.paragraph_format.first_line_indent = 0
            p.paragraph_format.keep_together = True
        else:
            p = doc.add_paragraph(value)
            p.paragraph_format.widow_control = True

    doc.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
