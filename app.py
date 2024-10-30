from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Nicolas', 10)
restaurante_praca.receber_avaliacao('Nicolas', 2)

def main():
   Restaurante.listar_restaurantes() 

if __name__ == '__main__':
    main()