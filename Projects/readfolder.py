import os

def readfile():
    file_name = input('拖入或输入文件路径：').strip().strip('"').strip("'")
    if os.path.isdir(file_name):  
        print('这是一个文件夹，请拖入文件而不是文件夹！')
        return readfile()  
    elif os.path.isfile(file_name):  
        print(f'这是一个文件，路径为：{file_name}')
        return file_name
    else:  
        print('路径无效，请检查路径是否正确')
        return readfile()  
    