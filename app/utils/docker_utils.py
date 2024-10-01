import docker
import paramiko

def get_remote_docker_client(hostname, username=None, key_filename=None):
    if hostname == "localhost":
        return docker.from_env()
    
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, username=username, key_filename=key_filename)
    
    docker_socket = ssh_client.get_transport().open_session()
    docker_socket.exec_command('docker system dial-stdio')
    
    return docker.APIClient(stream=docker_socket)