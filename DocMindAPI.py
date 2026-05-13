# ─────────────────────────────────────────────────────────────
# DocMind — Validação da API Claude
# ─────────────────────────────────────────────────────────────
# Alterações em relação ao código anterior:
#
# 1. A chave de API saiu do código e foi para o arquivo .env
#    - ANTES: ANTHROPIC_API_KEY = "sk-ant-..." direto no código
#    - DEPOIS: load_dotenv() + os.getenv("ANTHROPIC_API_KEY")
#
# 2. Adicionado o framework LangChain para comunicação com a API
#    - ANTES: anthropic.Anthropic() chamado diretamente
#    - DEPOIS: ChatAnthropic() via langchain_anthropic
#
# 3. Adicionado ChatPromptTemplate para estruturar o prompt
#    - ANTES: mensagem fixa dentro do messages=[...]
#    - DEPOIS: prompt template reutilizável com variável {pergunta}
#
# 4. Criação de uma chain (prompt | llm) conforme padrão LangChain
#    - ANTES: cliente.messages.create(...)
#    - DEPOIS: chain.invoke({"pergunta": ...})
#
# 5. Removida a biblioteca "time" (não necessária com LangChain)
# ─────────────────────────────────────────────────────────────

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
import os

# Carrega a chave do arquivo .env
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if __name__ == "__main__":
    print("=" * 50)
    print("  DocMind — Validação da API Claude")
    print("=" * 50)

    # Configuração do modelo via LangChain
    llm = ChatAnthropic(
        model="claude-sonnet-4-6",
        anthropic_api_key=api_key,
        temperature=0.7
    )

    # Template de prompt reutilizável
    prompt = ChatPromptTemplate.from_template(
        """
        Você é o DocMind, um assistente especializado em análise de documentos PDF.
        Responda sempre em português de forma clara e objetiva.

        Pergunta:
        {pergunta}
        """
    )

# Criação da chain — encadeia o prompt com o modelo (prompt → llm)
chain = prompt | llm
 
# Entrada do usuário
pergunta_usuario = input("Digite sua pergunta: ")
 
# Execução da chain com a pergunta fornecida
resposta = chain.invoke({
    "pergunta": pergunta_usuario
})
 
# Exibe a resposta retornada pela IA
print("\nResposta da IA:\n")
print(resposta.content)
 