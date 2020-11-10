from measurements import *

from matplotlib import pyplot as plt
import matplotlib.dates as mdates

if __name__ == '__main__':
	all_real_dates = [i[0] for i in all_real_data]
	all_real_angles = [i[1] for i in all_real_data]

	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	plt.plot(all_real_dates, all_real_angles)
	plt.gcf().autofmt_xdate()

	plt.title("Sun Angle Dynamic")

	plt.xlabel("Date")
	plt.ylabel("Angle, radians")

	plt.show()


