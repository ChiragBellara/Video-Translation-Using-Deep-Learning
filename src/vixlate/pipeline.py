from pathlib import Path
from .config import settings
from .io_utils import make_job_dir, cleanup_dir
from .ffmpeg_utils import demux_to_wav, mux_aac
from .asr_service import transcribe
from .tts_service import synthesize
from .aligner_service import stitch_segments


def run_pipeline(video_path: str, to_lang: str) -> dict:
    job_dir = make_job_dir(settings.storage_root)
    try:
        video_in = Path(video_path)
        wav_in = job_dir / "audio" / "original.wav"
        demux_to_wav(video_in, wav_in)

        asr = transcribe(str(wav_in), settings.whisper_model)
        seg_wavs = []
        for i, seg in enumerate(asr["segments"]):
            out_wav = job_dir / "audio" / f"seg_{i:03d}.wav"
            synthesize(seg["text"], str(wav_in), out_wav,
                       settings.tts_model, to_lang)
            seg_wavs.append(out_wav)

        tts_full = stitch_segments(wav_in, seg_wavs, asr["segments"], )
        final_mp4 = job_dir / "final.mp4"
        mux_aac(video_in, tts_full, final_mp4)

        return {"status": "succeeded", "job_dir": str(job_dir), "final": str(final_mp4)}
    except Exception as e:
        return {"status": "failed", "error": str(e), "job_dir": str(job_dir)}
