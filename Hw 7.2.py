import os 

def print_docs(directory):
    use_files = os.walk(directory)
    for i in use_files:
        print(f'Директория {i[0]}\nПапки {", ".join([folder for folder in i[1]])} \nФайлы : {", ".join([file for file in i[2]])} \n')
print_docs(input())