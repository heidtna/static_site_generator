import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>", f"ERROR: Unexpected output from node: {str(node)}")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Here", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click Here</a>', f"ERROR: Unexpected output from node: {str(node)}")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!", f"ERROR: Unexpected output from node: {str(node)}")
