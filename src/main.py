from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
  grandchild_node = LeafNode("b", "grandchild")
  child_node = ParentNode("span", [grandchild_node])
  parent_node = ParentNode("div", [child_node])

  print(parent_node.to_html())

main()