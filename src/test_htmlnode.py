import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.tag, node2.tag)

    def test_neq(self) -> None:
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("div", "This is a div")
        self.assertNotEqual(node.tag, node2.tag)

    def test_none(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertIsNone(node.props)

    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            props={
                "class": "text",
                "href": "https://www.example.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="text" href="https://www.example.com" target="_blank"',
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
