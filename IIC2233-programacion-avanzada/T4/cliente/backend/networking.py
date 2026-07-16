import socket
import json
from PyQt5.QtCore import QThread, pyqtSignal
from parametros import (TAMANO_CHUNK, CLAVE_CIFRADO, BYTES_LARGO,
                        PAQUETES_LARGO, ID_BYTES, PATH_CONEXION_BACKEND)
from random import shuffle

class Cliente(QThread):
    senal_empezar_juego = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        
        with open(PATH_CONEXION_BACKEND, "rb") as file:
            conexion = json.load(file)
            
        host = conexion["host"]  
        port = conexion["puerto"]   
        
        self.port = port
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.socket.connect((self.host, self.port))
            print(f"Se logro conectar correctamente al servidor. ip: {self.host}")
            self.manejar_flujo()
            

        except ConnectionError:
            print("[BACK] No se logró conectar")
            self.socket.close()
            exit()
    
    def manejar_flujo(self) -> None:
        
        while True:
            mensaje = input("ingresa el mensaje: ")
            self.enviar_mensaje(mensaje)
            print(f'se ha enviado el siguiente mensaje al servidor: {mensaje}')
            mensaje_servidor = self.recibir_mensaje()
            print(f"server: {mensaje_servidor}")
            
    def enviar_mensaje(self, mensaje: str) -> None:
        
        mensaje_b = bytearray(json.dumps(mensaje).encode("utf-8"))
        largo_original = len(mensaje_b)
        clave = bytearray(json.dumps(CLAVE_CIFRADO).encode("utf-8"))
        
        if largo_original % TAMANO_CHUNK != 0:
            extender = TAMANO_CHUNK - (largo_original % TAMANO_CHUNK)
            bytes_extender = b"\x00" * extender
            mensaje_b.extend(bytes_extender)
        
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
        self.socket.sendall(largo_final)
        self.socket.sendall(paquetes_desordenados)
        return largo_final + paquetes_desordenados
    
    def recibir_mensaje(self) -> str:
        
        sock = self.socket
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


