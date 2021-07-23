from datetime import date, time, datetime
import sys

def trabalhando_date():
    x = date.today()
    print(x.strftime('%A/%B/%Y'))

def trabalhando_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H/%M/%S'))

def trabalhando_date_time():
    agora = datetime.now() 
    print(agora.strftime('%d/%m/%Y - %H/%M/%S'))
    print(agora.strftime('%c'))
    tupla = ('Segunda', 'Terça', 'Qaurata', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[agora.weekday()])
    
    data_criada = datetime(2021, 7, 18, 00, 00, 00)
    print(data_criada.strftime('%c'))
    print(tupla[data_criada.weekday()])

    data_str = '01/01/2019'
    data_convertida = datetime.strptime(data_str, '%d/%m/%Y')
    print(data_convertida)

if __name__ == "__main__":
    trabalhando_date()
    trabalhando_time()
    trabalhando_date_time()
