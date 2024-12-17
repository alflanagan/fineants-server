"""
Classes used to recognize and parse some kind of input.
"""
import re
from typing import AnyStr, Match, Optional


class Recognizer:
    def matches(self, some_str):
        """
        True if `some_str` is recognized.
        """
        return False


class RegExRecognizer(Recognizer):
    """
    Checks for a match against a regular expression.
    """

    default_regex = ""  # override for child classes

    def __init__(self, regex=""):
        """
        Create a recognizer which recognizes matches to `regex`.

        If `regex` omitted or `""`, uses the class `default_regex`.
        """
        regex = self.default_regex if regex == "" else regex
        self.regex = re.compile(regex)

    def matches(self, some_str: AnyStr) -> Optional[Match[AnyStr]]:
        """
        True if `some_str` matches the regex.
        """
        return self.regex.match(some_str)
