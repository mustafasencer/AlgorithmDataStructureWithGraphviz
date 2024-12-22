a = [["9:00", "10:30"], ["12:00", "13:00"], ["14:30", "18:00"]]
a1 = ["9:00", "20:00"]
b = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
b1 = ["10:00", "18:30"]
duration = 30

merged = [
	["9:00", "11:30"],
]


def solve(a, b, a1, b1, duration):
	merge_unavailables(a, b)


def merge_unavailables(a, b):
	merged_unavailable_times = []
	i = 0
	j = 0
	while i < len(a) or j < len(b):
		if compare_times(a[i][0], b[j][0]) == -1:
			if compare_times(a[i][1], b[j][0]) == 1:
				merged_unavailable_times.append([a[i][0], b[j][1]])
				i += 1
			else:
				j += 1
		else:
			if compare_times(b[i][1], a[j][0]) == -1:
				merged_unavailable_times.append([b[i][0], a[j][1]])
				j += 1
			else:
				i += 1


def compare_times(time_1, time_2):
	hour_1, minutes_1 = time_1.split(":")
	hour_2, minutes_2 = time_2.split(":")

	time_1_final = int(hour_1) * 60 + int(minutes_1)
	time_2_final = int(hour_2) * 60 + int(minutes_2)
	if time_1_final > time_2_final:
		return 1
	elif time_1_final == time_2_final:
		return 0
	else:
		return -1
