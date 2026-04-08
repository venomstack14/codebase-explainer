from flask import Flask, render_template, request, jsonify

from parser import load_codebase
from analyzer import build_dependency_graph
from explainer import explain_file, explain_project
from qa import answer_question

app = Flask(__name__)

parsed_data_global = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    global parsed_data_global

    data = request.json
    folder_path = data.get("path")

    parsed_data = load_codebase(folder_path)
    parsed_data_global = parsed_data

    overview = explain_project(parsed_data)

    files = []
    for file, details in parsed_data.items():
        files.append(explain_file(file, details))

    graph = build_dependency_graph(parsed_data)

    graph_data = {
        "nodes": list(graph.nodes),
        "edges": list(graph.edges)
    }

    return jsonify({
        "overview": overview,
        "files": files,
        "graph": graph_data
    })

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")

    answer = answer_question(query, parsed_data_global)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)