#Inheritance Exercise:
class TonyStark:
      def assemble1(IronMan):
          print("The Avenger.I Am IronMan")
 

class MorganStark(TonyStark):
      def assemble2(IronMan):
          print("Tony Daughter.I Love U 3000")
 

class Pepper(TonyStark):
      def assemble3(IronMan):
          print("Tony Wife.Prood That TOny Stark Has a Heart")
  

Averange1 = MorganStark()
Averange2 = Pepper()
Averange1.assemble1()
Averange1.assemble2()
Averange2.assemble3()
