from mahoa import MaHoa
from giaima import GiaiMa
from nhandienamthanh import AmThanhToText
from nhandienhinhanh import XuLyAnh
def main():
    while True:
        print("\nChọn tác vụ:")
        print("1. Mã hóa văn bản")
        print("2. Giải mã văn bản")
        print("3. Chuyển âm thanh thành văn bản")
        print("4. Trích xuất văn bản từ ảnh")
        print("5. Thoát")
        choice = input("Nhập lựa chọn (1-5): ")
        if choice == "1":
            plaintext = input("Nhập dữ liệu cần mã hóa: ")
            key_phrase = input("Nhập mật khẩu: ")
            mahoa = MaHoa(key_phrase)
            cipher_b64, iv_b64 = mahoa.ma_hoa(plaintext)
            print("\nKẾT QUẢ MÃ HÓA:")
            print(f"Ciphertext (Base64): {cipher_b64}")
            print(f"IV (Base64): {iv_b64}")
        elif choice == "2":
            encrypted_data = input("Nhập chuỗi đã mã hóa (Base64): ")
            key_phrase = input("Nhập mật khẩu: ")
            iv_base64 = input("Nhập IV (Base64): ")
            decrypted_data = GiaiMa.decrypt(encrypted_data, key_phrase, iv_base64)
            print(f"\nDữ liệu sau giải mã: {decrypted_data}")
        elif choice == "3":
            am_thanh = AmThanhToText()
            am_thanh.chuyen_doi()
        elif choice == "4":
            image_path = input("Nhập đường dẫn tới ảnh: ")
            ket_qua = XuLyAnh.extract_text_from_image(image_path)
            print("Văn bản trích xuất từ ảnh:", ket_qua)
        elif choice == "5":
            print("Chương trình kết thúc.")
            break  # Thoát khỏi vòng lặp vô hạn
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
if __name__ == "__main__":
    main()
