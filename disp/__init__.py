# import os
import sys
from pathlib import Path
from flask import Flask, render_template
import shared.common as cmn
from shared import make_log

# path = os.path.dirname(__file__)
# write_log = make_log.Log(path)

# デフォルトのパスを設定
path = Path(__file__).parent
path /= '../'
default_path = path.resolve()

write_log = make_log.Log(default_path)


try:
    # app = Flask(__name__, static_folder='../vue/dist/js/', template_folder='../vue/dist/')
    app = Flask(__name__, static_folder=f'{default_path}/static', template_folder=f'{default_path}/templates')
    app.config.from_object('disp.config')

    from disp import views
except Exception as e:
    write_log.err(e)
    sys.exit(1)
