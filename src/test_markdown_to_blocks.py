import unittest
from markdown_to_blocks import (
    BlockType,
    markdown_to_blocks,
    block_to_blocktype,
)

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_block_split(self):
        text = '''# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item



    This is a line with whitespace at the front
    '''
        blocks = markdown_to_blocks(text)
        expected = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
            '- This is the first list item in a list block\n- This is a list item\n- This is another list item',
            'This is a line with whitespace at the front',
        ]
        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_blocks_to_blocktypes(self):
        md = '''
#### Heading

####### Technically not a heading

```
Code block
```

- unordered list
- second
- third

> quote
>second quote with no starting space

1. ordered list
2. second
3. third
        '''
        blocks = markdown_to_blocks(md)
        types = []
        for block in blocks:
            x = block_to_blocktype(block)
            types.append(x.value)
        expected = ['heading', 'paragraph', 'code', 'unordered_list', 'quote', 'ordered_list']
        self.assertEqual(types, expected)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)
