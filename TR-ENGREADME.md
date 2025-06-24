# 🏠 Web Tabanlı Konut Fiyat Tahmin Uygulaması / Web-based House Price Prediction Application

Bu proje, kullanıcıdan alınan konut bilgilerine göre makine öğrenmesi algoritmaları kullanarak **konut fiyat tahmini** yapan web tabanlı bir uygulamadır.

This project is a **web-based machine learning application** that predicts house prices based on user-provided housing data.

---

## 📌 Proje Özeti / Project Overview

📈 Konut piyasasında doğru fiyat tahmini, alım-satım kararlarını doğrudan etkiler. Bu uygulama, **Flask ve Python** tabanlı bir backend ile çalışır ve eğitilmiş bir `.pickle` modeli ile tahminleri gerçekleştirir.

Accurate price prediction is key in real estate decisions. This application uses a **Flask-Python backend** powered by a trained `.pickle` machine learning model.

---

## ⚙️ Kullanılan Teknolojiler / Technologies Used

- Python 3
- Flask (Web Framework)
- Scikit-learn (ML models)
- TensorFlow / Keras (Neural Networks)
- Pandas, NumPy (Data handling)
- HTML & CSS (Frontend)
- Pickle (Model Serialization)

---

## 🧠 Kullanılan Algoritmalar / Algorithms Used

Aşağıdaki algoritmalar test edildi, değerlendirildi ve karşılaştırıldı:

The following models were implemented and evaluated:

- ✅ Gradient Boosting Machine (GBM) *(best performer)*
- Linear & Ridge Regression
- Random Forest Regressor
- Neural Networks (Keras)
- XGBoost
- Support Vector Regression (SVR)
- Ensemble Learning (RF + GBM + XGBoost)

---

## 📊 Veri Seti / Dataset

- **Kaynak / Source:** Kaggle – Tehran House Prices (Vala Khorasani)
- **Boyut / Size:** ~11.000 kayıt
- **Özellikler / Features:**
  - Alan (m²), Oda Sayısı
  - Otopark, Asansör, Depo (Binary)
  - Adres (23 semt için one-hot encoded)
  - Fiyat (USD)

---

## 🖥️ Uygulama Akışı / Application Workflow

1. Kullanıcı formdan giriş yapar / User inputs data via web form
2. Flask backend verileri işler / Backend preprocesses input
3. Model tahmini yapar / Prediction is made using `.pickle` model
4. Sonuç arayüzde gösterilir / Result is displayed on the frontend

---

## 🧪 Değerlendirme Metrikleri / Evaluation Metrics

- 📉 Mean Absolute Error (MAE)
- 📉 Root Mean Square Error (RMSE)
- 📈 R² Score

> GBM modeli en iyi performansı göstermiştir (R² ≈ 0.81).

GBM showed the best performance with R² ≈ 0.81 and fast prediction time (<1s).

---

## 🚀 Gelecek Geliştirmeler / Future Improvements

- Gerçek zamanlı veri entegrasyonu / Real-time data integration
- Farklı şehir/dil desteği / Multi-city & multi-language support
- Gelişmiş görselleştirme (Plotly, D3.js) / Advanced visualization
- Cloud deployment (Heroku, AWS, Render)

---



