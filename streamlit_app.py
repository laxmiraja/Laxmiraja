import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Srinivasan
##### *Resume* 
''')

image = Image.open('Srini.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Developer and Administrator with almost ten+ years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Passion for data integrity, visualization, and statistics. I’m excited to apply my passion for data science to the collaborative efforts of aChevron team focused on insightful, high-quality data analytics and visualizations.
- Innovative and scientifically rigorous recent graduate with a significant data science internship experience to bring to the table. With a team-oriented attitude, eager to contribute my abilities in quantitative modeling and experimentation to enhance the experience of Pinterest users around the world.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Srinivasan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#professional-summary">Professional Summary</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelors of Commerce**, *University of Madras*, Chennai',
'2004-2007')
st.markdown('''
- Percentage: `60%`
- Graduated with First Class Honors.
''')

txt('**Higher Secondary Education**, *Pennalurpet Government Higher Secondary School*, Thiruvallur',
'2002-2004')
st.markdown('''
- Percentage: `70%`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Senior Data Intedgrity Associate, India Ed-ops Team**, LexisNexis, RELX, Chennai',
'2019-2021')
st.markdown('''
- Created an aggregated report daily for the client to make investment decisions and help analyze market trends.
- Built an internal visualization platform for the clients to view historic data, make comparisons between various issuers, analytics for different bonds and market.
- The model collects, merges daily data from market providers and applies different cleaning techniques to eliminate bad data points.
- The model merges the daily data with the historical data and applies various quantitative algorithms to check the best fit for the day.
- Captures the changes for each market to create a daily email alert to the client to help make better investment decisions.
- Built the model on Azure platform using Python and Spark for the model development and Dash by plotly for visualizations.
- Built REST APIs to easily add new analytics or issuers into the model.
- Automate different workflows, which are initiated manually with Python scripts and Unix shell scripting.
- Create, activate and program in Anaconda environment.
- Worked on predictive analytics use-cases using Python language.
- Clean data and processed third party spending data into maneuverable deliverables within specific format with Excel macros and python libraries such as NumPy, SQLAlchemy and matplotlib.
- Used Pandas as API to put the data as time series and tabular format for manipulation and retrieval of data.
- Helped with the migration from the old server to Jira database (Matching Fields) with Python scripts for transferring and verifying the information.
- Analyze Format data using Machine Learning algorithm by Python Scikit-Learn.
- Experience in python, Jupyter, Scientific computing stack (numpy, scipy, pandasand matplotlib).
- Perform troubleshooting, fixed and deployed many Python bug fixes of the two main applications that were a main source of data for both customers and internal customer service team.
- Write Python scripts to parse JSON documents and load the data in database.
- Generating various capacity planning reports (graphical) using Python packages like Numpy, matplotlib.
- Analyzing various logs that are been generating and predicting/forecasting next occurrence of event with various Python libraries.
- Created Autosys batch processes to fully automate the model to pick the latest as well as the best bond that fits best for that market.
- Created a framework using plotly, dash and flask for visualizing the trends and understanding patterns for each market using the history data.
- Used python APIs for extracting daily data from multiple vendors.
- Used Spark and SparkSQL for data integrations, manipulations.Worked on a POC for creating a docker image on azure to run the model
''')

txt('**Data Intedgrity Associate, India Ed-ops Team**, LexisNexis, RELX, Chennai',
'2012-2019')
st.markdown('''
- Built scalable and deployable machine learning models.
- Utilized Sqoop to ingest real-time data. Used analytics libraries Sci-Kit Learn, MLLIB and MLxtend.
- Extensively used Python's multiple data science packages like Pandas, NumPy, matplotlib, Seaborn, SciPy, Scikit-learn and NLTK.
- Performed Exploratory Data Analysis, trying to find trends and clusters.
- Built models using techniques like Regression, Tree based ensemble methods, Time Series forecasting, KNN, Clustering and Isolation Forest methods.
- Worked on data that was a combination of unstructured and structured data from multiple sources and automated the cleaning using Python scripts.
- Extensively performed large data read/writes to and from csv and excel files using pandas.
- Tasked with maintaining RDD's using SparkSQL.
- Communicated and coordinated with other departments to collection business requirement.
- Tackled highly imbalanced Fraud dataset using undersampling with ensemble methods, oversampling and cost sensitive algorithms.
- Improved fraud prediction performance by using random forest and gradient boosting for feature selection with Python Scikit-learn.
- Implemented machine learning model (logistic regression, XGboost) with Python Scikitlearn.
- Optimized algorithm with stochastic gradient descent algorithm Fine-tuned the algorithm parameter with manual tuning and automated tuning such as Bayesian Optimization.
- Developed a technical brief based on the business brief. This contains detailed steps and stages of developing and delivering the project including timelines.
- After sign-off from the client on technical brief, started developing the SAS codes.
- Wrote the data validation SAS codes with the help of Univariate, Frequency procedures.
- Summarising the data at customer level by joining the datasets of customer transaction, dimension and from 3rd party sources.
- Separately calculated the KPIs for Target and Mass campaigns at pre-promo-post periods with respective to their transactions, spend and visits.
- Also measured the KPIs at MoM (Month on Month), QoQ (Quarter on Quarter) and YoY (Year on Year) with respect to pre-promo-post.
- Measured the ROI based on the differences pre-promo-post KPIs.
- Extensively used SAS procedures like IMPORT, EXPORT, SORT, FREQ, MEANS, FORMAT, APPEND, UNIVARIATE, DATASETS and REPORT.
- Standardised the data with the help of PROC STANDARD.
- Implemented cluster analysis (PROC CLUSTER and PROC FASTCLUS) iteratively.
- Worked extensively with data governance team to maintain data models, Metadata and dictionaries.
- Used Python to preprocess data and attempt to find insights.
- Iteratively rebuild models dealing with changes in data and refining them over time.
- Created and published multiple dashboards and reports using Tableau server.
- Extensively used SQL queries for legacy data retrieval jobs.
- Tasked with migrating the django database from MySQL to PostgreSQL.
- Gained expertise in Data Visualization using matplotlib, Bokeh and Plotly.
- Responsible for maintaining and analyzing large datasets used to analyze risk by domain experts.
- Developed Hive queries that compared new incoming data against historic data. Built tables in Hive to store large volumes of data.
- Used big data tools Spark (Sparksql, Mllib) to conduct the real time analysis of credit card fraud based on AWS * Performed Data audit, QA of SAS code/projects and sense check of results.
''')

#####################
st.markdown('''
## Professional Summary
''')
st.info('''
- Highly efficient Data Scientist/Data Analyst with 6+ years of experience in Data Analysis, Machine Learning, Data mining with large data sets of Structured and Unstructured data, Data Acquisition, Data Validation, Predictive modeling, Data Visualization, Web Scraping. Adept in statistical programming languages like R and Python including Big Data technologies like Hadoop, Hive.
- Proficient in managing entire data science project life cycle and actively involved in all the phases of project life cycle including data acquisition, data cleaning, data engineering, features scaling, features engineering, statistical modeling (decision trees, regression models,clustering), dimensionality reduction using Principal Component Analysis and Factor Analysis, testing and validation using ROC plot, K - fold cross-validation and data visualization.
- Adept and deep understanding of Statistical modeling, Multivariate Analysis, model testing, problem analysis, model comparison, and validation.
- Expertise in transforming business requirements into analytical models, designing algorithms, building models, developing data mining and reporting solutions that scale across a massive volume of structured and unstructured data.
- Skilled in performing data parsing, data manipulation and data preparation with methods including describe data contents, compute descriptive statistics of data, regex, split and combine, Remap, merge, subset, reindex, melt and reshape.
- Experience in using various packages in R and python-like ggplot2, caret, dplyr, Rweka, gmodels, twitter, NLP, Reshape2, rjson, plyr, pandas, NumPy, Seaborn, SciPy, Matplotlib, sci-kit-learn, Beautiful Soup.
- Extensive experience in Text Analytics, generating data visualizations using R, Python and creating dashboards using tools like Tableau.
- Hands on experience with big data tools like Hadoop, Spark, Hive, Pig, PySpark, Spark SQL,PySpark Hands on experience in implementing LDA, Naive Bayes and skilled in Random Forests, Decision Trees, Linear and Logistic Regression, SVM, Clustering, neural networks, Principle Component Analysis.
- Good Knowledge in Proof of Concepts (PoC's), gap analysis and gathered necessary data for analysis from different sources, prepared data for data exploration using data munging.
- Good industry knowledge, analytical &amp;problem-solving skills and ability to work well within a team as well as an individual.
- Expertise in transforming business requirements into analytical models, designing algorithms, building models, developing data mining and reporting solutions that scale across a massive volume of structured and unstructured data.
- Experience in designing stunning visualizations using Tableau software and publishing and presenting dashboards, Storyline on web and desktop platforms.
- Experience and Technical proficiency in Designing, Data Modeling Online Applications, Solution Lead for Architecting Data Warehouse/Business Intelligence Applications.
- Experience with Data Analytics, Data Reporting, Ad-hoc Reporting, Graphs, Scales, PivotTables and OLAP reporting.
- Highly skilled in using Hadoop (pig and Hive) for basic analysis and extraction of data in the infrastructure to provide data summarization.
- Highly skilled in using visualization tools like Tableau, ggplot2, dash, flask for creating dashboards.
- Worked and extracted data from various database sources like Oracle, SQL Server, DB2, regularly accessing JIRA tool and other internal issue trackers for the Project development.
- Highly creative, innovative, committed, intellectually curious, business savvy with good communication and interpersonal skills.
- Extensive experience in Data Visualization including producing tables, graphs, listings using various procedures and tools such as Tableau.
''')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/srinivasan-nc-8525b223a')
txt2('Facebook', 'https://www.facebook.com/profile.php?id=100002941390748')
txt2('GitHub', 'https://github.com/NCXSX/')
