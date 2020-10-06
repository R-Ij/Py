#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import glob
# import re
# import os
import numpy as np
import pandas as pd


class PDCommon:
    def __init__(self):
        self.cls_name = 'PDCommon-'
        self.csv_path = ''              # csvファイルのフルパス
        self.csv_header = None          # ヘッダーの位置
        self.csv_header_name = None     # 任意で設定するヘッダー名
        self.csv_index = None           # indexの位置
        self.csv_col = None             # 指定する列または行(リスト)
        self.del_col = None             # 指定しない列(リスト)
        self.skip_row = None            # 指定しない行(数値の場合は先頭からの行数、リストの場合は位置指定)
        self.ch_row = None              # 指定する行(リスト)
        self.csv_rows = None            # 最初の指定数行読み込み
        self.csv_encode = None          # 文字コード
        self.csv_d_type = 'object'      # 要素の型指定(デフォルトでは"01"など、先頭の0を取り込む)

    def r_csv(self):
        """
        csvファイルをpandasで読み込む関数
        :return:
        """
        csv_header = self.csv_header - 1 if self.csv_header is not None else None
        csv_header_name = self.csv_header_name if self.csv_header_name is not None else None
        csv_index = self.csv_index - 1 if self.csv_index is not None else None
        csv_col = self.csv_col if self.csv_col is not None else None
        ch_row = self.ch_row if self.ch_row is not None else None
        skip_row = self.skip_row if self.skip_row is not None else None
        csv_rows = self.csv_rows if self.csv_rows is not None else None
        csv_d_type = self.csv_d_type if self.csv_d_type is not None else 'object'

        if ch_row is not None:
            df = pd.read_csv(self.csv_path, index_col=csv_index, header=csv_header,
                             names=csv_header_name, usecols=csv_col,
                             skiprows=lambda x: x not in ch_row, nrows=csv_rows,
                             encoding=self.csv_encode, dtype=csv_d_type)
        else:
            df = pd.read_csv(self.csv_path, index_col=csv_index, header=csv_header,
                             names=csv_header_name, usecols=csv_col, skiprows=skip_row, nrows=csv_rows,
                             encoding=self.csv_encode, dtype=csv_d_type)
        return df

    @staticmethod
    def rd_sample(rd_csv, rd_n=0, rd_ax=0):
        """
        ランダムサンプリング関数
        :param rd_csv: 取得したcsv
        :param rd_n:
        :param rd_ax:
        :return:
        """
        spl = rd_csv.head().sample(n=rd_n, axis=rd_ax)
        return spl

    def idx(self, rd_csv, rd_col, m='max', rd_head=None):
        """
        指定した列の最小、または最大の値を含む行を抽出
        :param rd_csv:  取得したcsv
        :param rd_col:  最大、または最小を求める列
        :param m:       最大、または最小
        :param rd_head: ヘッダーの位置
        :return: 算出した行
        """
        if m == 'max':
            spl = rd_csv[rd_col].idxmax()
        elif m == 'min':
            spl = rd_csv[rd_col].idxmin()
        else:
            spl = None

        if spl is not None:
            self.csv_rows = None
            self.del_col = None
            self.csv_header = rd_head
            if rd_head is not None:
                if type(spl) is list:
                    # spl = [i + 1 for i in spl]                  # 行番号を直感的な値にする(1を加算)
                    spl = np.array(spl) + 1                     # numpyの配列に変換
                    spl = spl.tolist()                          # 通常のリストに変換
                    self.ch_row = spl.insert(0, rd_head - 1)    # ヘッダーを先頭に追加
                else:
                    spl += 1                                    # 行番号を直感的な値にする(1を加算)
                    self.ch_row = [rd_head - 1, spl]            # ヘッダーを先頭に追加してリスト化
            else:
                # ヘッダーなし
                self.ch_row = spl
            return self.r_csv()

    @staticmethod
    def any_ch(rd_csv, rd_col, a_val, port=False):
        """
        指定の列に、任意の値を含む行を抽出
        :param rd_csv: 取得したcsv
        :param rd_col: 指定の列
        :param a_val:  任意の値
        :param port:   True: 部分一致 False: 完全一致
        :return:       抽出した行
        """
        if port:
            return rd_csv[rd_csv[rd_col].str.contains(a_val)]    # 部分一致
        else:
            return rd_csv[rd_csv[rd_col] == a_val]               # 完全一致

    @staticmethod
    def pd_std(rd_csv, rd_col):
        """
        指定の列の標準偏差を出力する
        :param rd_csv: 取得したcsv
        :param rd_col: 指定の列
        :return:
        """
        # mn = rd_csv[[rd_col]].mean()[rd_col]
        i_std = rd_csv[[rd_col]].std()[rd_col]
        return i_std.round(2)

    @staticmethod
    def pd_statistics(rd_csv, rd_col):
        """
        指定の列の標準偏差を出力する
        :param rd_csv: 取得したcsv
        :param rd_col: 指定の列
        :return:
        """
        i_mn = rd_csv[[rd_col]].mean()[rd_col]          # 平均値
        i_std = rd_csv[[rd_col]].std()[rd_col]          # 標準偏差
        i_med = rd_csv[[rd_col]].median()[rd_col]       # 中央値
        i_max = rd_csv[[rd_col]].max()[rd_col]          # 最大値
        i_min = rd_csv[[rd_col]].min()[rd_col]          # 最小値
        return {'average': i_mn.round(2), 'standard deviation': i_std.round(2),
                'median': i_med.round(2), 'max': i_max.round(2), 'min': i_min.round(2)}

    @staticmethod
    def pd_remove_cd(rd_csv, ax, col_dex):
        """
        指定の列、または行を削除
        :param rd_csv: 取得したcsv
        :param ax: 1:列 0:行
        :param  col_dex: 列、または行番号
        :return:
        """
        col_dex = [i - 1 for i in col_dex]  # 行番号を正常にする
        if ax == 1:
            return rd_csv.drop(rd_csv.columns[col_dex], axis=ax)
        elif ax == 0:
            return rd_csv.drop(rd_csv.index[col_dex], axis=ax)


if __name__ == '__main__':
    cs = PDCommon()

    try:
        cs.csv_path = f'../csv/sbi_sec_result_20201005.csv'
        cs.csv_header = 1
        # cs.csv_rows = 20
        # cs.csv_encode = 'SHIFT-JIS'
        cs.csv_encode = 'utf-8'
        cs.csv_col = ['銘柄（コード）', '評価額', '損益', '損益（％）']
        ts = cs.r_csv()
        print(ts)
        # print(cs.idx(ts, '現在年齢', m='max', rd_head=cs.csv_header))
        # print(ts.duplicated(subset='45 契約情報_加盟店名'))
        # print(cs.any_ch(ts, '45 契約情報_加盟店名', 'アップルコンピュータ（株）'))
        # print(cs.pd_statistics(ts, '現在年齢'))
    except Exception as e:
        print(str(e))
