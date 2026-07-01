from unittest import main, TestCase
from generate_page import extract_title


class TestGeneratePage(TestCase):
    def test_extract_title(self):
        markdown = """
# This is the title
"""
        title = extract_title(markdown)
        self.assertEqual(title, "This is the title")

    def test_extract_title_with_whitespace(self):
        markdown = """
#    This is the title with whitespace
"""
        title = extract_title(markdown)
        self.assertEqual(title, "This is the title with whitespace")

    def test_extract_title_with_no_title(self):
        markdown = """
This is a paragraph without a title.
"""
        title = extract_title(markdown)
        self.assertEqual(title, "")

    def test_extract_title_with_headings(self):
        markdown = """
# First Title
# Second Title

## First Subtitle

### First Sub-subtitle
"""
        title = extract_title(markdown)
        self.assertEqual(title, "First Title")

if __name__ == "__main__":
    main()
