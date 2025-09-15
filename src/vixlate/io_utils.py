from pathlib import Path
import uuid
import shutil


def make_job_dir(root: str) -> Path:
    job_id = str(uuid.uuid4())
    p = Path(root) / job_id
    p.mkdir(parents=True, exist_ok=True)
    (p / "audio").mkdir(exist_ok=True)
    (p / "video").mkdir(exist_ok=True)
    (p / "subs").mkdir(exist_ok=True)
    return p


def cleanup_dir(p: Path):
    if p.exists():
        shutil.rmtree(p, ignore_errors=True)
