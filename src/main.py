from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode

def main():
  # text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
  # print(text_node)
  # html_node = HTMLNode("a", "Google", None, {"href": "https://google.com", "target": "_blank"})
  # print(html_node.props_to_html())
  # print(html_node)
  leaf_node1 = LeafNode("p", "This is a paragraph of text.")
  leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
  print(leaf_node1.to_html())
  print(leaf_node2.to_html())

main()