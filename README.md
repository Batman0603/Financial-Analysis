# 📊 Financial Statement Analysis API

A backend service built with **FastAPI** that processes financial Excel files and extracts meaningful insights such as **P&L data, Balance Sheet, KPIs, and insights**.

---

# 🚀 Features

* 📁 Upload Excel financial statements
* 📊 Automatically detect:

  * Profit & Loss (P&L)
  * Balance Sheet
  * Cash Flow (if available)
* 🧠 Intelligent row filtering (Revenue, Profit, Expenses, etc.)
* 📈 KPI Calculation:

  * Revenue
  * Profit
  * Expenses
  * Profit Margin %
  * Expense Ratio %
* ⚠️ Business insights generation (e.g., low profit margin)
* 🛡️ Error handling & clean API responses

---

# 🏗️ Project Structure

```
financial-analysis/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   │
│   ├── api/
│   │   └── routes.py          # API endpoints
│   │
│   ├── services/
│   │   ├── analysis_service.py   # Main processing logic
│   │   ├── excel_service.py     # Excel reading logic
│   │   ├── classify_service.py  # Sheet classification
│   │   ├── kpi_service.py       # KPI calculations
│   │   └── insight_service.py   # Insight generation
│   │
│   ├── utils/
│   │   └── filters.py           # Row filtering logic
│   │
│   └── models/
│       └── response_model.py    # Response schemas (optional)
│
├── uploads/                    # Uploaded files (temporary storage)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/financial-analysis.git
cd financial-analysis
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Linux / Mac**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

---

# 🌐 API Access

* Swagger UI:
  👉 http://127.0.0.1:8000/docs

* ReDoc:
  👉 http://127.0.0.1:8000/redoc

---

# 📤 API Usage

## Upload Financial File

### Endpoint:

```
POST /upload
```

### Request:

* Form-data
* Key: `file`
* Value: Excel file (.xlsx)

---

### Response Example:

```json
{
  "message": "File processed successfully",
  "data": {
    "status": "success",
    "data": {
      "pnl": [...],
      "balance_sheet": [...],
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

# 🧠 Core Logic

## 1. Excel Processing

* Reads all sheets
* Converts to pandas DataFrames

## 2. Sheet Classification

* Identifies:

  * P&L
  * Balance Sheet
  * Cash Flow

## 3. Row Filtering

Filters only relevant financial rows:

* Revenue / Sales
* Profit
* Expenses
* Wages
* Tax
* Depreciation

---

## 4. KPI Calculation

```python
profit_margin = (profit / revenue) * 100
expense_ratio = (expenses / revenue) * 100
```

Handles:

* Missing values
* Zero division
* Noisy Excel data

---

## 5. Insight Generation

Example rules:

* Profit margin < 10% → ⚠️ Low profit margin
* High expense ratio → ⚠️ High expenses

---

# 🛡️ Error Handling

The system safely handles:

* Missing columns (`particulars`)
* Invalid Excel files
* Empty sheets
* Parsing failures

Example:

```json
{
  "status": "error",
  "message": "Processing error: invalid file format"
}
```

---

# 📦 Requirements

```
fastapi
uvicorn
pandas
openpyxl
python-multipart
```

---

# 🧪 Testing

Use Swagger UI:

1. Open `/docs`
2. Click `POST /upload`
3. Upload Excel file
4. View structured output

---

# 🚀 Future Enhancements

* 📊 Frontend Dashboard (React)
* 📈 Charts (Revenue vs Profit)
* 📁 Multi-file upload
* 🤖 AI-based financial insights
* 📤 Export to PDF / Excel

---

# 👨‍💻 Author

KARTHIKEYAN K R
---

# ⭐ Notes

This project demonstrates:

* Real-world Excel parsing challenges
* Financial data normalization
* Backend architecture design
* Production-ready error handling

---

# 💡 Tip

Financial Excel files are messy.
This project is built to **handle real-world inconsistencies**, not perfect data.

---


