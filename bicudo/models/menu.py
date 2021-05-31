# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

#response.menu = [
#    (T('Home'), False, URL('default', 'index'), [])
#]

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

if auth.is_logged_in():
    if auth.has_membership('USUARIO'):
         response.menu += [
            ('MENU', False, '',[
                (T('Oferecer Serviços'), False, URL(request.application,'usuario','oferecer_servico'),[]),
            ]),
            ]
    if auth.has_membership('ADMIN'):
        _app = request.application
        response.menu += [
            ('Administrar', False, '',[
                (T('Tipos de Serviços'), False, URL(request.application,'admin','servico'),[]),
            ]),
            (T('This App'), False, '#', [
                (T('Design'), False, URL('admin', 'default', 'design/%s' % _app)),
                (T('Controller'), False,
                URL(
                    'admin', 'default', 'edit/%s/controllers/%s.py' % (_app, request.controller))),
                (T('View'), False,
                URL(
                    'admin', 'default', 'edit/%s/views/%s' % (_app, response.view))),
                (T('DB Model'), False,
                URL(
                    'admin', 'default', 'edit/%s/models/db.py' % _app)),
                (T('Menu Model'), False,
                URL(
                    'admin', 'default', 'edit/%s/models/menu.py' % _app)),
                (T('Config.ini'), False,
                URL(
                    'admin', 'default', 'edit/%s/private/appconfig.ini' % _app)),
                (T('Layout'), False,
                URL(
                    'admin', 'default', 'edit/%s/views/layout.html' % _app)),
                (T('Stylesheet'), False,
                URL(
                    'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % _app)),
                (T('Database'), False, URL(_app, 'appadmin', 'index')),
                (T('Errors'), False, URL(
                    'admin', 'default', 'errors/' + _app)),
                (T('About'), False, URL(
                    'admin', 'default', 'about/' + _app)),
            ]),
            (T('Documentation'), False, '#', [
                (T('Online book'), False, 'http://www.web2py.com/book'),
                (T('Preface'), False,
                'http://www.web2py.com/book/default/chapter/00'),
                (T('Introduction'), False,
                'http://www.web2py.com/book/default/chapter/01'),
                (T('Python'), False,
                'http://www.web2py.com/book/default/chapter/02'),
                (T('Overview'), False,
                'http://www.web2py.com/book/default/chapter/03'),
                (T('The Core'), False,
                'http://www.web2py.com/book/default/chapter/04'),
                (T('The Views'), False,
                'http://www.web2py.com/book/default/chapter/05'),
                (T('Database'), False,
                'http://www.web2py.com/book/default/chapter/06'),
                (T('Forms and Validators'), False,
                'http://www.web2py.com/book/default/chapter/07'),
                (T('Email and SMS'), False,
                'http://www.web2py.com/book/default/chapter/08'),
                (T('Access Control'), False,
                'http://www.web2py.com/book/default/chapter/09'),
                (T('Services'), False,
                'http://www.web2py.com/book/default/chapter/10'),
                (T('Ajax Recipes'), False,
                'http://www.web2py.com/book/default/chapter/11'),
                (T('Components and Plugins'), False,
                'http://www.web2py.com/book/default/chapter/12'),
                (T('Deployment Recipes'), False,
                'http://www.web2py.com/book/default/chapter/13'),
                (T('Other Recipes'), False,
                'http://www.web2py.com/book/default/chapter/14'),
                (T('Helping web2py'), False,
                'http://www.web2py.com/book/default/chapter/15'),
                (T("Buy web2py's book"), False,
                'http://stores.lulu.com/web2py'),
            ]),
                         ] 
