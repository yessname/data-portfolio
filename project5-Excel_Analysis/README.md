# 📈 Data Jobs Market Analysis (Excel)

An Excel-based analysis project exploring **salaries, skills, and demand** across data-related jobs.

The project analyzes how skills influence salary levels and which technologies are most common in the data job market.

---

## 📌 Project Overview

This project demonstrates:

- Cleaning and transforming data with **Power Query**  
- Building a relational model with **Power Pivot**  
- Analyzing data using **PivotTables, PivotCharts, and DAX**  
- Exploring relationships between skills, salary, and demand  

---

## 🎯 Project Goals

- Analyze whether more skills lead to higher pay  
- Compare salaries across regions  
- Identify the most common skills in data jobs  
- Evaluate salary value of top skills  

---

## 🌍 Dataset

The project uses a **2023 data jobs dataset** based on real-world job postings.

The dataset includes:

- Job titles  
- Salaries  
- Locations  
- Skills  

---

## 🛠 Excel Features Used

- Pivot Tables  
- Pivot Charts  
- DAX (Data Analysis Expressions)  
- Power Query  
- Power Pivot  

---

## 🏗 Analysis Sections

The analysis focuses on four main questions.

---

### 1️⃣ Do More Skills Lead to Higher Pay?

Using **Power Query**, the dataset was cleaned and split into two tables:

- job information  
- skills linked to job IDs  

**Insight**

Jobs requiring more skills—such as **Senior Data Engineer** and **Data Scientist**—tend to have higher median salaries. Roles requiring fewer skills generally show lower salary levels.

---

### 2️⃣ Salary by Region

Using **PivotTables and DAX**, median salary was calculated across regions.

Example DAX measure:

```excel
Median Salary := MEDIAN(data_jobs_all[salary_year_avg])
