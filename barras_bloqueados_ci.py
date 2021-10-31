import resSim1 as sim1
import resSim2 as sim2
import resSim3 as sim3
import resSim4 as sim4
import resSim5 as sim5
import random
import time
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h, h*6

numCars = [sim1.nCars, sim2.nCars, sim3.nCars, sim4.nCars, sim5.nCars]

print(numCars)

BloqueiosGreedy = []
BloqueiosGreedy.append(np.average(sim1.Bloqueios[0]))
BloqueiosGreedy.append(np.average(sim2.Bloqueios[0]))
BloqueiosGreedy.append(np.average(sim3.Bloqueios[0]))
BloqueiosGreedy.append(np.average(sim4.Bloqueios[0]))
BloqueiosGreedy.append(np.average(sim5.Bloqueios[0]))

BloqueiosNancy = []
BloqueiosNancy.append(np.average(sim1.Bloqueios[1]))
BloqueiosNancy.append(np.average(sim2.Bloqueios[1]))
BloqueiosNancy.append(np.average(sim3.Bloqueios[1]))
BloqueiosNancy.append(np.average(sim4.Bloqueios[1]))
BloqueiosNancy.append(np.average(sim5.Bloqueios[1]))

BloqueiosRamdom = []
BloqueiosRamdom.append(np.average(sim1.Bloqueios[2]))
BloqueiosRamdom.append(np.average(sim2.Bloqueios[2]))
BloqueiosRamdom.append(np.average(sim3.Bloqueios[2]))
BloqueiosRamdom.append(np.average(sim4.Bloqueios[2]))
BloqueiosRamdom.append(np.average(sim5.Bloqueios[2]))

BloqueiosBest = []
BloqueiosBest.append(np.average(sim1.Bloqueios[3]))
BloqueiosBest.append(np.average(sim2.Bloqueios[3]))
BloqueiosBest.append(np.average(sim3.Bloqueios[3]))
BloqueiosBest.append(np.average(sim4.Bloqueios[3]))
BloqueiosBest.append(np.average(sim5.Bloqueios[3]))

BloqueiosWorst = []
BloqueiosWorst.append(np.average(sim1.Bloqueios[4]))
BloqueiosWorst.append(np.average(sim2.Bloqueios[4]))
BloqueiosWorst.append(np.average(sim3.Bloqueios[4]))
BloqueiosWorst.append(np.average(sim4.Bloqueios[4]))
BloqueiosWorst.append(np.average(sim5.Bloqueios[4]))


BloqueiosGWO = []
BloqueiosGWO.append(np.average(sim1.Bloqueios[5]))
BloqueiosGWO.append(np.average(sim2.Bloqueios[5]))
BloqueiosGWO.append(np.average(sim3.Bloqueios[5]))
BloqueiosGWO.append(np.average(sim4.Bloqueios[5]))
BloqueiosGWO.append(np.average(sim5.Bloqueios[5]))


NomesMetodos = ['Greedy', 'NANCY', 'Best', 'Worst', 'REALTEC']

ci_BloqueiosGreedy = []
ci_BloqueiosGreedy.append(mean_confidence_interval(sim1.Bloqueios[0])[3])
ci_BloqueiosGreedy.append(mean_confidence_interval(sim2.Bloqueios[0])[3])
ci_BloqueiosGreedy.append(mean_confidence_interval(sim3.Bloqueios[0])[3])
ci_BloqueiosGreedy.append(mean_confidence_interval(sim4.Bloqueios[0])[3])
ci_BloqueiosGreedy.append(mean_confidence_interval(sim5.Bloqueios[0])[3])

ci_BloqueiosNancy = []
ci_BloqueiosNancy.append(mean_confidence_interval(sim1.Bloqueios[1])[3])
ci_BloqueiosNancy.append(mean_confidence_interval(sim2.Bloqueios[1])[3])
ci_BloqueiosNancy.append(mean_confidence_interval(sim3.Bloqueios[1])[3])
ci_BloqueiosNancy.append(mean_confidence_interval(sim4.Bloqueios[1])[3])
ci_BloqueiosNancy.append(mean_confidence_interval(sim5.Bloqueios[1])[3])
     
ci_BloqueiosRamdom = []
ci_BloqueiosRamdom.append(mean_confidence_interval(sim1.Bloqueios[2])[3])
ci_BloqueiosRamdom.append(mean_confidence_interval(sim2.Bloqueios[2])[3])
ci_BloqueiosRamdom.append(mean_confidence_interval(sim3.Bloqueios[2])[3])
ci_BloqueiosRamdom.append(mean_confidence_interval(sim4.Bloqueios[2])[3])
ci_BloqueiosRamdom.append(mean_confidence_interval(sim5.Bloqueios[2])[3])

ci_BloqueiosBest = []
ci_BloqueiosBest.append(mean_confidence_interval(sim1.Bloqueios[3])[3])
ci_BloqueiosBest.append(mean_confidence_interval(sim2.Bloqueios[3])[3])
ci_BloqueiosBest.append(mean_confidence_interval(sim3.Bloqueios[3])[3])
ci_BloqueiosBest.append(mean_confidence_interval(sim4.Bloqueios[3])[3])
ci_BloqueiosBest.append(mean_confidence_interval(sim5.Bloqueios[3])[3])

ci_BloqueiosWorst = []
ci_BloqueiosWorst.append(mean_confidence_interval(sim1.Bloqueios[4])[3])
ci_BloqueiosWorst.append(mean_confidence_interval(sim2.Bloqueios[4])[3])
ci_BloqueiosWorst.append(mean_confidence_interval(sim3.Bloqueios[4])[3])
ci_BloqueiosWorst.append(mean_confidence_interval(sim4.Bloqueios[4])[3])
ci_BloqueiosWorst.append(mean_confidence_interval(sim5.Bloqueios[4])[3])

ci_BloqueiosGWO = []
ci_BloqueiosGWO.append(mean_confidence_interval(sim1.Bloqueios[5])[3])
ci_BloqueiosGWO.append(mean_confidence_interval(sim2.Bloqueios[5])[3])
ci_BloqueiosGWO.append(mean_confidence_interval(sim3.Bloqueios[5])[3])
ci_BloqueiosGWO.append(mean_confidence_interval(sim4.Bloqueios[5])[3])
ci_BloqueiosGWO.append(mean_confidence_interval(sim5.Bloqueios[5])[3])

print("BLOQUEIOS")
print("Greedy")
print(BloqueiosGreedy)
print(ci_BloqueiosGreedy)
print("Nancy")
print(BloqueiosNancy)
print(ci_BloqueiosNancy)
print("GWO")
print(BloqueiosGWO)
print(ci_BloqueiosGWO)
print("Best")
print(BloqueiosBest)
print(ci_BloqueiosBest)
print("Worst")
print(BloqueiosWorst)
print(ci_BloqueiosWorst)


labels = numCars

x = np.arange(len(labels))  # the label locations
width = 0.28  # the width of the bars

r1 = np.arange(len(labels))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]
r4 = [x + width for x in r3]
r5 = [x + width for x in r4]
r6 = [x + width for x in r5]

fig, ax = plt.subplots()
rects1 = ax.bar(r1, BloqueiosGreedy, width, color='blue', label='Greedy', yerr = ci_BloqueiosGreedy)
rects2 = ax.bar(r2, BloqueiosNancy, width, color='green', label='Nancy',yerr = ci_BloqueiosNancy)
rects3 = ax.bar(r3, BloqueiosGWO, width, color='red', label='Ratec', yerr = ci_BloqueiosGWO)
#rects4 = ax.bar(r4, BloqueiosBest, width, color='purple', label='Best', yerr = ci_BloqueiosBest)
#rects5 = ax.bar(r5, BloqueiosWorst, width, color='black', label='Worst', yerr = ci_BloqueiosWorst)


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of services blocked', fontsize=12, fontweight='bold')
#ax.set_title('Blocked Services')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = int(rect.get_height())
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 20),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


##autolabel(rects1)
##autolabel(rects2)
##autolabel(rects3)
##autolabel(rects4)
##autolabel(rects5)


fig.tight_layout()
##plt.errorbar(numCars, BloqueiosNancy, label=NomesMetodos[1], color='red', linestyle='solid',  marker='s', markerfacecolor='red', yerr = ci_BloqueiosNancy )
##plt.errorbar(numCars, BloqueiosRamdom, label=NomesMetodos[2], color='green', linestyle='dotted',  marker='^', markerfacecolor='green',  yerr = ci_BloqueiosRamdom )
##plt.errorbar(numCars, BloqueiosBest, label=NomesMetodos[3], color='purple', linestyle='dashdot',  marker='D', markerfacecolor='purple',  yerr = ci_BloqueiosBest )
##plt.errorbar(numCars, BloqueiosWorst, label=NomesMetodos[4], color='black', linestyle='dashed',  marker='P', markerfacecolor='black',  yerr = ci_BloqueiosWorst )
plt.legend(loc='best',fontsize=12)
##plt.title("Blocked Services")
##plt.ylabel("Number of services blocked")
plt.xlabel("Number of UEs", fontsize=12, fontweight='bold')
plt.tick_params(axis='both', labelsize=12)
##plt.xticks(numCars,[str(i) for i in numCars])
###plt.xaxis(min(numCars),max(numCars)+1)

plt.show()


