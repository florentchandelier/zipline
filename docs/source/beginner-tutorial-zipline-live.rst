Zipline-live beginner tutorial
------------------------------
Zipline-Live, a Pythonic Algorithmic Trading Library http://www.zipline-live.io

Basics
~~~~~~

Zipline-live, the on-premise trading platform built on top of Quantopian’s Zipline. It aims to provide the ability to live trade code written for the zipline codebase. 

It is designed to be an extensible, drop-in replacement for zipline with multiple brokerage support to enable on premise trading of zipline algorithms.

zipline-live with Interactive Brokers TWS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lets take a look at a very simple algorithm from the ``examples``
directory, ``buyapple.py``:

.. code-block:: python

   from zipline.examples import buyapple
   buyapple??


.. code-block:: python

   from zipline.api import order, record, symbol


   def initialize(context):
       pass


   def handle_data(context, data):
       sym = symbol("AAPL")
       log.info("handle_data: price={}".format(data.current(sym, 'price') ) )


Running the algorithm
~~~~~~~~~~~~~~~~~~~~~

To now test this algorithm on financial data, ``zipline`` provides three
interfaces: A command-line interface, ``IPython Notebook`` magic, and
:func:`~zipline.run_algorithm`.

Ingesting Data
^^^^^^^^^^^^^^
If you haven't ingested the data, run:

.. code-block:: bash

   $ zipline ingest -b quantopian-quandl

where ``<bundle>`` is the name of the bundle to ingest, defaulting to
:ref:`quantopian-quandl <quantopian-quandl-mirror>`.

you can check out the :ref:`ingesting data <ingesting-data>` section for
more detail.

Command line interface
^^^^^^^^^^^^^^^^^^^^^^

Start zipline-live with --broker and --broker-uri specified.

.. code-block:: python

    zipline run -f ~/zipline-algos/demo.py --state-file ~/zipline-algos/demo.state --realtime-bar-target ~/zipline-algos/realtime-bars/ --broker ib --broker-uri localhost:7496:1232 --bundle quantopian-quandl --data-frequency minute


.. parsed-literal::

    [2017-08-18 15:07:24.850838] INFO: IB Broker: Connecting: localhost:7496:1232
    Server Version: 76
    TWS Time at connection:20170818 11:07:24 EST
    [2017-08-18 15:07:24.973549] ERROR: IB Broker: [504] Not connected
    [2017-08-18 15:07:24.977206] INFO: IB Broker: [2104] Market data farm connection is OK:eufarm
    [2017-08-18 15:07:24.977584] INFO: IB Broker: [2104] Market data farm connection is OK:usfuture
    [2017-08-18 15:07:24.977852] INFO: IB Broker: [2104] Market data farm connection is OK:cashfarm
    [2017-08-18 15:07:24.978034] INFO: IB Broker: [2104] Market data farm connection is OK:usfarm.us
    [2017-08-18 15:07:24.978198] INFO: IB Broker: [2104] Market data farm connection is OK:usfarm
    [2017-08-18 15:07:24.978356] INFO: IB Broker: [2106] HMDS data farm connection is OK:ushmds
    [2017-08-18 15:07:25.178885] INFO: IB Broker: Managed accounts: ['********']
    [2017-08-18 15:07:25.280132] INFO: IB Broker: Local-Broker Time Skew: 0 days 00:00:01
    [2017-08-18 15:07:26.104361] WARNING: Loader: Refusing to download new benchmark data because a download succeeded at 2017-08-18 14:48:52+00:00.
    [2017-08-18 15:07:26.288726] INFO: Live Trading: initialization done
    [2017-08-18 15:08:00.323263] INFO: algo: handle_data: price=nan
    [2017-08-18 15:09:00.471625] INFO: algo: handle_data: price=158.08
    [2017-08-18 15:10:00.624054] INFO: algo: handle_data: price=158.12


Conclusions
~~~~~~~~~~~

You can extend the demo algorithm to obtain portfolio data or to create orders. 

Feel free to ask questions on `slack
list <https://zipline-live.slack.com>`__, report
problems on our `GitHub issue
tracker <https://github.com/zipline-live/zipline/issues?state=open>`__
