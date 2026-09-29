from pathlib import Path
p=Path('outputs/carwise/app.js')
s=p.read_text(encoding='utf-8')
s=s.replace('สรุปอาการเพื่อประกอบการตรวจ</p></div></div>${draft?', 'สรุปอาการเพื่อประกอบการตรวจ</p></div></div></div>${draft?')
s=s.replace('หากต้องการเริ่มใหม่ ใช้ปุ่มเริ่มเคสใหม่','หากต้องการเริ่มใหม่ ใช้ปุ่มล้างแบบร่าง')
s=s.replace("${draft.answers.length?'<button", "<div class=\"divider\"></div><button class=\"text-link\" data-action=\"reset-draft\">ล้างแบบร่างและเริ่มใหม่</button>${draft.answers.length?'<button")
s=s.replace("else if(a==='demo')demo();", "else if(a==='reset-draft'){if(window.confirm('ล้างเฉพาะแบบร่างนี้และเริ่มใหม่? เคสที่บันทึกแล้วจะยังอยู่')){draft=null;persist();go('home')}}else if(a==='demo')demo();")
s=s.replace("if(cases.some(x=>x.id===c.id)){toast('มีรหัสเคสนี้แล้ว ไฟล์เดิมจะไม่ถูกเขียนทับ');return;}", "const existing=cases.findIndex(x=>x.id===c.id);if(existing>=0&&!window.confirm('พบรหัสเคสเดิม ต้องการแทนที่ด้วยข้อมูลจากไฟล์นี้หรือไม่? ควรส่งออกเคสเดิมไว้ก่อน'))return;")
s=s.replace("cases.unshift(imported);persist();", "if(existing>=0)cases[existing]=imported;else cases.unshift(imported);persist();")
# A required mark should not force a separate line in a flex-column label.
s=s.replace('ยี่ห้อ / รุ่นรถ <span class="required">*</span>', '<span>ยี่ห้อ / รุ่นรถ <span class="required">*</span></span>')
p.write_text(s,encoding='utf-8')
