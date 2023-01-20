"""empty message

Revision ID: 5b9d05118599
Revises: 
Create Date: 2023-01-19 21:51:13.287375

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5b9d05118599'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AgendaCliente',
    sa.Column('id_agenda', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('hora_inicio', sa.Time(), nullable=False),
    sa.Column('hora_termino', sa.Time(), nullable=False),
    sa.Column('ocupado', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id_agenda')
    )
    op.create_table('AgendaDelProfesional',
    sa.Column('id_agenda', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_profesional', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('hora_inicio', sa.Time(), nullable=False),
    sa.Column('hora_termino', sa.Time(), nullable=False),
    sa.Column('ocupado', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id_agenda')
    )
    op.create_table('Cliente',
    sa.Column('id_cliente', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rut', sa.String(length=12), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido_materno', sa.String(length=100), nullable=True),
    sa.Column('apellido_paterno', sa.String(length=100), nullable=False),
    sa.Column('codigo_telefono', sa.String(length=3), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('direccion', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id_cliente'),
    sa.UniqueConstraint('rut')
    )
    op.create_table('Especialidades',
    sa.Column('id_especialidad', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_servicio', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.Column('id_profesional', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_especialidad')
    )
    op.create_table('Profesional',
    sa.Column('id_profesional', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rut', sa.String(length=12), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido_materno', sa.String(length=100), nullable=False),
    sa.Column('apellido_paterno', sa.String(length=100), nullable=True),
    sa.Column('codigo_telefono', sa.String(length=3), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('direccion', sa.String(length=100), nullable=False),
    sa.Column('especialidad', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id_profesional'),
    sa.UniqueConstraint('rut')
    )
    op.create_table('Servicios',
    sa.Column('id_servicio', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('descripcion', sa.String(length=100), nullable=True),
    sa.Column('duracion', sa.Integer(), nullable=True),
    sa.Column('precio', sa.Integer(), nullable=True),
    sa.Column('imagen', sa.String(length=100), nullable=True),
    sa.Column('id_profesional', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_servicio')
    )
    with op.batch_alter_table('profesional', schema=None) as batch_op:
        batch_op.drop_index('rut')

    op.drop_table('profesional')
    op.drop_table('servicios')
    op.drop_table('especialidades')
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.drop_index('rut')

    op.drop_table('cliente')
    op.drop_table('agendacliente')
    op.drop_table('agendadelprofesional')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agendadelprofesional',
    sa.Column('id_agenda', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_profesional', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('fecha', sa.DATE(), nullable=False),
    sa.Column('hora_inicio', mysql.TIME(), nullable=False),
    sa.Column('hora_termino', mysql.TIME(), nullable=False),
    sa.Column('ocupado', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_agenda'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('agendacliente',
    sa.Column('id_agenda', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_cliente', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('fecha', sa.DATE(), nullable=False),
    sa.Column('hora_inicio', mysql.TIME(), nullable=False),
    sa.Column('hora_termino', mysql.TIME(), nullable=False),
    sa.Column('ocupado', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_agenda'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('cliente',
    sa.Column('id_cliente', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('rut', mysql.VARCHAR(length=12), nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('apellido_materno', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('apellido_paterno', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('codigo_telefono', mysql.VARCHAR(length=3), nullable=False),
    sa.Column('telefono', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('direccion', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id_cliente'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.create_index('rut', ['rut'], unique=False)

    op.create_table('especialidades',
    sa.Column('id_especialidad', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_servicio', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('descripcion', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('id_profesional', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_especialidad'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('servicios',
    sa.Column('id_servicio', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('descripcion', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('duracion', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('precio', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id_profesional', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_servicio'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('profesional',
    sa.Column('id_profesional', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('rut', mysql.VARCHAR(length=12), nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('apellido_materno', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('apellido_paterno', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('codigo_telefono', mysql.VARCHAR(length=3), nullable=False),
    sa.Column('telefono', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('direccion', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('especialidad', mysql.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id_profesional'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('profesional', schema=None) as batch_op:
        batch_op.create_index('rut', ['rut'], unique=False)

    op.drop_table('Servicios')
    op.drop_table('Profesional')
    op.drop_table('Especialidades')
    op.drop_table('Cliente')
    op.drop_table('AgendaDelProfesional')
    op.drop_table('AgendaCliente')
    # ### end Alembic commands ###