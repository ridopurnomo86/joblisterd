from bs4 import BeautifulSoup
import requests


def main(link):
    data = []
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find('div', {'class': "sx2jih0 zcydq8bm"}
                     ).find('div', {'class': "sx2jih0", "data-automation": "jobListing"})
    jobs_articles = jobs.find_all('article', {
        "class": "sx2jih0 sx2jih1 zcydq85u zcydq8h c6ROG_0 _18qlyvc14 _18qlyvc17 zcydq832 zcydq835"})

    for index, job in enumerate(jobs_articles):
        job_icon_image = job.find('img', {"class": "sx2jih0 pXyoU_0"})
        job_full_image = job.find(
            'img', {'class': "sx2jih0 zcydq84u zcydq84v zcydq84s rE8hQ_0", "data-automation": "job-card-banner"})
        job_name = job.find(
            "h1", {"class": "sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvca"}).text
        job_location = job.find(
            "span", {'class': "sx2jih0 zcydq84u zcydq80 iwjz4h0"}).text
        job_company = job.find(
            "span", {"class": "sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc1 _18qlyvca"})
        job_specialist = job.findAll(
            "dd", {"class": "sx2jih0 zcydq84y"})[1].text
        job_type = job.findAll("dd", {"class": "sx2jih0 zcydq84y"})[2].text
        salary = job.findAll("span", {
            "class": "sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc3 _18qlyvc7"})
        last_update = job.find("time", {"class": "sx2jih0 zcydq84u"})[
            "datetime"]

        data.append({
            "id": f"{index + 1}",
            "icon_image": f"{job_icon_image['src'] if job_icon_image is not None else '-'}",
            "full_image": f"{job_full_image['src'] if job_full_image is not None else '-'}",
            "salary": f"{salary[1].text if len(salary) > 1 else '-'}",
            "name": f'{job_name}',
            "specialist_type": f'{job_specialist}',
            "type": f'{job_type}',
            "company_name": f"{job_company.text if job_company != None else '-'}",
            "location": f'{job_location}',
            "last_update": f'{last_update}'
        })

    return data
