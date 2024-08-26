from llama_cpp import Llama

# Path to your local model file
model_path = "D:\Python\gpt_query/openchat-3.6-8b-20240522-Q6_K.gguf"
model_path2 = "D:\Python\gpt_query/codeninja-1.0-openchat-7b.Q4_K_M.gguf"

# Load the model with llama-cpp-python
llm = Llama(model_path=model_path2, n_ctx= 4096, n_gpu_layers = 32, n_threads=4,split_mode=4, verbose=True)

def generate_text(
    prompt="2+2*2=",
    max_tokens=256,
    temperature=0.1,
    top_p=0.5,
    echo=False,
    stop=["#"],
):
    output = llm(
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        echo=echo,
        stop=stop,
    )
    output_text = output["choices"][0]["text"].strip()
    return output_text

def generate_prompt_from_template(input):
    chat_prompt_template = f"""system
Ты - мудрая и опытная гадалка, способная предсказывать будущее. Твоя задача - дать одно четкое и конкретное предсказание на завтрашний день для того, кто читает это сообщение. Предсказание должно быть понятным, позитивным и полезным. Важно, чтобы оно звучало как настоящее пророчество от гадалки.

Пожалуйста, начни своё предсказание с фразы: 'Завтра тебя ожидает...', и продолжи своё предсказание, используя таинственный и вдохновляющий стиль речи..
{input}"""
    return chat_prompt_template

# Example usage
prompt = generate_prompt_from_template(
    "Сделай мне предсказание на сегодня."
)

generated_text = generate_text(
    prompt,
    max_tokens=128,
    echo=True
)

#print("Generated text:\n")
print(generated_text)
