import os
import gitlab
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def auth_gitlab():
    gl = None
    try:
        gl = gitlab.Gitlab(url=os.getenv('GITLAB_URL'), private_token=os.getenv('GITLAB_PERSONAL_TOKEN'))
        gl.auth()
        
    except gitlab.GitlabAuthenticationError as e:
        print(f"Error connecting to gitlab: {e}")
        return None
    
    return gl

def create_project():
    gl = auth_gitlab()
    if gl is not None:
        user = gl_obj.users.list(username='rodolfo.aravena')[0]
        user_project = user.projects.create({'name': 'project'})
        user_projects = user.projects.list()

def bulk_users_creation(data):
    gl = auth_gitlab()
    if gl is not None:
        for idx, row in data.iterrows():
            user = gl.users.create({
                        'email': row.CORREO,
                        'password': row.pswd,
                        'username': row.usuario,
                        'name': row.NOMBRE})
            user.activate()

def bulk_add_member_to_project():
    # TODO: Asignar proyecto
    pass
    



gl_obj = auth_gitlab()

# data = pd.read_csv('<your_csv_file_here>')

# bulk_users_creation(data, gl_obj)


