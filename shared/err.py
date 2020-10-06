import linecache
import sys
import json

import shared.common as s_cmn
import shared.constant as const
import shared.w_log as w_log


class Err:

    def __init__(self):
        # 共通クラスの読み込み
        self.cmn = s_cmn.Common()
        # self.pmn = p_cmn.PDCommon()
        self.const = const.Constant()
        self.wl = w_log.Log()

        # 初期値
        self.log = ''
        with open(self.const.DIR_JSON_PASS, 'r', encoding=self.const.CSV_UNICODE_SIG) as f:
            self.lf = json.load(f)
        self.err_log = self.cmn.dir_end_check(self.lf['Dir']['DirLog']) + 'err.log'

    def print_ex(self, log_name='Error-main'):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        line_no = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, line_no, f.f_globals)
        e = 'Exception in ({}, Line {} "{}"): {}'.format(filename, line_no, line.strip(), exc_obj)
        self.log = log_name
        self.wl.err_log('---------------------------------------------------------------------------------', self.log)
        self.wl.err_log(e, self.log)
        # print('Exception in ({}, Line {} "{}"): {}'.format(filename, line_no, line.strip(), exc_obj))
