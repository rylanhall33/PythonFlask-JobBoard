import pytest
import inspect

from .utils import *
from jobs import app

@pytest.mark.app_import_flask
def test_app_import_flask_module1():
    assert 'Flask' in dir(app), 'Have you imported the `Flask` class from `flask`?'
    assert inspect.isclass(app.Flask), '`Flask` is not a class.'
    assert 'render_template' in dir(app), '`render_template` has not been imported.'
    assert inspect.isfunction(app.render_template), '`render_template` is not a function.'

@pytest.mark.app_create_flask_app
def test_app_create_flask_app_module1():
    assert 'app' in dir(app), 'Have you created an instance of the `Flask` class called `app`?'
    assert isinstance(app.app, app.Flask), '`app` is not an instance of the `Flask` class.'

@pytest.mark.templates_folder
def test_templates_folder_module1():
    assert os.path.isdir('jobs/templates'), 'The `templates` folder has not been created.'

@pytest.mark.index_template
def test_index_template_module1():
    assert template_exists('index'), 'The `index.html` template does not exist in the `templates` folder.'
    assert template_find('index', 'h1', limit=1), "The `<h1>` in the `index.html` template does not contain the contents 'Jobs'."
    assert template_find('index', 'h1', limit=1)[0].text == 'Jobs', "The `<h1>` in the `index.html` template does not contain the contents 'Jobs'."

@pytest.mark.app_index_route_function
def test_app_index_route_function_module1():
    assert 'app' in dir(app), 'Have you created an instance of the `Flask` class called `app`?'
    assert 'jobs' in dir(app), 'Have you created the `jobs` function?'
    result = [item for item in get_functions(app.jobs) if item.startswith('render_template:index.html')]
    assert len(result) == 1, 'Have you called the `render_template` function.'

@pytest.mark.app_route_decoractors
def test_app_route_decoractors_module1():
    assert 'app' in dir(app), 'Have you created an instance of the `Flask` class called `app`?'
    assert template_exists('index'), 'The `index.html` template does not exist in the `templates` folder.'
    assert 'jobs' in dir(app), 'Have you created the `jobs` function?'

    rules = list_routes(app.app)

    assert 'jobs:GET,HEAD,OPTIONS:/' in rules, 'Have you decorated the `jobs` function with the `/` route?'
    assert 'jobs:GET,HEAD,OPTIONS:/jobs' in rules, 'Have you decorated the `jobs` function with the `/jobs` route?'
