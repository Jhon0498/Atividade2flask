from flask import Flask, render_template_string, request # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
       return render_template_string('''
        <h1>Avaliação contínua: Aula 030</h1>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/identificacao">Identificação</a></li>
            <li><a href="/contexto">Contexto da requisição</a></li>
        </ul>
    ''')      
@app.route('/identificacao')
def identificacao():
    return render_template_string("""
        <h1>Avaliação contínua: Aula 030</h1>
        <h2>Aluno: Jhonatan Mendes</h2> 
        <h2>Prontuário: PT3026931</h2>
        <h2>Instituição: IFSP</h2>
        <a href="/">Voltar</a>
     """)
    
@app.route('/contexto')
def contexto():
    user_agent = request.headers.get("User-agent")
    remote_ip = request.remote_addr
    host_name = request.host
    
    return render_template_string("""
        <h1>Avaliação contínua: Aula 030</h1>
        <h2>Seu navegador é: {{user_agent}}</h2>     
        <h2>O ip remoto é: {{remote_ip}}</h2>
        <h2> O host da aplicação é: {{host_name}}</h2>
        <a href="/">Voltar</a>
        
    """, user_agent=user_agent, remote_ip=remote_ip, host_name=host_name)
if __name__ == '__main__':
    app.run(debug=True)


