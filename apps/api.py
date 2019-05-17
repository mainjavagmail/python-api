# -*- coding: utf-8 -*-

# Importamos as classes API e Resource
from flask_restful import Api, Resource
from apps.users.resources import SignUp
from apps.users.resources_admin import AdminUserPageList, AdminUserResource


class Index(Resource):  # Criamos uma classe que extende de Resource

    # Definimos a operação get do protocolo http
    def get(self):

        # retornamos um simples dicionário que será automáticamente
        # retornado em json pelo flask
        return {'hello': 'world by apps'}


# Instânciamos a API do FlaskRestful
api = Api()


def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index
    api.add_resource(Index, '/')
    api.add_resource(SignUp, '/users')
    api.add_resource(AdminUserPageList, '/admin/users/page/<int:page_id>')
    api.add_resource(AdminUserResource, '/admin/users/<string:user_id>')
    api.add_resource(AuthResource, '/auth')
    api.add_resource(RefreshTokenResource, '/auth/refresh')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)
