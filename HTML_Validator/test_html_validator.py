import unittest
from html_reader import HtmlReader
from html_tag import HtmlTag
from html_validator import HtmlValidator


class TestHtmlValidator(unittest.TestCase):
    path_to_test_files = './'

    def validate_test_file(self, filename):
        try:
            tags = HtmlReader.get_tags_from_html_file(self.path_to_test_files + filename)
            result = HtmlValidator.is_valid_html(tags)
            return result
        except Exception as e:
            print(f"An exception ({e}) occurred while reading {filename}. Make sure it's in the correct path.")
            return None

    def test_file1(self):
        result = self.validate_test_file("test1.html")
        self.assertIsNotNone(result, "is_valid_html returns None for a valid HTML file.")
        self.assertEqual(len(result), 0, "Expected empty stack for valid HTML.")

    def test_file2(self):
        result = self.validate_test_file("test2.html")
        self.assertIsNotNone(result, "is_valid_html returns None when file ends without closing tags.")
        expected = [HtmlTag("html", True), HtmlTag("b", True)]
        self.assertEqual(result.to_list(), expected, "Returned stack does not match expected unmatched tags.")

    def test_file3(self):
        result = self.validate_test_file("test3.html")
        self.assertIsNotNone(result, "is_valid_html returns None when tags are closed in incorrect order.")
        expected = [HtmlTag("b", True), HtmlTag("i", True)]
        self.assertEqual(result.to_list(), expected, "Returned stack does not match expected mismatched tags.")

    def test_file4(self):
        result = self.validate_test_file("test4.html")
        self.assertIsNone(result, "Expected None when closing tag has no matching opening tag.")

    def test_file5(self):
        result = self.validate_test_file("test5.html")
        self.assertIsNotNone(result, "is_valid_html returns None for valid HTML.")
        self.assertEqual(len(result), 0, "Expected empty stack for valid HTML.")

    def test_file6(self):
        result = self.validate_test_file("test6.html")

        self.assertIsNotNone(result, "is_valid_html returns None when some tags are not closed.")
        expected = [HtmlTag("html", True), HtmlTag("head", True), HtmlTag("title", True), HtmlTag("p", True)]

        self.assertEqual(result.to_list(), expected, "Returned stack does not match expected unmatched tags.")

    def test_file7(self):
        result = self.validate_test_file("test7.html")
        self.assertIsNone(result, "Expected None for HTML containing only a closing tag.")


if __name__ == '__main__':
    unittest.main()
