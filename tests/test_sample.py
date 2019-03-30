from ytilities.adwords import MyClass


def test_pass():
    assert True, "dummy sample test"


def test_get_5():
    myclass = MyClass()
    assert myclass.get_5() == 5, "MyClass get_5 returns 5"
