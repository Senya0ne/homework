from src.MainClass import MainClass


def test_get_local_number():
    local_number = MainClass()
    assert local_number.get_local_number() == 20, "Число не равняется 20"
