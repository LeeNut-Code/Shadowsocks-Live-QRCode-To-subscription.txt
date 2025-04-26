import cv2

class QRCodeReader:
    def decode_qr_code(self, image_path):
        """
        解码二维码图片，返回内容。
        """
        try:
            # 读取图像
            image = cv2.imread(image_path)
            if image is None:
                print(f"Failed to load image: {image_path}")
                return None

            # 初始化二维码检测器
            detector = cv2.QRCodeDetector()
            data, _, _ = detector.detectAndDecode(image)

            if data:
                return data
            else:
                print(f"No QR Code found in image: {image_path}")
                return None
        except Exception as e:
            print(f"Error decoding QR Code: {e}")
            return None