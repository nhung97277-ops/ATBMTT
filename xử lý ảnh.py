import pytesseract # type: ignore
from PIL import Image # type: ignore
class XuLyAnh:
    pytesseract.pytesseract.tesseract_cmd = r'E:\Program Files\Tesseract-OCR\tesseract.exe'
    @staticmethod
    def extract_text_from_image(image_path):
        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img, lang='vie')
            return text.strip() if text else "Không tìm thấy văn bản trong ảnh."
        except Exception as e:
            return f"Đã xảy ra lỗi khi xử lý ảnh: {e}"
