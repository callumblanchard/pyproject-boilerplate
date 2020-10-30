import logging
import os.path


def logger_init(name):
    log_dir = os.environ.get("LOG_DIR", "log")
    log_file_name = os.environ.get("LOG_FILE_NAME", "logfile.log")
    log_date_fmt = os.environ.get("LOG_DATE_FMT", "%H:%M:%S")

    assert os.path.exists(log_dir)

    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
        level=logging.DEBUG,
        datefmt=log_date_fmt,
        filename=os.path.join(log_dir, log_file_name),
    )

    logging.getLogger("chardet.charsetprober").disabled = True

    return logging.getLogger(name)
