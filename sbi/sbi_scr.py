import os
import re
import time
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from shared import common, make_log, cryptography, pd_common
import traceback
from pathlib import Path


# デフォルトのパスを設定
path = Path(__file__).parent
path /= '../'
default_path = path.resolve()


def connect_sbi(account, password, name):
    options = Options()
    # 非表示
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options, executable_path='D:\\geckodriver-v0.27.0-win64\\geckodriver.exe')

    # SBI証券のトップ画面を開く
    driver.get('https://www.sbisec.co.jp/ETGate')

    time.sleep(3)

    # ログイン情報
    input_user_id = driver.find_element_by_name('user_id')
    input_user_id.send_keys(account)
    input_user_password = driver.find_element_by_name('user_password')
    input_user_password.send_keys(password)

    # ログインボタンをクリック
    driver.find_element_by_name('ACT_login').click()

    return driver


def get_stock_data(driver):

    time.sleep(4)

    # ポートフォリオ
    driver.find_element_by_xpath('//*[@id="link02M"]/ul/li[1]/a/img').click()

    html = driver.page_source.encode('utf-8')

    soup = BeautifulSoup(html, "html.parser")

    # 株式情報を取得
    table_data = soup.find_all("table", bgcolor="#9fbf99", cellpadding="4", cellspacing="1", width="100%")

    # 株式（現物/特定預り）
    df_stock_specific = pd.read_html(str(table_data), header=0)[0]
    df_stock_specific = format_data(df_stock_specific, '株式（現物/特定預り）', '')

    # 株式（現物/NISA預り）
    # df_stock_fund_nisa = pd.read_html(str(table_data), header=0)[1]
    # df_stock_fund_nisa = format_data(df_stock_fund_nisa, '株式(現物/NISA預り)', '上場ＴＰＸ')

    # 投資信託（金額/特定預り）
    # df_fund_specific = pd.read_html(str(table_data), header=0)[2]
    df_fund_specific = pd.read_html(str(table_data), header=0)[1]
    df_fund_specific = format_data(df_fund_specific, '投資信託（金額/特定預り）', '')

    # 投資信託（金額/NISA預り）
    # df_fund_nisa = pd.read_html(str(table_data), header=0)[3]
    # df_fund_nisa = format_data(df_fund_nisa, '投資信託（金額/NISA預り）', '')

    # 投資信託（金額/つみたてNISA預り）
    # df_fund_nisa_tsumitate = pd.read_html(str(table_data), header=0)[4]
    # df_fund_nisa_tsumitate = format_data(df_fund_nisa_tsumitate, '投資信託（金額/つみたてNISA預り）', '')

    df_ja_result = pd.concat(
        [
            df_stock_specific,
            # df_stock_fund_nisa,
            df_fund_specific,
            # df_fund_nisa,
            # df_fund_nisa_tsumitate
        ]
    )
    df_ja_result['date'] = datetime.date.today()

    return df_ja_result


def format_data(df_data, category, fund):

    if category == '株式（現物/特定預り）':
        df_data = df_data.loc[:, ['銘柄（コード）', '評価額', '損益', '損益（％）', '前日比', '前日比（％）']]
    elif category == '':
        df_data = df_data.loc[:, ['ファンド名', '評価額', '損益', '損益（％）', '前日比', '前日比（％）']]
    else:
        df_data = df_data.loc[:, ['評価額', '損益', '損益（％）', '前日比', '前日比（％）']]

    df_data['カテゴリー'] = category
    if fund != '':
        df_data['ファンド名'] = fund

    return df_data


def export_data(df_result, name):
    """
    取得したデータをファイルに出力する

    Parameters:
        df_result: Union
            サイトから取得したデータ
        name: str
            ファイル名

    Returns:


    Notes:
        特記事項を記載する

    Raises:
        エラーパターンを記載する
    """
    date = after_fifteen()
    df_result.to_csv('../csv/' + name + f'_result_{date}.csv')


def read_data():
    """
    データを読み込む

    Parameters
        df_result: Union
            サイトから取得したデータ
        name: str
            ファイル名

    Returns
        ts: DataFrame
            株式データ


    Notes:
        特記事項を記載する

    Raises:
        エラーパターンを記載する
    """
    cs = pd_common.PDCommon()
    # csv_path = '../csv/'
    # csv_path = __file__
    # csv_path = os.path.dirname(__file__)
    # PosixPathを文字列に変換する
    csv_path = str(default_path) + '/csv/'

    csv_list = common.file_list(dir=csv_path, extension='.csv')

    # 最新の情報のみ取得
    csv_file = max(csv_list)

    cs.csv_path = csv_path + csv_file
    cs.csv_header = 1
    # cs.csv_rows = 20
    # cs.csv_encode = 'SHIFT-JIS'
    cs.csv_encode = 'utf-8'
    cs.csv_col = ['銘柄（コード）', '評価額', '損益', '損益（％）']
    df = cs.r_csv()

    return df


def molding_data(df):
    """
    データ成形

    """
    stock_data = []

    # カラム名
    stock_columns = list(df.columns)

    for index, row in df.iterrows():

        # 株式データを整形してリスト化
        m = re.search(r'\d+', row[0])
        if m:
            df.iloc[index, 0] = row[0].replace(m.group(), '').strip()
        r = list(row)
        stock_data.append(r)

    return stock_columns, stock_data


def after_fifteen():
    """
    15時(東証の立会時間)より前か否か判定

    Parameters:

    Returns
        d: str
            日付(YYYYmmDD)

    Notes:
        特記事項を記載する

    Raises:
        エラーパターンを記載する
    """
    h = datetime.datetime.now().hour
    if h > 14:
        d = datetime.date.today().strftime("%Y%m%d")
    else:
        d = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d")

    return d


def main():

    write_log = make_log.Log(default_path)

    driver = None

    try:
        write_log.debug_log('Start SBI')

        crypt = cryptography.Crypt()

        account_name = crypt.composite('username')
        password = crypt.composite('password')

        name = 'sbi_sec'

        driver = connect_sbi(account_name, password, name)
        write_log.debug_log('Connect SBI')
        df_stock_result = get_stock_data(driver)
        write_log.debug_log('Get Data')
        export_data(df_stock_result, name)
        write_log.debug_log('Export Data')

    except Exception as e:
        write_log.error_log(str(e))
        err_list = traceback.format_exc().split('\n')
        for err in err_list:
            write_log.error_log(err)

    finally:
        if driver:
            # ブラウザを閉じる
            driver.quit()
        write_log.debug_log('End SBI')


if __name__ == '__main__':
    main()
