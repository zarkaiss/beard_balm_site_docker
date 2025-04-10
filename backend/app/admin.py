from flask_admin.contrib.sqla import ModelView
from flask import session, redirect, url_for, request,abort, render_template
from flask_login import current_user
import flask_login as login
from flask_admin import BaseView, expose
import requests
from requests.auth import HTTPBasicAuth
import json
import pprint
import pandas as pd
from pandas.io.json import json_normalize
pd.set_option('display.expand_frame_repr', False)




class AdminView(ModelView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.is_admin == True:
            return True
        return False

    column_exclude_list = ('password')


    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.login'))
            
    


# class SnipCart(BaseView):
#     @expose('/')
#     def APIview(self):
#         token = "ST_Yzc2NmQ4MjQtMjNiNC00ZGRlLWFjMmItYTIzNzk5NTE1OWZkNjM3MDU2NDQxNTA4ODU1NzA4"
#         url = "https://app.snipcart.com/api/orders/?offset=0&limit=5&status=processed"
#         headers = {'Content-type': 'application/json', "Accept": "application/json"}
#         content = requests.get(url, headers=headers, auth=HTTPBasicAuth(token, ""))
#         #frame2 = pd.read_json(content.text)
#         frame = json.loads(content.text)
#         # pp = pprint.PrettyPrinter()
#         # pp.pprint(frame)
#         #root_level = frame['items'][0]
#         #for k, v in root_level.items():
#         #    print(f"{k}\n{v}")
#         #frame1 = json_normalize(frame['items'],['items'])
#         #df = json_normalize(frame.to_dict('list'),['items']).unstack().apply(pd.Series)
#         #df1 = df.pivot_table(index=df.index.get_level_values(1), aggfunc=' '.join)
#         #frame1 = json_normalize(frame)
#         #frame1.head(16)
#         #print(content.text)
        
#         return self.render('snipcart.html', frame=frame)
