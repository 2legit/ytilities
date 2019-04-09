from ytilities import *

def test_pass():
    assert True, "dummy sample test"

def test_get_5():
    myclass = adwords.MyClass()
    assert myclass.get_5() == 5, "MyClass get_5 returns 5"


print(__name__)
print(adwords.MyClass.get_5())