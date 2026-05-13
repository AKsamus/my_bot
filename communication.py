import pyttsx3
import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer


class Communication():
    def __init__(self, vosk_model_path="vosk-model-small-en-in-0.4"):
        self.command_type = 'Communication'
        # 🔊 Speech engine (pyttsx3)
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)

        # 🎧 Vosk speech recognizer
        self.model = Model(vosk_model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        # warm-up to avoid first word drop
        self.engine.say("ready")
        self.engine.runAndWait()


        # audio buffer
        self.audio_queue = queue.Queue()

    # ---------------------------
    # 🔊 SPEAKING
    # ---------------------------
    def speak(self, text: str):
        print(f"🤖 Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    # ---------------------------
    # 🎧 LISTENING (blocking)
    # ---------------------------
    def _audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.audio_queue.put(bytes(indata))

    def listen(self, subject):              #subject is command_type class e.g. mode, mobility
        print("🎧 Listening...")
        
        methods = ', '.join([
                    method_s for method_s in dir(subject)
                    if callable(getattr(subject, method_s)) and not method_s.startswith("__")
                    ])

        self.speak('Please use following commands, '+methods)

        with sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self._audio_callback,
        ):

            while True:
                data = self.audio_queue.get()

                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "")
                    print(f'you said 🔊: {text}')
                    if text:
                        if 'exit' in text:
                            self.speak('Ok, bye.')
                            return None
                        method = getattr(subject, text, None)
                        if callable(method):
                            self.speak(method.__name__+', got it.')
                            #return class only for mode
                            if subject.repeatable:
                                pass
                            else:
                                return method()
                        else:
                            self.speak('Command does not exist. Please one of the mentioned commands '+methods)


