Primes
======

Script that determines if a given number is prime, and to find consecutive prime numbers.

Used this as a way to learn Cython.


Installation
------------

If installing on Linux, you should run the following first::

    $ sudo apt-get install python3-dev


Regardless of OS, setuptools is required::

    $ pip3 install setuptools


All of the other requirements are handled in setup.py, which will be run when you install like this::

    $ pip3 install git+git://github.com/dskrypa/primes


Compiling Cython Modules
------------------------

To re-compile the cprimes Cython module::

    $ ./setup.py build_ext --inplace && cython -a ./cprimes.pyx
