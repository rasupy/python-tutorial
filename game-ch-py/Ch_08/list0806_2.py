# クリアしたか判定
import tkinter
import tkinter.messagebox

key = ""  # キーの値を入れる変数の宣言


def key_down(e):  # キーを押した時に実行する関数の定義
    global key
    key = e.keysym  # 押されたキーの値をkeyに代入


def key_up(e):  # キーを離した時に実行する関数の定義
    global key
    key = ""  # keyの値を空にする


mx = 1
my = 1
yuka = 0  # 床の数を数える変数


def main_proc():  # メイン処理の関数の定義
    global mx, my, yuka
    if key == "Up" and maze[my - 1][mx] == 0:
        my -= 1
    if key == "Down" and maze[my + 1][mx] == 0:
        my += 1
    if key == "Left" and maze[my][mx - 1] == 0:
        mx -= 1
    if key == "Right" and maze[my][mx + 1] == 0:
        mx += 1
    if maze[my][mx] == 0:
        maze[my][mx] = 2  # 通路を通った印に変更
        yuka += 1
        canvas.create_rectangle(
            mx * 80, my * 80, mx * 80 + 79, my * 80 + 79, fill="pink", width=0
        )  # 通路をピンクで描画
    canvas.delete("MYCHR")  # キャラクターの削除
    canvas.create_image(
        mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR"
    )  # キャラクターの再描画
    if yuka == 30:
        canvas.update()
        tkinter.messagebox.showinfo("クリア！", "迷路をすべて塗りました！")
    else:
        root.after(300, main_proc)  # 300ミリ秒後にmain_proc関数を呼び出す


root = tkinter.Tk()  # ウィンドウの作成
root.title("迷路内を塗る")  # ウィンドウタイトルの設定
root.bind("<KeyPress>", key_down)  # キーが押された時の処理を登録
root.bind("<KeyRelease>", key_up)  # キーが離された時の処理を登録
canvas = tkinter.Canvas(width=800, height=560, bg="white")  # キャンバスの作成
canvas.pack()  # キャンバスの配置

maze = [  # 迷路のデータ（1: 壁, 0: 通路）(7x10)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:  # 壁の場合
            canvas.create_rectangle(
                x * 80, y * 80, x * 80 + 79, y * 80 + 79, fill="skyblue"
            )  # 壁を水色で描画
img = tkinter.PhotoImage(
    file="../py_samples/Chapter8/mimi_s.png"
)  # キャラクター画像の読み込み
canvas.create_image(
    mx * 80 + 40, my * 80 + 40, image=img, tag="MYCHR"
)  # キャラクターの描画
main_proc()  # メイン処理の呼び出し
root.mainloop()  # ウィンドウの表示
