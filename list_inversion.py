def list_inverse(matrix):
	transpose = []
	for c in range(0,len(matrix[0])):
		row=[]
		for r in matrix:
			row.append(r[c])
		transpose.append(row)

	return transpose

print(list_inverse([[1,2,3, 'n'],
					[4,5,6, 'n'],
					[7,8,9, 'n']]))
