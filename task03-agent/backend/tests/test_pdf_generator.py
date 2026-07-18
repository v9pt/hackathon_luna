import base64
from app.utils.pdf_generator import generate_pdf, md_to_html


def test_md_to_html_formatting() -> None:
    text = "This is **bold** and *italic* and `code`."
    html_out = md_to_html(text)
    assert "<b>bold</b>" in html_out
    assert "<i>italic</i>" in html_out
    assert '<font face="Courier"' in html_out
    assert "code" in html_out


def test_generate_pdf_basic() -> None:
    markdown = """# Wearable Tech Competitors Report
## Executive Summary
This is a summary paragraph.
- Bullet point 1
- Bullet point 2
1. Numbered item 1
2. Numbered item 2
```python
print("Hello World")
```
"""
    pdf_bytes = generate_pdf(markdown)
    assert isinstance(pdf_bytes, bytes)
    assert len(pdf_bytes) > 0
    # PDF files start with the magic header %PDF-
    assert pdf_bytes.startswith(b"%PDF-")


def test_generate_pdf_with_charts() -> None:
    # A tiny 1x1 black pixel PNG image in base64
    base64_pixel = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk"
        "YAAAAAYAAjCB0C8AAAAASUVORK5CYII="
    )
    
    # 1. Test using charts parameter
    charts = [{"name": "test_chart.png", "base64": base64_pixel}]
    markdown = "# Report with Charts\nThis is a report."
    pdf_bytes = generate_pdf(markdown, charts=charts)
    assert isinstance(pdf_bytes, bytes)
    assert pdf_bytes.startswith(b"%PDF-")

    # 2. Test using inline markdown base64 images
    markdown_inline = f"""# Inline Chart Report
Here is the chart:
![Inline Chart](data:image/png;base64,{base64_pixel})
"""
    pdf_bytes_inline = generate_pdf(markdown_inline)
    assert isinstance(pdf_bytes_inline, bytes)
    assert pdf_bytes_inline.startswith(b"%PDF-")
