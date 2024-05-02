from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS, XSD

# Define namespaces
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
pub = Namespace("http://www.example.edu/publication/")

# Create an empty graph
g = Graph()

# Add triples to the graph
g.add((pub.keyword, RDF.type, RDFS.Class))
g.add((pub.paper, RDF.type, RDFS.Class))
g.add((pub.author, RDF.type, RDFS.Class))
g.add((pub.conference, RDF.type, RDFS.Class))
g.add((pub.workshop, RDF.type, RDFS.Class))
g.add((pub.journal, RDF.type, RDFS.Class))
g.add((pub.organization, RDF.type, RDFS.Class))
g.add((pub.person, RDF.type, RDFS.Class))
g.add((pub.author, RDFS.subClassOf, pub.person))

g.add((pub.paper_review, RDF.type, RDFS.Class))
g.add((pub.paper_writer, RDF.type, RDFS.Class))
g.add((pub.conf_publication, RDF.type, RDFS.Class))
g.add((pub.workshop_publication, RDF.type, RDFS.Class))
g.add((pub.journal_publication, RDF.type, RDFS.Class))

g.add((pub.cites, RDF.type, RDF.Property))
g.add((pub.cites, RDFS.domain, pub.paper))
g.add((pub.cites, RDFS.range, pub.paper))

g.add((pub.contains, RDF.type, RDF.Property))
g.add((pub.contains, RDFS.domain, pub.paper))
g.add((pub.contains, RDFS.range, pub.keyword))

g.add((pub.affiliation, RDF.type, RDF.Property))
g.add((pub.affiliation, RDFS.domain, pub.author))
g.add((pub.affiliation, RDFS.range, pub.organization))

g.add((pub.corresponding_author, RDF.type, RDF.Property))
g.add((pub.corresponding_author, RDFS.domain, pub.paper))
g.add((pub.corresponding_author, RDFS.range, pub.author))

g.add((pub.written_by, RDF.type, RDF.Property))
g.add((pub.written_by, RDFS.domain, pub.paper))
g.add((pub.written_by, RDFS.range, pub.author))

g.add((pub.keyword_name, RDFS.domain, pub.keyword))
g.add((pub.keyword_name, RDFS.range, XSD.string))
g.add((pub.keyword_name, RDF.type, RDF.Property))

g.add((pub.paper_id, RDFS.domain, pub.paper))
g.add((pub.paper_id, RDFS.range, XSD.string))
g.add((pub.paper_id, RDF.type, RDF.Property))

g.add((pub.title, RDFS.domain, pub.paper))
g.add((pub.title, RDFS.range, XSD.string))
g.add((pub.title, RDF.type, RDF.Property))

g.add((pub.abstract, RDFS.domain, pub.paper))
g.add((pub.abstract, RDFS.range, XSD.string))
g.add((pub.abstract, RDF.type, RDF.Property))

g.add((pub.citation_count, RDFS.domain, pub.paper))
g.add((pub.citation_count, RDFS.range, XSD.integer))
g.add((pub.citation_count, RDF.type, RDF.Property))

g.add((pub.publication_date, RDFS.domain, pub.paper))
g.add((pub.publication_date, RDFS.range, XSD.date))
g.add((pub.publication_date, RDF.type, RDF.Property))

g.add((pub.author_id, RDFS.domain, pub.author))
g.add((pub.author_id, RDFS.range, XSD.string))
g.add((pub.author_id, RDF.type, RDF.Property))

g.add((pub.author_name, RDFS.domain, pub.author))
g.add((pub.author_name, RDFS.range, XSD.string))
g.add((pub.author_name, RDF.type, RDF.Property))

g.add((pub.org_id, RDFS.domain, pub.organization))
g.add((pub.org_id, RDFS.range, XSD.int))
g.add((pub.org_id, RDF.type, RDF.Property))

g.add((pub.org_name, RDFS.domain, pub.organization))
g.add((pub.org_name, RDFS.range, XSD.string))
g.add((pub.org_name, RDF.type, RDF.Property))

g.add((pub.org_type, RDFS.domain, pub.organization))
g.add((pub.org_type, RDFS.range, XSD.string))
g.add((pub.org_type, RDF.type, RDF.Property))

g.add((pub.conf_id, RDFS.domain, pub.conference))
g.add((pub.conf_id, RDFS.range, XSD.integer))
g.add((pub.conf_id, RDF.type, RDF.Property))

g.add((pub.conf_name, RDFS.domain, pub.conference))
g.add((pub.conf_name, RDFS.range, XSD.string))
g.add((pub.conf_name, RDF.type, RDF.Property))

g.add((pub.journal_id, RDFS.domain, pub.journal))
g.add((pub.journal_id, RDFS.range, XSD.integer))
g.add((pub.journal_id, RDF.type, RDF.Property))

g.add((pub.journal_name, RDFS.domain, pub.journal))
g.add((pub.journal_name, RDFS.range, XSD.string))
g.add((pub.journal_name, RDF.type, RDF.Property))

g.add((pub.workshop_id, RDFS.domain, pub.workshop))
g.add((pub.workshop_id, RDFS.range, XSD.integer))
g.add((pub.workshop_id, RDF.type, RDF.Property))

g.add((pub.workshop_name, RDFS.domain, pub.workshop))
g.add((pub.workshop_name, RDFS.range, XSD.string))
g.add((pub.workshop_name, RDF.type, RDF.Property))

g.add((pub.paper_reviewed, RDFS.domain, pub.paper_review))
g.add((pub.paper_reviewed, RDFS.range, pub.paper))
g.add((pub.paper_reviewed, RDF.type, RDF.Property))

g.add((pub.reviwer, RDFS.domain, pub.paper_review))
g.add((pub.reviwer, RDFS.range, pub.author))
g.add((pub.reviwer, RDF.type, RDF.Property))

g.add((pub.review_count, RDFS.domain, pub.paper_review))
g.add((pub.review_count, RDFS.range, XSD.string))
g.add((pub.review_count, RDF.type, RDF.Property))

g.add((pub.suggested_decision, RDFS.domain, pub.paper_review))
g.add((pub.suggested_decision, RDFS.range, XSD.string))
g.add((pub.suggested_decision, RDF.type, RDF.Property))

g.add((pub.conf_pub_conference, RDFS.domain, pub.conf_publication))
g.add((pub.conf_pub_conference, RDFS.range, pub.conference))
g.add((pub.conf_pub_conference, RDF.type, RDF.Property))

g.add((pub.conf_pub_paper, RDFS.domain, pub.conf_publication))
g.add((pub.conf_pub_paper, RDFS.range, pub.paper))
g.add((pub.conf_pub_paper, RDF.type, RDF.Property))

g.add((pub.conf_pub_year, RDFS.domain, pub.conf_publication))
g.add((pub.conf_pub_year, RDFS.range, XSD.integer))
g.add((pub.conf_pub_year, RDF.type, RDF.Property))

g.add((pub.conf_pub_edition, RDFS.domain, pub.conf_publication))
g.add((pub.conf_pub_edition, RDFS.range, XSD.integer))
g.add((pub.conf_pub_edition, RDF.type, RDF.Property))

g.add((pub.ws_pub_workshop, RDFS.domain, pub.workshop_publication))
g.add((pub.ws_pub_workshop, RDFS.range, pub.workshop))
g.add((pub.ws_pub_workshop, RDF.type, RDF.Property))

g.add((pub.ws_pub_paper, RDFS.domain, pub.workshop_publication))
g.add((pub.ws_pub_paper, RDFS.range, pub.paper))
g.add((pub.ws_pub_paper, RDF.type, RDF.Property))

g.add((pub.ws_pub_year, RDFS.domain, pub.workshop_publication))
g.add((pub.ws_pub_year, RDFS.range, XSD.integer))
g.add((pub.ws_pub_year, RDF.type, RDF.Property))

g.add((pub.ws_pub_edition, RDFS.domain, pub.workshop_publication))
g.add((pub.ws_pub_edition, RDFS.range, XSD.integer))
g.add((pub.ws_pub_edition, RDF.type, RDF.Property))

g.add((pub.jr_pub_journal, RDFS.domain, pub.journal_publication))
g.add((pub.jr_pub_journal, RDFS.range, pub.journal))
g.add((pub.jr_pub_journal, RDF.type, RDF.Property))

g.add((pub.jr_pub_paper, RDFS.domain, pub.journal_publication))
g.add((pub.jr_pub_paper, RDFS.range, pub.paper))
g.add((pub.jr_pub_paper, RDF.type, RDF.Property))

g.add((pub.jr_pub_year, RDFS.domain, pub.journal_publication))
g.add((pub.jr_pub_year, RDFS.range, XSD.integer))
g.add((pub.jr_pub_year, RDF.type, RDF.Property))

g.add((pub.jr_pub_volume, RDFS.domain, pub.journal_publication))
g.add((pub.jr_pub_volume, RDFS.range, XSD.integer))
g.add((pub.jr_pub_volume, RDF.type, RDF.Property))

# Serialize the graph to RDF/XML format
g.serialize(destination='./output/kg_tbox.rdf', format='xml')
