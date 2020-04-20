import os
from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from flask_login import current_user, login_required

from .models import Category, HarvestedCanabis, PackagedCanabis
from .forms import EditHarvestedCanabis, CreateHarvestedCanabisForm,\
    EditPackagedCanabisForm, CreatePackagedCanabisForm


main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')


@main_bp.route('/', defaults={'path': 'index.html'})
@main_bp.route('/<path>')
@login_required
def index(path):

    content = None

    try:

        # try to match the pages defined in -> pages/<input file>
        return render_template('layouts/default.html',
                               content=render_template('pages/'+path, current_user=current_user))
    except:

        return render_template('layouts/auth-default.html',
                               content=render_template('pages/404.html'))


# Render the profile page
@main_bp.route('/profile.html')
@login_required
def profile():

    return render_template('layouts/default.html',
                           content=render_template('pages/profile.html'))


# Render the display page
@main_bp.route('/display/<category_id>')
@login_required
def display_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    all_harvested_canabis = HarvestedCanabis.query.filter_by(category_id=category.id)
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/display.html',
                               category=category,
                               all_harvested_canabis=all_harvested_canabis
                           ))


# delete page
@main_bp.route('/delete/<product_id>', methods=['GET', 'POST'])
@login_required
def delete_harvested_canabis(product_id):
    if current_user.is_admin == False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    harvested_canabis = HarvestedCanabis.query.get(product_id)
    if request.method == 'POST':
        HarvestedCanabis.delete(harvested_canabis)
        flash('harvested canabis deleted successfully')
        return redirect(url_for('main_bp.index'))
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/delete_harvested_canabis.html',
                               harvested_canabis=harvested_canabis,
                               product_id=harvested_canabis.id))


# Edit the profile page
@main_bp.route('/edit/<product_id>', methods=['GET', 'POST'])
@login_required
def edit_harvested_canabis(product_id):
    if current_user.is_admin == False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    harvested_canabis = HarvestedCanabis.query.get(product_id)
    form = EditHarvestedCanabis(obj=harvested_canabis)
    if form.validate_on_submit():
        harvested_canabis.product_name = form.product_name.data
        harvested_canabis.product_batch = form.product_batch.data
        harvested_canabis.net_weight_received = form.net_weight_received.data
        harvested_canabis.balance = form.balance.data
        harvested_canabis.category_id = form.category_id.data
        harvested_canabis.transaaction_date = form.transaction_date.data
        print('transaction_date: ', harvested_canabis.transaaction_date)
        HarvestedCanabis.save(harvested_canabis)
        flash('harvested canabis edit successfully')
        return redirect(url_for('main_bp.index'))
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/edit_harvested_canabis.html',
                               form=form))


# Render the harvested canabis  page
@main_bp.route('/add.html/<product_id>', methods=['GET', 'POST'])
@login_required
def add_harvested_canabis(product_id):
    if current_user.is_admin == False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    form = CreateHarvestedCanabisForm()
    form.product_id.data = product_id  # pre-populates product_id
    if form.validate_on_submit():
        print('on submit')

        product_name = form.product_name.data
        print('product name is :', product_name)
        product_batch = form.product_batch.data
        net_weight_received = form.net_weight_received.data
        balance = form.balance.data
        category_id = form.category_id.data
        # category = form.category.data
        transaction_date = datetime.strptime(request.form.get('transaction_date'), '%Y-%m-%d')
        # transaction_date = form.transaction_date.data
        result = HarvestedCanabis.query.filter_by(product_name=product_name).first()
        print('result is {}'.format(result))
        print('transaction_date', transaction_date)
        harvestedCanabis = HarvestedCanabis(
            product_name=product_name,
            product_batch=product_batch,
            net_weight_received=net_weight_received,
            balance=balance,
            category_id=category_id,
            # category=category,
            transaction_date=transaction_date
        )
        HarvestedCanabis.save(harvestedCanabis)
        harvested_canabis_list = HarvestedCanabis.query.all()
        print('new list is :', harvested_canabis_list)
        flash('harvested canabis added succesfully')
        return redirect(url_for('main_bp.display_category', category_id=category_id))

    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/add_harvested_canabis.html',
                               form=form,
                               product_id=product_id
                           ))


# Render the harvested canabis  page
@main_bp.route('/harvested_canabis.html')
@login_required
def harvested_canabis():
    harvested_canabis_list = HarvestedCanabis.query.all()
    length = len(harvested_canabis_list)
    print('list harvested canabis')
    print(length)
    print(harvested_canabis_list)
    print(type(harvested_canabis_list))
    return render_template(
        'layouts/default.html',
        content=render_template(
            'pages/harvested_canabis.html',
            current_user=current_user,
            all_canabis=harvested_canabis_list,
            length=length
        ))


"""
    Packaged canabis
"""


# Render the harvested canabis  page
@main_bp.route('/packaged_canabis.html')
@login_required
def packaged_canabis():
    packaged_canabis_list = PackagedCanabis.query.all()
    length = len(packaged_canabis_list)
    print('list harvested canabis')
    print(length)
    print(packaged_canabis_list)
    print(type(packaged_canabis_list))
    return render_template(
        'layouts/default.html',
        content=render_template(
            'pages/packaged_canabis.html',
            current_user=current_user,
            length=length,
            packaged_canabis_list=packaged_canabis_list
        ))


# delete page
@main_bp.route('/delete_packaged_canabis.html/<product_id>', methods=['GET', 'POST'])
@login_required
def delete_packaged_canabis(product_id):
    if current_user.is_admin == False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    packaged_canabis = PackagedCanabis.query.get(product_id)
    if request.method == 'POST':
        PackagedCanabis.delete(packaged_canabis)
        flash('harvested canabis deleted successfully')
        return redirect(url_for('main_bp.index'))
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/delete_packaged_canabis.html',
                               packaged_canabis=packaged_canabis,
                               product_id=packaged_canabis.id))


# Edit the profile page
@main_bp.route('/edit_packaged_canabis.html/<product_id>', methods=['GET', 'POST'])
@login_required
def edit_packaged_canabis(product_id):

    if current_user.is_admin == False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    packaged_canabis = PackagedCanabis.query.get(product_id)
    form = EditPackagedCanabisForm(obj=packaged_canabis)
    if form.validate_on_submit():
        packaged_canabis.source = form.source.data
        packaged_canabis.product_name = form.product_name.data
        packaged_canabis.product_batch = form.product_batch.data
        packaged_canabis.net_weight_received = form.net_weight_received.data
        packaged_canabis.balance = form.balance.data
        packaged_canabis.category_id = form.category_id.data
        packaged_canabis.transaction_date = form.transaction_date.data
        print('transaction_date: ', packaged_canabis.transaction_date)
        PackagedCanabis.save(packaged_canabis)
        flash('harvested canabis edit successfully')
        return redirect(url_for('main_bp.index'))
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/edit_packaged_canabis.html',
                               form=form))


# Render the harvested canabis  page
@main_bp.route('/add_packaged_canabis.html/<product_id>', methods=['GET', 'POST'])
@login_required
def add_packaged_canabis(product_id):
    if current_user.is_admin == False:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/403.html'))
    form = CreatePackagedCanabisForm()
    form.product_id.data = product_id  # pre-populates product_id
    if form.validate_on_submit():
        print('on submit')
        source = form.source.data
        product_name = form.product_name.data
        print('product name is :', product_name)
        product_batch = form.product_batch.data
        net_weight_received = form.net_weight_received.data
        balance = form.balance.data
        category_id = form.category_id.data
        # category = form.category.data
        transaction_date = datetime.strptime(request.form.get('transaction_date'), '%Y-%m-%d')
        # transaction_date = form.transaction_date.data
        result = PackagedCanabis.query.filter_by(product_name=product_name).first()
        print('result is {}'.format(result))
        print('transaction_date', transaction_date)
        packagedCanabis = PackagedCanabis(
            product_name=product_name,
            product_batch=product_batch,
            net_weight_received=net_weight_received,
            balance=balance,
            category_id=category_id,
            source=source,
            transaction_date=transaction_date
        )
        PackagedCanabis.save(packagedCanabis)
        packaged_canabis_list = PackagedCanabis.query.all()
        print('new list is :', packaged_canabis_list)
        flash('harvested canabis added succesfully')
        return redirect(url_for('main_bp.display_category_packaged', category_id=category_id))

    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/add_packaged_canabis.html',
                               form=form,
                               product_id=product_id
                           ))


# Render the display page
@main_bp.route('/display_packaged_canabis.html/<category_id>')
@login_required
def display_category_packaged(category_id):
    category = Category.query.filter_by(id=category_id).first()
    all_packaged_canabis = PackagedCanabis.query.filter_by(category_id=category.id)
    return render_template('layouts/default.html',
                           content=render_template(
                               'pages/display_packaged_canabis.html',
                               category=category,
                               all_packaged_canabis=all_packaged_canabis
                           ))