from check_pwd import check_pwd

def test_empty_string():
    assert not check_pwd(""), "Empty string should fail"

def test_too_short():
    assert not check_pwd("Ab1!"), "Password shorter than 8 chars should fail"

def test_too_long():
    assert not check_pwd("A1!abcdefghijklmNOPQRST"), "Password longer than 20 chars should fail"

def test_missing_lowercase():
    assert not check_pwd("ABCDEFG1!"), "Password with no lowercase should fail"

def test_missing_uppercase():
    assert not check_pwd("abcdefg1!"), "Password with no uppercase should fail"

def test_missing_digit():
    assert not check_pwd("Abcdefg!"), "Password with no digit should fail"

def test_missing_symbol():
    assert not check_pwd("Abcdefg1"), "Password with no allowed symbol should fail"

def test_invalid_symbol_only():
    assert not check_pwd("Abcdefg1?"), "Password with only unallowed symbol should fail"

def test_valid_password():
    assert check_pwd("Abcdef1!"), "Password meeting all criteria should pass"

def test_edge_min_length():
    assert check_pwd("A1b2C3d!"), "Password of length 8 meeting criteria should pass"

def test_edge_max_length():
    assert check_pwd("Ab1!Ab1!Ab1!Ab1!Ab1!"), "Password of length 20 meeting criteria should pass"

def main():
    test_empty_string()
    test_too_short()
    test_too_long()
    test_missing_lowercase()
    test_missing_uppercase()
    test_missing_digit()
    test_missing_symbol()
    test_invalid_symbol_only()
    test_valid_password()
    test_edge_min_length()
    test_edge_max_length()
    print("All tests passed!")

if __name__ == "__main__":
    main()
