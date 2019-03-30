import logging


class MyClass(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("package initialized")

    @staticmethod
    def get_5():
        return 5
