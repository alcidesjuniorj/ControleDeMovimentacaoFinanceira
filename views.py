from models import Conta, engine,Bancos, Status, Historico, Tipos
from sqlmodel import Session, select
from datetime import date,timedelta

def criar_conta(conta:Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco == conta.banco)
        results = session.exec(statement).all()
        if results:
            print("Já existe uma conta nesse banco!")
            return
        
        session.add(conta)
        session.commit()

def listar_contas():
    with Session(engine) as session:
        statement = select(Conta)
        results = session.exec(statement).all()
    return results

def desativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == id)
        conta = session.exec(statement).first()

        if conta.valor > 0:
            print(f"Essa conta ainda possui saldo: {conta.valor}")
            #raise ValueError(f'Essa conta ainda possui saldo. {conta.valor}')
        
        conta.status = Status.INATIVO
        session.commit()

def ativar_conta(id, valor):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == id)
        conta = session.exec(statement).first()

        if valor <= 0:
            print(f"Necessário depositar uma valor para ativar a conta.")
            return
                
        conta.status = Status.ATIVO
        conta.valor = valor
        session.commit()

def transferir_saldo(id_conta_saida, id_conta_entrada, valor):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == id_conta_saida)
        conta_saida = session.exec(statement).first()
        if conta_saida.valor < valor:
            raise ValueError('Saldo Insuficiente.')
        
        statement = select(Conta).where(Conta.id == id_conta_entrada)
        conta_entrada = session.exec(statement).first()

        conta_saida.valor -= valor
        historico_saida = Historico(conta_id= id_conta_saida, tipo=Tipos.SAIDA, valor=valor, data = date.today())
        movimentar_dinheiro(historico_saida)

        conta_entrada.valor +=valor
        historico_entrada = Historico(conta_id= id_conta_entrada, tipo=Tipos.ENTRADA, valor=valor, data = date.today())
        movimentar_dinheiro(historico_entrada)

        session.commit()
        print('Tranferencia efetuada com sucesso!!!')        

def movimentar_dinheiro(historico: Historico):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id==historico.conta_id)
        conta = session.exec(statement).first()

        if historico.tipo == Tipos.ENTRADA:
            conta.valor += historico.valor
        else:
            if conta.valor < historico.valor:
                raise ValueError("Saldo insuficiente")
            conta.valor -= historico.valor

        session.add(historico)
        session.commit()
        return historico
    
def total_contas():
    with Session(engine) as session:
        statement = select(Conta)
        contas = session.exec(statement).all()

    total = 0
    for conta in contas:
        total += conta.valor

    return float(total)

def buscar_historicos_entre_datas(data_inicio: date, data_fim: date):
    with Session(engine) as session:
        statement = select(Historico).where(
            Historico.data >= data_inicio,
            Historico.data <= data_fim
        )
        resultados = session.exec(statement).all()
        return resultados

def criar_grafico_por_conta():
    with Session(engine) as session:
        statement = select(Conta).where(Conta.status == Status.ATIVO)
        contas = session.exec(statement).all()
        bancos = [i.banco.value for i in contas]
        total = [i.valor for i in contas]
        import matplotlib.pyplot as plt
        plt.bar(bancos, total)
        plt.show()

#conta = Conta(valor=6000.00, banco = Bancos.PICPAY)
#criar_conta(conta)

#for conta in listar_contas():
 #   print(conta.banco)
 
#ativar_conta(1,15.0)
#transferir_saldo(1, 2, 4.95)

#historico = Historico(conta_id= 1, tipo=Tipos.ENTRADA, valor=5.5, data = date.today())
#movimentar_dinheiro(historico)

#print(total_contas())

#x = buscar_historicos_entre_datas(date.today() - timedelta(days=1), date.today()+timedelta(days=1))
#print(x)

criar_grafico_por_conta()