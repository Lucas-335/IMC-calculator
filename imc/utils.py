class Imc():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def imc_calculated(self):
        weight_ = self.weight
        height_ = self.height
        imc =  round(weight_/(height_*height_),2)
        
        if imc < 16:
            return f'{imc} - magreza grave'
        elif imc >= 16 and imc < 17:
            return f'{imc} - magreza moderada'
        elif imc >= 17 and imc < 18.6:
            return f'{imc} - magreza leve'
        elif imc >= 18.6 and imc < 25:
            return f'{imc} - peso ideal'
        elif imc >= 25 and imc < 30:
            return f'{imc} - sobrepeso'
        elif imc >= 30 and imc < 35:
            return f'{imc} - obesidade grau 1'
        elif imc >= 35 and imc < 40:
            return f'{imc} - obesidade severa (grau 2)'
        else:
            return f'{imc} - obesidade mórbida (grau 3)'