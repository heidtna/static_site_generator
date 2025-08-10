from typing import List, Union
from textnode import TextType, TextNode
from htmlnode import HTMLNode

class SplitNode:
    @staticmethod
    def split_node_delimiter(old_nodes: List[Union[TextNode, HTMLNode]], delimiter, text_type: TextType):
        new_nodes = []
        for node in old_nodes:
            # We only care about modifying TEXT nodes
            if not isinstance(node, TextNode):
                new_nodes.append(node)
                continue

            # Delimiters must come in pairs (count should be even)
            if node.text.count(delimiter) % 2 != 0:
                raise Exception(f"Text must contain an even number of delimiters - Found {node.text.count(delimiter)}")

            segments = node.text.split(delimiter)
            for i in range(0, len(segments)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(segments[i], TextType.PLAIN))
                else:
                    match delimiter:
                        case "**":
                            new_nodes.append(TextNode(segments[i], TextType.BOLD))
                        case "_":
                            new_nodes.append(TextNode(segments[i], TextType.ITALLIC))
                        case "`":
                            new_nodes.append(TextNode(segments[i], TextType.CODE))
                        case _:
                            raise Exception(f"Invalid delimiter type: {delimiter}")

            
        raise NotImplementedError("This method is not finished.")