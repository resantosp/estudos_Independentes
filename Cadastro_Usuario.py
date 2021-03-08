#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações. 

nome = input('Nome de usuário: ')
senha = input('Senha: ')
while nome == senha:
    print('Senha inválida. Sua senha não pode ser igual ao nome de usuário. Tente novamente.')
    senha = input('Senha: ')
print('Usuário cadastrado com sucesso. Vá para a página inicial.')
