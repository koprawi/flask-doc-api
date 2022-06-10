from flask import Flask, jsonify
from flask_restx import Resource, Api, fields

app = Flask(__name__)
apidoc = Api(app, version='1.0', title='SIA API', 
description = 'SIA API v 1.0') 

sia = apidoc.namespace('sia', description='SIA API')
mahasiswa_model = sia.model('SIA', {
    'id': fields.Integer(required=True, description='id identifier'),
    'nama': fields.String(required=True, description='nama mahasiswa')
})

mahasiswa = [

    {
        'id':1,
        'nama':'Budi'
    },
    {
        'id':2,
        'nama':'Andi'
    },
    {
        'id':3,
        'nama':'Ani'
    },

]

@app.route('/')
def hello():
    return jsonify({'message':'hello world'})

@sia.route('/mahasiswa')
class Mahasiswa_all(Resource):
    @sia.doc('get_mahasiswa_model')
    @sia.marshal_with(mahasiswa_model)
    def get(self):
        return mahasiswa


@sia.route('/mahasiswa/<int:id>')
@sia.param('id', 'id identifier')
class Mahasiswa_by_id(Resource):
    @sia.doc('get_mahasiswa_model')
    @sia.marshal_with(mahasiswa_model)
    def get(self, id):
        data = {}
        for x in mahasiswa:
            if x['id'] == id:
                data = {
                    'id': x['id'],
                    'nama': x['nama']
                }
        return data

if __name__ == '__main__':
    app.run(debug=True)
