# Customer Churn Analysis

Bu bootcamp projesi, bir telekomünikasyon şirketinin müşterilerinin hizmetten ayrılıp ayrılmayacağını (`Churn`) incelemektedir. Amaç; müşteri, hizmet, abonelik ve ödeme bilgilerini kullanarak churn davranışını anlamak ve temel bir sınıflandırma modeli kurmaktır.

## Proje Hakkında

Customer churn, müşterinin bir hizmeti kullanmayı bırakmasıdır. Projede önce veri yapısı ve churn ile ilişkili gözlenen farklılıklar incelenmiş, ardından veri modellemeye hazırlanarak Logistic Regression ile değerlendirilmiştir.

## Veri Seti

Veri seti, [IBM Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d/blob/d5371f5d83a446ad5673cbcca3b814b926491f8a/data/Telco-Customer-Churn.csv) veri setidir.

- Ham veri boyutu: **7.043 satır × 21 sütun**
- Her satır bir müşteriyi temsil eder.
- Ön işleme sırasında `TotalCharges` sütununda yalnızca boşluk içeren 11 problemli kayıt çıkarılmıştır. Modelleme verisi 7.032 satırdan oluşur.

## Projede Yapılanlar

- Exploratory Data Analysis
- Data Visualization
- Data Preprocessing
- Logistic Regression
- Model Evaluation

## Temel Bulgular

- Aylık sözleşme grubunda churn oranı %42,71 iken bir yıllık sözleşmede %11,27, iki yıllık sözleşmede %2,83'tür.
- Churn eden müşterilerin medyan müşteri süresi 10 ay, churn etmeyenlerin ise 38 aydır.
- Churn eden müşterilerin medyan aylık ücreti 79,65; churn etmeyenlerin medyanı 64,43'tür.
- Fiber optic internet hizmeti (%41,89) ve Electronic check ödeme yöntemi (%45,29) gruplarında daha yüksek churn oranları gözlenmiştir.

Bu bulgular veri setindeki gözlenen ilişkileri gösterir; neden-sonuç ilişkisi kurmaz.

## Model Sonuçları

Logistic Regression, test setinde majority-class baseline'ından daha iyi sonuç vermiştir.

| Metrik | Sonuç |
| --- | ---: |
| Accuracy | %80,45 |
| Majority-class baseline accuracy | %73,42 |
| Churn precision | %64,95 |
| Churn recall | %57,49 |
| Churn F1-score | %60,99 |

Model, testteki 374 gerçek churn müşterisinin 215'ini doğru tahmin etmiş; 159 müşteriyi false negative olarak kaçırmıştır. Bu nedenle sınıflar tam dengeli olmadığından accuracy tek başına yeterli bir değerlendirme değildir.

## Görseller

![Churn dağılımı](outputs/figures/churn_distribution.png)

![Sözleşme türüne göre churn oranı](outputs/figures/contract_churn.png)

![Logistic Regression confusion matrix](outputs/figures/confusion_matrix.png)

## Proje Yapısı

```text
customer-churn-analysis/
├── customer_churn_analysis.ipynb
├── data/
│   └── Telco-Customer-Churn.csv
├── outputs/
│   └── figures/
├── README.md
└── requirements.txt
```

## Kullanılan Teknolojiler

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- Jupyter Notebook

## Çalıştırma

```bash
git clone https://github.com/barissurkit/customer-churn-analysis.git
cd customer-churn-analysis
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook customer_churn_analysis.ipynb
```
