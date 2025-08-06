from dataclasses import dataclass
from typing import List, Dict, Optional

from htmlnode import HTMLNode

@dataclass
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List[HTMLNode], properties: Optional[Dict[str, str]]):
        super().__init__(tag, None, children, properties)

    def to_html(self):
        if not self.tag:
            raise ValueError("ERROR: ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ERROR: ParentNode must have at least one child node.")
        
        output = f'<{self.tag}{self.props_to_html(self.properties)}>'
        
        for child in self.children:
            output += child.to_html()
        
        output += f'<{self.tag}>'