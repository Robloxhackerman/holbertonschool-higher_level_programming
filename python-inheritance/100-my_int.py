#!/usr/bin/python3
"""Hmmmm"""


class MyInt(int):
    """El pibe rebelde"""

    def __eq__(self, other):
        """UNO: red reverse"""

        return super().__ne__(other)

    def __ne__(self, other):
        """UNO: blue reverse"""

        return super():__eq__(other)
