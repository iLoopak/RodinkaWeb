const menuButton = document.querySelector('.menu-button');
const nav = document.querySelector('.nav');

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

  try {
    const destination = new URL(appLink.href, window.location.href);
    if (destination.origin !== 'https://app.mojerodinka.cz') return;

    const textSource = appLink.cloneNode(true);
    textSource.querySelectorAll('[aria-hidden="true"]').forEach((element) => element.remove());
    window.dataLayer = window.dataLayer || [];
    if (typeof window.dataLayer.push !== 'function') return;
    window.dataLayer.push({
      event: 'cta_app_click',
      cta_location: appLink.dataset.analyticsLocation,
      cta_text: textSource.textContent.replace(/\s+/g, ' ').trim(),
      page_path: window.location.pathname,
      page_language: document.documentElement.lang.split('-')[0],
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

// The spot ends on a painted "try Rodinka" button. From the moment it appears,
// a link over the picture makes it (and the rest of the end card) clickable.
const spotCta = document.querySelector('.spot-cta');

if (spotVideo && spotCta) {
  const ctaAt = Number(spotVideo.dataset.ctaAt);
  const syncSpotCta = () => {
    spotCta.hidden = !(spotVideo.currentTime >= ctaAt);
  };

  ['timeupdate', 'seeking', 'ended', 'emptied'].forEach((type) => spotVideo.addEventListener(type, syncSpotCta));
}
