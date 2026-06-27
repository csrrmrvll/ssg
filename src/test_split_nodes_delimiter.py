from unittest import main, TestCase
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(TestCase):
    def test_split_nodes_delimiter_space(self):
        old_nodes = [TextNode("Hello world", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, " ", TextType.TEXT)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[1].text, " ")
        self.assertEqual(new_nodes[2].text, "world")

    def test_split_nodes_delimiter_comma(self):
        old_nodes = [TextNode("Hello,world", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, ",", TextType.TEXT)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[1].text, ",")
        self.assertEqual(new_nodes[2].text, "world")

    def test_split_nodes_delimiter_unsupported(self):
        old_nodes = [TextNode("Hello world", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "@", TextType.TEXT)

    def test_split_nodes_delimiter_bold(self):
        old_nodes = [TextNode("Hello world", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, " ", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, " ")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, "world")
        self.assertEqual(new_nodes[2].text_type, TextType.BOLD)

    def test_split_nodes_delimiter_italic(self):
        old_nodes = [TextNode("Hello world", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, " ", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Hello")
        self.assertEqual(new_nodes[0].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[1].text, " ")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, "world")
        self.assertEqual(new_nodes[2].text_type, TextType.ITALIC)


if __name__ == "__main__":
    main()
