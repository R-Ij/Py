#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shared.common as s_cmn
import shared.constant as const
import datetime
import qrcode
import json
from shared import w_log as wl
import shared.err as err


class MakeQR:

    def __init__(self, max_state=0, qr_dir='', main_oxn=None, main_xrn=None):
        # 共通クラスの読み込み
        self.cmn = s_cmn.Common()
        self.const = const.Constant()
        self.err = err.Err()

        # OpenPyXL
        self.main_oxn = main_oxn

        # xlrd
        self.main_xrn = main_xrn

        # 初期値
        self.log = 'MakeQR-'
        # log_name = self.log + 'init'

        # 保存先
        self.qr_dir = qr_dir

        # 最大作成数
        self.max_state = max_state
        # try:
        #     with open(self.const.DIR_JSON_PASS, 'r', encoding=self.const.CSV_UNICODE_SIG) as f:
        #         self.lf = json.load(f)
        #     self.qr_dir = self.cmn.dir_end_check(self.lf['Dir']['DirQR'])
        # except Exception as e:
        #     wl.Log().o_log(self.const.ERR_MESSAGE + str(e), log_name)
        #     self.err.print_ex(log_name)

    def make_qr(self, pr_cell, data_row, data_col, state_number=0):
        """
        QRコードを作成する関数
        :param   pr_cell: QRコードに変換するデータ
        :param   data_row:
        :param   data_col:
        :param   state_number:
        :return: 画像ファイル格納先(ファイル名含む)
        """
        log_name = self.log + 'make_qr'

        w_log = wl.Log()

        try:
            # 最大値に達した場合は終了する
            if state_number == self.max_state + 1:
                return True

            elif state_number == 1:
                # セルの値を取得するため、xrldでブックを開く
                with self.main_xrn.xlr_b() as xlb:

                    if xlb is None:
                        w_log.o_log(self.main_oxn.file_name + ':' + self.const.QR_WORKBOOK_ERR, log_name)
                        return False

                    # セルの値を取得
                    info = self.main_xrn.xlr_data_get(xl_row=state_number-1+data_row, xl_col=data_col)

                    # 画像添付のため、OpenPyXLでブックを開く
                    with self.main_oxn.oxl_b(del_flg=True) as wb:
                        if wb is None:
                            w_log.o_log(self.main_oxn.file_name + ':' + self.const.QR_WORKBOOK_ERR, log_name)
                            return False
                        if self.make_qr_sub(pr_cell, data_row, data_col, state_number, info, w_log):
                            self.make_qr(pr_cell, data_row, data_col, state_number + 1)
                        else:
                            return False
            else:
                info = self.main_xrn.xlr_data_get(xl_row=state_number-1+data_row, xl_col=data_col)

                if self.make_qr_sub(pr_cell, data_row, data_col, state_number, info, w_log):
                    self.make_qr(pr_cell, data_row, data_col, state_number + 1)
                else:
                    return False

            return True

        #     img = qrcode.make(info)
        #     full_pass = self.qr_dir + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '_qr.png'
        #
        #     img.save(full_pass)
        #     return full_pass
        #
        except Exception as e:
            wl.Log().o_log(self.const.ERR_MESSAGE + str(e), log_name)
            self.err.print_ex(log_name)
            return ''

    def make_qr_sub(self, pr_cell_sub, data_row_sub, data_col_sub, state_number_sub,
                    info_sub, w_log_sub=wl.Log()):

        log_name = self.log + 'make_qr_sub'

        try:

            if info_sub != '':
                img = qrcode.make(info_sub.encode('shift_jis'))
                full_path = self.qr_dir + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '_qr.png'

                img.save(full_path)

                if full_path != '':
                    self.main_oxn.work_cell = pr_cell_sub[state_number_sub - 1]

                if self.main_oxn.xl_print():
                    # ログを書く
                    pass
                else:
                    # ログを書く
                    return False
            else:
                self.make_qr(pr_cell_sub, data_row_sub, data_col_sub, state_number_sub + 1)

            return True

        except Exception as e:
            wl.Log().o_log(self.const.ERR_MESSAGE + str(e), log_name)
            self.err.print_ex(log_name)
            return ''


if __name__ == '__main__':
    # 単体確認用
    qr = MakeQR().make_qr('https://www.yahoo.co.jp/')
    print(qr)
