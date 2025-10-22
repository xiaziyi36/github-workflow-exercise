import pytest
from app.app import dedupe, add

def test_dedupe():
    """测试去重功能"""
    assert list(dedupe([1, 2, 2, 3])) == [1, 2, 3]
    assert list(dedupe(['a', 'b', 'b', 'a'])) == ['a', 'b']

def test_add():
    """测试加法功能"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_dedupe_empty():
    """测试空列表去重"""
    assert list(dedupe([])) == []