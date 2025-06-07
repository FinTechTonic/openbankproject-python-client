Installation
============

The OpenBankProject Client can be installed using pip:

.. code-block:: bash

    pip install openbankproject-client

For development or to build documentation, you can install with additional dependencies:

.. code-block:: bash

    pip install openbankproject-client[docs]

Requirements
-----------

* Python 3.8 or higher
* requests >= 2.30.0

Optional Dependencies
-------------------

* sphinx >= 8.2.3 (for documentation)
* sphinx-rtd-theme >= 3.0.2 (for documentation)

Development Installation
----------------------

To install the package in development mode:

.. code-block:: bash

    git clone https://github.com/FinTechTonic/openbankproject-python-client.git
    cd openbankproject-python-client
    pip install -e .[docs] 