from os import listdir
'''
파일 새로 쓰기
f = open('test.txt', 'w') -> 'a' 파일에 문자열 추가하기
f.write('문자열 쓰기\n')
f.close()

파일 한 줄씩 읽기
f = open('test.txt', 'r')
contents = f.readline()  -> f.readlines(파일의 모든 내용을 리스트형식으로 가져오기) ,f.read(파일의 모든내용 읽기)
print(contents)
f.close()

파일내 현재위치 변경하기(seek)
f = open('test.txt', 'r+')
contents = f.read()
print(contents)
f.write('문자열 추가 테스트\n')
f.seek(0)
contents = f.read()
print(contents)
f.close()'''


#CSV파일 열기
write_file = open('statistics.csv', 'w')
write_file.write('년월,매출\n')


csv_files = 'csv_files/'
file_list = listdir(csv_files)
file_list.sort()

for f_name in file_list:
    if f_name[-3:] != 'csv':
        continue

    sum_value = 0
    f = open(csv_files+f_name, 'r')
    while True:
        row = f.readline()
        if not row:
            break

        data = row.split(',')
        if data[1].isdigit():
            sum_value += int(data[1])

    write_file.write('%s,%d\n'%(f_name[:7], sum_value))
    f.close()

write_file.close()
