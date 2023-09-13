#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
- 標準入出力を利用するクラスが継承すべきクラス
"""

"""
- 入出力を行うクラスはこのクラスを継承してreadとwriteを実装すること
- 現状はclustering.pyに使用,main.pyの機能が増えると使うかも
"""

__author__ = "SYHNE"
__date__ = "20 May 2023"

from abc import ABCMeta, abstractmethod

class IOInterface:

    """
    [抽象メソッド]
        read():
            標準入力から文字列を受け取る

        write():
            標準出力に書き込む
    """

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass