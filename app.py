from app import app

app.config['SECRET_KEY'] = 'supercalifragilisticexpialidocious'
app.run(debug=True)