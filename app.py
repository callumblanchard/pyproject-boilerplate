# app.py

from lib.logtimer import log_time
from lib.loggerinit import logger_init

log = logger_init(__name__)


@log_time
def main():
    log.info("Hello, World!")


if __name__ == "__main__":
    main()
