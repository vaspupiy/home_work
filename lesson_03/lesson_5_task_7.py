import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    total = [{}, {'average_profit': 0}]
    n_profit_firm = 0
    profit = 0
    for line in f.readlines():
        firm = line.split()
        total[0][firm[0] + ', ' + firm[1]] = int(firm[2]) - int(firm[3])
        if total[0][firm[0] + ', ' + firm[1]] >= 0:
            n_profit_firm += 1
            profit += total[0][firm[0] + ', ' + firm[1]]
    total[1]['average_profit'] = profit / n_profit_firm

with open('text_7_result.json', 'w', encoding='utf-8') as fj:
    json.dump(total, fj, indent=4, ensure_ascii=False)
