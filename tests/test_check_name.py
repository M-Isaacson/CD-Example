from app.functions import check_name


def test_is_valid_name():
    assert check_name.is_valid_name("Piet") is True
    assert check_name.is_valid_name("Donald") is False
    assert check_name.is_valid_name("kees") is True
