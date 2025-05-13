# SmartLocal – Trợ lý ảo giọng nói realtime 🧠🔊

SmartLocal là một trợ lý ảo đơn giản tích hợp gRPC để nhận diện và tổng hợp giọng nói thời gian thực. Dự án này được viết hoàn toàn bằng Python, dễ dàng mở rộng và tích hợp thêm AI trả lời câu hỏi.

## 🎯 Tính năng

- 🎙 Nhận diện giọng nói thời gian thực (Realtime Speech-to-Text)
- 🗣 Tổng hợp giọng nói từ văn bản (Text-to-Speech)
- 📡 Giao tiếp client-server qua gRPC
- 🧠 Logic xử lý câu hỏi đơn giản, có thể tích hợp AI nâng cao
- 🌐 Giao diện web HTML đơn giản

## 🛠 Công nghệ sử dụng

- Python 3
- gRPC + Protobuf
- `pyttsx3`, `speech_recognition`, `flask`
- HTML (giao diện frontend)

## 📦 Cấu trúc thư mục

```
smartlocal/
├── app.py                  # Web server chính (Flask)
├── grpc_server.py          # gRPC server xử lý STT/TTS
├── grpc_client.py          # gRPC client
├── assistant.proto         # Định nghĩa protobuf
├── assistant_pb2.py        # File sinh ra từ protobuf
├── assistant_pb2_grpc.py   # File sinh ra từ protobuf
├── actions.py              # Các hành động phản hồi người dùng
├── logic.py                # Logic xử lý câu hỏi
├── tts.py                  # Tổng hợp giọng nói
├── templates/
│   └── index.html          # Giao diện người dùng
└── temp.mp3                # File âm thanh tạm thời
```

## 🚀 Hướng dẫn chạy

### 1. Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
```

> Nếu chưa có file `requirements.txt`, bạn có thể cài thủ công:
```bash
pip install grpcio grpcio-tools flask pyttsx3 speechrecognition
```

### 2. Tạo file protobuf

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. assistant.proto
```

### 3. Chạy gRPC server

```bash
python grpc_server.py
```

### 4. Chạy Flask Web App

```bash
python app.py
```

Sau đó mở trình duyệt tại: [http://localhost:8080](http://localhost:8080)

## 💬 Ví dụ

Bạn có thể nói:  
- "Mấy giờ rồi?"
- "Thời tiết hôm nay thế nào?"
- "Tạm biệt"

---

📌 Project phù hợp với mục đích học tập, demo tích hợp STT-TTS và gRPC realtime.
