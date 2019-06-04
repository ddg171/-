#! python3
#coding UTF-8

import os, shutil, sys
import shelve

import tkinter.messagebox
import tkinter.font as font
from tkinter import filedialog as tkFileDialog

import namefix  as nf

#基本設定
app_name = "ファイル名から単語を消すやつ"
app_size = "500x170" 

#rootウィンドウの設定
root = tkinter.Tk()
root.title(app_name)
root.geometry(app_size)
root.resizable(0,0) #ウィンドウサイズを固定

#各フォームの説明文
form1_text ="フォルダを指定してください"
form1_dialog_text="選択"
form2_text ="単語を指定してください"
checkbtn_text ="変更対象にフォルダを含める場合はチェック"

#ラベルの設定
label_font = font.Font(root, family="System",size=14, weight="normal")
#チェックボタンの設定
checkbtn_font= font.Font(root, family="System",size=16, weight="normal")
#ボタンの設定
btn_font = font.Font(root, family="System",size=18, weight="normal")

#変数
dir_buffer =tkinter.StringVar() #対象となるディレクトリを格納
keyword_buffer =tkinter.StringVar() #対象となる単語を格納
folder_conf = tkinter.BooleanVar() #フォルダ除外設定
folder_conf.set(False)

#設定ファイルがある場合は設定を読み出し
latest_config= shelve.open("config")
try:
    keyword_init = latest_config["keyword"]
    dir_init = latest_config["dir_"]
except KeyError:
    keyword_init = ""
    dir_init = ""
latest_config.close()

#入力欄1（パスを入力する欄）
tkinter.Label(text=form1_text, font=label_font).pack()
dir_entry = tkinter.Entry(root, textvariable=dir_buffer, width=70)
dir_entry.insert(tkinter.END, dir_init)
dir_entry.pack(anchor = 'w',fill="both" )

#ダイアログ使用時の動作
def dir_dialog_action(event):
    dir_entry.delete(0, tkinter.END)
    dir_=tkFileDialog.askdirectory()
    dir_entry.insert(tkinter.END, dir_)

#GUIでのフォルダ選択ボタン
dir_dialog = tkinter.Button(text=form1_dialog_text, font=btn_font)
dir_dialog.bind("<Button-1>",dir_dialog_action)
dir_dialog.pack(anchor = 'w')

#入力欄2（単語を入力する欄）
tkinter.Label(text=form2_text, font=label_font).pack()
word_entry = tkinter.Entry(root, textvariable=keyword_buffer,width=70)
word_entry.insert(tkinter.END,keyword_init) 
word_entry.pack(anchor = 'w', fill="both" )

#チェックボタン
chk_btn1=tkinter.Checkbutton(root, text= checkbtn_text, variable= folder_conf, font=checkbtn_font)
chk_btn1.pack(anchor = 'w' ) 

#ボタン1を押した場合の動作(実行処理)
def btn1_action(event):
    dir_= dir_buffer.get()
    keyword= keyword_buffer.get()
    folder_set =folder_conf.get()

    file_list = nf.dir_check(dir_)
    if file_list == False:
        tkinter.messagebox.showerror(title="エラー", message="存在しない場所か未対応の形式が含まれています。")
    else:
       #変更対象のファイル一覧を作成
        file_list= nf.file_filter(dir_,  keyword, folder_set,*file_list)
        if len(file_list) >0:
            if tkinter.messagebox.askokcancel(title="確認",message="{}個のファイルを変更します。".format(len(file_list))) == 1:
                #変更処理を実行
                nf.rename(dir_, keyword,*file_list)
            else:
                tkinter.messagebox.showinfo(title="中断",message="処理を中断します。")
        else:
            tkinter.messagebox.showinfo(title="確認",message="変更するファイルはありません。")
    tkinter.messagebox.showinfo(title="終了",message="処理を終了します")
    #実施後に設定を保存する
    config = shelve.open("config")
    config["keyword"] = keyword
    config["dir_"] = dir_
    config.close()


#ボタン1(実行ボタン)
btn1 = tkinter.Button(text="実行", font=btn_font)
btn1.bind("<Button-1>", btn1_action)
btn1.pack(anchor = 'se' )



root.mainloop()