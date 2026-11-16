import os,json,urllib.request as u
T={};KL=[0]*512
V=[0,100,320,330,500,900,0]
KN=[14,18,31,33,-14,-18,-31,-33]
DG=[15,17,-15,-17];OR=[1,16,-1,-16];DR=DG+OR
DT=[0,0,KN,DG,OR,DR,DR]
DM={0:2,4:3,7:1,112:8,116:12,119:4}
class TE(Exception):pass
P=[[0]*128 for _ in range(7)]
for i in range(128):
 r=i>>4;f=i&7;a=min(f,7-f);c=a+min(r,7-r)
 P[1][i]=P[4][i]=6*r+2*a
 for j,z in((2,10),(3,8),(5,3),(6,-3)):P[j][i]=z*c
def ld(ms):
 global B,s,C,E,K,NP
 B=[0]*128
 for i,p in enumerate([4,2,3,5,6,3,2,4]):
  B[i]=p;B[i+16]=1;B[i+96]=-1;B[i+112]=-p
 s=1;C=15;E=-1;K=[4,116];NP=14
 for u in ms:mk(next(m for m in gn(0)if nm(m)==u))
def nm(m):
 f=m&127;t=m>>7&127;q=m>>14
 return f'{chr(97+f%8)}{f//16+1}{chr(97+t%8)}{t//16+1}'+('nbrq'[q-2]if q else'')
def gn(q):
 m=[]
 for i,p in enumerate(B):
  if p*s<=0:continue
  a=p*s
  if a==1:
   u=16*s
   for t in(i+u-1,i+u,i+u+1):
    if t&136:continue
    x=B[t]
    if t==i+u:
     if x:continue
     if q and t>>4 not in(0,7):continue
    elif x*s>=0 and t!=E:continue
    if t>>4 in(0,7):
     m+=[i|t<<7|z<<14 for z in(5,4,3,2)]
    else:m.append(i|t<<7)
    if t==i+u and i>>4==1+5*(s<0) and not B[t+u]:m.append(i|(t+u)<<7)
  else:
   D=DT[a]
   for d in D:
    for k in range(1,8*(2<a<6)or 2):
     t=i+d*k
     if t&136:break
     x=B[t]
     if x*s<=0 and(x or not q):m.append(i|t<<7)
     if x:break
   if not q and a==6 and i in(4,116) and not at(i,-s):
    o=i&112;b=C>>2*(s<0)
    if b&1 and not(B[o+5]or B[o+6])and not(at(o+5,-s)or at(o+6,-s)):m.append(i|(o+6)<<7)
    if b&2 and not(B[o+1]or B[o+2]or B[o+3])and not(at(o+3,-s)or at(o+2,-s)):m.append(i|(o+2)<<7)
 return m
def at(t,u):
 for d in DR:
  for k in range(1,8):
   x=t+d*k
   if x&136:break
   y=B[x]
   if y:
    if y==5*u or y==(3+(d in OR))*u or(k==1 and(y==u and d*u<0 and d in DG or y==6*u)):return 1
    break
 for d in KN:
  x=t+d
  if not x&136 and B[x]==2*u:return 1
def mk(m):
 global s,C,E,NP
 f=m&127;t=m>>7&127;q=m>>14;p=B[f];c=B[t];e=abs(p)==1 and t==E and not c
 if e:c=B[t-16*s];B[t-16*s]=0
 w=(m,c,C,E,NP,t-16*s*e)
 B[t]=q*s if q else p;B[f]=0
 if abs(p)==6:
  K[s<0]=t
  if t-f==2:B[t-1]=B[t+1];B[t+1]=0
  elif f-t==2:B[t+1]=B[t-2];B[t-2]=0
 if c and 1<abs(c)<6:NP-=1
 if q:NP+=1
 C&=~DM.get(f,0)&~DM.get(t,0)
 E=t-16*s if abs(p)==1 and abs(t-f)==32 else -1
 s=-s
 return w
def un(w):
 global s,C,E,NP
 m,c,C,E,NP,cs=w
 s=-s;f=m&127;t=m>>7&127;q=m>>14;p=B[t]
 B[f]=s if q else p
 B[cs]=c;B[t]=0 if cs!=t else c
 if abs(p)==6:
  K[s<0]=f
  if t-f==2:B[t+1]=B[t-1];B[t-1]=0
  elif f-t==2:B[t-2]=B[t+1];B[t+1]=0
def ev():return s*sum((V[abs(p)]+P[abs(p)][i^112*(p<0)])*((p>0)*2-1)for i,p in enumerate(B)if p)
def sr(g,d,p):
 global N,s,E
 N+=1
 if N>100001:raise TE
 k=(tuple(B),C,E,s);e=T.get(k)
 if e and e[0]>=d and(e[2]>=g)==e[1]:return e[2]
 tm=e[3]if e else 0
 ck=at(K[s<0],-s)
 if d<=0 and not ck:
  b=ev()
  if b>=g:return b
  ms=gn(1)
 else:
  b=-9e4;ms=gn(0)
 if d>2 and p and not ck and NP>0:
  s=-s;x=E;E=-1;c=-sr(1-g,d-3,p+1);s=-s;E=x
  if c>=g:return c
 ms.sort(key=lambda m:(m==tm)*9999+(m==KL[p])*5000+10*V[abs(B[m>>7&127])],reverse=1)
 bm=0;f=0
 for m in ms:
  w=mk(m)
  if at(K[s>0],s):un(w);continue
  f=1;c=-sr(1-g,d-1,p+1);un(w)
  if c>b:b=c;bm=m
  if c>=g:
   KL[p]=m
   if d>0:T[k]=(d,1,c,m)
   return c
 if not f:return p-90000 if ck else b*(d<=0)
 if d>0:T[k]=(d,b>=g,b,bm)
 return b
def ch():
 global N
 T.clear();KL[:]=[0]*512
 ms=gn(0);lg=[]
 for m in ms:
  w=mk(m)
  if not at(K[s>0],s):lg.append(m)
  un(w)
 if len(lg)==1:return nm(lg[0])
 N=0;bm=lg[0];v=0
 for d in range(64):
  try:
   lo=-9e4;hi=9e4;g=v
   while lo<hi:
    c=sr(g,d,0)
    if c>=g:lo=c
    else:hi=c
    g=(lo+hi+1)//2
   v=lo;sr(v,d,0)
   e=T.get((tuple(B),C,E,s))
   if e and e[3]:bm=e[3]
  except TE:break
 return nm(bm)
def post(p,o):
 return json.load(u.urlopen(U+p,json.dumps(o).encode()))
def main():
 global U
 U=os.getenv('MAKEFUN_ENV_URL')
 while 1:
  g=post('/game',{})
  if g['status']=='done':return
  while g['status']=='your_move':
   ld(g['moves']);g=post('/move',{'game':g['game'],'move':ch()})
if __name__[0]=='_':main()
