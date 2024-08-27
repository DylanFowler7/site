import unittest

from textnode import TextNode

class TestTextNodeConversion(unittest.TestCase):
        
    def test_bold_conversion(self):
        # Create a bold TextNode instance
        bold_node = TextNode("Hello", "bold")
                                    
        # Convert to HTML
        html_node = text_node_to_html_node(bold_node)
                                                            
        # Expected HTML output
        expected_html = "<b>Hello</b>"
                                                                                    
        # Assert the result matches the expected HTML
        self.assertEqual(html_node, expected_html)

        # You can create more test methods for italic, code, link, etc.
                                                                                                                
if __name__ == '__main__':
unittest.main()
