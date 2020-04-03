from prometheus_client import REGISTRY, generate_latest
from CsvCollector import CsvCollector
from flask import Flask, redirect
import const

app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def get_metrics():
    return generate_latest()


@app.route("/", methods=["GET"])
def redirect_metrics():
    return redirect("/metrics", code=300)


def main():
    REGISTRY.register(CsvCollector(const.csv_directory))
    app.run("0.0.0.0", port=4050)


if __name__ == '__main__':
    main()
