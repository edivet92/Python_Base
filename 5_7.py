import json
with open('resul.json', 'w', encoding='utf-8') as carrot:
    with open('text5_7.txt', 'r', encoding='utf-8') as firms:
        voc_firms = {}
        profit = 0
        for line in firms:
            firm_name = line[:line.find(" ")]
            proseeds_list = list(map(int, "".join(i for i in line if '0' <= i <= '9' or i == " ").split()))
            revenue = proseeds_list[0] - proseeds_list[1]
            if revenue >= 0:
                profit += revenue
            voc_firms[firm_name] = revenue
        average_profit = profit / len(voc_firms)
        final_list = [voc_firms, {'average_profit': profit / len(voc_firms)}]
        print(final_list)
    json.dump(final_list, carrot, indent=2, ensure_ascii=False)