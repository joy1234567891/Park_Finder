# **Park Finder: A Vancouver Park Search Web App**  

## **Overview**  
Park Finder is a **Python-based web application** that helps users **find parks in Vancouver** based on their preferred **neighborhoods** and **features**. Built with **Streamlit**, **Pandas**, and **REST APIs**, the app allows users to **search for parks, explore detailed park information, and visualize park distributions** through interactive charts.  

## **Features**  
🔹 **Search Parks:** Users can **filter parks by neighborhood or features** (washrooms, facilities, special features, dog-off-leash areas).  
🔹 **Explore Parks:** A randomly selected park is displayed with **detailed information** (facilities, washrooms, special features).  
🔹 **Visualize Data:** A **bar chart** shows the number of parks in each neighborhood, helping users understand park distribution.  

## **Technologies Used**  
- **Python** – Core programming language  
- **Streamlit** – Web application framework  
- **Pandas** – Data analysis and manipulation  
- **REST API Integration** – Fetching real-time data from public APIs  
- **JSON Data Processing** – Extracting, cleaning, and structuring data for better analysis  
- **Data Visualization** – Creating interactive charts using `st.bar_chart()`  

## **Data Sources**  
This project retrieves data from Vancouver's **Open Data API**:  
- **[Parks](https://opendata.vancouver.ca/explore/dataset/parks/export/)**
- **[Parks Washrooms](https://opendata.vancouver.ca/explore/dataset/parks-washrooms/export/)**
- **[Parks Facilities](https://opendata.vancouver.ca/explore/dataset/parks-facilities/export/)**
- **[Parks Special Features](https://opendata.vancouver.ca/explore/dataset/parks-special-features/export/)**
- **[Dog-Off-Leash Parks](https://opendata.vancouver.ca/explore/dataset/dog-off-leash-parks/export/)**  

## **Install Dependencies**  
pip install -r requirements.txt

## **Run the Streamlit App**  
streamlit run app.py
