
# coding: utf-8

# On teste tous les sous-ensembles possible dans l'interval fourni. Cependant, afin d'optimiser le processus nous eliminant certains éléments qui sont clairement non utile et ne donnerai que des combinaisons dont le produit n'est pas un carré parfait.

# In[1]:


def premier(limit):
    # determine les nombre premier contenu dans un interval donner a l'aide du crible d'Erasthosten
    a = [True] * limit
    a[0: 1] = [False, False]

    # tous les nombres multiple d'un nombre premier reçoivent False
    for i, is_prime in enumerate(a):
        if is_prime:
            # yield est l'equivalent de return mais permet de gagner de l'espace en ram
            yield i
            for n in range(i*i, limit+1, i):
                a[n] = False


# In[2]:


def power(a):
    # produit l'ensemble de tous les sous ensemble d'une collection
    result = [[]]
    for elem in a:
        result.extend([x + [elem] for x in result])
    
    # le premier element i.e l'ensemble vide est eliminer
    return result[1:]


# In[3]:


def C(a,b):
    I = range(a, b+1)
    primes = list( premier(b) )

    # elimine les nombres premier qui n'apparaissent au dela de b/2 qand a < b/2
    if b > 2*a :
        p = [ i for i in primes if i > b//2 ]
        I = list( set(I) - set(p) )
    
    # elmine tous les nombre premier et composite dont au moins un facteur ne se repete pas dans l'interval
    else :
        p = [ i for i in primes if i > a ]
        I = list( set(I) - set(p) )
        
        q = [ i for i in primes if i > b-a and i < a ]
        
        for q_ in q :
            e = (b//q_)*q_
            I = list( set(I) - set([e]) ) 

    T = 0
    
    # calcule des produits de chaque sub_set et verifie si sa racine carré est un entier
    for s in power(I):
        produit = 1

        for i in s :
            produit = produit * i

        sq = produit**(1/2)
        if sq%1 == 0 :
            T += 1

    print("Nombre de carrés parfait formés a partir de l'interval fournie =", T)


# In[4]:


C(40, 55)

