# settings_test.py

from example.settings import *
import os

#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_RUNNER = 'django_jenkins.runner.CITestSuiteRunner'

COVERAGE_REPORT_HTML_OUTPUT_DIR = '.cover'

# django-jenkins
INSTALLED_APPS += (
    'django_jenkins',
)
JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
 #   'django_jenkins.tasks.run_pyflakes',
 #   'django_jenkins.tasks.run_flake8',
)
PROJECT_APPS = (
    'todo',
)

NOSE_ARGS = [
    '--with-xunit',
    '--with-coverage',
    '--cover-xml',
    '--cover-html',
    '--cover-package=todo', 
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.db'),
    }
}


