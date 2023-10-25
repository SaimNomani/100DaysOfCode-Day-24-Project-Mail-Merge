with open("Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()
    for i in range(len(names)):
        if '\n' in names[i]:
            names[i]=names[i].rstrip(names[i][-1])
with open('Input/Letters/starting_letter.txt', mode='r') as sample_letter:
    file_content=sample_letter.read()
    for name in names:
        file_content=file_content.replace('[name]', name)
        with open(f'Output/ReadyToSend/send_to_{name}.txt', mode='w') as ready_to_send_letter:
            ready_to_send_letter.write(file_content)

