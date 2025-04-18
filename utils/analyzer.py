import requests
from bs4 import BeautifulSoup

def analyze_site(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        metas = soup.find_all('meta')
        viewport = any('viewport' in (meta.get('name') or '') for meta in metas)

        responsive = viewport
        issues = []
        if not viewport:
            issues.append("There is no viewport meta-tag — The website may not display correctly on mobile devices.")

        # Додатковий аналіз CSS-класів (наприклад, використання Bootstrap або media queries)
        used_bootstrap = any('bootstrap' in link.get('href', '') for link in soup.find_all('link'))
        if not used_bootstrap:
            issues.append("There is no Bootstrap — Responsive grid may be missing")

        score = 100
        if not viewport: score -= 30
        if not used_bootstrap: score -= 20

        return {
            'responsive': responsive,
            'score': max(score, 0),
            'issues': issues,
            'tips': [
                "Use viewport meta-tag for better adaptivity.",
                "Use CSS media queries or frameworks like a Bootstrap."
            ]
        }
    except Exception as e:
        return {
            'responsive': False,
            'score': 0,
            'issues': [f"Error uploading site: {e}"],
            'tips': []
        }
