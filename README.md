# Rodinka landing page

Statická landing page bez build procesu a závislostí.

## Lokální spuštění

```bash
python3 -m http.server 4173
```

Poté otevřete `http://localhost:4173`.

## Vercel

Repozitář stačí připojit k Vercelu jako projekt s framework presetem **Other**. Build command ani output directory nejsou potřeba.

Závěrečné CTA vede přímo do aplikace na `https://moje-rodinka.vercel.app/`.
