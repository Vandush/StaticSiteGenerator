import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test(self):
        lst = []
        tag = 'This is a tag'
        lst.append(f'TAG: {tag}')
        value = 'This is a value'
        lst.append(f'VALUE: {value}')
        children = [
            'childrenOne',
            'childrenTwo'
        ]
        lst.append(f'CHILDREN: {children}')
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        lst.append(f'PROPS: {props}')
        
        expectedOne = ' href="https://www.google.com" target="_blank"'
        expectedTwo = '\n'.join(lst)

        nodeOne = HTMLNode(tag, value, children, props)
        nodeTwo = HTMLNode()

        self.assertEqual(nodeOne.prop_to_html(), expectedOne)
        self.assertEqual(nodeOne.__repr__(), expectedTwo)
        self.assertNotEqual(nodeOne.__repr__(), nodeTwo.__repr__())


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

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

