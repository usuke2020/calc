import tkinter as tk
# ボタンの配置
BUTTONS = [
  ['(', ')', '%', 'AC'],  
  ['7', '8', '9', '/'],
  ['4', '5', '6', '*'],
  ['1', '2', '3', '-'],
  ['0', '.', '=', '+']
]

#ボタンイベント
def make_click(ch):
    def click(e):
        print(ch)
        if ch == '=': calc(0); return
        else: disp.insert(tk.END, ch)
    return click

#計算式の計算
def calc(e):
    label["text"] = '= ' + str(eval(disp.get()))


#ウィンドウの作成
win = tk.Tk()
win.title("電卓")           #タイトル
win.geometry("400x350")     #サイズ


#ディスプレイ部分
disp = tk.Entry(win, font=('', 20), justify="center")
disp.pack(fill='x')
disp.bind('<Return>', calc)
label = tk.Label(win, font=('', 20), anchor="center")
label.pack(fill='x')


#電卓のボタンを一括作成
fr = tk.Frame(win)
fr.pack()
for y, cols in enumerate(BUTTONS):
    for x, n in enumerate(cols):
        btn = tk.Button(fr, text=n, font=('', 20), width=6, height=1)
        btn.grid(row=y+1, column=x+1)
        btn.bind('<1>', make_click(n))


# 起動
win.mainloop()