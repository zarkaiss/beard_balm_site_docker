from app import db
from app.main import bp
from flask_login import current_user, login_user, logout_user, login_required
from flask import render_template, abort, flash, redirect, url_for, request, current_app
from app.main.forms import LoginForm, RegistrationForm, FeedBackForm, ResetPasswordRequestForm, ResetPasswordForm
from app.models import User, Feedback, Product
from werkzeug.urls import url_parse
import redis
from rq import Queue, Connection
from app.main.tasks import send_email
from app.main.utils import encode_token, generate_url, decode_token
from sqlalchemy.exc import IntegrityError
from app.email import send_password_reset_email
from itsdangerous import URLSafeTimedSerializer


@bp.route("/")
def landing():
    feedback_ = Feedback.query.filter_by(approved=True).limit(3).all()
    return render_template('landing.html', feedback_=feedback_)


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


@bp.route('/reset', methods=["GET", "POST"])
def reset():
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
        
        except:
            flash('Invalid email address!', 'danger')
            return render_template('reset_password_request.html', form=form)
        
        if user.confirmed:
            send_password_reset_email(user.email)
            flash('Please check your email for a password reset link.', 'success')
        else:
            flash('Your email address must be confirmed before attempting a password reset', 'danger')
        
        return redirect(url_for('main.login'))
    
    return render_template('reset_password_request.html', form=form)
    
@bp.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    try:
        password_reset_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        email = password_reset_serializer.loads(token, salt='password-reset-salt', max_age=3600)
    
    except:
        flash('The password reset link is invalid or has expired.', 'danger')
        return redirect(url_for('main.login'))
        
    form = ResetPasswordForm()
    
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=email).first()
            
        except:
            flash('Invalid email address!', 'danger')
            return redirect(url_for('main.login'))
            
        user.set_password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('main.login'))
        
    return render_template('reset_password.html', form=form, token=token)



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




# @bp.route('/reset_password_request', methods=['GET', 'POST'])
# def reset_password_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('main.landing'))
#     form = ResetPasswordRequestForm()
#     if form.validate_on_submit():
#         try:

#             user = User.query.filter_by(email=form.email.data).first()
#             #token = encode_token(user.email)
#             ##Closer with that token figure out error tomorrow use http://www.patricksoftwareblog.com/password_reset_via_email_link/
#             token = user.get_reset_password_token(user)
#             confirm_url = generate_url('main.reset_password', token)
#             redis_url = current_app.config['REDIS_URL']
#             body = render_template('email/reset_password.html', confirm_url=confirm_url) 
#             with Connection(redis.from_url(redis_url)):
#                 if user:
#                     q = Queue()
#                     q.enqueue(send_password_reset_email, user)
#                 flash('Check your email for the instructions to reset your password.')
#             return redirect(url_for('main.login'))
#         except IntegrityError:
#             flash('Email address not found.', 'danger')

#     return render_template('reset_password_request.html', title='Reset Password', form=form)



# @bp.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('main.landing'))
#     user = User.verify_reset_password_token(token)
#     if not user:
#         return redirect(url_for('main.index'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         user.set_password(form.password.data)
#         db.session.commit()
#         flash('Your password has been reset.')
#         return redirect(url_for('main.login'))
#     return render_template('reset_password.html', form=form)
