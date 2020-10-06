#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import shared.common as s_cmn


class Log:
    def __init__(self):
        self.cmn = s_cmn.Common()
        with open('json/dir.json', 'r', encoding='utf-8_sig') as e:
            # lf = json.load(e)
            lf = json.load(e)
        self.ok_log = self.cmn.dir_end_check(lf['Dir']['DirLog']) + 'app.log'
        self.e_log = self.cmn.dir_end_check(lf['Dir']['DirLog']) + 'err.log'

    def err_log(self, w_val, def_name):
        dt_now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        with open(self.e_log, mode='a') as f:
            f.write(str(w_val) + ' / ' + def_name + ': ' + dt_now + '\n')

    def o_log(self, w_val, def_name):
        dt_now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        with open(self.ok_log, mode='a') as f:
            f.write(str(w_val) + ' / ' + def_name + ': ' + dt_now + '\n')
