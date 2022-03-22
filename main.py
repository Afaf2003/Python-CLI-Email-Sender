import typer  # To Taking input in cmd we use this module
import smtplib  # Use fro sending Mails to other
app = typer.Typer()


@app.command()
def enter(sender: str, receivers: str, password: str, subject: str, body: list[str]):
    body1 = ""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    for i in body:
        body1 = body1 + " " + i
    # Taking body as multiple sting we define another variable
    message = f'subject:{subject}\n\n{body1}'
    server.starttls()
    server.login(sender, password)
    print('Login Successfully')
    server.sendmail(sender, receivers, message)
    print("Email Sent Successfully")


if __name__ == "__main__":
    app()
