from dataclasses import dataclass
from enum import Enum

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
