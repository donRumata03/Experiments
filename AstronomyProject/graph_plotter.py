from measurements import *

from matplotlib import pyplot as plt
import matplotlib.dates as mdates


def set_plot_formatter():
	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
	plt.gca().xaxis.set_major_locator(mdates.DayLocator())

def setup_plot_finishing(radians_or_degrees: bool = False):
	plt.title("Sun Angle Dynamic")

	plt.xlabel("Date")
	plt.ylabel(f"Angle, {'radians' if radians_or_degrees else 'degrees'}")

	plt.ylim(bottom=0)

	plt.legend()
	plt.show()


def add_date_data_to_plot(data: List[Tuple], name: str, convert_to_degrees: bool = True):
	all_real_dates = [i[0] for i in data]
	all_real_angles = [i[1] for i in data]

	if convert_to_degrees:
		all_real_angles = [math.degrees(i) for i in all_real_angles]

	plt.scatter(all_real_dates, all_real_angles, label=name + f" ({len(data)} points)")
	plt.gcf().autofmt_xdate()


if __name__ == '__main__':
	set_plot_formatter()

	add_date_data_to_plot(real_data_by_vova, "Vova's data")
	add_date_data_to_plot(real_data_by_andrew, "Andrew's data")
	add_date_data_to_plot(real_data_by_sergey, "Sergey's data")
	add_date_data_to_plot(real_data_by_nikita, "Nikita's data")

	setup_plot_finishing()



