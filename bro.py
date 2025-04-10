from app import create_app, db
import redis
from rq import Connection, Worker
from app.models import User, Product, Feedback, UserSchema, ProductSchema
from flask.cli import FlaskGroup


app = create_app()
application = create_app()
cli = FlaskGroup(create_app=create_app)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Product": Product,
        "Feedback": Feedback,
        "UserSchema": UserSchema,
        "ProductSchema": ProductSchema,
    }


@cli.command("run_worker")
def run_worker():
    redis_url = app.config["REDIS_URL"]
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(app.config["QUEUES"])
        worker.work()


if __name__ == "__main__":
    cli()
