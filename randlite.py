import os
import json
import random

# 定义战利品表的根目录
source_folder = './data/minecraft/loot_tables'

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

            # 将随机化后的内容写回对应的文件中
            for file_path, loot_table in zip(file_paths, loot_tables):
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(loot_table, f, indent=4)

print("Completed. Each subfolder's loot tables have been randomized within their respective folder.")
