from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta' 


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'ronal01' and password == '123456':
            session['username'] = username  
            flash('Bienvenido, ' + username + '!', 'success')  
            return redirect(url_for('home')) 
        else:
            flash('Credenciales incorrectas. Inténtalo de nuevo.', 'danger')
    return render_template('login.html')


@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return redirect(url_for('login'))  

@app.route('/logout')
def logout():
    session.pop('username', None)  
    flash('Has cerrado sesión correctamente.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
