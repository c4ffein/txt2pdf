#!/usr/bin/env python

"""txt2pdf - Markdown to PDF conversion tool.

Usage: txt2pdf [options] INPUT.MD OUTPUT.PDF

Options:
    --css=STYLE.CSS
    --header=HEADER.HTML
    --footer=FOOTER.HTML
    --html-to-stdout
"""
import os
import sys
import argparse

from txt2pdf import __version__
from txt2pdf.core import txt2pdf


def main(argv=None):

    # Parse command line arguments
    parser = argparse.ArgumentParser(description=f"txt2pdf {__version__}\n{__doc__}")
    parser.add_argument("md_file_path", metavar="INPUT.MD")
    parser.add_argument("pdf_file_path", metavar="OUTPUT.MD")
    parser.add_argument("--css", metavar="css_file_path", dest="css_file_path", help="path to the CSS")
    parser.add_argument("--header", metavar="header_file_path", dest="header_file_path", help="path to the header")
    parser.add_argument("--footer", metavar="footer_file_path", dest="footer_file_path", help="path to the footer")
    parser.add_argument(
        "--html-to-stdout", dest="print_html_to_stdout", help="don't print by default", action="store_true"
    )
    args = parser.parse_args()
    base_url = os.getcwd()

    txt2pdf(
        args.pdf_file_path,
        md_file_path=args.md_file_path,
        css_file_path=args.css_file_path,
        header_file_path=args.header_file_path,
        footer_file_path=args.footer_file_path,
        print_html_to_stdout=args.print_html_to_stdout,
        base_url=base_url,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
