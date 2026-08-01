"""Locate Project Root
        │
        ▼
Expose Common Directories
        │
        ▼
Framework imports these constants"""
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
#print(PROJECT_ROOT)
CONFIG_DIR = PROJECT_ROOT / "config"
LOG_DIR = PROJECT_ROOT / "logs"
REPORT_DIR = PROJECT_ROOT / "reports"
TESTS_DIR = PROJECT_ROOT / "tests"