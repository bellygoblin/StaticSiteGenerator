from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
  # text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
  # print(text_node)
  html_node = HTMLNode("a", "Google", None, {"href": "https://google.com", "target": "_blank"})
  print(html_node.props_to_html())
  print(html_node)

main()