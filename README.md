# 🎵 lets-dance

Create custom music playlists using the YouTube API and download them effortlessly using [`pytube`](https://github.com/pytube/pytube).

---

## 📦 Features

- ✅ Search and collect songs for any list of artists.
- ✅ Automatically generates a `musica.csv` with song titles and URLs.
- ✅ Downloads audio tracks to a local `/musica` directory (created if it doesn't exist).
- ✅ Select the maximum number of songs per artist.
- ✅ Optionally includes similar/recommended songs in the results.

---

## ⚙️ Requirements

- Python 3.8+
- YouTube Data API v3 key
- See `requirements.txt` for package dependencies.

Install them using:

```bash
pip install -r requirements.txt
```

Habilita la API de youtube y obtén el token en: https://console.cloud.google.com/apis/library
