# Попросил гпт исправить чтение файла на гитхабе, не судите строго, я не знал, как такое фиксится

import json

with open('EDA_F1.ipynb', 'r', encoding='utf-8') as file:
    notebook = json.load(file)

for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        if 'execution_count' not in cell:
            cell['execution_count'] = None

with open('EDA_F1_fixed.ipynb', 'w', encoding='utf-8') as file:
    json.dump(notebook, file, ensure_ascii=False, indent=4)
