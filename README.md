# DragonBall-DataBase_-DB-DB-
Projeto para DB de DB

Obra: (Nome, data_ini, data_fin, imagem)
Saga: (Nome, desc, ep_ini, ep_fin, Obra_id, imagem)

Raça: (Nome, cor, desc, poderBase, imagem)
Transformação: (Nome, cor, poder, especial, efeitoCol, imagem, tempo_lim)
PersonagemBase: (Nome, Raça_id, data_nasc, sexo,  imagem)

PersonagemSaga: (PersonagemBase_id, Saga_id, poder, Trans_id[], imagem)

1) baixar .zip em node.js
descompactar em c:\node
2) abrir powershell no modo admin
3) executar: 
 setx /M PATH "%PATH%;C:\node\"  
