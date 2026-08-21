import json, re

path = r'c:\Users\22881\Desktop\Гениратор ТЗ\bitrix_fields.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Print full metadata for CMK-relevant fields found by enum values
TARGET_IDS = [
    'UF_CRM_1733494955',  # prepayment %
    'UF_CRM_1744896704',  # ACTIVITY CMK
    'UF_CRM_1761221968757',  # delivery point
    'UF_CRM_1761222082',  # iblock - warehouse?
    'UF_CRM_1762861520',
    'UF_CRM_1776410250',
    'UF_CRM_1747210029',
    'UF_CRM_1751373674',
    'UF_CRM_1707998114',
    'UF_CRM_1707998503',
    'UF_CRM_1690169191',
    'UF_CRM_1690169216',
    'UF_CRM_1695959583',
    'UF_CRM_1722838069',
    'UF_CRM_1761634508',
    'UF_CRM_1755844579',
    'UF_CRM_1721728435',
    'UF_CRM_1721728466',
    'UF_CRM_1768977461',  # crm - kit?
    'UF_CRM_1752662025',
    'UF_CRM_1755267110',
    'UF_CRM_1721712374',
    'UF_CRM_1716963585',
    'UF_CRM_1734616709',
    'UF_CRM_1736519656',
    'UF_CRM_1752832825',
    'UF_CRM_1754462560',
    'UF_CRM_1748958727',
    'UF_CRM_1720602525007',
    'UF_CRM_1743773583',
    'UF_CRM_1743774058',
    'UF_CRM_1745475319042',
    'UF_CRM_1745475372851',
    'UF_CRM_1761646229793',
    'UF_CRM_1761803104459',
    'UF_CRM_1775741479135',
    'UF_CRM_1776144193626',
    'UF_CRM_1776144992737',
    'UF_CRM_1728643943',
    'UF_CRM_1728653780',
    'UF_CRM_1699868867936',
    'UF_CRM_1699868885804',
    'UF_CRM_1699868897916',
    'UF_CRM_1766416206142',
    'UF_CRM_1764313823',
    'UF_CRM_1752554725307',
    'UF_CRM_1709189980',
    'UF_CRM_1761806538582',
    'UF_CRM_1761806582927',
    'UF_CRM_1761643215004',
    'UF_CRM_1761736812715',
    'UF_CRM_1726643225',
    'UF_CRM_1726643258',
    'UF_CRM_1746525501598',
    'UF_CRM_1746525533096',
    'UF_CRM_1782398428946',
    'UF_CRM_1782398774783',
    'UF_CRM_1762861653744',
    'UF_CRM_1762861667177',
    'UF_CRM_1754905306118',
    'UF_CRM_1755176636122',
    'UF_CRM_1749039012954',
    'UF_CRM_1776144086668',
    'UF_CRM_1776409922842',
    'UF_CRM_1728643157',
    'UF_CRM_1728643207',
    'UF_CRM_1728643717',
    'UF_CRM_1728643797',
    'UF_CRM_1691061522',
    'UF_CRM_1691061574',
    'UF_CRM_1721821582',
    'UF_CRM_1712655484',
    'UF_CRM_1698122453',
    'UF_CRM_1698124622',
    'UF_CRM_1698146293',
    'UF_CRM_1706274250',
    'UF_CRM_1722867358',
    'UF_CRM_1726150091',
    'UF_CRM_1754462454',
    'UF_CRM_1761634981',
    'UF_CRM_1785222223',
    'UF_CRM_1747291699',
    'UF_CRM_1719837619',
    'UF_CRM_1667760345',
    'UF_CRM_1674826014',
    'UF_CRM_1722496233',
    'UF_CRM_1721820611',
    'UF_CRM_1721820934',
    'UF_CRM_1752663182',
    'UF_CRM_1752663539',
    'UF_CRM_1747209895',
    'UF_CRM_1739539921',
    'UF_CRM_3834411152636',
    'UF_CRM_1709113227',  # region?
    'UF_CRM_1747213696241',
    'UF_CRM_1761221407151',
    'UF_CRM_1728641720',
    'UF_CRM_1728642400',
    'UF_CRM_1728642442',
    'UF_CRM_1756291374',
    'UF_CRM_1756291386',
    'UF_CRM_1756291400',
    'UF_CRM_1756291428',
    'UF_CRM_1756291460',
    'UF_CRM_1756291500',
    'UF_CRM_1756291521',
    'UF_CRM_1776410544520',
    'UF_CRM_1777541207629',
    'UF_CRM_1778563768958',
    'UF_CRM_1778584578245',
    'UF_CRM_1778584642482',
    'UF_CRM_1781085927590',
    'UF_CRM_1781085937532',
    'UF_CRM_1782368775994',
    'UF_CRM_1782370849316',
    'UF_CRM_1755514565005',
    'UF_CRM_1755514636981',
    'UF_CRM_1755514936719',
    'UF_CRM_1755515217593',
    'UF_CRM_1755515440202',
    'UF_CRM_1746430055845',
    'UF_CRM_1746696611',
    'UF_CRM_1747043933299',
    'UF_CRM_1722519481',
    'UF_CRM_1722519499',
    'UF_CRM_1722519514',
    'UF_CRM_1722519621',
    'UF_CRM_1712655375',
    'UF_CRM_1712655400',
    'UF_CRM_1712655531',
    'UF_CRM_1712655594',
    'UF_CRM_1712655614',
    'UF_CRM_1712655632',
    'UF_CRM_1712655679',
    'UF_CRM_1712655701',
    'UF_CRM_1712655722',
    'UF_CRM_1712655749',
    'UF_CRM_1712655765',
    'UF_ONEC_GUID',
    'UF_CRM_1696331830205',
    'UF_CRM_1743502641396',
    'UF_CRM_1747633240072',
    'UF_CRM_1747633601911',
    'UF_CRM_1747646213915',
    'UF_CRM_1746430159402',
    'UF_CRM_1754459726594',
    'UF_CRM_1754905185286',
    'UF_CRM_1763624574',
    'UF_CRM_1775220067844',
    'UF_CRM_1695959129006',
    'UF_CRM_1698812862550',
    'UF_CRM_1698816090552',
    'UF_CRM_1765539308475',
    'UF_CRM_1765373368231',
    'UF_CRM_1762780595925',
    'UF_CRM_1762861280726',
    'UF_CRM_1762861308584',
    'UF_CRM_1762149276463',
    'UF_CRM_1762409410483',
    'UF_CRM_1758102005981',
    'UF_CRM_1756766787095',
    'UF_CRM_1757058733560',
    'UF_CRM_1757059335202',
    'UF_CRM_1757076796186',
    'UF_CRM_1757308888620',
    'UF_CRM_1757308928508',
    'UF_CRM_1755241378',
    'UF_CRM_1751519650835',
    'UF_CRM_1751952830276',
    'UF_CRM_1743502490465',
    'UF_CRM_1736323632',
    'UF_CRM_1733205619',
    'UF_CRM_1725884223',
    'UF_CRM_1722953876',
    'UF_CRM_1721914588',
    'UF_CRM_1722248478',
    'UF_CRM_1722504781',
    'UF_CRM_1722837975',
    'UF_CRM_1712656417',
    'UF_CRM_1713249781',
    'UF_CRM_1710252214728',
    'UF_CRM_1692597555804',
    'UF_CRM_1692597591192',
    'UF_CRM_1692599968621',
    'UF_CRM_1692599995461',
    'UF_CRM_1691061627458',
    'UF_CRM_1691061639385',
    'UF_CRM_1666782686',
    'UF_CRM_1666782828',
    'UF_CRM_1666782875',
    'UF_CRM_1666782989',
    'UF_CRM_1666783421',
    'UF_CRM_1667281404',
    'UF_CRM_1667909648',
    'UF_CRM_1668599304',
    'UF_CRM_1712656167',
    'UF_CRM_1744896002',
    'UF_CRM_1744896051',
    'UF_CRM_1712655484',
    'UF_CRM_1698122453',
    'UF_CRM_1698124622',
    'UF_CRM_1698146293',
    'UF_CRM_1706274250',
    'UF_CRM_1726150091',
    'UF_CRM_1754462454',
    'UF_CRM_1761634981',
    'UF_CRM_1785222223',
    'UF_CRM_1747291699',
    'UF_CRM_1719837619',
    'UF_CRM_1667760345',
    'UF_CRM_1674826014',
    'UF_CRM_1722496233',
    'UF_CRM_1721820611',
    'UF_CRM_1721820934',
    'UF_CRM_1752663182',
    'UF_CRM_1752663539',
    'UF_CRM_1747209895',
    'UF_CRM_1739539921',
    'UF_CRM_3834411152636',
]

out_lines = []
for fid in TARGET_IDS:
    if fid not in data:
        continue
    finfo = data[fid]
    out_lines.append(f'\n===== {fid} =====')
    for k in sorted(finfo.keys()):
        v = finfo[k]
        if k == 'items' and v:
            out_lines.append(f'  items:')
            for it in v[:15]:
                out_lines.append(f'    {it}')
        elif k == 'settings' and v:
            out_lines.append(f'  settings: {json.dumps(v, ensure_ascii=False)[:300]}')
        else:
            s = str(v)
            if len(s) > 200: s = s[:200] + '...'
            out_lines.append(f'  {k}: {s}')

# Search fields with Russian titles (not equal to field id)
out_lines.append('\n\n===== FIELDS WITH REAL RUSSIAN TITLES =====')
for fid, finfo in data.items():
    title = finfo.get('title', '')
    if title and title != fid and re.search(r'[а-яА-ЯёЁ]', title):
        out_lines.append(f'{fid} | {title} | {finfo.get("type")}')

# Search by keyword in any string value of field
out_lines.append('\n\n===== KEYWORD SEARCH IN ALL FIELD VALUES =====')
keywords = ['Заказ клиента', 'Подразделение', 'Группа проект', 'Наша компан', 'Руководитель', 
            'Утверждающ', 'предоплат', 'Конечный', 'Склад выдачи', 'Пункт доставки',
            'производств', 'отгруз', 'Комплектац', 'Проектная', 'Направление деятельности',
            'Заказ поставщ', 'GUID', '1С', 'Проект клиента', 'Компания, от которой']
raw = json.dumps(data, ensure_ascii=False)
for kw in keywords:
    if kw.lower() in raw.lower():
        # find which fields contain keyword
        for fid, finfo in data.items():
            fs = json.dumps(finfo, ensure_ascii=False)
            if kw.lower() in fs.lower() and title != fid:
                t = finfo.get('title', fid)
                out_lines.append(f'  {kw!r} -> {fid} title={t}')

# STAGE_ID - look for status type fields
if 'STAGE_ID' in data:
    st = data['STAGE_ID']
    out_lines.append('\n\n===== STAGE_ID =====')
    out_lines.append(json.dumps(st, ensure_ascii=False, indent=2)[:5000])

with open(r'c:\Users\22881\Desktop\Гениратор ТЗ\_extracted\bitrix_cmk_fields.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
print('done', len(out_lines))
