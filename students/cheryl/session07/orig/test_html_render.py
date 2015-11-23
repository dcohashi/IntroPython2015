#!/usr/bin/env python3

from io import StringIO
import html_render as hr

def test_init():
    assert hr.Element.tag_name == 'html'
    element = hr.Element()
    assert element.tag_name == "html"
    assert element.indent == 4

def test_init2():
    element = hr.Element("this is a string")
    assert "this is a string" in element.content 
    element2 = hr.Element()
    assert None not in element2.content

def test_append():
    element = hr.Element("string1")
    element.append("string2")
    assert "string2" in element.content
    assert "string1" in element.content

def test_render():
    element = hr.Element("string1")
    element.append("string2")
    f = StringIO()
    element.render(f)
    f.seek(0)
    text = f.read()
    assert "string1" in text
    print(text)
    assert text.startswith("<html>")
    assert text.endswith("</html>")

def test_body():
    element = hr.Body("body")
    f = StringIO()
    element.render(f)
    f.seek(0)
    text = f.read()
    assert "body" in text
    assert text.startswith("<body>")
    assert text.endswith("</body>")

def test_paragraph():
    element = hr.P("paragraph")
    f = StringIO()
    element.render(f)
    f.seek(0)
    text = f.read()
    assert "paragraph" in text
    assert text.startswith("<p>")
    assert text.endswith("</p>")

def test_nest_render():
    e = hr.Element()
    p = hr.P("paragraph")
    e.append(p)
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read()
    assert "paragraph" in text
    assert text.startswith("<html>")
    assert text.endswith("</html>")
    print(text)
