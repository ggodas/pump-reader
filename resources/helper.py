import os
import json
import logging
import logging.config
import logging.handlers
import sys


def config_logger(loader_path,
                  log_name='component',
                  configure_root=False,
                  root_level=logging.WARN,
                  max_files=5,
                  max_size=5242880):
    real_path = os.path.realpath(loader_path)
    if os.path.isdir(real_path):
        dir_path = real_path
    else:
        dir_path = os.path.dirname(real_path)

    filename = os.path.join(dir_path, log_name + '.log')

    formatter = logging.Formatter("%(asctime)-6s: %(name)s - %(levelname)s - "
                                  "%(thread)d - %(threadName)s - %(message)s")

    rotating_file_logger = logging.handlers.RotatingFileHandler(filename, 'a', max_size, max_files, encoding="utf-8")
    rotating_file_logger.setLevel(logging.DEBUG)  # DEBUG Log
    # rotating_file_logger.setLevel(logging.ERROR)  # Production Log
    rotating_file_logger.setFormatter(formatter)

    comp_logger = logging.getLogger(log_name)
    comp_logger.addHandler(rotating_file_logger)
    comp_logger.setLevel(logging.DEBUG)

    if configure_root:
        root_logger = logging.getLogger()
        root_logger.addHandler(rotating_file_logger)
        root_logger.setLevel(root_level)


def get_path(directory='', file_name_with_extension=''):
    # type: (str, str) -> str
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), directory, file_name_with_extension)


def read_json_from_file_as_dictionary(json_file_path):
    with open(json_file_path, 'rb') as content_file:
        complete_json = content_file.read()
        return json.loads(complete_json.decode("utf-8"))
