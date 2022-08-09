from blog import create_app, create_user

app = create_app()

if __name__ == '__main__':
    create_user()
    app.run(debug=True)





# from flask import Flask
# from werkzeug.security import generate_password_hash, check_password_hash
#
# app = Flask(__name__)
#
# username_db, password_db = ('mike', '12345')
#
#
# @app.route('/login/<username>&<password>')
# def hash_pass(username, password):
#     if username == username_db and check_password_hash(generate_password_hash(password), password_db):
#         return f'Пользователь {username_db} успешно авторизован'
#     else:
#         return 'Ошибка входа. Check your login or password and try it again'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



