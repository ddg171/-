#coding UTF-8

import os, shutil, sys
import tkinter.messagebox
import NameFix  

#ウィンドウの設定
app_name = "ファイル名から単語を消すやつ"
app_size = "400x300" 



#各フォームの説明文
form1_text ="ディレクトリを選択"
form2_text ="単語を選択"
checkbox_text ="変更対象にフォルダを含める"

#rootウィンドウ
root = tkinter.Tk()
root.title(app_name)
root.geometry(app_size)
root.resizable(0,0) #ウィンドウサイズを固定

#変数
dir_target =tkinter.StringVar() #対象となるディレクトリを格納
keyword =tkinter.StringVar() #対象となる単語を格納

#入力欄1（ディレクトリを入力する欄）
tkinter.Label(text=form1_text).pack()
dir_entry = tkinter.Entry(root, textvariable=dir_target, width=40)
dir_entry.pack()


#入力欄2（単語を入力する欄）
tkinter.Label(text=form2_text).pack()
word_entry = tkinter.Entry(root, textvariable=keyword, width=40) 
word_entry.pack()


#ボタン1を押した場合の動作
def btn1_action(event):
    target= dir_target.get()
    key= keyword.get()
    result = NameFix.rename(target,key)
    if type(result) is int:
        tkinter.messagebox.showinfo("実行結果", "{}個のファイルを変更しました。".format(str(result)))
    else:
        tkinter.messagebox.showwarning("失敗", "ディレクトリがありません。")

#ボタン1
btn1 = tkinter.Button(text=u"実行")
btn1.bind("<Button-1>", btn1_action)
btn1.pack()



root.mainloop()