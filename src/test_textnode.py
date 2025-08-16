import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        nodeOne = TextNode('This is a test node', TextType.BOLD)
        nodeTwo = TextNode('This is a test node', TextType.BOLD)
        self.assertEqual(nodeOne, nodeTwo)

        nodeThree = TextNode('This is a test node', TextType.ITALIC)
        nodeFour = TextNode('This is a test node', TextType.CODE)
        self.assertNotEqual(nodeThree, nodeFour)

        nodeFive = TextNode('This is a test node', TextType.BOLD, None)
        self.assertEqual(nodeOne, nodeFive)

        nodeSix = TextNode('This could be a test node', TextType.BOLD)
        self.assertNotEqual(nodeFive, nodeSix)

        nodeSeven = TextNode('This is a test node', TextType.BOLD, 'test.com')
        self.assertNotEqual(nodeSeven, nodeOne)

if __name__ == "__main__":
    unittest.main()
