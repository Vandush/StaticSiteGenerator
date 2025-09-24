from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

from textnode_to_htmlnode import text_node_to_html_node

def main():

    '''
    node = TextNode('This is some anchor text', 'image', 'https://www.boot.dev')
    print(node.__repr__())
    x = text_node_to_html_node(node)
    print(x)
    print(x.to_html())
    '''
    '''
    grandchildren = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            ParentNode("div", grandchildren, {"href": "https://www.google.com"}),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())
    '''
    #node = LeafNode("p", "This is a paragraph of text.")
    #print(node.to_html())

    #node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    #print(node.to_html())
    #print(node.__repr__())
    
    #props = {
    #"href": "https://www.google.com",
    #"target": "_blank",
    #}
    #node = HTMLNode('This is a tag', 'This is a value', None, props)
    #print(node.props_to_html())
    #print(node.__repr__())
    
    #node = TextNode('This is some anchor text', TextType.TEXT, 'https://www.boot.dev')
    #print(node)

main()
