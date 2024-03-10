from lib import lexer, Query, Key, Value, Range


def test_parser():
    assert lexer("id: 123") == [Key("id"), Value("123")]
    assert lexer('id: "potatoe chips"') == [Key("id"), Value("potatoe chips")]
    assert lexer("id: [1 TO 12]") == [Key("id"), Range(1, 12)]


def test_lexer():
    pass
