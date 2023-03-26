# linkscraper

Link Scraper cli

**Parameters:**

| Parameter   | Dscription  | Required   |
|---|---|---|
| -u, --url   | URL to scan  | Yes  |
| -s, --section   | Display a section  | No  |
| -p, --plugin  | Load a plugin  | No  |

## Functions

*Get core data:* ``python linkscraper.py -u http://example.com -s get-core`` or ``linkscraper -u http://example.com -s get-core``

*Get headers data:* ``python linkscraper.py -u http://example.com -s get-headers`` or ``linkscraper -u http://example.com -s get-headers``

*Get cookies:* ``python linkscraper.py -u http://example.com -s get-cookies`` or ``linkscraper -u http://example.com -s get-cookies``

*Get js files:* ``python linkscraper.py -u http://example.com -s get-js-files`` or ``linkscraper -u http://example.com -s get-js-files``

*Get css files:* ``python linkscraper.py -u http://example.com -s get-css-files`` or ``linkscraper -u http://example.com -s get-css-files``

*Get images file:* ``python linkscraper.py -u http://example.com -s get-images-files`` or ``linkscraper -u http://example.com -s get-images-files``

*Check if WordPress runs:* ``python linkscraper.py -u http://example.com -s get-plugins -p wp-detect`` or ``linkscraper -u http://example.com -s get-plugins -p wp-detect``

*Get screenshot of url:* ``python linkscraper.py -u http://example.com -s get-plugins -p mshots`` or ``linkscraper -u http://example.com -s get-plugins -p mshots``

*Get page title:* ``python linkscraper.py -u http://example.com -s get-plugins -p page-title`` or ``linkscraper -u http://example.com -s get-plugins -p page-title``
