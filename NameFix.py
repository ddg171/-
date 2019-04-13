#coding UTF-8

import os, shutil

def rename(dir_target,keyword):
    if os.path.exists(dir_target)== True:
        #指定されたディレクトリのファイル一覧を取得
        file_list = os.listdir(dir_target)
        #ファイル名にkeywordがついているファイルを抽出
        target_list=[]
        for item in file_list:
            if keyword in item:
                target_list.append(item)
        #リネーム
        for target in target_list:
            new_name =target.replace(keyword,"")
            shutil.move(dir_target + "\\" + target, dir_target + "\\" + new_name)
        return len(target_list)

    else:
        print("指定されたディレクトリは存在しません。")  
        return None
        