from flask import Flask, request, render_template
from helper import input_filter, retrieve, relevant_doc, get_docs, get_inputs, generate

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def main():
    if request.method == "POST":
        inputs = {
            "From Port": request.form.get("From Port"),
            "To Port": request.form.get("To Port"),
            "Loading Port": request.form.get("Loading Port"),
            "Discharging Port": request.form.get("Discharging Port"),
            "ship_type": request.form.get("ship_type"),
            "dwt": request.form.get("dwt"),
            "length": request.form.get("length"),
            "width": request.form.get("width"),
            "CAPEX Description": request.form.get("CAPEX Description"),
            "Fuel Type": request.form.get("Fuel Type"),
            "Cargo Type": request.form.get("Cargo Type"),
            "Laycan Start": request.form.get("Laycan Start"),
            "Laycan End": request.form.get("Laycan End"),
            "Pooling Price": request.form.get("Pooling Price"),
            
        }
        res = retrieve(input_filter(inputs))
        inputs_with_context = get_inputs(res)
        metadata_list = get_docs(res)
        pdf_files = relevant_doc(metadata_list)
        briefing = generate(inputs_with_context)
        
        return render_template("dashboard.html", briefing=briefing, pdf_files=pdf_files)
    
    
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)