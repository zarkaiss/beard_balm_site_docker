activate_this = '/var/www/html/bro/bro/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))
import sys
sys.path.insert(0, '/var/www/html/bro')
from app import create_app
app = create_app()
application = create_app()

