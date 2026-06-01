import sys
from pathlib import Path

# use pytest always

# /py route.exe/ -m pytest tests/test_gates.py

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.ui.main_window import MainWindow


def main():

    app = MainWindow()

    app.mainloop()


if __name__ == "__main__":
    main()