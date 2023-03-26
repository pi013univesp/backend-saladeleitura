from datetime import datetime

def Time_to_log():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    return data_e_hora_em_texto

def log_print(text):
    print(f"\n{text}, Horario: {Time_to_log()}")