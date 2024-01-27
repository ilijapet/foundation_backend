from foundation_backend.utils_fun.collections import deep_update
from foundation_backend.utils_fun.get_seetings_from_env import get_settings_from_environment

# import environ

# env_file = os.path.join(BASE_DIR, ".env")  # type: ignore
# env = environ.Env()
# env.read_env(env_file)

# if os.path.isfile(env_file):
#     # read a local .env file
#     env.read_env(env_file)
#     POSTGRES_PASSWORD = env("POSTGRES_PASSWORD")
#     POSTGRES_USER = env("POSTGRES_USER")
#     ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")
# else:
#     raise ValueError("We cannot find .env file")

# System environment variables
# 1) With globals() we are picking up all python globals == base_dict from
# deep_update # function
#
# 2) With get_settings_from_environment function we are picking up all envvars,
# checking if they start with BACKENDSETTINGS_
#
# 2.1) If yes then convert to string via misc.py function yaml_coerce and
# assigne to == update_with from deep_update function
#
# 3) Now when we have existing setting variables and the one that developers
# added to envvars we can update existing settings with new ones and on
# this way overwrite (but just in local dev context) existing settings.
#
# On this way we can overwrite production with local allowing devlopers
# to change settings on local machine without influencing production settings
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore
