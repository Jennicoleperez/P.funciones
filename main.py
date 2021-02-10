def combinatoria (n,k):
  """devuelve la combinatoria de n en k 
  $\frac{n!}{k!(n-k)!}$

  Arguments:
    n {Int} -- La cardinalidad del conjunto 
    k {Int} -- La cardinalidad del subconjunto 
  """
  n_fact = 1
  for num in range(1, n+1):
    n_fact *= num
  
  k_fact = 1
  for num in range(1, k+1):
    k_fact *= num

  n_k_fact = 1
  for num in range(1, (n-k)+1):
    n_k_fact *= num
 


  