from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from SqlHelper import SqlHelper
from json_tricks import dumps

app = Flask(__name__)
api = Api(app)

sqlHelper = SqlHelper()

product_put_args = reqparse.RequestParser()
product_put_args.add_argument("id" , type=int , help="id is required", required=True)
product_put_args.add_argument("product_id" , type=int , help="product_id is required", required=True)
product_put_args.add_argument("product_name" , type=str , help="product_name is required", required=True)
product_put_args.add_argument("price_newest" , type=int , help="price_newest is required", required=False)
product_put_args.add_argument("price_average" , type=int , help="price_average is required", required=False)
product_put_args.add_argument("price_best" , type=int , help="price_best is required", required=False)
product_put_args.add_argument("price_worst" , type=int , help="price_worst is required", required=False)
product_put_args.add_argument("discount_priceleft" , type=float , help="discount_priceleft is required", required=False)
product_put_args.add_argument("discount_percent" , type=float , help="discount_percent is required", required=False)
product_put_args.add_argument("average_safe" , type=float , help="average_safe is required", required=False)
product_put_args.add_argument("average_safe_worst" , type=float , help="average_safe_worst is required", required=False)
product_put_args.add_argument("diff_best" , type=int , help="diff_best is required", required=False)
product_put_args.add_argument("url" , type=str , help="url is required", required=False)
product_put_args.add_argument("best_historical_flag" , type=bool , help="best_historical_flag is required", required=False)
product_put_args.add_argument("umbral" , type=int , help="umbral is required", required=False)
product_put_args.add_argument("umbral_flag" , type=bool , help="umbral_flag is required", required=False)
product_put_args.add_argument("reg_date" , type=str , help="reg_date is required", required=False)

productHistorical = {}

def abort_if_product_id_doesnt_exist(productHistorical, product):

    if product not in productHistorical:

        abort(400, message="Could not find product...")



def abort_if_product_exists(productHistorical, product):

    if product in productHistorical:

        abort(409, message="product already exists with that ID...")



class APIComparator(Resource):


    def get(self, product_id):
        product_id -= 1
        productHistorical = sqlHelper.select_comparator()
        product = productHistorical[product_id]
        abort_if_product_id_doesnt_exist(productHistorical, product)
        return dumps(product)

    def put(self, product_id):
        #corregir el put
        product = productHistorical[product_id]
        abort_if_product_exists(productHistorical, product)
        args = product_put_args.parse_args()
        productHistorical[product_id] = args
        return productHistorical[product_id], 201


class APIComparatorList(Resource):

    def get(self):

        productHistorical = sqlHelper.select_comparator()
        return dumps(productHistorical)

    def put(self, product_id):
        #corregir el put
        product = productHistorical[product_id]
        abort_if_product_exists(productHistorical, product)
        args = product_put_args.parse_args()
        productHistorical[product_id] = args
        return productHistorical[product_id], 201


api.add_resource(APIComparator, "/comparator/product/<int:product_id>")
api.add_resource(APIComparatorList, "/comparator/list/")

if __name__ == "__main__":
    app.run(debug=True)