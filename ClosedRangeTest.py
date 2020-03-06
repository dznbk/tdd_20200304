from pytest import fixture, raises
from ClosedRange import ClosedRange


@fixture
def closed_range():
    return ClosedRange(3, 8)


def test_整数閉区間インスタンスを生成時に下端点3_上端点8を指定することができる():
    assert isinstance(ClosedRange(3, 8), ClosedRange)


def test_整整数閉区間インスタンスを生成時に下端点3と上端点3で指定することができる():
    assert isinstance(ClosedRange(3, 3), ClosedRange)


def test_整数閉区間インスタンスから取得した下端点が3である(closed_range):
    assert closed_range.bottom == 3


def test_整数閉区間インスタンスから取得した上端点が8である(closed_range):
    assert closed_range.top == 8


def test_文字列表現を返す(closed_range):
    assert closed_range.build_string() == '[3, 8]'


def test_上端点より大きい下端点を指定して閉区間を作ろうとするとエラーが起きる():
    with raises(ValueError):
        ClosedRange(8, 3)


def test_3から8の閉区間は5を含むかどうかを判定できる(closed_range):
    assert closed_range.include_number(5) is True


def test_3から8の閉区間は1を含むかどうかを判定できる(closed_range):
    assert closed_range.include_number(1) is False


def test_3_8の閉区間は3_8の閉区間と等価かどうかを判定できる(closed_range):
    assert closed_range.is_same(ClosedRange(3, 8))


def test_3_8の閉区間は3_5の閉区間と等価かどうかを判定できる(closed_range):
    assert closed_range.is_same(ClosedRange(3, 5)) is False


def test_4_7の閉区間は3_8の閉区間に完全に含まれると判定される(closed_range):
    assert closed_range.include_range(ClosedRange(4, 7))


def test_閉区間が完全に含まれるかの判定の引数が閉区間インスタンスで無い場合はエラーとなる(closed_range):
    with raises(TypeError):
        closed_range.include_range(None);
