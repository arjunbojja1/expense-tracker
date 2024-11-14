from flask import Blueprint, render_template, request, redirect, url_for, flash
from .database import get_db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction_type = request.form['transaction_type']
        category = request.form['category']
        amount = request.form['amount']
        description = request.form['description']

        conn = get_db()
        cur = conn.cursor()
        cur.execute('INSERT INTO transactions (type, category, amount, date, description) VALUES (?, ?, ?, CURRENT_TIMESTAMP, ?)',
                    (transaction_type, category, amount, description))
        conn.commit()
        conn.close()

        flash('Transaction added successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('add_transaction.html')

@main.route('/view')
def view_transactions():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM transactions ORDER BY date DESC')
    rows = cur.fetchall()
    conn.close()
    return render_template('view_transactions.html', transactions=rows)
