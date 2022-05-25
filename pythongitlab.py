import gitlab
import pandas as pd


def auth_gitlab(uri, token):
    gl = None
    try:
        gl = gitlab.Gitlab(url=uri, private_token=token)
        gl.auth()
        
    except gitlab.GitlabAuthenticationError as e:
        print(f"Error connecting to gitlab: {e}")
        gl = None
    
    return gl

def bulk_users_creation(data, gl=None):
    if gl is not None:
        for idx, row in data.iterrows():
            user = gl.users.create({
                        'email': row.CORREO,
                        'password': row.pswd,
                        'username': row.usuario,
                        'name': row.NOMBRE})
        

gl_obj = auth_gitlab('<your_gilab_url_here>','<your_gilab_token_here>')

data = pd.read_csv('<your_csv_file_here>')

bulk_users_creation(data, gl_obj)

