
# coding: utf-8

# Implémentation de l'algorithme Sliding Window modifié afin de minimiser les précalcules.

# In[1]:


from math import log


# In[2]:


# wrapper de la fonction principale
def minProd(K):
    
    s = 3  # = ch(1)==0 + ch(2)==1 + ch(3)==2
    
    # on calcule a partir de 4 qui est le premier exemple non trivial
    for n in range(4, K+1) :
        smalest = float('inf') # afin de pouvoir comparer initialament    
        
        for k in range(1, int( log(n, 2) )+1 ):
            if smalest > sliding_window(n=n, k=k) :
                smalest = sliding_window(n=n, k=k)
        s = s + smalest

    return s


# In[3]:


# la methode necessite un parametre k que l'on determine par brute force
def sliding_window(n, k):

    # chaine d'exponenentiel de depart
    odd_pow = {1:2, 2:4}

    # convertion vers base 2
    m = bin(n)
    m = m[2:]
    m = m[::-1]

    # variable de la boucle
    X, i, ch_len = 1, len(m)-1, 0

    # lecture de droite a gauche du chiffre qui sera inverser par la suite
    while i > -1 :
        
        if m[i] == '1' :
            
            # retention de la plus longue sequence
            for a in range(k) :

                # evite le choix d'un indexe < 0
                if i-a > 0 :
                    b = i-a
                else :
                    b = 0

                if m[b] == '1' :
                    window = m[ b:i+1 ]
                    c = b

            # remise de la sequence dans l'ordre initiale
            window = window[::-1]

            # mise au carre
            for _ in range(i-c+1):
                X = X**2
            
            # ne compte pas la mise au carre si celle-ci est appliquer a X > 1
            if X > 1 :
                ch_len += i-c+1
            
            # ne calcule que les expos impaires demandes
            while int(window, 2) not in odd_pow :
                i = len(odd_pow)-1
                odd_pow[2*i+1] = odd_pow[2*i-1]*2

            # n'effectur pas la multiplication si le 2eme terme egale 1
            if odd_pow[ int(window, 2) ] > 1 :

                # si X == 1 la multiplication est effectuee mais non comptabiliser
                if X > 1 :
                    ch_len += 1

                X = X*odd_pow[ int(window, 2) ]
            
            i = c-1
    
        else : 
            X, ch_len, i = X*X, ch_len+1, i-1

    ch_len += len(odd_pow)-1  # on ajoute le nombre de precalcules effectuees
    return ch_len


# In[4]:


# Execution
a = 200
print( "Sommes des chaines d'exponentiations a l'aide de l'algorithme sliding window, pour borne sup =", a ,":", minProd(K=a) )

