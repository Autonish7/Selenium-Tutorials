import logging
logging.basicConfig(filename=r"C:\Users\U6033331\Desktop\test.log",
                    format= '%(asctime)s: %(levelname)s : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

# logging.debug("This is debug message")  # Not critical to print in console
# logging.info("This is info message")  # Not critical to print in console
# logging.critical("This is critical message")
# logging.error("This is error message")
# logging.warning("This is warning message")

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")  # Not critical to print in console
logger.info("This is info message")  # Not critical to print in console
logger.critical("This is critical message")
logger.error("This is error message")
logger.warning("This is warning message")
