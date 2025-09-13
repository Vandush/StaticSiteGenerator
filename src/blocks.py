from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def markdown_to_blocks(markdown):
    splitStrings = []
    tmp = markdown.split("\n\n")
    for i in tmp:
        line = i.strip()
        if line != '':
            splitStrings.append(line)
    return splitStrings

def block_to_block_type(block):
    headers = ('# ', '## ', '### ', '#### ', '##### ', '###### ')
    if block.startswith(headers):
        return BlockType.HEADING
    elif block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    elif block.startswith('>'):
        tmp = block.split('\n')
        for i in tmp:
            if i.startswith('>') != True:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith('- '):
        tmp = block.split('\n')
        for i in tmp:
            if i.startswith('- ') != True:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith('1. '):
        tmp = block.split('\n')
        x = 1
        for i in tmp:
            if i.startswith(f'{x}. ') != True:
                return BlockType.PARAGRAPH
            x += 1
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
