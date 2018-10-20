#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import pandas as pd
import numpy as np
import requests
import os

def get_benchmark_returns(symbol):
    """
    Get a Series of benchmark returns from IEX associated with `symbol`.
    Default is `SPY`.

    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.

    The data is provided by IEX (https://iextrading.com/), and we can
    get up to 5 years worth of data.
    """
    r = requests.get(
        'https://api.iextrading.com/1.0/stock/{}/chart/5y'.format(symbol)
    )
    data = json.loads(r.text)

    df = pd.DataFrame(data)

    df.index = pd.DatetimeIndex(df['date'])
    df = df['close']

    return df.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]


def get_localcsv_benchmark_returns(symbol, local_benchmark):
    """
    Get a Series of benchmark returns with `symbol`.
    Default is `SPY`.
    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.
    localpath : str
        absolute path where to find benchmark csv file.
    """

    ''' open saved csv files '''

    current_dir = os.getcwd()
    os.chdir(local_benchmark)
    filename = str(symbol + '.csv')
    data = pd.read_csv(filename)
    data.columns = map(str.lower, data.columns)

    data['date'] = pd.to_datetime(data['date']).copy()
    data.set_index('date', drop=False, inplace=True)
    try:
        data = data['close']
    except:
        data = data['adj close']
        
    os.chdir(current_dir)

    data = data.fillna(method='ffill')

    return data.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
