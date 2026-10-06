import pymysql
import json
from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey,  DateTime, Text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class voluntario(Base):
    __tablename__ = 'voluntario'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    contrasena = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    telefono = Column(String(255), nullable=False)
    fecha_registro = Column(String(255), nullable=False)
    #comuna_id = Column(BigInteger, nullable=False)
    comuna_id = Column(BigInteger, ForeignKey("comuna.id"), nullable=False)

    #confesiones = relationship("Confesion", back_populates="usuario", cascade="all, delete")

class avistamiento(Base):
     __tablename__ = 'avistamiento'
    
     id = Column(BigInteger, primary_key=True, autoincrement=True)
     voluntario_id = Column(Integer, ForeignKey("voluntario.id"), nullable=False)
     ave_id = Column(Integer, ForeignKey("ave.id"), nullable=False)
     fecha_hora = Column(DateTime, nullable=False)
     lugar = Column(String(255), nullable=False)
     descripcion = Column(Text, nullable=False)

class ave(Base):
     __tablename__ = 'ave'
    
     id = Column(BigInteger, primary_key=True, autoincrement=True)
     nombre = Column(String(255), nullable=False)
     

class comuna(Base):
     __tablename__ = 'comuna'
    
     id = Column(BigInteger, primary_key=True, autoincrement=True)
     nombre = Column(String(255), nullable=False)
     region_id = Column(String(255), nullable = False)

class region(Base):
     __tablename__ = 'region'
    
     id = Column(BigInteger, primary_key=True, autoincrement=True)
     nombre = Column(String(255), nullable=False)

class registro(Base):
    __tablename__ = 'registro'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(255), nullable=False)
    nombre_archivo = Column(String(255), nullable=False)
    avistamiento_id = Column(Integer, ForeignKey("avistamiento.id"), nullable=False)

# funciones db
def get_user_by_id(id):
    session = SessionLocal()
    user = session.query(voluntario).filter_by(id=id).first()
    session.close()
    return user

def get_user_by_email(email):
    session = SessionLocal()
    user = session.query(voluntario).filter_by(email=email).first()
    session.close()
    return user

def get_user_by_username(username):
    session = SessionLocal()
    user = session.query(voluntario).filter_by(nombre=username).first()
    session.close()
    return user

def get_ave(nombre):
    session = SessionLocal()
    bird = session.query(ave).filter_by(nombre = nombre).first()
    session.close()
    return bird



def create_voluntario(username, password, email, fono, comunaa):
    session = SessionLocal()
    comuna_encontrada = session.query(comuna).filter_by(nombre=comunaa.strip()).first()
    new_user = voluntario(nombre=username, contrasena=password, email=email, telefono = fono, fecha_registro = datetime.now(), comuna_id = comuna_encontrada.id)
    session.add(new_user)
    session.commit()
    session.close()

def get_regis(page_size):
    session = SessionLocal()
    confesiones = session.query(registro).limit(page_size).all()
    session.close()
    return confesiones

def get_avistamientos():
    with SessionLocal() as session:
        filas = (
            session.query(avistamiento, voluntario.nombre, ave.nombre, registro)
            .join(
                voluntario,
                avistamiento.voluntario_id == voluntario.id
            )
            .join(ave, avistamiento.ave_id == ave.id)
            .outerjoin(
                registro,
                registro.avistamiento_id == avistamiento.id
            )
            .order_by(avistamiento.id.desc(), registro.id.asc())
            .all()
        )

        data = {}

        for avis, autor, nombre_ave, archivo in filas:
            if avis.id not in data:
                data[avis.id] = {
                    "autor": autor,
                    "ave": nombre_ave,
                    "fecha": avis.fecha_hora.strftime("%d/%m/%Y %H:%M"),
                    "lugar": avis.lugar,
                    "descripcion": avis.descripcion or "",
                    "archivos": []
                }

            if archivo is not None:
                data[avis.id]["archivos"].append({
                    "ruta": archivo.ruta_archivo,
                    "nombre": archivo.nombre_archivo
                })

        return list(data.values())


#def create_avistamiento(vol_id, ave_id, fecha, lugar, descripcion):
    #session = SessionLocal()
    #new_avis = avistamiento(voluntario_id = vol_id, ave_id = ave_id, fecha_hora = fecha, lugar = lugar, descripcion = descripcion)
    #session.add(new_avis)
    #avistamient = session.query(avistamiento).filter_by(id = new_avis.id).first()
    #session.commit()
    #session.close()
    #return avistamient

def create_avistamiento(vol_id, ave_id, fecha, lugar, descripcion):
    with SessionLocal.begin() as session:
        new_avis = avistamiento(
            voluntario_id=vol_id,
            ave_id=ave_id,
            fecha_hora=fecha,
            lugar=lugar,
            descripcion=descripcion
        )
        session.add(new_avis)
        session.flush()  # Ejecuta el INSERT y obtiene el ID.
        avis_id = new_avis.id

    # Al salir del bloque se realiza el commit.
    return avis_id
def create_registro(ruta, nombre_arch, avis_id):
    session = SessionLocal()
    new_regis = registro(ruta_archivo = ruta, nombre_archivo = nombre_arch, avistamiento_id = avis_id)
    session.add(new_regis)
    session.commit()
    session.close()


def register_vol(username, password, email, fono, comuna):
    if get_user_by_email(email) is not None:
        return False, "El correo ya esta en uso."
    
    if get_user_by_username(username) is not None:
        return False, "El nombre de usuario esta en uso."
    
    create_voluntario(username, password, email, fono, comuna)
    return True, None

def login_user(username, password):
    a_user = get_user_by_username(username)
    if a_user is None:
        return False, "Usuario o contraseña incorrectos."
    
    if a_user.contrasena != password:
        return False, "Usuario o contraseña incorrectos."
    
    return True, None
