const menuButton = document.querySelector('.menu-button');
const nav = document.querySelector('.nav');
const themeSwitcher = document.querySelector('[data-theme-switch]');

if (themeSwitcher) {
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  let manualTheme = null;
  try {
    const savedTheme = window.localStorage.getItem('rodinka_theme');
    if (savedTheme === 'light' || savedTheme === 'dark') manualTheme = savedTheme;
  } catch (error) {
    // The switch still works for this page when storage is unavailable.
  }

  const updateTheme = (theme) => {
    document.documentElement.dataset.theme = theme;
    themeSwitcher.setAttribute('aria-pressed', String(theme === 'dark'));
    themeSwitcher.setAttribute('aria-label', theme === 'dark'
      ? themeSwitcher.dataset.lightLabel
      : themeSwitcher.dataset.darkLabel);
    document.querySelector('meta[name="theme-color"]')?.setAttribute(
      'content', theme === 'dark' ? '#282b24' : '#fffdf8'
    );
  };

  updateTheme(document.documentElement.dataset.theme);
  themeSwitcher.addEventListener('click', () => {
    manualTheme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    updateTheme(manualTheme);
    try {
      window.localStorage.setItem('rodinka_theme', manualTheme);
    } catch (error) {
      // The current page still honors the choice.
    }
  });
  systemTheme.addEventListener('change', (event) => {
    if (manualTheme === null) updateTheme(event.matches ? 'dark' : 'light');
  });
}

if (menuButton && nav) {
  const closeMenu = () => {
    nav.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
  };

  menuButton.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(open));
  });

  nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav.classList.contains('open')) {
      closeMenu();
      menuButton.focus();
    }
  });
}

const revealElements = document.querySelectorAll('.reveal');

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  revealElements.forEach((element) => observer.observe(element));
} else {
  revealElements.forEach((element) => element.classList.add('visible'));
}

const consentPanel = document.querySelector('[data-cookie-consent]');
const cookieSettingsButtons = document.querySelectorAll('[data-cookie-settings]');
const consentConfig = window.rodinkaConsent || {
  key: 'rodinka_analytics_consent',
  version: 1,
  analytics: 'denied',
};
let consentReturnFocus = null;

const readStoredConsent = () => {
  try {
    const savedConsent = JSON.parse(window.localStorage.getItem(consentConfig.key));
    if (
      savedConsent
      && savedConsent.version === consentConfig.version
      && (savedConsent.analytics === 'granted' || savedConsent.analytics === 'denied')
    ) {
      return savedConsent.analytics;
    }
  } catch (error) {
    // Consent remains denied when storage is unavailable or invalid.
  }
  return null;
};

const showConsentPanel = (focusPanel = false) => {
  if (!consentPanel) return;
  consentPanel.hidden = false;
  if (focusPanel) {
    consentPanel.querySelector('[data-consent-choice]')?.focus();
  }
};

const hideConsentPanel = () => {
  if (!consentPanel) return;
  consentPanel.hidden = true;
  if (consentReturnFocus instanceof HTMLElement) {
    consentReturnFocus.focus();
  }
  consentReturnFocus = null;
};

const updateAnalyticsConsent = (analytics) => {
  consentConfig.analytics = analytics;
  try {
    if (!window.dataLayer || typeof window.dataLayer.push !== 'function') {
      window.dataLayer = [];
    }
    const consentCommand = typeof window.gtag === 'function'
      ? window.gtag
      : function consentCommandFallback() { window.dataLayer.push(arguments); };
    consentCommand('consent', 'update', {
      analytics_storage: analytics,
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied',
    });
  } catch (error) {
    // Persistence and UI behavior do not depend on Google scripts.
  }

  try {
    window.localStorage.setItem(consentConfig.key, JSON.stringify({
      version: consentConfig.version,
      analytics,
    }));
  } catch (error) {
    // The current page still honors the choice even when it cannot be persisted.
  }

  hideConsentPanel();
};

if (consentPanel) {
  if (readStoredConsent() === null) {
    showConsentPanel();
  }

  consentPanel.querySelectorAll('[data-consent-choice]').forEach((button) => {
    button.addEventListener('click', () => updateAnalyticsConsent(button.dataset.consentChoice));
  });
}

cookieSettingsButtons.forEach((button) => {
  button.addEventListener('click', () => {
    consentReturnFocus = button;
    showConsentPanel(true);
  });
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && consentPanel && !consentPanel.hidden) {
    hideConsentPanel();
  }
});

document.addEventListener('click', (event) => {
  const appLink = event.target instanceof Element
    ? event.target.closest('a[data-analytics-location]')
    : null;
  if (!appLink) return;

  // Do not queue or replay conversion events without analytics consent.
  if (consentConfig.analytics !== 'granted') return;
  try {
    const platform = appLink.dataset.storePlatform;
    const isStore = platform === 'ios' || platform === 'android';
    const destination = new URL(appLink.href, window.location.href);
    if (!isStore && destination.origin !== 'https://app.mojerodinka.cz') return;
    window.dataLayer = window.dataLayer || [];
    if (typeof window.dataLayer.push !== 'function') return;
    window.dataLayer.push({
      event: isStore ? 'store_cta_click' : 'web_app_cta_click',
      ...(isStore ? { platform } : {}),
      placement: appLink.dataset.analyticsLocation,
      locale: document.documentElement.lang.split('-')[0],
    });
  } catch (error) {
    // Navigation is never delayed or cancelled when analytics is unavailable.
  }
});

const spotVideo = document.querySelector('.spot-video');
const spotCover = document.querySelector('.spot-cover');

if (spotVideo && spotCover) {
  spotVideo.controls = false;

  spotCover.addEventListener('click', () => {
    spotVideo.poster = spotCover.querySelector('img').currentSrc;
    if (window.matchMedia('(max-width: 560px)').matches) {
      spotVideo.src = spotVideo.dataset.srcTall;
    }
    spotVideo.controls = true;
    spotCover.hidden = true;
    spotVideo.focus({ preventScroll: true });
    spotVideo.play().catch(() => {});
  });
}

const spotCta = document.querySelector('.spot-cta');

if (spotVideo && spotCta) {
  // The closing "try Rodinka" pill is part of the picture, so the link only
  // exists from the moment it appears. Sizes are pixels of the 1080 px cuts:
  // the pill is centred and 104 px tall, and the link overhangs it a little
  // to be an easier target.
  const pillHeight = 104;
  const slack = 14;
  const pillCentreY = { wide: 831.5 / 1080, tall: 1395 / 1920 };
  const showFrom = Number(spotCta.dataset.from);
  const pillWidth = Number(spotCta.dataset.width);

  const placeSpotCta = () => {
    const { videoWidth, videoHeight, clientWidth, clientHeight } = spotVideo;
    if (!videoWidth || !videoHeight) return;
    // Mirror object-fit: contain, so the link follows the drawn picture even
    // when the cut and the frame disagree, e.g. after rotating a phone.
    const scale = Math.min(clientWidth / videoWidth, clientHeight / videoHeight);
    const unit = (Math.min(videoWidth, videoHeight) * scale) / 1080;
    const centreY = (clientHeight - videoHeight * scale) / 2
      + videoHeight * scale * (videoWidth > videoHeight ? pillCentreY.wide : pillCentreY.tall);
    const width = (pillWidth + 2 * slack) * unit;
    const height = (pillHeight + 2 * slack) * unit;
    spotCta.style.left = `${(clientWidth - width) / 2}px`;
    spotCta.style.top = `${centreY - height / 2}px`;
    spotCta.style.width = `${width}px`;
    spotCta.style.height = `${height}px`;
  };

  spotVideo.addEventListener('timeupdate', () => {
    const show = spotVideo.currentTime >= showFrom;
    if (show) placeSpotCta();
    spotCta.hidden = !show;
  });
  window.addEventListener('resize', () => {
    if (!spotCta.hidden) placeSpotCta();
  });
}

// Každodenní Rodinka episodes. As with the spot, the poster is a button until
// the first play, so the video is only downloaded when someone asks for it.
const startShort = (short) => {
  const video = short.querySelector('.short-video');
  const cover = short.querySelector('.short-cover');
  if (!video || !cover) return;
  if (!cover.hidden) {
    const poster = cover.querySelector('img');
    video.poster = poster.currentSrc || poster.src;
    video.controls = true;
    cover.hidden = true;
  }
  video.play().catch(() => {});
};

document.querySelectorAll('.short').forEach((short) => {
  const video = short.querySelector('.short-video');
  const cover = short.querySelector('.short-cover');
  if (!video || !cover) return;
  video.controls = false;
  cover.addEventListener('click', () => {
    startShort(short);
    video.focus({ preventScroll: true });
  });
});

// The homepage lists the episodes beside one player: a pick puts its episode
// in the player's place and starts it.
const seriesPicks = document.querySelectorAll('.series-pick');

seriesPicks.forEach((pick) => {
  pick.addEventListener('click', () => {
    const chosen = document.getElementById(pick.getAttribute('aria-controls'));
    if (!chosen) return;
    seriesPicks.forEach((other) => {
      const short = document.getElementById(other.getAttribute('aria-controls'));
      const isChosen = short === chosen;
      other.setAttribute('aria-current', String(isChosen));
      if (!short) return;
      short.toggleAttribute('data-active', isChosen);
      if (!isChosen) short.querySelector('.short-video')?.pause();
    });
    startShort(chosen);
    chosen.scrollIntoView({ block: 'nearest' });
  });
});

// One video at a time: starting any of them pauses the rest, the spot included.
document.addEventListener('play', (event) => {
  document.querySelectorAll('video').forEach((video) => {
    if (video !== event.target) video.pause();
  });
}, true);

// The Nováks on the homepage: their notes fly into the Today screen, the
// day rail follows the reader, and their mark settles into the Rodinka logo.
(() => {
  const reduce = typeof window.matchMedia === 'function' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------------- hero */
  const stage = document.querySelector('.nd-stage');
  const toggle = document.querySelector('.nd-toggle');
  if (stage && toggle) {
    const notes = [...stage.querySelectorAll('.nd-note')];
    notes.forEach((note) => { note.dataset.r = note.style.getPropertyValue('--r'); });

    // Where each note has to land: measured with the phone already in place.
    const measure = () => {
      stage.classList.add('nd-measuring');
      const phone = stage.querySelector('.nd-phone');
      const prev = phone.style.transition;
      phone.style.transition = 'none';
      stage.dataset.state = 'calm';
      const targets = notes.map((note) => {
        const row = document.getElementById(note.dataset.target);
        return row ? row.getBoundingClientRect() : null;
      });
      stage.dataset.state = 'chaos';
      void phone.offsetWidth;
      phone.style.transition = prev;
      stage.classList.remove('nd-measuring');
      return targets;
    };

    const calm = () => {
      const targets = measure();
      notes.forEach((note, i) => {
        const t = targets[i];
        if (!t) return;
        const box = note.getBoundingClientRect();
        const dx = t.left + t.width * 0.62 - (box.left + box.width / 2);
        const dy = t.top + t.height / 2 - (box.top + box.height / 2);
        note.style.setProperty('--dx', `${dx}px`);
        note.style.setProperty('--dy', `${dy}px`);
        note.style.setProperty('--s', String(Math.max(0.12, (t.height * 1.3) / box.height)));
        note.style.setProperty('--r', '0deg');
        const row = document.getElementById(note.dataset.target);
        if (row) row.style.setProperty('--row-delay', `${i * 90}ms`);
      });
      stage.dataset.state = 'calm';
      toggle.setAttribute('aria-pressed', 'true');
    };

    const chaos = () => {
      notes.forEach((note) => {
        note.style.removeProperty('--dx');
        note.style.removeProperty('--dy');
        note.style.removeProperty('--s');
        note.style.setProperty('--r', note.dataset.r);
      });
      stage.dataset.state = 'chaos';
      toggle.setAttribute('aria-pressed', 'false');
    };

    toggle.hidden = false;
    let touched = false;
    toggle.addEventListener('click', () => {
      touched = true;
      if (stage.dataset.state === 'chaos') calm(); else chaos();
    });

    // First impression: let the chaos breathe for a moment, then tidy it up once.
    if (!reduce && 'IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        if (!entries.some((e) => e.isIntersecting)) return;
        io.disconnect();
        setTimeout(() => { if (!touched) calm(); }, 2200);
      }, { threshold: 0.6 });
      io.observe(stage);
    }
    window.addEventListener('resize', () => { if (stage.dataset.state === 'calm') calm(); });
  }

  /* ---------------------------------------------------------------- day rail */
  const rail = document.querySelector('.nd-rail');
  if (rail && 'IntersectionObserver' in window) {
    const links = [...rail.querySelectorAll('a[data-stop]')];
    const marker = rail.querySelector('.nd-rail-marker');
    const list = rail.querySelector('ol');
    const setActive = (id) => {
      links.forEach((a) => {
        const on = a.dataset.stop === id;
        if (on) {
          a.setAttribute('aria-current', 'step');
          const x = a.offsetLeft - list.scrollLeft + a.offsetWidth / 2 - marker.offsetWidth / 2 + list.offsetLeft;
          marker.style.setProperty('--mx', `${x}px`);
          if (list.scrollWidth > list.clientWidth) list.scrollTo({ left: a.offsetLeft - list.clientWidth / 2 + a.offsetWidth / 2, behavior: reduce ? 'auto' : 'smooth' });
        } else {
          a.removeAttribute('aria-current');
        }
      });
    };
    const io = new IntersectionObserver((entries) => {
      const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (visible[0]) setActive(visible[0].target.dataset.stop);
    }, { rootMargin: '-35% 0px -45% 0px', threshold: [0, 0.25, 0.5] });
    document.querySelectorAll('.nd-stop').forEach((s) => io.observe(s));
    setActive(links[0]?.dataset.stop);
  }

  /* ---------------------------------------------------------------- finale */
  const finale = document.querySelector('.nd-finale');
  if (finale && !('IntersectionObserver' in window)) finale.classList.add('is-gathered', 'is-logo');
  if (finale && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      if (!entries.some((e) => e.isIntersecting)) return;
      io.disconnect();
      finale.classList.add('is-gathered');
      setTimeout(() => finale.classList.add('is-logo'), reduce ? 0 : 2300);
    }, { threshold: 0.6 });
    io.observe(finale);
  }
})();
