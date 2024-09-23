Local Development
=================

Prerequisites
--------------

- GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher

In the rest of the documentation on local development, it is assumed that the `python` command in your OS shell runs the above Python interpreter (unless a virtual environment is activated).

macOS / Linux
--------------

Clone the repository
~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    cd /path/to/put/project/in
    git clone https://github.com/JasonBats/Python-OC-Lettings-FR.git


Create the virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    python -m venv venv
    apt-get install python3-venv

(If the previous step throws errors about a missing package on Ubuntu)

Activate the environment

.. code-block:: bash

    source venv/bin/activate

- Confirm that the `python` command runs the Python interpreter in the virtual environment

.. code-block:: bash

    which python

- Confirm that the version of the Python interpreter is 3.6 or higher

.. code-block:: bash

    python --version
- Confirm that the `pip` command runs the pip executable in the virtual environment

.. code-block:: bash

    which pip

- To deactivate the environment

.. code-block:: bash

    deactivate

- Install requirements

.. code-block:: bash

    pip install -r requirements.txt
