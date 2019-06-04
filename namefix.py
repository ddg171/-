#coding UTF-8

import os, shutil

#指定されたディレクトリが存在するか確認し、ある場合はディレクトリ内のファイル、フォルダ一覧を返す関数
def dir_check(dir_input):
    if os.path.exists(dir_input)== True:
        return os.listdir(dir_input)
    else:
        return False


#ディレクトリ内のファイル、フォルダから指定された単語の含まれる物を抽出する関数
def file_filter(path_, keyword_input, folder,*file_list ):
    filtered_list =[]
    for item in file_list:
        if keyword_input in item:
            if os.path.isdir(path_+"\\"+ item) and folder==False:
                pass
            elif item == keyword_input:
                pass
            else:
                filtered_list.append(item)
    return filtered_list

#リネームする関数
def rename(dir_ ,keyword,*file_list,):
    for orig_name in file_list:
        new_name = orig_name.replace(keyword,"")
        shutil.move(dir_ + "\\" + orig_name, dir_ + "\\" + new_name)
    return True

#ダイアログでフォルダ選択を行う関数


#TODO 拡張子が変更されるファイルの有無を出力する関数