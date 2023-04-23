# Linkscraper

Clone this repository.

```shell
git clone https://github.com/thesilvaemily/linkscraper.git
```

To install dependencies.

```python
pip install -r requirements.txt
```

## Parameters

| Parameter                   | Description                        | Required                | Default                            |
| --------------------------- | ---------------------------------- | ----------------------- | ---------------------------------- |
| -u, --url                   | URL to scan                        | Yes                     |                                    |
| -a, --action                | Run an action                      | No                      | ``get-core``                       |
| -p, --plugin                | Load a plugin                      | No                      |                                    |
| -k, --key                   | Set the API key                    | Yes, if plugin is needs |                                    |
| -f, --file                  | Save output file                   | Yes, if plugin is needs |                                    |
| -b, --browser               | Set the browser to take screenshot | No                      | ``chrome``                         |
| -t, --title                 | Set title the screenshot on Imgur  | No                      | ``Screenshot made by Linkscraper`` |
| -up, --upload               | Upload the screenshot to Imgur    | No                      |                                    |
| -oel, --only-external-links | Show only external links           | No                      | `false`                          |
| -ssc, --show-status-code    | Show status code                   | No                      | `false`                          |
| -smf, --show-minify-files   | Show only minify files             | No                      | `false`                          |
| -filter, --filter           | Filter data                        | No                      |                                    |
| -d, --download              | Download static files              | No                      | `false`                          |
| -version, --version         | Show current version               | No                      |                                    |

## Functions

*Get core:*

```shell
python linkscraper -u https://example.com -a get-core
```

*Get headers:*

```shell
python linkscraper -u https://example.com -a get-headers
```

* *Get headers and filter header (new):*

  ```shell
  python linkscraper -u https://example.com -a get-headers -filter header
  ```

*Get cookies:*

```shell
python linkscraper -u https://example.com -a get-cookies
```

* *Get cookies and filter cookie (new):*

  ```shell
  python linkscraper -u https://example.com -a get-cookies -filter cookie
  ```

*Get js files:*

```shell
python linkscraper -u https://example.com -a get-js-files
```

* *Get js files and filter files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-js-files -filter example.js
  ```
* *Get js files and show only minify files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-js-files -smf true
  ```
* *Get js files and download files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-js-files -d true
  ```

*Get css files:*

```shell
python linkscraper -u https://example.com -a get-css-files
```

* *Get css files and filter files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-css-files -filter example.css
  ```
* *Get css files and show only minify files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-css-files -smf true
  ```
* *Get css files and download files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-css-files -d true
  ```

*Get images files:*

```shell
python linkscraper -u https://example.com -a get-images-files
```

* *Get images files and filter files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-images-files -filter example.png
  ```
* *Get images files and download files (new):*

  ```shell
  python linkscraper -u https://example.com -a get-images-files -d true
  ```

*Get links: (new)*

```shell
python linkscraper -u https://example.com -a get-links
```

* *Get links and filter url (new):*

  ```shell
  python linkscraper -u https://example.com -a get-links -filter domain.com
  ```
* *Get links and show only external links: (new)*

  ```shell
  python linkscraper -u https://example.com -a get-links -oel true
  ```
* *Get links and show status code (new):*

  ```shell
  python linkscraper -u https://example.com -a get-links -ssc true
  ```

*Get emails: (new)*

```shell
python linkscraper -u https://example.com -a get-emails
```

* *Get emails and filter email (new):*

  ```shell
  python linkscraper -u https://example.com -a get-css-files -filter example@domain.com
  ```

## Plugins

*wp-detect:*

```shell
python linkscraper -u https://example.com -a get-plugins -p wp-detect
```

*whois (new):*

```shell
python linkscraper -u https://example.com -a get-plugins -p whois
```

*page-details (new):*

```shell
linkscraper -u https://example.com -a get-plugins -p page-details
```

*robots (new):*

```shell
python linkscraper -u https://example.com -a get-plugins -p robots
```

*virustotal (new):*

```shell
python linkscraper -u https://example.com -a get-plugins -p virustotal -k YOUR_VIRUSTOTAL_KEY
```

* *virustotal and get key in ENV variable (new):*

  ```shell
  python linkscraper -u https://example.com -a get-plugins -p virustotal -k env:VIRUSTOTAL_KEY
  ```

*ip-location (new):*

```shell
python linkscraper -u https://example.com -a get-plugins -p ip-location
```

*screenshot (new):*

```shell
python linkscraper -u https://example.com -a get-plugins -p screenshot -f screenshot.png -b chrome
```

* *screenshot and upload to Imgur (new):*

  ```shell
  python linkscraper -u https://example.com -a get-plugins -p screenshot -f screenshot.png -b chrome -up imgur -k YOUR_IMGUR_CLIENT_ID -t "Title of post here"
  ```
* *screenshot and upload to Imgur and get key in ENV variable (new):*

  ```shell
  python linkscraper -u https://example.com -a get-plugins -p screenshot -f screenshot.png -b chrome -up imgur -k env:IMGUR_CLIENT_ID -t "Title of post here"
  ```

## Additional links

* [Get your free VirusTotal Key](https://www.virustotal.com/gui/my-apikey)
* [Get your free Imgur Client ID](https://api.imgur.com/oauth2/addclient)

## Changelog

> Current version: ``2.0.0``

Added

* Function ``get-links`` was added
* Function ``get-emails`` was added
* Function `download_css` wass added
* Function `download_js` wass added
* Function `download_images` wass added

Improvements

* Improvement in interface
* Improvement in plugin ``wp-detect``

Plugins removed

* Plugin ``mshots`` was removed and replacement by ``screenshot``
* Plugin ``page-title`` was removed and replacement by ``page-details``

Plugins added

* Plugin ``whois`` was added
* Plugin ``imgur`` was added
* Plugin ``robots`` was added
* Plugin ``virustotal`` was added
* Plugin ``screenshot`` was added
* Plugin ``ip-location`` was added
* Plugin ``page-details`` was added

## External API's use

* [Imgur](https://imgur.com)
* [VirusTotal](https://virustotal.com)
* [IP-API](https://ip-api.com/)
* [who.is](https://who.is/)

## Dependencies

* beautifulsoup4
* cloudscraper
* pyfiglet
* pyperclip
* requests
* selenium
* whois
* rich
* python-decouple

## License

Code licensed under [MIT License](https://github.com/kremilly/linkscraper/blob/main/LICENSE)
