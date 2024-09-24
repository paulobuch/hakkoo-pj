from flask import Flask, request, redirect
import requests

app = Flask(__name__)


# Substitua esses valores pelos seus
CLIENT_ID = '8829308963748176'
CLIENT_SECRET = 'ff3f17170f6d3c5380e2420c5a31d73d'
REDIRECT_URI = 'https://127.0.0.1:5000/callback'


@app.route('/')
def index():
    # Redireciona para a URL de autorização do Instagram
    auth_url = (f'https://api.instagram.com/oauth/authorize?client_id={CLIENT_ID}'
                f'&redirect_uri={REDIRECT_URI}&response_type=code')
    return redirect(auth_url)


@app.route('/callback')
def callback():
    # Recebe o código de autorização
    code = request.args.get('code')

    # Troca o código de autorização por um token de acesso
    token_url = 'https://api.instagram.com/oauth/access_token'
    payload = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': code
    }
    response = requests.post(token_url, data=payload)
    data = response.json()

    # Exibe o token de acesso
    access_token = data.get('access_token')
    return f'Access Token: {access_token}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, ssl_context=('cert.pem', 'key.pem'))
