"""
WSGI config for learnoskill project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnoskill.settings')

application = get_wsgi_application()
<<<<<<< HEAD

=======
>>>>>>> 77f80a2ef915dac1ebda05591c2683aa5fccca06
