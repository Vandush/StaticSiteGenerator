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
from markdown_to_htmlnode import markdown_to_html_node

md = """
#### This is a Header

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

def main():
    print(markdown_to_html_node(md))
    
#    md = '''
#### Heading

####### Technically not a heading

#        ```
#Code block
#        ```

#- unordered list
#- second
#- third

#> quote
#>second quote with no starting space

#1. ordered list
#2. second
#3. third
#    '''    
#    blocks = markdown_to_blocks(md)
#    types = []
#    print(blocks)
#    for block in blocks:
#        x = block_to_blocktype(block)
#        types.append(x.value)
#    print(types)

    '''
    text = "This is a string with **bold characters**, and _italic characters_, as well as `hacker code`, a link [to boot dev](https://www.boot.dev) and an image of and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    nodes = text_to_textnodes(text)
    for node in nodes:
        print(node)
    '''
    '''
    text = 'This is text without any links or images.'
    #text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #print(extract_markdown_images(text))
    #print(extract_markdown_links(text))
    node = TextNode(text, 'text')
    nodes = [node]
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    for node in nodes:
        print(node)
    '''
    '''
    node = TextNode("This is a node with **bold** and _itlaic_ and `code`.", 'text')
    nodes = [node]
    delimiters = {
        '_': 'italic',
        '`': 'code',
        '**': 'bold',
    }
    for delimiter in delimiters:
        text_type = delimiters[delimiter]
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)
    for i in nodes:
        print(i)
    '''
    '''
    nodeOne = TextNode("`This` is text with a `code block` and another `second code block`.", TextType.TEXT)
    nodeTwo = TextNode("Second ndoe with a single `code block`", 'text')
    nodeThree = TextNode("Third without any code block", 'text')
    new_nodes = split_nodes_delimiter([nodeOne, nodeTwo, nodeThree], "`", TextType.CODE)
    print(new_nodes)
    '''
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
