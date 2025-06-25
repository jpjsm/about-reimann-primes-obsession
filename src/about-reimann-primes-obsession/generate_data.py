import matplotlib.pyplot as plt
import numpy as np
import pickle
from decimal import Decimal, getcontext
from pathlib import Path
from datetime import datetime, timedelta

ctx = getcontext()
ctx.prec = 100  # Set precision
spotsaver = Path("SpotSaver.pkl")
data = {}
if spotsaver.exists():
    with open("SpotSaver.pkl", "rb") as infile:
        data = pickle.load(infile)

    start = datetime.now()
    for i in range(len(data["x"])):
        delta = datetime.now() - start
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(
            f"{datetime.now().isoformat(timespec='seconds'): <30} {days: >2}d {hours: >2}H {minutes: >2}M {seconds: >2}S -> {data["x"][i]: >32,} {data['y_frac'][i] : >48,.36f} {data['y_float'][i]: >48,.36f}"
        )

else:
    data["exp"] = 0
    data["i"] = 0
    data["harmonic_dec"] = Decimal(0)
    data["harmonic_float"] = 0.0
    data["x"] = []
    data["y_frac"] = []
    data["y_float"] = []
start = datetime.now()
for i in range(data["i"] + 1, (10**24) + 1):
    data["i"] = i
    data["harmonic_dec"] += Decimal(1) / Decimal(i)
    data["harmonic_float"] += 1.0 / i

    if i == 10 ** data["exp"]:
        data["exp"] += 1
        data["x"].append(i)
        data["y_frac"].append(data["harmonic_dec"])
        data["y_float"].append(data["harmonic_float"])

        with open("SpotSaver.pkl", "wb") as outfile:
            pickle.dump(data, outfile)

        delta = datetime.now() - start
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(
            f"{datetime.now().isoformat(timespec='seconds'): <30} {days: >2}d {hours: >2}h {minutes: >2}m {seconds: >2}s -> {i: >32,} {data['harmonic_dec'] : >48,.36f} {data['harmonic_float']: >48,.36f}"
        )

    if (i % 1_000_000) == 0:
        with open("SpotSaver.pkl", "wb") as outfile:
            pickle.dump(data, outfile)
