# Instalace na lokalním prostředí

## Requirements
virtualenv

### Packages
python-3.5.5  # vycházíme z verze python pro Debian stable  

## Start project
I. stažení kódů a základní úpravy
```
git clone [projetct_name_git_url]
cd project_name
mkvirtualenv -p /usr/bin/python3.5 env
pip install -r requirements/local.pip
cp main/settings/local.py.sample main/settings/local.py
cp .env.sample .env
```    
II. Nastav si lokální settingy v souboru `main/settings/local.py` - volitelné.  
III. Nastav si proměnou prostředí DJANGO_SETTINGS_MODULE = main.setttings.localhost  
 - Pycharm - nastavení webserveru
 - Pycharm - preferences - Django
 - Pycharm - preferences - terminal     

III. Vytvoř si databázi v Postgresql, napr.:
```
sudo -u postgres psql
CREATE USER directit WITH PASSWORD 'directit';
CREATE DATABASE directit OWNER directit;
GRANT CONNECT ON DATABASE directit TO directit;
\c directit;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO directit;
```
IV. Uprav si proměnné v souboru `.env` 
    - určitě bude potřeba nastavit DB připojení k tvé lokální postgres db
    - pokud nepoužíváš smtp backend, tak nemusíš vyplňovat věci pro nastavení mailingu
    
V. Vytvoř si tabulky v DB `./manage.py migrate`

VI. Spusť projekt `./manage.py runserver`

## Seed data
```
python manage.py seed_categories
python manage.py seed_tags
python manage.py seed_consultants
python manage.py seed_suppliers
```
# Deploy
```
ansible-playbook deploy_production.yml -u administrator
ansible-playbook deploy_develop.yml -u administrator
```