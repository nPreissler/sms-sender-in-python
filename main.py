import pandas as pd
from twilio.rest import Client 
        
account_sid = "[twilio_account_sid]"
auth_token = "[twilio_auth_token]"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas: {vendas}.')
        message = client.messages.create(
            to="[your_phone_number]",
            from_="[your_twilio_number]",
            body=f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor}, Vendas: {vendas}')
        print(message.sid)