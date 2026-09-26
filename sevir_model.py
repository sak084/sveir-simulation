import matplotlib.pyplot as plt
import pandas as pd

class SEVIR:
    df = pd.read_csv("owid-covid-data.csv")
    us = df[df["location"] == "United States"]
    window = us[(us["date"] >= "2021-01-01") & (us["date"] <= "2021-03-01")]

    # initializes constant variables for sveir model
    # infection rate: number of infections/number of people at risk 
    # (assume 100% vaccine efficacy, and recovered people can get it too rn)
    # incubation rate: 1/average incubation period = 1/5 days = 0.2
    # len: all of the entries in the dataset 

    infectionRate = window["total_cases"].mean() / (window["population"].mean() - 
                    window["total_vaccinations"].mean() - window["total_cases"].mean())
    incubationRate = 0.2
    recoveryRate = 0.1
    days = len(window)

    first_row = window.iloc[0]
    N = first_row["population"]

    initialSusceptible = first_row["population"] - first_row["total_vaccinations"] - first_row["total_cases"]
    initialVaccinated = first_row["total_vaccinations"]
    initialInfected = first_row["total_cases"]

    #calculate initial recovered manually by doing total cases - total deaths - active cases
    initialRecovered = first_row["total_cases"] - first_row["total_deaths"] - initialInfected

    # calculate initial exposed manually by subtracting s,v,i,r from p
    initialExposed = first_row["population"] - initialSusceptible - initialVaccinated - initialInfected - initialRecovered 
 
    averageVaccinationRate = window["new_vaccinations_smoothed_per_million"].mean()/ 1000000
    def __init__(self, vaccinationRate = averageVaccinationRate):
        self.vaccinationRate = vaccinationRate

    # calculates, S, E, V, I, and R values for each day
    # appends the values to a list to be graphed by plot()
    def addCounts(self):
        susceptible = [self.initialSusceptible]
        exposed = [self.initialExposed]
        vaccinated = [self.initialVaccinated]
        infected = [self.initialInfected]
        recovered = [self.initialRecovered]

        for i in range(self.days):
            # calculating rate of change per day, respectively
            dS = -(self.infectionRate * infected[-1] * susceptible[-1])/self.N - self.vaccinationRate * susceptible [-1]
            dE = (self.infectionRate * infected[-1] * susceptible[-1]/self.N) - self.incubationRate * exposed [-1]
            dI = self.incubationRate * exposed[-1] - self.recoveryRate * infected[-1]
            dV = self.vaccinationRate * susceptible[-1]
            dR = self.recoveryRate * infected[-1]

            # adding new numbers to the list, which shows number of susceptible, infected, and recovered by day
            susceptible.append(susceptible[-1] + dS)
            exposed.append(exposed[-1] + dE)
            vaccinated.append(vaccinated[-1] + dV)
            infected.append(infected[-1] + dI)
            recovered.append(recovered[-1] + dR)

        return susceptible, exposed, vaccinated, infected, recovered

    # helper function to get the days as a list to plot as x
    def getDaysList (self):
        daysList = []
        for i in range(self.days+1):
            daysList.append(i)
        return daysList

    # graphing the lists using matplotlib
    def plot(self, ax, daysList, susceptible, exposed, vaccinated, infected, recovered):
        ax.plot(daysList, susceptible, label = "Susceptible")
        ax.plot(daysList, exposed, label = "Exposed")
        ax.plot(daysList, vaccinated, label = "Vaccinated")
        ax.plot(daysList, infected, label = "Infected")
        ax.plot(daysList, recovered, label = "Recovered")
        ax.set_xlabel("Days", fontsize = 10)
        ax.set_ylabel("Population", fontsize = 10)
        ax.legend()
        ax.grid(True)

# main method that plots four sevir graphs with various vaccination rates
def main():
    # making four separate subplots
    fig, axs = plt.subplots(2,2)
    plt.title = "SEVIR Model Comparison with vaccination rates"

    # simulating different vaccination rates in comparison to what we have now
    initialVaccinationRate = SEVIR.averageVaccinationRate

    # subplot #1 (upper left)- Halved Current Rate
    model1 = SEVIR(0.5 * initialVaccinationRate) 
    s1, e1, v1, i1, r1 = model1.addCounts()
    daysList1 = model1.getDaysList()
    model1.plot(axs[0][0], daysList1, s1, e1, v1, i1, r1)
    axs[0][0].set_title("Halved Current Rate", fontsize = 10)

    # subplot #2 (upper right)- Current Rate
    model2 = SEVIR(initialVaccinationRate) 
    s2, e2, v2, i2, r2 = model2.addCounts()
    daysList2 = model2.getDaysList()
    model2.plot(axs[0][1], daysList2, s2, e2, v2, i2, r2)
    axs[0][1].set_title("Current Rate", fontsize = 10)

    # subplot #3 (lower left)- Doubled Current Rate
    model3 = SEVIR(2 * initialVaccinationRate) 
    s3, e3, v3, i3, r3 = model3.addCounts()
    daysList3 = model3.getDaysList()
    model3.plot(axs[1][0], daysList3, s3, e3, v3, i3, r3)
    axs[1][0].set_title("Doubled Current Rate", fontsize = 10)

    # subplot #4 (lower right)- Quadrupled Current Rate
    model4 = SEVIR(4 * initialVaccinationRate) 
    s4, e4, v4, i4, r4 = model4.addCounts()
    daysList4 = model4.getDaysList()
    model4.plot(axs[1][1], daysList4, s4, e4, v4, i4, r4)
    axs[1][1].set_title("Quadrupled Current Rate", fontsize = 10)

    plt.show()

# run main() if the file is executed properly
if __name__ == "__main__":
    main()
