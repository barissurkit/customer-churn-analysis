# Katkı Rehberi

Katkıda bulunmak istediğiniz için teşekkürler!

## Kurulum

1. Repository'yi fork'layıp klonlayın.
2. Python 3.12 ile sanal ortam oluşturun ve bağımlılıkları kurun:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt pytest
   ```

## Testleri çalıştırma

```bash
pytest tests
```

Testler not defterindeki kod hücrelerini çalıştırır; not defterini değiştirirseniz testlerin ve README'deki sonuçların hâlâ tutarlı olduğunu kontrol edin.

## Pull request beklentileri

- `main` dalına doğrudan push yapmayın; ayrı bir dal açıp pull request gönderin.
- Pull request'i tek bir konuya odaklı tutun ve ne değiştiğini kısaca açıklayın.
- Not defterini commit etmeden önce hücreleri baştan sona (Restart & Run All) çalıştırın.
- `pytest tests` yerelde geçmeli; GitHub Actions iş akışı (CI) yeşil olmalıdır.
- Gizli bilgi (anahtar, parola vb.) eklemeyin.
