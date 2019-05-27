#coding UTF-8

#指定したディレクトリ内のファイルから特定の単語を削除するプログラム
import os, shutil,shelve

import namefix as nf


dir_ ="" #変更対象のあるディレクトリ
keyword="_orig" #変更する単語。
folder_set = False #フォルダを変更対象に含めるかどうか。標準では含めない。
#filename_restriction =["\\","*","?",";",":","/","<",">","|",] #ファイル名に使用できない文字のリスト(現時点では不使用)
#filepath_limit = 260 #パスを含めたファイル名の文字数上限（現時点では不使用）



#設定ファイルがある場合は設定を読み出し
latest_config= shelve.open("config")
try:
    keyword = latest_config["keyword"]
    dir_ = latest_config["dir_"]
except KeyError:
    pass
if keyword != "" and dir_ != "":
    latest_config.clear()
latest_config.close()


#リネームしたいファイルのあるディレクトリを指定
print("ファイルのあるディレクトリを指定してください")
if dir_ !="":
    print("空欄の場合は\n{}\nが指定されます".format(dir_))
if dir !="":
    dir_ = input()


#ファイル名から削除したい単語を指定
keyword_select = input("ファイル名から消去したい単語を入力してください\n空欄の場合は{}を削除します。\n".format(keyword))
if keyword_select !="":
    keyword = keyword_select

#変更対象にフォルダを含めるか確認
print("変更対象にフォルダを含めますか？(Y/N)")
if input() =="Y":
    folder_set = True
    print("フォルダを変更対象に含めます")
else:
    print("フォルダを変更対象に含ません")

#ここから処理開始

#指定されたディレクトリのファイル一覧を取得
file_list = nf.dir_check(dir_)
if file_list == False:
    print("ディレクトリあるいはファイルが存在しません。")
else:
    #変更対象のファイル一覧を作成
    file_list= nf.file_filter(dir_,  keyword, folder_set,*file_list)
    if len(file_list) >0:
        print("{}個のファイルを変更します。".format(len(file_list)))
        #変更処理を実行
        nf.rename(dir_, keyword,*file_list)
    else:
        print("変更するファイルはありません。")

    #実施後に設定を保存する
    config = shelve.open("config")
    config["keyword"] =keyword
    config["dir_"] = dir_
    config.close()

print("終了")