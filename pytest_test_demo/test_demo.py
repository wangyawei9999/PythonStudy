import pytest


def test_001():
    assert 1+2 == 3


def test_002():
    assert 1 + 2 == 0


class TestLogin:
    def test_003(self):
        assert 1+1 == 2


@pytest.mark.parametrize('a, b', [(10, 20), (30, 40)])
def test_003(a, b):
    assert a + b == 30


if __name__ == '__main__':
    pytest.main(['test_demo.py', '-s', '--html=/Users/user/PycharmProjects/TestProject/report/result.html'])
