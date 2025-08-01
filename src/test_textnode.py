import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node_1 = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node_1, node_2, f"ERROR: Nodes not equal: [{node_1}] != [{node_2}]")

    def test_different_text_not_equal(self):
        node_1 = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node_1, node_2, f"ERROR: Nodes with different 'text' values should not be equal: \n\tNode 1: [{node_1}] \n\tNode 2: [{node_2}]")

    def test_different_type_not_equal(self):
        node_1 = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is a text node", TextType.ITALLIC)
        self.assertNotEqual(node_1, node_2, f"ERROR: Nodes with different 'text_type' values should not be equal: \n\tNode 1: [{node_1}] \n\tNode 2: [{node_2}]")

    def test_link_equal(self):
        node_1 = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        node_2 = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        self.assertEqual(node_1, node_2, f"ERROR: Nodes not equal: [{node_1}] != [{node_2}]")

    def test_link_different_url_not_equal(self):
        node_1 = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        node_2 = TextNode("This is a text node", TextType.LINK, "https://sample.com")
        self.assertNotEqual(node_1, node_2, f"ERROR: Nodes with different 'url' values should not be equal: \n\tNode 1: [{node_1}] \n\tNode 2: [{node_2}]")

    def test_link_without_url_fails(self):
        try:
            _ = TextNode("This link doesn't have a url", TextType.LINK)
        except Exception as e:
            self.assertIsInstance(e, AttributeError, f"ERROR: Unexpected error type:\n\tExpecting {type(AttributeError).__name__}\n\tRaised {type(e).__name__}")
            self.assertIn("LINK and IMAGE nodes must have a url", str(e), "ERROR: Unexpected AttributeError")

    def test_image_without_url_fails(self):
        try:
            _ = TextNode("This image doesn't have a url", TextType.IMAGE)
        except Exception as e:
            self.assertIsInstance(e, AttributeError, f"ERROR: Unexpected error type:\n\tExpecting {type(AttributeError).__name__}\n\tRaised {type(e).__name__}")
            self.assertIn("LINK and IMAGE nodes must have a url", str(e), "ERROR: Unexpected AttributeError")

if __name__ == "__main__":
    unittest.main()