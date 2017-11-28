freqs = [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88]
carnatic_keys = ['S', 'r', 'R', 'g', 'G', 'm', 'M', 'P', 'd', 'D', 'n', 'N']
shifts = {
	'C': 0,
	'C#': 1,
	'D': 2,
	'D#': 3,
	'E': 4,
	'F': 5,
	'F#': 6,
	'G': 7,
	'G#': 8,
	'A': 9,
	'A#': 10,
	'B': 11
}
connections = {
	('S', 'r'): ['r', 'S,r'],
	('S', 'R'): ['R', 'SGR'],
	('S', 'g'): ['g', 'SmR', 'mg,'],
	('S', 'G'): ['G', 'SPG'],
	('S', 'm'): ['m', 'Sm,'],
	('S', 'M'): ['M', 'SPM'],
	('S', 'P'): ['P', 'SP,'],
	('S', 'd'): ['d', 'Sd,'],
	('S', 'D'): ['D', 'DPD,', 'SS*D,'],
	('S', 'n'): ['n', 'Sn,'],
	('S', 'N'): ['N', 'SN,'],
	('S', 'S*'): ['S*', 'SS*,']
}