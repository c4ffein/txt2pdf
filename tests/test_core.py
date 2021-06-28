# -*- coding: utf-8 -*-
import pytest

from os import remove
from os.path import exists

from txt2pdf import txt2pdf
from txt2pdf.exceptions import ValidationError

from .defaults import OUTPUT_PDF


def setup_function(function):
    """Remove temporary PDF files"""

    if exists(OUTPUT_PDF):
        remove(OUTPUT_PDF)


def test_generate_pdf_from_raw_markdown():

    assert not exists(OUTPUT_PDF)

    txt2pdf(OUTPUT_PDF, md_content="# hi there!")
    assert exists(OUTPUT_PDF)


def test_raises_a_validation_error_when_generated_html_is_empty():

    with pytest.raises(ValidationError):
        txt2pdf(OUTPUT_PDF)
