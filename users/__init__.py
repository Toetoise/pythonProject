from flask import Blueprint, render_template

users = Blueprint('users',
                  __name__,
                  static_folder='user_static',
                  template_folder='user_templates',
                  url_prefix='/users')
# 绑定url地址，指定对应的蓝图


@users.route('/add')
def users_add():
    return '添加成功'


@users.route('/del')
def users_del():
    return render_template('user.html')
