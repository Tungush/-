import json, re

path = r'c:\Users\22881\Desktop\Гениратор ТЗ\bitrix_fields.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

keywords = ['комплект', 'конечн', 'тип кли', 'проектн', 'guid', 'поставщ', 'выставл', '1с', 'заказ клиента', 'заказ постав', 'клиент', 'физ', 'юр']
lines = []
for fid, finfo in sorted(data.items()):
    labels = [finfo.get(k,'') for k in ('formLabel','listLabel','filterLabel','title')]
    text = ' | '.join(str(l) for l in labels if l).lower()
    if any(k in text for k in keywords):
        fl = finfo.get('formLabel') or finfo.get('title') or fid
        if fl == fid and not any(k in text for k in keywords if k not in ['guid','1с','клиент']):
            continue
        items = finfo.get('items') or []
        line = f'{fid:30} | {fl:55} | {finfo.get("type")}'
        lines.append(line)
        if items and len(items) <= 20:
            for it in items:
                lines.append(f'    {it.get("ID")}: {it.get("VALUE")}')

# Also search PARENT_ID or crm_entity for smart processes
for fid, finfo in sorted(data.items()):
    if finfo.get('type') == 'crm_entity' or 'PARENT_ID' in fid:
        fl = finfo.get('formLabel') or finfo.get('title') or fid
        lines.append(f'{fid:30} | {fl:55} | {finfo.get("type")}')

# STAGE_ID
if 'STAGE_ID' in data:
    st = data['STAGE_ID']
    lines.append(f'\nSTAGE_ID type={st.get("type")} items={len(st.get("items") or [])}')
    lines.append(str(st)[:2000])

out = r'c:\Users\22881\Desktop\Гениратор ТЗ\_extracted\bitrix_search2.txt'
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(len(lines))
