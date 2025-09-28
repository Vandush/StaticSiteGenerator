from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNodes = []
    for node in old_nodes:
        if node.textType == TextType.TEXT: # or node.textType == TextType.BOLD or node.textType == TextType.ITALIC:
            string = node.text
            esc = re.escape(delimiter) # This let's special characters like '**' work.
            matchs = re.findall(rf"{esc}(.*?){esc}", node.text)
            stringSplit = []
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
