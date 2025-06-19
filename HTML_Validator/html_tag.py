import re
# from collections import deque
from my_queue import MyQueue
class HtmlTag:
    SELF_CLOSING_TAGS = {
        "!doctype", "!--", "?xml", "xml", "area", "base",
        "basefont", "br", "col", "frame", "hr", "img",
        "input", "link", "meta", "param"
    }

    WHITESPACE = " \f\n\r\t"

    def __init__(self, element: str, is_open_tag: bool):
        self.element = element.lower()
        self.open_tag = is_open_tag

    def get_element(self):
        return self.element

    def is_open_tag(self):
        return self.open_tag and not self.is_self_closing()

    def matches(self, other):
        return (other is not None
                and self.element.lower() == other.element.lower()
                and self.open_tag != other.open_tag)

    def is_self_closing(self):
        return self.element in HtmlTag.SELF_CLOSING_TAGS

    # def __eq__(self, other):
    #     return (isinstance(other, HtmlTag)
    #             and self.element == other.element
    #             and self.open_tag == other.open_tag)

    def __eq__(self, other):
        if isinstance(other, HtmlTag):
            return self.element == other.element and self.open_tag == other.open_tag
        return False


    def __str__(self):
        if self.element == "!--":
            return "<!-- -->"
        return f"<{'' if self.open_tag else '/'}{self.element}>"


    # /**
    #  * The remaining fields and functions are related to HTML file parsing.
    #  */

    # // a set of tags that don't need to be matched (self-closing)

    @staticmethod
    def tokenize(text: str):
        buf = text
        queue = MyQueue()

        while True:
            next_tag = HtmlTag.next_tag(buf)
            if not next_tag:
                break
            queue.enqueue(next_tag)

            # Properly find end of current tag to slice buffer
            open_bracket = buf.find("<")
            close_bracket = buf.find(">", open_bracket)
            if close_bracket == -1:
                break  # malformed, exit loop
            buf = buf[close_bracket + 1:]

        return queue

    @staticmethod
    def next_tag(buf: str):
        open_bracket = buf.find("<")
        close_bracket = buf.find(">")

        if open_bracket >= 0 and close_bracket > open_bracket:
            # Check for comments
            comment_index = open_bracket + 4
            if (comment_index <= len(buf) and
                buf[open_bracket + 1:comment_index] == "!--"):
                close_bracket = buf.find("-->", comment_index)
                if close_bracket < 0:
                    return None
                close_bracket += 3

            element = buf[open_bracket + 1:close_bracket].strip()

            # Remove attributes
            for ws in HtmlTag.WHITESPACE:
                attr_index = element.find(ws)
                if attr_index >= 0:
                    element = element[:attr_index]

            # Determine open/close tag
            is_open_tag = True
            if element.startswith("/"):
                is_open_tag = False
                element = element[1:]

            element = re.sub(r"[^a-zA-Z0-9!-]+", "", element)

            return HtmlTag(element, is_open_tag)

        return None
