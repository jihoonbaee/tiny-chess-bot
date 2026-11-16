import os,json,urllib.request as u
V=(0,100,320,330,500,900,0)
KN=(-33,-31,-18,-14,14,18,31,33)
DG=(-17,-15,15,17)
OR=(-16,-1,1,16)
DR=DG+OR
DM={4:3,0:2,7:1,116:12,112:8,119:4}
X=136
P=[[V[a]]*128 for a in range(7)]
for i in range(128):
 f=i&7;r=i>>4;c=min(f,7-f)+min(r,7-r)
 P[1][i]+=7*r;P[2][i]+=6*c;P[3][i]+=4*c;P[5][i]+=2*c;P[4][i]+=3*r;P[6][i]-=2*c
T={};N=0;NP=14;KL=[0]*128;TE=TimeoutError
def at(q,y):
 for o in KN:
  if not(q+o)&X and B[q+o]==2*y:return 1
 for o in DR:
  t=q+o
  while not t&X and not B[t]:t+=o
  if t&X:continue
  b=B[t]
  if b==5*y or b==(3*y if o in DG else 4*y)or t==q+o and(b==6*y or o in DG and o*y<0 and b==y):return 1
 return 0
def ev():return sum(P[p][i]if p>0 else-P[-p][i^112]for i,p in enumerate(B)if p)*s
def gn(cp):
 M=[]
 for f,p in enumerate(B):
  if p*s<=0:continue
  a=abs(p)
  if a==1:
   d=16*s;t=f+d;L=[]
   if not t&X and not B[t]:
    if t>>4 in(0,7)or not cp:L+=[t]
    if not cp and f>>4==1+5*(s<0)and not B[f+2*d]:L+=[f+2*d]
   for o in(d-1,d+1):
    t=f+o
    if not t&X and(B[t]*s<0 or t==E):L+=[t]
   for t in L:
    if t>>4 in(0,7):
     for q in(5,4,3,2):M+=[f+t*128+q*16384]
    else:M+=[f+t*128]
  else:
   for o in(KN,DG,OR,DR,DR)[a-2]:
    t=f+o
    for _ in range(8*(2<a<6)or 1):
     if t&X:break
     if B[t]:M+=[f+t*128]if B[t]*s<0 else[];break
     if not cp:M+=[f+t*128]
     t+=o
 if not cp:
  e=60-56*s
  for k,n in((1,1),(2,-1)):
   b=k<<2*(s<0)
   if C&b and B[e]==6*s and not(B[e+n]or B[e+2*n]or n<0 and B[e+3*n])and all(not at(q,-s)for q in(e,e+n,e+2*n)):M+=[e+(e+2*n)*128]
 return M
def mk(m):
 global C,E,s,NP
 f=m&127;t=(m>>7)&127;q=m>>14;p=B[f]
 w=(B[:],C,E,K[:],NP)
 if p==s and t==E and not B[t]:B[t-16*s]=0
 B[f]=0;c=B[t]
 NP-=1<abs(c)<6
 B[t]=q*s if q else p
 NP+=q>0
 if abs(p)==6:
  K[(1-s)//2]=t
  if abs(t-f)==2:
   rf=t+1 if t>f else t-2;rt=t-1 if t>f else t+1;B[rt]=B[rf];B[rf]=0
 C&=~(DM.get(f,0)|DM.get(t,0))
 E=f+16*s if p==s and abs(t-f)==32 else -1
 s=-s
 return w
def un(w):
 global C,E,s,NP
 B[:],C,E,K[:],NP=w;s=-s
def sr(g,d,p):
 global N,E,s
 N+=1
 if N>1e5:raise TE
 ck=at(K[(1-s)//2],-s)
 d+=ck and d>0
 tm=0
 if d<=0:
  if ck:ms=gn(0);bo=-999999
  else:
   st=ev()
   if st>=g:return st
   ms=gn(1);bo=st
 else:
  k=(tuple(B),C,E,s);e=T.get(k)
  if e:
   tm=e[3]
   if e[0]>=d:
    if e[1]>=g:return e[1]
    if e[2]<g:return e[2]
  if d>2 and not ck and NP>0:
   z=E;E=-1;s=-s;sc=-sr(1-g,d-3,p+1);s=-s;E=z
   if sc>=g:return sc
  ms=gn(0);bo=-999999
 ms.sort(key=lambda m:(m==tm)*9999+(m==KL[p])*5000+10*V[abs(B[(m>>7)&127])],reverse=True)
 bm=0;nl=0
 for m in ms:
  w=mk(m)
  if at(K[(1+s)//2],s):un(w);continue
  nl+=1
  sc=-sr(1-g,d-1,p+1)
  un(w)
  if sc>=g:
   KL[p]=m
   if d>0:T[k]=(d,max(-89e3,min(89e3,sc)),999999,m)
   return sc
  if sc>bo:bo=sc;bm=m
 if not nl:return p-9e4 if ck else 0 if d>0 else st
 if d>0:T[k]=(d,-999999,max(-89e3,min(89e3,bo)),bm)
 return bo
def ch():
 global N
 T.clear()
 ms=gn(0)
 lg=[]
 for m in ms:
  w=mk(m)
  if not at(K[(1+s)//2],s):lg+=[m]
  un(w)
 if len(lg)==1:return lg[0]
 N=0;bm=lg[0];pv=0
 for d in range(64):
  try:
   lo=-9e4;hi=9e4;gm=pv
   while lo<hi:
    sc=sr(gm,d,0)
    if sc>=gm:lo=sc
    else:hi=sc
    gm=(lo+hi+1)//2
   pv=lo
   sr(pv,d,0)
   e=T.get((tuple(B),C,E,s))
   if e and e[3]:bm=e[3]
  except TE:break
 return bm
def ld(mv):
 global B,s,C,E,K,NP
 B=[0]*128;s=1;C=15;E=-1;K=[4,116];NP=14
 for i,v in enumerate(map(int,'42356324')):
  B[i]=v;B[i+16]=1;B[i+96]=-1;B[i+112]=-v
 for o in mv:
  for m in gn(0):
   if nm(m)==o:mk(m);break
def nm(m):
 f=m&127;t=(m>>7)&127;q=m>>14
 return chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)+('nbrq'[q-2] if q else '')
U=os.getenv('MAKEFUN_ENV_URL','')
def po(p,d):return json.load(u.urlopen(u.Request(U+p,data=json.dumps(d).encode())))
def main():
 while 1:
  g=po('/game',{})
  if g.get('status')=='done':return
  if g['status']!='your_move':continue
  L=g.get('legal_moves')or['e2e4']
  try:
   ld(g['moves']);o=nm(ch())
   if o not in L:o=L[0]
  except Exception:o=L[0]
  try:po('/move',{'game':g['game'],'move':o})
  except Exception:pass
if __name__[0]=='_':main()
