from src.MainClass import MainClass


def test_get_class_string():
    private_string = MainClass()
    assert "Hello" in private_string.get_class_string(), "Строка не содержит Hello"
    assert "hello" in private_string.get_class_string(), "Строка не содержит hello"
