import os
import sys
from datetime import date

# Add project root to path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.app import app, db
from src.model.obra import Obra
from src.model.saga import Saga
from src.model.raca import Raca
from src.model.personagembase import PersonagemBase
from src.service.common_service import create_object, get_object_by_attribute

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
                imagem='https://static.wikia.nocookie.net/dragonball/images/4/4c/Saiyans.jpg',
                cor='#FFD700',  # Dourado
                poderBase=1000
            ),
            'Namekuseijin': get_or_create_object(
                Raca,
                nome='Namekuseijin',
                desc='Raça pacífica do Planeta Namekusei, com habilidades de cura e criação das esferas do dragão.',
                imagem='https://static.wikia.nocookie.net/dragonball/images/f/f2/Namekians.jpg',
                cor='#228B22',  # Verde floresta
                poderBase=500
            ),
            'Humano': get_or_create_object(
                Raca,
                nome='Humano',
                desc='Habitantes da Terra, com potencial para desenvolver poderes através de treinamento.',
                imagem='https://static.wikia.nocookie.net/dragonball/images/e/e5/Humans.jpg',
                cor='#CD853F',  # Marrom peru
                poderBase=100
            ),
            'Androide': get_or_create_object(
                Raca,
                nome='Androide',
                desc='Seres artificiais criados por cientistas, com poder ilimitado.',
                imagem='https://static.wikia.nocookie.net/dragonball/images/8/89/Androids.jpg',
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
            imagem='https://static.wikia.nocookie.net/dragonball/images/4/4b/Dragon_Ball_Anime_Logo.png'
        )

        # Sagas Dragon Ball
        get_or_create_object(
            Saga,
            desc='Saga Pilaf',
            epIni=1,
            epFim=13,
            obra_id=db_classico.id,
            imagem='https://static.wikia.nocookie.net/dragonball/images/5/53/Emperor_Pilaf_Saga.jpg'
        )

        get_or_create_object(
            Saga,
            desc='21º Torneio de Artes Marciais',
            epIni=14,
            epFim=28,
            obra_id=db_classico.id,
            imagem='https://static.wikia.nocookie.net/dragonball/images/a/a3/Tournament_Saga.jpg'
        )

        # Dragon Ball Z
        dbz = get_or_create_object(
            Obra,
            nome='Dragon Ball Z',
            dtIni=date(1989, 4, 26),
            dtFim=date(1996, 1, 31),
            imagem='https://static.wikia.nocookie.net/dragonball/images/4/4a/Dragon_Ball_Z_Anime_Logo.png'
        )

        # Sagas DBZ
        get_or_create_object(
            Saga,
            desc='Saga dos Saiyajins',
            epIni=1,
            epFim=35,
            obra_id=dbz.id,
            imagem='https://static.wikia.nocookie.net/dragonball/images/c/c5/SaiyanSagaNV.png'
        )

        get_or_create_object(
            Saga,
            desc='Saga de Freeza',
            epIni=36,
            epFim=107,
            obra_id=dbz.id,
            imagem='https://static.wikia.nocookie.net/dragonball/images/f/f7/FreezaSagaNV.png'
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