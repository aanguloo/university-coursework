from typing import Generator, Iterable 
from datetime import date   #para comparar fechas
import utilidades

def cargar_usuarios(path: str) -> Generator:
    with open(path, "r", encoding= "utf-8") as file:
        file.readline()
        for line in file:
            usuario = line.strip().split(";")
            yield utilidades.Usuarios(*usuario)


def cargar_productos(path: str) -> Generator:
    with open(path, "r", encoding= "utf-8") as file:
        file.readline()
        for line in file:
            productos = line.strip().split(";")
            productos[2] = float(productos[2])
            productos[3] = int(productos[3])
            yield utilidades.Productos(*productos)

def cargar_ordenes(path: str) -> Generator:
    with open(path, "r", encoding= "utf-8") as file:
        file.readline()
        for line in file:
            ordenes = line.strip().split(";")
            yield utilidades.Ordenes(*ordenes)


def cargar_ordenes_items(path: str) -> Generator:
    with open(path, "r", encoding= "utf-8") as file:
        file.readline()
        for line in file:
            ordenes_items = line.strip().split(";")
            ordenes_items[2] = int(ordenes_items[2])
            yield utilidades.OrdenesItems(*ordenes_items)


def cargar_proveedores(path: str) -> Generator:
    with open(path, "r", encoding= "utf-8") as file:
        file.readline()
        for line in file:
            proveedor = line.strip().split(";")
            yield utilidades.Proveedor(*proveedor)


def cargar_proveedores_productos(path: str) -> Generator:
    with open(path, "r", encoding= "utf-8") as file:
        file.readline()
        for line in file:
            proveedor_producto = line.strip().split(";")
            yield utilidades.ProveedoresProductos(*proveedor_producto)


# CONSULTAS


# CONSULTAS SIMPLES (1 GENERADOR)


def productos_desde_fecha(generador_productos: Generator,
                            fecha: str, inverso: bool) -> Generator:
    
    fecha_filtro = date.fromisoformat(fecha)
    
    if inverso == True:
        return filter(lambda producto: date.fromisoformat(producto.fecha_modificacion)\
            <= fecha_filtro, generador_productos)
    else:
        return filter(lambda producto: date.fromisoformat(producto.fecha_modificacion)\
            >= fecha_filtro, generador_productos)


def buscar_orden_por_contenido(generador_ordenes_items: Generator,
                id_producto: str, cantidad: int) -> Generator:
    
    generador_filter_id = filter(lambda orden_item: orden_item.id_base_datos_producto \
        == id_producto and orden_item.cantidad_productos == cantidad, generador_ordenes_items)
    return map(lambda orden_item: orden_item.id_base_datos_orden, generador_filter_id)

def proveedores_por_estado(generador_proveedores: Generator,
                        estado: str) -> Generator:
    generador_filter_estado = filter(lambda proveedor: proveedor.estado == estado, \
        generador_proveedores)
    return map(lambda proveedor: proveedor.nombre_proveedor, generador_filter_estado)


def ordenes_segun_estado_orden(generador_ordenes: Generator,
                            estado_orden: str) -> Generator:
    return filter(lambda orden: orden.estado_orden == estado_orden, \
        generador_ordenes)


def ordenes_entre_fechas(generador_ordenes: Generator,
                        fecha_inicial: str, fecha_final: str) -> Generator:
    
    if fecha_inicial == "-":
        return filter(lambda orden: date.fromisoformat(orden.fecha_creacion) \
            <= date.fromisoformat(fecha_final), generador_ordenes)
    elif fecha_final == "-":
        return filter(lambda orden: date.fromisoformat(orden.fecha_creacion) \
            >= date.fromisoformat(fecha_inicial), generador_ordenes)
    else:
        return filter(lambda orden: date.fromisoformat(orden.fecha_creacion) \
            >= date.fromisoformat(fecha_inicial) and \
            date.fromisoformat(orden.fecha_creacion) <= \
            date.fromisoformat(fecha_final)\
            , generador_ordenes)
            

#https://stackoverflow.com/questions/2166147/namedtuple-replace-doesnt-work-as-described-in-the-documentation
def modificar_estado_orden_ordenes_previas_fecha(generador_ordenes: Generator,
                                                fecha: str, cambio_estados: dict) -> Generator:
    
    generador_fechas_anteriores = filter(lambda orden: date.fromisoformat(orden.fecha_creacion) \
                                < date.fromisoformat(fecha), generador_ordenes)
    estados_actual = list(cambio_estados.keys())
    generador_estados_actuales = filter(lambda orden: orden.estado_orden in estados_actual, 
                                        generador_fechas_anteriores)
    return map(lambda orden: orden._replace(estado_orden=cambio_estados[orden.estado_orden]),
            generador_estados_actuales)


# CONSULTAS COMPLEJAS (2 o 3 GENERADORES)
def producto_mas_popular(generador_productos: Generator,
                        generador_ordenes: Generator, generador_ordenes_items: Generator,
                        fecha_inicial: str, fecha_final: str, ranking: int) -> Iterable:
    
    pass 


def ordenes_usuario(generador_productos: Generator,
                    generador_ordenes: Generator, generador_ordenes_items: Generator,
                    ids_usuario: list) -> dict:
    
    
    diccionario_ordenes_usuarios = {}
    diccionarios_productos_id_cantidad = {producto.id_base_datos: producto.cantidad_por_unidad
                                        for producto in generador_productos}
    lista_ordenes = list(generador_ordenes)
    lista_ordenes_items = list(generador_ordenes_items)
    
    for usuario in set(ids_usuario):
        generador_ordenes_filtradas_id_usuario = filter(lambda orden: orden.id_base_datos_usuario
                                                        == usuario, lista_ordenes)
        base_datos_ordenes = set(map(lambda orden: orden.id_base_datos, 
                                generador_ordenes_filtradas_id_usuario))
        generador_orden_items = filter(lambda orden: orden.id_base_datos_orden in 
                                    base_datos_ordenes, lista_ordenes_items)
        diccionario_producto_cantidad = {}
        
        for orden in generador_orden_items:
            
            if not orden.id_base_datos_producto in diccionario_producto_cantidad:
                diccionario_producto_cantidad[orden.id_base_datos_producto] = \
                    diccionarios_productos_id_cantidad[orden.id_base_datos_producto] * \
                        orden.cantidad_productos
            else:
                diccionario_producto_cantidad[orden.id_base_datos_producto] += \
                    diccionarios_productos_id_cantidad[orden.id_base_datos_producto] * \
                        orden.cantidad_productos
        diccionario_ordenes_usuarios[usuario] = diccionario_producto_cantidad
    return diccionario_ordenes_usuarios

def valor_orden(generador_productos: Generator,
                generador_ordenes_items: Generator, id_orden: str) -> float:
    
    generador_ordenes_id = filter(lambda orden: orden.id_base_datos_orden == id_orden,
                                        generador_ordenes_items)
    diccionario_productos = {producto.id_base_datos: producto.precio
                            for producto in generador_productos}
    costo = 0
    for orden in generador_ordenes_id:
        costo += diccionario_productos[orden.id_base_datos_producto] * orden.cantidad_productos
    return float(costo)

def proveedores_segun_precio_productos(generador_productos: Generator, generador_proveedores: 
    Generator, generador_proveedor_producto: Generator, precio: float) -> list:
    
    pass
def precio_promedio_segun_estado_orden(generador_ordenes: Generator,
                                    generador_ordenes_items: Generator,
                                    generador_productos: Generator, 
                                    estado_orden: str) -> float:
    
    generador_ordenes_filtradas = filter(lambda orden: orden.estado_orden == estado_orden, 
                                        generador_ordenes)
    
    set_ordenes_filtradas = set([orden.id_base_datos for orden in generador_ordenes_filtradas])
    generador_orden_productos_id = filter(lambda orden: orden.id_base_datos_orden in \
        set_ordenes_filtradas, generador_ordenes_items)
    
    diccionario_productos = {producto.id_base_datos: producto.precio
                            for producto in generador_productos}
    costo = 0
    for orden in generador_orden_productos_id:
        costo += diccionario_productos[orden.id_base_datos_producto] * orden.cantidad_productos
    
    try:
        valor_promedio = float(round(costo / len(set_ordenes_filtradas), 2))
        return valor_promedio
    except ZeroDivisionError:
        return 0.0

def cantidad_vendida_productos(generador_productos: Generator,
                            generador_ordenes_items: Generator, 
                            ids_productos: list) -> dict:
    
    base_datos_productos = set(ids_productos)
    cantidad_vendida = {id: 0 for id in ids_productos}
    productos_cantidad = {producto.id_base_datos: producto.cantidad_por_unidad
                        for producto in generador_productos}
    
    ordenes_filtradas = filter(lambda orden: orden.id_base_datos_producto in base_datos_productos,
                generador_ordenes_items)
    
    for orden in ordenes_filtradas:
        cantidad_vendida[orden.id_base_datos_producto] += \
        productos_cantidad[orden.id_base_datos_producto] * orden.cantidad_productos 
    
    return cantidad_vendida


def ordenes_dirigidas_al_estado(generador_ordenes: Generator,
                                generador_usuarios: Generator, estado: str) -> Generator:
    
    generador_filtrados_estados = filter(lambda usuario: usuario.direccion.split(" ")[-2] \
                                        == estado, generador_usuarios)
    base_datos_usuarios = set()
    for usuario in generador_filtrados_estados:
        base_datos_usuarios.add(usuario.id_base_datos)
    
    return filter(lambda orden: orden.id_base_datos_usuario in base_datos_usuarios,
                generador_ordenes)


def ganancias_dadas_por_clientes(generador_productos: Generator,
                                generador_ordenes: Generator, 
                                generador_ordenes_items: Generator,
                                ids_usuarios: list) -> dict:
    
    diccionario_ganancias = {id_usuario: 0 for id_usuario in ids_usuarios}
    diccionario_productos_id_precio = {producto.id_base_datos: producto.precio
                                    for producto in generador_productos}
    lista_ordenes = list(generador_ordenes)
    lista_ordenes_items = list(generador_ordenes_items)
    for id_usuario in ids_usuarios:
        
        ordenes_filtradas = filter(lambda orden: orden.id_base_datos_usuario == id_usuario,
                                lista_ordenes)
        id_ordenes = set([orden.id_base_datos for orden in ordenes_filtradas])
        ordenes_items_filtrados = filter(lambda orden: orden.id_base_datos_orden in id_ordenes,
                                lista_ordenes_items)
        
        for orden in ordenes_items_filtrados:
            precio_producto = diccionario_productos_id_precio[orden.id_base_datos_producto]
            cantidad_productos = orden.cantidad_productos
            diccionario_ganancias[id_usuario] += precio_producto * cantidad_productos
    return diccionario_ganancias
def modificar_estados_ordenes_dirigidas_al_estado(generador_ordenes: Generator,
                                                generador_usuarios: Generator, estado: str,
                                                cambio_estados_ordenes: dict) -> Generator:
    
    generador_ordenes_en_estado = ordenes_dirigidas_al_estado(generador_ordenes, 
                                                            generador_usuarios,
                                                            estado)
    estados_actual = list(cambio_estados_ordenes.keys())
    generador_estados_actuales = filter(lambda orden: orden.estado_orden in estados_actual, 
                                        generador_ordenes_en_estado)
    return map(lambda orden: orden._replace(estado_orden= \
        cambio_estados_ordenes[orden.estado_orden]), generador_estados_actuales)



def agrupar_items_por_maximo_pedido(generador_productos: Generator,
                                    generador_ordenes_items: Generator) -> Generator:
    
    diccionario_orden_producto = {}
    
    for orden_item in generador_ordenes_items:
        if not orden_item.id_base_datos_producto in diccionario_orden_producto:
            diccionario_orden_producto[orden_item.id_base_datos_producto] = [orden_item]
            
        else:
            diccionario_orden_producto[orden_item.id_base_datos_producto].append(orden_item)
            
    lista_productos = []
    for producto in generador_productos:
        try:
            lista_ordenes = diccionario_orden_producto[producto.id_base_datos]
            max_cantidad_ordenada = max(lista_ordenes,  
                                key = lambda orden: 
                                orden.cantidad_productos).cantidad_productos
            if max_cantidad_ordenada == 1:
                lista_productos.append(producto)
        
            elif max_cantidad_ordenada > 1:
                nueva_unidad_de_medida = utilidades.cambio_unidad_medida(producto.unidad_de_medida)
                nueva_cantidad_unidad = max_cantidad_ordenada * producto.cantidad_por_unidad 
                nuevo_precio = producto.precio * max_cantidad_ordenada
                nueva_fecha_modificacion = utilidades.fecha_actual()
                producto = producto._replace(precio = nuevo_precio, 
                            cantidad_por_unidad = nueva_cantidad_unidad,
                            unidad_de_medida = nueva_unidad_de_medida, 
                            fecha_modificacion = nueva_fecha_modificacion)
                lista_productos.append(producto)
        except KeyError:
            continue
    return (producto for producto in lista_productos)





