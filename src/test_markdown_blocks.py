from unittest import main, TestCase
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToHTML(TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_block_to_block_type(self):
        self.assertEqual(
            block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH
        )
        self.assertEqual(
            block_to_block_type("# This is a heading\n"), BlockType.HEADING
        )
        self.assertEqual(block_to_block_type("```\nThis is code\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(">This is also a quote"), BlockType.QUOTE)
        self.assertEqual(
            block_to_block_type("- This is an unordered list item"),
            BlockType.ULIST,
        )
        self.assertEqual(
            block_to_block_type("1. This is an ordered list item"),
            BlockType.OLIST,
        )


if __name__ == "__main__":
    main()
