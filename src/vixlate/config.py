from pydantic import BaseModel
import os


class Settings(BaseModel):
    storage_root: str = os.getenv("VIXLATE_STORAGE_ROOT", "./data")
    whisper_model: str = os.getenv("VIXLATE_WHISPER_MODEL", "medium")
    tts_model: str = os.getenv(
        "VIXLATE_TTS_MODEL", "tts_models/multilingual/multi-dataset/xtts_v2")
    redis_url: str = os.getenv("VIXLATE_REDIS_URL", "redis://localhost:6379/0")


settings = Settings()
