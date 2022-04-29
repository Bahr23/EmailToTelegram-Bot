from bs4 import BeautifulSoup


def get_message_profile(html):
    soup = BeautifulSoup(html, 'lxml')
    response = {
        'main-link': {
            'text': soup.find(
                "a",
                {"style": "color:#4674ca;font-size:16px;font-weight:600;margin-right:10px;text-decoration:none"}
            ).text,
            'href': soup.find(
                "a",
                {"style": "color:#4674ca;font-size:16px;font-weight:600;margin-right:10px;text-decoration:none"}
            )['href']
        }
    }

    if soup.find_all('h3', string='Exception'):
        response['Exception'] = {
            soup.find( "pre", {"style": "background-color:#f4f5f6;border-radius:4px;color:#3d4649;font-family:'menlo' , 'monaco' , 'courier new' , monospace;font-size:14px;font-weight:normal;margin:0 0 15px 0;padding:15px;white-space:pre-wrap;word-wrap:break-word"}
            ).text.replace('<', '≪').replace('>', '≫') 
        }

    if soup.find(string='IP Address:'):
        response['User'] = {soup.find(string='IP Address:').find_next('td').text}

    if soup.find_all('h3', string='Request'):
        response['Request'] = {
            'URL': {
                'text': soup.find(string='URL').find_next(
                    "a",
                    {"style": "color:#4674ca;font-weight:500;text-decoration:none"}
                ).text,
                'href': soup.find(string='URL').find_next(
                    "a",
                    {"style": "color:#4674ca;font-weight:500;text-decoration:none"}
                )['href']
            },
        }
        query = soup.find(
                "code",
                {"style": "font-family:'menlo' , 'monaco' , 'courier new' , monospace;font-size:14px;font-weight:normal;word-break:break-word"}
            )
        if query:
            response['Request']['Query'] = query.text
    return response
