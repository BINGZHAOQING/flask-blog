# encoding=utf-8
# __Author__: BingZhaoQing
# __Date__: 2020-11-16


from app import create_app, db
from app.models import User

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
