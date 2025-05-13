from datetime import datetime
from actions import handle_action

def handle_question(text):
    text = text.lower()
    now = datetime.now()

    need_close = any(kw in text for kw in ["đóng trình duyệt", "đóng lại", "đóng luôn", "thoát"])

    # Giờ
    if "mấy giờ" in text or "bây giờ là mấy giờ" in text:
        response = f"Bây giờ là {now.strftime('%H:%M')}"
    
    # Thời tiết
    elif "thời tiết" in text:
        response = "Tôi chưa có kết nối dữ liệu thời tiết. Nhưng tôi nghĩ trời đang đẹp!"

    # Mở Google
    elif "mở google" in text:
        handle_action("open_google")
        response = "Đang mở Google."

    elif "mở youtube" in text:
        handle_action("open_youtube")
        response = "Đang mở YouTube."

    elif "mở facebook" in text:
        handle_action("open_facebook")
        response = "Đang mở Facebook."

    elif "mở zalo" in text:
        handle_action("open_zalo")
        response = "Đang mở Zalo."

    else:
        response = "Tôi chưa hiểu câu hỏi, bạn có thể hỏi lại nhé."

    # 👉 Sau khi xử lý xong, nếu có yêu cầu đóng
    if need_close:
        handle_action("close_browser")
        response += " Tôi đã đóng trình duyệt theo yêu cầu."

    return response
