Django-Analog
=============

Simple per-model log models for Django apps.

|Build Status| |Coverage Status| |Documentation Status|

Compatibility
-------------

* Django 5.2+
* Python 3.11+

Basic Usage
-----------

.. code:: python

    from django.db import models
    from analog import define_log_model

    class MyModel(models.Model):
        value = models.IntegerField(default=0)

    MyModelLogEntry = define_log_model(MyModel)

    m = MyModel.objects.create(value=42)
    m.add_log_entry('Something occurred')
    assert m.log_entries.last().message == 'Something occurred'

Development
-----------

Tests
~~~~~

::

    uv run pytest

Lint
~~~~

::

    uv run ruff check .
    uv run ruff format --check .

Multi-version testing
~~~~~~~~~~~~~~~~~~~~~

::

    uv run tox

Documentation
~~~~~~~~~~~~~

::

    uv run sphinx-build -b html docs docs/_build

.. |Build Status|
   image:: https://github.com/andersinno/django-analog/workflows/Test/badge.svg
   :target: https://github.com/andersinno/django-analog/actions
.. |Coverage Status|
   image:: https://codecov.io/gh/andersinno/django-analog/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/andersinno/django-analog
.. |Documentation Status|
   image:: https://readthedocs.org/projects/django-analog/badge/?version=latest
   :target: http://django-analog.readthedocs.org/en/latest/?badge=latest
