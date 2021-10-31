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

ServicosGreedy = []
ServicosGreedy.append(np.average(sim1.Servicos[0]))
ServicosGreedy.append(np.average(sim2.Servicos[0]))
ServicosGreedy.append(np.average(sim3.Servicos[0]))
ServicosGreedy.append(np.average(sim4.Servicos[0]))
ServicosGreedy.append(np.average(sim5.Servicos[0]))

ServicosNancy = []
ServicosNancy.append(np.average(sim1.Servicos[1]))
ServicosNancy.append(np.average(sim2.Servicos[1]))
ServicosNancy.append(np.average(sim3.Servicos[1]))
ServicosNancy.append(np.average(sim4.Servicos[1]))
ServicosNancy.append(np.average(sim5.Servicos[1]))

#ServicosRamdom = []
#ServicosRamdom.append(np.average(sim1.Servicos[2]))
#ServicosRamdom.append(np.average(sim2.Servicos[2]))
#ServicosRamdom.append(np.average(sim3.Servicos[2]))
#ServicosRamdom.append(np.average(sim4.Servicos[2]))
#ServicosRamdom.append(np.average(sim5.Servicos[2]))

ServicosBest = []
ServicosBest.append(np.average(sim1.Servicos[3]))
ServicosBest.append(np.average(sim2.Servicos[3]))
ServicosBest.append(np.average(sim3.Servicos[3]))
ServicosBest.append(np.average(sim4.Servicos[3]))
ServicosBest.append(np.average(sim5.Servicos[3]))

ServicosWorst = []
ServicosWorst.append(np.average(sim1.Servicos[4]))
ServicosWorst.append(np.average(sim2.Servicos[4]))
ServicosWorst.append(np.average(sim3.Servicos[4]))
ServicosWorst.append(np.average(sim4.Servicos[4]))
ServicosWorst.append(np.average(sim5.Servicos[4]))

ServicosGWO = []
ServicosGWO.append(np.average(sim1.Servicos[5]))
ServicosGWO.append(np.average(sim2.Servicos[5]))
ServicosGWO.append(np.average(sim3.Servicos[5]))
ServicosGWO.append(np.average(sim4.Servicos[5]))
ServicosGWO.append(np.average(sim5.Servicos[5]))


NomesMetodos = ['Greedy', 'NANCY', 'Best', 'Worst', 'REALTEC']

ci_ServicosGreedy = []
ci_ServicosGreedy.append(mean_confidence_interval(sim1.Servicos[0])[3])
ci_ServicosGreedy.append(mean_confidence_interval(sim2.Servicos[0])[3])
ci_ServicosGreedy.append(mean_confidence_interval(sim3.Servicos[0])[3])
ci_ServicosGreedy.append(mean_confidence_interval(sim4.Servicos[0])[3])
ci_ServicosGreedy.append(mean_confidence_interval(sim5.Servicos[0])[3])

ci_ServicosNancy = []
ci_ServicosNancy.append(mean_confidence_interval(sim1.Servicos[1])[3])
ci_ServicosNancy.append(mean_confidence_interval(sim2.Servicos[1])[3])
ci_ServicosNancy.append(mean_confidence_interval(sim3.Servicos[1])[3])
ci_ServicosNancy.append(mean_confidence_interval(sim4.Servicos[1])[3])
ci_ServicosNancy.append(mean_confidence_interval(sim5.Servicos[1])[3])
     
#ci_ServicosRamdom = []
#ci_ServicosRamdom.append(mean_confidence_interval(sim1.Servicos[2])[3])
#ci_ServicosRamdom.append(mean_confidence_interval(sim2.Servicos[2])[3])
#ci_ServicosRamdom.append(mean_confidence_interval(sim3.Servicos[2])[3])
#ci_ServicosRamdom.append(mean_confidence_interval(sim4.Servicos[2])[3])
#ci_ServicosRamdom.append(mean_confidence_interval(sim5.Servicos[2])[3])

ci_ServicosBest = []
ci_ServicosBest.append(mean_confidence_interval(sim1.Servicos[3])[3])
ci_ServicosBest.append(mean_confidence_interval(sim2.Servicos[3])[3])
ci_ServicosBest.append(mean_confidence_interval(sim3.Servicos[3])[3])
ci_ServicosBest.append(mean_confidence_interval(sim4.Servicos[3])[3])
ci_ServicosBest.append(mean_confidence_interval(sim5.Servicos[3])[3])

ci_ServicosWorst = []
ci_ServicosWorst.append(mean_confidence_interval(sim1.Servicos[4])[3])
ci_ServicosWorst.append(mean_confidence_interval(sim2.Servicos[4])[3])
ci_ServicosWorst.append(mean_confidence_interval(sim3.Servicos[4])[3])
ci_ServicosWorst.append(mean_confidence_interval(sim4.Servicos[4])[3])
ci_ServicosWorst.append(mean_confidence_interval(sim5.Servicos[4])[3])

ci_ServicosGWO = []
ci_ServicosGWO.append(mean_confidence_interval(sim1.Servicos[5])[3])
ci_ServicosGWO.append(mean_confidence_interval(sim2.Servicos[5])[3])
ci_ServicosGWO.append(mean_confidence_interval(sim3.Servicos[5])[3])
ci_ServicosGWO.append(mean_confidence_interval(sim4.Servicos[5])[3])
ci_ServicosGWO.append(mean_confidence_interval(sim5.Servicos[5])[3])

print("ATENDIDOS")
print("Greedy")
print(ServicosGreedy)
print(ci_ServicosGreedy)
print("Nancy")
print(ServicosNancy)
print(ci_ServicosNancy)
print("GWO")
print(ServicosGWO)
print(ci_ServicosGWO)
print("Best")
print(ServicosBest)
print(ci_ServicosBest)
print("Worst")
print(ServicosWorst)
print(ci_ServicosWorst)


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
rects1 = ax.bar(r1, ServicosGreedy, width, color='blue', label='Greedy', yerr = ci_ServicosGreedy)
rects2 = ax.bar(r2, ServicosNancy, width, color='green', label='Nancy',yerr = ci_ServicosNancy)
#rects3 = ax.bar(r3, ServicosRamdom, width, color='green', label='Random', yerr = ci_ServicosRamdom)
rects3 = ax.bar(r3, ServicosGWO, width, color='red', label='Ratec', yerr = ci_ServicosGWO)
#rects4 = ax.bar(r4, ServicosBest, width, color='purple', label='Best', yerr = ci_ServicosBest)
#rects5 = ax.bar(r5, ServicosWorst, width, color='black', label='Worst', yerr = ci_ServicosWorst)


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of services attempted', fontsize=12, fontweight='bold')
#ax.set_title('Cars Attempt')
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
##plt.errorbar(numCars, ServicosNancy, label=NomesMetodos[1], color='red', linestyle='solid',  marker='s', markerfacecolor='red', yerr = ci_ServicosNancy )
##plt.errorbar(numCars, ServicosRamdom, label=NomesMetodos[2], color='green', linestyle='dotted',  marker='^', markerfacecolor='green',  yerr = ci_ServicosRamdom )
##plt.errorbar(numCars, ServicosBest, label=NomesMetodos[3], color='purple', linestyle='dashdot',  marker='D', markerfacecolor='purple',  yerr = ci_ServicosBest )
##plt.errorbar(numCars, ServicosWorst, label=NomesMetodos[4], color='black', linestyle='dashed',  marker='P', markerfacecolor='black',  yerr = ci_ServicosWorst )
plt.legend(loc='1', fontsize=12)
##plt.title("Blocked Services")
##plt.ylabel("Number of services blocked")
plt.xlabel("Number of UEs", fontsize=12, fontweight='bold')
plt.tick_params(axis='both', labelsize=12)
##plt.xticks(numCars,[str(i) for i in numCars])
###plt.xaxis(min(numCars),max(numCars)+1)

plt.show()


