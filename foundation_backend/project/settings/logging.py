FORMATTERS = {
    "standard": {
        "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
    },
}

HANDLERS = {
    'app_1': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': 'debug_app_1.log',
        'formatter': 'standard',
    },
    'app_2': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': './foundation_backend/log/debug_app_2.log',
        'formatter': 'standard',
    }
}

LOGGERS = {
    'app1': {
        'handlers': ['app_1'],
        'level': 'DEBUG',
        'propagate': False,
    },
    # Give name of loggers based on the module name
    'foundation_backend.project.urls': {
        'handlers': ['app_2'],
        'level': 'DEBUG',
        'propagate': False,
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    # how to format the output
    "formatters": FORMATTERS,
    # how to handle log messages
    "handlers": HANDLERS,
    # what do we want to log
    "loggers": LOGGERS,
    # "root": {
    #     "level": "DEBUG",
    #     "handlers": ["file"],
    # },
}
