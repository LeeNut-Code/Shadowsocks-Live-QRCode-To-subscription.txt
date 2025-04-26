# Shadowsocks Live QRCode To subscription.txt

## 项目简介

本项目旨在帮助用户在观看 YouTuber [不良林](https://www.youtube.com/@bulianglin) 的节点分享直播时，自动截取屏幕中的二维码，并生成一个名为 `shadowsocks_subscription.txt` 的文件，以便快速导入到 Shadowsocks 中，简化节点配置流程。

## 功能说明

1. **自动截屏**：程序运行后，每隔 1 分钟自动截取屏幕一次。
2. **二维码解码**：从截取的屏幕图片中提取二维码内容。
3. **生成订阅文件**：将解码后的 Shadowsocks 节点信息保存到 `shadowsocks_subscription.txt` 文件中。
4. **定时停止**：程序将在 30 分钟后自动停止截屏操作。

## 使用方法

1. 确保已安装以下依赖：
- Python 3.7 或更高版本
- 必要的 Python 库（如 `pyzbar`、`pillow` 等）
2. 克隆本项目到本地：
   ```bash
   git clone https://github.com/your-repo/shadowsocks-subscription-generator.git
   cd shadowsocks-subscription-generator
   ```
	>注意：程序路径不能有中文

3. 安装依赖

	```bash
	pip install -r requirements.txt
	```
4. 打开并观看直播，将浏览器的播放器置于屏幕中，运行脚本:
	```bash
	python start.py
	```
5. 程序运行后会自动截屏并生成 shadowsocks_subscription.txt 文件，文件内容可直接导入到 Shadowsocks 客户端。

## 注意事项
- 请确保运行脚本时，直播窗口处于屏幕可见范围内，且二维码清晰可见。
- 程序默认运行 30 分钟，您可以根据需要修改脚本中的运行时长。
- 如果二维码无法正确解码，请检查屏幕截图的清晰度或调整分辨率。

## 贡献
欢迎提交 Issue 或 Pull Request 来改进本项目。如果您有任何建议或问题，请随时与我们联系。

