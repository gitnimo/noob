def add(x,y):
    return x+y
def test1():
    assert 2 == add(1,1)
def test2():
    assert 1 != add(1,1)
#pytest -vv test_A.py 測試ㄎ
#pytest --durations=0 -vv test_A.py 計算時間