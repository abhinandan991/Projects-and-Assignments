import os
import random
import re
import sys
import math

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    pgdict={}
    for y in corpus:
        pgdict[y]=0
    c=corpus[page]
    n=len(c)
    if n==0:
        for i in corpus:
            pgdict[i]=1/len(corpus)
            return pgdict
    for j in corpus[page]:
        pgdict[j]=(damping_factor/n)
    for x in corpus:
        pgdict[x]=pgdict[x]+((1-damping_factor)/len(corpus))
    return pgdict
        
    
        


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    dic={}
    sample=[] 
    f=random.choice(list(corpus))
    sample.append(f)
    for i in range(n):
        tm=transition_model(corpus,f,damping_factor)
        ap=list(tm.keys())
        al=list(tm.values())
        nf=random.choices(ap,weights=al,k=1)
        sample.append(nf[0])
        f=nf[0]
    for y in corpus:
        dic[y]=(sample.count(y))/n
    return dic

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank={}
    newrank={}
    N=len(corpus)
    for q in corpus:
        pagerank[q]=1/N
    repeat = True

    while repeat:
        for page in pagerank:
            total = float(0)
            for possible_page in corpus:               
                if page in corpus[possible_page]:
                    total += pagerank[possible_page] / len(corpus[possible_page])             
                if not corpus[possible_page]:
                    total += pagerank[possible_page] / len(corpus)
            newrank[page] = (1 - damping_factor) / len(corpus) + damping_factor * total
        repeat = False        
        for page in pagerank:
            if not math.isclose(newrank[page], pagerank[page], abs_tol=0.001):
                repeat = True
            pagerank[page] = newrank[page]

    return pagerank

    
        


if __name__ == "__main__":
    main()
