from dataclasses import dataclass
from typing import List, Dict, Optional

from htmlnode import HTMLNode

@dataclass
class LeafNode(HTMLNode):
    def __init__(self, tag: Optional[str], value: str, properties: Dict[str,str] = None):
        self.tag = tag
        self.value = value
        self.properties = properties

        # TODO: Need to call parent constructor
        #super().__init__()

    def to_html(self):
        if not self.value:
            raise ValueError('Leaf nodes must have a value')        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag: {self.tag}, value: {self.value}, properties: {self.properties})"