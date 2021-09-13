from app import app


@app.route('/', methods=['GET', 'POST'])
def home():
    return f'Hello world!'


@app.route('/<name>', methods=['GET', 'POST'])
def home_named(name):
    return f'Hello {name}'
