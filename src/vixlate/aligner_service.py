from typing import List
from pathlib import Path
from pydub import AudioSegment


def stitch_segments(original_wav: Path, seg_wavs: List[Path], segments_meta) -> Path:
    # naive initial version: simply concatenate TTS segments; later add gaps & atempo
    out = AudioSegment.silent(duration=0)
    for w in seg_wavs:
        out += AudioSegment.from_wav(w)
    target = original_wav.parent / "tts_concat.wav"
    out.export(target, format="wav")
    return target
