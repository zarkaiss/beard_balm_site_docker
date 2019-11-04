from flask_admin.contrib.sqla import ModelView
from flask import session, redirect, url_for, request,abort
from flask_login import current_user
import flask_login as login
from flask_admin import BaseView, expose
import requests
from requests.auth import HTTPBasicAuth




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


class SnipCart(BaseView):
    @expose('/')
    def APIview(self):
        token = "ST_Yzc2NmQ4MjQtMjNiNC00ZGRlLWFjMmItYTIzNzk5NTE1OWZkNjM3MDU2NDQxNTA4ODU1NzA4"
        url = "https://app.snipcart.com/api/orders"
        headers = {'Content-type': 'application/json', "Accept": "application/json"}
        content = requests.get(url, headers=headers, auth=HTTPBasicAuth(token, ""))
    
        return(content.text)


