from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    if text_node.textType not in TextType:
        raise ValueError('Not a valid Text Type')
    if text_node.textType == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.textType == TextType.BOLD:
        return LeafNode('b', text_node.text)
    if text_node.textType == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    if text_node.textType == TextType.CODE:
        return LeafNode('code', text_node.text)
    if text_node.textType == TextType.LINK:
        return LeafNode('a', text_node.text, {'href': text_node.url})
    if text_node.textType == TextType.IMAGE:
        return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
    return 'AHHHHH'
