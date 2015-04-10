import os
import sys	
sys.path.append('/srv/app/MyTestProject/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'MyTestProject.settings'
from django.core.wsgi import get_wsgi_application
#application = django.core.handlers.wsgi.WSGIHandler()
application = get_wsgi_application()
