import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD

# Define namespaces
keyword_pub = Namespace("http://www.example.edu/publication/keyword/")
organization_pub = Namespace("http://www.example.edu/publication/organization/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()

def keywords():
    keywords_df = pd.read_csv('./data/keywords.csv')

    for index, row in keywords_df.iterrows():
        subject = URIRef(keyword_pub + row['keywords'].replace(" ","_"))
        predicate = RDF.type
        obj = URIRef('Keyword')
        
        keyword_literal = Literal(row['keywords'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, keyword_pub.keyword, keyword_literal))

    # Serialize the RDF graph to Turtle format and print
    print(g.serialize(format="turtle"))



def organizations():
    organization_df = pd.read_csv('./data/organizations.csv')

    for index, row in organization_df.iterrows():
        subject = URIRef(organization_pub + row['name'].replace(" ",""))
        predicate = RDF.type
        obj = URIRef('Organization')

        org_name_literal = Literal(row['name'], datatype = XSD.string)
        org_type_literal = Literal(row['type'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, keyword_pub.org_name, org_name_literal))
        g.add((subject, keyword_pub.org_type, org_type_literal))

    # Serialize the RDF graph to Turtle format and print
    print(g.serialize(format="turtle"))


if __name__ == "__main__":
    keywords()
    # organizations()