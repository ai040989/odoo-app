{
    'name': 'Mon premier Module Odoo',
    'version': '1.0',
    'summary': 'module test',
    'description': """
    mon tout premier module odoo,xml,python,
    javascript
    """,
    'author': 'Ali Methnani',
    'website': 'https://www.mon-site-web.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/mon_module_views.xml',
    ],
    'images': [
        'static/src/image/icon.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
