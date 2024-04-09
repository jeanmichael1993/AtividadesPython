class Televisao:
    def __init__(self):
        self.volume = 50  # volume padrão
        self.canal = 1    # canal padrão

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def aumentar_canal(self):
        self.canal += 1

    def diminuir_canal(self):
        if self.canal > 1:
            self.canal -= 1

    def trocar_canal(self, novo_canal):
        self.canal = novo_canal

    def consultar_volume(self):
        return self.volume

    def consultar_canal(self):
        return self.canal


class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao

    def aumentar_volume(self):
        self.televisao.aumentar_volume()

    def diminuir_volume(self):
        self.televisao.diminuir_volume()

    def aumentar_canal(self):
        self.televisao.aumentar_canal()

    def diminuir_canal(self):
        self.televisao.diminuir_canal()

    def trocar_canal(self, novo_canal):
        self.televisao.trocar_canal(novo_canal)

    def consultar_volume(self):
        return self.televisao.consultar_volume()

    def consultar_canal(self):
        return self.televisao.consultar_canal()



tv = Televisao()
controle = ControleRemoto(tv)

print("Volume atual:", controle.consultar_volume())
print("Canal atual:", controle.consultar_canal())

controle.aumentar_volume()
controle.aumentar_volume()
controle.diminuir_volume()

print("Volume atual:", controle.consultar_volume())
controle.aumentar_canal()
controle.aumentar_canal()
controle.trocar_canal(5)

print("Canal atual:", controle.consultar_canal())
