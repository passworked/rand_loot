import os
import shutil
import random

# 原始文件夹路径
source_folder = r'./data/randloot/loot_tables'
# 目标文件夹路径，确保这个文件夹可以被创建
target_folder = r'./new_data/minecraft/loot_tables'

# 确保目标文件夹存在
os.makedirs(target_folder, exist_ok=True)

# 步骤1：遍历原始目录收集战利品表文件的完整路径
loot_table_paths = []
for root, _, files in os.walk(source_folder):
    for file in files:
        if file.endswith(".json"):  # 确保只处理JSON文件
            full_path = os.path.join(root, file)
            loot_table_paths.append(full_path)

# 步骤2：复制文件结构到新目录，不复制文件内容
for path in loot_table_paths:
    relative_path = os.path.relpath(path, source_folder)
    target_path = os.path.join(target_folder, relative_path)
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    shutil.copy(path, target_path)

# 步骤3：读取新目录中所有文件的内容
loot_table_contents = []
new_loot_table_paths = []
for root, _, files in os.walk(target_folder):
    for file in files:
        if file.endswith(".json"):
            full_path = os.path.join(root, file)
            new_loot_table_paths.append(full_path)
            with open(full_path, 'r', encoding='utf-8') as file:
                loot_table_contents.append(file.read())

# 步骤4：随机打乱内容
random.shuffle(loot_table_contents)

# 步骤5：将打乱后的内容写回新目录中的相应文件
for path, content in zip(new_loot_table_paths, loot_table_contents):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Completed. Loot tables have been randomized and copied to the new directory.")
