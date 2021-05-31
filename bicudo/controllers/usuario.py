@auth.requires_membership('USUARIO')    
def oferecer_servico():
    query=db.servico.prestador==session.auth.user.id
    grid = SQLFORM.grid(query, maxtextlength=200,showbuttontext=False)
    return dict(grid=grid)
