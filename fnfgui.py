#coding UTF-8

import os, shutil, sys
import tkinter.messagebox
import NameFix  

#ウィンドウの設定
app_name = "ファイル名から単語を消すやつ"
app_size = "300x200"


#rootウィンドウ
root = tkinter.Tk()
root.title(app_name)
root.geometry(app_size)

#グローバル変数
dir_target =tkinter.StringVar()
keyword =tkinter.StringVar()

#入力欄1（ディレクトリを入力する欄）
tkinter.Label(text="ディレクトリを選択").pack()
dir_entry = tkinter.Entry(root, textvariable=dir_target, width=40)
dir_entry.pack()


#入力欄2（単語を入力する欄）
tkinter.Label(text="単語を選択").pack()
word_entry = tkinter.Entry(root, textvariable=keyword, width=40) 
word_entry.pack()

#ボタンを押した場合の動作
def btn1_action(event):
    target= dir_target.get()
    key= keyword.get()
    result = NameFix.rename(target,key)
    if type(result) is int:
        tkinter.messagebox.showinfo("結果", "{}個のファイルを変更しました。".format(str(result)))
    else:
        tkinter.messagebox.showwarning("失敗", "ディレクトリがありません。")

#ボタン
btn1 = tkinter.Button(text=u"実行")
btn1.bind("<Button-1>", btn1_action)
btn1.pack()

root.mainloop()