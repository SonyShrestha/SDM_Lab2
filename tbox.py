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
g.add((pub.reviewer, RDF.type, RDFS.Class))
g.add((pub.venue, RDF.type, RDFS.Class))
g.add((pub.publication, RDF.type, RDFS.Class))

g.add((pub.reviewer, RDFS.subClassOf, pub.person))
g.add((pub.author, RDFS.subClassOf, pub.person))
g.add((pub.conferenece, RDFS.subClassOf, pub.venue))
g.add((pub.workshop, RDFS.subClassOf, pub.venue))
g.add((pub.venue, RDFS.subClassOf, pub.publication))
g.add((pub.journal, RDFS.subClassOf, pub.publication))

g.add((pub.jr_volume, RDF.type, RDFS.Class))
g.add((pub.conf_edition, RDF.type, RDFS.Class))
g.add((pub.ws_edition, RDF.type, RDFS.Class))

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
g.add((pub.org_id, RDFS.range, XSD.integer))
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

g.add((pub.conf_edition_paper_rel, RDFS.domain, pub.conf_edition))
g.add((pub.conf_edition_paper_rel, RDFS.range, pub.paper))
g.add((pub.conf_edition_paper_rel, RDF.type, RDF.Property))

g.add((pub.conf_year, RDFS.domain, pub.conf_edition))
g.add((pub.conf_year, RDFS.range, XSD.integer))
g.add((pub.conf_year, RDF.type, RDF.Property))

g.add((pub.conf_edition_rel, RDFS.domain, pub.conf_edition))
g.add((pub.conf_edition_rel, RDFS.range, pub.conference))
g.add((pub.conf_edition_rel, RDF.type, RDF.Property))

g.add((pub.jr_vol_paper_rel, RDFS.domain, pub.jr_volume))
g.add((pub.jr_vol_paper_rel, RDFS.range, pub.paper))
g.add((pub.jr_vol_paper_rel, RDF.type, RDF.Property))

g.add((pub.jr_vol_rel, RDFS.domain, pub.jr_volume))
g.add((pub.jr_vol_rel, RDFS.range, pub.journal))
g.add((pub.jr_vol_rel, RDF.type, RDF.Property))

g.add((pub.jr_year, RDFS.domain, pub.jr_volume))
g.add((pub.jr_year, RDFS.range, XSD.integer))
g.add((pub.jr_year, RDF.type, RDF.Property))

g.add((pub.ws_edition_paper_rel, RDFS.domain, pub.ws_edition))
g.add((pub.ws_edition_paper_rel, RDFS.range, pub.paper))
g.add((pub.ws_edition_paper_rel, RDF.type, RDF.Property))

g.add((pub.ws_year, RDFS.domain, pub.ws_edition))
g.add((pub.ws_year, RDFS.range, XSD.integer))
g.add((pub.ws_year, RDF.type, RDF.Property))

g.add((pub.ws_edition_rel, RDFS.domain, pub.ws_edition))
g.add((pub.ws_edition_rel, RDFS.range, pub.workshop))
g.add((pub.ws_edition_rel, RDF.type, RDF.Property))

g.add((pub.paper_reviewer_rel, RDFS.domain, pub.paper_review))
g.add((pub.paper_reviewer_rel, RDFS.range, pub.paper))
g.add((pub.paper_reviewer_rel, RDF.type, RDF.Property))

g.add((pub.review_content, RDFS.domain, pub.paper_review))
g.add((pub.review_content, RDFS.range, XSD.string))
g.add((pub.review_content, RDF.type, RDF.Property))

g.add((pub.suggested_decision, RDFS.domain, pub.paper_review))
g.add((pub.suggested_decision, RDFS.range, XSD.string))
g.add((pub.suggested_decision, RDF.type, RDF.Property))

g.add((pub.reviewed_by, RDFS.domain, pub.paper_review))
g.add((pub.reviewed_by, RDFS.range, pub.reviewer))
g.add((pub.reviewed_by, RDF.type, RDF.Property))

g.add((pub.reviewer_name, RDFS.domain, pub.reviewer))
g.add((pub.reviewer_name, RDFS.range, xsd.string))
g.add((pub.reviewer_name, RDF.type, RDF.Property))

g.add((pub.corresponding_author, RDFS.subPropertyOf, pub.written_by))

g.add((pub.conf_year, RDFS.subPropertyOf, pub.pub_year))
g.add((pub.jr_year, RDFS.subPropertyOf, pub.pub_year))
g.add((pub.ws_year, RDFS.subPropertyOf, pub.pub_year))

g.add((pub.conf_edition, RDFS.subPropertyOf, pub.pub_edition))
g.add((pub.ws_edition, RDFS.subPropertyOf, pub.pub_edition))

g.add((pub.conf_edition_paper_rel, RDFS.subPropertyOf, pub.pub_edition))
g.add((pub.ws_edition_paper_rel, RDFS.subPropertyOf, pub.pub_edition))

g.add((pub.jr_edition_paper_rel, RDFS.subPropertyOf, pub.prop_publication))
g.add((pub.pub_edition, RDFS.subPropertyOf, pub.prop_publication))

# Serialize the graph to RDF/XML format
g.serialize(destination='./output/kg_tbox.ttl', format='turtle')
