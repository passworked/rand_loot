# 随机掉落数据包

## 默认版本：1.20.2

> **注意：** 为了在其他版本中使用本数据包，您需要修改`pack.mcmeta`文件以及对应版本的战利品表。

## 使用方法

1. **下载release**：
   下载并解压文件后，运行 `rand.exe` 或者 `randlite.exe` 来打乱战利品表。
2. **执行随机化**：
   - **全随机模式**：运行 `rand.exe`，在这种模式下，铃兰的掉落物可能是末地城宝箱的战利品，但有许多物品可能无法正常获取。
   - **半随机模式**：运行`randlite.exe`，这种模式下方块绑定方块，实体绑定实体，结构绑定结构，基本上所有物品都能正常获取。

3. **安装数据包**：
   将生成的`rand_loot`文件夹整个拖拽进`./save/你的存档/datapacks/`目录下。

4. **激活数据包**：
   如果随机掉落没有生效，请在服务端或是客户端管理员键入`/reload`来重新载入数据包。

## 命令参考

- **启用数据包**：
  ```bash
  /datapack enable "file/rand_loot"
  ```
## Todo List

- [ ] 适配更多Minecraft版本，更新`pack.mcmeta`文件以支持至最新的游戏版本。
- [X] 打包python文件。
