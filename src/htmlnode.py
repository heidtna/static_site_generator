from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class HTMLNode:
    """
    Represents a 'node' in an HTML document. Can be a block or inline. Will only output HTML
    """
    def __init__(self, 
                 tag: Optional[str] = None, 
                 value: Optional[str] = None, 
                 children: List["HTMLNode"] = None, 
                 properties: Optional[Dict[str, str]] = None):
        """
        Contstructor. All parameters are optional, with the following logic applying:
            1. A node without a 'tag' will render as raw text.
            2. A node without a 'value' will be assumed to have children nodes.
            3. A node without 'children' will be assumed to have a value.
            4. A node without 'props' won't have any attributes.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.properties = properties

    def to_html(self):
        """
        Treated as a virtual method. Specific implementation is left to inheritors. 
        """
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.properties or len(self.properties) < 1:
            return ""
        
        output = ""

        for key, value in self.properties.items():
            # each property begins with a space
            output += f' {key}="{value}"'   

        return output
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, properties: {self.properties})"