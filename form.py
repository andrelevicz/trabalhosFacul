import requests

def render_login_form():
    form_html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Formulário de Login</title>
    </head>
    <body>
        <h1>Formulário de Login</h1>
        <form action="/login" method="post">
            <label for="email">E-mail:</label>
            <input type="email" id="email" name="email" required><br>

            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required><br>

            <input type="submit" value="Login">
        </form>
    </body>
    </html>
    '''
    return form_html

def login():
    email = input('Digite seu e-mail: ')
    password = input('Digite sua senha: ')

    data = {
        'email': email,
        'password': password
    }

    response = requests.post('http://seu_servidor/login', json=data)
    result = response.json()

    if result['deu certo']:
        print('Login bem-sucedido!')
    else:
        print('Falha no login:', result['message'])

# Exemplo de uso:
if __name__ == '__main__':
    form_html = render_login_form()
    print(form_html)

    login()