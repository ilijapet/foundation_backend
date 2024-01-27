from pathlib import Path

import environ
from split_settings.tools import include, optional

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Namsapacing our custom environment variables
ENVVAR_SETTINGS_PREFIX = 'BACKENDSETTINGS_'

LOCAL_SETTINGS_PATH = str(BASE_DIR / "local/settings.dev.py")

include(
    'base.py',
    # "logging.py",
    # Here wew are loading our local settings to override the base settings
    # Each developer can have his own local settings
    optional(LOCAL_SETTINGS_PATH),
    # Here we are loading our environment settings to override the base settings
    "envvars.py",
)
