from flask import Blueprint, render_template, request, redirect, url_for, flash
from .database import get_db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT SUM(amount) FROM transactions WHERE type="Income"')
    income = cur.fetchone()[0] or 0
    cur.execute('SELECT SUM(amount) FROM transactions WHERE type="Expense"')
    expense = cur.fetchone()[0] or 0
    conn.close()
    return render_template('index.html', income=income, expense=expense)

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

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_transaction(id):
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        transaction_type = request.form['transaction_type']
        category = request.form['category']
        amount = request.form['amount']
        description = request.form['description']
        cur.execute('UPDATE transactions SET type=?, category=?, amount=?, description=? WHERE id=?',
                    (transaction_type, category, amount, description, id))
        conn.commit()
        conn.close()
        flash('Transaction updated successfully!', 'success')
        return redirect(url_for('main.view_transactions'))
    else:
        cur.execute('SELECT * FROM transactions WHERE id=?', (id,))
        transaction = cur.fetchone()
        conn.close()
        return render_template('edit_transaction.html', transaction=transaction)

@main.route('/delete/<int:id>')
def delete_transaction(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM transactions WHERE id=?', (id,))
    conn.commit()
    conn.close()
    flash('Transaction deleted successfully!', 'success')
    return redirect(url_for('main.view_transactions'))