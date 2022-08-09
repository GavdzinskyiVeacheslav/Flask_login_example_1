from flask import render_template, request, redirect, flash, url_for, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from blog.models import check_password_hash
from blog import bcrypt
from blog.main.forms import LoginForm
from blog.models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            # if user and bcrypt.check_password_hash(user.password, form.password.data):
            #     login_user(user, remember=form.remember.data)
            #     next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.account'))
        else:
            flash('Войти не удалось. Пожалуйста, проверьте электронную почту или пароль', 'danger')
    return render_template('login.html', form=form, title='Логин', legend='Войти')


@main.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html', title='Аккаунт', current_user=current_user)


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))










