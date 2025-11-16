# Documentation - Déployer l'IA avec Docker pour analyse de risque

Ce dépôt contient un exemple minimal pour te lancer rapidement.

## Étapes détaillées

1. Construire et démarrer : `docker-compose up --build`

2. Vérifier l'API : `http://localhost:8000/docs`

3. Adapter le modèle : remplacer `api/risk_model.joblib` par ton modèle entraîné

4. Brancher les sources de données : modifier `worker/worker.py` pour consommer ton SI (SIEM, CMDB, vuln scanners)

5. Production : utiliser registry interne, déployer sur Kubernetes, sécuriser secrets (KMS, Vault), ajouter monitoring

