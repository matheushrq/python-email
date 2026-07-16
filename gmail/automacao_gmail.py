from imap_tools import MailBox, AND
import os

user = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
server = os.getenv("SERVER")
port = int(os.getenv("PORT"))
email_from = os.getenv("EMAIL_FROM")
email_subject = os.getenv("EMAIL_SUBJECT")

def testa_conexao():
    try:
        meu_email = MailBox(server, port).login(user, password)
        return meu_email
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return False

meu_email = testa_conexao()

lista = meu_email.fetch(AND(from_=email_from, subject=email_subject))

def processar_emails(mes, dia):
    try:
        pasta_destino = "arquivo"
        os.makedirs(pasta_destino, exist_ok=True)

        for email in lista:
            if len(email.attachments) > 0:
                for anexo in email.attachments:
                    if anexo.filename.endswith('.pdf'):
                        with open(os.path.join(pasta_destino, f"{mes}_{dia}_{anexo.filename}"), "wb") as f:
                            f.write(anexo.payload)
                        print(f"Anexo {anexo.filename} salvo com sucesso em {pasta_destino}!")
    except Exception as e:
        print(f"Erro ao processar emails: {e}")