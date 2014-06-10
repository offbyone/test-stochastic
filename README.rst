=================
 Test Stochastic
=================

.. image:: https://travis-ci.org/offbyone/test-stochastic.svg?branch=mainline
        :alt: Build Status
        :target: https://travis-ci.org/offbyone/test-stochastic

Why?
====

Have you ever worried that your unit tests depend on each other in some
subtle but critical way? Would you like to find instances of this
without having to comment out and re-run each individual test over and
over again? If so, test-stochastic is your huckleberry!

Installation
============

``test-stochastic`` can be installed using standard Python packaging
tools. It uses setuptools extension points to integrate with test
runners, so that's required as well.
