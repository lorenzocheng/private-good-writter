#!/usr/bin/env python3
"""
Markdown to PDF converter for goodWritter
Usage: python3 md_to_pdf.py <input.md> [output.pdf]
"""

import sys
from pathlib import Path
import markdown
from jinja2 import Template
from weasyprint import HTML

def extract_metadata(content):
    """Extract YAML frontmatter from markdown content"""
    metadata = {
        'title': '未命名文档',
        'date': '',
        'author': '毅湃科技',
        'doc_type': '文档'
    }

    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            frontmatter = content[3:end].strip()
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    if key in metadata:
                        metadata[key] = value
            content = content[end+3:].strip()

    return metadata, content

def md_to_html(md_content):
    """Convert markdown to HTML"""
    extensions = [
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ]
    return markdown.markdown(md_content, extensions=extensions)

def generate_pdf(md_file, output_file=None):
    """Generate PDF from markdown file"""
    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract metadata and content
    metadata, md_content = extract_metadata(content)

    # Convert markdown to HTML
    html_content = md_to_html(md_content)

    # Load template
    script_dir = Path(__file__).parent
    template_path = script_dir / 'template.html'
    with open(template_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())

    # Render template
    full_html = template.render(
        title=metadata['title'],
        date=metadata['date'],
        author=metadata['author'],
        doc_type=metadata['doc_type'],
        content=html_content
    )

    # Generate PDF
    if output_file is None:
        output_file = md_file.with_suffix('.pdf')

    html = HTML(string=full_html, base_url=str(script_dir.parent))
    html.write_pdf(output_file)

    print(f"PDF generated: {output_file}")
    return output_file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_pdf.py <input.md> [output.pdf]")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not input_file.exists():
        print(f"Error: File {input_file} not found")
        sys.exit(1)

    generate_pdf(input_file, output_file)
