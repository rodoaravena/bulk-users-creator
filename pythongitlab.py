import gitlab
import pandas as pd

def create_project():
    user = gl_obj.users.list(username='rodolfo.aravena')[0]
    user_project = user.projects.create({'name': 'project'})
    user_projects = user.projects.list()
    
def auth_gitlab():
    gl = None
    try:
        gl = gitlab.Gitlab(url=uri, private_token=token)
        gl.auth()
        
    except gitlab.GitlabAuthenticationError as e:
        print(f"Error connecting to gitlab: {e}")
        return None
    
    return gl

def bulk_users_creation(data):
    gl = auth_gitlab()
    if gl is not None:
        for idx, row in data.iterrows():
            user = gl.users.create({
                        'email': row.CORREO,
                        'password': row.pswd,
                        'username': row.usuario,
                        'name': row.NOMBRE})

def bulk_users_creation(data):
    gl = auth_gitlab()
    if gl is not None:
        for idx, row in data.iterrows():
            user = gl.users.create({
                        'email': row.CORREO,
                        'password': row.pswd,
                        'username': row.usuario,
                        'name': row.NOMBRE})

def bulk_add_member_to_project():
    pass
    # member = project.members.create({'user_id': user.id, 'access_level':
    #                             gitlab.const.DEVELOPER_ACCESS})
        

gl_obj = auth_gitlab('<your_gilab_url_here>','<your_gilab_token_here>')

data = pd.read_csv('<your_csv_file_here>')

bulk_users_creation(data, gl_obj)

