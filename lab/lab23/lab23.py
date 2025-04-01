import matplotlib.pyplot as plt


def get_scores():
    with open("admission_algorithms_dataset.csv", "r") as file:
        data = file.readlines()
        i = 1
        values = []
        while i < len(data):
            values.append(data[i].split(","))
            i += 1

        sat = []
        for value in values:
            sat.append(float(value[1]))

        gpa = []
        for value in values:
            gpa.append(float(value[2]))

        return sat, gpa


def get_spectra(filename):
    with open(filename, "r") as file:
        data = file.readlines()
        i = 0
        values = []
        while i < len(data):
            values.append(data[i].split())
            i += 1

        wavelength = []
        for value in values:
            wavelength.append(float(value[0]))

        flux = []
        for value in values:
            flux.append(float(value[1]))

        return wavelength, flux


def plot_histogram():
    sat, gpa = get_scores()

    plt.hist(sat)
    plt.savefig("sat_score.png")
    plt.clf()

    plt.hist(gpa)
    plt.savefig("gpa.png")
    plt.clf()


def plot_scatter():
    sat, gpa = get_scores()

    plt.scatter(gpa, sat)
    plt.savefig("correlation.png")
    plt.clf()


def plot_spectra():
    wavelength1, flux1 = get_spectra("spectrum1.txt")
    wavelength2, flux2 = get_spectra("spectrum2.txt")

    plt.plot(wavelength1, flux1, 'b')
    plt.plot(wavelength2, flux2, 'g')
    plt.savefig("spectra.png")
    plt.clf()


def main():
    # plot_histogram()
    # plot_scatter()
    # plot_spectra()
    pass

if __name__ == "__main__":
    main()
