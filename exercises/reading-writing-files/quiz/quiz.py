import random

capitals = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas",
}

for quizNum in range(27):

    # Create the quiz and answer key files.
    quiz_file = open(
        f"exercises\\reading-writing-files\\quiz\\quizfiles\\capitals-quiz{quizNum + 1}.txt",
        "w",
    )
    answer_keys_file = open(
        f"exercises\\reading-writing-files\\quiz\\quizfiles\\answers-key-file{quizNum + 1}.txt",
        "w",
    )

    # Write out the header for the quiz.
    quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quiz_file.write(f"{(' ' * 20)} State Capitals Quiz (Form {quizNum + 1})\n\n")

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

# Loop through all states, making a question for each
    correct_answer = capitals[states[quizNum]]

    wrong_answers = list(capitals.values())    
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, k=3)

    answer_options = wrong_answers + [correct_answer]
    random.shuffle(answer_options)

    # Write the question and answer options to the quiz file.
    quiz_file.write(f"{quizNum}. What is the capital of {states[quizNum]}\n")

    for i in range(4):
        quiz_file.write(f"{'ABCD'[i]}) {answer_options[i]}")
        quiz_file.write("\n")

    # TODO: Write the answer key to a file.
    # answer_keys_file.write(f"{quizNum + 1}. {'ABCD'[answer_options.index(correct_answer)]})")

    answer_keys_file.write('%s. %s\n' % (quizNum + 1, 'ABCD'[answer_options.index(correct_answer)]))

    quiz_file.close()
    answer_keys_file.close()
