from flask import Blueprint, render_template
from bluelog.models import Post
import json


blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return render_template('blog/index.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    pass


@blog_bp.route('/about')
def about():
    # 测试
    from bluelog.forms import LoginForm
    form = LoginForm()
    return render_template('blog/about.html', form=form)


@blog_bp.route('/get_blogs/<int:page>')
def get_blogs(page):
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, 10)
    posts = pagination.items
    data = {
        'total_pages': pagination.pages,
        'page': pagination.page,
        'posts': []
    }
    for post in posts:
        data['posts'].append(post.to_json())

    return json.dumps(data)
