def guardar_data_atual() -> str:
    """
    Função que guarda a data atual
    :return: Data forma textual
    """
    try:
        dia: int = int(input("Digite o dia atual: "))
        mes: int = int(input("Digite o mês atual: "))
        ano: int = int(input("Digite o ano atual: "))
    except ValueError as error:
        print("Valor errado!")
    except (TypeError, IndexError) as errors:
        print(TypeError, IndexError)
    else:
        if mes < 10:
            mes = "0"+str(mes)
        return str(str(dia)+"/"+str(mes)+"/"+str(ano))
    finally:
        print("Fim!")


def imprimir_data(data_atual: str):
    """
    Função para imprimir data atual
    :param data_atual: valor string com a data atual
    """
    mes: str = '02'
    dia, mes, ano = data_atual.split('/')
    mes_texto: str = ''
    match mes:
        case '01':
            mes_texto = 'Janeiro'
        case '02':
            mes_texto = 'Fevereiro'
        case '03':
            mes_texto = 'Março'
        case '04':
            mes_texto = 'Abril'
        case '05':
            mes_texto = 'Maio'
        case '06':
            mes_texto = 'Junho'
        case '07':
            mes_texto = 'Julho'
        case '08':
            mes_texto = 'Agosto'
        case '09':
            mes_texto = 'Setembro'
        case '10':
            mes_texto = 'Outubro'
        case '11':
            mes_texto = 'Novembro'
        case '12':
            mes_texto = 'Dezembro'
    print(f'{dia} de {mes_texto} de {ano}')


if __name__ == "__main__":
    data_atual: str = guardar_data_atual()
    imprimir_data(data_atual)

