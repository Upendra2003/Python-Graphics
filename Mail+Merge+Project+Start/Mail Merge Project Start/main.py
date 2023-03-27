PLACEHOLDER = "[name]"
with open(r"C:\Upendra\Python\Python_Graphics\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()

with open(r"C:\Upendra\Python\Python_Graphics\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
        with open(rf"C:\Upendra\Python\Python_Graphics\Mail+Merge+Project+Start\Mail Merge Project Start\Output\ReadyToSend\{stripped_name}.txt",mode='w') as file:
            file.write(new_letter)

    