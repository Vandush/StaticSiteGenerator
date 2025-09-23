import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = HTMLNode('This is a tag', 'This is a value', None, props)
        expected = '''HTMLNode(tag="This is a tag", value="This is a value", children=None, props={'href': 'https://www.google.com', 'target': '_blank'})'''
        self.assertEqual(node.__repr__(), expected)


        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            '''HTMLNode(tag="p", value="What a strange world", children=None, props={'class': 'primary'})''',
        )


    def test_props_to_html(self):
        props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = HTMLNode('This is a tag', 'This is a value', None, props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_LeafNode(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = '''<p>This is a paragraph of text.</p>'''
        self.assertEqual(node.to_html(), expected)

        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '''<a href="https://www.google.com">Click me!</a>'''
        self.assertEqual(node.to_html(), expected)

        expected = '''HTMLNode(tag="a", value="Click me!", children=None, props={'href': 'https://www.google.com'})'''
        self.assertEqual(node.__repr__(), expected)


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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
