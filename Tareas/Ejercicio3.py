"""
Ejercicio 03. Crear las siguientes funciones:
  Los humanos tienen 10 bases
  Los marcianos atacan 1 base a la vez
  Las bases no pueden ser atacadas mas de una vez
  attack(3) -> Destruir la base 3
  attack(5) -> Destruir la base 5
  game_over() -> False, quedan las bases 1 2 4 6 7 8 9 10
  attack(1)
  attack(2)
  attack(10)
  attack(8)
  game_over() -> False, quedan las bases 4 6 7 9
  attack(4)
  attack(6)
  attack(7)
  attack(9)
  game_over() -> True
  El objetivo es implementar dichas funciones
  Por último:
  attack(3.5) -> Atacaria la mitad de la base 3
  attack(4.2) -> Atacando el 20% de la base 4 y queda el 80%
  attack(4.6) -> Atacando el 60% de la base 4 y queda el 20%
  attack(4.2) -> Destruyo la base 4
  attack(5) -> Destruye al 100% la base 5
"""
bases = [1,2,3,4,5,6,7,8,9,10]

while (len(bases)) <= 10 and (len(bases)) != 0:
  print ("ingresa la base a atacar :")
  base_atacar=input ()
  
  def game_over(bases):
    if len(bases) != 0:
      return ("False, quedan {}".format(bases))
    else:
      return ("True")
  
  def attack (bases,base_atacar):
    bases.remove(base_atacar)
    return bases

  if base_atacar == "game_over":
    print (game_over(bases))
  elif int(base_atacar) in bases:
    base_atacar=int(base_atacar)
    attack(bases,base_atacar)
  else:
    print ("La base no existe o ya fue eliminada")

if (len(bases)) == 0:
  print ("Juego finalizado")  
