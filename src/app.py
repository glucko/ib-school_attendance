from .__init__ import app
@app.route("/")
def index():
    return "hello"

@app.route('/api/getqr/<int:id>', methods=['GET'])
def get_qr(id):
    pass

@app.route('/api/signin/<int:id>', methods=['POST'])
def signin(id):
    pass
