# from pydub import AudioSegment
# import uuid
# import shutil

# import subprocess
# import json
# from pathlib import Path
# import os

# from typing import List, TypedDict
# import whisper

# from pathlib import Path
# from TTS.api import TTS
# _ttsmodel = None

# _model = None
# os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"


# def make_job_dir(root: str) -> Path:
#     job_id = str(uuid.uuid4())
#     p = Path(root) / job_id
#     p.mkdir(parents=True, exist_ok=True)
#     (p / "audio").mkdir(exist_ok=True)
#     (p / "video").mkdir(exist_ok=True)
#     (p / "subs").mkdir(exist_ok=True)
#     return p


# def cleanup_dir(p: Path):
#     if p.exists():
#         shutil.rmtree(p, ignore_errors=True)


# def run_ffmpeg(args: list[str]) -> None:
#     proc = subprocess.run(
#         ["ffmpeg", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     if proc.returncode != 0:
#         raise RuntimeError(proc.stderr.decode("utf-8")[:500])


# def demux_to_wav(video: Path, wav: Path):
#     run_ffmpeg(["-y", "-i", str(video), "-ac", "1", "-ar", "16000", str(wav)])


# def mux_aac(video_in: Path, audio_in: Path, out_mp4: Path):
#     run_ffmpeg(["-y", "-i", str(video_in), "-i", str(audio_in),
#                 "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", str(out_mp4)])


# def transcribe(wav_path: str, model_name: str):
#     global _model
#     if _model is None:
#         _model = whisper.load_model(model_name)
#     result = _model.transcribe(wav_path, task="translate", fp16=False)
#     # result already contains segments; return only needed fields
#     return {"text": result.get("text", ""), "segments": [
#         {"start": s["start"], "end": s["end"], "text": s["text"].strip()} for s in result.get("segments", [])
#     ]}


# def synthesize(text: str, speaker_ref: str, out_wav: Path, model_name: str):
#     global _ttsmodel
#     if _ttsmodel is None:
#         _ttsmodel = TTS(model_name)
#     # _ttsmodel.tts_to_file(text=text, speaker_wav=speaker_ref,
#     #                       language="en", file_path=str(out_wav))
#     _ttsmodel.tts_to_file(text=text, file_path=str(out_wav),
#                           speaker_wav=speaker_ref,
#                           language="en", split_sentences=True)


# # job_dir = make_job_dir("../data")
# # print(job_dir)
# # video_path = "../tests/videofile.mp4"
# # video_in = Path(video_path)
# # print(video_in)
# # wav_in = job_dir / "audio" / "original.wav"
# # print(wav_in)
# # demux_to_wav(video_in, wav_in)

# # asr = transcribe(str(wav_in), "medium")  # has "segments"
# # print(asr)

# asr = {'text': " What if, what if, laziness is a habit of thinking about the cost of things or the effort instead of thinking about the payoff? I'm going to say it again to get a few more heads to explode. What if laziness is nothing but a habit of thinking about the effort instead of thinking about the outcome? What if you could reverse laziness by simply developing a habit of thinking more about the, let's say, the delicious food that you would like to enjoy instead of how long it would take you to get up and go get it? So, but the real question is if you were to test this at home and try to see if you can think more about the good outcome and less about the work, would you get it done? Why is it that people have a second child? Why does a woman who goes through this awful, awful childbirth have a second child? Don't they always say the same thing? If I remembered how bad this was, I wouldn't do it again. Right? So the not thinking about the effort is vital to actually the survival of humanity. If we focused on how hard it was to have a baby, you just wouldn't do it or you do too little of it. But if you focus on how awesome it would be to have a family, well, there you go. You're going to go through the pain because you've already committed. Am I ambitious or do I simply have a thinking habit which produces dopamine because I'm thinking about the positive outcome and is the dopamine the thing that gets me up and moving? And when you're observing me, you say, how the hell do you get so much done? Right? And how do I do it? I think it's just this. I think it's just this. When I think of all the things I do, I think about them in terms of their benefits. So here's your tip. It's going to change some of your lives.", 'segments': [{'start': 0.0, 'end': 13.0, 'text': 'What if, what if, laziness is a habit of thinking about the cost of things or the effort instead of thinking about the payoff?'}, {'start': 13.0, 'end': 19.0, 'text': "I'm going to say it again to get a few more heads to explode."}, {
#     'start': 19.0, 'end': 30.0, 'text': 'What if laziness is nothing but a habit of thinking about the effort instead of thinking about the outcome?'}, {'start': 30.0, 'end': 44.0, 'text': "What if you could reverse laziness by simply developing a habit of thinking more about the, let's say, the delicious food that you would like to enjoy instead of how long it would take you to get up and go get it?"}, {'start': 44.0, 'end': 59.0, 'text': 'So, but the real question is if you were to test this at home and try to see if you can think more about the good outcome and less about the work, would you get it done?'}, {'start': 59.0, 'end': 69.0, 'text': 'Why is it that people have a second child? Why does a woman who goes through this awful, awful childbirth have a second child?'}, {'start': 69.0, 'end': 77.0, 'text': "Don't they always say the same thing? If I remembered how bad this was, I wouldn't do it again. Right?"}, {'start': 77.0, 'end': 90.0, 'text': "So the not thinking about the effort is vital to actually the survival of humanity. If we focused on how hard it was to have a baby, you just wouldn't do it or you do too little of it."}, {'start': 90.0, 'end': 100.0, 'text': "But if you focus on how awesome it would be to have a family, well, there you go. You're going to go through the pain because you've already committed."}, {'start': 100.0, 'end': 113.0, 'text': "Am I ambitious or do I simply have a thinking habit which produces dopamine because I'm thinking about the positive outcome and is the dopamine the thing that gets me up and moving?"}, {'start': 113.0, 'end': 123.0, 'text': "And when you're observing me, you say, how the hell do you get so much done? Right? And how do I do it? I think it's just this. I think it's just this."}, {'start': 123.0, 'end': 132.0, 'text': "When I think of all the things I do, I think about them in terms of their benefits. So here's your tip. It's going to change some of your lives."}]}


# job_dir = Path("../data/fdc33c09-773b-45bb-90e9-a388e405a6f2")
# # seg_wavs = []
# # for i, seg in enumerate(asr["segments"]):
# #     out_wav = job_dir / "audio" / f"seg_{i:03d}.wav"
# #     synthesize(seg["text"], str("../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/original.wav"), out_wav,
# #                "tts_models/multilingual/multi-dataset/xtts_v2")
# #     seg_wavs.append(out_wav)


# def stitch_segments(original_wav: Path, seg_wavs: List[Path], segments_meta) -> Path:
#     # naive initial version: simply concatenate TTS segments; later add gaps & atempo
#     out = AudioSegment.silent(duration=0)
#     for w in seg_wavs:
#         out += AudioSegment.from_wav(w)
#     target = original_wav.parent / "tts_concat.wav"
#     out.export(target, format="wav")
#     return target


# seg_wavs = [Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_000.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_001.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_002.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_003.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_004.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_005.wav'),
#             Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_006.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_007.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_008.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_009.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_010.wav'), Path('../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/seg_011.wav')]


# # tts_full = stitch_segments(Path(
# # "../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/original.wav"), seg_wavs, asr["segments"])

# video_path = "../tests/videofile.mp4"
# video_in = Path(video_path)
# tts_full = Path(
#     "../data/fdc33c09-773b-45bb-90e9-a388e405a6f2/audio/tts_concat.wav")
# final_mp4 = job_dir / "final.mp4"
# mux_aac(video_in, tts_full, final_mp4)


import subprocess
from pathlib import Path


def run_ffmpeg(args: list[str]) -> None:
    proc = subprocess.run(
        ["ffmpeg", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8")[:500])


def mux_aac(video_in: Path, audio_in: Path, out_mp4: Path):
    run_ffmpeg(["-y", "-i", str(video_in), "-i", str(audio_in),
                "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                "-shortest", str(out_mp4)])


video_in = Path("../../tests/videofile.mp4")
tts_full = Path(
    "../../data/31c2612e-cf81-4455-8801-af7f11049f53/audio/tts_concat.wav")
final_mp4 = Path("../../data/31c2612e-cf81-4455-8801-af7f11049f53/final.mp4")
mux_aac(video_in, tts_full, final_mp4)
