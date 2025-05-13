import assistant_pb2
import assistant_pb2_grpc
import grpc
import pyaudio

def send_audio_to_grpc():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, frames_per_buffer=CHUNK)

    def audio_stream():
        for _ in range(60):  # ~4 giây
            data = stream.read(CHUNK)
            yield assistant_pb2.VoiceRequest(audio_chunk=data)

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = assistant_pb2_grpc.VoiceAssistantStub(channel)
        responses = stub.Converse(audio_stream())

        for res in responses:
            if res.text:
                stream.stop_stream()
                stream.close()
                p.terminate()
                return res.text
