import gradio as gr
import whisper
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

config = dotenv_values(".env")

ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]

def trasnlator(audio_file):
    # 1.Transcribe audio to text (whisper)
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language = "Spanish", fp16 = False)
        transcription = result["text"]
    except Exception as error:
        raise gr.Error(f"An error occurred during the transcription process: {str(error)}")
    
    print(f"Original text: {transcription}")

    # 2.Translate the text (translate)
    try:
        en_transcription = Translator(from_lang = "es", to_lang = "en").translate(transcription)
        it_transcription = Translator(from_lang = "es", to_lang = "it").translate(transcription)
        pt_transcription = Translator(from_lang = "es", to_lang = "pt").translate(transcription)
        ja_transcription = Translator(from_lang = "es", to_lang = "ja").translate(transcription)
    except Exception as error:
        raise gr.Error(f"An error occurred during the translation process: {str(error)}")

    print(f"Translated text to english: {en_transcription}") 
    print(f"Translated text to italian: {it_transcription}") 
    print(f"Translated text to portuguese: {pt_transcription}") 
    print(f"Translated text to japanese: {ja_transcription}")

    # 3. Generate audio from the translated text (elevenlabs)

    en_save_file_path = text_to_speach(en_transcription, "en")
    it_save_file_path = text_to_speach(it_transcription, "it")
    pt_save_file_path = text_to_speach(pt_transcription, "pt")
    ja_save_file_path = text_to_speach(ja_transcription, "ja")

    return en_save_file_path, it_save_file_path, pt_save_file_path, ja_save_file_path

# Function to generate audio in any language

def text_to_speach(text: str, language: str) -> str:    
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY,)
        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB", 
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2_5",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,        
            )
        )

        save_file_path = f"{language}.mp3"

        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)   

        return save_file_path
    
    except Exception as error:
        raise gr.Error(f"An error occurred during the generation process: {str(error)}")  


web = gr.Interface(
    fn = trasnlator,
    inputs = gr.Audio(
        sources = ["microphone"],
        type = "filepath",
        label = "Spanish"
    ),
    outputs = [
        gr.Audio(label = "English"),
        gr.Audio(label = "Italian"),
        gr.Audio(label = "Portuguese"),
        gr.Audio(label = "Japanese")
        ],
    title = "Voice translator",
    description = "AI-powered voice translator for multiple languages"
)

web.launch()