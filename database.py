import mysql.connector
from mysql.connector import Error

def conectar ():
    try: # tente executar
        conexao = mysql.connector.connect(
        host="localhost",       # Endereço
        user="root",            # Usuário
        password="senai",       # Senha
        database="estodolist"   # Datbase criado
        )

        cursor = conexao.cursor(dictionary=True) # Devolve no formato Dict
        # retorna duas informações: Conexão e cursor
        return conexao, cursor 

    except Error as erro: # ERRO!
        print(f"ERRO! Falha ao se conectar com o banco de dados: {erro}")
        return None, None


def inserir_tarefa(Nome_tarefa,Descricao,Categoria,Data_prazo,Prioridade):
    conexao, cursor = conectar() # Se conectar com BD

    # Verifica se a conexão funcionou
    if conexao is None:
        return False

    try:
        # %s SQL Parametrizado para evitar SQL Injection
        sql = "INSERT INTO tarefa (nomeTarefa,descricao,categoria,dataPrazo,prioridade) VALUES (%s, %s ,%s ,%s , %s)"
        # Executa o SQL Parametrizado e passa os parâmetro da função
        cursor.execute(sql,(Nome_tarefa,Descricao,Categoria,Data_prazo,Prioridade))
        # Confirma as alterações
        conexao.commit()
        # Retornar TRUE para função principal
        return True
    
    except Error as erro:
        print(f"ERRO! Falha ao inserir a terefa: {erro}")
        return False
    finally: # Encerra dando certo ou não. ERRO!
        cursor.close() #fechou o cursor
        conexao.close() #Fechou a conexao 

# Retorna todas as tarefas cadastradas no Banco de Dados
def consultar_tarefas():

    # Chama a função Conectar
    conexao, cursor = conectar()

    #Verificar se a conexão falhou
    if conexao is None:
        return[] #Lista Vazia

    try: # tente executar o comando SQL
        # Selecione todas as colunas da(origem) tabela tarefa;
        sql =   """
                SELECT 
                  idTarefa AS Idtarefa,
                  dataPrazo AS Data_prazo,
                  status,
                  prioridade AS Prioridade,
                  categoria AS Categoria,
                  nomeTarefa AS Nome_tarefa,
                  descricao AS Descricao

                FROM tarefa
                """
        # Executa o comando da variável SQL
        cursor.execute(sql)

        # Buscar todas as linhas da consulta executada
        tarefas = cursor.fetchall()

        # Retorna para a programação principal as terefas
        return tarefas # Lista de Dicionarios (DICT)

    except Error as erro: #se der erro
        print(f"ERRO! Falha ao listar as tarefas: {erro}")
        return[] # Retorna lista vazia em caso de erro

    finally: #Finalize sempre
        cursor.close() # Encerra o cursor
        conexao.close() # Encerra a conexao


# Essa função marca como concluida a tarefa indicada
def concluir_tarefa(idtarefa):

    conexao, cursor = conectar()

    if conexao is None:
        return False

    try:
        sql = "UPDATE tarefa SET status = 'Concluida' WHERE idTarefa = %s"
        cursor.execute(sql,(idtarefa,)) # , obrigatoria para informar q é tupla
        conexao.commit() # Confirma a alterção nos dados

        return True

    except Error as erro:
        print(f"ERRO! Falha ao listar as tarefas: {erro}")
        return False # Retorna falso em caso de erro

    finally:
        cursor.close() # Encerra o cursor
        conexao.close() # Encerra a conexao


# Essa função editara as tarefas indicada
def alterar_tarefa(idtarefa,Nome_tarefa,Descricao,Categoria,Data_prazo,Prioridade):

    conexao, cursor = conectar()

    if conexao is None:
        return False

    try: 
        sql = """
        UPDATE tarefa
        SET 
        nomeTarefa = %s,
        descricao = %s,
        categoria = %s, 
        dataPrazo = %s, 
        prioridade = %s
        WHERE idtarefa = %s
        """
        cursor.execute(sql,(Nome_tarefa, Descricao, Categoria, Data_prazo, Prioridade, idtarefa)) 
        
        conexao.commit() # Confirma a alterção nos dados

        return True

    except Error as erro:
        print(f"ERRO! Falha ao editar as tarefas: {erro}")
        return False # Retorna falso em caso de erro

    finally:
        cursor.close() # Encerra o cursor
        conexao.close() # Encerra a conexao

def apagar_tarefa(idtarefa):

    conexao, cursor = conectar()

    if conexao is None:
        return False

    try: 
        sql = "DELETE FROM tarefa WHERE idtarefa = %s"
        
        cursor.execute(sql,(idtarefa,)) 
        
        conexao.commit() # Confirma a exclusão

        return True

    except Error as erro:
        print(f"ERRO! Falha ao excluir a tarefa: {erro}")
        return False # Retorna falso em caso de erro

    finally:
        cursor.close() # Encerra o cursor
        conexao.close() # Encerra a conexao