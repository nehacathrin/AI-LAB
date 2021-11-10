# 8 puzzle iterative dfs method
src=[1,2,3,-1,4,5,6,7,8]
target=[1,2,3,4,5,-1,6,7,8]

def idfs(src,target,depth):
  for limit in range(0,depth+1):
    vis=[]
    if dfs(src,target,limit,vis):
      return True
  return False

def gen(state,m,b):
  temp=state[:]
  if m=='l':
    temp[b],temp[b-1]=temp[b-1],temp[b]
  if m=='r':
    temp[b],temp[b+1]=temp[b+1],temp[b]
  if m=='u':
    temp[b],temp[b-3]=temp[b-3],temp[b]
  if m=='d':
    temp[b],temp[b+3]=temp[b+3],temp[b]

  return temp

def possible_move(state,vis):
  b=state.index(-1)
  dir=[]
  move=[]
  if b<=5:
    dir.append('d')
  if b>=3:
    dir.append('u')
  if b%3>0:
    dir.append('l')
  if b%3<2:
    dir.append('r')
  
  for i in dir:
    temp=gen(state,i,b)
    if not temp in vis:
      move.append(temp)

  print(move)
  return move

def dfs(src,target,limit,vis):
  if src==target :
    return True
  if limit<0 :
    return False
  vis.append(src)
  move=possible_move(src,vis)
  for m in move :
    if dfs(m,target,limit-1,vis):
      return True
  return False


print(idfs(src,target,1))