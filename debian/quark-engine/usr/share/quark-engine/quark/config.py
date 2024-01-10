# -*- coding: utf-8 -*-
# This file is part of Quark-Engine - https://github.com/quark-engine/quark-engine
# See the file 'LICENSE' for copying permission.

from pathlib import Path

HOME_DIR = f"{Path.home()}/.quark-engine/"
SOURCE = "https://github.com/quark-engine/quark-rules"
DIR_PATH = f"{HOME_DIR}quark-rules/rules"

DEBUG = False

Path(HOME_DIR).mkdir(parents=True, exist_ok=True)
