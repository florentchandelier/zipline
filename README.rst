
zipline-live | florent chandelier / development branch
============

Welcome to *zipline-live/flo-development branch*, built atop the \
original `zipline-live master github <https://github.com/zipline-live/zipline>`_, the on-premise trading platform \
built on top of Quantopian’s `zipline <https://github.com/quantopian/zipline>`_.

zipline-live is designed to be an extensible, drop-in replacement for zipline with multiple brokerage support to \
enable on premise trading of zipline algorithms.

See the `tutorial <https://github.com/florentchandelier/zipline/blob/development/docs/source/beginner-tutorial-
zipline-live.rst>`_ and `features <http://www.zipline-live.io/features>`_ for further details.

.. |Apache License| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://www.apache.org/licenses/LICENSE-2.0

Features in zipline-live/flo development branch
============

- multi-account support for single sign-on consolidated/individual or linked/advisor accounts `branch <https://github.com/florentchandelier/zipline/tree/feat/specify_accountID_liveTrading>`_

- local benchmark from local csv files for unlimited history in backtest and custom benchmarks (default IEX is only 5yrs from current day) `branch <https://github.com/florentchandelier/zipline/tree/feat/local_benchmark>`_
