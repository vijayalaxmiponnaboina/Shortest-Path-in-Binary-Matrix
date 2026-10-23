from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        ans=1

        # edge case
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return -1

        q.append((0,0))
        grid[0][0]=1
        while q:

            size=len(q)
            for i in range(size):
                i,j=q.popleft()

                if i==m-1 and j==n-1:
                    return ans

                # UP
                if i-1>=0 and grid[i-1][j]==0:
                    q.append((i-1,j))
                    grid[i-1][j]=1

                # DOWN
                if i+1<m and grid[i+1][j]==0:
                    q.append((i+1,j))
                    grid[i+1][j]=1

                # LEFT
                if j-1>=0 and grid[i][j-1]==0:
                    q.append((i,j-1))
                    grid[i][j-1]=1

                # RIGHT
                if j+1<n and grid[i][j+1]==0:
                    q.append((i,j+1))
                    grid[i][j+1]=1
                
                # TOP_LEFT
                if i!=0 and j!=0 and grid[i-1][j-1]==0:
                    q.append((i-1,j-1))
                    grid[i-1][j-1]=1

                # TOP_RIGHT
                if i>0 and j+1<n and grid[i-1][j+1]==0:
                    q.append((i-1,j+1))
                    grid[i-1][j+1]=1

                # BOTTOM_LEFT
                if j>0 and i+1<m and grid[i+1][j-1]==0:
                    q.append((i+1,j-1))
                    grid[i+1][j-1]=1

                # BOTTOM_RIGHT
                if i+1<m and j+1<n and grid[i+1][j+1]==0:
                    q.append((i+1,j+1))
                    grid[i+1][j+1]=1
            ans+=1
        return -1