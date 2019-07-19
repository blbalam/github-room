from shutil import copyfile
from os import listdir, makedirs
from os.path import isdir


'''
#폴더의 파일 목록 조회: listdir
#파일 삭제하기 : os.unlink
#파일을 복사하는 : copyfile
#파일 및 폴더 존재 유무 확인하기: os.path.exists
#폴더 복사하기 : shutil.copytree
#폴더 삭제하기 : shutil.rmtree
#폴더 생성: makedirs
#폴더가 이미 존재하는지 확인 : isdir
'''

#폴더의 파일목록 조회하기
orig_dir = "C:\\scandata\\"
out_dir  = "C:\\organized\\"

file_list = listdir(orig_dir)


#파일명 분석하기
for f_name in file_list:
    f_date = f_name[5:-4]
    f_date = f_date.split('_')
    f_date = f_date[0]
    f_date = f_date.split('-')

    year  = f_date[0]
    month = f_date[1]
    day   = f_date[2]

#폴더 생성하기
    target_dir = out_dir + year + "\\" + month + "\\" + day
    if not isdir(target_dir):
        makedirs(target_dir)

#파일 복사하기
    copyfile(orig_dir+f_name, target_dir+"\\" + f_name)
    print(orig_dir+f_name + " => " + target_dir+"\\" + f_name)
