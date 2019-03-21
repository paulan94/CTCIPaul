def riverSizes(matrix):
    # Write your code here.
	ans = []
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			if matrix[r][c] == 1:
				length = dfs(matrix,r,c)
				ans.append(length)
	print (ans)
	return ans

def dfs(matrix,r,c):
	height = 1
	print (r,c)
	if (r < 0) or (c < 0) or (r >= len(matrix)) or (c >= len(matrix[0])) or matrix[r][c] == 0:
		return 0
	else:
		matrix[r][c] = 0
		height += dfs(matrix,r+1,c)
		height += dfs(matrix,r-1,c)
		height += dfs(matrix,r,c+1)
		height += dfs(matrix,r,c-1)
		return height


riverSizes([[1,1,1,0,1,1,0,0,0,1,0]])
