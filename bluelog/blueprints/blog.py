from flask import Blueprint, render_template, request, current_app
from bluelog.models import Post
import json


blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/', defaults={'page': 1})
@blog_bp.route('/page/<int:page>')
def index(page):
    per_page = current_app.config['BLUELOG_POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page)
    return render_template('blog/index.html', pagination=pagination, posts=pagination.items)


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    pass


@blog_bp.route('/about')
def about():
    # 测试
    from bluelog.forms import LoginForm
    form = LoginForm()
    return render_template('blog/about.html', form=form)


@blog_bp.route('/post/<slug>', methods=['GET', 'POST'])
def show_post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/post.html', post=post)

