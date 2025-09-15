from pathlib import Path
from TTS.api import TTS
_model = None


def synthesize(text: str, speaker_ref: str, out_wav: Path, model_name: str, to_lang: str):
    global _model
    if _model is None:
        _model = TTS(model_name)
    _model.tts_to_file(text=text, speaker_wav=speaker_ref,
                       language=to_lang, file_path=str(out_wav))
