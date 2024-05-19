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
        subject = URIRef(pub + 'organization/'+str(row['id']))

        org_name_literal = Literal(row['name'], datatype = XSD.string)
        org_type_literal = Literal(row['type'], datatype = XSD.string)
        
        g.add((subject, pub.org_name, org_name_literal))
        g.add((subject, pub.org_type, org_type_literal))

    return g



def authors():
    author_df = pd.read_csv('./data/authors.csv')

    for index, row in author_df.iterrows():
        subject = URIRef(pub + 'author/'+str(row['authorId']))

        author_name_literal = Literal(row['authorName'], datatype = XSD.string) 
        author_aff_org_literal = URIRef(pub + 'organization/'+str(row['affiliatedOrg']))
        
        g.add((subject, pub.author_name, author_name_literal))
        g.add((subject, pub.affiliation, author_aff_org_literal))

    return g


def reviewers():
    conf_reviewers_df = pd.read_csv('./data/conference_paper.csv')
    conf_reviewers_df = conf_reviewers_df[["reviewers"]]
    workshop_reviewers_df = pd.read_csv('./data/workshop_paper.csv')
    workshop_reviewers_df = workshop_reviewers_df[["reviewers"]]
    journal_reviewers_df = pd.read_csv('./data/journal_paper.csv')
    journal_reviewers_df = journal_reviewers_df[["reviewers"]]
    reviewers = pd.concat([conf_reviewers_df, workshop_reviewers_df, journal_reviewers_df])
    reviewers['authorId'] = reviewers['reviewers'].str.split(',')
    reviewers = reviewers.explode('authorId')
    reviewers = reviewers[["authorId"]]
    reviewers.drop_duplicates(inplace=True)

    author_df = pd.read_csv('./data/authors.csv')
    author_df['authorId'] = author_df['authorId'].astype(str)

    reviewer_df = pd.merge(author_df, reviewers, on='authorId', how='inner')

    for index, row in reviewer_df.iterrows():
        subject = URIRef(pub + 'reviewer/'+str(row['authorId']))

        reviewer_name_literal = Literal(row['authorName'], datatype = XSD.string) 

        g.add((subject, pub.reviewer_name, reviewer_name_literal))

    return g



def keywords():
    keywords_df = pd.read_csv('./data/keywords.csv')

    for index, row in keywords_df.iterrows():
        subject = URIRef(pub + 'keyword/'+row['keywords'].replace(" ","_").lower())
        
        keyword_literal = Literal(row['keywords'], datatype = XSD.string)
        
        g.add((subject, pub.keyword_name, keyword_literal))

    return g



def journals():
    journal_df = pd.read_csv('./data/journals.csv')

    for index, row in journal_df.iterrows():
        subject = URIRef(pub + 'journal/'+ str(row['id']))

        journal_name_literal = Literal(row['jcwName'], datatype = XSD.string) 

        g.add((subject, pub.journal_name, journal_name_literal))

    return g



def workshops():
    workshop_df = pd.read_csv('./data/workshops.csv')

    for index, row in workshop_df.iterrows():
        subject = URIRef(pub + 'workshop/' + str(row['id']))

        workshop_name_literal = Literal(row['jcwName'], datatype = XSD.string)
        
        g.add((subject, pub.workshop_name, workshop_name_literal))

    return g



def conferences():
    conference_df = pd.read_csv('./data/conferences.csv')

    for index, row in conference_df.iterrows():
        subject = URIRef(pub + 'conference/' + str(row['id']))

        conference_name_literal = Literal(row['jcwName'], datatype = XSD.string)
        
        g.add((subject, pub.conf_name, conference_name_literal))

    return g



def conference_paper():
    conference_paper_df = pd.read_csv('./data/conference_paper.csv')

    for index, row in conference_paper_df.iterrows():
        subject = URIRef(pub + 'paper/'+row['paperId'])

        title_literal = Literal(row['title'], datatype = XSD.string)
        abstract_literal = Literal(row['abstract'], datatype = XSD.string)
        citation_count_literal = Literal(row['citationCount'], datatype = XSD.int)
        publication_date_literal = Literal(row['publicationDate'], datatype = XSD.date)
        
        g.add((subject, pub.title, title_literal))
        g.add((subject, pub.abstract, abstract_literal))
        g.add((subject, pub.citation_count, citation_count_literal))
        g.add((subject, pub.publication_date, publication_date_literal))
        
        g.add((subject, pub.corresponding_author, URIRef(pub + 'author/'+str(row['correspondingAuthorId']))))

        for keyword in row["keywords"].split(","):
            g.add((subject, pub.contains, URIRef(pub + 'keyword/'+str(keyword.strip().replace(" ","_").lower()))))

        for author in row["authorId"].split(","):
            g.add((subject, pub.written_by, URIRef(pub + 'author/'+str(author))))
        
        for cited_paper_id in row["citedPaperId"].split(","):
            g.add((subject, pub.cites, URIRef(pub + 'paper/'+str(cited_paper_id))))

    return g



def conference_publication():
    conference_paper_df = pd.read_csv('./data/conference_paper.csv')

    for index, row in conference_paper_df.iterrows():
        paper = URIRef(pub + 'paper/'+str(row['paperId']))
        year_literal = Literal(row['year'], datatype = XSD.int)
        conference = URIRef(pub + 'conference/'+str(row['jcwName']))        

        subject = URIRef(pub + 'paper='+str(row['paperId'])+'/edition='+str(row['jcwName']))
        g.add((subject, pub.conf_year, year_literal))
        g.add((subject, pub.conf_edition_rel, conference))
        g.add((subject, pub.conf_edition_paper_rel, paper))
    
    for index1, row1 in conference_paper_df.iterrows():
        paper_id1 = row1['paperId']

        for author1 in row1["authorId"].split(","):
            subject1 = URIRef(pub + 'paper/'+paper_id1)
            # g.add((subject1, RDF.type, pub.paper))
            g.add((subject1, pub.written_by, URIRef(pub + 'author/'+str(author1))))

    for index1, row1 in conference_paper_df.iterrows():
        paper_id2 = row1['paperId']

        for idx,reviewer in enumerate(row1["reviewers"].split(",")):
            review_content = row1['reviews'].split(",")[idx]
            suggested_decision = row1['review_decision'].split(",")[idx]
            subject2 = URIRef(pub + 'paper='+paper_id2+'/reviewer='+reviewer)

            g.add((subject2, pub.paper_reviewer_rel, URIRef(pub + 'paper/'+str(paper_id2))))
            g.add((subject2, pub.reviewed_by, URIRef(pub + 'reviewer/'+str(reviewer))))
            g.add((subject2, pub.review_content, Literal(review_content, datatype = XSD.string)))
            g.add((subject2, pub.suggested_decision, Literal(suggested_decision, datatype = XSD.string)))

    return g


def workshop_paper():
    workshop_paper_df = pd.read_csv('./data/workshop_paper.csv')

    for index, row in workshop_paper_df.iterrows():
        subject = URIRef(pub + 'paper/'+row['paperId'])

        title_literal = Literal(row['title'], datatype = XSD.string)
        abstract_literal = Literal(row['abstract'], datatype = XSD.string)
        citation_count_literal = Literal(row['citationCount'], datatype = XSD.int)
        publication_date_literal = Literal(row['publicationDate'], datatype = XSD.date)
        
        g.add((subject, pub.title, title_literal))
        g.add((subject, pub.abstract, abstract_literal))
        g.add((subject, pub.citation_count, citation_count_literal))
        g.add((subject, pub.publication_date, publication_date_literal))
        g.add((subject, pub.corresponding_author, URIRef(pub + 'author/'+str(row['correspondingAuthorId']))))

        for keyword in row["keywords"].split(","):
            g.add((subject, pub.contains, URIRef(pub + 'keyword/'+str(keyword.strip().replace(" ","_").lower()))))

        for author in row["authorId"].split(","):
            g.add((subject, pub.written_by, URIRef(pub + 'author/'+str(author))))
        
        if pd.notna(row['citedPaperId']):
            for cited_paper_id in row["citedPaperId"].split(","):
                g.add((subject, pub.cites, URIRef(pub + 'paper/'+str(cited_paper_id))))

    return g


def workshop_publication():
    workshop_paper_df = pd.read_csv('./data/workshop_paper.csv')

    for index, row in workshop_paper_df.iterrows():
        paper = URIRef(pub + 'paper/'+str(row['paperId']))
        year_literal = Literal(row['year'], datatype = XSD.int)
        workshop = URIRef(pub + 'workshop/'+str(row['jcwName']))  

        subject = URIRef(pub + 'paper='+str(row['paperId'])+'/edition='+str(row['jcwName']))
        g.add((subject, pub.ws_year, year_literal))
        g.add((subject, pub.ws_edition_rel, workshop))
        g.add((subject, pub.ws_edition_paper_rel, paper))
    
    for index1, row1 in workshop_paper_df.iterrows():
        paper_id1 = row1['paperId']

        for author1 in row1["authorId"].split(","):
            subject1 = URIRef(pub + 'paper/'+paper_id1)
            g.add((subject1, pub.written_by, URIRef(pub + 'author/'+str(author1))))
    
    for index1, row1 in workshop_paper_df.iterrows():
        paper_id2 = row1['paperId']

        for idx,reviewer in enumerate(row1["reviewers"].split(",")):
            review_content = row1['reviews'].split(",")[idx]
            suggested_decision = row1['review_decision'].split(",")[idx]
            subject2 = URIRef(pub + 'paper='+paper_id2+'/reviewer='+reviewer)
            
            g.add((subject2, pub.paper_reviewer_rel, URIRef(pub + 'paper/'+str(paper_id2))))
            g.add((subject2, pub.reviewed_by, URIRef(pub + 'reviewer/'+str(reviewer))))
            g.add((subject2, pub.review_content, Literal(review_content, datatype = XSD.string)))
            g.add((subject2, pub.suggested_decision, Literal(suggested_decision, datatype = XSD.string)))

    return g


def journal_paper():
    journal_paper_df = pd.read_csv('./data/journal_paper.csv')

    for index, row in journal_paper_df.iterrows():
        subject = URIRef(pub + 'paper/'+row['paperId'])

        title_literal = Literal(row['title'], datatype = XSD.string)
        abstract_literal = Literal(row['abstract'], datatype = XSD.string)
        citation_count_literal = Literal(row['citationCount'], datatype = XSD.int)
        publication_date_literal = Literal(row['publicationDate'], datatype = XSD.date)
        
        g.add((subject, pub.title, title_literal))
        g.add((subject, pub.abstract, abstract_literal))
        g.add((subject, pub.citation_count, citation_count_literal))
        g.add((subject, pub.publication_date, publication_date_literal))
        g.add((subject, pub.corresponding_author, URIRef(pub + 'author/'+str(row['correspondingAuthorId']))))

        for keyword in row["keywords"].split(","):
            g.add((subject, pub.conatins, URIRef(pub + 'keyword/'+str(keyword.strip().replace(" ","_").lower()))))

        for author in row["authorId"].split(","):
            g.add((subject, pub.written_by, URIRef(pub + 'author/'+str(author))))
        
        if pd.notna(row['citedPaperId']):
            for cited_paper_id in row["citedPaperId"].split(","):
                g.add((subject, pub.cites, URIRef(pub + 'paper/'+str(cited_paper_id))))

    return g

def journal_publication():
    journal_paper_df = pd.read_csv('./data/journal_paper.csv')

    for index, row in journal_paper_df.iterrows():
        paper = URIRef(pub + 'paper/'+str(row['paperId']))
        year_literal = Literal(row['year'], datatype = XSD.int)
        workshop = URIRef(pub + 'journal/'+str(row['jcwName']))  

        subject = URIRef(pub + 'paper='+str(row['paperId'])+'/volume='+str(row['jcwName']))
        g.add((subject, pub.jr_year, year_literal))
        g.add((subject, pub.jr_edition_rel, workshop))
        g.add((subject, pub.jr_edition_paper_rel, paper))
    
    for index1, row1 in journal_paper_df.iterrows():
        paper_id1 = row1['paperId']

        for author1 in row1["authorId"].split(","):
            subject1 = URIRef(pub + 'paper/'+paper_id1)

            g.add((subject1, pub.written_by, URIRef(pub + 'author/'+str(author1))))
    
    for index1, row1 in journal_paper_df.iterrows():
        paper_id2 = row1['paperId']

        for idx,reviewer in enumerate(row1["reviewers"].split(",")):
            review_content = row1['reviews'].split(",")[idx]
            suggested_decision = row1['review_decision'].split(",")[idx]
            subject2 = URIRef(pub + 'paper='+paper_id2+'/reviewer='+reviewer)
            
            g.add((subject2, pub.paper_reviewer_rel, URIRef(pub + 'paper/'+str(paper_id2))))
            g.add((subject2, pub.reviewed_by, URIRef(pub + 'reviewer/'+str(reviewer))))
            g.add((subject2, pub.review_content, Literal(review_content, datatype = XSD.string)))
            g.add((subject2, pub.suggested_decision, Literal(suggested_decision, datatype = XSD.string)))

    return g


if __name__ == "__main__":
    reviewer = reviewers()
    organization = organizations()
    author = authors()
    keyword = keywords()
    journal = journals()
    conference = conferences()
    workshop = workshops()
    workshop_paper = workshop_paper()
    journal_paper = journal_paper()
    conference_paper = conference_paper()
    workshop_publication = workshop_publication()
    journal_publication = journal_publication()
    conference_publication = conference_publication()
    kg = reviewer + organization + author + keyword + journal + conference + workshop + workshop_paper + journal_paper + conference_paper + workshop_publication + journal_publication + conference_publication
    kg.serialize(destination='./output/12A-B2-ShresthaPaudel.ttl', format='turtle')
    
