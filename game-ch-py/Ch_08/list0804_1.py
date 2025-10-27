import tkinter

root = tkinter.Tk()  # ウィンドウの作成
root.title("迷路の表示")  # ウィンドウタイトルの設定

canvas = tkinter.Canvas(width=800, height=560, bg="white")  # キャンバスの作成
canvas.pack()  # キャンバスの配置

# 迷路のデータ（1: 壁, 0: 通路）
maze = [
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
                x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill="gray"
            )  # 壁を灰色で描画
root.mainloop()  # ウィンドウの表示
