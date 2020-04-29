# -*- coding:utf-8 -*-
# 扫描生成
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

content_path = [here,"_posts"]
output_path = [here,"blogs"]

file_require = {}

root_path = "/".join(content_path)
out_space = "/".join(output_path)
  
def search_Dir(dir_path):
    for path in os.listdir(dir_path):

        content_path.append(path)
        output_path.append(path)
        cur_path = "/".join(content_path)
        out_path= "/".join(output_path)
        if os.path.isfile(cur_path) and cur_path.endswith('.ipynb'):
            filename,suffix = os.path.splitext(out_path)
            html_path = filename + ".html"
            file_require[cur_path] = html_path
        elif os.path.isdir(cur_path) and not cur_path.endswith(".ipynb_checkpoints"):
            search_Dir(cur_path)
            if not os.path.isdir(out_path):
                os.makedirs(out_path)

        content_path.pop()
        output_path.pop()
    
search_Dir(root_path)

for jpy in file_require:
    cmd = "jupyter nbconvert --to html %s --output %s"%(jpy,file_require[jpy])
    print(cmd)
    os.system(cmd)

os.system("jupyter nbconvert --to html --execute .\index.ipynb --output index.html")

# print("exit")
# sys.exit()
#主页刷新
# 纯导出
# jupyter nbconvert --to html .\index.ipynb 
# 指定导出
# jupyter nbconvert --to html .\index.nbconvert.ipynb --output index.html
# 执行导出
# jupyter nbconvert --to html --execute .\index.ipynb --output index1.html