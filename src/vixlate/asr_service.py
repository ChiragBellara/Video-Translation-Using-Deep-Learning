from typing import List, TypedDict
import whisper


class Segment(TypedDict):
    start: float
    end: float
    text: str


class ASRResult(TypedDict):
    text: str
    segments: List[Segment]


_model = None


def transcribe(wav_path: str, model_name: str) -> ASRResult:
    global _model
    if _model is None:
        _model = whisper.load_model(model_name)
    result = _model.transcribe(wav_path, task="translate")
    # result already contains segments; return only needed fields
    return {"text": result.get("text", ""), "segments": [
        {"start": s["start"], "end": s["end"], "text": s["text"].strip()} for s in result.get("segments", [])
    ]}
