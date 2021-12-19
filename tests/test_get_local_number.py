from src.ui.MainPageObject import MainClass


def test_get_сlass_number():
    private_number = MainClass()
    assert private_number.get_local_number() > 45, "Число меньше 45"
