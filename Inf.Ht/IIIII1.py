from IIIII import check

import pytest


def test1():
    assert check('zyz')==False


def test2():
    assert check('zyz@gmail.com')==False


def test3():
    assert check('zyyz@gmail.com')==True


def test4():
    assert check('shark@mail.ru')==False


def test5():
    assert check('')==False


def test6():
    assert check(3)==False


def test7():
    assert check('zyyz@2@.com')==False


def test8():
    assert check('zyyz@gmail.commm')==False


def test9():
    assert check('zyyyz@yandex')==False


def test10():
    assert check('zzz@g.com')==False


def test11():
    assert check('zzz@sleep.yes')==True