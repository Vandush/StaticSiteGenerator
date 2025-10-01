import re
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

from textnode_to_htmlnode import textNodesToHTMLNodes #text_node_to_html_node
from inline_markdown_to_textnode import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
)
from markdown_to_blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_blocktype,
)
'''
class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'



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
'''
def blockToHtmlNode(block, blockType):
    if blockType not in BlockType:
        raise ValueError('Invalid Block Type')
    if blockType == BlockType.PARAGRAPH:
        nodes = textNodesToHTMLNodes(text_to_textnodes(block))
        return ParentNode('p', nodes)
    if blockType == BlockType.HEADING:
        match = re.findall(r"^#+", block)
        print(len(match[0]))
        pass



def markdown_to_html_node(markdown):
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        blocktype = block_to_blocktype(block)
        node = blockToHtmlNode(block, blocktype)
        print(node.__repr__())
    return nodes
