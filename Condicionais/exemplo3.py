temperatura = float(input("Digite a temperatura: "))

if temperatura >= 30:
    print("""- Baianos vão a praia, dançam, cantam e comem acarajé.
          - Cariocas vão a praia e jogam futevolei.
          - Mineiros comem um “queijin” na sombra.
          - Todos os paulistas vão para Praia Grande e enfrentam 2 horas de fila nas padarias e supermercados da região.
          - Gaúchos esgotam os estoques de protetor solar e isotônicos da cidade.""")

elif temperatura <30 and temperatura >= 25:
    print("""- Baianos não deixam os filhos sairem ao vento após as 17 horas.
          - Cariocas vão à praia mas não entram na água.
          - Mineiros comem um feijão tropeiro.
          - Paulistas fazem churrasco nas suas casas do litoral, poucos ainda entram na água.
          - Gaúchos reclamam do calor e não fazem esforço devido esgotamento físico.""")

elif temperatura < 25 and  temperatura >=15:
    print("""- Baianos tremem incontrolavelmente de frio.
- Cariocas se reúnem para comer fondue de queijo.
- Mineiros continuam bebendo pinga perto do fogão a lenha.
- Paulistas ainda estão presos nos congestionamentos na volta do litoral.
- Gaúchos dirigem com os vidros abaixados.
          """)

elif temperatura <15 and temperatura >= 10:
    print  ("""- Decretado estado de calamidade na Bahia.
- Cariocas usam sobretudo, cuecas de lã, luvas e toucas.
- Mineiros continuam bebendo pinga e colocam mais lenha no fogão.
- Paulistas vão a pizzarias e shopping centers com a família.
- Gaúchos botam uma camisa de manga comprida.""")

elif temperatura < 10 and temperatura >=5:
    print("""- Bahia entra no armagedon.
- César Maia lança a candidatura do Rio para as olimpíadas de inverno.
- Mineiros continuam bebendo pinga e quentão ao lado do fogão a lenha.
- Paulistas lotam hospitais e clínicas devido doenças causadas pela inversão térmica.
- Gaúchos fecham as janelas de casa.""")
    
elif temperatura <5:
    print (""" - Não existe mais vida na Bahia. Nem animal, nem vegetal, nem mineral.
- No Rio, César Maia veste 7 casacos e lança o “Ixxnoubórdi in Rio”.
- Mineiros entram em coma alcoólico ao lado do fogão a lenha.
- Paulistas não saem de casa e dão altos índices de audiência a Gilberto Barros, Gugu Liberato, Luciana Gimenes e Silvio Santos.
- Gaúchos aproveitam o friozinho pra assar uma carne no quintal de casa.""")
