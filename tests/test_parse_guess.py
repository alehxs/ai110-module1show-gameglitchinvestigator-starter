from logic_utils import parse_guess

def test_parse_guess_empty():
    ok, val, err = parse_guess("")
    assert ok == False and err == "Enter a guess."

def test_parse_guess_valid_int():
    ok, val, err = parse_guess("42")
    assert ok == True and val == 42 and err is None

def test_parse_guess_float_string():
    ok, val, err = parse_guess("3.7")
    assert ok == True and val == 3 and err is None

def test_parse_guess_non_numeric():
    ok, val, err = parse_guess("abc")
    assert ok == False and err == "That is not a number."