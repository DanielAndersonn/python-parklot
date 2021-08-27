import sqlite3


try:
    sqliteC = sqlite3.connect(  ' SQLite_Python.db')
    sqlite_criando_tabela = ''' CREATE TABLE estacionamento (
      
      id PRIMARY KEY ,
      CorCarro TEXT NOT NULL,
      placaCarro TEXT NOT NULL,
      Hora  INT NOT NULL,
      totalPagar REAL NOT NULL

    )''' 


    Cursor = sqliteC.cursor()
    print('Banco de Dados criado com Sucesso conectado com SQLite')

    sqlite_select_query = 'select sqlicte_version() ;'
    curso. execute(sqlite_select_query)
    record =  cursor.fetchall()
    print('Banco de Dados versão:', record)
    cursor.close()

    except  sqlite3.Error as error:
        print(' Erro na conecção ao banco de dados sqlite',error)
    
    finally:
        if sqliteC:
            sqliteC.close()
            print('A conecção ao banco de Dados foi finalizada')

        
        