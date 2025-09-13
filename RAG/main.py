from flask import Flask, request, render_template
from helper import input_filter, retrieve, relevant_doc, get_docs, get_inputs, generate

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def main():
    if request.method == "POST":
        inputs = {
            "origin_port": request.form.get("origin_port"),
            "destination_port": request.form.get("destination_port"),
            "ship_type": request.form.get("ship_type"),
            "dwt": request.form.get("dwt"),
            "length": request.form.get("length"),
            "width": request.form.get("width"),
            "draft": request.form.get("draft"),
            "fuel_type": request.form.get("fuel_type"),
            "cargo": request.form.get("cargo"),
            "timeframe": request.form.get("timeframe")
        }
        res = retrieve(input_filter(inputs))
        inputs_with_context = get_inputs(res)
        metadata_list = get_docs(res)
        pdf_files = relevant_doc(metadata_list)
        briefing = generate(inputs_with_context)
        
        return render_template("dashboard.html", briefing=briefing, pdf_files=pdf_files)
    