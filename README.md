# 📊 Financial Statement Analysis API

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-teal?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Pandas-Data--Processing-black?style=for-the-badge&logo=pandas" />
  <img src="https://img.shields.io/badge/OpenPyXL-Excel-orange?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=yourusername&label=Project+Views&color=0e75b6&style=flat" />
  <img src="https://img.shields.io/github/stars/yourusername/financial-analysis?style=social" />
  <img src="https://img.shields.io/github/forks/yourusername/financial-analysis?style=social" />
</p>

---

## 🧠 Overview

A **FastAPI-based backend service** that processes financial Excel files and extracts structured insights such as:

- 📊 Profit & Loss  
- 📑 Balance Sheet  
- 💸 Cash Flow  
- 📈 KPIs  
- ⚠️ Business insights  

Built to handle real-world messy Excel files with consistency and accuracy.

---

## ⚡ Features

- 📁 Upload Excel financial statements  
- 📊 Automatic sheet detection (P&L, Balance Sheet, Cash Flow)  
- 🧠 Intelligent row filtering  
- 📈 KPI calculations  
- ⚠️ Insight generation  
- 🛡️ Robust error handling  

---

## 🏗️ Architecture

```
        ┌──────────────┐
        │   Client     │
        └──────┬───────┘
               │
        ┌──────▼────────┐
        │   FastAPI     │
        │   Backend     │
        └──────┬────────┘
               │
   ┌───────────┼────────────┐
   │           │            │
   ▼           ▼            ▼
Excel     Processing     KPI Engine
Parser     Logic         + Insights
(pandas)                Generator
```

---

## 🧩 Project Structure

```
financial-analysis/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── analysis_service.py
│   │   ├── excel_service.py
│   │   ├── classify_service.py
│   │   ├── kpi_service.py
│   │   └── insight_service.py
│   ├── utils/
│   │   └── filters.py
│   └── models/
│       └── response_model.py
│
├── uploads/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/financial-analysis.git
cd financial-analysis
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Access

- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

---

## 📤 API Usage

### Endpoint

```
POST /upload
```

### Request

- Form-data  
- Key: `file`  
- Value: Excel file (.xlsx)

---

### Response Example

```json
{
  "message": "File processed successfully",
  "data": {
    "status": "success",
    "data": {
      "pnl": [],
      "balance_sheet": [],
      "cashflow": []
    },
    "kpis": {
      "revenue": 328957748.06,
      "profit": 52056151.38,
      "expenses": 102541739,
      "profit_margin_%": 15.82,
      "expense_ratio_%": 31.17
    },
    "insights": [
      "⚠️ Low profit margin"
    ]
  }
}
```

---

## 🧠 Core Logic

### 📄 Excel Processing
- Reads all sheets  
- Converts to pandas DataFrames  

### 🧩 Sheet Classification
- Identifies:
  - P&L  
  - Balance Sheet  
  - Cash Flow  

### 🔍 Row Filtering
Extracts:
- Revenue  
- Profit  
- Expenses  
- Tax  
- Depreciation  

### 📈 KPI Calculation

```python
profit_margin = (profit / revenue) * 100
expense_ratio = (expenses / revenue) * 100
```

Handles:
- Missing values  
- Zero division  
- Noisy Excel data  

---

### ⚠️ Insight Generation

- Profit margin < 10% → Low profit margin  
- High expense ratio → High expenses  

---

## 🛡️ Error Handling

Handles:

- Invalid Excel files  
- Missing columns  
- Empty sheets  
- Parsing failures  

Example:

```json
{
  "status": "error",
  "message": "Processing error: invalid file format"
}
```

---

## 📦 Requirements

```
fastapi
uvicorn
pandas
openpyxl
python-multipart
```

---

## 🧪 Testing

1. Open `/docs`  
2. Use `POST /upload`  
3. Upload Excel file  
4. View output  

---

## 🚀 Future Enhancements

- 📊 Frontend dashboard  
- 📈 Data visualization  
- 📁 Multi-file upload  
- 🤖 AI-based insights  
- 📤 Export reports  

---

## 👨‍💻 Author

**KARTHIKEYAN K R**

---

## ⭐ Notes

- Handles real-world Excel inconsistencies  
- Clean modular backend architecture  
- Designed for scalability and production use  

---
