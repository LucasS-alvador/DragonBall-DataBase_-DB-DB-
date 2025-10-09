# DragonBall-DataBase_-DB-DB-
Projeto para DB de DB

Obra: (Nome, data_ini, data_fin, imagem)
Saga: (Nome, desc, ep_ini, ep_fin, Obra_id, imagem)

Raça: (Nome, cor, desc, poderBase. imagem)
Transformação: (Nome, cor, poder, especial, efeitoCol, imagem, tempo_lim)
PersonagemBase: (Nome, Raça_id, data_nasc, sexo,  imagem)
PersonagemSaga: (PersonagemBase_id, Saga_id, poder, Trans_id[], imagem)