from main.IOinterface import IOInterface
class clustering(IOInterface):

    """
    [インスタンス変数]

        poly_num
            重合数。intの整数値を持つ。
        structure
            xyzファイルの配列。※ファイル名でなくファイルの中身がそのまま入っている。

    [インスタンスメソッド]
        
        __init__(player_distribution, face_distribution_type, card_distribution_type, initial_dice_face_type):
            player_distribution     -   "human"か"computer"の文字列配列
            face_distribution_type  -   ゲームで使用するフェイスの組成タイプ、詳細はmain.py
            card_distribution_type  -   ゲームで使用するカードの組成タイプ、詳細はmain.py
            initial_dice_face_type  -   ゲームで使用する初期ダイスの組成タイプ、詳細はmain.py

        game():
            ゲームのメイン処理が書かれるメソッド。
            main.pyでclusteringインスタンスが作成されたあと、このメソッドが呼び出される。

        read():
            コマンドを要求するメッセージを表示し、入力コマンドを返すメソッド。

        write(string):
            改行をいれたあと、stirngを出力するメソッド。
            各所でprintをするとログが取りづらいので、出力は一旦ここを介するように。

        write_wrong_command_message():
            無効なコマンド（illegalな操作ではない）を入力したときに呼び出されるメソッド。
            エラーログを表示する。

        choose_first_action(player):
            1つ目の行動のコマンドの入力を受け付け処理するメソッド。

        print_help():
            可能なコマンド一覧を表示するメソッド。

        make_face_distribution(face_distribution_type):
            フェイスの組成タイプを受け取り、人数を加味して、実際に使用すべきフェイスのidの配列を返すメソッド。

        make_initial_dice_face(player_list, initial_dice_face_type):
            最初のダイスの組成タイプを受け取り、各プレイヤーに対して最初のダイスを発行するコマンド。
            Playerの内部のDicesにアクセスしてDiceを追加する。
    """
    def __init__(self,structure, poly_num,):
        self.structure = structure
        self.poly_num = poly_num

    def write(self, sentense):
        print(sentense)

    def read(self):
        return input("\n> loading done\n")
    def 