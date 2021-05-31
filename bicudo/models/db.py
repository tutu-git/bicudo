# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
GENERO = {
    1:"Masculino",
    2:"Feminino",
    3:"Prefiro não responder",
    4:"Outros"
}

ESTADO = {
    1:"Acre (AC)",
    2:"Alagoas (AL)",
    3:"Amapá (AP)",
    4:"Amazonas (AM)",
    5:"Bahia (BA)",
    6:"Ceará (CE)",
    7:"Distrito Federal (DF)",
    8:"Espírito Santo (ES)",
    9:"Goiás (GO)",
    10:"Maranhão (MA)",
    11:"Mato Grosso (MT)",
    12:"Mato Grosso do Sul (MS)",
    13:"Minas Gerais (MG)",
    14:"Pará (PA)",
    15:"Paraíba (PB)",
    16:"Paraná (PR)",
    17:"Pernambuco (PE)",
    18:"Piauí (PI)",
    19:"Rio de Janeiro (RJ)",
    20:"Rio Grande do Norte (RN)",
    21:"Rio Grande do Sul (RS)",
    22:"Rondônia (RO)",
    23:"Roraima (RR)",
    24:"Santa Catarina (SC)",
    25:"São Paulo (SP)",
    26:"Sergipe (SE)",
    27:"Tocantins (TO)"
}


auth.settings.extra_fields['auth_user'] = [
    Field('cpf',length=14,requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'auth_user.cpf')],comment="Formato: 000.000.000-00"),
    Field('data_nascimento','date',label='Data de Nascimento',requires = IS_DATE(format=('%d-%m-%Y'))),
    Field('genero','integer',requires=IS_IN_SET(GENERO),represent = lambda v,r: GENERO[v]),
    Field('telefone',length=14,comment="Formato (99)99999-9999"),
    Field('logradouro','string',requires=IS_NOT_EMPTY()),
    Field('numero',length=10,label='Número',requires=IS_NOT_EMPTY()), #string cobre tipos 99A, 99B e etc.
    Field('complemento','string'),
    Field('bairro','string',requires=IS_NOT_EMPTY()),
    Field('cidade','string',requires=IS_NOT_EMPTY()),
    Field('estado','integer',requires=IS_IN_SET(ESTADO),represent = lambda v,r: ESTADO[v]),
    Field('cep','string',requires=IS_NOT_EMPTY())
    ]

auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

auth.settings.everybody_group_id = 2

auth.settings.create_user_groups = False # define que não será criado um grupo para cada usuário criado
auth.settings.actions_disabled = ['verify_email','impersonate']
auth.messages.access_denied = 'Sem permissão de acesso'      
auth.messages.invalid_login = 'Login inválido'
auth.messages.logged_in = 'Usuário Logado'
auth.messages.logged_out = 'Usuário Deslogado'
auth.messages.password_changed = 'Senha alterada'
auth.messages.delete_label = 'Marque para deletar'

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

db.define_table('tipo_servico',
                Field('nome','string',requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'tipo_servico.nome')]),
                format='%(nome)s'
    )

db.define_table('servico',
                Field('prestador',db.auth_user,writable=False,default=session.auth.user.id if session.auth else None),
                #Field('prestador',db.auth_user,writable=False),
                #Field('tipo','list:reference tipo_servico',requires=IS_IN_DB(db, 'tipo_servico.id',db.tipo_servico._format, multiple=True)),
                Field('tipos','list:reference tipo_servico'),
                Field('descricao','text',requires=IS_NOT_EMPTY())
    )

# se tabela de usuários está vazia cria grupos e usuário administrador
if db(db.auth_user).isempty():
    admin = db.auth_user.insert(
            password = db.auth_user.password.validate('123456')[0],
            email = 'admin@x.com',
            first_name = 'Administrador',
            last_name = 'do Sistema',
            cpf = '999.999.999-99',
            data_nascimento = request.now,
            genero = 4,
            telefone = '(99)99999-9999',
            logradouro = 'R.',
            numero = '0',
            complemento = '-',
            bairro = 'B.',
            cidade = 'C',
            estado = 1,
            cep = '00000-00'
        )
    # cria o grupo administrador
    grupo_admin = auth.add_group(role = 'ADMIN')
    grupo_usuario = auth.add_group(role = 'USUARIO')
    # insere usuário administrador no grupo administrador
    auth.add_membership(grupo_admin, admin)
    auth.add_membership(grupo_usuario, admin)

ADMIN = auth.has_membership('ADMIN')
#USUARIO = auth.has_membership('USUARIO')

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
