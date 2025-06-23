from stack import Stack
from html_tag import HtmlTag

class HtmlValidator:

    @staticmethod
    def is_valid_html(tags):
        """
        Takes a queue of HtmlTag objects and returns a stack of unmatched opening tags (if any).
        If tags are in incorrect order or unmatched, return the current stack.
        If a closing tag appears with no opening tag, return None.
        """
        stack=Stack()
        while not tags.is_empty():
            tag=tags.dequeue()
            if tag.is_self_closing():
                continue
            elif tag.is_open_tag():
                stack.push(tag)
            else:
                if stack.is_empty():
                    return None
                elif tag.matches(stack.peek()):
                    stack.pop()
                else:
                    return stack  
        return stack     
                