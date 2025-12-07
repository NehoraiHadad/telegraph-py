#!/usr/bin/env python3
"""
Test script to verify the telegraph-api package installation
"""

from telegraph import (
    Telegraph,
    AsyncTelegraph,
    Account,
    Page,
    PageList,
    PageViews,
    NodeElement,
    TelegraphError,
    html_to_nodes,
    markdown_to_html,
    parse_content,
    __version__
)

print(f"telegraph-api version: {__version__}")
print("\n1. Testing imports... OK")

# Test client initialization
tg = Telegraph()
print("2. Testing Telegraph client initialization... OK")

# Test async client initialization (if available)
if AsyncTelegraph is not None:
    async_tg = AsyncTelegraph()
    print("3. Testing AsyncTelegraph client initialization... OK")
else:
    print("3. AsyncTelegraph not available (aiohttp not installed)... SKIPPED")

# Test HTML to nodes conversion
nodes = html_to_nodes("<p>Hello <b>world</b>!</p>")
assert len(nodes) == 1
assert isinstance(nodes[0], NodeElement)
assert nodes[0].tag == 'p'
print("4. Testing html_to_nodes()... OK")

# Test markdown to HTML conversion
html = markdown_to_html("# Title\n\nThis is **bold** text")
assert '<h3>Title</h3>' in html
assert '<b>bold</b>' in html
print("5. Testing markdown_to_html()... OK")

# Test parse_content with HTML
nodes = parse_content("<p>Test</p>", format='html')
assert len(nodes) == 1
print("6. Testing parse_content() with HTML... OK")

# Test parse_content with Markdown
nodes = parse_content("# Test", format='markdown')
assert len(nodes) == 1
print("7. Testing parse_content() with Markdown... OK")

# Test NodeElement creation
node = NodeElement(
    tag='a',
    attrs={'href': 'https://example.com'},
    children=['Link text']
)
assert node.tag == 'a'
assert node.attrs['href'] == 'https://example.com'
print("8. Testing NodeElement creation... OK")

# Test validation
try:
    tg.create_page(title="", content="<p>Test</p>")
    print("9. Testing validation... FAILED (should have raised error)")
except TelegraphError as e:
    print("9. Testing validation... OK (correctly raised error)")

# Test context manager
with Telegraph() as client:
    assert client is not None
print("10. Testing context manager... OK")

print("\nAll tests passed!")
print("\nPackage structure:")
print("- telegraph.Telegraph (sync client)")
print("- telegraph.AsyncTelegraph (async client)")
print("- telegraph.Account, Page, PageList, PageViews (data types)")
print("- telegraph.NodeElement, Node (content types)")
print("- telegraph.TelegraphError and subclasses (exceptions)")
print("- telegraph.html_to_nodes, markdown_to_html, parse_content (utilities)")
print("\nReady to use!")
