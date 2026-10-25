from pathlib import Path
import json,base64,zipfile
p=Path(__file__).parent;root=p.parent
seed=json.loads((p/'seed.json').read_text());assert len(seed)==278
(p/'seed.js').write_text('const INITIAL_TERMS='+json.dumps(seed,ensure_ascii=False).replace('<','\\u003c')+';')
html=(p/'index.html').read_text()
html=html.replace('<link rel="stylesheet" href="style.css">','<style>'+(p/'style.css').read_text()+'</style>')
svg='data:image/svg+xml;base64,'+base64.b64encode((p/'shin.svg').read_bytes()).decode()
for name in ['seed.js','strategies.js','app.js','xlsx.js','vendor/jszip.min.js','importer.js','learning.js']:
 js=(p/name).read_text().replace('src="shin.svg"','src="'+svg+'"')
 html=html.replace('<script src="'+name+'"></script>','<script>'+js+'</script>')
out=root/'downloads';out.mkdir(exist_ok=True)
html=html.replace('</body>','<script type="text/plain" id="third-party-licenses">'+(p/'vendor/JSZIP-LICENSE.md').read_text()+'</script></body>')
f=out/'Research-Studio-v2.html';f.write_text(html);f.chmod(0o644)
readme='''小新研究室 V2 · 章节翻译工作台

1. 解压后，用 Chrome 普通窗口打开 Research-Studio-v2.html，无需 Python、云端部署或注册。
2. 章节工作台：选择第 1—24 章，分别保存中文原文、DeepSeek、GPT-6、人工译本，右侧保存完整指令及学习／翻译阶段记录。
3. 278 项对照表：点“批量导入／识别”，默认导入章节原文及三方 TXT／DOCX；自动找中文词条，生成整章对齐指令，复制到独立 AI 会话，再整表粘贴返回内容，经原句存在性校验后批量导入。并非自动联网调用模型；语义对应仍需核对。也可导入现成 XLSX／CSV／TSV。默认只填空白，保留重复词条和导入前版本。
4. 学习页：六节通用机器翻译原理、实验设计说明及论文来源，支持自己的笔记和学习勾选。
5. 正文自动保存；“保存本章版本”留存快照。指令和词条的编辑会保留旧版。
6. 数据保存在当前浏览器的 IndexedDB 中。每天导出全部 JSON 备份到电脑；切换路径／浏览器或清理数据前务必备份。
7. 旧版应用与其数据保持独立，不自动混入本版。旧版备份不可直接导入新版；请保留旧文件。
8. 五类 Excel 导出为 .xlsx 工作簿，Excel 可打开，严格保留原表 15 列，另附章节关联、Aixélá 策略标注及对齐核对工作表。JSON 备份才包含所有正文、指令和笔记。
9. GPT-6、Deepseek V3.2 为用户表格中的研究列标签，不表示应用已核实对应产品的型号或模式。按使用界面记录实际完整模型名称。

本应用仅记录真实实验，不发送提示词、不调用模型、不自动生成译文。
'''
(out/'V2-README.txt').write_text(readme)
with zipfile.ZipFile(out/'Research-Studio-v2.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.write(f,'Research-Studio-v2/Research-Studio-v2.html');z.writestr('Research-Studio-v2/README.txt',readme);z.write(p/'vendor/JSZIP-LICENSE.md','Research-Studio-v2/JSZIP-LICENSE.txt')
print('Built',f.name,len(html.encode()),'bytes; 278 terms; 24 chapters')
