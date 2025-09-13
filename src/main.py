from textnode import *
from htmlnode import *
from blocks import *

import re

def text_node_to_html_node(text_node):
    if text_node.text_type.value not in TextType:
        raise Exception("big silly brain")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url,})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", '', {"src": text_node.url, "alt": text_node.text})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            newNodes.append(n)
        else:
            tmp = []
            splitString = n.text.split(delimiter)
            if len(splitString) > 2 and len(splitString)%2 != 0:
                formatedText = splitString[1::2]
                plainText = splitString[::2]
                index = 0
                for k in range(len(plainText)):
                    if k == 0:
                        index = 0
                    if k != len(plainText)-1 and plainText[k] != '':
                        tmp.append(TextNode(plainText[k], TextType.TEXT))
                        tmp.append(TextNode(formatedText[index], text_type))
                        index += 1
                    if k != len(plainText)-1 and plainText[k] == '':
                        tmp.append(TextNode(formatedText[index], text_type))
                        index += 1
                    if k == len(plainText)-1 and plainText[k] != '':
                        tmp.append(TextNode(plainText[k], TextType.TEXT))
            elif len(splitString) > 1 and len(splitString)%2 == 0:
                raise Exception("Invalid Markdown syntax OR nested Markdown syntax.")
            else:
                tmp.append(TextNode(splitString[0], TextType.TEXT))
            newNodes.extend(tmp)
    return newNodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    newNodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            newNodes.append(n)
        else:
            text = n.text
            matches = extract_markdown_images(n.text)
            if len(matches) == 0:
                newNodes.append(n)
            else:
                for m in range(len(matches)):
                    match = f'![{matches[m][0]}]({matches[m][1]})'
                    splitString = text.split(match, 1)
                    text = splitString[1]
                    if splitString[0] != '':
                        newNodes.append(TextNode(splitString[0], TextType.TEXT))
                    newNodes.append(TextNode(matches[m][0], TextType.IMAGE, matches[m][1]))
                    if m == len(matches)-1 and text != '':
                        newNodes.append(TextNode(text, TextType.TEXT))
    return newNodes


def split_nodes_link(old_nodes):
    newNodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            newNodes.append(n)
        else:
            text = n.text
            matches = extract_markdown_links(n.text)
            if len(matches) == 0:
                newNodes.append(n)
            else:
                for m in range(len(matches)):
                    match = f'[{matches[m][0]}]({matches[m][1]})'
                    splitString = text.split(match, 1)
                    text = splitString[1]
                    if splitString[0] != '':
                        newNodes.append(TextNode(splitString[0], TextType.TEXT))
                    newNodes.append(TextNode(matches[m][0], TextType.LINK, matches[m][1]))
                    if m == len(matches)-1 and text != '':
                        newNodes.append(TextNode(text, TextType.TEXT))
    return newNodes

def text_to_textnodes(text):
    nodes = []
    for i in TextType:
        if i == TextType.TEXT:
            nodes.append(TextNode(text, i))
        if i == TextType.BOLD:
            nodes = split_nodes_delimiter(nodes, "**", i)
        if i == TextType.ITALIC:
            nodes = split_nodes_delimiter(nodes, "_", i)
        if i == TextType.CODE:
            nodes = split_nodes_delimiter(nodes, "`", i)
        if i == TextType.LINK:
            nodes = split_nodes_link(nodes)
        if i == TextType.IMAGE:
            nodes = split_nodes_image(nodes)
    return nodes

def main():
    md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

    result = markdown_to_blocks(md)
    for i in result:
        x = block_to_block_type(i)
        print(x)

main()
