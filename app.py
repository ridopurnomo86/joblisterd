from flask import Flask, request
import json
from crawling import main

app = Flask(__name__)


@app.route("/")
def index():
    return "Server is Running"


@app.route("/job-search")
def get_listjob():
    return json.dumps(main('https://www.jobstreet.co.id/en/job-search/job-vacancy.php'))


@app.route("/job-search/country")
def get_listjob_by_country():
    filter = request.args.get('filter')
    return json.dumps(main(f"https://www.jobstreet.co.id/en/job-search/${filter}-jobs/"))


@app.route("/job-search/search")
def get_listjob_by_search():
    filter = request.args.get('filter')
    return json.dumps(main(f"https://www.jobstreet.co.id/en/job-search/${filter}-jobs/"))


@app.route("/job-search/salary")
def get_listjob_by_salary():
    filter = request.args.get('filter')
    return json.dumps(main(f"https://www.jobstreet.co.id/en/job-search/job-vacancy.php?salary={filter or 0}&salary-max=2147483647"))


if __name__ == "__main__":
    app.run(debug=True)
