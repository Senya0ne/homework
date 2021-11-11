from src.MainClass import MainClass


def test_get_local_number():
    local_number = MainClass()
    assert local_number.get_local_number() == 14, "Число не равняется 14"
