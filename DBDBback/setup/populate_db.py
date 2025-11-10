import os
import sys
from datetime import date

# Add project root to path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Also add the `src` folder to path so modules like `app` and `database` are importable
SRC = os.path.join(ROOT, 'src')
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from app import app, db
from model.obra import Obra
from model.saga import Saga
from model.raca import Raca
from model.personagembase import PersonagemBase
from service.common_service import create_object, get_object_by_attribute

def get_or_create_object(Model, **kwargs):
    """Get an existing object or create a new one if it doesn't exist"""
    query_kwargs = {k: v for k, v in kwargs.items() if k != 'desc' and k != 'descricao'}
    instance = Model.query.filter_by(**query_kwargs).first()
    if instance is None:
        instance = create_object(Model, **kwargs)
    return instance

def populate_db():
    with app.app_context():
        # Criar raças principais
        racas = {
            'Saiyajin': get_or_create_object(
                Raca,
                nome='Saiyajin',
                desc='Uma raça guerreira do Planeta Vegeta, conhecida por seu orgulho e poder de luta crescente.',
                imagem='https://static.wikia.nocookie.net/tkoc/images/c/c4/SaiyansDBKK.png/revision/latest?cb=20130305060812&path-prefix=pt-br',
                cor='#FFD700',  # Dourado
                poderBase=1000
            ),
            'Namekuseijin': get_or_create_object(
                Raca,
                nome='Namekuseijin',
                desc='Raça pacífica do Planeta Namekusei, com habilidades de cura e criação das esferas do dragão.',
                imagem='https://www.einerd.com/wp-content/uploads/2021/02/namekuseijins-dragon-ball-super-e1614168124558.jpg',
                cor='#228B22',  # Verde floresta
                poderBase=500
            ),
            'Humano': get_or_create_object(
                Raca,
                nome='Humano',
                desc='Habitantes da Terra, com potencial para desenvolver poderes através de treinamento.',
                imagem='https://static.wikia.nocookie.net/dragonball/images/d/d8/SatanFan%28Jmp%29.png/revision/latest?cb=20110222143410',
                cor='#CD853F',  # Marrom peru
                poderBase=100
            ),
            'Androide': get_or_create_object(
                Raca,
                nome='Androide',
                desc='Seres artificiais criados por cientistas, com poder ilimitado.',
                imagem='https://static.wikia.nocookie.net/dragonball/images/1/10/Androids.jpeg/revision/latest?cb=20141228144731&path-prefix=pt-br',
                cor='#4682B4',  # Azul aço
                poderBase=5000
            )
        }

        # Dragon Ball
        db_classico = get_or_create_object(
            Obra,
            nome='Dragon Ball',
            dtIni=date(1986, 2, 26),
            dtFim=date(1989, 4, 19),
            imagem='https://imgsrv.crunchyroll.com/cdn-cgi/image/fit=cover,format=auto,quality=85,width=1920/keyart/G8DHV7W21-backdrop_wide'
        )

        # Sagas Dragon Ball
        get_or_create_object(
            Saga,
            desc='Saga Pilaf',
            epIni=1,
            epFim=13,
            obra_id=db_classico.id,
            imagem='https://lh4.googleusercontent.com/proxy/Pv26eoJTCtZhJ9lK_-OkyTw2g03SvVqZK4bItkS3PQW2toEGhQFqJQROuD1tYL-yDZ7JjIHoE2mG-1EJoGLJVO4Snq6DVB-B2AU8r8CIn1USS8m-la7_yjUT7sWEmmSYEQ'
        )

        get_or_create_object(
            Saga,
            desc='21º Torneio de Artes Marciais',
            epIni=14,
            epFim=28,
            obra_id=db_classico.id,
            imagem='https://static.wikia.nocookie.net/dragonball/images/c/c4/Tournamentsagaconceptart.jpg/revision/latest/scale-to-width-down/648?cb=20150415021349&path-prefix=pt-br'
        )

        # Dragon Ball Z
        dbz = get_or_create_object(
            Obra,
            nome='Dragon Ball Z',
            dtIni=date(1989, 4, 26),
            dtFim=date(1996, 1, 31),
            imagem='https://m.media-amazon.com/images/S/pv-target-images/c9295bf92a8c87f865116be60daa6a31509823c8c11da3fcbc5a6dc589ff9da2.jpg'
        )

        # Sagas DBZ
        get_or_create_object(
            Saga,
            desc='Saga dos Saiyajins',
            epIni=1,
            epFim=35,
            obra_id=dbz.id,
            imagem='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0sSwREAJH9f90DqHjlSK1aOOh_sI3-i9aKw&s'
        )

        get_or_create_object(
            Saga,
            desc='Saga de Freeza',
            epIni=36,
            epFim=107,
            obra_id=dbz.id,
            imagem='https://i.redd.it/whats-your-favourite-section-of-the-frieza-saga-v0-hf4cnw2o5uue1.png?width=1000&format=png&auto=webp&s=8d2bbe99f5660e3df8f59e4e085f709a97da9ad2'
        )

        get_or_create_object(
            Saga,
            desc='Saga dos Androides',
            epIni=108,
            epFim=139,
            obra_id=dbz.id,
            imagem='https://static.wikia.nocookie.net/dragonball/images/b/b5/AndroidSagaNV.png'
        )

        # Dragon Ball Super
        dbs = get_or_create_object(
            Obra,
            nome='Dragon Ball Super',
            dtIni=date(2015, 7, 5),
            dtFim=date(2018, 3, 25),
            imagem='https://static.wikia.nocookie.net/dragonball/images/4/4b/Dragon_Ball_Super_Logo.png'
        )

        # Sagas DBS
        get_or_create_object(
            Saga,
            desc='Saga do Deus da Destruição Bills',
            epIni=1,
            epFim=14,
            obra_id=dbs.id,
            imagem='https://static.wikia.nocookie.net/dragonball/images/7/72/God_of_Destruction_Beerus_Saga.jpg'
        )

        get_or_create_object(
            Saga,
            desc='Saga do Torneio do Poder',
            epIni=77,
            epFim=131,
            obra_id=dbs.id,
            imagem='https://static.wikia.nocookie.net/dragonball/images/4/4c/Tournament_of_Power.jpg'
        )

        # Personagens principais
        get_or_create_object(
            PersonagemBase,
            nome='Son Goku',
            dataNasc=date(737, 4, 16),  # Ano 737 na cronologia DB
            raca_id=racas['Saiyajin'].id,
            descricao='Protagonista da série, um Saiyajin criado na Terra que se tornou seu maior protetor.',
            sexo='M',
            imagem='https://static.wikia.nocookie.net/dragonball/images/5/5b/Goku_DB_Ep_001.png'
        )

        get_or_create_object(
            PersonagemBase,
            nome='Vegeta',
            dataNasc=date(732, 11, 12),  # Ano 732 na cronologia DB
            raca_id=racas['Saiyajin'].id,
            descricao='Príncipe dos Saiyajins, inicialmente um vilão que se torna um dos principais heróis.',
            sexo='M',
            imagem='https://static.wikia.nocookie.net/dragonball/images/d/dc/Vegeta_DBZ_Ep_01.png'
        )

        get_or_create_object(
            PersonagemBase,
            nome='Piccolo',
            dataNasc=date(753, 5, 9),  # Ano 753 na cronologia DB
            raca_id=racas['Namekuseijin'].id,
            descricao='Inicialmente um vilão, se torna um dos mentores e aliados mais importantes de Gohan.',
            sexo='M',
            imagem='https://static.wikia.nocookie.net/dragonball/images/5/5d/Piccolo_DBZ_Ep_01.png'
        )

        get_or_create_object(
            PersonagemBase,
            nome='Gohan',
            dataNasc=date(757, 5, 18),  # Ano 757 na cronologia DB
            raca_id=racas['Saiyajin'].id,  # Meio-Saiyajin, mas classificado como Saiyajin
            descricao='Filho de Goku e Chi-Chi, possui um potencial imenso e se torna um dos guerreiros mais poderosos.',
            sexo='M',
            imagem='https://static.wikia.nocookie.net/dragonball/images/3/3c/Gohan_DBZ_Ep_01.png'
        )

if __name__ == '__main__':
    try:
        populate_db()
        print("Banco de dados populado com sucesso!")
    except Exception as e:
        print(f"Erro ao popular banco de dados: {str(e)}")