p='index.html';s=open(p,encoding='utf-8').read()
def R(a,b):
    global s
    assert a in s, "NOT FOUND: "+a[:100]
    s=s.replace(a,b)

# ===== paleta: dorado más saturado, verde-negro como las imágenes =====
R("--bg:#0F1411; --bg2:#19211C; --bg3:#232D26; --ink:#F1F2EC; --ink2:#A4AEA6; --line:#2E3A32;",
  "--bg:#0B0F0C; --bg2:#141A16; --bg3:#1D2620; --ink:#F1F2EC; --ink2:#9AA69D; --line:#2B3830;")
R("--plata:#E3BE4A; --plata-bg:#3A3218; --mierda:#B8865A; --mierda-bg:#3A2A1E;",
  "--plata:#F0C64A; --plata-bg:#3A3013; --mierda:#B8865A; --mierda-bg:#3A2A1E;")

# ===== PORTADA con la moneda de fondo =====
R('''<section class="screen on" id="portada">
  <div class="hero">''','''<section class="screen on" id="portada">
  <div class="portadaImg"></div>
  <div class="hero">''')
R('''.hero{margin:40px 0 24px}''','''.portadaImg{background:url(img/portada.jpg) center 42% / cover no-repeat;border-radius:10px;aspect-ratio:9/11;margin:0 0 18px;box-shadow:0 12px 30px rgba(0,0,0,.55);position:relative}
.portadaImg::after{content:"";position:absolute;left:0;right:0;bottom:0;height:45%;background:linear-gradient(transparent,var(--bg));border-radius:0 0 10px 10px}
#portada{justify-content:flex-start;padding-top:14px}
.hero{margin:-38px 0 20px;position:relative;z-index:2}''')
R('  <div class="eyebrow">Versión de prueba · 0.1</div>\n','')
R('<h1><span class="p">Plata</span><br>o <span class="m">Mierda</span></h1>','<h1><span class="p">Plata</span><br>o <span class="m">Mierda</span></h1>')
R("h1{font-size:clamp(56px,19vw,96px);text-transform:uppercase;margin:0}",
  "h1{font-size:clamp(52px,17vw,88px);text-transform:uppercase;margin:0;text-shadow:0 4px 18px rgba(0,0,0,.8)}")
R("<button class=\"btn\" id=\"bRandom\">Tirar <small>El equipo te toca. No se elige. Así es esto.</small></button>",
  "<button class=\"btn oro\" id=\"bRandom\">Tirar <small>El equipo te toca. No se elige. Así es esto.</small></button>")
R(".btn{display:block;width:100%;padding:15px 16px;font-size:17px;font-weight:700;background:var(--ink);color:var(--bg);margin-top:10px;text-align:left}",
  """.btn{display:block;width:100%;padding:15px 16px;font-size:17px;font-weight:700;background:var(--ink);color:var(--bg);margin-top:10px;text-align:left}
.btn.oro{background:linear-gradient(180deg,#F7DA7A,#C99A20);color:#241a02;border:1px solid #8a6a10;box-shadow:0 4px 14px rgba(240,198,74,.25);font-family:"Anton",sans-serif;font-size:22px;letter-spacing:.06em;text-transform:uppercase;text-align:center;padding:14px}
.btn.oro small{color:#3a2c05;opacity:.85;font-family:"Archivo",sans-serif;font-size:12.5px;letter-spacing:0;text-transform:none;font-weight:400}""")

# ===== ENTRADA ÉPICA con la imagen =====
R("""function epico(done){
  const d=document.createElement('div'); d.className='epic'; d.innerHTML='<div class="w p">Plata</div><div class="w">o</div><div class="w m">Mierda</div>';
  document.body.appendChild(d);
  const ws=d.querySelectorAll('.w'); const vib=(ms)=>{try{navigator.vibrate&&navigator.vibrate(ms)}catch(e){}};
  const hit=(i)=>{ws[i].classList.add('hit'); d.classList.remove('shake'); void d.offsetWidth; d.classList.add('shake'); vib(i===2?160:80); SFX.play(i===2?'impactofinal':'impacto')};
  setTimeout(()=>hit(0),150); setTimeout(()=>hit(1),650); setTimeout(()=>hit(2),1150);
  setTimeout(()=>{d.classList.remove('shake');d.classList.add('zoom')},1900);
  setTimeout(()=>{d.remove();done()},2600);
}""",
"""function epico(done){
  const d=document.createElement('div'); d.className='epic'; d.innerHTML='<div class="epicImg" id="epicImg"></div>';
  document.body.appendChild(d);
  const img=d.querySelector('.epicImg');
  const vib=(ms)=>{try{navigator.vibrate&&navigator.vibrate(ms)}catch(e){}};
  const golpe=(cls,ms,snd)=>{ img.classList.remove('g1','g2','g3'); void img.offsetWidth; img.classList.add(cls); d.classList.remove('shake'); void d.offsetWidth; d.classList.add('shake'); vib(ms); SFX.play(snd) };
  setTimeout(()=>golpe('g1',80,'impacto'),120);
  setTimeout(()=>golpe('g2',80,'impacto'),700);
  setTimeout(()=>golpe('g3',170,'impactofinal'),1280);
  setTimeout(()=>{d.classList.remove('shake');d.classList.add('polvo')},2100);
  setTimeout(()=>{d.remove();done()},2900);
}""")
R('''.epic .w{font-family:"Anton",sans-serif;font-size:clamp(72px,24vw,150px);line-height:.92;text-transform:uppercase;opacity:0;transform:scale(9);will-change:transform,opacity}
.epic .w.hit{animation:slam .42s cubic-bezier(.15,.9,.25,1) forwards}
@keyframes slam{0%{opacity:0;transform:scale(9) translateY(-6%)}55%{opacity:1;transform:scale(.94)}78%{transform:scale(1.07)}100%{opacity:1;transform:scale(1)}}''',
'''.epic .epicImg{width:100%;height:100%;background:url(img/epica.jpg) center/cover no-repeat;opacity:0;transform:scale(6);will-change:transform,opacity}
.epic .epicImg.g1{animation:slam1 .5s cubic-bezier(.15,.9,.25,1) forwards}
.epic .epicImg.g2{animation:slam2 .5s cubic-bezier(.15,.9,.25,1) forwards}
.epic .epicImg.g3{animation:slam3 .6s cubic-bezier(.15,.9,.25,1) forwards}
@keyframes slam1{0%{opacity:0;transform:scale(6)}60%{opacity:.55;transform:scale(1.5)}100%{opacity:.55;transform:scale(1.45)}}
@keyframes slam2{0%{opacity:.55;transform:scale(1.45)}60%{opacity:.85;transform:scale(1.18)}100%{opacity:.85;transform:scale(1.15)}}
@keyframes slam3{0%{opacity:.85;transform:scale(1.15)}45%{opacity:1;transform:scale(.99)}70%{transform:scale(1.05)}100%{opacity:1;transform:scale(1)}}
.epic.polvo{animation:polvito .8s ease-in forwards}
@keyframes polvito{0%{filter:blur(0);opacity:1;transform:scale(1)}100%{filter:blur(14px);opacity:0;transform:scale(1.22)}}''')
R('.epic{position:fixed;left:0;top:0;width:100%;height:100%;background:var(--bg);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0;z-index:50;overflow:hidden}',
  '.epic{position:fixed;left:0;top:0;width:100%;height:100%;background:#000;display:flex;align-items:center;justify-content:center;z-index:50;overflow:hidden}')
R('@media (prefers-reduced-motion:reduce){.epic .w{opacity:1;transform:none;animation:none}.epic.shake,.epic.zoom{animation:none}}',
  '@media (prefers-reduced-motion:reduce){.epic .epicImg{opacity:1;transform:none;animation:none}.epic.shake,.epic.polvo{animation:none}}')

# ===== ARCO con foto de fondo y grilla alineada =====
R('''  sh.innerHTML=`<div class="eyebrow">${titulo}</div><p class="sit">${sit}</p><div class="arco"><div class="red">${cells.join("")}<div class="gk" id="gk">${GK_IDLE}${GK_ARMS}</div></div></div><p class="sub">${modo==="patear"?"Tocá un casillero del arco para patear.":"Tocá un casillero para elegir a dónde te tirás."}</p>`;
  const gk=$('#gk');gk.querySelector('svg:first-child').classList.add('idle');gk.querySelector('svg:last-child').classList.add('arms');''',
'''  const foto=modo==="patear"?"arco-patear":"arco-atajar";
  sh.innerHTML=`<div class="eyebrow">${titulo}</div><p class="sit">${sit}</p><div class="arcoFoto ${foto}"><div class="red">${cells.join("")}</div></div><p class="sub">${modo==="patear"?"Tocá un casillero del arco para patear.":"Tocá un casillero para elegir a dónde te tirás."}</p>`;''')
R('''.arco{margin:12px 0 4px;background:linear-gradient(var(--pasto),var(--pasto2));padding:14px 10px 6px;border-radius:8px;position:relative}''',
'''.arcoFoto{position:relative;margin:12px 0 4px;border-radius:8px;overflow:hidden;aspect-ratio:9/16;max-height:46vh;background:#000 center/cover no-repeat;box-shadow:0 8px 24px rgba(0,0,0,.5)}
.arcoFoto.arco-patear{background-image:url(img/arco-patear.jpg)}
.arcoFoto.arco-atajar{background-image:url(img/arco-atajar.jpg)}
.arcoFoto .red{position:absolute;border:0;background:none;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(3,1fr);aspect-ratio:auto}
.arcoFoto.arco-patear .red{left:5.5%;top:44.5%;width:89%;height:15.8%}
.arcoFoto.arco-atajar .red{left:1.5%;top:48.4%;width:97%;height:21.9%}
.arcoFoto .cell{border:1px solid rgba(240,198,74,.28);background:rgba(0,0,0,.05)}
.arcoFoto .cell:hover,.arcoFoto .cell:focus-visible{background:rgba(240,198,74,.35)}
.arcoFoto .cell.pick{background:rgba(240,198,74,.6);box-shadow:inset 0 0 14px rgba(255,255,255,.5)}
.arcoFoto .cell.gkcell{background:rgba(226,91,74,.55);box-shadow:inset 0 0 14px rgba(255,120,100,.7)}
.arcoFoto .cell.ball::after{content:"";position:absolute;inset:0;margin:auto;width:34%;aspect-ratio:1;border-radius:50%;background:#fff;box-shadow:inset -3px -3px 0 #999,0 0 10px rgba(255,255,255,.6)}
.arco{margin:12px 0 4px;background:linear-gradient(var(--pasto),var(--pasto2));padding:14px 10px 6px;border-radius:8px;position:relative}''')
# el arquero: en vez de mover el SVG, marcar su celda
R("      const k=keeperAI();gk.style.left=colPos(k.c);gk.style.bottom=rowBottom(k.r);\n      setTimeout(()=>{gk.classList.add('stretch');",
  "      const k=keeperAI();\n      setTimeout(()=>{const kc=sh.querySelector(`.cell[data-r=\"${k.r}\"][data-c=\"${k.c}\"]`); if(kc)kc.classList.add('gkcell');")
R("      const s=shooterAI();gk.style.left=colPos(c);gk.style.bottom=rowBottom(r);\n      setTimeout(()=>{gk.classList.add('stretch');",
  "      const s=shooterAI();\n      setTimeout(()=>{const kc=sh.querySelector(`.cell[data-r=\"${r}\"][data-c=\"${c}\"]`); if(kc)kc.classList.add('gkcell');")
open(p,'w',encoding='utf-8').write(s);print('ok',len(s))
