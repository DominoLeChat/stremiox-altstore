# StremioX AltStore Source

Auto-generated AltStore source pour StremioX sur iOS.

## URL de la source (pour Feather/eSign)

```
https://raw.githubusercontent.com/dominolechat/stremiox-altstore/apps.json
```

## Comment ça marche

Ce repo utilise GitHub Actions pour :
1. Vérifier chaque jour la dernière release de [StremioX](https://github.com/mamaclapper/StremioX)
2. Trouver l'IPA iOS dans les assets
3. Gén Automatically génrer `apps.json` au format AltStore
4. Committer et push le fichier

Le workflow se déclenche :
- Tous les jours à 00:00 UTC (schedule)
- Manuellement via "Run workflow" dans Actions
- À chaque nouvelle release de StremioX (optionnel)

## Ajouter dans Feather

1. Ouvrir Feather
2. Settings → Sources → `+`
3. Coller l'URL ci-dessus
4. StremioX apparaît dans la liste des apps

## Trigger manuel

Dans GitHub → Actions → "Update AltStore Source" → "Run workflow"
