import requests
from bs4 import BeautifulSoup
from colorama import Fore

def extract_content_and_href(url):
    # Get the HTML content of the page
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # List to store the results
    results = []

    # Find all <td class="title"> tags
    td_tags = soup.find_all("td", class_="title")

    # Iterate over the <td class="title"> tags
    for td_tag in td_tags:
        # Find the <span class="titleline"> tag inside the <td class="title"> tag
        span_tag = td_tag.find("span", class_="titleline")
        if span_tag is not None:
            # Find the <a> tag inside the <span class="titleline"> tag
            a_tag = span_tag.find("a")
            if a_tag is not None:
                # Get the content of the <a> tag
                content = a_tag.text
                # Get the value of the "href" attribute of the <a> tag
                href = a_tag.get("href")
                # Add the results to the list
                results.append((content, href))

    return results

# HackerNews URL
url = "https://news.ycombinator.com/"

# Call the function and get the results
results = extract_content_and_href(url)

# Print the results
for content, href in results:
    print(Fore.GREEN + "Content:" + Fore.RED + content)
    print(Fore.GREEN + "Href:" + Fore.BLUE + href)
    print()
