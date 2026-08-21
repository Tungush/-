import json

path = r'c:\Users\22881\Desktop\Гениратор ТЗ\bitrix_fields.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build index by formLabel/listLabel
by_label = {}
for fid, finfo in data.items():
    for key in ('formLabel', 'listLabel', 'filterLabel', 'title'):
        label = finfo.get(key, '')
        if label and label != fid:
            by_label.setdefault(label.strip(), []).append(fid)

# CMK-relevant labels to find
SEARCH = [
    'Заказ клиента', 'Подразделение', 'Группа проект', 'Наша компания',
    'Руководитель', 'Утверждающ', 'Требуемая дата', 'Дата отгруз',
    'Размер предоплаты', 'Проект', 'Конечный заказчик', 'Регион',
    'Направление деятельности', 'Склад выдачи', 'Пункт доставки',
    'Проектная документ', 'Комплектац', 'Компания, от которой',
    'Заказ поставщ', 'GUID', '1С', 'факт', 'производ',
    'Сайт', 'Клиент', 'ORGANIZATION', 'PM', 'Связан',
    'Заказ клиента (1С)', 'ответ 1С', 'Тип клиента', 'CLIENT',
    'Проект клиента', 'Склад', 'Комплектация',
    'Подразделение ЦМК', 'Группа проектов',
]

lines = []
lines.append('=== MATCH BY LABEL (partial) ===')
for search in SEARCH:
    for label, fids in sorted(by_label.items()):
        if search.lower() in label.lower():
            for fid in fids:
                finfo = data[fid]
                t = finfo.get('type')
                req = finfo.get('isRequired')
                items = finfo.get('items') or []
                line = f'{search!r:30} | {label:45} | {fid:25} | {t}'
                if req: line += ' | REQUIRED'
                lines.append(line)
                if items and len(items) <= 15:
                    for it in items:
                        lines.append(f'    enum: ID={it.get("ID")} VALUE={it.get("VALUE")}')

# All unique formLabels containing CMK-related words
lines.append('\n=== ALL CMK-RELATED LABELS ===')
cmk_words = ['цмк', 'заказ', 'склад', 'производ', 'отгруз', 'предоплат', 'комплект', '1с', 'guid', 'поставщ', 'номенклат']
for label in sorted(by_label.keys()):
    if any(w in label.lower() for w in cmk_words):
        for fid in by_label[label]:
            finfo = data[fid]
            lines.append(f'{label} | {fid} | {finfo.get("type")}')

# STAGE_ID statuses
if 'STAGE_ID' in data:
    st = data['STAGE_ID']
    items = st.get('items') or []
    lines.append(f'\n=== STAGE_ID items: {len(items)} ===')
    for it in items:
        if 'C56' in str(it.get('ID','')) or '56' in str(it.get('STATUS_ID','')) or 'цмк' in str(it.get('VALUE','')).lower() or 'CMK' in str(it.get('ID','')).upper():
            lines.append(f'  {it}')
    # print all if few CMK matches, else search STATUS_ID pattern
    cmk_stages = [it for it in items if '56' in str(it.get('STATUS_ID', it.get('ID','')))]
    lines.append(f'CMK stages found: {len(cmk_stages)}')
    for it in cmk_stages:
        lines.append(f'  STATUS_ID={it.get("STATUS_ID", it.get("ID"))} | {it.get("VALUE")}')

out = r'c:\Users\22881\Desktop\Гениратор ТЗ\_extracted\bitrix_labels.txt'
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('lines', len(lines))
