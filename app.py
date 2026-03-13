from flask import Flask,render_template,request,redirect,session,flash
import psycopg2
app = Flask(__name__)
app.secret_key = "123456" #porque estamos trabalhando com sessao

def ligar_banco():
    banco = psycopg2.connect(
        host="localhost",
        dbname="SiteContato",
        user="postgres",
        password="senai",
        port="5432"
    )
    return banco



@app.route('/')
def inicio():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('index.html')



@app.route('/tipografia')
def tipografia():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('typography.html')



@app.route('/componente')
def componente():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('components.html')



@app.route('/icone')
def icone():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('icons.html')



@app.route('/variacao_icone')
def variacao_icone():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('icon-variations.html')



@app.route('/sobre')
def sobre():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('about.html')



@app.route('/404')
def sorry():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('404.html')



@app.route('/portfolio2')
def portfolio2():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('portfolio-2cols.html')



@app.route('/portfolio3')
def portfolio3():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('portfolio-3cols.html')



@app.route('/portfolio4')
def portfolio4():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('portfolio-4cols.html')



@app.route('/detalhe_portifolio')
def detalhe_portifolio():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('portfolio-detail.html')



@app.route('/blog_esquerda')
def blog_esquerda():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('blog-left-sidebar.html')



@app.route('/blog_direita')
def blog_direita():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('blog-right-sidebar.html')



@app.route('/post_esquerda')
def post_esquerda():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('post-left-sidebar.html')



@app.route('/post_direita')
def post_direita():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('post-right-sidebar.html')



@app.route('/tabela')
def tabela():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('pricingbox.html')


@app.route('/contato')
def Contato():
    if "usuario_id" not in session:
        return redirect("/login")
    return render_template('contact.html')



@app.route("/contato/enviar", methods=['POST'])
def enviar_contato():
    nome = request.form.get('nome')
    email = request.form.get('email')
    assunto = request.form.get('assunto')
    mensagem = request.form.get('mensagem')
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("""
                    INSERT INTO contato(nome, email, assunto, mensagem)
                    VALUES (%s, %s, %s, %s)
                    """, (nome, email, assunto, mensagem)
                   )
    banco.commit()
    banco.close()
    return redirect("/contato")


                                                    ### Login ###
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar',methods=['POST'])
def autenticar():
    email = request.form.get('email')
    senha = request.form.get('senha')
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("""
        SELECT id,nome
        FROM usuario
        WHERE email = %s AND senha = %s
    """, (email, senha))
    usuario = cursor.fetchone()
    banco.close()
    if usuario:
        session['usuario_id'] = usuario[0]
        session['usuario_nome'] = usuario[1]
        return redirect("/")
    else:
        flash('Login inválido')
        return redirect("/login")

@app.route('/deslogar')
def logout():
    session.clear()
    return redirect("/login")


                                                ### Cadastro ###
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/criar', methods=["POST"])
def criar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute( """
        INSERT INTO usuario (nome, email, senha)
        VALUES (%s,%s,%s)""", (nome, email, senha))
    banco.commit()
    banco.close()
    return redirect("/")


@app.route('/termos')
def termos():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run()
