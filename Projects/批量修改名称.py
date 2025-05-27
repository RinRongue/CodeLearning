import os

folder_path=input('欢迎使用批量修改文件名称脚本\n本脚本可将文件按文件名排序\n并修改成文件名+序号的形式\n拖动文件或文件夹到终端内\n或输入文件夹的绝对路径：').strip().strip('"').strip("'")
if os.path.isfile(folder_path):
    folder_path = os.path.dirname(folder_path)
print(f'读取到文件夹路径为{folder_path}')
files = sorted(f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))
# files = []
# for f in os.listdir(folder_path):
#     full_path = os.path.join(folder_path, f)
#     if os.path.isfile(full_path):
#         files.append(f)
# files.sort()

file_name=input('文件原始名称：')
for i,filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    name, ext = os.path.splitext(filename)
    new_name = f'{file_name} No.{i+1}{ext}'
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print(f'文件名已修改')