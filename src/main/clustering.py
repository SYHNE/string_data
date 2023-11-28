from main.IOinterface import IOInterface
from sklearn import cluster, preprocessing  # 機械学習用のライブラリを利用
import matplotlib.pyplot as plt  # プロット用のライブラリを利用
import numpy as np  # numpyという行列などを扱うライブラリを利用
import pandas as pd #pandasというデータ分析ライブラリを利用
from sklearn.decomposition import PCA

class clustering(IOInterface):

    """
    [インスタンス変数]

        poly_num
            重合数。intの整数値を持つ。
        structure
            xyzファイルの配列。※ファイル名でなくファイルの中身がそのまま入っている。

    [インスタンスメソッド]
        

        read():
            コマンドを要求するメッセージを表示し、入力コマンドを返すメソッド。
        pca():
            pdのdataframeに対しpcaして返す。

        write(string):
            改行をいれたあと、stirngを出力するメソッド。
            各所でprintをするとログが取りづらいので、出力は一旦ここを介するように。

        write_wrong_command_message():
            無効なコマンド（illegalな操作ではない）を入力したときに呼び出されるメソッド。
            エラーログを表示する。

        print_help():
            可能なコマンド一覧を表示するメソッド。

    """
    def __init__(self, structure, poly_num):
        self.structure = structure
        self.poly_num = poly_num

    def write(self, sentense):
        print(sentense)

    def read(self):
        return input("\n> loading done\n")
    
    @staticmethod
    def pca(df):
        sc = preprocessing.StandardScaler()
        sc.fit(df)
        df_norm = sc.transform(df)
        PCA_set = PCA(n_components=2)
        PCA_set.fit(df_norm)
        print("--- explained_variance_ratio_ ---")
        print(PCA_set.explained_variance_ratio_)
        print("--- components ---")
        print(PCA_set.components_)
        print("--- mean ---")
        print(PCA_set.mean_)
        print("--- covariance ---")
        print(PCA_set.get_covariance())
        return PCA_set

    @staticmethod
    def MeanShift(df, width):
        ms = cluster.MeanShift(bandwidth=width, seeds=df)
        ms.fit(df)
        return ms.labels_
    
    def two_dim_plot(df, width):
        data = pca(df)
        df_2d = pd.DataFrame(data)
        df_2d.index = df.index
        df_2d.columns = ['PC1', 'PC2']
        df_2d.head()
        labels = MeanShift(data, width)
        x = np.array([])
        y = np.array([])
        for i in range(len(df_2d.values)):
            x = np.append(x, float(df_2d.values[i][0]))
            y = np.append(y, float(df_2d.values[i][1]))
        plt.scatter(x, y, c=labels, s=6)
        plt.show()

