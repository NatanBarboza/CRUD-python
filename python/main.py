from conection import conect

def change_date(value):
    value = value.split('/')
    value = f'{value[2]}-{value[1]}-{value[0]}'
    return value

cursor = conect.cursor()

print("As funções que podem ser utilizadas são as seguintes:\n1-Read\n2-Create\n3-Update\n4-Delete")
function = int(input("Digite o tipo de função que deseja realizar:"))

if(function == 1):
    cursor.execute("SELECT * FROM tb_users;")
    linhas = cursor.fetchall()
    
    for i in linhas:
        print(i)
    
    cursor.close()

elif(function == 2):
    name_user = input("Digite o nome completo:")
    email_user = input("Digite o e-mail:")
    birth_date_user = input("Digite a data de nascimento (Ex.: dd/mm/aaaa):")
    active_user = bool(input("Usuário ativo(Obs.: 0 ou 1)? "))
    properties_user = int(input("Digite o nível de privilégio: "))
    exists = False

    birth_date_user = change_date(birth_date_user)

    cursor.execute("SELECT * FROM tb_users;")
    linhas = cursor.fetchall()
    
    for i in linhas:
        verification = i[1] == name_user
        if(verification == True):
            cursor.close()
            exists = True
            break
        else:
            continue
    
    if(exists == True):
        print("O nome já existe no banco. Por favor, rode novamente o código.")

    else:    
        cursor.execute(f"INSERT INTO tb_users (name_user, email_user, birth_date_user, active_user, properties_user) VALUES ('{name_user}', '{email_user}', '{birth_date_user}', {active_user}, {properties_user})")

        print(f"Os dados inseridos foram:\nNome: {name_user}\nE-mail: {email_user}\nData de Aniversário: {birth_date_user}\nEstado do Usuário: {active_user}\nNível de Privilégio: {properties_user}\n")

        conect.commit()

    cursor.close()

elif(function == 3):
    name_user_be_changed = input("Digite o nome do usuário que deseja modificar: ")
    print("Os campos são os seguintes:\n\n1-Nome\n2-E-mail\n3-Data de Aniversário\n4-Estado\n5-Privilégios")
    register_be_changed = int(input("Digite o campo que deseja modificar: "))
    if(register_be_changed == 4 or register_be_changed == 5):
        new_value = int(input("Digite o novo valor: "))

        if(register_be_changed == 4):
            cursor.execute(f"UPDATE tb_users SET active_user={new_value} WHERE name_user='{name_user_be_changed}';")

            conect.commit()

            cursor.close()
        
        else:
            cursor.execute(f"UPDATE tb_users SET properties_user={new_value} WHERE name_user='{name_user_be_changed}';")
            
            conect.commit()

            cursor.close()

    elif(register_be_changed == 1 or register_be_changed == 2 or register_be_changed == 3):
        new_value = input("Digite o novo valor: ")

        if(register_be_changed == 1):
            cursor.execute(f"UPDATE tb_users SET name_user='{new_value}' WHERE name_user='{name_user_be_changed}';")
            
            conect.commit()

            cursor.close()

        elif(register_be_changed == 2):
            cursor.execute(f"UPDATE tb_users SET email_user='{new_value}' WHERE name_user='{name_user_be_changed}';")
            
            conect.commit()

            cursor.close()
        
        else:
            new_value = change_date(new_value)
            cursor.execute(f"UPDATE tb_users SET birth_date_user='{new_value}' WHERE name_user='{name_user_be_changed}';")
                
            conect.commit()

            cursor.close()

elif(function == 4):
    name_user_be_excluded = input("Digite o nome do usuário que deseja excluir: ")

    cursor.execute(f"DELETE FROM tb_users WHERE name_user='{name_user_be_excluded}'")

    print(f"O registro excluído é o seguinte:\nNome: {name_user_be_excluded}")

    conect.commit()

    cursor.close()

cursor.close()
print("Conexão MySQL encerrada!")