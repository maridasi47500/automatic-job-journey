from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_branche", methods=["GET","POST"])
def add_one_branche():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into branche (name) values (:name)",request.form)
        user = query_db('select * from branche')
        return render_template("brancheform.html", branches=user, one_user=one_user, the_title="add new branche")
    user = query_db('select * from branche')
    one_user = query_db("select * from branche limit 1", one=True)
    return render_template("brancheform.html", branches=user, one_user=one_user, the_title="add new branche")

@app.route("/add_one_domaine", methods=["GET","POST"])
def add_one_domaine():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into domaine (name) values (:name)",request.form)
        user = query_db('select * from domaine')
        return render_template("domaineform.html", domaines=user, one_user=one_user, the_title="add new domaine")
    user = query_db('select * from domaine')
    one_user = query_db("select * from domaine limit 1", one=True)
    return render_template("domaineform.html", domaines=user, one_user=one_user, the_title="add new domaine")

@app.route("/add_one_secteurdapplication", methods=["GET","POST"])
def add_one_secteurdapplication():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into secteurdapplication (name) values (:name)",request.form)
        user = query_db('select * from secteurdapplication')
        return render_template("secteurdapplicationform.html", secteurdapplications=user, one_user=one_user, the_title="add new secteurdapplication")
    user = query_db('select * from secteurdapplication')
    one_user = query_db("select * from secteurdapplication limit 1", one=True)
    return render_template("secteurdapplicationform.html", secteurdapplications=user, one_user=one_user, the_title="add new secteurdapplication")

@app.route("/add_one_job", methods=["GET","POST"])
def add_one_job():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into job (name) values (:name)",request.form)
        user = query_db('select * from job')
        return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")
    user = query_db('select * from job')
    one_user = query_db("select * from job limit 1", one=True)
    return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into country (name) values (:name)",request.form)
        user = query_db('select * from country')
        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")
    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,phone,country_id,job_id,secteurdapplication_id,domaine_id,branche_id) values (:username,:email,:phone,:country_id,:job_id,:secteurdapplication_id,:domaine_id,:branche_id)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

