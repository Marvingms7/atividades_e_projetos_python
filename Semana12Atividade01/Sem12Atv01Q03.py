from operator import itemgetter

def carregar(arquivo):
    linhas = []
    with open(arquivo) as f:
        f.readline()
        for linha in f.readlines():
            data, abertura, alta, baixa, fechamento, volume = linha.strip().split(',')
            ano, mes, dia = data.split('-')
            linhas.append(
                {
                    "ano": int(ano),
                    "mes": int(mes),
                    "dia": int(dia),
                    "abertura": float(abertura),
                    "alta": float(alta),
                    "baixa": float(baixa),
                    "fechamento": float(fechamento),
                    "volume": int(volume),
                }
            )
    return linhas


def formatar_data(linha):
    meses = (
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    )
    d, m, a, = linha['dia'], linha['mes'], linha['ano']
    return f'{d:0>2d} de {meses[m - 1]} de {a}'


def media_volume(a, b, c):
    soma = cont = 0
    ordenado = sorted(a, key=itemgetter('ano', 'mes', 'dia'))
    for i in ordenado:
        if i['mes'] == b and i['ano'] == c:
            soma += i['volume']
            cont += 1
    media = soma / cont
    return media

def main():
    # Carregar os dados da empresa a partir do arquivo csv
    a_carregar = input("Digite o nome do arquivo.csv que deseja abrir: ").strip()
    mes = int(input("Digite o mês em que seja saber a media do volume: "))
    ano = int(input("Digite o ano em que seja saber a média do volume: "))
    abev3 = carregar(a_carregar)
    # Mostra o volume médio com base no mês e ano lido
    media_v = media_volume(abev3, mes, ano)
    print(f'O volume médio em {mes}/{ano} foi {media_v:.0f}')


if __name__ == '__main__':
    main()