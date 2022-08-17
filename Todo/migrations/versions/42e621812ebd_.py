"""empty message

Revision ID: 42e621812ebd
Revises: 
Create Date: 2022-06-22 21:05:43.544930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42e621812ebd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Cliente',
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('rut', sa.Integer(), nullable=False),
    sa.Column('dv', sa.String(length=1), nullable=False),
    sa.Column('primer_nombre', sa.String(length=250), nullable=False),
    sa.Column('segundo_nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=250), nullable=False),
    sa.Column('apellido_materno', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.Column('fono', sa.Integer(), nullable=False),
    sa.Column('correo', sa.String(length=250), nullable=False),
    sa.Column('estado', sa.String(length=1), nullable=False),
    sa.Column('comuna_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_usuario')
    )
    op.create_table('Comuna',
    sa.Column('id_comuna', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('Region_id_region', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_comuna')
    )
    op.create_table('Descuento',
    sa.Column('id_descuento', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('porcentaje', sa.String(length=250), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_descuento')
    )
    op.create_table('Descuento_Producto',
    sa.Column('id_pro', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.Column('descuento_id', sa.Integer(), nullable=True),
    sa.Column('fecha_inicio', sa.Date(), nullable=True),
    sa.Column('fecha_termino', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id_pro')
    )
    op.create_table('Despacho',
    sa.Column('id_despacho', sa.Integer(), nullable=False),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.Column('fecha_entrega', sa.Date(), nullable=True),
    sa.Column('hora_entrega', sa.Date(), nullable=True),
    sa.Column('rut_recibe', sa.String(length=250), nullable=True),
    sa.Column('nombre_recibe', sa.String(length=250), nullable=True),
    sa.Column('esto_despacho', sa.Integer(), nullable=False),
    sa.Column('venta_id', sa.Integer(), nullable=True),
    sa.Column('comuna_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_despacho')
    )
    op.create_table('Detalle',
    sa.Column('id_detalle', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.Column('descuento', sa.Integer(), nullable=False),
    sa.Column('estado', sa.String(length=1), nullable=False),
    sa.Column('venta_id', sa.Integer(), nullable=True),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_detalle')
    )
    op.create_table('Donacion',
    sa.Column('id_donacion', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_donacion')
    )
    op.create_table('Producto',
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=250), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('valor_venta', sa.Integer(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=500), nullable=False),
    sa.Column('imagen', sa.String(length=250), nullable=True),
    sa.Column('estado', sa.String(length=1), nullable=False),
    sa.PrimaryKeyConstraint('id_producto')
    )
    op.create_table('Region',
    sa.Column('id_region', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id_region')
    )
    op.create_table('Suscripcion',
    sa.Column('id_suscripcion', sa.Integer(), nullable=False),
    sa.Column('fecha_inicio', sa.Date(), nullable=False),
    sa.Column('fecha_termino', sa.Date(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_suscripcion')
    )
    op.create_table('Vendedor',
    sa.Column('id_vendedor', sa.Integer(), nullable=False),
    sa.Column('rut', sa.Integer(), nullable=False),
    sa.Column('dv', sa.String(length=1), nullable=False),
    sa.Column('primer_nombre', sa.String(length=250), nullable=False),
    sa.Column('segundo_nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=250), nullable=False),
    sa.Column('apellido_materno', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=False),
    sa.Column('fono', sa.Integer(), nullable=False),
    sa.Column('correo', sa.String(length=250), nullable=False),
    sa.Column('estado', sa.String(length=1), nullable=False),
    sa.Column('comuna_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_vendedor')
    )
    op.create_table('Venta',
    sa.Column('id_venta', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('descuento', sa.Integer(), nullable=True),
    sa.Column('sub_total', sa.Integer(), nullable=False),
    sa.Column('iva', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.Column('estado', sa.String(length=1), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.Column('vendedor_id', sa.Integer(), nullable=True),
    sa.Column('despacho_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_venta')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Venta')
    op.drop_table('Vendedor')
    op.drop_table('Suscripcion')
    op.drop_table('Region')
    op.drop_table('Producto')
    op.drop_table('Donacion')
    op.drop_table('Detalle')
    op.drop_table('Despacho')
    op.drop_table('Descuento_Producto')
    op.drop_table('Descuento')
    op.drop_table('Comuna')
    op.drop_table('Cliente')
    # ### end Alembic commands ###
