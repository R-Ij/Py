#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from contextlib import contextmanager
import shutil
import xlrd
from shared import w_log as wl
from shared import common as s_cmn
import shared.constant as const
import shared.err as err


class XLCommon:

    def __init__(self):
        self.cls_name = 'XLr-'

        # Excelテンプレートパス(デフォルト)
        self.file_path = ''
        self.file_name = ''
        self.tmp_path = ''
        self.save_path = ''
        self.dt_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

        # ブックの値(デフォルト)
        self.workbook = None
        self.worksheet = None
        self.work_cell = 'A1'

        # 画像のサイズ
        self.img_size = 280

        self.cmn = s_cmn.Common()
        self.const = const.Constant()
        self.err = err.Err()

    @contextmanager
    def xlr_b(self):
        """
        xlrdでExcelブックをコピーして開く関数(クローズも含む)
        :yield: workbook
        """
        log_name = self.cls_name + 'xlr_b'
        full_path = self.cmn.dir_end_check(self.file_path) + self.file_name

        try:
            shutil.copy(full_path, self.tmp_path)
            self.workbook = xlrd.open_workbook(full_path)
            yield self.workbook

            if self.workbook is not None:
                del self.workbook

        except Exception as e:
            wl.Log().o_log(self.const.ERR_MESSAGE + str(e), log_name)
            self.err.print_ex(log_name)
            return False

    def xlr_n_sheet_get(self):
        """
        xlrdでシート数を取得する関数
        """
        if self.workbook is not None:
            return self.workbook.nsheets
        else:
            return 0

    def xlr_data_get(self, xl_row=1, xl_col=1):
        """
        xlrdでセルの値を取得する関数(数式の値も取得する)
        :param xl_row: 行
        :param xl_col: 列
        :yield: セルの値
        """
        log_name = self.cls_name + 'xlr_data_get'
        try:
            wb = self.workbook
            if wb is not None:
                if type(self.worksheet) is str:
                    ws = wb.sheet_by_name(self.worksheet)
                elif type(self.worksheet) is int:
                    ws = wb.sheet_by_index(self.worksheet)
                else:
                    ws = wb.sheet_by_index(0)
            else:
                # シートの指定がない場合は、先頭のシートを参照する
                ws = wb.sheet_by_index(0)

            # 0スタートのため、-1の補正をかける
            wc = ws.cell(xl_row - 1, xl_col - 1)
            return wc.value

        except Exception as e:
            wl.Log().o_log(self.const.ERR_MESSAGE + str(e), log_name)
            self.err.print_ex(log_name)
            return ''

    def xlr_get_sheet_name(self):
        """
        xlrdでシート名を一覧で取得する関数
        """
        if self.workbook is not None:
            for name in self.workbook.sheet_names():
                yield name
        else:
            return None


if __name__ == '__main__':
    xl = XLCommon()
    # print(xl.xlr_data_get(row=3, col=6))

