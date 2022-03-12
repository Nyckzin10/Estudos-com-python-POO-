from abc import abstractclassmethod
from random import choice



class Veiculo:
    @abstractclassmethod
    def buscar_cliente(self) -> None: pass



class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Carro de luxo está buscando o cliente')



class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Carro  popular está buscando o cliente')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Moto de luxo está buscando o cliente')



class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Moto popular buscando o cliente')




#criação de classes, para os veiculos, aonde está na base de dados com base symplefactory!


#symplefactory 
class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'Moto_luxo':
            return MotoLuxo()
        if tipo == 'Moto':
            return MotoPopular()
        assert 0, "Veiculo não existe"
       



if __name__ == '__main__':
    carros_disponiveis = ['Popular', 'luxo', 'moto']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()







