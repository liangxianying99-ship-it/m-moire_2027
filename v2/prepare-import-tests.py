"""Prepare synthetic import fixtures. Development only; requires openpyxl."""
from pathlib import Path
import openpyxl,zipfile,json
p=Path('/tmp/research-import-fixtures');p.mkdir(exist_ok=True)
terms=json.loads((Path(__file__).parent/'seed.json').read_text())
headers=['序号','中文原文','原文位置','Deepseek V3.2 深度思考模式','Deepseek V3.2 深度思考模式 中文释义','Deepseek V3.2 深度思考模式 翻译方法','Deepseek V3.2 深度思考模式 原句','GPT-6 思考模式','GPT-6 思考模式 中文释义','GPT-6 思考模式 翻译方法','GPT-6 思考模式 原句','François Cheng, Anne Cheng译本','François Cheng, Anne Cheng译本 中文释义','François Cheng, Anne Cheng译本 翻译方法','François Cheng, Anne Cheng译本 原句']
w=openpyxl.Workbook();s=w.active;s.title='社会文化负载词';s.append(['合成测试样例，非研究数据']);s.append([]);s.append(headers);s.append([1,'作寿','第1章·第1段','fêter son anniversaire','庆祝生日','保留类：语言性（非文化性）翻译','Il voulait fêter son anniversaire.','célébrer son anniversaire',None,None,'Il voulait célébrer son anniversaire.','fêter un anniversaire',None,None,'On allait fêter un anniversaire.']);w.save(p/'filled.xlsx')
xml='<?xml version="1.0" encoding="UTF-8"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>他们为老人作寿。</w:t></w:r></w:p><w:p><w:r><w:t>第二段并没有目标词。</w:t></w:r></w:p></w:body></w:document>'
with zipfile.ZipFile(p/'source.docx','w',zipfile.ZIP_DEFLATED) as z:z.writestr('word/document.xml',xml)
(p/'deep.txt').write_text('Ils voulaient fêter son anniversaire.\nUn autre paragraphe.')
print('Synthetic import fixtures prepared')
