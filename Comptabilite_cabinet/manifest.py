{
    'name': 'Comptabilité Cabinet',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Gère les entreprises, comptes et écritures pour un cabinet comptable',
    'description': 'Module simple pour gérer plusieurs entreprises et leurs écritures comptables en Algérie',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/exemple_data.xml',
        'views/comptabilite_views.xml',


    ],
    'installable': True,
    'application': True,
}