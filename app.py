from flask import Flask
import config, os
from dotenv import load_dotenv

load_dotenv()



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def main():
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug=True)