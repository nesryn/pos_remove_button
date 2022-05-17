# -*- coding: utf-8 -*-
{
    'name': "pos remove info button",

    'summary': """
        pos""",

    'description': """
        Long description of module's purpose
    """,

    'category': 'pos',
    'version': '0.1',
    'author': "Nesrine Essaies",
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        'web.assets_qweb': [
            'pos_remove_button/static/src/xml/Screens/ProductScreen/ProductItem.xml',
            'pos_remove_button/static/src/xml/Screens/ProductScreen/ControlButtons/ProductInfoButton.xml'
        ],
    },
}
