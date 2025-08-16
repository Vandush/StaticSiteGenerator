from textnode import *
from htmlnode import *

def main():
    testNode = TextNode('have some text', TextType.IMAGE, 'def not the hub.com')
    print(testNode)
    '''
    node = LeafNode("p", "Hello, world!")
    print(node.to_html())
    #"<p>Hello, world!</p>")
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node.__repr__())
    print(node.to_html())
    #'<a href="https://www.google.com">Click me!</a>')
    '''
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

main()

