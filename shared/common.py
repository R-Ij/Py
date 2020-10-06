#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import re
import os


def dir_end_check(dir_n):
    """
    パスの末尾に'\'を付与する
    :param   dir_n: パス
    :return: 末尾に"\"を付与したパス
    """
    if dir_n[-1] != '\\':
        return dir_n + '\\'
    else:
        return dir_n


def dir_end_check2(dir_n):
    """
    パスの末尾に'/'を付与する
    :param   dir_n: パス
    :return: 末尾に"\"を付与したパス
    """
    if dir_n[-1] != '/':
        return dir_n + '/'
    else:
        return dir_n


def file_list(**kwargs):
    """
    フォルダ内のファイル名一覧を取得する

    Parameters:
        kwargs:
            dir: str
                ディレクトリ
            extension: str
                取得条件(拡張子)

    Returns:
        file_name: list
            ファイル一覧
    """
    # if os.name == 'nt':
    #     file_name = [os.path.basename(p) for p in glob.glob(kwargs['dir'] + '**', recursive=True)
    #                  if re.search(kwargs['extension'], p)]
    # elif os.name == 'posix':
    #     file_name = [os.path.basename(p) for p in glob.glob(kwargs['dir'] + '**', recursive=True)
    #                  if os.path.isfile(p)]
    # else:
    #     file_name = ''
    file_name = [os.path.basename(p) for p in glob.glob(kwargs['dir'] + '/*', recursive=True)
                 if re.search(kwargs['extension'], p)]

    return list(filter(lambda s: s != '', file_name))


def re_post(po_number):
    """
    郵便番号を正規表現で抽出する
    :param po_number: 郵便番号
    :return: xxx-xxxx
    """
    match = re.search('[0-9]{3}-[0-9]{4}', po_number)
    if match:
        return match.group(0)


def re_phone(ph_number):
    """
    郵便番号を正規表現で抽出する
    :param ph_number: 電話番号
    :return: xxx(xx, xxxx)-xxxx(xxx)-xxxx
    """
    if len(ph_number) in [12, 13]:
        ph_reg = re.compile(r'''(
            (\d{2,4})
            -
            (\d{2,4})
            -
            (\d{4}))''', re.VERBOSE)
        match = ph_reg.search(ph_number)
        if match:
            return match.group(0)


def file_remove(r_dir, r_ext):
    """
    フォルダ内の指定拡張子のファイルを削除する関数
    :param r_dir:
    :param r_ext:
    :return:
    """
    qr_pass = dir_end_check(r_dir)
    qr_list = file_list(dir=qr_pass, extension=r_ext)
    for qr_file in qr_list:
        os.remove(qr_pass + qr_file)
    return True


if __name__ == '__main__':
    print(file_list(dir=r'./', extension='.py'))
    # print(cmn.re_post('775-1122'))
    # print(re_phone('0803-34-5678'))
