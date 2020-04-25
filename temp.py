


my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return 'HELLO EVERYONE HOW IS IT GOING'


if __name__ == '__main__':
    my_awesome_app.run()








app = Flask(__name__)
app.debug = True
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route('/')
def index():
   return render_template('hello.html')
if __name__ == '__main__':
    app.run()
