import threading
import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = f.readline()
        while line != '':
            all_data.append(line)
            line = f.readline()


# file_names = ['file 1.txt','file 2.txt','file 3.txt','file 4.txt']
# start_time = time.time()
# for file_name in file_names:
#     read_info(f'./{file_name}')
# fin_time = time.time()
# print(fin_time - start_time)

if __name__ == '__main__':
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
    start_time = time.time()
    with multiprocessing.Pool(len(file_names)) as p:
        p.map(read_info, file_names)
    fin_time = time.time()
    print(fin_time - start_time)



