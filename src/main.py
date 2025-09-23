from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    node = LeafNode("p", "This is a paragraph of text.")
    print(node.to_html())

    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node.to_html())
    print(node.__repr__())
    
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
