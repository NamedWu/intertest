import requests
import readConfig as readConfig
from common.log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.json = {}
        self.url = None
        self.files = {}
        self.session = requests.session()

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    def set_json(self, json):
        self.json = json

    # defined http get method
    def get(self):
        try:
            res = self.session.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return res
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            res = self.session.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            # response.raise_for_status()
            return res
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def put(self):
        try:
            if self.json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = self.json.dumps(self.json)
            res = self.session.get(self.url, data=self.data, timeout=float(timeout))
            # response.raise_for_status()
            return res
        except TimeoutError:
            self.logger.error("Time out!")
            return None