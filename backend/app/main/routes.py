from app import db
from app.main import bp
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, abort, flash, redirect, url_for, request, current_app
from app.main.forms import LoginForm, RegistrationForm, FeedBackForm
from app.models import User, Feedback, Product
from werkzeug.urls import url_parse
import redis
from rq import Queue, Connection
from app.main.tasks import send_email
from app.main.utils import encode_token, generate_url, decode_token
from sqlalchemy.exc import IntegrityError


@bp.route("/")
def landing():
    feedback_ = Feedback.query.filter_by(approved=True).limit(3).all()
    return render_template('landing.html', feedback_=feedback_)



@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.landing'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.landing')
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.landing'))



@bp.route('/products')
def products():
    products_ = Product.query.all()
    return render_template('products.html', title='Products', products_=products_)



@bp.route('/products/<productid>')
def product_detail(productid):
    product_detail_ = Product.query.filter_by(productid=productid)
    return render_template('product_detail.html',product_detail_=product_detail_)




@bp.route('/about')
def about():

    return render_template('about.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    form = RegistrationForm()
    if form.validate_on_submit():
        try:

             user = User(username=form.username.data, email=form.email.data)
             user.set_password(form.password.data)
             db.session.add(user)
             db.session.commit()
             token = encode_token(user.email)
             confirm_url = generate_url('main.confirm_email', token)
             body = render_template('email.txt', confirm_url=confirm_url)
             redis_url = current_app.config['REDIS_URL']
             with Connection(redis.from_url(redis_url)):
                 q = Queue()
                 q.enqueue(send_email, user.email, body)
             flash('Congratulations, you are now a registered user!')
             return redirect(url_for('main.login'))
        except IntegrityError:
             db.session.rollback()
             flash('Sorry. That email already exists.', 'danger')
    users = User.query.all()
    return render_template('register.html', title='Register', form=form, users=users)



@bp.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    form = FeedBackForm(csrf_enabled=True)
    if form.validate_on_submit():
        new_feedback = Feedback(
            form.name.data,
            form.email1.data,
            form.subject.data,
            form.message.data
        )
        db.session.add(new_feedback)
        db.session.commit()
        flash('Your request has been submitted.')
        return redirect(url_for('main.feedback'))
    return render_template('feedback.html', title='Feedback',form=form)


@bp.route('/confirm/<token>')
def confirm_email(token):
    email = decode_token(token)
    if not email:
        flash('The confirmation links is invalid or has expired.', 'danger')
        return redirect(url_for('main.landing'))
    user = User.query.filter_by(email=email).first()
    if user.confirmed:
        flash('Account already confirmed.', 'success')
        return redirect(url_for('main.landing'))
    user.confirmed = True
    db.session.add(user)
    db.session.commit()
    flash('You have confirmed your account. Thanks!','success')
    return redirect(url_for('main.landing'))
