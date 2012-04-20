======================
Contributing to Womack
======================

Womack development is hosted on `github`_. If you want to contribute
to Womack, fork the project and follow the quickstart steps to try it
out. Then you might want to:

Install the development requirements
------------------------------------

Run ``make dev`` to install the default, server, test and docs
requirements.

Run tests
---------

Womack uses `tox`_, `nose2`_ and `selenium`_ to run its tests. There
are unit tests for the python code, and functional tests for the full
system.

* To run unit tests: ``tox`` (or ``make test``)

* To run functional tests: ``tox -e func`` (or ``make functional-test``)

  .. warning ::

     The functional tests are pretty slow, and require the Firefox
     selenium webdriver and redis.

Compile documentation
----------------------

Womack's documetation is built with `Sphinx`_. To compile Womack's
documentation, run ``make html`` from the top-level dir or in the
``docs`` dir. Docs are compiled to ``docs/_build/html``.

Contribute features, fixes or documentation
-------------------------------------------

Great! Here are some things you should know.

* Our python coding style standard is to stick to `pep8`_ except where
  that would be egregiously ugly. In particular we prefer to avoid
  tabs and trailing whitespace, and keep lines to 80 characters or
  below.

* Our javascript coding style is:

  * Try to keep it readable.

  * Keep things out of global scope.

* Any new code must come with tests and documentation.

* Bugfixes should *start* with a new test (that fails) and end with
  that new test passing.

* We prefer that patches be submitted as pull requests.


.. _github: https://github.com/leapfrogdevelopment/womack/
.. _Sphinx: http://sphinx.pocoo.org/
.. _tox: http://tox.testrun.org/
.. _nose2: http://nose-devs.github.com/nose2/
.. _selenium: http://seleniumhq.org/
.. _pep8: http://www.python.org/dev/peps/pep-0008/
