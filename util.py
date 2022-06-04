BOARD_MAP = {'advisory council of medical physicist': '60',
             'board of acupuncture': '38',
             'board of athletic training': '10',
             'board of chiropractic medicine': '5',
             'board of clinical laboratory personnel': '66',
             'board of csw/mft/mhc': '52',
             'board of dentistry': '7',
             'board of hearing aid specialists': '36',
             'board of massage therapy': '14',
             'board of medicine': '15',
             'board of naturopathic medicine': '16',
             'board of nursing': '17',
             'board of occupational therapy practice': '56',
             'board of opticianry': '20',
             'board of optometry': '18',
             'board of orthotists and prosthetists': '31',
             'board of osteopathic medicine': '19',
             'board of pharmacy': '22',
             'board of physical therapy practice': '55',
             'board of podiatric medicine': '21',
             'board of psychology': '27',
             'board of respiratory care': '57',
             'bureau of emergency medical services': '25',
             'certified social workers': '54',
             'council of licensed midwifery': '32',
             'dietetics and nutrition practice council': '61',
             'electrolysis council': '65',
             'emt/ paramedic/ rad tech/ med phys certification unit': '76',
             'genetic counseling': '53',
             'nursing home administrators': '8',
             'public safety telecommunications': '24',
             'school psychology': '41',
             'speech-language pathology and audiology': '30',
             'out-of-state telehealth providers': '96'}

def get_dl(soup):
    keys, values = [], []
    for dl in soup.findAll("dl", {"class": "dl-horizontal"}):
        for dt in dl.findAll("dt"):
            keys.append(dt.text.strip())
        for dd in dl.findAll("dd"):
            values.append(dd.text.strip())
    return dict(zip(keys, values))


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://mqa-internet.doh.state.fl.us',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://mqa-internet.doh.state.fl.us/MQASearchServices/HealthCareProviders',
    'Accept-Language': 'en-US,en;q=0.9'}