#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
xyz_data→clusteringして可視化まで行うメインクラス
"""

"""
- これを実行することでプログラムが走るようにする
- 引数は 重合数,xyzフォルダ名 (python main.py 8 8mer_xyz)
- 対話モードなどをユーティリティを実装する可能性を考慮して作ったがclustering.pyを直接実行しても良い
"""

__author__ = "SYHNE"
__version__ = "0.0.0"
__date__ = "23 Oct 2023"

import sys
from main import clustering
np.set_printoptions(threshold=10000)
#from main.IOinterface import IOInterface

def main(x,y):
    data = clustering(x, y)
    data.two_dim_plot()


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])