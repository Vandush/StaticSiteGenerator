import unittest
from textnode_to_htmlnode import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode('This is some anchor text', 'text', 'https://www.boot.dev')
        x = text_node_to_html_node(node)
        expected = 'This is some anchor text'
        self.assertEqual(x.to_html(), expected)

    def test_bold(self):
        node = TextNode('This is some anchor text', 'bold', 'https://www.boot.dev')
        x = text_node_to_html_node(node)
        expected = '<b>This is some anchor text</b>'
        self.assertEqual(x.to_html(), expected)

    def test_link(self):
        node = TextNode('This is some anchor text', 'link', 'https://www.boot.dev')
        x = text_node_to_html_node(node)
        expected = '<a href="https://www.boot.dev">This is some anchor text</a>'
        self.assertEqual(x.to_html(), expected)

    def test_image(self):
        node = TextNode('This is some anchor text', 'image', 'https://www.boot.dev')
        x = text_node_to_html_node(node)
        expected = '<img src="https://www.boot.dev" alt="This is some anchor text"></img>'
        self.assertEqual(x.to_html(), expected)

    def boots_test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def boots_test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def boot_test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

