#!/usr/bin/env python3
"""
Markdown to Typst converter for goodWritter
Usage: python3 md_to_typst.py <input.md> [output.typ]
"""

import sys
import re
from pathlib import Path

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

def extract_signature(content):
    """Extract signature div from markdown content"""
    pattern = r'<div class="signature">.*?</div>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Extract name and date from the div
        div_content = match.group(0)
        # Remove HTML tags
        div_content = re.sub(r'<[^>]+>', '', div_content)
        # Split by newlines
        lines = [line.strip() for line in div_content.split('\n') if line.strip()]
        if len(lines) >= 2:
            name = lines[0]
            date = lines[1]
            # Remove the div from content
            content = content[:match.start()] + content[match.end():]
            return content, name, date
    return content, None, None

def md_to_typst(md_content):
    """Convert markdown to Typst format"""
    # Remove HTML tags (except signature which is already extracted)
    md_content = re.sub(r'<[^>]+>', '', md_content)

    # Convert headers
    md_content = re.sub(r'^# (.+)$', r'= \1', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^## (.+)$', r'== \1', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^### (.+)$', r'=== \1', md_content, flags=re.MULTILINE)

    # Convert bold
    md_content = re.sub(r'\*\*(.+?)\*\*', r'*\1*', md_content)

    # Convert italic
    md_content = re.sub(r'\*(.+?)\*', r'_\1_', md_content)

    # Convert tables
    def convert_table(match):
        lines = match.group(0).strip().split('\n')
        if len(lines) < 2:
            return match.group(0)

        # Parse header
        header = [cell.strip() for cell in lines[0].split('|')[1:-1]]

        # Skip separator line
        rows = []
        for line in lines[2:]:
            if line.strip():
                row = [cell.strip() for cell in line.split('|')[1:-1]]
                rows.append(row)

        # Build Typst table
        typst_table = '#table(\n'
        typst_table += f'  columns: ({", ".join(["1fr"] * len(header))}),\n'
        typst_table += '  table.header(\n'
        typst_table += '    ' + ', '.join([f'[{h}]' for h in header]) + ',\n'
        typst_table += '  ),\n'
        for row in rows:
            typst_table += '  ' + ', '.join([f'[{cell}]' for cell in row]) + ',\n'
        typst_table += ')'

        return typst_table

    # Match markdown tables
    table_pattern = r'(\|.+\|\n\|[-| ]+\|\n(?:\|.+\|\n?)*)'
    md_content = re.sub(table_pattern, convert_table, md_content)

    # Convert lists
    md_content = re.sub(r'^- (.+)$', r'- \1', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^\d+\. (.+)$', r'+ \1', md_content, flags=re.MULTILINE)

    # Convert horizontal rules
    md_content = re.sub(r'^---+$', '', md_content, flags=re.MULTILINE)

    # Convert paragraphs (add blank lines between paragraphs)
    md_content = re.sub(r'\n\n+', '\n\n', md_content)

    return md_content

def generate_typst(md_file, output_file=None):
    """Generate Typst from markdown file"""
    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract metadata
    metadata, content = extract_metadata(content)

    # Extract signature before converting to Typst
    content, signature_name, signature_date = extract_signature(content)

    # Convert markdown to Typst
    typst_content = md_to_typst(content)

    # Add template import
    typst_content = '#import "../scripts/template.typ": *\n\n' + typst_content

    # Add signature if found
    if signature_name and signature_date:
        typst_content += f'\n\n#signature("{signature_name}", "{signature_date}")'

    # Generate output file
    if output_file is None:
        output_file = md_file.with_suffix('.typ')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(typst_content)

    print(f"Typst generated: {output_file}")
    return output_file

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        print("Usage: python3 md_to_typst.py <input.md> [output.typ]")
        print("\nConvert Markdown files to Typst format.")
        print("\nArguments:")
        print("  input.md    Path to the Markdown file to convert")
        print("  output.typ  Path for the output Typst file (optional)")
        sys.exit(0)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not input_file.exists():
        print(f"Error: File {input_file} not found")
        sys.exit(1)

    generate_typst(input_file, output_file)
