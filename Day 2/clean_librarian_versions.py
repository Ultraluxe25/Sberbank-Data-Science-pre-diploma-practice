def clean_librarian_versions(file_name: str) -> None:
    with open(file_name, 'r') as file_name:
        with open('requirements.txt', 'w') as result_file:
            modules_list = file_name.readlines()
            for index, module_name in enumerate(modules_list):
                if '==' not in module_name:
                    modules_list[index] = module_name[:module_name.index(' ')]
                else:
                    modules_list[index] = module_name[:-1]

            for module in modules_list:
                result_file.write(module + '\n')


file = 'modules.txt'
clean_librarian_versions(file)
