# デジタルフレームを作成
import tkinter

pnum = 0  # 写真番号


def photograph():  # 写真を表示する関数
    global pnum
    canvas.delete("PH")  # 以前の写真を削除
    canvas.create_image(400, 300, image=photo[pnum], tag="PH")  # 写真を表示
    pnum += 1
    if pnum >= len(photo):  # 写真番号が範囲外なら
        pnum = 0  # 最初の写真に戻る
    root.after(7000, photograph)  # 7秒後に再度実行


root = tkinter.Tk()
root.title("デジタルフォトフレーム")
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()

photo = [  # 写真データのリスト
    tkinter.PhotoImage(file="../py_samples/Chapter8/cat00.png"),
    tkinter.PhotoImage(file="../py_samples/Chapter8/cat01.png"),
    tkinter.PhotoImage(file="../py_samples/Chapter8/cat02.png"),
    tkinter.PhotoImage(file="../py_samples/Chapter8/cat03.png"),
]
photograph()  # 写真表示を開始
root.mainloop()
