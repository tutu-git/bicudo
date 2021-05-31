@auth.requires_membership('ADMIN')    
def servico():
    #fields = [db.escola.nome, db.escola.regional, db.escola.inep]
    #grid = SQLFORM.grid(db.escola, fields=fields, maxtextlength=200,showbuttontext=False)
    grid = SQLFORM.grid(db.tipo_servico, maxtextlength=200,showbuttontext=True)
    return dict(grid=grid)
