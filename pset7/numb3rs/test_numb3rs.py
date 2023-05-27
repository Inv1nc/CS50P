from numb3rs import validate


def test_valid_ip():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True


def test_invalid_ip():
      assert validate("Inv1nc") == False
      assert validate("x.x.x.x") == False
      assert validate("298.1.1.1") == False
      assert validate("285.563.325.3786") == False
      assert validate("255.x.x.x") == False
      assert validate("1.190.20.400") == False
