import os, sys
sys.path.append(os.path.abspath('.'))

from weather_au import summary

w = summary.Summary(search='parkville+vic')

print(w.summary_text())
