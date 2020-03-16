{
    'name': "calendar_scheduling",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'calendar',
        # 'calendar_resource',
        'sale',
        # 'sale_product_pack',
    ],

    'data': [
        'views/views.xml',
    ],

    'description': """
        USAGE
        On Sale Order, add (1) From date (2) To date (3) Order Line with a product.
        Click button to Schedule Events (top right corner in the sheet).
    """
}
