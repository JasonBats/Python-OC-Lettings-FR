Getting started
=================


Run project
-----------


Run locally
~~~~~~~~~~~~
.. code-block:: bash

    python manage.py runserver


Deploy
~~~~~~~~~~~~

- Push on your own repo
- Link repo to railway.app or similar (Render, Google Cloud platform)
    - **SECRET_KEY** (Django generated secret key to generate session ID for each user)
    - **SENTRY_DSN** (Project's ID in sentry to track errors)

.. image:: source/railway-env.jpg
|
- Link repo to your docker hub project

- Set environment variables in GitHub:
    - **SECRET_KEY** (Django generated secret key to generate session ID for each user)
    - **DOCKER_PASSWORD**
    - **DOCKER_USERNAME**
.. image:: source/github-env.jpg

|
Testing
~~~~~~~
- Run tests :
.. code-block:: bash

    python coverage run -m pytest

- Generate html report about coverage

.. code-block:: bash

    python coverage html

- Report is generated at htmlcov/index.html

Linting
~~~~~~~
- Run linting check and report generation :
.. code-block:: bash

    flake8

- Report is generated at flake8report/index.html as specified in .flake8 conf file.

