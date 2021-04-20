from flask import Blueprint, render_template

goods = Blueprint('goods',
                  __name__,
                  static_folder='goods_static',
                  template_folder='goods_templates',
                  url_prefix='/goods')


@goods.route('/apple')
def goods_apple():
    return '商品：苹果'


@goods.route('/banana')
def goods_banana():
    return render_template('goods.html')