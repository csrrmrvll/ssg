from unittest import main, TestCase

from split_nodes_items import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodesItems(TestCase):
    def test_split_image_at_the_beginning(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) is at the beginning",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" is at the beginning", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_in_the_middle(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) in the middle",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_at_the_end(self):
        node = TextNode(
            "This is a text and at the end there is an ![image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text and at the end there is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_images_at_the_beginning_and_end(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) is at the beginning and at the end another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" is at the beginning and at the end another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_in_the_middle(self):
        node = TextNode(
            "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another"
            " ![second image](https://i.imgur.com/3elNhQu.png) in the middle",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_in_the_middle_and_at_the_end(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            " and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_at_the_beginning_and_in_the_middle(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) at the beginning"
            "  and ![second image](https://i.imgur.com/3elNhQu.png) in the middle",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" at the beginning  and ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_at_the_beginning(self):
        node = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png) is at the beginning",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" is at the beginning", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_in_the_middle(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) in the middle",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_at_the_end(self):
        node = TextNode(
            "This is a text and at the end there is a [link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text and at the end there is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links_at_the_beginning_and_end(self):
        node = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png) is at the beginning and at the end another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" is at the beginning and at the end another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_in_the_middle(self):
        node = TextNode(
            "This is a text with a [link](https://i.imgur.com/zjjcJKZ.png) and another"
            " [second link](https://i.imgur.com/3elNhQu.png) in the middle",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" in the middle", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_in_the_middle_and_at_the_end(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
            " and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_at_the_beginning_and_in_the_middle(self):
        node = TextNode(
            "[link](https://i.imgur.com/zjjcJKZ.png) at the beginning"
            "  and [second link](https://i.imgur.com/3elNhQu.png) in the middle",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" at the beginning  and ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" in the middle", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    main()
