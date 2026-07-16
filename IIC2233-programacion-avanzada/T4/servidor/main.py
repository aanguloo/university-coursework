from server import (Servidor)



if __name__ == "__main__":
    
    servidor = Servidor()
    servidor.bind_listen()  
    servidor.accept_connections_thread()
