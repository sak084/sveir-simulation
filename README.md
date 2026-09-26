# sveir_simulation

💉 An epidemic model for COVID-19 transmission simulating how different vaccination rates during the early vaccine rollout stage (January 2021-March 2021) would have affected cases across the United States.

Tools: Python, Matplotlib, pandas

* Extended Susceptible-Infected-Recovered model to contain Susceptible, Exposed, Vaccinated, Infectious, and Recovered categories for higher accuracy.
(A shortcoming of this model is that dead individuals are not accounted for)

Sources: 

Equations: SEIR equation (Santosh, et al. 2025.)
<img width="442" height="53" alt="Equations: SEIR equation (Santosh, et al. 2025.)" src="https://github.com/user-attachments/assets/357cc2fe-59ad-4594-875f-931f17650cb3" />
* added additional category for vaccinated and adjusted equations

📓 Literature-Derived Parameters: 
* Used literature-derived parameters for constant variables reflecting COVID-19 Alpha variant rates during early vaccine rollout period (early 2021)
  
  - incubationRate = 1/incubation period = 1/4.9 ~ 0.2
    (Manica, et al. 2022 https://pmc.ncbi.nlm.nih.gov/articles/PMC9837419/)
    
  - recoveryRate = 1/duration of illness = 1/9.95 ~ 0.1
    * duration of illness = 9.95, averaged from low of 6.5 and high of 13.4 (Byrne, et al. 2020. https://bmjopen.bmj.com/content/10/8/e039856)
     
Example Graphs with Half, Original, Double, and Quadruple Vaccination Rates
src="<img width="1364" height="851" alt="Graphs with Half, Original, Double, and Quadruple Vaccination Rates" src="https://github.com/user-attachments/assets/d0cd30e6-dc98-48ea-ae89-d057eb51a70a" />

## Setup
1. Clone the repo
2. Download the dataset: curl -o owid-covid-data.csv https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv
3. Install dependencies: pip install pandas matplotlib
4. Run: python3 sevir_model.py
   
Ideas for future implementation:
- herd immunity threshold analysis
- account for factors such as deaths and vaccine efficacy
