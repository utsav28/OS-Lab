def path(mat,i,j,m,n):
    down = right = True
    if i==m-1 and j==n-1:
        return True
    
    if i<m-1 and j<n-1 and mat[i+1][j]==0 and mat[i][j+1] ==0 :
        return False

    if i<m-1 and mat[i+1][j]==1:
        if path(mat,i+1,j,m,n):
            return True
        
    if j<n-1 and mat[i][j+1]==1 :
        if path(mat,i,j+1,m,n):
            return True
    return False
            
arr = [[1,1,1,1],
       [1,0,1,0],
       [1,1,1,0],
       [1,1,1,1]]
print(arr)
if path(arr,0,0,4,4):
    print ("Path Exists")
else:
    print ("Path doesn't exist")
