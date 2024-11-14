from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATETIME = datetime.now().strftime("%d-%b-%y %H%M%S")

CAPTURE_DIR = Path.joinpath(BASE_DIR / "captures")
TEMP_DIR = Path.joinpath(CAPTURE_DIR / f"temp_{DATETIME}")
VIDEO_DIR = Path.joinpath(TEMP_DIR / "video")
TRACE_ZIP = Path.joinpath(TEMP_DIR, "trace.zip")

SLOW_MO_TIME = 5000
BROWSER_LAUNCH_TIMEOUT = 50000

HEADLESS = False
WINDOW_SIZE = {"width": 1920, "height": 1080}
