# login com lista 

lista = []
# menu iterativo (amoow)
while True:
    print('*** MENU DE LOGIN ***')
    print ('1 - Fazer login')
    print ('2 - Registra-se')
    print('3 - Usuarios Registrados')
    print('4 - Excluir usuarios registrados')
    print ('5 - Sair')
    opcao = input('Escolha uma opção (1-5): ')

        # Fazer login
    if opcao == '1':
        usuario = input('Digite seu nome de usuario: ')
        if usuario in lista:
            print(f'Bem-vindo, {usuario}!')
        else:
            print('Usuario não encontrado. Tente novamente.')
            # Registro
    elif opcao == '2':
        novo_usuario = input('Digite o nome de usuario que deseja registrar: ')
        if novo_usuario in lista:
            print('Este nome de usuario já está em uso. Tente outro.')
        else:
            lista.append(novo_usuario)
            print(f'Usuario "{novo_usuario}" registrado com sucesso!')
            # Usuarios existentes
    elif opcao == '3':
        if not lista:
            print('Nenhum usuario registrado.')
        else:
            print('Usuarios registrados:')
            for user in lista:
                print('- ' + user)
                # Excluir usuarios
    elif opcao == '4':
        usuario_excluir = input('Digite o nome do usuario que deseja excluir: ')
        if usuario_excluir in lista:
            lista.remove(usuario_excluir)
            print(f'Usuario "{usuario_excluir}" excluido com sucesso.')
        else:
            print('Usuario não encontrado. Não foi possível excluir.')
          # Leavinnnng  
    elif opcao == '5':
        print('Saindo do programa. Ate mais!')
        break
    # Caso coloque outra opcao
    else:
        print('Opção inválida. Por favor, escolha uma opção entre 1 e 5.')
print('Usuarios registrados:', lista)

