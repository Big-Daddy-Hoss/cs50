from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
   jar = Jar()
   jar.deposit(13)
   assert jar.capacity == 0



def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(5)
    assert jar.capacity == 11
    jar.withdraw(1)
    assert jar.capacity == 12
    jar.withdraw(1)
    assert jar.capacity == 12
