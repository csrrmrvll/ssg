import unittest
from htmlnode import HTMLNode


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
            "p", "This is a paragraph",
            props={
                "class": "text",
                "href": "https://www.example.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(),
            'class="text" href="https://www.example.com" target="_blank"',
        )
