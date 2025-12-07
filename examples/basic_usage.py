#!/usr/bin/env python3
"""
Basic usage example for telegraph-api

This example demonstrates how to:
1. Create a Telegraph account
2. Create a page with HTML content
3. Create a page with Markdown content
4. Edit a page
5. Get page information
6. Get page views
"""

from telegraph import Telegraph

def main():
    # Create a Telegraph client
    tg = Telegraph()

    print("Creating Telegraph account...")
    account = tg.create_account(
        short_name="PythonBot",
        author_name="Python Developer",
        author_url="https://github.com"
    )
    print(f"Account created! Access token: {account.access_token[:20]}...")

    # Create a page with HTML content
    print("\nCreating page with HTML content...")
    html_page = tg.create_page(
        title="HTML Example",
        content="""
        <h3>Welcome to Telegraph API</h3>
        <p>This is a <b>bold</b> statement and this is <i>italic</i> text.</p>
        <blockquote>This is a quote from someone famous.</blockquote>
        <ul>
            <li>First item</li>
            <li>Second item</li>
            <li>Third item</li>
        </ul>
        <p>Visit <a href="https://telegra.ph">Telegraph</a> for more information.</p>
        """,
        author_name="Python Developer"
    )
    print(f"Page created: {html_page.url}")
    print(f"Views: {html_page.views}")

    # Create a page with Markdown content
    print("\nCreating page with Markdown content...")
    markdown_page = tg.create_page(
        title="Markdown Example",
        content="""
# Welcome to Telegraph

This is a page created with **Markdown**!

## Features

- Easy to write
- Clean syntax
- *Beautiful* formatting

### Code Example

`inline code` and code blocks:

```
def hello():
    print("Hello, Telegraph!")
```

[Click here](https://telegra.ph) to visit Telegraph.
        """,
        content_format="markdown",
        author_name="Python Developer"
    )
    print(f"Page created: {markdown_page.url}")

    # Edit the page
    print("\nEditing the HTML page...")
    edited_page = tg.edit_page(
        path=html_page.path,
        title="Updated HTML Example",
        content="<h3>This page has been updated!</h3><p>New content here.</p>"
    )
    print(f"Page updated: {edited_page.url}")

    # Get page information
    print("\nGetting page information...")
    page_info = tg.get_page(
        path=html_page.path,
        return_content=True
    )
    print(f"Title: {page_info.title}")
    print(f"Description: {page_info.description}")
    print(f"Views: {page_info.views}")
    print(f"Can edit: {page_info.can_edit}")

    # Get page list
    print("\nGetting page list...")
    page_list = tg.get_page_list(offset=0, limit=10)
    print(f"Total pages: {page_list.total_count}")
    for i, page in enumerate(page_list.pages, 1):
        print(f"{i}. {page.title} - {page.url}")

    # Get page views
    print("\nGetting page views...")
    views = tg.get_views(path=html_page.path)
    print(f"Total views for '{html_page.title}': {views.views}")

    print("\nDone! All examples completed successfully.")
    print(f"\nYour access token: {account.access_token}")
    print("Save this token to reuse your account later!")

if __name__ == "__main__":
    main()
