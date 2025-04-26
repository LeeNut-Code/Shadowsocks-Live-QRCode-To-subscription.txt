import json

class ShadowsocksGenerator:
    def generate_subscription(self, qr_contents, output_file):
        """
        根据二维码内容生成Shadowsocks订阅文件。
        """
        try:
            # 将二维码内容写入订阅文件
            with open(output_file, 'w', encoding='utf-8') as f:
                for content in qr_contents:
                    f.write(content + '\n')
            return output_file
        except Exception as e:
            print(f"Error generating subscription file: {e}")
            return None