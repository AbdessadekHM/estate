{
    'name': "estate",
    'depends':['base','mail'],
    'category': 'Real Estate/Brokerage',
    'data': [
        "security/security.xml",
        "security/ir.rule.xml",
        "security/ir.model.access.csv",
        "data/ir_actions_data.xml",
        "data/ir_cron_data.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_menus.xml",
        "views/res_users_views.xml"

    ],
    'demo': [
        'demo/estate_demo.xml',
    ],

}
