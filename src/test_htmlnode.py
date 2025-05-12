import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode("a", "Google", None, {"href": "https://google.com", "target": "_blank"})
    node2 = HTMLNode("a", "Google", None, {"href": "https://google.com", "target": "_blank"})
    self.assertEqual(node, node2)

  def test_props_to_html(self):
    node = HTMLNode("a", "Google", None, {"href": "https://google.com", "target": "_blank"})
    self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

  def test_repr(self):
    node = HTMLNode("a", "Google", None, {"href": "https://google.com", "target": "_blank"})
    self.assertEqual(node.__repr__(), "HTMLNode(a, Google, None, {'href': 'https://google.com', 'target': '_blank'})")

if __name__ == "__main___":
  unittest.main()