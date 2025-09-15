import subprocess
from pathlib import Path


def run_ffmpeg(args: list[str]) -> None:
    proc = subprocess.run(
        ["ffmpeg", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8")[:500])


def demux_to_wav(video: Path, wav: Path):
    run_ffmpeg(["-y", "-i", str(video), "-ac", "1", "-ar", "16000", str(wav)])


def mux_aac(video_in: Path, audio_in: Path, out_mp4: Path):
    run_ffmpeg(["-y", "-i", str(video_in), "-i", str(audio_in),
                "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", str(out_mp4)])
