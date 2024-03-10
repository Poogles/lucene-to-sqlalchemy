from typing import Any


# Grouping brackets
OPENING_BRACKET = "("
CLOSING_BRACKET = ")"
# Range brackets
OPENING_RANGE = "["
CLOSING_RANGE = "]"
KEY_DELIMITER = ":"
QUOTE = '"'
WHITESPACE = " "


class Key:
    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, other) -> bool:
        if not isinstance(self, type(other)):
            return False

        if self.value == other.value:
            return True

        return False

    def __repr__(self):
        return f"Key({self.value})"


class Value:
    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, other) -> bool:
        if not isinstance(self, type(other)):
            return False

        if self.value == other.value:
            return True

        return False

    def __repr__(self):
        return f"Value({self.value})"


class Range:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __eq__(self, other) -> bool:
        if not isinstance(self, type(other)):
            return False

        if self.start == other.start and self.end == other.end:
            return True

        return False

    def __repr__(self):
        return f"Range({self.start}, {self.end})"


def _peek(query: list[str], depth: int | None = None, char: str | None = None) -> str:
    """Peek through the query into the future."""
    pass


def lexer(query: str) -> Any:
    # Current pointer.
    loc = 0
    token_builder: list[str] = []
    lexed_values: list[Key | Value | Range] = []

    while True:
        try:
            current_token = query[loc]
        # We've got to the end of the token.
        except IndexError:
            # If nothing is in the current list of tokens...
            if not token_builder:
                break

            lexed_values.append(Value(value="".join(token_builder)))
            token_builder = []
            break

        match current_token:
            # Ignore whitespace for now
            case " ":
                pass

            case ":":
                lexed_values.append(Key(value="".join(token_builder)))
                token_builder = []

            case '"':
                # Local starting loc, trimmed of the double quote.
                _local_loc = loc + 1
                endquote_indx = query[_local_loc:].find('"')
                token_builder.extend(
                    [x for x in query[_local_loc : _local_loc + endquote_indx]]
                )
                # Advance past the double quotes.
                loc += endquote_indx + 1

            case "[":
                # Local starting loc, trimmed of the double quote.
                _local_loc = loc + 1
                endquote_indx = query[_local_loc:].find("]")
                range_query = query[_local_loc : _local_loc + endquote_indx]
                outputs = range_query.split("TO")

                start, end = int(outputs[0]), int(outputs[1])
                lexed_values.append(Range(start=start, end=end))
                # Advance past the double quotes.
                loc += endquote_indx + 1

            case _:
                token_builder.append(current_token)

        # Next token.
        loc += 1
    return lexed_values


class Query:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __eq__(self, other):
        if (
            isinstance(type(self), type(other))
            and self.key == other.key
            and self.value == other.value
        ):
            return True

        return False

    def __repr__(self):
        return f"Query({self.key}: {self.value})"
