V1: Modelo Monolítico (Rascunho)
Inicialmente, as Unidades Curriculares (UC) estavam presas a uma única Licenciatura através de uma ForeignKey.
•	Problema: Redundância extrema se quisesse adicionar outra licenciatura do DEISI que partilhasse a mesma cadeira.
V2: Modelo Relacional Flexível (Atual)
Introdução de relações ManyToManyField entre Licenciatura e UC, e entre Projeto e Tecnologia.
•	Melhoria: O modelo passou a refletir a realidade académica da Universidade Lusófona, onde as UCs são transversais a vários cursos.


Justificação das Decisões de Modelação
Licenciatura
1.	Relação com UCs: Definida como ManyToManyField porque as UCs são módulos reutilizáveis entre diferentes licenciaturas do departamento.
Unidades Curriculares (UC)
1.	Imagem por UC: Inclusão de um campo de imagem para que cada cadeira tenha uma identidade visual no portfólio, facilitando a navegação.
2.	Relação com Projetos: em que uma unidade curricular pode ter vários projetos mas cada projeto só pertence a uma unidade curricular
Projetos
1.	Campo GitHub URL: Definido como obrigatório. Justificação: Como portfólio de engenharia, o código é a prova principal da competência do aluno.
2.	Conceitos Aplicados: Campo de texto longo para justificar a nota e demonstrar que os objetivos pedagógicos da UC foram atingidos no projeto.
Tecnologias
1.	Nível de Interesse: Criado um ranking de 1 a 5 para que o recrutador perceba quais as tecnologias em que o aluno quer focar a sua carreira.
2.	Logótipo e Site: Atributos incluídos para profissionalizar a apresentação visual e fornecer contexto externo sobre a ferramenta.
TFCs
1.	Modelação via JSON: A estrutura foi planeada para ser compatível com o formato JSON de 2025, facilitando a importação em massa de dados de finalistas.
2.	Destaque de Interesse: Campo booleano para permitir que certos TFCs apareçam na "homepage" do portfólio.
Making Of
1.	Campo uso_ia: Decisão ética de documentar como ferramentas como o Gemini ajudaram na estruturação da base de dados.
2.	Ligação à UC: O Making Of está relacionado com as UCs para contextualizar as dificuldades técnicas sentidas em cada etapa do curso.

Ajuste do Modelo TFC e Making Of

Decisão: Expansão do modelo TFC para incluir campos de autor e orientador. Justificação: A estrutura JSON de 2025 fornecida contém metadados específicos que são cruciais para a catalogação académica, permitindo filtrar trabalhos por orientador ou ano de conclusão

Desafio nas Migrações: Ao adicionar novos atributos ao modelo TFC, surgiu um erro de "non-nullable field". Resolução: Foi aplicada uma solução de "one-off default" (valor vazio) via terminal para garantir que os registos existentes na base de dados não impedissem a atualização da estrutura. Esta experiência reforçou a importância de definir blank=True em campos opcionais.

Após analisar os dados da API da Lusófona, decidi incluir os campos objetivos e area_cientifica no modelo UnidadeCurricular. Isto permite que o portfólio forneça um contexto académico rigoroso sobre o que foi estudado em cada disciplina, enriquecendo a apresentação das competências adquiridas.

Evolução da Modelação e Dados:
•	Refinamento de Projetos: Adicionei o campo repositorio ao modelo Projeto para permitir que o visitante aceda diretamente ao código-fonte no GitHub.
•	Categorização de Tecnologias: Criei um campo de categoria nas Tecnologias para organizar melhor o portfólio entre linguagens, frameworks e ferramentas de devops.
•	Justificação: Esta estrutura permite uma navegação mais intuitiva e profissional, demonstrando organização técnica.
