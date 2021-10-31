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

NegadosGreedy = []
NegadosGreedy.append(np.average(sim1.Negados[0]))
NegadosGreedy.append(np.average(sim2.Negados[0]))
NegadosGreedy.append(np.average(sim3.Negados[0]))
NegadosGreedy.append(np.average(sim4.Negados[0]))
NegadosGreedy.append(np.average(sim5.Negados[0]))

NegadosNancy = []
NegadosNancy.append(np.average(sim1.Negados[1]))
NegadosNancy.append(np.average(sim2.Negados[1]))
NegadosNancy.append(np.average(sim3.Negados[1]))
NegadosNancy.append(np.average(sim4.Negados[1]))
NegadosNancy.append(np.average(sim5.Negados[1]))

#NegadosRamdom = []
#NegadosRamdom.append(np.average(sim1.Negados[2]))
#NegadosRamdom.append(np.average(sim2.Negados[2]))
#NegadosRamdom.append(np.average(sim3.Negados[2]))
#NegadosRamdom.append(np.average(sim4.Negados[2]))
#NegadosRamdom.append(np.average(sim5.Negados[2]))

NegadosBest = []
NegadosBest.append(np.average(sim1.Negados[3]))
NegadosBest.append(np.average(sim2.Negados[3]))
NegadosBest.append(np.average(sim3.Negados[3]))
NegadosBest.append(np.average(sim4.Negados[3]))
NegadosBest.append(np.average(sim5.Negados[3]))

NegadosWorst = []
NegadosWorst.append(np.average(sim1.Negados[4]))
NegadosWorst.append(np.average(sim2.Negados[4]))
NegadosWorst.append(np.average(sim3.Negados[4]))
NegadosWorst.append(np.average(sim4.Negados[4]))
NegadosWorst.append(np.average(sim5.Negados[4]))


NegadosGWO = []
NegadosGWO.append(np.average(sim1.Negados[5]))
NegadosGWO.append(np.average(sim2.Negados[5]))
NegadosGWO.append(np.average(sim3.Negados[5]))
NegadosGWO.append(np.average(sim4.Negados[5]))
NegadosGWO.append(np.average(sim5.Negados[5]))


NomesMetodos = ['Greedy', 'NANCY', 'Best', 'Worst', 'REALTEC']

ci_NegadosGreedy = []
ci_NegadosGreedy.append(mean_confidence_interval(sim1.Negados[0])[3])
ci_NegadosGreedy.append(mean_confidence_interval(sim2.Negados[0])[3])
ci_NegadosGreedy.append(mean_confidence_interval(sim3.Negados[0])[3])
ci_NegadosGreedy.append(mean_confidence_interval(sim4.Negados[0])[3])
ci_NegadosGreedy.append(mean_confidence_interval(sim5.Negados[0])[3])

ci_NegadosNancy = []
ci_NegadosNancy.append(mean_confidence_interval(sim1.Negados[1])[3])
ci_NegadosNancy.append(mean_confidence_interval(sim2.Negados[1])[3])
ci_NegadosNancy.append(mean_confidence_interval(sim3.Negados[1])[3])
ci_NegadosNancy.append(mean_confidence_interval(sim4.Negados[1])[3])
ci_NegadosNancy.append(mean_confidence_interval(sim5.Negados[1])[3])
     
#ci_NegadosRamdom = []
#ci_NegadosRamdom.append(mean_confidence_interval(sim1.Negados[2])[3])
#ci_NegadosRamdom.append(mean_confidence_interval(sim2.Negados[2])[3])
#ci_NegadosRamdom.append(mean_confidence_interval(sim3.Negados[2])[3])
#ci_NegadosRamdom.append(mean_confidence_interval(sim4.Negados[2])[3])
#ci_NegadosRamdom.append(mean_confidence_interval(sim5.Negados[2])[3])

ci_NegadosBest = []
ci_NegadosBest.append(mean_confidence_interval(sim1.Negados[3])[3])
ci_NegadosBest.append(mean_confidence_interval(sim2.Negados[3])[3])
ci_NegadosBest.append(mean_confidence_interval(sim3.Negados[3])[3])
ci_NegadosBest.append(mean_confidence_interval(sim4.Negados[3])[3])
ci_NegadosBest.append(mean_confidence_interval(sim5.Negados[3])[3])

ci_NegadosWorst = []
ci_NegadosWorst.append(mean_confidence_interval(sim1.Negados[4])[3])
ci_NegadosWorst.append(mean_confidence_interval(sim2.Negados[4])[3])
ci_NegadosWorst.append(mean_confidence_interval(sim3.Negados[4])[3])
ci_NegadosWorst.append(mean_confidence_interval(sim4.Negados[4])[3])
ci_NegadosWorst.append(mean_confidence_interval(sim5.Negados[4])[3])

ci_NegadosGWO = []
ci_NegadosGWO.append(mean_confidence_interval(sim1.Negados[5])[3])
ci_NegadosGWO.append(mean_confidence_interval(sim2.Negados[5])[3])
ci_NegadosGWO.append(mean_confidence_interval(sim3.Negados[5])[3])
ci_NegadosGWO.append(mean_confidence_interval(sim4.Negados[5])[3])
ci_NegadosGWO.append(mean_confidence_interval(sim5.Negados[5])[3])

print("NEGADOS")
print("Greedy")
print(NegadosGreedy)
print(ci_NegadosGreedy)
print("Nancy")
print(NegadosNancy)
print(ci_NegadosNancy)
print("GWO")
print(NegadosGWO)
print(ci_NegadosGWO)
print("Best")
print(NegadosBest)
print(ci_NegadosBest)
print("Worst")
print(NegadosWorst)
print(ci_NegadosWorst)


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
rects1 = ax.bar(r1, NegadosGreedy, width, color='blue', label='Greedy', yerr = ci_NegadosGreedy)
rects2 = ax.bar(r2, NegadosNancy, width, color='green', label='Nancy',yerr = ci_NegadosNancy)
rects3 = ax.bar(r3, NegadosGWO, width, color='red', label='Ratec', yerr = ci_NegadosGWO)
#rects4 = ax.bar(r4, NegadosBest, width, color='purple', label='Best', yerr = ci_NegadosBest)
#rects5 = ax.bar(r5, NegadosWorst, width, color='black', label='Worst', yerr = ci_NegadosWorst)


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of services denied', fontsize=12, fontweight='bold')
#ax.set_title('Denied Services')
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
##plt.errorbar(numCars, NegadosNancy, label=NomesMetodos[1], color='red', linestyle='solid',  marker='s', markerfacecolor='red', yerr = ci_NegadosNancy )
##plt.errorbar(numCars, NegadosRamdom, label=NomesMetodos[2], color='green', linestyle='dotted',  marker='^', markerfacecolor='green',  yerr = ci_NegadosRamdom )
##plt.errorbar(numCars, NegadosBest, label=NomesMetodos[3], color='purple', linestyle='dashdot',  marker='D', markerfacecolor='purple',  yerr = ci_NegadosBest )
##plt.errorbar(numCars, NegadosWorst, label=NomesMetodos[4], color='black', linestyle='dashed',  marker='P', markerfacecolor='black',  yerr = ci_NegadosWorst )
plt.legend(loc='best', fontsize=12)
##plt.title("Blocked Services")
##plt.ylabel("Number of services blocked")
plt.xlabel("Number of UEs", fontsize=12, fontweight='bold')
plt.tick_params(axis='both', labelsize=12)
##plt.xticks(numCars,[str(i) for i in numCars])
###plt.xaxis(min(numCars),max(numCars)+1)

plt.show()


