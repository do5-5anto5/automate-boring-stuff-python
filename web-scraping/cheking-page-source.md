# Checking if a page needs BeautifulSoup or Playwright

## Method: curl in terminal

View full page source:
```bash
curl -s https://example.com
```

Search for specific content directly:
```bash
curl -s https://example.com | grep "content you want"
```

## How to interpret

- **Content found in output** → static HTML → BeautifulSoup is enough
- **Content not found / output is mostly `<script>` tags** → JS-rendered → use Playwright