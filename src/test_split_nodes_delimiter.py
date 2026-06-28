from unittest import main, TestCase
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(TestCase):
    def test_split_nodes_delimiter_space(self):
        old_nodes = [TextNode("Hello world", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, " ", TextType.TEXT)
        expected_nodes = [
            TextNode("Hello", TextType.TEXT),
            TextNode("world", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_comma(self):
        old_nodes = [TextNode("Hello,world", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, ",", TextType.TEXT)
        expected_nodes = [
            TextNode("Hello", TextType.TEXT),
            TextNode("world", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_unsupported(self):
        old_nodes = [TextNode("Hello world", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "@", TextType.TEXT)

    def test_split_nodes_delimiter_bold(self):
        old_nodes = [
            TextNode(
                "This is text with a **bolded phrase** in the middle", TextType.TEXT
            )
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_italic(self):
        old_nodes = [
            TextNode("This is text with a _italic phrase_ in the middle", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_code(self):
        old_nodes = [
            TextNode("This is text with a `code block` in the middle", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)


if __name__ == "__main__":
    main()
