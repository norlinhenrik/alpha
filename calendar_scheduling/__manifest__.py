{
    'name': "calendar_scheduling",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'calendar',
        # 'calendar_resource',
        'sale_management',
        # 'sale_product_pack',
    ],

    'data': [
        'views/views.xml',
    ],

    'description': """
        USAGE
        On Sale Order, add (1) Customer (2) From date (3) To date (4) Order Line with a product.
        Click button to Schedule Events (top right corner in the sheet).
    """
}
