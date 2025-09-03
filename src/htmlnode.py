class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def prop_to_html(self):
        if self.props == None:  # I didn't think to do these two lines.
            return ''
        string = ''
        for i in self.props:
            string += ' ' + i + '="' + self.props[i] + '"'
        return string

    def __repr__(self):
        inputs = []
        inputs.append(f'TAG: {self.tag}')
        inputs.append(f'VALUE: {self.value}')
        inputs.append(f'CHILDREN: {self.children}')
        inputs.append(f'PROPS: {self.props}')
        return '\n'.join(inputs)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError('All leaf nodes must have a value')
        if self.tag == None:
            return f'{self.value}'
        else:
            return f'<{self.tag}{self.prop_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('Missing tag')
        if self.children == None:
            raise ValueError('Missing children')
        else:
            string = ''
            for i in self.children:
                string += i.to_html()
            return f'<{self.tag}{self.prop_to_html()}>{string}</{self.tag}>'


