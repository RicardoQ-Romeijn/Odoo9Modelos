# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class modelos9(models.Model):
#     _name = 'modelos9.modelos9'
#     _description = 'modelos9.modelos9'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class clientes(models.Model):
	_name = 'modelos9.clientes'
	_description = 'Modelo Clientes'

	idCliente = fields.Char(string='ID Cliente', required=True)
	dni = fields.Char(string='DNI', required=True)
	nombre = fields.Char(string='Nombre', required=True)
	direccion = fields.Char(string='Direccion', required=True)

	relidCliente = fields.One2many('modelos9.pedidos', 'idCliente', string='ID Cliente')

class proveedores(models.Model):
	_name = 'modelos9.proveedores'
	_description = 'Modelo Proveedor'

	idProveedor = fields.Char(string='ID Proveedor', required=True)
	nombre = fields.Char(string='Nombre', required=True)
	pais = fields.Char(string='Pais', required=True)
	telefono = fields.Char(string='Telefono', required=True)

	relidProveedor = fields.One2many('modelos9.productos', 'idProveedor', string='ID Proveedor')

class empleados(models.Model):
	_name = 'modelos9.empleados'
	_description = 'Modelo Empleados'

	idEmpleado = fields.Char(string='ID Empleado', required=True)
	dni = fields.Char(string='Dni', required=True)
	nombre = fields.Char(string='Nombre', required=True)
	direccion = fields.Char(string='Direccion', required=True)

	relidEmpleado = fields.One2many('modelos9.pedidos', 'idEmpleado', string='ID Empleados')

class categorias(models.Model):
	_name = 'modelos9.categorias'
	_description = 'Modelo Categorias'

	idCategoria = fields.Char(string='ID Categoria')
	nombre = fields.Char(string='Nombre', required=True)
	descripcion = fields.Char(string='Descripcion', required=True)

	relidCategoria = fields.One2many('modelos9.productos', 'idCategoria', string='ID Categorias')

# --------------------------------------------------------------------------------------------------

class productos(models.Model):
	_name = 'modelos9.productos'
	_description = 'Modelo Productos'

	idProducto = fields.Char(string='ID Producto', required=True)
	idProveedor = fields.Many2one('modelos9.proveedores', string='ID Proveedor', required=True)
	idCategoria = fields.Many2one('modelos9.categorias', string='ID Categorias', required=True)
	nombre = fields.Char(string='Nombre', required=True)
	preciounidad = fields.Char(string='Precio Por Producto', required=True)

	relidProducto = fields.One2many('modelos9.detpedidos', 'idProducto', string='ID Productos')

class pedidos(models.Model):
	_name = 'modelos9.pedidos'
	_description = 'Modelo Pedidos'

	idPedidos = fields.Char(string='ID Pedido', required=True)
	idCliente = fields.Many2one('modelos9.clientes', string='ID Clientes', required=True)
	idEmpleado = fields.Many2one('modelos9.empleados', string='ID Empleados', required=True)
	cargo = fields.Char(string='Cargo', required=True)
	date = fields.Date(string="Fecha Pedido", default=fields.Date.context_today)

	relidPedidos = fields.One2many('modelos9.detpedidos', 'idPedidos', string='ID Pedidos')

class detpedidos(models.Model):
	_name = 'modelos9.detpedidos'
	_description = 'Modelo Detalle Pedidos'

	idPedidos = fields.Many2one('modelos9.pedidos', string='ID Pedidos', required=True)
	idProducto = fields.Many2one('modelos9.productos', string='ID Productos', required=True)
	preciounidad = fields.Char(string='Precio Unidad', required=True)
	cantidad = fields.Char(string='Cantidad', required=True)

# --------------------------------------------------------------------------------------------------

class companiasenv(models.Model):
	_name = 'modelos9.companiasenv'
	_description = 'Modelo Compañias Envios'

	idCompanias = fields.Char(string='ID Compañias', required=True)
	nombre = fields.Char(string='Nombre', required=True)
	telefono = fields.Char(string='Telefono', required=True)

class transporte(models.Model):
	_name = 'modelos9.transporte'
	_description = 'Modelo Transporte'

	idTransporte = fields.Char(string='ID Transporte', required=True)
	nombre = fields.Char(string='Nombre', required=True)
	vehiculo = fields.Char(string='Vehiculo', required=True)
