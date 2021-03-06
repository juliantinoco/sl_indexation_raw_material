# -*- coding: utf-8 -*-
{
    'name': "sl_indexation_raw_material",

    'summary': """Automatic product indexation by specific category of raw material.""",

    'description': """
        Execute indexation when a purchase order is completed to update the costs of 
        all products in a specific category.

        Indexation determines the costs of the raw materials by weight, finds an average cost, 
        and adjusts the costs of the products in a category.

        Change view :
        - Add field in category
        TO COMPLETE
        In Development
    """,

    'author': "Mathieu Benoit",
    'company': "Mathben informatique",
    'website': "http://mathben.tech",
    'category': 'Warehouse',
    'version': '0.2',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'product', 'stock'],

    # always loaded
    'data': [
        # 'security/security.xml',
        'security/ir.model.access.csv',
        'views/indexation_raw_material_lines_views.xml',
        'views/indexation_raw_material_log_lines_views.xml',
        'views/product_views.xml',
        'views/purchase_views.xml',
        'views/stock_config_settings_views.xml',
        'wizard/compute_indexation_raw_material_views.xml',
        'wizard/clean_indexation_raw_material_views.xml',
        'views/stock_menu_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
