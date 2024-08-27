import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('1', '2', '3', '4')
        HTMLNode(node)


if __name__ == "__main__":
    unittest.main()
