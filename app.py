"""Align fictional transcript and protein measurements using a regularized canonical-correlation projection."""
from kit import *
TITLE='Paired Multi-Omics Latent Alignment'
LIVE=False

def invsqrt(matrix):
    values,vectors=np.linalg.eigh(matrix);return (vectors/np.sqrt(np.maximum(values,1e-10)))@vectors.T
def fit(x,y,k=4,reg=.1):
    mx=x.mean(axis=0);my=y.mean(axis=0);xx=x-mx;yy=y-my;n=len(x)-1;wx=invsqrt(xx.T@xx/n+reg*np.eye(x.shape[1]));wy=invsqrt(yy.T@yy/n+reg*np.eye(y.shape[1]));u,s,vt=np.linalg.svd(wx@(xx.T@yy/n)@wy,full_matrices=False);return dict(mx=mx,my=my,px=wx@u[:,:k],py=wy@vt.T[:,:k])
def normalize_rows(x):return x/np.maximum(np.linalg.norm(x,axis=1,keepdims=True),1e-12)
def run(d,a):
    rng=np.random.default_rng(a.seed);z=rng.normal(size=(650,4));x=z@rng.normal(size=(4,24))+rng.normal(0,.15,(650,24));y=z@rng.normal(size=(4,16))+rng.normal(0,.15,(650,16));m=fit(x[:500],y[:500]);ex=normalize_rows((x[500:]-m['mx'])@m['px']);ey=normalize_rows((y[500:]-m['my'])@m['py']);p=(ex@ey.T).argmax(axis=1)
    return dict(test_pair_retrieval_accuracy=float(np.mean(p==np.arange(150))),chance_accuracy=1/150,training_pairs=500,test_pairs=150,method='Regularized linear CCA; held-out pair matching'),dict(**m,transcript_embedding=ex,protein_embedding=ey)

if __name__=="__main__":main(run)
