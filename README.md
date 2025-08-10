# 🎮 趣味小游戏 - Python APK项目

这是一个使用Python Kivy框架开发的简单有趣的手机游戏，可以通过GitHub Actions自动构建APK文件。

## 🎯 游戏功能

- **点击游戏**: 点击按钮获得随机分数
- **连续奖励**: 连续点击有额外奖励分数
- **实时计时**: 显示游戏进行时间
- **重置功能**: 随时重置游戏重新开始
- **美观界面**: 现代化的UI设计，支持中文

## 🚀 快速开始

### 方法1: GitHub Actions自动构建（推荐）

1. **Fork本项目**到你的GitHub账户
2. **推送代码**到main或master分支
3. **查看Actions**: 在GitHub仓库页面点击"Actions"标签
4. **等待构建完成**: 构建过程大约需要10-15分钟
5. **下载APK**: 构建完成后在Actions页面下载APK文件

### 方法2: 本地构建

#### 环境要求
- Python 3.9+
- Android SDK
- Android NDK
- Buildozer

#### 安装步骤
```bash
# 安装依赖
pip install -r requirements.txt

# 安装buildozer
pip install buildozer

# 构建APK
buildozer android debug
```

## 📱 安装说明

1. 在Android手机上启用"未知来源"应用安装
2. 下载APK文件到手机
3. 点击APK文件进行安装
4. 安装完成后即可运行游戏

## 🔧 技术架构

- **框架**: Kivy 2.2.1
- **语言**: Python 3.9
- **构建工具**: Buildozer
- **目标平台**: Android 5.0+ (API 21+)
- **架构支持**: ARM v7, ARM64

## 🛠️ 常见问题解决

### 构建失败问题

1. **SDK版本问题**: 确保使用Android API 31和NDK 23b
2. **依赖冲突**: 使用requirements.txt中的精确版本
3. **权限问题**: 确保GitHub Actions有足够权限

### 运行时问题

1. **闪退**: 检查Android版本是否支持（需要5.0+）
2. **权限**: 确保应用有必要的存储权限
3. **兼容性**: 测试不同品牌手机的兼容性

## 📁 项目结构

```
pk/
├── main.py              # 主程序文件
├── requirements.txt     # Python依赖
├── buildozer.spec      # Buildozer配置
├── .github/workflows/  # GitHub Actions工作流
│   └── build-apk.yml
└── README.md           # 项目说明
```

## 🎨 自定义修改

### 修改游戏逻辑
编辑 `main.py` 文件中的游戏逻辑

### 修改应用信息
编辑 `buildozer.spec` 文件中的应用配置

### 修改构建配置
编辑 `.github/workflows/build-apk.yml` 文件

## 📞 技术支持

如果遇到问题，请：

1. 检查GitHub Actions的构建日志
2. 查看常见问题解决方案
3. 提交Issue描述具体问题

## 📄 许可证

本项目采用MIT许可证，可自由使用和修改。

## 🎉 成功案例

使用此工作流成功构建的APK已在多个Android设备上测试通过，包括：
- Samsung Galaxy系列
- Xiaomi系列
- Huawei系列
- 其他Android 5.0+设备

---

**注意**: 首次构建可能需要较长时间，请耐心等待。构建成功后，后续构建会更快。
