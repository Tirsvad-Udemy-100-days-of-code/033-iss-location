"""@brief Allows running the notifier with python -m iss_notifier."""

import sys

from iss_notifier.presentation.cli import main

if __name__ == "__main__":
    sys.exit(main())
