from dataclasses import dataclass
from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain text"
    BOLD_TEXT = "bold"
    ITALLIC_TEXT = "itallic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

@dataclass
class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str):
        self.text = text
        self.text_type = text_type
        self.url = url

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
