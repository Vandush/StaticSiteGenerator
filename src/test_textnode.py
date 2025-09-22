import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_None(self):
        node = TextNode('This is a text node', TextType.TEXT)
        expected = 'TextNode(This is a text node, text, None)'
        self.assertEqual(node.__repr__(), expected)

    def test_Not_eq(self):
        node = TextNode('This is a link', TextType.LINK, 'https://www.boot.dev')
        node2 = TextNode('This is a link', TextType.TEXT, 'https://www.boot.dev')
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
