Run project
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
- Link repo to your docker hub project
- Set environment variables in GitHub:

.. code-block::

    DOCKER_PASSWORD

.. code-block::

    DOCKER_USERNAME

.. code-block::

    SECRET_KEY

Testing
~~~~~~~
- Run tests :
.. code-block:: bash

    python coverage run -m pytest

- Generate html report about coverage

.. code-block:: bash

    python coverage html

Linting
~~~~~~~
- Run linting check and report generation :
.. code-block:: bash

    flake8

- Report is generated at flake8report/index.html as specified in .flake8 conf file.

