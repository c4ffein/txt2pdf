# txt2pdf : Convert Markdown files to PDF with styles.

Initially forked from https://github.com/jmaupetit/md2pdf

<p align="center">
  <a href="https://pypi.org/project/txt2pdf/" alt="PyPI">
      <img src="https://img.shields.io/pypi/v/txt2pdf?color=blueviolet" /></a>
  <a href="https://pypi.org/project/txt2pdf/" alt="Python Versions">
      <img src="https://img.shields.io/pypi/pyversions/txt2pdf?color=blueviolet" /></a>
  <a href="https://pypi.org/project/txt2pdf/" alt="PyPI Format">
      <img src="https://img.shields.io/pypi/format/txt2pdf?color=blueviolet" /></a>
  <a href="https://pypi.org/project/txt2pdf/" alt="License">
      <img src="https://img.shields.io/pypi/l/txt2pdf?color=blueviolet" /></a>
</p>

## Installation

Available through pip:

```bash
$ pip install txt2pdf
```

## Usage

### As a CLI

```
Usage:
    txt2pdf [options] INPUT.MD OUTPUT.PDF

Options:
    --css=STYLE.CSS
```

For example, try to generate the project documentation with:

```bash
$ txt2pdf README.md README.pdf
```

Optionally, you may load an external style (restricted to CSS2):

```bash
$ txt2pdf --css tests/resources/input.css README.md README.pdf
```

You may also include a HTML header and footer :

```bash
$ txt2pdf --header tests/resources/header.html README.md README.pdf
$ txt2pdf --footer tests/resources/footer.html README.md README.pdf
```

Optional debug by printing HTML to stdout, includes optional header and footer :

```bash
$ txt2pdf --html-to-stdout README.md README.pdf
```

### As a library

```python
from txt2pdf.core import txt2pdf

txt2pdf(
    pdf_file_path,
    md_content=None,
    md_file_path=None,
    css_file_path=None,
    html_header_content=None,
    html_header_file_path=None,
    html_footer_content=None,
    html_footer_file_path=None,
    base_url=None,
    print_html_to_stdout=False,
)
```

Function arguments:

* `pdf_file_path`: output PDF file path
* `md_content`: input markdown raw string content
* `md_file_path`: input markdown file path
* `css_file_path`: input styles path (CSS)
* `html_header_content`: input HTML header raw string content
* `html_header_file_path`: input HTML header file path
* `html_footer_content`: input HTML footer raw string content
* `html_footer_file_path`: input HTML footer file path
* `base_url`: absolute base path for markdown linked content (as images)
* `print_html_to_stdout`: print HTML to stdout for debug purposes

### With Docker

Install [Docker](https://www.docker.com/)

Build the image:

```bash
$ docker build -t txt2pdf .
```

Now run your image:

```bash
$ docker run --rm -v $PWD:/app txt2pdf --css styles.css INPUT.MD OUTPUT.PDF
```

## Troubleshooting on MacOSX

Ensure, Weasyprint is fully functional before using txt2pdf. You will find
installation instructions in the project documentation:
[https://weasyprint.readthedocs.io/en/latest/install.html](https://weasyprint.readthedocs.io/en/latest/install.html#macos)

In a few words, here are the few steps you will need to follow:

* Install XQuartz from:
  [https://xquartz.macosforge.org](https://xquartz.macosforge.org)
* Install all dependencies at once with
  [homebrew](http://mxcl.github.io/homebrew/) and go grab a coffee (this may
  take a while):

```bash
$ brew install cairo pango gdk-pixbuf libxml2 libxslt libffi
```

## Misc

### Using custom fonts in styles

WeasyPrint does not support the `@font-face` property yet (see [project issue
28](https://github.com/Kozea/WeasyPrint/issues/28)). If you use want to use
custom fonts, you should use system fonts and define them with the `font-family`
CSS property, like:

```
font-family: 'Neutraface Condensed';
```

Note that you should only define **one single** custom font, not a substitution list.

### Using code blocks
Generate default css defining a class for every code item type:

```bash
(venv) $ pygmentize -S default -f html -a .codehilite
```

## Contributing

### Hacking

Clone this project first:

```bash
$ git clone git@github.com:c4ffein/txt2pdf.git
```

Install it with its dependencies (ideally in a virtual environment):

```bash
$ cd txt2pdf
$ python -m venv venv
$ . venv/bin/activate
(venv) $ pip install .[dev]
```

### Running the test suite

To run the test suite with your active python version (virtual environment):

```bash
(venv) $ pytest
```

Lint the code via:

```bash
(venv) $ black -l 120
```

### Release a new version

```
(venv) $ pip install .[deploy]  # install flit if needed
(venv) $ flit publish --format sdist
```

## License

`txt2pdf` is released under the MIT License. See the LICENSE file for details.
