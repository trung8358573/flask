from base import app
from socket import gethostname


if __name__ == '__main__':
    db.create_all()
    if 'liveconsole' not in gethostname():
        app.run(debug=True)

