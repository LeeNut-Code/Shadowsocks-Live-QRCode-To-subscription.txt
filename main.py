import os
from qr_reader import QRCodeReader
from shadowsocks_generator import ShadowsocksGenerator
import shutil

def move_to_desktop(item_name):
    """
    将指定的文件或目录移动到桌面，如果存在。
    """
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    item_path = os.path.join(os.getcwd(), item_name)
    if os.path.exists(item_path):
        try:
            destination = os.path.join(desktop_path, item_name)
            if os.path.exists(destination):
                # 如果目标已存在，先删除
                if os.path.isdir(destination):
                    shutil.rmtree(destination)
                else:
                    os.remove(destination)
            shutil.move(item_path, destination)
            print(f"Moved {item_name} to Desktop.")
        except Exception as e:
            print(f"Error moving {item_name} to Desktop: {e}")
    else:
        print(f"{item_name} does not exist, skipping.")

def main():
    # 创建二维码读取器和Shadowsocks生成器的实例
    qr_reader = QRCodeReader()
    shadowsocks_generator = ShadowsocksGenerator()

    # 指定存放二维码图片的文件夹路径
    qr_images_folder = "Screenshots"  # 替换为实际路径
    output_subscription_file = "shadowsocks_subscription.txt"

    # 扫描文件夹中的所有图片
    qr_contents = []
    for filename in os.listdir(qr_images_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(qr_images_folder, filename)
            qr_content = qr_reader.decode_qr_code(image_path)
            if qr_content:
                print(f"Decoded QR Code from {filename}: {qr_content}")
                qr_contents.append(qr_content)
            else:
                print(f"Failed to decode QR Code from {filename}.")

    # 生成Shadowsocks订阅文件
    if qr_contents:
        subscription_file = shadowsocks_generator.generate_subscription(qr_contents, output_subscription_file)
        print(f"Subscription file generated: {subscription_file}")
    else:
        print("No valid QR Codes found.")

    # 将 Screenshots 目录和 shadowsocks_subscription.txt 移动到桌面
    move_to_desktop("Screenshots")
    move_to_desktop("shadowsocks_subscription.txt")

if __name__ == "__main__":
    main()