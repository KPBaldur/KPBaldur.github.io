# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 1. Crear modelos
# 2. importamos las librerias de flask

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc
from models import db, Producto, Descuento, Region, Comuna, Donacion, Suscripcion, Cliente, Vendedor, Despacho, Detalle, Venta, Descuento_Producto
from flask_cors import CORS, cross_origin

# 3. instanciamos la app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Conten-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# 5. Creamos la ruta por defecto para saber si mi app esta funcionado
# 6. ejecutamos el comando en la consola: python app.py o python3 app.py o py app.py y revisamos nuestro navegador
@app.route('/')
def index():
    return 'Hola Prueba'


# 7. Ruta para consultar todos los productos
@app.route('/productos', methods=['GET'])
def getProductos():
    user = Producto.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

# 12. Ruta para agregar producto
@app.route('/productos', methods=['POST'])
def addProducto():
    user = Producto()
    # asignar a variables lo que recibo mediante post

    user.codigo = request.json.get('codigo')
    user.nombre = request.json.get('nombre')
    user.valor_venta = request.json.get('valor_venta')
    user.stock = request.json.get('stock')
    user.descripcion = request.json.get('descripcion')
    user.imagen = request.json.get('imagen')
    user.estado = request.json.get('estado')

    Producto.save(user)

    return jsonify(user.serialize()),200

# 13. Creamos metodo para consultar un producto en especifico
@app.route('/productos/<id_producto>', methods=['GET'])
def getProducto(id_producto):
    user = Producto.query.get(id_producto)
    return jsonify(user.serialize()),200

# 14. Borrar producto
@app.route('/productos/<id_producto>', methods=['DELETE'])
def deleteProducto(id_producto):
    user = Producto.query.get(id_producto)
    Producto.delete(user)
    return jsonify(user.serialize()),200

# 15. Modificar producto
@app.route('/productos/<id_producto>', methods=['PUT'])
def updateProducto(id_producto):
    user = Producto.query.get(id_producto)

    user.codigo = request.json.get('codigo')
    user.nombre = request.json.get('nombre')
    user.valor_venta = request.json.get('valor_venta')
    user.stock = request.json.get('stock')
    user.descripcion = request.json.get('descripcion')
    user.imagen = request.json.get('imagen')
    user.estado = request.json.get('estado')

    Producto.save(user)

    return jsonify(user.serialize()),200



# 7. Ruta para consultar todos los Descuentos
@app.route('/descuentos', methods=['GET'])
def getDescuentos():
    desc = Descuento.query.all()
    desc = list(map(lambda x: x.serialize(), desc))
    return jsonify(desc),200

# 12. Ruta para agregar Descuento
@app.route('/descuentos', methods=['POST'])
def addDescuento():
    desc = Descuento()
    # asignar a variables lo que recibo mediante post
    desc.nombre = request.json.get('nombre')
    desc.fecha = request.json.get('fecha')
    desc.porcentaje = request.json.get('porcentaje')
    desc.estado = request.json.get('estado')
    
    Descuento.save(desc)

    return jsonify(desc.serialize()),200

# 13. Creamos metodo para consultar un Descuento en especifico
@app.route('/descuentos/<id_descuento>', methods=['GET'])
def getDescuento(id_descuento):
    desc = Descuento.query.get(id_descuento)
    return jsonify(desc.serialize()),200

# 14. Borrar Descuento
@app.route('/descuentos/<id_descuento>', methods=['DELETE'])
def deleteDescuento(id_descuento):
    desc = Descuento.query.get(id_descuento)
    Descuento.delete(desc)
    return jsonify(desc.serialize()),200

# 15. Modificar Descuento
@app.route('/descuentos/<id_descuento>', methods=['PUT'])
def updateDescuento(id_descuento):
    desc = Descuento.query.get(id_descuento)

    desc.nombre = request.json.get('nombre')
    desc.fecha = request.json.get('fecha')
    desc.porcentaje = request.json.get('porcentaje')
    desc.estado = request.json.get('estado')

    Descuento.save(desc)

    return jsonify(desc.serialize()),200


# 7. Ruta para consultar todos la regiones
@app.route('/regiones', methods=['GET'])
def getRegiones():
    reg = Region.query.all()
    reg = list(map(lambda x: x.serialize(), reg))
    return jsonify(reg),200

# 12. Ruta para agregar region
@app.route('/regiones', methods=['POST'])
def addRegion():
    reg = Region()
    # asignar a variables lo que recibo mediante post
    reg.nombre = request.json.get('nombre')
   

    Region.save(reg)

    return jsonify(reg.serialize()),200

# 13. Creamos metodo para consultar un region en especifico
@app.route('/regiones/<id_region>', methods=['GET'])
def getRegion(id_region):
    reg = Region.query.get(id_region)
    return jsonify(reg.serialize()),200

# 14. Borrar region
@app.route('/regiones/<id_region>', methods=['DELETE'])
def deleteRegion(id_region):
    reg = Region.query.get(id_region)
    Region.delete(reg)
    return jsonify(reg.serialize()),200

# 15. Modificar region
@app.route('/regiones/<id_region>', methods=['PUT'])
def updateRegion(id_region):
    reg = Region.query.get(id_region)

    reg.nombre = request.json.get('nombre')
    
    Region.save(reg)

    return jsonify(reg.serialize()),200

# 7. Ruta para consultar todos la Comunas
@app.route('/comunas', methods=['GET'])
def getComunas():
    comun = Comuna.query.all()
    comun = list(map(lambda x: x.serialize(), comun))
    return jsonify(comun),200

# 12. Ruta para agregar Comuna
@app.route('/comunas', methods=['POST'])
def addComuna():
    comun = Comuna()
    # asignar a variables lo que recibo mediante post
    comun.nombre = request.json.get('nombre')
    
    Comuna.save(comun)

    return jsonify(comun.serialize()),200

# 13. Creamos metodo para consultar un Comuna en especifico
@app.route('/comunas/<id_comuna>', methods=['GET'])
def getComuna(id_comuna):
    comun = Comuna.query.get(id_comuna)
    return jsonify(comun.serialize()),200

# 14. Borrar Comuna
@app.route('/comunas/<id_comuna>', methods=['DELETE'])
def deleteComuna(id_comuna):
    comun = Comuna.query.get(id_comuna)
    Comuna.delete(comun)
    return jsonify(comun.serialize()),200

# 15. Modificar Comuna
@app.route('/comunas/<id_comuna>', methods=['PUT'])
def updateComuna(id_comuna):
    comun = Comuna.query.get(id_comuna)

    comun.nombre = request.json.get('nombre')
    
    Comuna.save(comun)

    return jsonify(comun.serialize()),200


# 7. Ruta para consultar todos los Sucripciones
@app.route('/donaciones', methods=['GET'])
def getDonaciones():
    dona = Donacion.query.all()
    dona = list(map(lambda x: x.serialize(), dona))
    return jsonify(dona),200

# 12. Ruta para agregar suscripcion
@app.route('/donaciones', methods=['POST'])
def addDonacion():
    dona = Donacion()
    # asignar a variables lo que recibo mediante post

    dona.valor = request.json.get('valor')
    dona.fecha = request.json.get('fecha')
    dona.cliente_id = request.json.get('cliente_id')

    Donacion.save(dona)

    return jsonify(dona.serialize()),200

# 13. Creamos metodo para consultar una Donacion en especifico
@app.route('/donaciones/<id_donacion>', methods=['GET'])
def getDonacion(id_donacion):
    dona = Donacion.query.get(id_donacion)
    return jsonify(dona.serialize()),200

# 14. Borrar Donacion
@app.route('/donaciones/<id_donacion>', methods=['DELETE'])
def deleteDonacion(id_donacion):
    dona = Donacion.query.get(id_donacion)
    Donacion.delete(dona)
    return jsonify(dona.serialize()),200

# 15. Modificar Donacion
@app.route('/donaciones/<id_donacion>', methods=['PUT'])
def updateDonacion(id_donacion):
    dona = Donacion.query.get(id_donacion)

    dona.valor = request.json.get('valor')
    dona.fecha = request.json.get('fecha')
    dona.cliente_id = request.json.get('cliente_id')
   
    Donacion.save(dona)

    return jsonify(dona.serialize()),200


# 7. Ruta para consultar todos los Sucripciones
@app.route('/suscripciones', methods=['GET'])
def getSuscripciones():
    susc = Suscripcion.query.all()
    susc = list(map(lambda x: x.serialize(), susc))
    return jsonify(susc),200

# 12. Ruta para agregar suscripcion
@app.route('/suscripciones', methods=['POST'])
def addSuscripciones():
    susc = Suscripcion()
    # asignar a variables lo que recibo mediante post

    susc.valor = request.json.get('valor')
    susc.fecha = request.json.get('fecha')
    susc.cliente_id = request.json.get('cliente_id')

    Suscripcion.save(susc)

    return jsonify(susc.serialize()),200

# 13. Creamos metodo para consultar una Suscripcion en especifico
@app.route('/suscripciones/<id_suscripcion>', methods=['GET'])
def getSuscripcion(id_suscripcion):
    susc = Suscripcion.query.get(id_suscripcion)
    return jsonify(susc.serialize()),200

# 14. Borrar Suscripcion
@app.route('/suscripciones/<id_suscripcion>', methods=['DELETE'])
def deleteSuscripcion(id_suscripcion):
    susc = Suscripcion.query.get(id_suscripcion)
    Suscripcion.delete(susc)
    return jsonify(susc.serialize()),200

# 15. Modificar Suscripcion
@app.route('/suscripciones/<id_suscripcion>', methods=['PUT'])
def updateSuscripcion(id_suscripcion):
    susc = Suscripcion.query.get(id_suscripcion)

    susc.valor = request.json.get('valor')
    susc.fecha = request.json.get('fecha')
    susc.cliente_id = request.json.get('cliente_id')
   
    Suscripcion.save(susc)

    return jsonify(susc.serialize()),200


# 7. Ruta para consultar todos los clientes
@app.route('/clientes', methods=['GET'])
def getClientes():
    clie = Cliente.query.all()
    clie = list(map(lambda x: x.serialize(), clie))
    return jsonify(clie),200

# 12. Ruta para agregar clientes
@app.route('/clientes', methods=['POST'])
def addCliente():
    clie = Cliente()
    # asignar a variables lo que recibo mediante post

    clie.rut = request.json.get('rut')
    clie.dv = request.json.get('dv')
    clie.primer_nombre = request.json.get('primer_nombre')
    clie.segundo_nombre = request.json.get('segundo_nombre')
    clie.apellido_paterno = request.json.get('apellido_paterno')
    clie.apellido_materno = request.json.get('apellido_materno')
    clie.direccion = request.json.get('direccion')
    clie.fono = request.json.get('fono')
    clie.correo = request.json.get('correo')
    clie.estado = request.json.get('estado')
    clie.comuna_id  = request.json.get('comuna_id ')
    
    Cliente.save(clie)

    return jsonify(clie.serialize()),200

# 13. Creamos metodo para consultar una Cliente en especifico
@app.route('/clientes/<id_usuario>', methods=['GET'])
def getCliente(id_usuario):
    clie = Cliente.query.get(id_usuario)
    return jsonify(clie.serialize()),200

# 14. Borrar Cliente
@app.route('/clientes/<id_usuario>', methods=['DELETE'])
def deleteCliente(id_usuario):
    clie = Cliente.query.get(id_usuario)
    Cliente.delete(clie)
    return jsonify(clie.serialize()),200

# 15. Modificar Cliente
@app.route('/clientes/<id_usuario>', methods=['PUT'])
def updateCliente(id_usuario):
    clie = Cliente.query.get(id_usuario)

    clie.rut = request.json.get('rut')
    clie.dv = request.json.get('dv')
    clie.primer_nombre = request.json.get('primer_nombre')
    clie.segundo_nombre = request.json.get('segundo_nombre')
    clie.apellido_paterno = request.json.get('apellido_paterno')
    clie.apellido_materno = request.json.get('apellido_materno')
    clie.direccion = request.json.get('direccion')
    clie.fono = request.json.get('fono')
    clie.correo = request.json.get('correo')
    clie.estado = request.json.get('estado')
    clie.comuna_id  = request.json.get('comuna_id')
    
   
    Cliente.save(clie)

    return jsonify(clie.serialize()),200


# 7. Ruta para consultar todos los Vendedores
@app.route('/vendedores', methods=['GET'])
def getVendedores():
    vend = Vendedor.query.all()
    vend = list(map(lambda x: x.serialize(), vend))
    return jsonify(vend),200

# 12. Ruta para agregar vendedores
@app.route('/vendedores', methods=['POST'])
def addVendedores():
    vend = Vendedor()
    # asignar a variables lo que recibo mediante post

    vend.rut = request.json.get('rut')
    vend.dv = request.json.get('dv')
    vend.primer_nombre = request.json.get('primer_nombre')
    vend.segundo_nombre = request.json.get('segundo_nombre')
    vend.apellido_paterno = request.json.get('apellido_paterno')
    vend.apellido_materno = request.json.get('apellido_materno')
    vend.direccion = request.json.get('direccion')
    vend.fono = request.json.get('fono')
    vend.correo = request.json.get('correo')
    vend.estado = request.json.get('estado')
    vend.comuna_id  = request.json.get('comuna_id ')
    
    Vendedor.save(vend)

    return jsonify(vend.serialize()),200

# 13. Creamos metodo para consultar una Vendedor en especifico
@app.route('/vendedores/<id_vendedor>', methods=['GET'])
def getVendedor(id_vendedor):
    vend = Vendedor.query.get(id_vendedor)
    return jsonify(vend.serialize()),200

# 14. Borrar Vendedor
@app.route('/vendedores/<id_vendedor>', methods=['DELETE'])
def deleteVendedor(id_vendedor):
    vend = Vendedor.query.get(id_vendedor)
    Vendedor.delete(vend)
    return jsonify(vend.serialize()),200

# 15. Modificar Vendedor
@app.route('/vendedores/<id_vendedor>', methods=['PUT'])
def updateVendedor(id_vendedor):
    vend = Vendedor.query.get(id_vendedor)

    vend.rut = request.json.get('rut')
    vend.dv = request.json.get('dv')
    vend.primer_nombre = request.json.get('primer_nombre')
    vend.segundo_nombre = request.json.get('segundo_nombre')
    vend.apellido_paterno = request.json.get('apellido_paterno')
    vend.apellido_materno = request.json.get('apellido_materno')
    vend.direccion = request.json.get('direccion')
    vend.fono = request.json.get('fono')
    vend.correo = request.json.get('correo')
    vend.estado = request.json.get('estado')
    vend.comuna_id  = request.json.get('comuna_id ')
    
   
    Vendedor.save(vend)

    return jsonify(vend.serialize()),200


# 7. Ruta para consultar todos los Despachos
@app.route('/despachos', methods=['GET'])
def getDespachos():
    desp = Despacho.query.all()
    desp = list(map(lambda x: x.serialize(), desp))
    return jsonify(desp),200

# 12. Ruta para agregar Despacho
@app.route('/despachos', methods=['POST'])
def addDespachos():
    desp = Despacho()
    # asignar a variables lo que recibo mediante post

    desp.direccion = request.json.get('direccion')
    desp.fecha_entrega = request.json.get('fecha_entrega')
    desp.hora_entrega = request.json.get('hora_entrega')
    desp.rut_recibe = request.json.get('rut_recibe')
    desp.nombre_recibe = request.json.get('nombre_recibe')
    desp.esto_despacho = request.json.get('esto_despacho')
    desp.venta_id = request.json.get('venta_id')
    desp.comuna_id = request.json.get('comuna_id')
    
    Despacho.save(desp)

    return jsonify(desp.serialize()),200

# 13. Creamos metodo para consultar una Despacho en especifico
@app.route('/despachos/<id_despacho>', methods=['GET'])
def getDespacho(id_despacho):
    desp = Despacho.query.get(id_despacho)
    return jsonify(desp.serialize()),200

# 14. Borrar Despacho
@app.route('/despachos/<id_despacho>', methods=['DELETE'])
def deleteDespacho(id_despacho):
    desp = Despacho.query.get(id_despacho)
    Despacho.delete(desp)
    return jsonify(desp.serialize()),200

# 15. Modificar Despacho
@app.route('/despachos/<id_despacho>', methods=['PUT'])
def updateDespacho(id_despacho):
    desp = Despacho.query.get(id_despacho)

    desp.direccion = request.json.get('direccion')
    desp.fecha_entrega = request.json.get('fecha_entrega')
    desp.hora_entrega = request.json.get('hora_entrega')
    desp.rut_recibe = request.json.get('rut_recibe')
    desp.nombre_recibe = request.json.get('nombre_recibe')
    desp.esto_despacho = request.json.get('esto_despacho')
    desp.venta_id = request.json.get('venta_id')
    desp.comuna_id = request.json.get('comuna_id')
       
    Despacho.save(desp)

    return jsonify(desp.serialize()),200



# 7. Ruta para consultar todos los Detalles
@app.route('/detalles', methods=['GET'])
def getDetalles():
    det = Detalle.query.all()
    det = list(map(lambda x: x.serialize(), det))
    return jsonify(det),200

# 12. Ruta para agregar Detalle
@app.route('/detalles', methods=['POST'])
def addDetalles():
    det = Detalle()
    # asignar a variables lo que recibo mediante post

    det.cantidad = request.json.get('cantidad')
    det.valor = request.json.get('valor')
    det.descuento = request.json.get('descuento')
    det.estado = request.json.get('estado')
    det.venta_id = request.json.get('venta_id')
    det.producto_id = request.json.get('producto_id')
        
    Detalle.save(det)

    return jsonify(det.serialize()),200

# 13. Creamos metodo para consultar un Detalle en especifico
@app.route('/detalles/<id_detalle>', methods=['GET'])
def getDetalle(id_detalle):
    det = Detalle.query.get(id_detalle)
    return jsonify(det.serialize()),200

# 14. Borrar Detalle
@app.route('/detalles/<id_detalle>', methods=['DELETE'])
def deleteDetalle(id_detalle):
    det = Detalle.query.get(id_detalle)
    Detalle.delete(det)
    return jsonify(det.serialize()),200

# 15. Modificar Detalle
@app.route('/detalles/<id_detalle>', methods=['PUT'])
def updateDetalle(id_detalle):
    det = Detalle.query.get(id_detalle)

    det.cantidad = request.json.get('cantidad')
    det.valor = request.json.get('valor')
    det.descuento = request.json.get('descuento')
    det.estado = request.json.get('estado')
    det.venta_id = request.json.get('venta_id')
    det.producto_id = request.json.get('producto_id')
           
    Detalle.save(det)

    return jsonify(det.serialize()),200


# 7. Ruta para consultar todos los Ventas
@app.route('/ventas', methods=['GET'])
def getVentas():
    vta = Venta.query.all()
    vta = list(map(lambda x: x.serialize(), vta))
    return jsonify(vta),200

# 12. Ruta para agregar Venta
@app.route('/ventas', methods=['POST'])
def addVentas():
    vta = Venta()
    # asignar a variables lo que recibo mediante post

    vta.fecha = request.json.get('fecha')
    vta.descuento = request.json.get('descuento')
    vta.sub_total = request.json.get('sub_total')
    vta.iva = request.json.get('iva')
    vta.total = request.json.get('total')
    vta.estado = request.json.get('estado')
    vta.cliente_id = request.json.get('cliente_id')
    vta.vendedor_id = request.json.get('vendedor_id')
    vta.despacho_id = request.json.get('despacho_id')

    Venta.save(vta)

    return jsonify(vta.serialize()),200

# 13. Creamos metodo para consultar una Venta en especifico
@app.route('/ventas/<id_venta>', methods=['GET'])
def getVenta(id_venta):
    vta = Venta.query.get(id_venta)
    return jsonify(vta.serialize()),200

# 14. Borrar Venta
@app.route('/ventas/<id_venta>', methods=['DELETE'])
def deleteVenta(id_venta):
    vta = Venta.query.get(id_venta)
    Venta.delete(vta)
    return jsonify(vta.serialize()),200

# 15. Modificar Venta
@app.route('/ventas/<id_venta>', methods=['PUT'])
def updateVenta(id_venta):
    vta = Venta.query.get(id_venta)

    vta.fecha = request.json.get('fecha')
    vta.descuento = request.json.get('descuento')
    vta.sub_total = request.json.get('sub_total')
    vta.iva = request.json.get('iva')
    vta.total = request.json.get('total')
    vta.estado = request.json.get('estado')
    vta.cliente_id = request.json.get('cliente_id')
    vta.vendedor_id = request.json.get('vendedor_id')
    vta.despacho_id = request.json.get('despacho_id')

    Venta.save(vta)

    return jsonify(vta.serialize()),200


# 7. Ruta para consultar todos los Descuento_Producto
@app.route('/descuento_productos', methods=['GET'])
def getDescuento_Productos():
    dprod = Descuento_Producto.query.all()
    dprod = list(map(lambda x: x.serialize(), dprod))
    return jsonify(dprod),200

# 12. Ruta para agregar Descuento_Producto
@app.route('/descuento_productos', methods=['POST'])
def addDescuento_Productos():
    dprod = Descuento_Producto()
    # asignar a variables lo que recibo mediante post

    dprod.producto_id = request.json.get('producto_id')
    dprod.descuento_id = request.json.get('descuento_id')
    dprod.fecha_inicio = request.json.get('fecha_inicio')
    dprod.fecha_termino = request.json.get('fecha_termino')
               
    
    Descuento_Producto.save(dprod)

    return jsonify(dprod.serialize()),200

# 13. Creamos metodo para consultar un Descuento_Producto en especifico
@app.route('/descuento_productos/<id_pro>', methods=['GET'])
def getDescuento_Producto(id_pro):
    dprod = Descuento_Producto.query.get(id_pro)
    return jsonify(dprod.serialize()),200

# 14. Borrar Descuento_Producto
@app.route('/descuento_productos/<id_pro>', methods=['DELETE'])
def deleteDescuento_Producto(id_pro):
    dprod = Descuento_Producto.query.get(id_pro)
    Descuento_Producto.delete(dprod)
    return jsonify(dprod.serialize()),200

# 15. Modificar Descuento_Producto
@app.route('/descuento_productos/<id_pro>', methods=['PUT'])
def updateDescuento_Producto(id_pro):
    dprod = Descuento_Producto.query.get(id_pro)

    dprod.producto_id = request.json.get('producto_id')
    dprod.descuento_id = request.json.get('descuento_id')

    dprod.fecha_inicio = request.json.get('fecha_inicio')
    dprod.fecha_termino = request.json.get('fecha_termino')
        
    Descuento_Producto.save(dprod)

    return jsonify(dprod.serialize()),200


# 8. comando para iniciar mi app flask: flask db init
# 9. comando para migrar mis modelos:   flask db migrate
# 10. comando para crear nuestros modelos como tablas : flask db upgrade
# 11. comando para iniciar la app flask: flask run

# 4. Configurar los puertos nuestra app 
if __name__ == '__main__':
    app.run(port=5000, debug=True)