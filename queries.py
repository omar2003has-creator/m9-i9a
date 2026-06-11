PREFIX = """
PREFIX : <http://aispire.example.org/publications/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""
def q1():
   return """
    PREFIX : <http://aispire.example.org/publications/>
    SELECT DISTINCT  ?author
    WHERE {
       ?paper :authoredBy ?author ;
             :publishedIn :NeurIPS .
    
    }

    
    """
def q2():
    return """
        PREFIX : <http://aispire.example.org/publications/>
        SELECT ?topic (COUNT(?paper) AS ?n)
        WHERE {
          ?paper :topic ?topic .
        }
        GROUP BY ?topic
        """
def q3():
    return  """
PREFIX : <http://aispire.example.org/publications/>    
SELECT DISTINCT ?a ?b
WHERE {
    ?paper :authoredBy ?a ;
         :authoredBy ?b .
    FILTER (str(?a) < str(?b))
}"""

def q4():
    return """
        PREFIX : <http://aispire.example.org/publications/>
        SELECT ?paper ?doi
        WHERE {
          ?paper a :Paper .

          OPTIONAL {
            ?paper :doi ?doi .
          }
        }
        """
def q5():
    return """
        PREFIX : <http://aispire.example.org/publications/>
        ASK {
          {
            SELECT ?author
            WHERE {
              ?p :authoredBy ?author .
            }
            GROUP BY ?author
            HAVING (COUNT(?p) > 10)
          }
        }
        """
def q6():
    return """
        PREFIX : <http://aispire.example.org/publications/>
        CONSTRUCT {
          ?paper :authoredBy ?author .
        }
        WHERE {
          ?paper :year 2023 ;
                 :authoredBy ?author .
        }
    """
def q7():
    return """
        PREFIX : <http://aispire.example.org/publications/>
        SELECT ?paper ?cc
        WHERE {
          ?paper :citationCount ?cc .
        }
        ORDER BY DESC(?cc)
        LIMIT 5
    """
def q8():
    return """
        PREFIX : <http://aispire.example.org/publications/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

        SELECT ?author
        WHERE {
          ?author ?label "Hinton" .
          FILTER (?label = skos:prefLabel || ?label = skos:altLabel)
        }
    """