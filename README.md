# sveir_simulation

💉 An epidemic model for COVID-19 transmission simulating how different vaccination rates during the early pandemic could have affected the number of cases

Tools: Python, Matplotlib

* Extended to the SEVIR model, separating the population into five categories (Susceptible, Exposed, Vaccinated, Infectious, Recovered)
for higher accuracy. (A shortcoming of this model is that dead individuals are not accounted for)
* Used literature-derived perimeters for variables reflecting COVID-19 rates during early vaccine rollout period (early 2021) for adults 

Sources: 

Equations: SEIR equation (Santosh, et al. 2025.)
<img width="442" height="53" alt="Screenshot 2026-07-14 at 11 36 31 AM" src="https://github.com/user-attachments/assets/357cc2fe-59ad-4594-875f-931f17650cb3" />

* added additional category for vaccinated and adjusted equations


📓 Literature-Derived Perimeters: 
infectionRate = reproductionNumber # x recoveryRate = 5.08 x 0.1 = 0.51 (rounded to nearest hundredth)
    * reproductionNumber = 5.08 (Liu, et al. 2022. https://academic.oup.com/jtm/article/29/3/taac037/6545354)
    * recoveryRate = 0.1 (Liu, et al. 2022. https://academic.oup.com/jtm/article/29/3/taac037/6545354)
incubationRate = 1/incubation days
               = 1/6.6 -> 0.15 (rounded to nearest hundredth)
    * incubation days = 6.6 (Liao, et al. 2020. https://www.medrxiv.org/content/10.1101/2020.03.10.20032136v1)
recoveryRate 𝛾 = 1/duration of illness
             𝛾 = 1/9.95 -> 𝛾 = 0.10 (rounded to nearest hundredth)
    * duration of illness = 9.95, averaged from low of 6.5 and high of 13.4 (Byrne, et al. 2020. https://bmjopen.bmj.com/content/10/8/e039856)
    
Initial Values for Modeling (Umapathy, et al. 2024. https://ojs.wiserpub.com/index.php/CM/article/view/5746)
    N = 1000
    initialSusceptible = 100
    initialExposed = 200
    initialVaccinated = 100
    initialInfected = 200
    initialRecovered = 400

Example Graphs with 5% ,10%, 30%, and 70% Vaccination Rates
<img width="1235" height="797" alt="Screenshot 2026-07-14 at 12 29 42 PM" src="https://github.com/user-attachments/assets/34e63a0e-bec1-4c39-9ea0-ee99459ef327" />

Ideas for future implementation:
- herd immunity threshold analysis with factors like vaccine efficacy
- build a visualization with sliders for the variables
