import grpc
from concurrent import futures
import assistant_pb2
import assistant_pb2_grpc
import speech_recognition as sr
import wave
import os

class AssistantService(assistant_pb2_grpc.VoiceAssistantServicer):
    def Converse(self, request_iterator, context):
        recognizer = sr.Recognizer()
        audio_data = b''

        print("🎧 Server đang nhận audio từ client...")

        for i, request in enumerate(request_iterator):
            audio_data += request.audio_chunk
            print(f"📥 Nhận chunk {i + 1} ({len(request.audio_chunk)} bytes)")

        # Ghi ra file WAV chuẩn để nhận diện
        try:
            with wave.open("temp.wav", "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)  # 16-bit PCM → 2 bytes
                wf.setframerate(16000)
                wf.writeframes(audio_data)

            print("📦 Đang nhận diện giọng nói...")
            with sr.AudioFile("temp.wav") as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language="vi-VN")
                print("✅ Nhận diện:", text)

                yield assistant_pb2.VoiceResponse(
                    text=text,
                    lang="vi",
                    action=detect_action(text)
                )

        except Exception as e:
            print("❌ Lỗi nhận diện:", e)
            yield assistant_pb2.VoiceResponse(
                text="Không nhận diện được.",
                lang="vi",
                action=""
            )

        # Xoá file tạm
        if os.path.exists("temp.wav"):
            os.remove("temp.wav")

def detect_action(text):
    text = text.lower()
    if "google" in text: return "open_google"
    if "facebook" in text: return "open_facebook"
    if "youtube" in text: return "open_youtube"
    if "zalo" in text: return "open_zalo"
    if "đóng" in text or "close" in text: return "close_browser"
    return ""

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    assistant_pb2_grpc.add_VoiceAssistantServicer_to_server(AssistantService(), server)
    server.add_insecure_port('[::]:50051')
    print("🚀 gRPC Server đang chạy tại cổng 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
