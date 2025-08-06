import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_no_tag_should_error(self):
        try:
            _ = ParentNode(
                children=[HTMLNode(tag="div", value="My parent has no tag!")]
            )
        except Exception as e:
            self.assertIsInstance(e, TypeError, f'ERROR: Unexpected error occured. Expecting "ValueError" but {type(e).__name__} was raised')

    # TODO: Add A LOT more tests