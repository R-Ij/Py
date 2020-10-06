#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import shared.pd_common as p_cmn
import shared.common as s_cmn
# import shared.w_log as w_log


class CSVMake:

    def __init__(self):
        # 共通クラスの読み込み
        self.cmn = s_cmn.Common()
        self.pmn = p_cmn.PDCommon()
        # self.wl = w_log.Log()

        # ログ用
        self.cls_name = 'CSVMake-'
        self.log_name = self.cls_name + 'main'

        # csvファイル生成用
        self.csv_encoding = 'SHIFT-JIS'         # 文字コード
        self.csv_index = False                  # 行連番の要否
        self.csv_header = False                 # 列連番の要否
        self.csv_quote = '"'                    # 値を囲む文字列
        self.csv_quoting = csv.QUOTE_ALL        # クォーティング方針
        self.temp_pass = r'C:\Py_Project\test\IF債務者情報ファイル.csv'
        self.save_pass = r'C:\Py_Project\test\make\IF債務者情報ファイル.csv'

        # self.wl.o_log('----------------------------------------------------------------------------------',
        #               self.log_name)

    def csv_make_cd_remove(self, csv_ax, csv_col_dex, csv_head=None):
        """
        指定の列、または行を削除したcsvファイルを再出力する
        :param csv_ax: 行:0 列:1
        :param csv_col_dex:
        :param csv_head:
        :return:
        """
        main_pmn = self.pmn
        main_pmn.csv_pass = self.temp_pass
        main_pmn.csv_header = csv_head
        main_pmn.csv_encode = self.csv_encoding
        df = main_pmn.r_csv()
        cm = main_pmn.pd_remove_cd(df, csv_ax, csv_col_dex)
        cm.to_csv(self.save_pass, encoding=self.csv_encoding, index=self.csv_index, header=self.csv_header,
                  quotechar=self.csv_quote, quoting=self.csv_quoting)


if __name__ == '__main__':

    C = CSVMake()

    try:
        C.csv_quoting = csv.QUOTE_MINIMAL
        C.csv_make_cd_remove(1, [31], None)
        print('OK')
    except Exception as e:
        print(str(e))

