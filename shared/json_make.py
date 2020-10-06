#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import codecs

dic = {
    'Dir': {
        'Explanation': 'ディレクトリ(パス)',
        'DirQR': r'C:\Users\iijima\Desktop\資料\qr\確認\make_qr',
        'DirLog': r'C:\Users\iijima\Desktop\資料\qr\確認\log',
        'DirFile': r'C:\Users\iijima\Desktop\資料\qr\確認\data',
        'DirSave': r'C:\Users\iijima\Desktop\資料\qr\確認\make_file'
    },
    'File': {
        'Explanation': 'ファイル名',
        'DataFile': 'book1.xlsx'
    },
    'Worksheet': {
        'Explanation': 'シート名',
        'Data': 'sheet1'
    },
    'Cell': {
        'Explanation': 'セル',
        'DataRow': 3,
        'DataCol': 6,
        'PrintCell': 'F5'
    }

}

if __name__ == '__main__':
    with codecs.open(r'C:\Py_root\qr\json\dir.json', 'w', 'utf-8') as f:
        dump = json.dumps(dic, indent=4, ensure_ascii=False)
        f.write(dump)
