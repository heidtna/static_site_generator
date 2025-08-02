import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_constructor(self):
        # Arrage
        # Act
        node = HTMLNode("p", "some paragraph text")
        
        # Assert
        self.assertIn("TAG: p", str(node), f'ERROR: Unable to find tag "{node.tag}" in node "{str(node)}"')
        self.assertIn("some paragraph text", str(node), f'ERROR: Unexpected node parameters: {str(node)}')

    def test_htmlnode_properties(self):
        # Arrange
        prop_key = "class"
        prop_value = "link-query"

        # Act
        node = HTMLNode(tag="a", properties={prop_key: prop_value, "title": "retrieve options"})
        
        # Assert
        self.assertIn("class", str(node), f'ERROR: Property key "{prop_key}" in node properties "{str(node.properties)}"')
        self.assertIn("options", str(node), f'ERROR: Unexpected property value: {node.properties}')

    def test_htmlnode_children_node(self):
        # Arrange
        # Act
        child = HTMLNode(tag="span", properties={"class": "query"})
        parent = HTMLNode(tag="div", children=child, properties={"class": "directory"})
        
        # Assert
        self.assertIn("TAG: div", str(parent), f'ERROR: Parent node tag "{parent.tag}" not found: NODE="{str(parent)}"')
        self.assertIn("TAG: span", str(parent), f'ERROR: Child node tag "{child.tag}" not found in parent node "{str(parent)}"')

if __name__ == "__main__":
    unittest.main()