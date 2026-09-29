from pathlib import Path
import zipfile
root=Path('outputs/carwise')
html=(root/'index.html').read_text(encoding='utf-8')
html=html.replace('<link rel="stylesheet" href="styles.css">','<style>\n'+(root/'styles.css').read_text(encoding='utf-8')+'\n</style>')
for name in ('engine.js','app.js'):
    html=html.replace(f'<script src="{name}"></script>','<script>\n'+(root/name).read_text(encoding='utf-8')+'\n</script>')
Path('outputs/Carwise.html').write_text(html,encoding='utf-8')
with zipfile.ZipFile('outputs/Carwise-project.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.iterdir()):
        if p.is_file(): z.write(p,'carwise/'+p.name)
print('Created standalone HTML and source ZIP')
