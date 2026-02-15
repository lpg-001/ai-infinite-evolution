# GitHub推送指南

## 前置准备

1. **GitHub账号**：确保你已经有一个GitHub账号
2. **Git配置**：确保已经配置了Git用户信息

```bash
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱"
```

## 推送步骤

### 方法1：通过GitHub网页创建仓库（推荐）

1. **在GitHub上创建新仓库**
   - 访问 https://github.com/new
   - 仓库名称：`ai-infinite-evolution`（或你喜欢的名称）
   - 描述：`AI无限进化系统 - 让AI能够持续学习和进化的智能技能系统`
   - 选择 **Public** 或 **Private**
   - **不要**勾选"Initialize this repository with a README"（因为我们已经有了）
   - 点击"Create repository"

2. **连接本地仓库到GitHub**

```bash
# 添加远程仓库（将YOUR_USERNAME替换为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/ai-infinite-evolution.git

# 或者使用SSH（如果你配置了SSH密钥）
git remote add origin git@github.com:YOUR_USERNAME/ai-infinite-evolution.git
```

3. **推送代码**

```bash
# 推送主分支到GitHub
git push -u origin master

# 或者如果你的默认分支是main
git push -u origin main
```

### 方法2：使用GitHub CLI（如果已安装）

```bash
# 创建仓库并推送
gh repo create ai-infinite-evolution --public --source=. --remote=origin --push
```

### 方法3：手动设置远程仓库

如果你已经创建了GitHub仓库，直接连接：

```bash
# 查看当前远程仓库
git remote -v

# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/ai-infinite-evolution.git

# 推送代码
git push -u origin master
```

## 验证推送

推送成功后，访问你的GitHub仓库页面，应该能看到所有文件。

## 后续更新

以后每次更新代码后，使用以下命令推送：

```bash
# 添加更改
git add .

# 提交更改
git commit -m "更新说明"

# 推送到GitHub
git push
```

## 常见问题

### Q: 推送时提示需要认证？

A: 使用以下方法之一：
1. **使用Personal Access Token**（推荐）
   - 在GitHub设置中生成Token
   - 推送时使用Token作为密码

2. **使用SSH密钥**
   - 生成SSH密钥：`ssh-keygen -t ed25519 -C "your_email@example.com"`
   - 将公钥添加到GitHub账户

### Q: 推送时提示"remote origin already exists"？

A: 先删除现有远程仓库，再添加新的：

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/ai-infinite-evolution.git
```

### Q: 如何更改远程仓库地址？

A: 使用以下命令：

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/new-repo-name.git
```

## 仓库设置建议

推送成功后，建议在GitHub仓库设置中：

1. **添加仓库描述**：`AI无限进化系统 - 让AI能够持续学习和进化的智能技能系统`
2. **添加主题标签**：`ai` `cursor` `skill-system` `automation` `machine-learning`
3. **添加README徽章**：README.md中已经包含了徽章代码
4. **设置默认分支**：确保使用`main`或`master`作为默认分支
5. **启用Issues和Discussions**：方便用户反馈和讨论

## 完成！

推送成功后，你的AI无限进化系统就已经在GitHub上了！🎉

---

**提示**：记得在README.md中将`your-username`替换为你的实际GitHub用户名！