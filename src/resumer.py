from transformers import pipeline
"""
python3 -m pip install tensorflow[and-cuda]
# Verify the installation:
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
"""


summarizer = pipeline(
    "summarization",
    model="neuralmind/bert-large-portuguese-cased",
    tokenizer="neuralmind/bert-large-portuguese-cased"
    )

texto = """
Em todas as disciplinas e áreas do conhecimento, seja ela exata, humana ou biológica, é de fundamental importância o estudo investigativo dos primeiros pensadores de determinado assunto, bem como de suas respectivas teorias, princípios, fórmulas, etc, pois os estudos destes pioneiros são a base estrutural do conhecimento atual e o primeiro degrau de apoio para que novos pesquisadores possam se amparar nestas teorias e propor outras mais avançadas e adequadas ao contexto atual.

No estudo investigativo, os pesquisadores encontrarão desde teorias complementares obsoletas e inadequadas às necessidades atuais até teorias intactas e perfeitamente aplicáveis, passando por outras que devem apenas serem aperfeiçoadas. 

Na disciplina de Administração não é diferente devido ao infinito leque de autores que contribuíram à constituição da Teoria Geral da Administração. Dentro da Teoria Geral da Administração, existe uma divisão chamada Teoria Clássica da Administração formada pela Teoria da Administração Científica (Frederick Taylor), Teoria Administrativa (Henri Fayol) e Teoria da Burocracia (Max Weber).

Henri Fayol, engenheiro educado na França, foi o maior teórico da perspectiva clássica, introduziu as funções da administração, aceitas e aplicadas atualmente no mundo todo e escreveu os Princípios Gerais da Administração, que são o tema desta pesquisa.

O problema de pesquisa deste artigo é tentar avaliar portanto, através do método de pesquisa bibliográfica : Qual é a aplicabilidade dos princípios de Fayol na administração moderna ? Ou seja, verificar se estes princípios podem ser aplicados atualmente e caso o sejam, em que proporção devem ser utilizados.

Tem-se como objetivo verificar se o fayolismo é obsoleto ou aplicável e a justificativa para este trabalho é explicada pelo fato de ser um tema muito interessante e discutido entre pesquisadores no meio acadêmico do mundo todo,além do que pode ser de grande utilidade a gestores e futuros gestores administrativos que certamente deverão utilizar estes princípios em busca da eficiência e da eficácia nos processos de administração material e humana.
"""

resumo = summarizer(
    texto,
    max_length=130,
    min_length=30,
    length_penalty=2.0,
    num_beams=4,
    do_sample=False
)
print(resumo[0]['summary_text'])

