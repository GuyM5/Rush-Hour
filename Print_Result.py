import numpy as np
import torch
import matplotlib.pyplot as plt
#deafult reward: 10 for win , +0.1 for step close and -0.1 for step backwards
# קובץ 4 LR = 0.0001 כל 5000 מוסיף עוד רכב
# קובץ 5 LR = 0.0001 כל 10000 מוסיף עוד רכב
# קובץ 6 LR = 0.0001 כל 10000 מוסיף רכב אחד עם פרס של 0.2 לפי כל כיוון
# קובץ 7 LR = 0.0001 כל 5000 מוסיף רכב אחד עם פרס של 0.2 לפי כל כיוון
# קובץ 8 LR = 0.0001 כל 10000 מוסיף רכב אחד עם פרס של 0.2 לפי כל כיוון 
# קובץ 9 זהה ל8 רק עושים עליו דיבאג
#קובץ 10 LR = 0.01 כל 10000 מוסיף רכב אחד עם פרס של 0.2 לפי כל כיוון 
#קובץ 11 LR = 0.001 כל 12000 מוסיף רכב אחד עם פרס של 0.2 לפי כל כיוון
#קובץ 12 LR = 0.001 כל 12000 מוסיף רכב אחד עם פרס של 0.1 לפי כל כיוון
#קובץ 13 LR = 0.0001 כל 12000 מוסיף רכב אחד עם פרס של 0.1 לפי כל כיוון
###-------Trainer------------------------
#קובץ 14 LR = 0.0001 כל 10000 מוסיף רכב אחד עם פרס0.1 לכיוון
#קובץ 15 LR = 0.0001 כל 10000 מוסיף רכב אחד עם פרס0.2 לכיוון

Directory = 'Data'
Files_num = [14,15]
results_path = []
random_results_path = []
for num in Files_num:
    file = f'results_{num}.pth'
    results_path.append(file)
    file = f'random_results_{num}.pth'
    random_results_path.append(file)

results = []
for path in results_path:
    results.append(torch.load(Directory+'/'+path))

random_results = []
for path in random_results_path:
    random_results.append(torch.load(Directory+'/'+path))

for i in range(len(results)):
    print(results_path[i], max(results[i]['results']), np.argmax(results[i]['results']), len(results[i]['results']))
    results[i]['avglosses'] = list(filter(lambda k:  0< k <100, results[i]['avglosses'] ))

with torch.no_grad():
    for i in range(len(results)):
        fig, ax_list = plt.subplots(3,1)
        fig.suptitle(results_path[i])
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
        ax_list[0].plot(results[i]['results'])
        ax_list[1].plot(random_results[i])
        ax_list[2].plot(results[i]['avglosses']) 
        plt.tight_layout()

plt.show()