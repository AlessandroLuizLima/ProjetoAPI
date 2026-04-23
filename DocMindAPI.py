import anthropic
import time

ANTHROPIC_API_KEY = "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"

if __name__ == "__main__":
    print("=" * 50)
    print("  DocMind — Validação da API Claude")
    print("=" * 50)

    cliente = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    print("Conectando à API...")

    inicio = time.time()
    resposta = cliente.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=200,
        messages=[
            {"role": "user", "content": "Responda em português: Qual é o seu nome e o que você pode fazer?"}
        ]
    )
    fim = time.time()

    print(f"\nResposta: {resposta.content[0].text}")
    print(f"\nModelo        : {resposta.model}")
    print(f"Tokens entrada: {resposta.usage.input_tokens}")
    print(f"Tokens saída  : {resposta.usage.output_tokens}")
    print(f"Tempo         : {fim - inicio:.2f}s")

    print("\n" + "=" * 50)
    print("  API funcionando corretamente!")
    print("=" * 50)