# 📊 EdTech Influencer Analytics Dashboard

![GitHub Repo stars](https://img.shields.io/github/stars/Gyanankur23/youtube-instagram-influencer-dashboard?style=social)
![GitHub forks](https://img.shields.io/github/forks/Gyanankur23/youtube-instagram-influencer-dashboard?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Gyanankur23/youtube-instagram-influencer-dashboard?style=social)
![GitHub issues](https://img.shields.io/github/issues/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub closed issues](https://img.shields.io/github/issues-closed/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub license](https://img.shields.io/github/license/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub repo size](https://img.shields.io/github/repo-size/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub last commit](https://img.shields.io/github/last-commit/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub contributors](https://img.shields.io/github/contributors/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub language count](https://img.shields.io/github/languages/count/Gyanankur23/youtube-instagram-influencer-dashboard)
![GitHub top language](https://img.shields.io/github/languages/top/Gyanankur23/youtube-instagram-influencer-dashboard)
![Code size](https://img.shields.io/github/languages/code-size/Gyanankur23/youtube-instagram-influencer-dashboard)
![Lines of code](https://img.shields.io/tokei/lines/github/Gyanankur23/youtube-instagram-influencer-dashboard)
![Activity](https://img.shields.io/github/commit-activity/m/Gyanankur23/youtube-instagram-influencer-dashboard)
![Made with](https://img.shields.io/badge/Made%20with-HTML5-red)
![Platform](https://img.shields.io/badge/Platform-Web-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/version-1.0.0-green)

A professional Power BI-style analytics dashboard for EdTech influencers, featuring comprehensive data visualization, cross-filtering capabilities, and modern UI/UX design.

## 🎯 Features

- **Power BI-Quality UI**: Consistent blue theme with professional card-based design
- **6 KPI Cards**: Real-time metrics including total creators, subscribers, engagement rates
- **5-6 Slicers Per Page**: Cross-filtering by Core Area, Subject, Platform, Auditor, Year
- **5-7 Visuals Per Page**: Bar, Column, Pie, Donut, Radar, Line, Area, Scatter, Gauge charts
- **Interactive Data Table**: Searchable table with all creator metrics
- **Creator Profiles**: Individual radar charts and performance gauges
- **Growth Trends**: Timeline analysis with engagement tracking
- **Responsive Design**: Works seamlessly across desktop and tablet devices
- **Real-time Filtering**: Instant updates across all visualizations
- **Professional Tooltips**: Detailed information on hover

## 📊 Dashboard Pages

### 1. Ecosystem Overview
- Top 10 creators by subscribers (Horizontal Bar Chart)
- Core area distribution (Pie Chart)
- Subject distribution (Donut Chart)
- Platform comparison (Column Chart)
- Engagement gauge (Doughnut Gauge)
- Channel growth timeline (Line Chart)
- Subscribers vs Views scatter plot
- Detailed data table with search

### 2. Subject Analysis
- Subject performance radar chart
- Subject vs Core Area matrix (Stacked Bar)
- Subject engagement comparison (Grouped Column)
- Subject area polar chart
- Physics, Chemistry, Mathematics, Biology KPIs

### 3. Platform Performance
- Platform performance comparison (Grouped Bar)
- Cross platform types distribution (Donut)
- Platform engagement rate (Line Chart)
- Platform growth area (Area Chart)
- YouTube vs Other platform metrics

### 4. Creator Profiles
- Individual creator selection
- Creator profile card with metrics
- Performance radar chart
- Engagement gauge
- Random creator explorer

### 5. Growth Trends
- Channel growth timeline
- Subscriber growth trend (Area Chart)
- Engagement trend over time
- Cross platform adoption rate

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Edge, Safari)
- Local web server (Python's built-in HTTP server)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Gyanankur23/youtube-instagram-influencer-dashboard.git
cd youtube-instagram-influencer-dashboard
```

2. Install Python dependencies:
```bash
pip install pandas openpyxl
```

3. Process the Excel data:
```bash
python extract_data.py
```

4. Start the local server:
```bash
python -m http.server 8000
```

5. Open your browser and navigate to:
```
http://localhost:8000/dashboard.html
```

## 📁 Project Structure

```
youtube-instagram-influencer-dashboard/
├── Youtube & Instagram influencers.xlsx    # Source Excel data
├── cleaned_data.csv                       # Processed CSV data
├── dashboard_data.json                    # JSON data for dashboard
├── extract_data.py                        # Data extraction script
├── dashboard.html                         # Main dashboard file
├── data_export.json                       # Exported data
└── README.md                              # Documentation
```

## 🎨 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: TailwindCSS (via CDN)
- **Charts**: Chart.js
- **Icons**: Font Awesome 6
- **Data Processing**: Python, Pandas
- **Data Source**: Excel (.xlsx)

## 📊 Data Metrics

The dashboard tracks the following metrics for 466+ EdTech influencers:

- **Creator Information**: Name, Channel Name, Platform
- **Engagement Metrics**: Subscribers, Average Views, Engagement Rate
- **Content Classification**: Core Area (JEE, NEET, JEE/NEET, Other)
- **Subject Tags**: Physics, Chemistry, Mathematics, Biology, General
- **Cross-Platform**: Presence on Instagram, Telegram, LinkedIn, WhatsApp
- **Auditor Assignment**: Data validation and quality control
- **Timeline**: Channel start year and growth tracking

## 🔧 Configuration

### Data Source

The dashboard uses data from `Youtube & Instagram influencers.xlsx`. To update the data:

1. Replace the Excel file with your updated data
2. Run the extraction script:
```bash
python extract_data.py
```
3. Refresh the dashboard in your browser

### Customization

- **Theme Colors**: Modify CSS variables in the `<style>` section of `dashboard.html`
- **KPI Metrics**: Update the `updateKPIs()` function in the JavaScript section
- **Chart Types**: Modify chart configurations in the render functions

## 📈 Usage

### Filtering Data

1. Use the slicer dropdowns to filter by:
   - Core Area (JEE, NEET, JEE/NEET, Other)
   - Subject (Physics, Chemistry, Mathematics, Biology, General)
   - Platform (YouTube, Other)
   - Cross Platform (Yes/No)
   - Auditor (Assigned team members)
   - Start Year (2011-2024)

2. All visualizations update automatically based on selected filters

### Navigation

- Click on sidebar items to switch between pages
- Use the "Reset Filters" button to clear all selections
- Use the "Refresh" button to reload data

### Creator Profiles

1. Navigate to "Creator Profiles" page
2. Select a creator from the dropdown
3. View individual performance metrics
4. Use "Random Creator" to explore different profiles

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Data sourced from EdTech influencer research
- Built with Chart.js for data visualization
- Styled with TailwindCSS for modern UI
- Icons provided by Font Awesome

## 📞 Contact

For questions or support, please open an issue on GitHub or contact the repository owner.

## 🔗 Links

- [Live Demo](https://github.com/Gyanankur23/youtube-instagram-influencer-dashboard)
- [Issue Tracker](https://github.com/Gyanankur23/youtube-instagram-influencer-dashboard/issues)
- [Pull Requests](https://github.com/Gyanankur23/youtube-instagram-influencer-dashboard/pulls)

## 📊 Dashboard Preview

![Dashboard Preview](https://img.shields.io/badge/Preview-Live-brightgreen)
![Documentation](https://img.shields.io/badge/Docs-Complete-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-success)
![Build](https://img.shields.io/badge/Build-Passing-success)

---

Made with ❤️ by [Gyanankur Baruah](https://github.com/Gyanankur23)

**⭐ If you find this project helpful, please consider giving it a star on GitHub!**
