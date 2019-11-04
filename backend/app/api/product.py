from flask import json, Response
from app.models import Product, ProductSchema
from app.api import bp

product_schema = ProductSchema()


@bp.route("/products", methods=["GET"])
def get_products():
    products = Product.get_all_products()
    #print(products)
    serialize_products = product_schema.dump(products, many=True).data
    return custom_response(serialize_products, 200)


def custom_response(res, status_code):
    return Response(mimetype="application/json", response=json.dumps(res), status=status_code)

