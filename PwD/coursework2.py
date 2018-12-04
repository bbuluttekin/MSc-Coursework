import json
from collections import Counter
import time
import datetime
from random import randint, seed
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

seed(404)


def myHealthcare(n=1000, output="dictionary"):
    """
    Simulates n number of observations in specified range and returns
    data frame.

    Parameters:
    ===========
    n : (int) Number of observations you want to simulate.

    output: (str) Sets the type of the output format.
    Available formats: Dictionary, json, numpy array, list
    """
    temperature = [randint(36, 39) for i in range(n)]
    heart_rate = [randint(55, 100) for i in range(n)]
    pulse = [randint(55, 100) for i in range(n)]
    blood_pressure = [randint(120, 121) for i in range(n)]
    respiratory_rate = [randint(11, 17) for i in range(n)]
    oxygen_saturation = [randint(93, 100) for i in range(n)]
    ph = [randint(71, 76) / 10 for i in range(n)]
    ts = []
    current_time = datetime.datetime(2018, 12, 9)
    time_step = datetime.timedelta(seconds=5)
    while len(ts) < n:
        ts.append(current_time)  # .strftime('%Y-%m-%d %H:%M:%S')
        current_time += time_step

    simulated_data = {"ts": ts,
                      "temp": temperature,
                      "hr": heart_rate,
                      "pulse": pulse,
                      "bloodpr": blood_pressure,
                      "resrate": respiratory_rate,
                      "oxsat": oxygen_saturation,
                      "ph": ph}

    if output == "dictionary":
        return simulated_data
    elif output == "json":
        return json.dumps(simulated_data)
    elif output == "array":
        return np.array([i for i in zip(ts,
                                        temperature,
                                        heart_rate,
                                        pulse,
                                        blood_pressure,
                                        respiratory_rate,
                                        oxygen_saturation,
                                        ph
                                        )])
    elif output == "list":
        lst_format = []
        for t, te, he, pu, bl, re, ox, p in zip(ts,
                                                temperature,
                                                heart_rate,
                                                pulse,
                                                blood_pressure,
                                                respiratory_rate,
                                                oxygen_saturation,
                                                ph):
            lst_format.append([t, te, he, pu, bl, re, ox, p])
        return lst_format


def abnormalSignAnalytics(data, n=50, variable="pulse"):
    """
    Samples the data and detects abnormal values in given value.
    """
    sample_data = {}

    for col, values in data.items():
        sample_data[col] = values[: n]

    def pulse_abnormal(x): return x < 60 or x > 99

    def blood_abnormal(x): return x > 120

    abnormal_val = []
    count = 0
    for i in sample_data[variable]:
        if variable == "pulse":
            if pulse_abnormal(i):
                count += 1
                index = sample_data[variable].index(i)
                abnormal_val.append([sample_data["ts"][index],
                                     sample_data[variable][index]])
        if variable == "bloodpr":
            if blood_abnormal(i):
                count += 1
                index = sample_data[variable].index(i)
                abnormal_val.append([sample_data["ts"][index],
                                     sample_data[variable][index]])
        if variable != "pulse" and variable != "bloodpr":
            raise ValueError("Only pulse and bloodpr variables excepted!")
    return [variable, count, abnormal_val]


def frequencyAnalytics(data, n=50):
    """
    Calculates the frequency of values in the sampled data.
    """
    sample_data = {}

    for col, values in data.items():
        sample_data[col] = values[:n]

    freq = Counter(sample_data['pulse'])
    ts = [i for i, j in abnormalSignAnalytics(data, n=n)[2]]
    ab_val = [j for i, j in abnormalSignAnalytics(data, n=n)[2]]

    plt.style.use('seaborn-white')
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    ax[1].hist(sample_data['pulse'], 50)
    ax[1].set_xlabel('Pulse \n 2B')
    ax[1].set_ylabel('Frequency')
    ax[1].set_title('Histogram of Pulse frequency')
    ax[0].plot(sample_data["ts"], sample_data["pulse"])
    ax[0].plot(ts, ab_val, "o")
    ax[0].axhline(y=100, color='r')
    ax[0].axhline(y=59, color='r')
    for tick in ax[0].get_xticklabels():
        tick.set_rotation(45)
    ax[0].set_xlabel('Time \n 2A')
    ax[0].set_ylabel('Pulse')
    ax[0].set_title('Plot of abnormal values vs pulse rates over a time')
    plt.show()
    return freq


def plotAnalyticsComplexity():
    return NotImplementedError


def HealthAnalyzer(data, value=56, method="naive"):
    """
    Search function for health data searches for specific pulse value.
    """
    if method == "naive":
        val_list = []
        for i in data:
            if i[3] == value:
                val_list.append(i)
        return val_list
    if method == "binary":
        data = sorted(data, key=lambda x: x[3])
        return data


def benchmarking():
    return NotImplementedError


# print(myHealthcare(output='array')[:10])

#print(HealthAnalyzer(myHealthcare(n=20, output="list"), method="binary"))
#print(HealthAnalyzer(myHealthcare(n=20, output="list"), method="naive"))
print(myHealthcare(n=30))
print(abnormalSignAnalytics(myHealthcare(n=30), n=30))
