(function () {
  "use strict";

  document.documentElement.classList.remove("no-js");

  /* ---------- i18n ----------
     Korean is authored directly in the HTML (default language).
     English comes from this dictionary (data-i18n="key") or from an
     inline data-en="..." attribute on the element itself. */
  var EN = {
    "skip": "Skip to content",
    "top.addr": "2727 W Olympic Blvd Ste 208, Los Angeles · Across from Hannam Chain",
    "top.hours": "Mon–Fri 8:30 AM – 5:30 PM",

    "nav.home": "Home",
    "nav.about": "Our Physician",
    "nav.services": "Services",
    "nav.videos": "Video Column",
    "nav.contact": "Contact",

    "hero.title": "Our promise:<br />patient-centered<br /><em>cardiology care</em>",
    "hero.lead": "Jae Hyung Cho, MD Cardiology provides accurate diagnosis and evidence-based treatment. You are seen personally by a cardiologist trained at and practicing with Cedars-Sinai Medical Center.",
    "cta.book": "Book a Visit (213) 908-6434",
    "cta.doctor": "Meet Dr. Cho",
    "hero.b1": "Board-Certified Internist",
    "hero.b2": "Board-Certified Cardiologist",
    "hero.b3": "Echocardiography Certified (NBE)",

    "stat1": "Years of clinical experience",
    "stat2": "Cardiac arrhythmias, Cedars-Sinai",
    "stat3": "Former Clinical Assistant Professor",
    "stat4": "Current Medical Staff",

    "doc.title": "Our Physician",
    "doc.lead": "Accurate diagnosis and trusted treatment to protect your heart health.",
    "sign": "Dr. Cho",
    "about.title": "Jae Hyung Cho, MD, PhD",
    "about.timeTitle": "Training & Career",
    "tl1.t": "Internal Medicine Residency",
    "tl2.t": "Cardiology Fellowship",
    "tl3.y": "Prior",
    "tl3.t": "Clinical Assistant Professor",
    "tl4.y": "Now",
    "tl4.t": "Medical Staff",

    "svc.kicker": "Services",
    "svc.title": "From diagnosis to long-term care, all in one place",
    "svc.all": "View all services",
    "svc.desc": "Accurate diagnosis and a structured treatment plan tailored to every patient.",
    "svcp.title": "Entrust your heart to Dr. Cho",
    "c1.t": "Hypertension",
    "c1.d": "Careful blood pressure assessment, lifestyle guidance and medication to help prevent heart and stroke complications.",
    "c2.t": "Hyperlipidemia",
    "c2.d": "Comprehensive cholesterol and cardiovascular risk evaluation with personalized treatment goals.",
    "c3.t": "Angina Pectoris",
    "c3.d": "Identifying the cause of chest pain or pressure, with a focus on early detection of coronary artery disease.",
    "c4.t": "Myocardial Infarction",
    "c4.d": "Medication management and ongoing follow-up to support recovery and prevent recurrence after a heart attack.",
    "c5.t": "Congestive Heart Failure",
    "c5.d": "Managing shortness of breath, swelling and fatigue with guideline-directed therapy to help improve quality of life.",
    "c6.t": "Cardiac Arrhythmias",
    "c6.d": "With a PhD in arrhythmias, Dr. Cho specializes in atrial fibrillation, palpitations, fainting and other rhythm disorders.",
    "c7.t": "Cardiovascular Prevention",
    "c7.d": "Evaluating risk factors such as family history, diabetes and smoking to help prevent heart disease before it starts.",
    "c7.link": "Schedule a consultation →",

    "tests.kicker": "Cardiac Diagnostics",
    "tests.title": "Precise testing to support<br />an accurate diagnosis",
    "tests.desc": "Results are interpreted personally by a cardiologist certified in echocardiography (NBE), and advanced imaging such as coronary CT and cardiac MRI is arranged when needed.",
    "t1.t": "Echocardiogram",
    "t1.d": "Real-time ultrasound of the heart’s structure, valves and pumping function.",
    "t2.t": "Exercise Stress Test",
    "t2.d": "Monitors ECG and blood pressure during exercise to evaluate coronary artery disease.",
    "t3.t": "Vascular Ultrasound",
    "t3.d": "Checks the carotid and peripheral arteries for narrowing or abnormal blood flow.",
    "t4.t": "CT Coronary Angiogram",
    "t4.d": "Non-invasive, detailed imaging of coronary narrowing and calcification.",
    "t5.t": "Cardiac MRI",
    "t5.d": "High-resolution imaging to assess heart muscle condition and function.",

    "vid.kicker": "Video Column",
    "vid.homeTitle": "Heart health, explained by Dr. Cho",
    "vid.all": "View all videos",
    "vid.title": "Video Column",
    "vid.lead": "Dr. Cho explains heart conditions in clear, easy-to-follow videos (in Korean).",
    "vid.channel": "Visit our YouTube channel",

    "band.title": "Talk to a cardiologist today",
    "band.desc": "Chest pain, palpitations, shortness of breath or high blood pressure? Don’t wait to get checked.",

    "ct.kicker": "Contact",
    "ct.title": "Request an Appointment",
    "ct.desc": "Please call our office to schedule your visit.",
    "ct.map": "View map",
    "ct.addr": "Address",
    "ct.addrNote": "On Olympic Blvd, across from Hannam Chain",
    "ct.dir": "Get directions →",
    "ct.hours": "Hours",
    "ct.wk": "Monday – Friday",
    "ct.wkTime": "8:30 AM – 5:30 PM",
    "ct.phone": "Phone",
    "ct.tel": "Tel.",
    "ct.fax": "Fax.",

    "ft.name": "Jae Hyung Cho, MD Cardiology",
    "ft.emergency": "In case of a medical emergency, call 911 immediately."
  };

  var EN_TITLES = {
    "index.html": "Jae Hyung Cho, MD Cardiology | Cardiologist in Koreatown, Los Angeles",
    "doctor.html": "Our Physician | Jae Hyung Cho, MD Cardiology",
    "services.html": "Services | Jae Hyung Cho, MD Cardiology",
    "videos.html": "Video Column | Jae Hyung Cho, MD Cardiology",
    "contact.html": "Contact | Jae Hyung Cho, MD Cardiology"
  };
  var KO_TITLE = document.title;
  var page = document.body.getAttribute("data-page");

  var keyed = document.querySelectorAll("[data-i18n]");
  var inline = document.querySelectorAll("[data-en]");
  var KO = {};
  keyed.forEach(function (el) { KO[el.getAttribute("data-i18n")] = el.innerHTML; });
  inline.forEach(function (el) { el.setAttribute("data-ko", el.textContent); });

  function setLang(lang) {
    var en = lang === "en";
    keyed.forEach(function (el) {
      var k = el.getAttribute("data-i18n");
      el.innerHTML = en && EN[k] != null ? EN[k] : KO[k];
    });
    inline.forEach(function (el) {
      el.textContent = el.getAttribute(en ? "data-en" : "data-ko");
    });
    document.documentElement.lang = lang;
    document.title = en ? (EN_TITLES[page] || KO_TITLE) : KO_TITLE;
    document.querySelectorAll(".lang button").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang));
    });
    try { localStorage.setItem("lang", lang); } catch (e) {}
  }

  var initial = "ko";
  var q = new URLSearchParams(location.search).get("lang");
  if (q === "en" || q === "ko") initial = q;
  else { try { if (localStorage.getItem("lang") === "en") initial = "en"; } catch (e) {} }
  if (initial !== "ko") setLang(initial);

  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.dataset.lang); });
  });

  /* ---------- Header / mobile menu ---------- */
  var header = document.getElementById("header");
  var nav = document.getElementById("nav");
  var toggle = document.getElementById("menuToggle");

  function onScroll() { header.classList.toggle("is-scrolled", window.scrollY > 10); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  function closeMenu() {
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  }
  toggle.addEventListener("click", function () {
    var open = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(open));
  });

  /* ---------- Video modal ---------- */
  var modal = document.getElementById("videoModal");
  var frame = modal.querySelector(".modal__frame");
  var lastFocus = null;

  function openVideo(id) {
    lastFocus = document.activeElement;
    frame.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) +
      '?autoplay=1&rel=0" title="YouTube video" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>';
    modal.classList.add("is-open");
    document.body.style.overflow = "hidden";
    modal.querySelector(".modal__close").focus();
  }
  function closeVideo() {
    if (!modal.classList.contains("is-open")) return;
    modal.classList.remove("is-open");
    frame.innerHTML = "";
    document.body.style.overflow = "";
    if (lastFocus) lastFocus.focus();
  }
  document.querySelectorAll("[data-video]").forEach(function (b) {
    b.addEventListener("click", function () { openVideo(b.getAttribute("data-video")); });
  });
  modal.addEventListener("click", function (e) {
    if (e.target === modal || e.target.closest(".modal__close")) closeVideo();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { closeVideo(); closeMenu(); }
  });

  /* ---------- Video filters ---------- */
  var filterBtns = document.querySelectorAll("[data-filter]");
  filterBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var cat = btn.getAttribute("data-filter");
      filterBtns.forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      document.querySelectorAll("#videoGrid .video").forEach(function (v) {
        v.hidden = cat !== "all" && v.getAttribute("data-cat") !== cat;
        if (!v.hidden) v.classList.add("is-visible");
      });
    });
  });

  /* ---------- Reveal on scroll ---------- */
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -40px 0px" });
    items.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 70 + "ms";
      io.observe(el);
    });
  } else {
    items.forEach(function (el) { el.classList.add("is-visible"); });
  }

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
