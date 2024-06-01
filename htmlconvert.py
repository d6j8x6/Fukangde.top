import os

def read_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None

def modify_html_content(html_content):
    # 在这里进行你的修改操作
    # 例如，使用正则表达式替换Django导入形式为静态网页导入形式
    modified_html = html_content.replace('png', 'jpg')# 这里只是一个示例，你可以根据需要进行修改(png -> jpg)
    return modified_html

def save_modified_html(file_path, modified_html):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_html)
        print(f"修改后的HTML已保存到 {file_path}")
    except Exception as e:
        print(f"保存文件时出错：{e}")

# 示例用法
input_html_file = 'worker(png).html'
output_html_file = 'worker.html'

html_content = read_html_file(input_html_file)
if html_content:
    modified_content = modify_html_content(html_content)
    save_modified_html(output_html_file, modified_content)
else:
    print(f"找不到文件：{input_html_file}")
