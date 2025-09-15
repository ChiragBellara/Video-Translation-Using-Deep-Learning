from vixlate.pipeline import run_pipeline
from pathlib import Path
import os

os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"

if __name__ == "__main__":
    print(run_pipeline(str(Path("tests/Video-878.mp4")), "en"))
