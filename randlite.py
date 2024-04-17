import os
import json
import random
import shutil

# 定义战利品表的根目录
source_folder = r'./loot_tables'
# 目标文件夹路径，确保这个文件夹可以被创建
target_folder = r'./rand_loot/data/minecraft/loot_tables'

# 确保目标文件夹存在，如果存在则清空内容
if os.path.exists(target_folder):
    for root, dirs, files in os.walk(target_folder, topdown=False):
        for file in files:
            if not file.endswith('.mcmeta'):
                os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
else:
    os.makedirs(target_folder)

# 遍历战利品表的根目录
for root, subdirs, files in os.walk(source_folder):
    if root == source_folder:
        # 对根目录下的每个子目录进行操作
        for subdir in subdirs:
            subdir_path = os.path.join(root, subdir)
            loot_tables = []
            file_paths = []

            # 收集当前子目录中所有战利品表的内容和路径
            for file in os.listdir(subdir_path):
                if file.endswith('.json'):
                    file_path = os.path.join(subdir_path, file)
                    file_paths.append(file_path)

                    with open(file_path, 'r', encoding='utf-8') as f:
                        loot_tables.append(json.load(f))

            # 随机打乱当前子目录中所有战利品表的内容
            random.shuffle(loot_tables)

            # 创建目标子目录
            target_subdir = os.path.join(target_folder, subdir)
            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)

            # 将随机化后的内容写回对应的文件中，确保写入新的目标目录
            for file_path, loot_table in zip(file_paths, loot_tables):
                new_file_path = os.path.join(target_subdir, os.path.basename(file_path))
                with open(new_file_path, 'w', encoding='utf-8') as f:
                    json.dump(loot_table, f, indent=4)

print("Completed. Each subfolder's loot tables have been randomized and written to the new location.")
