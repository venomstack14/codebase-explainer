async function analyze() {
  const path = document.getElementById("path").value;

  const res = await fetch("/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ path })
  });

  const data = await res.json();

  document.getElementById("overview").innerText = data.overview;

  let filesHTML = "";
  data.files.forEach(f => {
    filesHTML += `<div>${f}</div><hr/>`;
  });

  document.getElementById("files").innerHTML = filesHTML;

  document.getElementById("graph").innerText =
    "Nodes: " + data.graph.nodes.length +
    "\nEdges: " + data.graph.edges.length;
}

async function ask() {
  const query = document.getElementById("question").value;

  const res = await fetch("/ask", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ query })
  });

  const data = await res.json();

  document.getElementById("answer").innerText = data.answer;
}