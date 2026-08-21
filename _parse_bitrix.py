import json
import re

path = r'c:\Users\22881\Desktop\Гениратор ТЗ\bitrix_fields.json'
out = r'c:\Users\22881\Desktop\Гениратор ТЗ\_extracted\bitrix_fields_report.txt'
map_out = r'c:\Users\22881\Desktop\Гениратор ТЗ\_extracted\bitrix_mapping.json'

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Keywords for CMK integration fields
KEYWORDS = [
    'заказ', 'подраздел', 'проект', 'компан', 'руковод', 'утвержд',
    'дата', 'предоплат', 'конечн', 'регион', 'направлен', 'склад',
    'доставк', 'документ', 'комплект', 'номенклат', 'клиент', 'поставщ',
    'guid', '1с', '1c', 'производ', 'отгруз', 'сайт', 'организац',
    'соглас', 'связан', 'коммент', 'тип кли', 'группа', 'бин',
    'факт', 'план', 'артикул', 'логист', 'эсф', 'наклад',
]

lines = []
mapping = []

for fid, finfo in sorted(data.items(), key=lambda x: x[0]):
    if not isinstance(finfo, dict):
        continue
    title = (finfo.get('title') or finfo.get('formLabel') or finfo.get('listLabel') or '').strip()
    ftype = finfo.get('type') or finfo.get('userTypeId') or ''
    items = finfo.get('items') or []
    
    title_lower = title.lower()
    is_relevant = (
        fid.startswith('UF_CRM_') or
        fid in ('ID', 'TITLE', 'CATEGORY_ID', 'STAGE_ID', 'COMPANY_ID', 'OPPORTUNITY', 'CURRENCY_ID', 'ASSIGNED_BY_ID') or
        any(k in title_lower for k in KEYWORDS)
    )
    
    entry = {
        'id': fid,
        'title': title,
        'type': ftype,
        'isRequired': finfo.get('isRequired') or finfo.get('mandatory'),
        'items': [{'ID': i.get('ID'), 'VALUE': i.get('VALUE')} for i in items if isinstance(i, dict)] if items else []
    }
    mapping.append(entry)
    
    if is_relevant:
        lines.append(f'=== {fid} ===')
        lines.append(f'  title: {title}')
        lines.append(f'  type: {ftype}')
        if entry['isRequired']:
            lines.append(f'  required: {entry["isRequired"]}')
        if items:
            lines.append(f'  items ({len(items)}):')
            for it in items[:40]:
                if isinstance(it, dict):
                    lines.append(f'    ID={it.get("ID")} | VALUE={it.get("VALUE")}')
            if len(items) > 40:
                lines.append(f'    ... +{len(items)-40} more')
        lines.append('')

with open(out, 'w', encoding='utf-8') as f:
    f.write(f'Total fields: {len(data)}\nUF_CRM: {sum(1 for k in data if k.startswith("UF_CRM_"))}\n\n')
    f.write('\n'.join(lines))

with open(map_out, 'w', encoding='utf-8') as f:
    json.dump(mapping, f, ensure_ascii=False, indent=2)

print('report:', out)
print('mapping:', map_out)
print('total', len(data), 'uf', sum(1 for k in data if k.startswith('UF_CRM_')))
