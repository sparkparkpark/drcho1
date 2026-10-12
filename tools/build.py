# Regenerates the site pages from shared templates.
# Usage (from the project root): python3 tools/build.py .
import sys, os, html
OUT = sys.argv[1]

PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'
PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
CLOCK = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h16M14 6l6 6-6 6"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.5v15l13-7.5z"/></svg>'
ECG = '<svg class="hero__ecg" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true"><path d="M0 120 H360 L385 120 L400 90 L415 120 L440 120 L455 135 L475 20 L495 175 L515 120 L560 120 L590 100 L620 120 H1200" /></svg>'
TEL = "tel:+12139086434"


def head(title, desc, schema=False):
    s = f'''<!doctype html>
<html lang="ko" class="no-js">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="assets/dr-cho.webp" />
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" />
  <link rel="stylesheet" href="styles.css" />
'''
    if schema:
        s += '''  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Physician","name":"Jae Hyung Cho, MD, PhD","alternateName":"조재형 심장내과","medicalSpecialty":"Cardiovascular","telephone":"+1-213-908-6434","faxNumber":"+1-213-908-5986","address":{"@type":"PostalAddress","streetAddress":"2727 W Olympic Blvd Ste 208","addressLocality":"Los Angeles","addressRegion":"CA","postalCode":"90006","addressCountry":"US"},"openingHours":"Mo-Fr 08:30-17:30","url":"https://www.jhccardiology.com","sameAs":["https://www.youtube.com/@jhccardiology"]}
  </script>
'''
    return s


NAV = [("index.html", "nav.home", "홈"),
       ("doctor.html", "nav.about", "의료진 소개"),
       ("services.html", "nav.services", "진료 안내"),
       ("videos.html", "nav.videos", "영상칼럼"),
       ("contact.html", "nav.contact", "오시는 길")]


def header(active):
    links = "\n".join(
        f'        <a href="{h}" data-i18n="{k}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, k, t in NAV)
    return f'''</head>
<body data-page="{active}">
  <a class="skip" href="#main" data-i18n="skip">본문 바로가기</a>
  <div class="topbar">
    <div class="container topbar__inner">
      <span class="topbar__item">{PIN}<span data-i18n="top.addr">2727 W Olympic Blvd Ste 208, Los Angeles · 한남체인 건너편</span></span>
      <span class="topbar__item topbar__hours">{CLOCK}<span data-i18n="top.hours">월–금 오전 8:30 – 오후 5:30</span></span>
    </div>
  </div>
  <header class="header" id="header">
    <div class="container header__inner">
      <a href="index.html" class="brand" aria-label="Home">
        <img src="assets/logo.webp" alt="조재형 심장내과 Jae Hyung Cho, MD Cardiology" width="500" height="119" />
      </a>
      <nav class="nav" id="nav" aria-label="Main">
{links}
        <a href="{TEL}" class="btn btn--primary nav__call-mobile">{PHONE}<span>(213) 908-6434</span></a>
      </nav>
      <div class="header__actions">
        <div class="lang" role="group" aria-label="Language">
          <button type="button" data-lang="ko" aria-pressed="true">한국어</button>
          <button type="button" data-lang="en" aria-pressed="false">EN</button>
        </div>
        <button class="menu-toggle" id="menuToggle" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span></button>
      </div>
    </div>
  </header>
'''


def page_head(key_title, title, key_desc, desc, crumb_key, crumb):
    return f'''    <section class="page-head">
      {ECG}
      <div class="container">
        <h1 class="page-head__title" data-i18n="{key_title}">{title}</h1>
        <p class="page-head__desc" data-i18n="{key_desc}">{desc}</p>
      </div>
    </section>
'''


def cta(after_dark=False):
    cls = "cta-band cta-band--after-dark" if after_dark else "cta-band"
    return f'''    <section class="{cls}">
      <div class="container">
        <div class="cta-band__inner reveal">
          <div>
            <h2 data-i18n="band.title">심장내과 전문의와 상담하세요</h2>
            <p data-i18n="band.desc">가슴 통증, 두근거림, 숨참, 고혈압이 있으시다면 미루지 말고 진료를 받아보세요.</p>
          </div>
          <div class="cta-band__actions">
            <a href="{TEL}" class="btn btn--gold btn--lg">{PHONE}(213) 908-6434</a>
          </div>
        </div>
      </div>
    </section>
'''


FOOTER = f'''  </main>
  <footer class="footer">
    <div class="container">
      <div class="footer__top">
        <div>
          <p class="footer__name" data-i18n="ft.name">조재형 심장내과</p>
          <p class="footer__sub">Jae Hyung Cho, MD Cardiology</p>
        </div>
        <div>
          <h4>Menu</h4>
          <nav class="footer__nav">
{chr(10).join(f'            <a href="{h}" data-i18n="{k}">{t}</a>' for h, k, t in NAV)}
          </nav>
        </div>
        <div>
          <h4>Contact</h4>
          <p>2727 W Olympic Blvd Ste 208<br />Los Angeles, CA 90006</p>
          <a href="{TEL}" class="footer__tel">(213) 908-6434</a>
          <p>Fax. (213) 908-5986</p>
        </div>
      </div>
      <div class="footer__notice">
        <p><strong>NOTICE TO CONSUMERS:</strong> Medical doctors are licensed and regulated by the Medical Board of California, <a href="tel:+18006332322">(800) 633-2322</a>, <a href="https://www.mbc.ca.gov" target="_blank" rel="noopener">www.mbc.ca.gov</a>.<span class="footer__notice-ko" data-en=""> (의사는 캘리포니아 의료위원회의 면허 및 규제를 받습니다.)</span></p>
        <p>The Open Payments database is a federal tool used to search payments made by drug and device companies to physicians and teaching hospitals. It can be found at <a href="https://openpaymentsdata.cms.gov" target="_blank" rel="noopener">https://openpaymentsdata.cms.gov</a>.<span class="footer__notice-ko" data-en=""> (Open Payments 데이터베이스는 제약 및 의료기기 회사가 의사와 교육병원에 지급한 금액을 검색할 수 있는 연방 정부 도구입니다.)</span></p>
      </div>
      <div class="footer__bottom">
        <p>© <span id="year">2026</span> Jae Hyung Cho, MD Cardiology. All rights reserved.</p>
        <p data-i18n="ft.emergency">응급 상황 시에는 즉시 911에 전화하십시오.</p>
      </div>
    </div>
  </footer>
  <a href="{TEL}" class="fab" aria-label="Call (213) 908-6434">{PHONE}</a>
  <div class="modal" id="videoModal" role="dialog" aria-modal="true" aria-label="Video">
    <div class="modal__box">
      <button class="modal__close" type="button" aria-label="Close">✕</button>
      <div class="modal__frame"></div>
    </div>
  </div>
  <script src="script.js"></script>
</body>
</html>
'''

# ---------------- data ----------------
ICONS = {
    "c1": '<path d="M4 18a8 8 0 1 1 16 0"/><path d="M12 18l4-6"/><circle cx="12" cy="18" r="1.4"/>',
    "c2": '<path d="M3 12h18"/><path d="M3 7c3 0 3 3 6 3s3-3 6-3 3 3 6 3"/><path d="M3 17c3 0 3-3 6-3s3 3 6 3 3-3 6-3"/>',
    "c3": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/><path d="M12 8v4"/><path d="M12 15h.01"/>',
    "c4": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/><path d="M8 11h2l1-2 2 4 1-2h2"/>',
    "c5": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/><path d="M9 13l3-3 3 3"/>',
    "c6": '<path d="M2 12h4l2-5 3 10 3-12 2 7h6"/>',
    "c7": '<path d="M12 3l7 3v5c0 4.5-3 8.5-7 10-4-1.5-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
}
CONDITIONS = [
    ("c1", "고혈압", "Hypertension", "혈압의 정확한 평가와 생활습관 교정, 약물 치료를 통해 심뇌혈관 합병증 예방을 돕습니다."),
    ("c2", "고지혈증", "Hyperlipidemia", "콜레스테롤 수치와 심혈관 위험도를 종합 평가하여 맞춤형 치료 목표를 설정합니다."),
    ("c3", "협심증", "Angina Pectoris", "가슴 통증 및 압박감의 원인을 정밀 검사로 확인하고, 관상동맥 질환의 조기 진단에 힘씁니다."),
    ("c4", "심근경색", "Myocardial Infarction", "심근경색 이후의 회복과 재발 방지를 위한 약물 관리 및 지속적인 추적 진료를 제공합니다."),
    ("c5", "심부전", "Congestive Heart Failure", "숨참, 부종, 피로감 등 증상을 관리하고 최신 가이드라인에 따른 치료로 삶의 질 향상을 돕습니다."),
    ("c6", "부정맥", "Cardiac Arrhythmias", "부정맥 전공 박사로서 심방세동, 두근거림, 실신 등 심장 리듬 이상을 전문적으로 진료합니다."),
    ("c7", "심장질환 예방", "Cardiovascular Prevention", "가족력, 당뇨, 흡연 등 위험 요인을 평가하고 심장 질환을 미리 예방하는 건강 관리를 돕습니다."),
]
TESTS = [
    ("t1", "심장 초음파", "Echocardiogram", "심장의 구조, 판막, 펌프 기능을 초음파로 실시간 확인합니다."),
    ("t2", "운동 부하 검사", "Exercise Stress Test", "운동 중 심전도와 혈압 변화를 관찰하여 관상동맥 질환을 평가합니다."),
    ("t3", "혈관 초음파", "Vascular Ultrasound", "경동맥 및 말초혈관의 협착이나 혈류 이상을 확인합니다."),
    ("t4", "관상동맥 CT", "CT Coronary Angiogram", "관상동맥의 협착과 석회화를 비침습적으로 정밀하게 촬영합니다."),
    ("t5", "심장 MRI", "Cardiac MRI", "심근의 상태와 기능을 고해상도 영상으로 평가합니다."),
]

# (id, category, ko title, en title, radio)
VIDEOS = [
    ("01akByBpCmM", "etc", "판막질환", "Valvular Heart Disease", False),
    ("fdS6sOGYiqA", "etc", "대동맥류", "Aortic Aneurysm", False),
    ("448yZfrONyI", "arr", "심방세동", "Atrial Fibrillation", True),
    ("NOmkPF9E330", "arr", "심실빈맥", "Ventricular Tachycardia", False),
    ("qiLw6xo3uaM", "arr", "심실상성 빈맥", "Supraventricular Tachycardia", False),
    ("DXIbmJDdCkI", "arr", "조기수축", "Premature Contractions", False),
    ("4VDpL5XAzhk", "arr", "심방조동", "Atrial Flutter", False),
    ("f0Jqvc2Z0bc", "arr", "심방세동 2부", "Atrial Fibrillation, Part 2", False),
    ("sSvKU3YRfDo", "arr", "심방세동 1부", "Atrial Fibrillation, Part 1", False),
    ("t6tUCm1UakI", "arr", "부정맥", "Cardiac Arrhythmias", False),
    ("IlMApZhOr54", "arr", "부정맥", "Cardiac Arrhythmias", True),
    ("uLUdJ_MmHBs", "cad", "협심증", "Angina", True),
    ("YZS7h3Iamp8", "cad", "심근경색 2부", "Heart Attack, Part 2", False),
    ("9dlyRwbtdIA", "cad", "심근경색 1부", "Heart Attack, Part 1", False),
    ("LWW3ZHQZ28w", "cad", "협심증 2부", "Angina, Part 2", False),
    ("bYGawoNRa_s", "cad", "협심증 1부", "Angina, Part 1", False),
    ("yXuwpkRCIHQ", "cad", "협심증 · 심근경색", "Angina & Heart Attack", True),
    ("zMy_qnvQsNA", "lip", "고지혈증 2부", "High Cholesterol, Part 2", False),
    ("-m1qUN1gd2g", "lip", "고지혈증 1부", "High Cholesterol, Part 1", False),
    ("wMajxNLWI8g", "htn", "고혈압", "Hypertension", True),
    ("1ECw8oEwW50", "htn", "고혈압 2부", "Hypertension, Part 2", False),
    ("hHIXlTRpBhY", "htn", "고혈압 1부", "Hypertension, Part 1", False),
]
CATS = [("all", "전체", "All"), ("htn", "고혈압", "Hypertension"), ("lip", "고지혈증", "Cholesterol"),
        ("cad", "협심증 · 심근경색", "Angina & Heart Attack"), ("arr", "부정맥", "Arrhythmias"), ("etc", "혈관 · 판막", "Vessels & Valves")]
CAT_LABEL = {c: (k, e) for c, k, e in CATS}


def video_card(v, reveal=True):
    vid, cat, ko, en, radio = v
    tag_ko, tag_en = ("라디오코리아 출연", "Radio Korea") if radio else CAT_LABEL[cat]
    title_ko = html.escape(ko + (" (라디오코리아)" if radio else ""))
    title_en = html.escape(en + (" (Radio Korea)" if radio else ""))
    return f'''          <button type="button" class="video{" reveal" if reveal else ""}" data-video="{vid}" data-cat="{cat}">
            <span class="video__thumb">
              <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360" />
              <span class="video__play">{PLAY}</span>
              <span class="video__tag" data-en="{html.escape(tag_en)}">{html.escape(tag_ko)}</span>
            </span>
            <span class="video__title" data-en="{title_en}">{title_ko}</span>
          </button>'''


def cards_html(link_cta=True):
    out = []
    for k, t, en, d in CONDITIONS:
        if k == "c7":
            out.append(f'''          <article class="card card--feature reveal">
            <div class="card__icon"><svg viewBox="0 0 24 24">{ICONS[k]}</svg></div>
            <h3><span data-i18n="{k}.t">{t}</span><small>{en}</small></h3>
            <p data-i18n="{k}.d">{d}</p>
            <a href="{TEL}" class="card__link" data-i18n="c7.link">상담 예약하기 →</a>
          </article>''')
        else:
            out.append(f'''          <article class="card reveal">
            <div class="card__icon"><svg viewBox="0 0 24 24">{ICONS[k]}</svg></div>
            <h3><span data-i18n="{k}.t">{t}</span><small>{en}</small></h3>
            <p data-i18n="{k}.d">{d}</p>
          </article>''')
    return "\n".join(out)


def tests_html():
    items = "\n".join(f'''          <li class="test reveal">
            <span class="test__no">0{i+1}</span>
            <div><h3><span data-i18n="{k}.t">{t}</span><small>{en}</small></h3><p data-i18n="{k}.d">{d}</p></div>
          </li>''' for i, (k, t, en, d) in enumerate(TESTS))
    return f'''    <section class="section tests" id="tests">
      <div class="container tests__grid">
        <div class="tests__intro reveal">
          <p class="section__kicker section__kicker--light" data-i18n="tests.kicker">심장 내과 검사</p>
          <h2 class="section__title section__title--light" data-i18n="tests.title">정밀한 검사로<br />정확한 진단을 돕습니다</h2>
          <p class="section__desc section__desc--light" data-i18n="tests.desc">심초음파 인증(NBE)을 받은 심장내과 전문의가 직접 검사 결과를 판독하고, 필요한 경우 관상동맥 CT · 심장 MRI 등 고급 영상 검사까지 안내해 드립니다.</p>
        </div>
        <ol class="tests__list">
{items}
        </ol>
      </div>
    </section>
'''


INFO_CARDS = f'''          <div class="info reveal">
            <div class="info__icon">{PIN}</div>
            <div>
              <h3 data-i18n="ct.addr">주소</h3>
              <p>2727 W Olympic Blvd Ste 208<br />Los Angeles, CA 90006</p>
              <p class="info__note" data-i18n="ct.addrNote">올림픽 대로 한남체인 건너편</p>
              <a class="info__link" href="https://maps.google.com/?q=2727+W+Olympic+Blvd+Ste+208,+Los+Angeles,+CA+90006" target="_blank" rel="noopener" data-i18n="ct.dir">길찾기 →</a>
            </div>
          </div>
          <div class="info reveal">
            <div class="info__icon">{CLOCK}</div>
            <div>
              <h3 data-i18n="ct.hours">진료 시간</h3>
              <table class="hours">
                <tr><th data-i18n="ct.wk">월요일 – 금요일</th></tr>
                <tr><td data-i18n="ct.wkTime">오전 8:30 – 오후 5:30</td></tr>
              </table>
            </div>
          </div>
          <div class="info reveal">
            <div class="info__icon">{PHONE}</div>
            <div>
              <h3 data-i18n="ct.phone">연락처</h3>
              <p><span data-i18n="ct.tel">전화</span> <a href="{TEL}" class="info__phone">(213) 908-6434</a></p>
              <p><span data-i18n="ct.fax">팩스</span> (213) 908-5986</p>
            </div>
          </div>'''

# ---------------- index ----------------
latest = "\n".join(video_card(v) for v in VIDEOS[:3])
index = head("조재형 심장내과 | Jae Hyung Cho, MD Cardiology · Los Angeles",
             "LA 한인타운 조재형 심장내과 — 시더스 사이나이 수련, 심장내과·심초음파 전문의. 고혈압, 고지혈증, 협심증, 심부전, 부정맥 진료.", True) + header("index.html") + f'''
  <main id="main">
    <section class="hero">
      {ECG}
      <div class="container hero__grid">
        <div class="hero__text reveal">
          <p class="eyebrow"><span class="pulse-dot"></span><span>Cardiology · Koreatown, Los Angeles</span></p>
          <h1 class="hero__title" data-i18n="hero.title">환자중심의<br />심장내과 진료를<br /><em>약속드립니다</em></h1>
          <p class="hero__lead" data-i18n="hero.lead">조재형 심장내과는 정확한 진단과 근거 중심의 치료를 제공합니다. <br />시더스 사이나이 메디컬 센터에서 수련하고 진료하는 심장내과 전문의가 직접 진료합니다.</p>
          <div class="hero__cta">
            <a href="{TEL}" class="btn btn--primary btn--lg">{PHONE}<span data-i18n="cta.book">진료 예약 (213) 908-6434</span></a>
            <a href="doctor.html" class="btn btn--ghost btn--lg" data-i18n="cta.doctor">의료진 소개</a>
          </div>
          <ul class="hero__badges">
            <li data-i18n="hero.b1">미국 내과 전문의</li>
            <li data-i18n="hero.b2">미국 심장내과 전문의</li>
            <li data-i18n="hero.b3">심초음파 인증 (NBE)</li>
          </ul>
        </div>
        <div class="hero__visual reveal">
          <div class="hero__photo">
            <img src="assets/dr-cho.webp" alt="조재형 원장 Dr. Jae Hyung Cho" width="1500" height="1484" />
          </div>
          <div class="hero__card hero__card--b">
            <span class="hero__card-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M2 12h4l2-5 3 10 3-12 2 7h6"/></svg></span>
            <div><strong>Jae Hyung Cho</strong><span>MD, PhD</span></div>
          </div>
        </div>
      </div>
    </section>

    <section class="stats">
      <div class="container">
        <div class="stats__grid">
          <div class="stat reveal"><div class="stat__num">15<sup>+</sup></div><div class="stat__label" data-i18n="stat1">년 이상의 임상 경험</div></div>
          <div class="stat reveal"><div class="stat__num">Ph.D.</div><div class="stat__label" data-i18n="stat2">시더스 사이나이 부정맥 전공</div></div>
          <div class="stat reveal"><div class="stat__num stat__num--sm">Cleveland Clinic</div><div class="stat__label" data-i18n="stat3">임상조교수 역임</div></div>
          <div class="stat reveal"><div class="stat__num stat__num--sm">Cedars-Sinai</div><div class="stat__label" data-i18n="stat4">현 메디컬 스태프</div></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section__head section__head--row reveal">
          <div>
            <p class="section__kicker" data-i18n="svc.kicker">진료 분야</p>
            <h2 class="section__title" data-i18n="svc.title">심장 질환의 진단부터 관리까지, 한 곳에서</h2>
          </div>
          <a href="services.html" class="more-link"><span data-i18n="svc.all">진료 안내 전체 보기</span>{ARROW}</a>
        </div>
        <div class="cards">
{cards_html()}
        </div>
      </div>
    </section>

{tests_html()}    <section class="section section--soft">
      <div class="container">
        <div class="section__head section__head--row reveal">
          <div>
            <p class="section__kicker" data-i18n="vid.kicker">영상칼럼</p>
            <h2 class="section__title" data-i18n="vid.homeTitle">조재형 원장이 알려드리는 심장 건강</h2>
          </div>
          <a href="videos.html" class="more-link"><span data-i18n="vid.all">영상 전체 보기</span>{ARROW}</a>
        </div>
        <div class="videos">
{latest}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section__head section__head--row reveal">
          <div>
            <p class="section__kicker" data-i18n="ct.kicker">오시는 길</p>
            <h2 class="section__title" data-i18n="ct.title">진료 예약 안내</h2>
          </div>
          <a href="contact.html" class="more-link"><span data-i18n="ct.map">지도 보기</span>{ARROW}</a>
        </div>
        <div class="visit">
{INFO_CARDS}
        </div>
      </div>
    </section>
''' + cta() + FOOTER

# ---------------- doctor ----------------
import json, re
BIB = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bib.json"), encoding="utf-8"))


def t(ko, en, tag="span", cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-en="{html.escape(en)}">{html.escape(ko)}</{tag}>'


def li_list(items, cls="checklist"):
    return f'<ul class="{cls}">' + "".join(f'<li data-en="{html.escape(e)}">{html.escape(k)}</li>' for k, e in items) + "</ul>"


FOCUS = [("부정맥", "Cardiac arrhythmias"), ("관상동맥질환", "Coronary artery disease"), ("심부전", "Heart failure"),
         ("심장초음파", "Echocardiography"), ("심혈관 질환 예방", "Cardiovascular prevention")]
BOARD = [("미국 내과학회(ABIM) 심장내과 전문의", "Board Certified in Cardiovascular Disease, American Board of Internal Medicine"),
         ("미국 내과학회(ABIM) 내과 전문의", "Board Certified in Internal Medicine, American Board of Internal Medicine"),
         ("미국 심초음파 위원회(NBE) 인증 · 성인 종합 심초음파", "National Board of Echocardiography, Adult Comprehensive Echocardiography")]
HONORS = [("미국심장학회(ACC) 젊은 연구자상 최종 후보", "Young Investigator Award finalist, American College of Cardiology"),
          ("미국부정맥학회(HRS) 젊은 연구자상 최종 후보", "Young Investigator Award finalist, Heart Rhythm Society")]
MEMBERS = [("미국심장협회 (AHA) 회원", "Member, American Heart Association"),
           ("미국부정맥학회 (HRS) 회원", "Member, Heart Rhythm Society"),
           ("미국심장학회 (ACC) 회원", "Member, American College of Cardiology")]
PUBS = [
    ("의학 서적 『Arytmier』 중 ‘심장 부정맥의 유전자 및 세포 치료’ 챕터 저술",
     "Author of the chapter “Gene and cell therapy for the treatment of cardiac arrhythmia” in the medical textbook Arytmier"),
    ("Nature, Circulation, European Heart Journal 등에 심장 질환, 심부전 기전, 인공지능(AI) 심기능 평가 연구 게재",
     "Research in Nature, Circulation and the European Heart Journal on heart disease, heart failure mechanisms and AI-based cardiac function assessment"),
    ("JACC: Clinical Electrophysiology, Circulation: Arrhythmia and Electrophysiology 등에 부정맥 기전 및 박출률 보존 심부전(HFpEF) 돌연사 연구 게재",
     "Articles in JACC: Clinical Electrophysiology, Circulation: Arrhythmia and Electrophysiology and others on arrhythmia mechanisms and sudden death in HFpEF"),
    ("PLoS One, American Journal of Medicine 등에 코로나19 환자의 부정맥, 폐색전증 심초음파 예후 인자 연구 게재",
     "Studies in PLoS One, the American Journal of Medicine and others on arrhythmias in COVID-19 and echocardiographic prognosis in pulmonary embolism"),
]
TALKS = [
    ("시더스 사이나이 Smidt 심장 연구소 및 부정맥학회(HRS)에서 HFpEF 심실 부정맥 초청 강연",
     "Invited talks at the Cedars-Sinai Smidt Heart Institute and Heart Rhythm Society on ventricular arrhythmias in HFpEF"),
    ("미국심장학회(ACC) · 미국심장협회(AHA)에서 세포 치료, 코로나19 부정맥, 심장 아밀로이드증 등 다수 발표",
     "Numerous ACC and AHA presentations on cell therapy, arrhythmias in COVID-19, cardiac amyloidosis and more"),
    ("부정맥학회(HRS)에서 HFpEF 돌연사, 심박수 변동성, 심장 유래 세포 치료 효과 발표",
     "HRS presentations on sudden death, heart rate variability and cardiac-derived cell therapy in HFpEF"),
    ("미국내과의학회(ACP), 미국신장학회(ASN), 병원의학회(SHM) 등에서 임상 연구 발표",
     "Clinical research presented at ACP, ASN and the Society of Hospital Medicine"),
]


def fmt_ref(s):
    s = html.escape(s)
    s = re.sub(r"(Cho JH|Jae Hyung Cho)", r"<strong>\1</strong>", s)
    m = re.search(r"PMID: (\d+)", s)
    if m:
        s = s.replace(m.group(0), f'<a href="https://pubmed.ncbi.nlm.nih.gov/{m.group(1)}/" target="_blank" rel="noopener">PMID: {m.group(1)}</a>')
    return s


def acc(title_ko, title_en, count, items, open_=False):
    body = "\n".join(f"<li>{x}</li>" for x in items)
    return f'''          <details class="acc reveal"{" open" if open_ else ""}>
            <summary>{t(title_ko, title_en)}<span class="acc__count">{count}</span></summary>
            <ol class="pubs">
{body}
            </ol>
          </details>'''


papers = [fmt_ref(p) for p in BIB["papers"]]
reviews = [fmt_ref(p) for p in BIB["reviews"]]
book = [fmt_ref(p) for p in BIB["book"]]
abstracts = [f'<span class="pubs__title">{html.escape(a["t"])}</span><span>{fmt_ref(a["a"])}</span><em>{html.escape(a["v"])}</em>' for a in BIB["abstracts"]]

doctor = head("의료진 소개 | 조재형 심장내과", "조재형 원장 — 시더스 사이나이 부정맥 박사, 심장내과 펠로우십, 전 클리블랜드 클리닉 임상조교수. 연구 논문 및 학술 활동.") + header("doctor.html") + f'''
  <main id="main">
{page_head("doc.title", "의료진 소개", "doc.lead", "정확한 진단과 신뢰할 수 있는 치료로 환자분의 심장 건강을 지켜드립니다.", "nav.about", "의료진 소개")}
    <section class="section about">
      <div class="container about__grid">
        <div class="about__media reveal">
          <div class="about__frame">
            <img src="assets/dr-cho.webp" alt="조재형 원장 Dr. Jae Hyung Cho" width="1500" height="1484" />
          </div>
          <div class="about__sign">
            <span class="about__sign-ko" data-i18n="sign">조재형</span>
            <span class="about__sign-en">Jae Hyung Cho, MD, PhD</span>
          </div>
        </div>
        <div class="about__body reveal">
          <p class="section__kicker">Physician</p>
          <h2 class="section__title" data-i18n="about.title">의학박사 조재형 원장</h2>
          <p class="about__role" data-en="Board-certified cardiologist with a PhD in arrhythmia research">내과 · 심장내과 전문의, 부정맥 연구 박사</p>
          <div class="about__text">
            <p data-en="Dr. Jae Hyung Cho provides comprehensive cardiovascular care to adults with a wide range of heart conditions, including hypertension, hyperlipidemia, angina, myocardial infarction, heart failure and cardiac arrhythmias.">조재형 원장은 고혈압, 고지혈증, 협심증, 심근경색, 심부전, 부정맥 등 다양한 심장 질환을 가진 성인 환자에게 종합적인 심장내과 진료를 제공합니다.</p>
            <p data-en="Dr. Cho completed his internal medicine residency at the University of Illinois at Urbana-Champaign in 2013 and his cardiology fellowship at Cedars-Sinai Medical Center in 2021, where he also earned a PhD in cardiac arrhythmia research. He has served as a Clinical Assistant Professor at the Cleveland Clinic and is currently a member of the medical staff at Cedars-Sinai Medical Center.">2013년 일리노이 주립대학교 어바나-샴페인에서 내과 레지던트를 마쳤고, 2021년 시더스 사이나이 메디컬 센터에서 심장내과 펠로우십을 수료했으며, 같은 기관에서 부정맥 연구로 박사학위를 받았습니다. 클리블랜드 클리닉에서 임상조교수를 역임했으며 현재 시더스 사이나이 메디컬 센터의 메디컬 스태프로 활동하고 있습니다.</p>
          </div>

          <div class="focus">
            <h3 class="about__sub" data-en="Clinical Focus">주요 진료 분야</h3>
            <ul class="chips">{"".join(f'<li data-en="{html.escape(e)}">{html.escape(k)}</li>' for k, e in FOCUS)}</ul>
          </div>

          <div class="about__cols">
            <div>
              <h3 class="about__sub" data-en="Board Certification">전문의 자격</h3>
              {li_list(BOARD)}
            </div>
            <div>
              <h3 class="about__sub" data-i18n="about.timeTitle">수련 및 경력</h3>
              <ol class="timeline">
                <li><span class="timeline__year timeline__year--now" data-i18n="tl4.y">현재</span><div><strong data-en="Medical Director">대표원장</strong><span data-en="Jae Hyung Cho, MD Cardiology">조재형 심장내과</span></div></li>
                <li><span class="timeline__year" data-i18n="tl4.y">현재</span><div><strong data-i18n="tl4.t">메디컬 스태프</strong><span>Cedars-Sinai Medical Center</span></div></li>
                <li><span class="timeline__year" data-i18n="tl3.y">역임</span><div><strong data-i18n="tl3.t">임상조교수</strong><span>Cleveland Clinic</span></div></li>
                <li><span class="timeline__year">2021</span><div><strong data-i18n="tl2.t">심장내과 펠로우십</strong><span>Cedars-Sinai Medical Center</span></div></li>
                <li><span class="timeline__year">Ph.D.</span><div><strong data-en="PhD, Cardiac Arrhythmia Research">박사학위 (부정맥 연구)</strong><span>Cedars-Sinai Graduate School of Biomedical Sciences</span></div></li>
                <li><span class="timeline__year">2013</span><div><strong data-i18n="tl1.t">내과 레지던트</strong><span>University of Illinois at Urbana–Champaign</span></div></li>
              </ol>
            </div>
            <div>
              <h3 class="about__sub" data-en="Honors">수상</h3>
              {li_list(HONORS)}
            </div>
            <div>
              <h3 class="about__sub" data-en="Professional Memberships">학회 회원</h3>
              {li_list(MEMBERS)}
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--soft research">
      <div class="container">
        <div class="section__head reveal">
          <p class="section__kicker">Research</p>
          <h2 class="section__title" data-en="Research &amp; Academic Work">연구 및 학술 활동</h2>
          <p class="section__desc" data-en="Dr. Cho has published research on arrhythmias, heart failure and cardiac imaging in international journals including Nature and Circulation.">Nature, Circulation 등 국제 학술지에 부정맥 · 심부전 · 심장 영상 분야 연구를 발표해 왔습니다.</p>
        </div>
        <div class="rcards">
          <div class="rcard reveal">
            <div class="rcard__icon"><svg viewBox="0 0 24 24"><path d="M5 4h10l4 4v12H5z"/><path d="M15 4v4h4"/><path d="M8 12h8M8 16h6"/></svg></div>
            <h3 data-en="Publications">연구 논문 및 저서</h3>
            {li_list(PUBS, "dotlist")}
          </div>
          <div class="rcard reveal">
            <div class="rcard__icon"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/><path d="M7 11l3-3 2 2 4-4"/></svg></div>
            <h3 data-en="Presentations &amp; Invited Talks">학회 발표 및 초청 강연</h3>
            {li_list(TALKS, "dotlist")}
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container bib">
        <div class="section__head reveal">
          <p class="section__kicker">Bibliography</p>
          <h2 class="section__title" data-en="Full Bibliography">전체 논문 목록</h2>
        </div>
{acc("연구 논문", "Peer-Reviewed Research Papers", len(papers), papers, True)}
{acc("리뷰 논문", "Review Articles", len(reviews), reviews)}
{acc("의학 서적 챕터", "Book Chapter", len(book), book)}
{acc("학회 초록 및 발표", "Abstracts & Presentations", len(abstracts), abstracts)}
      </div>
    </section>
''' + cta() + FOOTER


# ---------------- services ----------------
services = head("진료 안내 | 조재형 심장내과", "고혈압, 고지혈증, 협심증, 심근경색, 심부전, 부정맥, 심장질환 예방 및 심장 초음파 등 심장 검사.") + header("services.html") + f'''
  <main id="main">
{page_head("svcp.title", "심장 건강, 조재형 심장내과에 맡기세요", "svc.desc", "환자 한 분 한 분의 상태에 맞춘 정확한 진단과 체계적인 치료 계획을 세워드립니다.", "nav.services", "진료 안내")}
    <section class="section">
      <div class="container">
        <div class="section__head reveal">
          <p class="section__kicker" data-i18n="svc.kicker">진료 분야</p>
          <h2 class="section__title" data-i18n="svc.title">심장 질환의 진단부터 관리까지, 한 곳에서</h2>
        </div>
        <div class="cards">
{cards_html()}
        </div>
      </div>
    </section>
{tests_html()}''' + cta(after_dark=True) + FOOTER

# ---------------- videos ----------------
filters = "\n".join(
    f'          <button type="button" data-filter="{c}" aria-pressed="{"true" if c == "all" else "false"}" data-en="{html.escape(e)}">{html.escape(k)}</button>'
    for c, k, e in CATS)
allv = "\n".join(video_card(v) for v in VIDEOS)
videos = head("영상칼럼 | 조재형 심장내과", "조재형 원장이 직접 설명하는 고혈압, 고지혈증, 협심증, 심근경색, 부정맥 등 심장 질환 영상칼럼.") + header("videos.html") + f'''
  <main id="main">
{page_head("vid.title", "영상칼럼", "vid.lead", "조재형 원장이 심장 질환에 대해 알기 쉽게 설명해 드립니다.", "nav.videos", "영상칼럼")}
    <section class="section">
      <div class="container">
        <div class="filters" role="group" aria-label="Category">
{filters}
        </div>
        <div class="videos" id="videoGrid">
{allv}
        </div>
        <div class="videos-cta reveal">
          <a href="https://www.youtube.com/@jhccardiology" target="_blank" rel="noopener" class="btn btn--primary btn--lg">
            <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.5v5l4.5-2.5z" fill="currentColor" stroke="none"/></svg>
            <span data-i18n="vid.channel">유튜브 채널 바로가기</span>
          </a>
        </div>
      </div>
    </section>
''' + cta() + FOOTER

# ---------------- contact ----------------
contact = head("오시는 길 | 조재형 심장내과", "2727 W Olympic Blvd Ste 208, Los Angeles, CA 90006 · 한남체인 건너편 · Tel (213) 908-6434", True) + header("contact.html") + f'''
  <main id="main">
{page_head("ct.title", "진료 예약 안내", "ct.desc", "진료 예약은 전화로 문의해 주세요.", "nav.contact", "오시는 길")}
    <section class="section">
      <div class="container contact__grid">
        <div class="contact__info">
{INFO_CARDS}
        </div>
        <div class="contact__map reveal">
          <iframe title="Map" src="https://maps.google.com/maps?q=2727%20W%20Olympic%20Blvd%20Ste%20208%2C%20Los%20Angeles%2C%20CA%2090006&z=16&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </section>
''' + FOOTER

for name, doc in [("index.html", index), ("doctor.html", doctor), ("services.html", services),
                  ("videos.html", videos), ("contact.html", contact)]:
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(doc)
print("ok")
