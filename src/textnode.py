from dataclasses import dataclass
from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALLIC = "itallic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

@dataclass
class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

        if self.text_type in (TextType.LINK, TextType.IMAGE):
            if not url:
                raise AttributeError("LINK and IMAGE nodes must have a url, but one was not provided.")
            
    def to_html_node(self):
        match self.text_type:
            case TextType.PLAIN:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALLIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINK:
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGE:
                return LeafNode("img", None, {"src": self.url, "alt": self.text})
            case _:
                raise Exception(f"Unable to convert TextNode.")

    def __eq__(self, object):
        if not isinstance(object, self.__class__):
            return False
        
        return (
            self.text == object.text
            and self.text_type == object.text_type
            and self.url == object.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

