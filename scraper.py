import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(URL: str)-> int:
    """
    this function count the citations_needed in this URL 
    takes in a url string and returns an integer.
    input : str
    output : integer
    """

    #requeste the data from the website
    page =requests.get(URL)
    
    #parser the data
    soup =BeautifulSoup(page.content,"html.parser")
    all=soup.find_all("sup",class_="noprint Inline-Template Template-Fact")
    citation_list=[]
    for i in all:
        citation_list.append(i.find("span").text.strip())
    return len(citation_list)


def get_citations_needed_report(URL: str)-> str:
    """
    This function returns every paragraphs have citations_needed in input URL 
    takes in a url string and returns a report string,the string should be formatted with each citation listed in the order found.
    input : str
    output : str
    """

    #requeste the data from the website
    page =requests.get(URL)
    
    #parser the data
    soup =BeautifulSoup(page.content,"html.parser")
    all=soup.find_all("p")
    parg_list=""
    for i in all:
        p=(i.find("sup",class_="noprint Inline-Template Template-Fact"))
        if p is not None:
            parg_list+=i.text.strip()
            parg_list+="\n"
    return parg_list




if __name__ =="__main__":
    URL="https://en.wikipedia.org/wiki/History_of_Mexico"
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))