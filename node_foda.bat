@echo off
:: Caminho onde o Node foi extraído
set NODE_DIR=C:\Users\discente\Downloads\node-v24.11.0-win-x64

:: Adiciona o Node temporariamente ao PATH
set PATH=%NODE_DIR%;%NODE_DIR%\node_modules\npm\bin;%PATH%

:: Abre o CMD já com o Node funcionando
cmd
