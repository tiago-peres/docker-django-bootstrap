import os


def pytest_addoption(parser):
    parser.addoption(
        '--django-bootstrap-image', action='store',
        default=os.environ.get('DJANGO_BOOTSTRAP_IMAGE', 'mysite:py3'),
        help='django-bootstrap docker image to test')


def pytest_report_header(config):
    return 'django-bootstrap docker image: {}'.format(
        config.getoption('--django-bootstrap-image'))
