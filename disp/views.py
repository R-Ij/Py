from disp import app, default_path
import shared.common as cmn
from sbi import sbi_scr
from flask import request, redirect, url_for, render_template, flash, session


img_path = f'{default_path}/static/img/main'
img_path_2 = '../static/img/main'


@app.route('/')
def index():
    # 株式データ取得
    df = sbi_scr.read_data()
    stock_columns, stock_data = sbi_scr.molding_data(df)

    images = cmn.file_list(dir=img_path, extension='.jpg')
    dt = sbi_scr.read_data()
    return render_template(
        'index.html',
        images=images,
        img_path=img_path_2,
        csv_data=dt,
        stock_columns=stock_columns,
        stock_data=stock_data
    )


@app.route('/regist')
def form():
    images = cmn.file_list(dir=img_path, extension='.jpg')
    return render_template('index.html', images=images, img_path=img_path_2)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            return redirect('/')
        return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect('/')

