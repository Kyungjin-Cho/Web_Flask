import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()


def extract_remoteok_jobs(keyword):
  url = f'https://remoteok.com/remote-{keyword}+rust-jobs'

  remoteok_result = scraper.get(url)
  remoteok_soup = BeautifulSoup(remoteok_result.text, "html.parser")
  job_box = remoteok_soup.find_all("tr", {"class": "job"})
  results = []

  for data in job_box:
    title = data.find("h2", {"itemprop": "title"}).string.strip()
    job_info = data.find("div", {"class": "location"}).string
    company = data['data-company'].strip()
    link = data['data-url']

    job_data = {
      'link': f"https://remoteok.io{link}",
      'company': company.replace(",", " "),
      'location': job_info.replace(",", " "),
      'position': title.replace(",", " "),
      'from': 'Remoteok'
    }
    results.append(job_data)
  return results