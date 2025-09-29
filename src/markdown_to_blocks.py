from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    index = 0
    for i in range(len(blocks)):
        x = i + index
        blocks[x] = blocks[x].strip()
        if blocks[x] == '':
            blocks.pop(x)
            index -= 1
    return blocks

def block_to_blocktype(block):
    headers = ('# ', '## ', '### ', '#### ', '##### ', '###### ')
    if block.startswith(headers):
        return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if block.startswith('>'):
        lines = block.split('\n')
        for line in lines:
            if line.startswith('>') != True:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith('- '):
        lines = block.split('\n')
        for line in lines:
            if line.startswith('-') != True:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith('1. '):
        lines = block.split('\n')
        x = 1
        for line in lines:
            if line.startswith(f'{x}. ') != True:
                return BlockType.PARAGRAPH
            x += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
