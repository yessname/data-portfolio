# 📊 Excel Salary Dashboard

An interactive salary dashboard built in **Microsoft Excel** to explore compensation trends across data-related jobs.

The dashboard allows users to compare salaries by **job title**, **country**, and **schedule type**, helping job seekers better understand the data job market.

---

## 📌 Project Overview

This project demonstrates:

- Building an interactive Excel dashboard  
- Comparing median salaries across job roles  
- Visualizing salary differences by country  
- Using formulas and data validation for dynamic filtering  

---

## 🎯 Project Goals

- Analyze salary trends for data jobs  
- Compare median salaries by role  
- Explore geographic salary differences  
- Create an interactive Excel dashboard  

---

## 🌍 Dataset

The project uses a jobs dataset containing real-world job posting data.

The dataset includes:

- Job titles  
- Salaries  
- Locations  
- Job schedule types  
- Skills  

---

## 🛠 Excel Features Used

- Charts  
- Formulas and Functions  
- Data Validation  

---

## 🏗 Dashboard Components

### Salary by Job Title

A horizontal **bar chart** showing median salary by job title.

- Sorted by salary for easier comparison  
- Highlights higher-paying roles such as senior and engineering positions  

---

### Salary by Country

A **map chart** visualizing median salaries across countries.

- Uses color intensity to highlight regional differences  
- Helps quickly identify global salary disparities  

---

### Interactive Filters

The dashboard includes filters for:

- Job Title  
- Country  
- Type  

These filters allow users to explore salary trends dynamically.

---

## 🧮 Key Formulas

### Median Salary

Calculates the median salary based on job title, country, and schedule type.

```excel
=MEDIAN(
IF(
    (jobs[job_title_short]=A2)*
    (jobs[job_country]=country)*
    (ISNUMBER(SEARCH(type,jobs[job_schedule_type])))*
    (jobs[salary_year_avg]<>0),
    jobs[salary_year_avg]
)
)
