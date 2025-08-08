from dataclasses import dataclass
from typing import List, Dict, Optional

from htmlnode import HTMLNode

@dataclass
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List[HTMLNode], properties: Optional[Dict[str, str]] = None):
        super().__init__(tag, None, children, properties)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ERROR: ParentNode must have a tag.")
        if self.children is None:
            raise ValueError("ERROR: ParentNode must have at least one child node.")
        
        childNodes = ""
        for child in self.children:
            childNodes += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{childNodes}</{self.tag}>'