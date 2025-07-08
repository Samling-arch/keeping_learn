在Windows的Ubuntu(WSL)环境中访问E盘的方法：

1. **打开Ubuntu终端**
    
    - 在Windows中启动Ubuntu终端
2. **导航到E盘目录**
    
    ```bash
    cd /mnt/e/OB/pro
    ```
    
3. **启动Claude Code**
    
    ```bash
    claude
    ```
    

## 注意事项

- 在WSL中，Windows的驱动器通过 `/mnt/` 挂载
- E盘对应路径是 `/mnt/e/`
- 路径中的反斜杠 `\` 在Linux中要改为正斜杠 `/`
- 如果文件夹名包含空格，需要用引号包围或使用转义字符

## 完整命令序列

```bash
# 打开Ubuntu终端后执行
cd /mnt/e/OB/pro
claude
```

这样Claude Code就会在你的 `E:\OB\pro` 目录中启动，可以开始处理该目录下的代码项目了。