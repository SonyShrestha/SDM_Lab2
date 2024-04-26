import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace, RDF, XSD

# Define namespaces
pub = Namespace("http://www.example.edu/publication/")
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph
g = Graph()



def organizations():
    organization_df = pd.read_csv('./data/organizations.csv')

    for index, row in organization_df.iterrows():
        subject = URIRef(pub + 'organizations/'+str(row['id']))
        predicate = RDF.type
        obj = pub.Organization

        org_name_literal = Literal(row['name'], datatype = XSD.string)
        org_type_literal = Literal(row['type'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.org_name, org_name_literal))
        g.add((subject, pub.org_type, org_type_literal))

    return g



def authors():
    author_df = pd.read_csv('./data/authors.csv')

    for index, row in author_df.iterrows():
        subject = URIRef(pub + 'authors/'+str(row['authorId']))
        predicate = RDF.type
        obj = pub.Author

        author_name_literal = Literal(row['authorName'], datatype = XSD.string) 
        author_aff_org_literal = URIRef(pub + 'organization/'+str(row['affiliatedOrg']))
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.author_name, author_name_literal))
        g.add((subject, pub.affiliated_org, author_aff_org_literal))

    return g



def keywords():
    keywords_df = pd.read_csv('./data/keywords.csv')

    for index, row in keywords_df.iterrows():
        subject = URIRef(pub + 'keywords/'+row['keywords'].replace(" ","_"))
        predicate = RDF.type
        obj = pub.Keyword
        
        keyword_literal = Literal(row['keywords'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.keyword, keyword_literal))

    return g



def journals():
    journal_df = pd.read_csv('./data/journals.csv')

    for index, row in journal_df.iterrows():
        subject = URIRef(pub + 'journals/'+ str(row['id']))
        predicate = RDF.type
        obj = pub.Journal

        journal_name_literal = Literal(row['jcwName'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.journal_name, journal_name_literal))

    return g



def workshops():
    workshop_df = pd.read_csv('./data/workshops.csv')

    for index, row in workshop_df.iterrows():
        subject = URIRef(pub + 'workshops/' + str(row['id']))
        predicate = RDF.type
        obj = pub.Workshop

        workshop_name_literal = Literal(row['jcwName'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.workshop_name, workshop_name_literal))

    return g



def conferences():
    conference_df = pd.read_csv('./data/workshops.csv')

    for index, row in conference_df.iterrows():
        subject = URIRef(pub + 'workshops/' + str(row['id']))
        predicate = RDF.type
        obj = pub.Conference

        conference_name_literal = Literal(row['jcwName'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.conference_name, conference_name_literal))

    return g



def conference_paper():
    conference_paper_df = pd.read_csv('./data/conference_paper.csv')

    for index, row in conference_paper_df.iterrows():
        subject = URIRef(pub + 'conference_paper/'+row['paperId'])
        predicate = RDF.type
        obj = pub.Paper

        title_literal = Literal(row['title'], datatype = XSD.string)
        abstract_literal = Literal(row['abstract'], datatype = XSD.string)
        year_literal = Literal(row['year'], datatype = XSD.int)
        citation_count_literal = Literal(row['citationCount'], datatype = XSD.int)
        publication_date_literal = Literal(row['publicationDate'], datatype = XSD.date)
        edition_literal = Literal(row['edition'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.title, title_literal))
        g.add((subject, pub.abstract, abstract_literal))
        g.add((subject, pub.year, year_literal))
        g.add((subject, pub.citation_count, citation_count_literal))
        g.add((subject, pub.publication_date, publication_date_literal))
        
        g.add((subject, pub.corresponding_author, URIRef(pub + 'author/'+str(row['correspondingAuthorId']))))
        g.add((subject, pub.edition, edition_literal))

        g.add((subject, pub.published_in, URIRef(pub + 'conference/' + str(row['jcwName']))))

        for keyword in row["keywords"].split(","):
            g.add((subject, pub.keyword, URIRef(pub + 'keyword/'+str(keyword.strip().replace(" ","_")))))

        for author in row["authorId"].split(","):
            g.add((subject, pub.written_by, URIRef(pub + 'author/'+str(author))))
        
        for cited_paper_id in row["citedPaperId"].split(","):
            g.add((subject, pub.cites, URIRef(pub + 'paper/'+str(cited_paper_id))))
        
        for reviewer in row["reviewers"].split(","):
            g.add((subject, pub.reviwed_by, URIRef(pub + 'author/'+str(reviewer))))

    return g


def workshop_paper():
    workshop_paper_df = pd.read_csv('./data/workshop_paper.csv')

    for index, row in workshop_paper_df.iterrows():
        subject = URIRef(pub + 'workshop_paper/'+row['paperId'])
        predicate = RDF.type
        obj = pub.Paper

        title_literal = Literal(row['title'], datatype = XSD.string)
        abstract_literal = Literal(row['abstract'], datatype = XSD.string)
        year_literal = Literal(row['year'], datatype = XSD.int)
        citation_count_literal = Literal(row['citationCount'], datatype = XSD.int)
        publication_date_literal = Literal(row['publicationDate'], datatype = XSD.date)
        edition_literal = Literal(row['edition'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.title, title_literal))
        g.add((subject, pub.abstract, abstract_literal))
        g.add((subject, pub.year, year_literal))
        g.add((subject, pub.citation_count, citation_count_literal))
        g.add((subject, pub.publication_date, publication_date_literal))
        g.add((subject, pub.corresponding_author, URIRef(pub + 'author/'+str(row['correspondingAuthorId']))))
        g.add((subject, pub.edition, edition_literal))

        g.add((subject, pub.published_in, URIRef(pub + 'workshop/'+ str(row['jcwName']))))

        for keyword in row["keywords"].split(","):
            g.add((subject, pub.keyword, URIRef(pub + 'keyword/'+str(keyword.strip().replace(" ","_")))))

        for author in row["authorId"].split(","):
            g.add((subject, pub.written_by, URIRef(pub + 'author/'+str(author))))
        
        if pd.notna(row['citedPaperId']):
            for cited_paper_id in row["citedPaperId"].split(","):
                g.add((subject, pub.cites, URIRef(pub + 'paper/'+str(cited_paper_id))))
        
        for reviewer in row["reviewers"].split(","):
            g.add((subject, pub.reviwed_by, URIRef(pub + 'author/'+str(reviewer))))

    return g



def journal_paper():
    journal_paper_df = pd.read_csv('./data/journal_paper.csv')

    for index, row in journal_paper_df.iterrows():
        subject = URIRef(pub + 'journal_paper/'+row['paperId'])
        predicate = RDF.type
        obj = pub.Paper

        title_literal = Literal(row['title'], datatype = XSD.string)
        abstract_literal = Literal(row['abstract'], datatype = XSD.string)
        year_literal = Literal(row['year'], datatype = XSD.int)
        citation_count_literal = Literal(row['citationCount'], datatype = XSD.int)
        publication_date_literal = Literal(row['publicationDate'], datatype = XSD.date)
        journal_volume_literal = Literal(row['journalVolume'], datatype = XSD.string)
        
        # Add triples to the RDF graph
        g.add((subject, predicate, obj))
        g.add((subject, pub.title, title_literal))
        g.add((subject, pub.abstract, abstract_literal))
        g.add((subject, pub.year, year_literal))
        g.add((subject, pub.citation_count, citation_count_literal))
        g.add((subject, pub.publication_date, publication_date_literal))
        g.add((subject, pub.corresponding_author, URIRef(pub + 'author/'+str(row['correspondingAuthorId']))))
        g.add((subject, pub.journal_volume, journal_volume_literal))

        g.add((subject, pub.published_in, URIRef(pub + 'journal/' + str(row['jcwName']))))

        for keyword in row["keywords"].split(","):
            g.add((subject, pub.keyword, URIRef(pub + 'keyword/'+str(keyword.strip().replace(" ","_")))))

        for author in row["authorId"].split(","):
            g.add((subject, pub.written_by, URIRef(pub + 'author/'+str(author))))
        
        if pd.notna(row['citedPaperId']):
            for cited_paper_id in row["citedPaperId"].split(","):
                g.add((subject, pub.cites, URIRef(pub + 'paper/'+str(cited_paper_id))))
        
        for reviewer in row["reviewers"].split(","):
            g.add((subject, pub.reviwed_by, URIRef(pub + 'author/'+str(reviewer))))

    return g


if __name__ == "__main__":
    organization = organizations()
    author = authors()
    keyword = keywords()
    journal = journals()
    conference = conferences()
    workshop = workshops()
    workshop_paper = workshop_paper()
    journal_paper = journal_paper()
    conference_paper = conference_paper()
    kg = organization + author + keyword + journal + conference + workshop + workshop_paper + journal_paper + conference_paper
    kg.serialize(destination='./output/kg_abox.ttl', format='turtle')