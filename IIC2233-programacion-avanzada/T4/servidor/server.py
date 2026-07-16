import socket
import sys
import json
import threading
from parametros import (TAMANO_CHUNK, CLAVE_CIFRADO, BYTES_LARGO,
                        PAQUETES_LARGO, ID_BYTES, PATH_CONEXION)
from random import shuffle

class Servidor:
    def __init__(self) -> None:
        
        with open(PATH_CONEXION, "rb") as file:
            conexion = json.load(file)
            
        host = conexion["host"]  
        port = conexion["puerto"]   
        
        self.contador_usuarios = 1
        self.usuarios = {}
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def bind_listen(self) -> None:

        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()
        print(f"Servidor escuchando en {self.host} : {self.port}")
        
    def accept_connections_thread(self) -> None:

        while True:
            id_usuario = self.contador_usuarios
            self.contador_usuarios += 1
            socket_usuario, address = self.socket_server.accept()
            self.usuarios[id_usuario] = (socket_usuario, address)
            print(f"Nuevo usuario conectado al juego: {socket_usuario} {address}")
            thread_usuario = threading.Thread(
                target=self.listen_client_thread,
                kwargs={'id_usuario': id_usuario},
                daemon=True)
            thread_usuario.start()
            
    def listen_client_thread(self, id_usuario: int) -> None:
        print("Un nuevo usuario ha ingresado al servidor.")
        
        print(f'[Cliente {id_usuario}] Nuevo cliente conectado')
        
        try:
            while True:
                mensaje_solicitud = self.recibir_mensaje(id_usuario)
                print(f'[Usuario {id_usuario}] Nuevo Mensaje: {mensaje_solicitud}')

                self.enviar_mensaje(id_usuario, "gracias por comunicarte con nosotros")
        
        except (ConnectionResetError, BrokenPipeError, socket.timeout) as error:
            print(f"Error usuario {id_usuario}: usuario desconectado| error "
                + f"{error}")
        
        finally:
            
            try:
                self.usuarios[id_usuario][0].close()
                print(f"Socket del usuario {id_usuario} cerrado existosamente")
            except OSError as e:
                print(f"Socket del usuario {id_usuario} ya fue cerrado")
            finally:
                if id_usuario in self.usuarios:
                    del self.usuarios[id_usuario]
                    print("usuario eliminado de la base de datos")
    
    def enviar_mensaje(self, id_usuario: int, mensaje: str) -> bytearray:
        sock = self.usuarios[id_usuario][0]
        mensaje_b = bytearray(json.dumps(mensaje).encode("utf-8"))
        largo_original = len(mensaje_b)
        
        if largo_original % TAMANO_CHUNK != 0:
            extender = TAMANO_CHUNK - (largo_original % TAMANO_CHUNK)
            bytes_extender = b"\x00" * extender
            mensaje_b.extend(bytes_extender)
        
        clave = bytearray(json.dumps(CLAVE_CIFRADO).encode("utf-8"))
        largo_extendido = len(mensaje_b)
        
        paquetes = bytearray()
        for i in range(0, largo_extendido, TAMANO_CHUNK):
            chunk = bytearray(mensaje_b[i:i + TAMANO_CHUNK])
            pos_chunk = int((i / TAMANO_CHUNK))
            pos_chunk = pos_chunk.to_bytes(4, byteorder='big')
            paquetes.extend(pos_chunk + chunk)
        
        
        largo_paquetes = len(paquetes)
        paquetes_xor = []
        for i in range(0, largo_paquetes, PAQUETES_LARGO):
            chunk = bytearray(paquetes[i:i + PAQUETES_LARGO])
            for byte in range(128):
                chunk[byte] = chunk[byte] ^ clave[byte]
            paquetes_xor.append(bytearray(chunk))
        
        shuffle(paquetes_xor)
        
        paquetes_desordenados = bytearray()
        for bytea in paquetes_xor:
            paquetes_desordenados.extend(bytea)
        
        largo_final = largo_original.to_bytes(4, byteorder='little')
        sock.sendall(largo_final)
        sock.sendall(paquetes_desordenados)
        return largo_final + paquetes_desordenados

    
    def recibir_mensaje(self, id_usuario: int) -> str:
        
        sock = self.usuarios[id_usuario][0]
        clave = bytearray(json.dumps(CLAVE_CIFRADO).encode("utf-8"))
        bytes_leidos = bytearray()
        while len(bytes_leidos) < BYTES_LARGO:
            restante = BYTES_LARGO - len(bytes_leidos)
            bytes_leer = min(BYTES_LARGO, restante)
            respuesta = sock.recv(bytes_leer)
            if len(respuesta) < bytes_leer:
                return "No hay un mensaje disponible"
            bytes_leidos.extend(respuesta)
            
        
        tamaño_original = int.from_bytes(bytes_leidos, byteorder='little')
        if tamaño_original % TAMANO_CHUNK != 0:
            extender = TAMANO_CHUNK - (tamaño_original % TAMANO_CHUNK)
        else:
            extender = 0
        
        tamaño_total = tamaño_original + extender
        cantidad_chuncks = int(tamaño_total / TAMANO_CHUNK)
        tamaño_incriptado = tamaño_total + cantidad_chuncks * ID_BYTES
            
        bytes_mensaje = bytearray()
        while len(bytes_mensaje) < tamaño_incriptado:
            restante = tamaño_incriptado - len(bytes_mensaje)
            bytes_leer = min(PAQUETES_LARGO, restante)
            respuesta = sock.recv(bytes_leer)
            bytes_mensaje.extend(respuesta)
            
        paquetes_sin_ordenar = bytearray()
    
        for i in range(0, len(bytes_mensaje), PAQUETES_LARGO):
            paquetes = bytearray(bytes_mensaje[i: i + PAQUETES_LARGO])
            for j in range(len(paquetes)):
                paquetes[j] = paquetes[j] ^ clave[j]
            paquetes_sin_ordenar.extend(paquetes)
    
    
        paquetes_ordenados_id = []
        for i in range(0, len(paquetes_sin_ordenar), PAQUETES_LARGO):
            id_paquete = int.from_bytes(paquetes_sin_ordenar[i: i + ID_BYTES], byteorder= 'big')
            chunck = paquetes_sin_ordenar[i + ID_BYTES: i + PAQUETES_LARGO]
            paquetes_ordenados_id.append((id_paquete, chunck))
    
        paquetes_ordenados_id.sort(key=lambda x: x[0])
        paquetes_ordenados = bytearray()
    
        for paquete in paquetes_ordenados_id:
            paquetes_ordenados.extend(paquete[1])
        return json.loads(paquetes_ordenados[:tamaño_original].decode("utf-8"))




