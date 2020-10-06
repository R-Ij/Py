#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Constant:

    def __init__(self):
        self.QR_ATTACH_ERR = 'QRコード貼り付け処理失敗。'
        self.QR_MAKE_ERR = 'QRコード作成に失敗しました。'
        self.QR_MAKE_MSG_FILE = 'ファイル目-'
        self.QR_MAKE_MSG_END = 'QRコード貼付、正常終了。'
        self.QR_VALUE_ERR = '値が取得できません。'
        self.LOG_START = '----------------------------------------------------------------------------------'
        self.QR_MAKE_START = 'QRコード作成処理開始。'

        self.CSV_SHIFT = 'SHIFT-JIS'
        self.CSV_CP932 = 'CP932'
        self.CSV_UNICODE_SIG = 'utf-8_sig'
        self.CSV_VALUE_ERR = '値が取得できません。'

        self.SUCCESSFUL_COMPLETION = '処理が正常終了しました。'

        self.ERR_MESSAGE = 'エラーが検出されました。：'

        self.DIR_JSON_PASS = 'json/dir.json'
