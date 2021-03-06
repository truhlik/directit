from django.utils import timezone

from main.apps.categories.models import Category
from main.apps.categories.serializers import CategorySerializer

default_projects = {
    '1': {
        'categories': ["Podniková architektura"],
        'name': 'Architektura IT',
        'description': 'Kde jsme dnes a kde chceme být zítra',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '2': {
        'categories': ["IT Infrastruktura", "Cloud", "IaaS", "SaaS", "PaaS", "DaaS"],
        'name': 'Cloud vs. On-Premise',
        'description': 'Analýza alternativ pro vybraný systém',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '3': {
        'categories': ["Automatizace firemních procesů", "Automatizace procesů a workflow", "Robotics", "RPA",
                       "Artificial Intelligence"],
        'name': 'Možnosti Automatizace',
        'description': 'Zhodnocení které funkce pro automatizaci uvažovat',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '4': {
        'categories': ["Licenční Audit", "Finanční analýza ICT", ""],
        'name': 'Licenční Audit a Optimalizace',
        'description': 'Změny licenčních modelů, expirace, upgrade, crossgrade a další',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '5': {
        'categories': ["Správa a monitoring sítí", "Přístupové sítě – switching, routing, wifi",
                       "Networking DC / SDN, Loadbalancing", "Jednotné řízení přístupu do sítě",
                       "Analýza síťového provozu (NBA)"],
        'name': 'Analýza',
        'description': 'Síťová infrastruktury a konektivita',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '6': {
        'categories': ["Školení ICT", "Školení ITIL na míru", "Školení metodik podnikové architektury", ""],
        'name': 'Školení specifických kompetencí',
        'description': 'IT pracovníci či uživatelé ',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '7': {
        'categories': ["Finanční analýza ICT", ""],
        'name': 'Finanční IT Audit',
        'description': 'Vybraná oblast a záměr',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '8': {
        'categories': ["Strategie IT Security", "Přístupové sítě – switching, routing, wifi"],
        'name': 'IT Security',
        'description': 'Bezpečnost sítě',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '9': {
        'categories': ["Strategie IT Security", "Správa a monitoring koncových zařízení",
                       "Zálohování koncových zařízení", "Bezpečnost koncových zařízení", "Identity management (IDM)"],
        'name': 'IT Security',
        'description': 'Bezpečnost dat na koncových stanicích',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '10': {
        'categories': ["Strategie IT Security", "Řešení pro zálohování a archivaci",
                       "Vysoká dostupnost a disaster recovery DC"],
        'name': 'IT Security',
        'description': 'Backup a disaster recovery ',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '11': {
        'categories': ["Strategie IT Security", "GDPR", "Bezpečnostní dokumentace"],
        'name': 'IT Security',
        'description': 'Legislativa a nařízení',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '12': {
        'categories': ["Identity management (IDM)"],
        'name': 'Analýza',
        'description': 'Identity Management v organizaci',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '13': {
        'categories': ["Business Continuity Management", "Vysoká dostupnost a disaster recovery DC"],
        'name': 'Business Continuity Management',
        'description': 'Postupy a identifikace slabých míst',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '14': {
        'categories': ["Podniková architektura a procesní analýza", "Procesní analýza"],
        'name': 'Procesní analýza',
        'description': 'Interní SLA, Issue tracking system',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '15': {
        'categories': ["Intranetové portály", "Komunikace, Networking a Spolupráce"],
        'name': 'Intranet a Interní Komunikace',
        'description': 'Interní marketing a informovanost',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '16': {
        'categories': ["Podpora a zajištění provozu IT"],
        'name': 'Externí SLA analýza',
        'description': 'Zajištění dostupnosti externích služeb',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '17': {
        'categories': ["Databáze", "Řešení pro zálohování a archivaci"],
        'name': 'Databáze',
        'description': 'Výkon, uložení dat, konsolidace serverů, licenční politika, backup ',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
    '18': {
        'categories': [],
        'name': 'Katalogu Služeb IT v Organizaci',
        'description': 'ITIL',
        "step1": 10,
        "step2": 10,
        "step3": 10,
        "step4": 0,
        "step5": 0,
        "step6": 0,
    },
}

empty_data = {
    "categories": [],
    "name": "",
    "description": "",
    "step1": 10,
    "step2": 10,
    "step3": 10,
    "step4": 0,
    "step5": 0,
    "step6": 0,
}


def get_data(project_id: int) -> dict:
    project_data = default_projects.get(project_id, None).copy()
    if project_data is None:
        return empty_data

    cat_list = project_data['categories']
    qs = Category.objects.filter(name__in=cat_list)
    project_data['categories'] = CategorySerializer(qs, many=10).data
    project_data['due_date'] = timezone.now().date() + timezone.timedelta(days=90)
    return project_data
