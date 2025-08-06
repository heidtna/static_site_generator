from dataclasses import dataclass
from typing import Dict, Optional

from htmlnode import HTMLNode

@dataclass
class LeafNode(HTMLNode):
    def __init__(self, tag: Optional[str], value: str, properties: Dict[str,str] = None):
        super().__init__(tag, value, None, properties)

    def to_html(self):
        if not self.value:
            raise ValueError('Leaf nodes must have a value')        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, properties: {self.properties})"