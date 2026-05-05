#!/usr/bin/env python3
"""
Markdown to PDF converter using Typst for goodWritter
Usage: python3 md_to_pdf_typst.py <input.md> [output.pdf]
"""

import sys
import subprocess
from pathlib import Path

def generate_pdf(md_file, output_file=None):
    """Generate PDF from markdown file using Typst"""
    # Convert markdown to Typst
    from md_to_typst import generate_typst
    typst_file = generate_typst(md_file)

    # Generate PDF using Typst
    if output_file is None:
        output_file = md_file.with_suffix('.pdf')

    # Get project root
    project_root = Path(__file__).parent.parent

    # Run Typst compile
    cmd = [
        'typst', 'compile',
        '--root', str(project_root),
        str(typst_file),
        str(output_file)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error generating PDF: {result.stderr}")
        sys.exit(1)

    print(f"PDF generated: {output_file}")

    # Clean up temporary Typst file
    typst_file.unlink()

    return output_file

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        print("Usage: python3 md_to_pdf_typst.py <input.md> [output.pdf]")
        print("\nConvert Markdown files to PDF using Typst.")
        print("\nArguments:")
        print("  input.md    Path to the Markdown file to convert")
        print("  output.pdf  Path for the output PDF (optional)")
        sys.exit(0)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not input_file.exists():
        print(f"Error: File {input_file} not found")
        sys.exit(1)

    generate_pdf(input_file, output_file)
