from enum import Enum

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, textType, url=None):
        self.text = text
        self.textType = TextType(textType)
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.textType == other.textType and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.textType.value}, {self.url})'


