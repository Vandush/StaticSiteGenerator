from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNodes = []
    for node in old_nodes:
        if node.textType == TextType.TEXT: # or node.textType == TextType.BOLD or node.textType == TextType.ITALIC:
            string = node.text
            esc = re.escape(delimiter) # This let's special characters like '**' work.
            matchs = re.findall(rf"{esc}(.*?){esc}", node.text)
            #stringSplit = []
            for match in matchs:
                tmp = string.split(f'{delimiter}{match}{delimiter}', 1)
                if tmp[0] != '':
                    newNodes.append(TextNode(tmp[0], 'text'))
                newNodes.append(TextNode(match, text_type))
                string = tmp[1]
            if string != '':
                newNodes.append(TextNode(string, 'text'))
        else:
            newNodes.append(node)
    return newNodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    newNodes = []
    for node in old_nodes:
        if node.textType == TextType.TEXT:
            string = node.text
            matchs = extract_markdown_images(string)
            x = 1
            for match in matchs:
                tmp = string.split(f'![{match[0]}]({match[1]})')
                if tmp[0] != '':
                    newNodes.append(TextNode(tmp[0], 'text'))
                newNodes.append(TextNode(match[0], 'image', match[1]))
                string = tmp[1]
            if string != '':
                newNodes.append(TextNode(string, 'text'))
        else:
            newNodes.append(node)
    return newNodes

def split_nodes_link(old_nodes):
    newNodes = []
    for node in old_nodes:
        if node.textType == TextType.TEXT:
            string = node.text
            matchs = extract_markdown_links(string)
            x = 1
            for match in matchs:
                tmp = string.split(f'[{match[0]}]({match[1]})')
                if tmp[0] != '':
                    newNodes.append(TextNode(tmp[0], 'text'))
                newNodes.append(TextNode(match[0], 'link', match[1]))
                string = tmp[1]
            if string != '':
                newNodes.append(TextNode(string, 'text'))
        else:
            newNodes.append(node)
    return newNodes

def text_to_textnodes(text):
    node = TextNode(text, 'text')
    nodes = [node]
    delimiters = {
            '_': 'italic',
            '`': 'code',
            '**': 'bold',
        }
    for delimiter in delimiters:
        text_type = delimiters[delimiter]
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
