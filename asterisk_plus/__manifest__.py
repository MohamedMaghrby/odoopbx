# ©️ OdooPBX by Odooist, Odoo Proprietary License v1.0, 2020
# -*- encoding: utf-8 -*-
{
    'name': 'Asterisk Plus',
    'version': '1.0',
    'author': 'Odooist',
    'price': 350,
    'currency': 'EUR',
    'maintainer': 'Odooist',
    'support': 'odooist@gmail.com',
    'license': 'LGPL-3',
    'category': 'Phone',
    'summary': 'Asterisk plus Odoo',
    'description': 'Asterisk plus Odoo',
    'depends': ['base', 'mail'],
    'external_dependencies': {
       'python': ['humanize', 'lameenc', 'phonenumbers', 'salt-pepper', 'SpeechRecognition', 'pyyaml'],
    },
    'data': [
        # Security rules
        'security/groups.xml',
        'security/server.xml',
        'security/server_record_rules.xml',
        'security/admin.xml',
        'security/admin_record_rules.xml',
        'security/user.xml',
        'security/user_record_rules.xml',
        'security/debug.xml',
        # Data
        'data/events.xml',
        'data/res_users.xml',
        'data/server.xml',
        # UI Views
        'views/assets.xml',
        'views/menu.xml',
        'views/server.xml',
        'views/settings.xml',
        'views/about.xml',
        'views/event.xml',
        'views/recording.xml',
        'views/res_users.xml',
        'views/user.xml',
        'views/res_partner.xml',
        'views/call.xml',
        'views/channel.xml',
        'views/channel_message.xml',
        'views/templates.xml',
        'views/tag.xml',
        'views/conf.xml',
        'views/security.xml',
        # Cron
        'views/ir_cron.xml',
        # Wizards
        'wizard/set_notes.xml',
        'wizard/call.xml',
        # Reports
        'reports/reports.xml',
        'reports/calls_report.xml',
        # Web Phone
        'views/web_phone_user.xml',
        'views/web_phone_settings.xml',
    ],
    'demo': [],
    "qweb": ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/logo.png'],
    'js': ['static/src/lib/*.js',
           'static/src/js/*.js'],
    'qweb': [
        'static/src/xml/*.xml',
    ],
}
