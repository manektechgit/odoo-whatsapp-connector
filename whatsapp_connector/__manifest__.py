{
    'name': 'Whatsapp Odoo Connector',
    'description': """Whatsapp Odoo Connector""",
    'version': '1.0',
    'summary': 'Whatsapp Odoo Connector',
    'sequence': 1,
    'license': 'OPL-1',
    'category': 'Connector',
    'depends': [
        'base', 'contacts', 'sale', 'crm', 'stock', 'sale_management', 'account', 'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'models/whatsapp_template.xml',
        'views/whatsapp_button_views.xml',
        'wizard/whatsapp_wizard.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
