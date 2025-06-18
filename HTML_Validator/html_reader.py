from html_tag import HtmlTag
from my_queue import MyQueue

class HtmlReader:
    """
    This class reads an HTML file and converts it into a queue of HtmlTag objects.
    Provided as a convenience class for testing.
    """

    @staticmethod
    def get_tags_from_html_file(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return HtmlTag.tokenize(html_content)
        # queue = MyQueue()
        # for tag in HtmlTag.tokenize(html_content):
        #     queue.enqueue(tag)
        # return queue
