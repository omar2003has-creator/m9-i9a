python - <<'EOF'
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph

PREFIX = """
PREFIX : <http://aispire.example.org/publications/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""

sparql = SPARQLWrapper("http://localhost:3030/publications/sparql")
sparql.setReturnFormat(JSON)

queries = {
    "Q1": PREFIX + "SELECT DISTINCT ?author WHERE { ?paper :authoredBy ?author ; :publishedIn :NeurIPS . }",
    "Q2": PREFIX + "SELECT ?topic (COUNT(?paper) AS ?n) WHERE { ?paper :topic ?topic . } GROUP BY ?topic",
    "Q7": PREFIX + "SELECT ?paper ?cc WHERE { ?paper :citationCount ?cc . } ORDER BY DESC(?cc) LIMIT 5",
    "Q8": PREFIX + "SELECT DISTINCT ?author WHERE { ?author ?label 'Hinton' . FILTER (?label = skos:prefLabel || ?label = skos:altLabel) }",
}

for name, q in queries.items():
    sparql.setQuery(q)
    r = sparql.query().convert()
    rows = r["results"]["bindings"]
    print(f"\n{name} — {len(rows)} rows:")
    for row in rows[:5]:
        print(" ", {k: v["value"].split("/")[-1] for k,v in row.items()})
EOF