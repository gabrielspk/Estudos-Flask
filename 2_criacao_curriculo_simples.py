from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '''

    <!DOCTYPE html>
    
    <html lang="en">
    
    <head>
    <meta charset="utf-8">
    <head>        
        <meta charset="utf-8">
        
        <meta name="viewport" content="width=device, initial scale=1.0">
        
        <title>Menu meu curriculo</title>
        
    </head>
    
    <body>
        <h1>Gabriel Ferreira</h1>
        <p><strong>Email:</strong>gabrielsilvaferreira007@gmail.com</p>
        <p><strong>Linkedin:</strong>linkedin_gabriel</p>
        <p><strong>Telefone:</strong>989407779</p>
        
        <h2>Objetivo profissional</h2>
        <p>Seu objetivo profissional</p>
        
        <h2>Experiência profissional</h2>
        <p>Detalhes da sua experiência profissional</p>
        
        <h2>Educacao</h2>
        <p>SENAI</p>
        
        <h2>Habilidades</h2>
        <ul>
            <li>habilidade 1</li>
            <li>habilidade 2</li>
            <li>hbailidade 3</li>
        </ul>
    </body>
    </html>
        
    '''

if __name__ == "__main__":
    app.run(debug=True)
