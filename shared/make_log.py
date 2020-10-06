from logging import basicConfig, getLogger, DEBUG, ERROR
import datetime
import traceback


class Log:
    def __init__(self, path):
        d = datetime.date.today().strftime("%Y%m%d")
        formatter = '%(levelname)s : %(asctime)s : %(message)s'
        # self.path = os.getcwd()
        # self.path = os.path.dirname(__file__)
        basicConfig(filename=f'{path}/log/logger_{d}.log', level=DEBUG, format=formatter)
        self.logger = getLogger(__name__)

    def debug_log(self, s):
        self.logger.setLevel(DEBUG)
        self.logger.debug(s)

    def error_log(self, s):
        self.logger.setLevel(ERROR)
        self.logger.error(s)

    def err(self, e):
        self.error_log(str(e))
        err_list = traceback.format_exc().split('\n')
        for er in err_list:
            self.error_log(er)
